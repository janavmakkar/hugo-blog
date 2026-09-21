"""Telegram command and callback handlers.

Formatting is HTML parse mode throughout; anything coming from the workbook or
LeetCode is escaped before it reaches a message. Blocking work (SQLite, the
LeetCode API, git) runs in a worker thread so the bot stays responsive.
"""
from __future__ import annotations

import asyncio
import html
import sqlite3

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from . import config, db, gitops, publish, service, stats
from .util import esc, human_date, plural

PAGE_SIZE = 8
DIFFICULTY_MARK = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴", "Unknown": "⚪"}

HELP = """<b>DSA pattern bot</b>

<b>Daily loop</b>
/today — today's problems
/more [n] — hand me n more (default 1)
/open — everything assigned but unsolved
/done [id] — solved it: publish + push
/skip [id] — put one back in the pool

<b>Tracking</b>
/progress — totals, pace, finish date
/topics — per-topic breakdown
/solved [topic] — solved, with blog links
/unsolved [topic] — still to do
/find &lt;text&gt; — search the sheet

<b>Plumbing</b>
/republish [id] — re-render after editing a notebook
/push — retry a failed push
/status — bot and repo health"""


# --------------------------------------------------------------------- helpers


def _kb(rows: list[list[InlineKeyboardButton]]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(rows)


def _mark(difficulty: str | None) -> str:
    return DIFFICULTY_MARK.get(difficulty or "Unknown", "⚪")


def _problem_line(row: sqlite3.Row, show_link: bool = True) -> str:
    """`🟡 Two Sum — Arrays / Two Pointers` with LeetCode and blog links."""
    title = esc(row["title"])
    head = f"{_mark(row['difficulty'])} <b>{title}</b>"
    if show_link:
        head = f"{_mark(row['difficulty'])} <a href=\"{esc(row['url'])}\">{title}</a>"
    context = f"{esc(row['topic_name'])} / {esc(row['pattern_name'])}"
    return f"{head}\n   <i>{context}</i>  ·  <code>#{row['id']}</code>"


def _assignment_block(items: list[service.Assigned]) -> str:
    lines = []
    for item in items:
        row = item.row
        lines.append(_problem_line(row))
        lines.append(f"   📓 <code>{esc(item.notebook)}</code>")
        lines.append("")
    return "\n".join(lines).rstrip()


def _more_keyboard(open_ids: list[int]) -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton("+1", callback_data="more:1"),
            InlineKeyboardButton("+2", callback_data="more:2"),
            InlineKeyboardButton("+5", callback_data="more:5"),
        ]
    ]
    if open_ids:
        rows.append([InlineKeyboardButton("✅ Mark one solved", callback_data="pick:done")])
        rows.append([InlineKeyboardButton("⏭ Skip one", callback_data="pick:skip")])
    rows.append([InlineKeyboardButton("📊 Progress", callback_data="show:progress")])
    return _kb(rows)


async def _reply(update: Update, text: str, markup=None) -> None:
    target = update.effective_message
    kwargs = {
        "parse_mode": ParseMode.HTML,
        "disable_web_page_preview": True,
        "reply_markup": markup,
    }
    if update.callback_query is not None:
        await update.callback_query.message.reply_text(text, **kwargs)
    else:
        await target.reply_text(text, **kwargs)


def _arg_int(context: ContextTypes.DEFAULT_TYPE, index: int = 0) -> int | None:
    try:
        return int(context.args[index])
    except (IndexError, ValueError, TypeError):
        return None


def _resolve_topic(conn: sqlite3.Connection, term: str | None) -> sqlite3.Row | None:
    if not term:
        return None
    term = term.strip().lower()
    for row in db.topics(conn):
        if term in (row["slug"], row["name"].lower()) or term in row["slug"]:
            return row
    return None


# -------------------------------------------------------------------- commands


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    def work() -> str:
        with db.session() as conn:
            progress = stats.compute(conn)
        when = f"{config.DAILY_HOUR:02d}:{config.DAILY_MINUTE:02d}"
        return (
            f"Ready. {progress.total} problems across "
            f"{len(progress.by_topic)} topics from your sheet.\n"
            f"I'll ping you with {config.DAILY_COUNT} of them every day at "
            f"<b>{when} {config.TIMEZONE_NAME}</b>.\n\n{HELP}"
        )

    await _reply(update, await asyncio.to_thread(work))


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _reply(update, HELP)


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    def work() -> tuple[str, list[int]]:
        with db.session() as conn:
            rows = service.batch_for(conn)
            open_rows = db.open_problems(conn)
            if not rows:
                if open_rows:
                    body = (
                        "Nothing new assigned today, but these are still open:\n\n"
                        + "\n\n".join(_problem_line(r) for r in open_rows)
                    )
                else:
                    body = "Nothing assigned today yet. Use /more to pull some now."
                return body, [r["id"] for r in open_rows]

            header = f"<b>Today · {human_date(service.today())}</b>\n\n"
            body = "\n\n".join(
                _problem_line(r)
                + (f"\n   📓 <code>{esc(r['notebook_path'] or '')}</code>" if r["notebook_path"] else "")
                + ("\n   ✅ solved" if r["status"] == "solved" else "")
                for r in rows
            )
            leftovers = [r for r in open_rows if r["id"] not in {x["id"] for x in rows}]
            if leftovers:
                body += "\n\n<b>Still open from earlier</b>\n\n" + "\n\n".join(
                    _problem_line(r) for r in leftovers
                )
            return header + body, [r["id"] for r in open_rows]

    text, open_ids = await asyncio.to_thread(work)
    await _reply(update, text, _more_keyboard(open_ids))


async def more(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    count = _arg_int(context) or 1
    await _assign_and_reply(update, max(1, min(count, 10)))


async def _assign_and_reply(update: Update, count: int) -> None:
    def work() -> tuple[str, list[int]]:
        with db.session() as conn:
            items = service.assign(conn, count, source="more")
            open_ids = [r["id"] for r in db.open_problems(conn)]
        if not items:
            return "Nothing left unsolved in the sheet. 🎉", open_ids
        head = f"<b>{len(items)} more {plural(len(items), 'problem')}</b>\n\n"
        return head + _assignment_block(items), open_ids

    text, open_ids = await asyncio.to_thread(work)
    await _reply(update, text, _more_keyboard(open_ids))


async def open_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    def work() -> tuple[str, list[int]]:
        with db.session() as conn:
            rows = db.open_problems(conn)
        if not rows:
            return "No open problems. Use /more when you want one.", []
        body = "\n\n".join(
            _problem_line(r) + f"\n   assigned {human_date(r['assigned_on'])}" for r in rows
        )
        return f"<b>Open ({len(rows)})</b>\n\n{body}", [r["id"] for r in rows]

    text, open_ids = await asyncio.to_thread(work)
    await _reply(update, text, _more_keyboard(open_ids))


async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    problem_id = _arg_int(context)
    if problem_id is None:
        await _picker(update, "done", "Which one did you solve?")
        return
    await _do_solve(update, problem_id)


async def _do_solve(update: Update, problem_id: int) -> None:
    await _reply(update, "Publishing… ⏳")

    def work() -> str:
        with db.session() as conn:
            result = service.solve(conn, problem_id)
        lines = [
            f"✅ <b>{esc(result.title)}</b> published.",
            "",
            f"🔗 <a href=\"{esc(result.post_url)}\">{esc(result.post_url)}</a>",
            f"📄 <code>{esc(result.post_path)}</code>",
        ]
        if result.mirrored:
            also = ", ".join(esc(m) for m in result.mirrored)
            lines.append(f"↔️ Also cleared the same problem under: {also}")
        lines.append("")
        lines.append(("🚀 " if result.git.pushed else "⚠️ ") + esc(result.git.message))
        if result.git.pushed:
            lines.append("<i>GitHub Pages usually takes a minute to rebuild.</i>")
        return "\n".join(lines)

    try:
        text = await asyncio.to_thread(work)
    except Exception as exc:  # surfaced to the user rather than lost in the log
        text = f"❌ Could not publish: <code>{esc(str(exc))}</code>"
    await _reply(update, text)


async def republish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    problem_id = _arg_int(context)
    if problem_id is None:
        await _picker(update, "pub", "Which write-up should I re-render?", solved=True)
        return
    await _do_republish(update, problem_id)


async def _do_republish(update: Update, problem_id: int) -> None:
    await _reply(update, "Re-rendering… ⏳")

    def work() -> str:
        with db.session() as conn:
            result = service.republish(conn, problem_id)
        return (
            f"♻️ <b>{esc(result.title)}</b> updated.\n"
            f"🔗 <a href=\"{esc(result.post_url)}\">{esc(result.post_url)}</a>\n\n"
            + ("🚀 " if result.git.pushed else "⚠️ ")
            + esc(result.git.message)
        )

    try:
        text = await asyncio.to_thread(work)
    except Exception as exc:
        text = f"❌ Could not re-render: <code>{esc(str(exc))}</code>"
    await _reply(update, text)


async def skip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    problem_id = _arg_int(context)
    if problem_id is None:
        await _picker(update, "skip", "Which one should go back in the pool?")
        return
    await _do_skip(update, problem_id)


async def _do_skip(update: Update, problem_id: int) -> None:
    def work() -> str:
        with db.session() as conn:
            row = service.skip(conn, problem_id)
        if row is None:
            return "No such problem."
        return (
            f"⏭ <b>{esc(row['title'])}</b> is back in the pool.\n"
            f"<i>The notebook is still on disk if you want it.</i>"
        )

    await _reply(update, await asyncio.to_thread(work))


async def _picker(update: Update, action: str, prompt: str, solved: bool = False) -> None:
    def work() -> list[sqlite3.Row]:
        with db.session() as conn:
            if solved:
                return db.list_by_status(conn, "solved", limit=12)
            return db.open_problems(conn)

    rows = await asyncio.to_thread(work)
    if not rows:
        await _reply(update, "Nothing to choose from right now.")
        return
    buttons = [
        [
            InlineKeyboardButton(
                f"{_mark(r['difficulty'])} {r['title'][:38]}",
                callback_data=f"{action}:{r['id']}",
            )
        ]
        for r in rows[:12]
    ]
    await _reply(update, prompt, _kb(buttons))


async def progress(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _reply(update, await asyncio.to_thread(_progress_text))


def _progress_text() -> str:
    with db.session() as conn:
        p = stats.compute(conn)
        days = stats.recent_days(conn, limit=7)

    lines = [
        "<b>📊 Progress</b>",
        "",
        f"<code>{stats.bar(p.solved / p.total if p.total else 0)}</code> "
        f"<b>{p.solved}/{p.total}</b> ({p.percent:.1f}%)",
        f"{p.remaining} left · {p.assigned} in progress · {p.published} published",
        "",
    ]

    if p.by_difficulty:
        lines.append("<b>By difficulty</b>")
        for d in p.by_difficulty:
            mark = DIFFICULTY_MARK.get(d["difficulty"], "⚪")
            lines.append(f"{mark} {d['difficulty']:<8} {d['solved']:>3}/{d['total']:<3}")
        lines.append("")

    lines.append("<b>By topic</b>")
    for t in p.by_topic:
        frac = t["solved"] / t["total"] if t["total"] else 0
        lines.append(
            f"<code>{stats.bar(frac, 8)}</code> {t['solved']:>2}/{t['total']:<3} "
            f"{esc(t['name'])}"
        )
    lines.append("")

    if p.first_solve:
        lines += [
            "<b>Pace</b>",
            f"Started {human_date(p.first_solve)} · {p.calendar_days} "
            f"{plural(p.calendar_days, 'day')} in · {p.active_days} active "
            f"{plural(p.active_days, 'day')}",
            f"{p.per_calendar_day:.2f} / day overall · "
            f"{p.per_active_day:.2f} on days you solve",
        ]
        if p.eta and p.remaining:
            lines.append(
                f"🏁 At this pace the sheet is done <b>{human_date(p.eta)}</b> "
                f"({p.days_left} {plural(p.days_left or 0, 'day')} away)"
            )
        elif not p.remaining:
            lines.append("🏁 Sheet complete. 🎉")
    else:
        lines.append("<i>No solves yet — the forecast starts with the first one.</i>")

    if days:
        lines.append("")
        lines.append("<b>Recent</b>")
        lines += [f"{human_date(d['day'])} — {d['n']}" for d in days]
    return "\n".join(lines)


async def topics(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    def work() -> tuple[str, InlineKeyboardMarkup]:
        with db.session() as conn:
            p = stats.compute(conn)
        lines = ["<b>Topics</b>", ""]
        for t in p.by_topic:
            frac = t["solved"] / t["total"] if t["total"] else 0
            lines.append(
                f"<code>{stats.bar(frac, 10)}</code> {t['solved']:>2}/{t['total']:<3} "
                f"{esc(t['name'])}"
            )
        buttons = [
            [InlineKeyboardButton(t["name"], callback_data=f"page:unsolved:{t['slug']}:0")]
            for t in p.by_topic
        ]
        return "\n".join(lines), _kb(buttons)

    text, markup = await asyncio.to_thread(work)
    await _reply(update, text, markup)


async def solved(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _send_list(update, "solved", " ".join(context.args or "") or None, 0)


async def unsolved(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _send_list(update, "unsolved", " ".join(context.args or "") or None, 0)


def _list_text(kind: str, topic_term: str | None, offset: int) -> tuple[str, InlineKeyboardMarkup | None]:
    statuses = ("solved",) if kind == "solved" else ("pending", "assigned")
    with db.session() as conn:
        topic = _resolve_topic(conn, topic_term)
        slug = topic["slug"] if topic else None
        total = db.count_by_status(conn, statuses, topic_slug=slug)
        rows = db.list_by_status(conn, statuses, topic_slug=slug, limit=PAGE_SIZE, offset=offset)
        patterns = {r["pattern_id"]: db.pattern(conn, r["pattern_id"]) for r in rows}

    scope = f" · {esc(topic['name'])}" if topic else ""
    if not total:
        return (f"Nothing {kind}{scope} yet.", None)

    title = "✅ Solved" if kind == "solved" else "📝 Still to do"
    head = f"<b>{title}{scope}</b> — {total}\n"
    if total > PAGE_SIZE:
        head += f"<i>showing {offset + 1}–{min(offset + PAGE_SIZE, total)}</i>\n"

    blocks = []
    for r in rows:
        block = _problem_line(r)
        if kind == "solved":
            if r["post_path"]:
                url = publish.post_url(patterns[r["pattern_id"]], r["post_anchor"])
                block += f"\n   ✍️ <a href=\"{esc(url)}\">write-up</a>"
            if r["solved_on"]:
                block += f"  ·  {human_date(r['solved_on'])}"
            if r["mirrored_from"]:
                block += "  ·  <i>via duplicate</i>"
        elif r["status"] == "assigned":
            block += "\n   ⏳ assigned"
        blocks.append(block)

    nav: list[InlineKeyboardButton] = []
    token = topic["slug"] if topic else "-"
    if offset:
        nav.append(
            InlineKeyboardButton(
                "◀ Prev", callback_data=f"page:{kind}:{token}:{max(0, offset - PAGE_SIZE)}"
            )
        )
    if offset + PAGE_SIZE < total:
        nav.append(
            InlineKeyboardButton(
                "Next ▶", callback_data=f"page:{kind}:{token}:{offset + PAGE_SIZE}"
            )
        )
    return head + "\n" + "\n\n".join(blocks), (_kb([nav]) if nav else None)


async def _send_list(update: Update, kind: str, topic_term: str | None, offset: int) -> None:
    text, markup = await asyncio.to_thread(_list_text, kind, topic_term, offset)
    await _reply(update, text, markup)


async def find(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    term = " ".join(context.args or "").strip()
    if not term:
        await _reply(update, "Usage: <code>/find two sum</code>")
        return

    def work() -> str:
        with db.session() as conn:
            rows = db.find_problems(conn, term)
        if not rows:
            return f"No match for <b>{esc(term)}</b>."
        body = "\n\n".join(
            _problem_line(r) + (f"\n   ✅ solved {human_date(r['solved_on'])}" if r["solved_on"] else "")
            for r in rows
        )
        return f"<b>{len(rows)} {plural(len(rows), 'match', 'matches')}</b>\n\n{body}"

    await _reply(update, await asyncio.to_thread(work))


async def push(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    def work() -> str:
        result = gitops.push_only()
        return ("🚀 " if result.ok else "⚠️ ") + esc(result.message)

    await _reply(update, await asyncio.to_thread(work))


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    def work() -> str:
        with db.session() as conn:
            p = stats.compute(conn)
            unknown = conn.execute(
                "SELECT COUNT(*) AS n FROM problems WHERE difficulty = 'Unknown'"
            ).fetchone()["n"]
        return "\n".join(
            [
                "<b>Status</b>",
                "",
                f"DB: <code>{esc(str(config.DB_PATH))}</code>",
                f"Problems: {p.total} ({unknown} without a difficulty)",
                f"Solved: {p.solved} · open: {p.assigned}",
                f"Branch: <code>{esc(gitops.current_branch())}</code> · "
                f"unpushed commits: {gitops.unpushed_count()}",
                f"Remote: <code>{esc(gitops.remote_url())}</code>",
                f"Auto-push: {'on' if config.AUTO_PUSH else 'off'}",
                f"Daily: {config.DAILY_COUNT} at {config.DAILY_HOUR:02d}:"
                f"{config.DAILY_MINUTE:02d} {config.TIMEZONE_NAME}",
            ]
        )

    await _reply(update, await asyncio.to_thread(work))


# ------------------------------------------------------------------- callbacks


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query.message is None or query.message.chat_id != config.OWNER_CHAT_ID:
        await query.answer("Not your bot.", show_alert=True)
        return
    await query.answer()
    data = query.data or ""
    action, _, rest = data.partition(":")

    if action == "more":
        await _assign_and_reply(update, int(rest or 1))
    elif action == "done":
        await _do_solve(update, int(rest))
    elif action == "skip":
        await _do_skip(update, int(rest))
    elif action == "pub":
        await _do_republish(update, int(rest))
    elif action == "pick":
        prompts = {
            "done": ("done", "Which one did you solve?", False),
            "skip": ("skip", "Which one should go back in the pool?", False),
            "pub": ("pub", "Which write-up should I re-render?", True),
        }
        act, prompt, is_solved = prompts.get(rest, ("done", "Pick one:", False))
        await _picker(update, act, prompt, solved=is_solved)
    elif action == "show" and rest == "progress":
        await _reply(update, await asyncio.to_thread(_progress_text))
    elif action == "page":
        kind, token, offset = rest.split(":")
        await _send_list(update, kind, None if token == "-" else token, int(offset))


# ------------------------------------------------------------------ daily job


async def daily_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Assign the day's problems and send the morning prompt."""

    def work() -> tuple[str, list[int]]:
        with db.session() as conn:
            items = service.assign(conn, config.DAILY_COUNT, source="daily")
            open_rows = db.open_problems(conn)
            p = stats.compute(conn)
        if not items:
            return "🎉 Every problem in the sheet is solved. Nothing left to assign.", []

        header = (
            f"<b>☀️ {human_date(service.today())}</b>\n"
            f"{len(items)} {plural(len(items), 'problem')} for today — "
            f"{p.solved}/{p.total} done so far.\n\n"
        )
        body = _assignment_block(items)
        leftover = [r for r in open_rows if r["id"] not in {i.row["id"] for i in items}]
        if leftover:
            body += (
                f"\n\n<i>{len(leftover)} still open from earlier — /open to see "
                f"{plural(len(leftover), 'it', 'them')}.</i>"
            )
        return header + body, [r["id"] for r in open_rows]

    text, open_ids = await asyncio.to_thread(work)
    await context.bot.send_message(
        chat_id=config.OWNER_CHAT_ID,
        text=text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=_more_keyboard(open_ids),
    )


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    import logging

    logging.getLogger("dsa-bot").exception("Handler failed", exc_info=context.error)
    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text(
            f"❌ Something went wrong: <code>{html.escape(str(context.error))}</code>",
            parse_mode=ParseMode.HTML,
        )
