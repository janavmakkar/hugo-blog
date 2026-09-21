"""Turn solved notebooks into Hugo posts, one post per (topic, pattern).

The post is not regenerated wholesale. Everything above the solutions marker -
front matter and the pattern intro - is yours to edit and is preserved once the
file exists. Below the marker each problem owns a fenced block delimited by
`<!-- problem:<slug> start/end -->`, so republishing one problem rewrites only
its own block and leaves the rest of the page alone.
"""
from __future__ import annotations

import base64
import json
import re
import sqlite3
from pathlib import Path

from . import config, db
from .util import human_date

_HEADING_RE = re.compile(r"^(#{1,6})(\s+)", re.M)
_FENCE_RE = re.compile(r"^(?:```|~~~)", re.M)
_ANSI_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")


def _cell_tags(cell: dict) -> set[str]:
    return {str(t) for t in (cell.get("metadata") or {}).get("tags") or []}


def _source(cell: dict) -> str:
    src = cell.get("source") or ""
    return "".join(src) if isinstance(src, list) else src


def _demote_headings(markdown: str, levels: int = 1) -> str:
    """Push notebook headings below the problem's own `##` heading.

    Headings inside fenced code blocks are left alone, since `#` there is a comment.
    """
    out: list[str] = []
    in_fence = False
    for line in markdown.splitlines():
        if _FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence:
            line = _HEADING_RE.sub(
                lambda m: "#" * min(6, len(m.group(1)) + levels) + m.group(2), line
            )
        out.append(line)
    return "\n".join(out)


def _fence(body: str, lang: str = "") -> str:
    """Fence `body`, widening the fence if the body itself contains backticks."""
    body = body.rstrip("\n")
    ticks = "```"
    while ticks in body:
        ticks += "`"
    return f"{ticks}{lang}\n{body}\n{ticks}"


def _clean_text(text: str) -> str:
    return _ANSI_RE.sub("", text).rstrip("\n")


def _stringify(value) -> str:
    return "".join(value) if isinstance(value, list) else str(value)


def _render_outputs(cell: dict, image_prefix: str, image_dir: Path) -> tuple[list[str], int]:
    """Render a code cell's outputs. Images are written to Hugo's static tree.

    text/plain is preferred over text/html because the site does not enable
    goldmark's `unsafe` renderer, so raw HTML tables would be dropped silently.
    """
    chunks: list[str] = []
    images = 0
    streams: list[str] = []

    for output in cell.get("outputs") or []:
        kind = output.get("output_type")

        if kind == "stream":
            streams.append(_stringify(output.get("text", "")))
            continue

        if kind == "error":
            trace = _clean_text("\n".join(output.get("traceback") or []))
            if trace:
                chunks.append(_fence(trace, "text"))
            continue

        data = output.get("data") or {}
        if "image/png" in data:
            images += 1
            payload = data["image/png"]
            raw = base64.b64decode(
                payload if isinstance(payload, str) else "".join(payload)
            )
            image_dir.mkdir(parents=True, exist_ok=True)
            name = f"{image_prefix}-{images}.png"
            (image_dir / name).write_bytes(raw)
            chunks.append(f"![output]({config.STATIC_IMG_URL}/{name})")
            continue
        if "text/plain" in data:
            text = _clean_text(_stringify(data["text/plain"]))
            if text:
                chunks.append(_fence(text, "text"))

    stream_text = _clean_text("".join(streams))
    if stream_text:
        chunks.insert(0, _fence(stream_text, "text"))
    return chunks, images


def notebook_to_section(
    notebook: dict, row: sqlite3.Row, image_prefix: str, image_dir: Path
) -> str:
    """Render one solved notebook as the `## <problem>` section of a pattern post."""
    difficulty = row["difficulty"] or "Unknown"
    meta_bits = [f"**{difficulty}**"]
    label = f"LeetCode {row['lc_id']}" if row["lc_id"] else "LeetCode"
    meta_bits.append(f"[{label}]({row['url']})")
    if row["solved_on"]:
        meta_bits.append(f"solved {human_date(row['solved_on'])}")

    parts = [
        f"## {row['title']} {{#{row['lc_slug']}}}",
        "",
        " · ".join(meta_bits),
        "",
    ]

    for cell in notebook.get("cells") or []:
        tags = _cell_tags(cell)
        if "no-publish" in tags or "meta" in tags:
            continue
        source = _source(cell).strip("\n")
        if not source and cell.get("cell_type") == "markdown":
            continue

        if cell["cell_type"] == "markdown":
            parts.append(_demote_headings(source).strip("\n"))
            parts.append("")
            continue

        if cell["cell_type"] != "code":
            continue

        if source and not source.strip().startswith("#!"):
            parts.append(_fence(source, "python"))
            parts.append("")
        rendered, _ = _render_outputs(cell, image_prefix, image_dir)
        if rendered:
            parts.append("**Output**")
            parts.append("")
            parts.append("\n\n".join(rendered))
            parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def _front_matter(pattern: sqlite3.Row) -> str:
    topic, name = pattern["topic_name"], pattern["name"]
    tags = json.dumps(["DSA", "python", "LeetCode", topic, name])
    return (
        "---\n"
        f'title: "{topic} · {name} | #DSA-Patterns"\n'
        f"keywords: {tags}\n"
        "categories: [DSA]\n"
        "draft: false\n"
        "defaultTheme: auto\n"
        f"tags: {tags}\n"
        "showToc: true\n"
        "comments: true\n"
        "cover:\n"
        f"  image: {config.POST_COVER}\n"
        "  alt: dsa-patterns\n"
        "---\n"
    )


def _intro(pattern: sqlite3.Row) -> str:
    lines = [
        f"Problems from my DSA pattern sheet under **{pattern['topic_name']} → "
        f"{pattern['name']}**, solved one at a time and written up as I go.",
        "",
    ]
    if pattern["scenario"] or pattern["clue"]:
        lines.append("## When to reach for this pattern")
        lines.append("")
        if pattern["scenario"]:
            lines.append(pattern["scenario"].strip())
            lines.append("")
        if pattern["clue"]:
            lines.append(f"**Clue in the wording** — {pattern['clue'].strip()}")
            lines.append("")
    return "\n".join(lines)


def _skeleton(pattern: sqlite3.Row) -> str:
    return _front_matter(pattern) + "\n" + _intro(pattern) + "\n" + config.SOLUTIONS_MARKER + "\n"


def _splice(document: str, slug: str, section: str) -> str:
    """Insert or replace one problem block, keeping every other block untouched."""
    start, end = f"<!-- problem:{slug} start -->", f"<!-- problem:{slug} end -->"
    block = f"{start}\n\n{section}\n{end}\n"

    pattern = re.compile(
        re.escape(start) + r".*?" + re.escape(end) + r"\n?", re.S
    )
    if pattern.search(document):
        return pattern.sub(lambda _m: block, document, count=1)

    if config.SOLUTIONS_MARKER not in document:
        document = document.rstrip() + "\n\n" + config.SOLUTIONS_MARKER + "\n"
    return document.rstrip() + "\n\n" + block


def publish_problem(conn: sqlite3.Connection, problem_id: int) -> dict:
    """Render a solved problem into its pattern post.

    Returns {post_path, post_url, anchor, images}. Raises if the notebook is missing.
    """
    row = db.problem(conn, problem_id)
    if row is None:
        raise ValueError(f"No problem with id {problem_id}")
    if not row["notebook_path"]:
        raise ValueError(f"{row['title']} has no notebook yet - run /notebook first")

    nb_path = config.REPO_ROOT / row["notebook_path"]
    if not nb_path.is_file():
        raise FileNotFoundError(f"Notebook missing on disk: {row['notebook_path']}")
    notebook = json.loads(nb_path.read_text(encoding="utf-8"))

    pattern = db.pattern(conn, row["pattern_id"])
    post_path = config.REPO_ROOT / pattern["post_path"]
    post_path.parent.mkdir(parents=True, exist_ok=True)

    document = post_path.read_text(encoding="utf-8") if post_path.exists() else _skeleton(pattern)
    image_prefix = f"{pattern['topic_slug']}-{pattern['slug']}-{row['lc_slug']}"
    section = notebook_to_section(notebook, row, image_prefix, config.STATIC_IMG_DIR)
    post_path.write_text(_splice(document, row["lc_slug"], section), encoding="utf-8")

    anchor = row["lc_slug"]
    db.set_published(conn, problem_id, pattern["post_path"], anchor)
    return {
        "post_path": pattern["post_path"],
        "post_url": post_url(pattern, anchor),
        "anchor": anchor,
        "title": row["title"],
    }


def post_url(pattern: sqlite3.Row, anchor: str | None = None) -> str:
    slug = Path(pattern["post_path"]).stem
    url = f"{config.SITE_BASE_URL}/leetcode/{slug}/"
    return f"{url}#{anchor}" if anchor else url


def republish_pattern(conn: sqlite3.Connection, pattern_id: int) -> list[dict]:
    """Re-render every solved problem in a pattern (after editing notebooks in bulk)."""
    return [
        publish_problem(conn, row["id"])
        for row in db.pattern_solutions(conn, pattern_id)
    ]
