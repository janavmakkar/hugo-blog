# DSA pattern bot

Daily Telegram prompts to solve problems from `DSA_Patterns.xlsx`, a notebook
created for each one, and a one-command path from a solved notebook to a
published post on <https://janav.in>.

## The loop

```
04:00 IST   bot picks 2 unsolved problems, one per pattern
            -> creates leetcode/solutions/<nn>-<topic>/<pattern>/<problem>.ipynb
            -> messages you the problems, links and notebook paths

you         solve it in Jupyter, submit on LeetCode, run the cells

/done       marks it solved
            -> renders the notebook into content/leetcode/<topic>-<pattern>.md
            -> commits notebook + post + any figures, pushes
            -> GitHub Actions rebuilds the site, bot replies with the live URL
```

One post per **(topic, pattern)** pair. The first solve in a pattern creates the
post from the sheet's own scenario and clue; every later solve appends a section
to the same file, so `Arrays · Two Pointers` grows into a real article instead of
scattering into a dozen stubs.

## Setup

```bash
cd ~/hugo-blog/leetcode
./setup.sh
```

It creates the virtualenv, installs dependencies, seeds the database, generates a
GitHub deploy key and installs the systemd user service. Re-run it any time; it
skips whatever is already done. Two steps need you:

1. **Bot token** — talk to [@BotFather](https://t.me/BotFather), `/newbot`, put
   the token in `leetcode/.env` as `TELEGRAM_BOT_TOKEN`.
2. **Chat id** — run `.venv/bin/python -m bot.whoami` **from `leetcode/`**, then
   message your bot. It waits indefinitely and writes `TELEGRAM_CHAT_ID` into
   `.env` itself. The bot answers this chat and ignores every other one, which
   matters because it can push to your repo.

   If it prints a 409, something else is already polling the bot — usually the
   service: `systemctl --user stop dsa-bot`, capture the id, start it again.

`setup.sh` also prints a public key to paste into
**GitHub → repo → Settings → Deploy keys → Add**, with *Allow write access*
ticked. Until that is done, commits still happen locally and `/push` retries.

Then:

```bash
systemctl --user enable --now dsa-bot
journalctl --user -u dsa-bot -f
```

> Day-to-day commands, DB queries and a troubleshooting table live in
> **[COMMANDS.md](COMMANDS.md)**.

## Telegram commands

| Command | What it does |
| --- | --- |
| `/today` | Today's problems, with notebook paths |
| `/more [n]` | Hand out `n` more (default 1, max 10) |
| `/open` | Everything assigned but not yet solved |
| `/done [id]` | Solved it: publish, commit, push |
| `/skip [id]` | Put one back in the pool |
| `/progress` | Totals, per-topic, per-difficulty, pace, finish date |
| `/topics` | Per-topic bars, tap one to drill in |
| `/solved [topic]` | Solved problems with links to their write-ups |
| `/unsolved [topic]` | What is left |
| `/find <text>` | Search the sheet |
| `/republish [id]` | Re-render after editing a notebook |
| `/push` | Retry a failed push |
| `/status` | DB, branch, unpushed commits, schedule |

Calling `/done` and friends without an id gives you a tap-to-pick list.

## Same thing without Telegram

```bash
.venv/bin/python -m bot.cli assign 2
.venv/bin/python -m bot.cli open
.venv/bin/python -m bot.cli done 41          # publish + push
.venv/bin/python -m bot.cli republish 41 --no-push
.venv/bin/python -m bot.cli progress
```

## Writing a notebook so it publishes well

Cells are tagged, and the tags decide what reaches the blog:

| Tag | Published? | Purpose |
| --- | --- | --- |
| `meta` | no | Problem header; the post builds its own |
| `statement` | no | LeetCode's text, kept local rather than republished |
| `cue` | no | Scenario/clue — the post shows these once in its intro |
| `approach` | **yes** | Your reasoning. This is the body of the section |
| `solution` | **yes** | Code plus its output |
| `tests` | **yes** | Driver cell; output becomes a result block |
| `complexity` | **yes** | Time and space |

Add `no-publish` to any cell's tags to keep it out of the post. In JupyterLab:
the property inspector (⚙ in the right sidebar) → *Cell metadata* → `tags`.

Headings inside a cell are demoted one level, since the problem itself is an
`h2`. Figures are written to `static/posts/leetcode/` and committed. Output is
rendered from `text/plain` rather than `text/html`, because the site does not
enable goldmark's `unsafe` renderer — a DataFrame publishes as a monospace block,
not an HTML table.

## Editing a published post

Everything above the `<!-- solutions -->` marker — front matter and the pattern
intro — is yours. The publisher never rewrites it after the file exists. Below
the marker each problem owns a block delimited by
`<!-- problem:<slug> start -->` / `<!-- problem:<slug> end -->`, and republishing
one problem replaces only its own block.

## Notes

* The same LeetCode problem appears under more than one pattern in the sheet (30
  of them). Solving it once clears every entry and points them at the same
  write-up, so the completion forecast stays honest. Set `MIRROR_DUPLICATES=0` in
  `.env` if you would rather solve each one separately.
* 19 rows have no difficulty: their sheet URLs are not real LeetCode slugs
  (`01-knapsack`, `factorial`, `friend-circles`, `implement-strstr`,
  `allocate-minimum-number-of-pages`, …). Fix the URL in the workbook and re-run
  `.venv/bin/python -m bot.seed` to pick them up.
* `dsa.db`, `.env` and `.venv/` are gitignored. Notebooks and posts are committed.
