# Command reference

Self-reference for the DSA pattern bot. Every command here was run against this
setup, not written from memory.

All CLI commands assume you are in `~/hugo-blog/leetcode` — the `bot` package
lives there, so `python -m bot.*` fails anywhere else.

```bash
cd ~/hugo-blog/leetcode
```

`.venv/bin/python` is used explicitly throughout so nothing depends on having the
virtualenv activated.

---

## 1. Quick card

| I want to… | Command |
| --- | --- |
| Get a problem now | Telegram `/more 1` |
| Publish what I solved | Telegram `/done` |
| See where I am | Telegram `/progress` |
| Do it without Telegram | `.venv/bin/python -m bot.cli assign 1` |
| Restart the bot | `systemctl --user restart dsa-bot` |
| Watch the log | `journalctl --user -u dsa-bot -f` |
| Run a query | `.venv/bin/python -m bot.sql "SELECT …"` |
| Re-read the spreadsheet | `.venv/bin/python -m bot.seed` |

---

## 2. Telegram

| Command | Does |
| --- | --- |
| `/start`, `/help` | Command list |
| `/today` | Today's problems with notebook paths |
| `/more [n]` | Hand out `n` more (default 1, capped at 10) |
| `/open` | Assigned but not yet solved |
| `/done [id]` | Solved it → publish, commit, push |
| `/skip [id]` | Back in the pool; notebook stays on disk |
| `/progress` | Totals, per-topic, per-difficulty, pace, finish date |
| `/topics` | Per-topic bars; tap one to drill in |
| `/solved [topic]` | Solved, with links to each write-up |
| `/unsolved [topic]` | What's left |
| `/find <text>` | Search the sheet |
| `/republish [id]` | Re-render after editing a notebook |
| `/push` | Retry a failed push |
| `/status` | DB, branch, unpushed commits, schedule |

Omit the id on `/done`, `/skip` and `/republish` to get a tap-to-pick list.
`[topic]` accepts a slug or a name: `/unsolved graphs`, `/solved linked list` (no quotes).

The bot replies only to chat id `1175324426`. Everything else is ignored.

---

## 3. CLI (same workflow, no phone)

```bash
.venv/bin/python -m bot.cli assign 2                 # pick 2, create notebooks
.venv/bin/python -m bot.cli assign 3 --topic graphs  # restricted to one topic
.venv/bin/python -m bot.cli open                     # what's in flight
.venv/bin/python -m bot.cli today                    # today's batch
.venv/bin/python -m bot.cli progress                 # stats + finish date
.venv/bin/python -m bot.cli find two sum             # search
.venv/bin/python -m bot.cli done 41                  # publish + commit + push
.venv/bin/python -m bot.cli done 41 --no-push        # publish + commit only
.venv/bin/python -m bot.cli republish 41             # re-render after edits
.venv/bin/python -m bot.cli skip 41                  # back in the pool
.venv/bin/python -m bot.cli push                     # retry a push
```

The id in `done`/`skip`/`republish` is the `#41` shown by `open`, `today` and the
Telegram messages.

---

## 4. Service

```bash
systemctl --user status dsa-bot            # is it alive
systemctl --user restart dsa-bot           # after editing .env or bot code
systemctl --user stop dsa-bot              # free the Telegram poll slot
systemctl --user start dsa-bot
systemctl --user disable --now dsa-bot     # stop and don't start at boot
systemctl --user enable --now dsa-bot      # back on

journalctl --user -u dsa-bot -f            # follow
journalctl --user -u dsa-bot -n 100        # last 100 lines
journalctl --user -u dsa-bot --since today
```

**Editing `.env` or anything in `bot/` needs a restart** — the service reads both
only at startup.

Run it in the foreground to see a traceback directly:

```bash
systemctl --user stop dsa-bot
.venv/bin/python -m bot.app
```

The unit survives logout and reboot because lingering is on
(`loginctl show-user $USER | grep Linger`).

---

## 5. Setup and re-setup

```bash
./setup.sh                                   # idempotent; skips finished steps
.venv/bin/python -m bot.whoami               # capture chat id into .env
.venv/bin/python -m bot.whoami --no-write    # just print it
.venv/bin/pip install -r requirements.txt    # re-install deps
.venv/bin/pip install -r requirements-lab.txt   # JupyterLab on the VPS
.venv/bin/jupyter lab --no-browser --port 8888
```

Rebuild the virtualenv from scratch (Ubuntu here has no `python3-venv`, so pip is
bootstrapped rather than installed with sudo):

```bash
rm -rf .venv
python3 -m venv --without-pip .venv
curl -sS https://bootstrap.pypa.io/get-pip.py | .venv/bin/python
.venv/bin/pip install -r requirements.txt
```

### Settings worth knowing (`leetcode/.env`, chmod 600)

| Key | Default | Effect |
| --- | --- | --- |
| `DAILY_HOUR` / `DAILY_MINUTE` | `4` / `0` | When the prompt fires |
| `DAILY_COUNT` | `2` | Problems per day |
| `TIMEZONE` | `Asia/Kolkata` | Bot's own clock; the VPS is on `+01` |
| `AUTO_PUSH` | `1` | `0` = commit locally, never push |
| `MIRROR_DUPLICATES` | `1` | Solving once clears the problem's other patterns |
| `SITE_BASE_URL` | `https://janav.in` | Used to build the links it sends you |
| `POST_COVER` | `posts/otter_basic_dsa.jpg` | Cover image on generated posts |

---

## 6. Database

`leetcode/dsa.db` — SQLite, gitignored. There is no `sqlite3` binary on this box,
so use the bundled runner:

```bash
.venv/bin/python -m bot.sql "SELECT …"              # table output
.venv/bin/python -m bot.sql --csv "SELECT …"        # CSV to stdout
.venv/bin/python -m bot.sql --readonly "SELECT …"   # can't write, for safety
echo "SELECT COUNT(*) FROM problems" | .venv/bin/python -m bot.sql
```

### Shape

```
topics (10) ──< patterns (56) ──< problems (271)
                                      ^
                              assignments (one row per hand-out)
```

`problems` is one row per **(pattern, problem)** pair, so the 271 rows cover 240
distinct LeetCode problems — 30 of them appear under more than one pattern
(one under three).

Columns that matter on `problems`:

| Column | Meaning |
| --- | --- |
| `status` | `pending` → `assigned` → `solved` |
| `difficulty` | `Easy` / `Medium` / `Hard` / `Unknown` |
| `lc_slug` | LeetCode title-slug; the join key for duplicates |
| `paid_only` | `1` = LeetCode Premium (24 of them) |
| `notebook_path` | Set when the notebook is created |
| `post_path`, `post_anchor` | Set when published; the anchor is the `lc_slug` |
| `mirrored_from` | Non-null = cleared because a duplicate was solved |
| `assigned_on`, `solved_on`, `published_at` | ISO dates |

### Inspection

```bash
# Overall
.venv/bin/python -m bot.sql "
SELECT COUNT(*) AS total, SUM(status='solved') AS solved,
       SUM(status='assigned') AS open FROM problems"

# Progress per pattern
.venv/bin/python -m bot.sql "
SELECT t.name AS topic, pa.name AS pattern, COUNT(*) AS total,
       SUM(p.status='solved') AS solved
FROM problems p
JOIN patterns pa ON pa.id = p.pattern_id
JOIN topics   t  ON t.id  = pa.topic_id
GROUP BY pa.id ORDER BY t.position, pa.position"

# Solved, with where the write-up lives
.venv/bin/python -m bot.sql "
SELECT title, solved_on, post_path, post_anchor
FROM problems WHERE status='solved' ORDER BY solved_on DESC"

# Solve counts per day (streak)
.venv/bin/python -m bot.sql "
SELECT solved_on AS day, COUNT(*) AS n FROM problems
WHERE solved_on IS NOT NULL GROUP BY solved_on ORDER BY day DESC"

# What was handed out, when, and why
.venv/bin/python -m bot.sql "
SELECT a.assigned_on, a.source, p.title
FROM assignments a JOIN problems p ON p.id = a.problem_id
ORDER BY a.id DESC LIMIT 20"

# Patterns not started yet
.venv/bin/python -m bot.sql "
SELECT t.name AS topic, pa.name AS pattern
FROM patterns pa JOIN topics t ON t.id = pa.topic_id
WHERE NOT EXISTS (SELECT 1 FROM problems p
                  WHERE p.pattern_id = pa.id AND p.status != 'pending')
ORDER BY t.position, pa.position"

# Problems listed under several patterns
.venv/bin/python -m bot.sql "
SELECT lc_slug, COUNT(*) AS appearances,
       GROUP_CONCAT(t.name || '/' || pa.name, ' | ') AS patterns
FROM problems p
JOIN patterns pa ON pa.id = p.pattern_id
JOIN topics   t  ON t.id  = pa.topic_id
GROUP BY lc_slug HAVING COUNT(*) > 1 ORDER BY appearances DESC"

# Sheet URLs that aren't real LeetCode problems
.venv/bin/python -m bot.sql "
SELECT DISTINCT lc_slug, url FROM problems WHERE difficulty='Unknown'"

# Premium-only problems (you may not be able to open these)
.venv/bin/python -m bot.sql "SELECT title, lc_slug FROM problems WHERE paid_only=1"

# Pick an easy one to warm up on
.venv/bin/python -m bot.sql "
SELECT p.id, p.title, t.name AS topic
FROM problems p
JOIN patterns pa ON pa.id = p.pattern_id
JOIN topics   t  ON t.id  = pa.topic_id
WHERE p.difficulty='Easy' AND p.status='pending' ORDER BY RANDOM() LIMIT 5"
```

### Corrections

Prefer `bot.cli` over raw SQL where one exists — it keeps notebook, post and git
in step. Use SQL when you need something the CLI doesn't expose.

```bash
# Solved it outside the bot and don't want a write-up
.venv/bin/python -m bot.sql "
UPDATE problems SET status='solved', solved_on=DATE('now') WHERE id=41"

# Undo that
.venv/bin/python -m bot.sql "
UPDATE problems SET status='pending', solved_on=NULL, mirrored_from=NULL WHERE id=41"

# Fix a difficulty the API couldn't resolve
.venv/bin/python -m bot.sql "
UPDATE problems SET difficulty='Medium' WHERE lc_slug='01-knapsack'"

# Retire a problem you never intend to do (premium, or a bogus sheet entry)
.venv/bin/python -m bot.sql "DELETE FROM problems WHERE lc_slug='strong-printer'"

# Start over completely (keeps the sheet import and difficulties)
.venv/bin/python -m bot.sql "
UPDATE problems SET status='pending', assigned_on=NULL, solved_on=NULL,
       notebook_path=NULL, post_path=NULL, post_anchor=NULL,
       published_at=NULL, mirrored_from=NULL"
.venv/bin/python -m bot.sql "DELETE FROM assignments"
```

A `DELETE FROM problems` row comes back on the next `bot.seed` run, because the
sheet is the source of truth. Fix the spreadsheet if you want it gone for good.

### Health and backup

```bash
.venv/bin/python -m bot.sql "PRAGMA integrity_check"
.venv/bin/python -m bot.sql "VACUUM"

cp dsa.db ~/dsa-$(date +%F).db                       # quick copy
.venv/bin/python -m bot.sql --csv "SELECT * FROM problems" > ~/problems.csv
```

The DB is *not* in git. The notebooks and posts are, so a lost DB costs you the
assignment history and dates, not the work. To rebuild after a loss:

```bash
.venv/bin/python -m bot.seed      # re-import sheet + fetch difficulties
# then mark the ones already published:
.venv/bin/python -m bot.sql "
UPDATE problems SET status='solved', solved_on=DATE('now')
WHERE lc_slug IN ('two-sum','course-schedule')"
```

---

## 7. Re-reading the spreadsheet

Run this after editing `DSA_Patterns.xlsx`. It's an upsert — solve state,
notebook paths and dates survive.

```bash
.venv/bin/python -m bot.seed                  # import + fetch missing metadata
.venv/bin/python -m bot.seed --skip-enrich    # import only, no network
.venv/bin/python -m bot.seed --enrich-only    # only fetch missing difficulties
.venv/bin/python -m bot.seed --enrich-only --delay 1.5   # gentler on LeetCode
.venv/bin/python -m bot.seed --limit 10       # try a handful first
```

New rows land as `pending`. Renaming a pattern creates a new one rather than
renaming in place, because patterns are keyed on their slug.

---

## 8. Publishing and git

Normally `/done` handles all of this. Manual equivalents:

```bash
cd ~/hugo-blog
git status
git log --oneline -10
git push origin HEAD:main                    # or Telegram /push

# What the bot generated
ls content/leetcode/                         # one post per topic+pattern
ls -R leetcode/solutions/                    # notebooks
ls static/posts/leetcode/                    # figures pulled from notebook output

# Commit the bot's own source (its commits never include this)
git add .gitignore leetcode && git commit -m "leetcode: bot"
```

Deploy key check:

```bash
ssh -T git@github.com-hugo-blog               # expect "successfully authenticated"
git -C ~/hugo-blog remote -v                  # expect git@github.com-hugo-blog:…
cat ~/.ssh/hugo-blog-deploy.pub               # the key to paste into GitHub
```

Pushing to `main` triggers `.github/workflows/hugo.yml`, which rebuilds and
deploys Pages — usually under a minute.

### Editing a published post by hand

* Above `<!-- solutions -->` — front matter and the pattern intro — is yours. The
  bot never rewrites it once the file exists.
* Below it, each problem sits between `<!-- problem:<slug> start -->` and
  `<!-- problem:<slug> end -->`. `/republish` replaces only that block.
* To change a solution's text, edit the **notebook** and `/republish`, or the post
  will be overwritten next time.

### Notebook cell tags

| Tag | Published | Purpose |
| --- | --- | --- |
| `meta` | no | Header; the post builds its own |
| `statement` | no | LeetCode's text, deliberately not republished |
| `cue` | no | Scenario/clue; the post shows these once in its intro |
| `approach` | **yes** | Your reasoning — the body of the section |
| `solution` | **yes** | Code and its output |
| `tests` | **yes** | Driver cell; output becomes a result block |
| `complexity` | **yes** | Time and space |

Add `no-publish` to any cell to hold it back. In JupyterLab: right sidebar → ⚙
property inspector → *Cell metadata* → `tags`.

---

## 9. Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| `no such file or directory: .venv/bin/python` | Wrong directory | `cd ~/hugo-blog/leetcode` |
| `Conflict (409)` from Telegram | Two pollers on one bot | `systemctl --user stop dsa-bot`, then restart after |
| Bot silent in Telegram | Service down, or wrong chat id | `systemctl --user status dsa-bot`; check `TELEGRAM_CHAT_ID` |
| `/done` says push failed | Deploy key missing or read-only | Re-add with **Allow write access**, then `/push` |
| Push says `Permission denied (publickey)` | Key not authorised | `cat ~/.ssh/hugo-blog-deploy.pub` → GitHub → Settings → Deploy keys |
| Post missing a solution section | Cell tagged `no-publish`, or notebook not saved | Check tags, save, `/republish` |
| Output block missing | Cell wasn't run before `/done` | Run the cell, save, `/republish` |
| DataFrame renders as text, not a table | `unsafe` HTML is off in `config.yml` | Expected; text/plain is used on purpose |
| Difficulty stuck on `Unknown` | Sheet URL isn't a real LeetCode slug | Fix the xlsx, re-run `bot.seed` |
| Daily prompt didn't arrive | Service restarted after 04:00, or clock | `journalctl --user -u dsa-bot --since yesterday`; `/more` meanwhile |
| Changed `.env`, nothing happened | Read only at startup | `systemctl --user restart dsa-bot` |
| `database is locked` | Two writers at once | Stop the service, run the command, start it |

---

## 10. Layout

```
~/hugo-blog/
├── content/leetcode/<topic>-<pattern>.md     generated posts
├── static/posts/leetcode/*.png               figures from notebook output
└── leetcode/
    ├── DSA_Patterns.xlsx                     source of truth
    ├── dsa.db                                state (gitignored)
    ├── .env                                  secrets (gitignored, chmod 600)
    ├── .venv/                                (gitignored)
    ├── setup.sh                              idempotent installer
    ├── README.md                             how it works
    ├── COMMANDS.md                           this file
    ├── systemd/dsa-bot.service.in            unit template
    ├── solutions/<nn>-<topic>/<pattern>/<problem>.ipynb
    └── bot/
        ├── app.py          entrypoint: handlers + 04:00 schedule
        ├── handlers.py     Telegram commands and buttons
        ├── cli.py          same workflow from the shell
        ├── service.py      assign / solve / republish / skip
        ├── sheet.py        xlsx parser (both workbook layouts)
        ├── seed.py         sheet -> DB, plus LeetCode metadata
        ├── db.py           schema and queries
        ├── notebooks.py    notebook generation
        ├── publish.py      notebook -> Hugo post
        ├── gitops.py       pathspec-limited commit and push
        ├── stats.py        progress, pace, finish date
        ├── leetcode_api.py GraphQL client
        ├── sql.py          the SQL runner used above
        ├── whoami.py       chat id capture
        ├── config.py       paths and .env
        └── util.py         slugs, dates, escaping
```
