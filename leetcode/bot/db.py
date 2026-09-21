"""SQLite storage: the sheet's contents plus what has been assigned and solved.

One row per (pattern, problem) pair, because the same LeetCode problem legitimately
appears under more than one pattern in the workbook. Solving it once mirrors the
result onto its siblings so the completion forecast stays honest.
"""
from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Iterator

from . import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS topics (
    id       INTEGER PRIMARY KEY,
    name     TEXT NOT NULL UNIQUE,
    slug     TEXT NOT NULL UNIQUE,
    position INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS patterns (
    id        INTEGER PRIMARY KEY,
    topic_id  INTEGER NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
    name      TEXT NOT NULL,
    slug      TEXT NOT NULL,
    position  INTEGER NOT NULL,
    scenario  TEXT NOT NULL DEFAULT '',
    clue      TEXT NOT NULL DEFAULT '',
    post_path TEXT,
    UNIQUE (topic_id, slug)
);

CREATE TABLE IF NOT EXISTS problems (
    id            INTEGER PRIMARY KEY,
    pattern_id    INTEGER NOT NULL REFERENCES patterns(id) ON DELETE CASCADE,
    position      INTEGER NOT NULL,
    title         TEXT NOT NULL,
    slug          TEXT NOT NULL,
    url           TEXT NOT NULL,
    lc_slug       TEXT NOT NULL,
    lc_id         TEXT,
    difficulty    TEXT NOT NULL DEFAULT 'Unknown',
    paid_only     INTEGER NOT NULL DEFAULT 0,
    status        TEXT NOT NULL DEFAULT 'pending',
    assigned_on   TEXT,
    solved_on     TEXT,
    notebook_path TEXT,
    post_path     TEXT,
    post_anchor   TEXT,
    published_at  TEXT,
    mirrored_from INTEGER REFERENCES problems(id),
    UNIQUE (pattern_id, lc_slug)
);

CREATE TABLE IF NOT EXISTS assignments (
    id          INTEGER PRIMARY KEY,
    problem_id  INTEGER NOT NULL REFERENCES problems(id) ON DELETE CASCADE,
    assigned_on TEXT NOT NULL,
    created_at  TEXT NOT NULL,
    source      TEXT NOT NULL DEFAULT 'daily',
    UNIQUE (problem_id, assigned_on)
);

CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_problems_status  ON problems(status);
CREATE INDEX IF NOT EXISTS idx_problems_lc_slug ON problems(lc_slug);
CREATE INDEX IF NOT EXISTS idx_assign_date      ON assignments(assigned_on);
"""

#: Columns joined onto every problem lookup so callers always get topic/pattern context.
PROBLEM_VIEW = """
SELECT p.*,
       pat.name  AS pattern_name,  pat.slug AS pattern_slug,
       pat.scenario, pat.clue,
       t.name    AS topic_name,    t.slug   AS topic_slug
FROM problems p
JOIN patterns pat ON pat.id = p.pattern_id
JOIN topics   t   ON t.id   = pat.topic_id
"""


def connect(path: Path | None = None) -> sqlite3.Connection:
    conn = sqlite3.connect(path or config.DB_PATH, timeout=30, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn


@contextmanager
def session(path: Path | None = None) -> Iterator[sqlite3.Connection]:
    """Short-lived connection that commits on success and rolls back on error."""
    conn = connect(path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)


def set_meta(conn: sqlite3.Connection, key: str, value: str) -> None:
    conn.execute(
        "INSERT INTO meta(key, value) VALUES (?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        (key, value),
    )


def get_meta(conn: sqlite3.Connection, key: str, default: str | None = None) -> str | None:
    row = conn.execute("SELECT value FROM meta WHERE key = ?", (key,)).fetchone()
    return row["value"] if row else default


# --------------------------------------------------------------------------- reads


def problem(conn: sqlite3.Connection, problem_id: int) -> sqlite3.Row | None:
    return conn.execute(PROBLEM_VIEW + " WHERE p.id = ?", (problem_id,)).fetchone()


def problems_on(conn: sqlite3.Connection, day: str) -> list[sqlite3.Row]:
    """Everything assigned for a given ISO date, in the order it was handed out."""
    return conn.execute(
        PROBLEM_VIEW
        + """
        JOIN assignments a ON a.problem_id = p.id
        WHERE a.assigned_on = ?
        ORDER BY a.id
        """,
        (day,),
    ).fetchall()


def open_problems(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    """Assigned but not yet solved, oldest first - the real working queue."""
    return conn.execute(
        PROBLEM_VIEW + " WHERE p.status = 'assigned' ORDER BY p.assigned_on, p.id"
    ).fetchall()


def pick_unsolved(
    conn: sqlite3.Connection, count: int, topic_slug: str | None = None
) -> list[sqlite3.Row]:
    """Pick random pending problems, at most one per pattern, spread across patterns.

    Picking a whole pattern first and a problem within it keeps the daily prompt
    varied instead of walking down whichever pattern happens to be longest.
    """
    params: list[object] = []
    where = "p.status = 'pending'"
    if topic_slug:
        where += " AND t.slug = ?"
        params.append(topic_slug)

    rows = conn.execute(
        PROBLEM_VIEW
        + f" WHERE {where} ORDER BY RANDOM()",
        params,
    ).fetchall()

    picked: list[sqlite3.Row] = []
    used_patterns: set[int] = set()
    seen_slugs: set[str] = set()
    for row in rows:
        if len(picked) >= count:
            break
        if row["pattern_id"] in used_patterns or row["lc_slug"] in seen_slugs:
            continue
        used_patterns.add(row["pattern_id"])
        seen_slugs.add(row["lc_slug"])
        picked.append(row)

    # Not enough distinct patterns left: top up allowing repeats within a pattern.
    if len(picked) < count:
        for row in rows:
            if len(picked) >= count:
                break
            if row["lc_slug"] in seen_slugs:
                continue
            seen_slugs.add(row["lc_slug"])
            picked.append(row)
    return picked


def find_problems(conn: sqlite3.Connection, term: str, limit: int = 25) -> list[sqlite3.Row]:
    like = f"%{term.strip()}%"
    return conn.execute(
        PROBLEM_VIEW + " WHERE p.title LIKE ? OR p.lc_slug LIKE ? ORDER BY p.id LIMIT ?",
        (like, like, limit),
    ).fetchall()


def list_by_status(
    conn: sqlite3.Connection,
    status: str | tuple[str, ...],
    topic_slug: str | None = None,
    limit: int | None = None,
    offset: int = 0,
) -> list[sqlite3.Row]:
    statuses = (status,) if isinstance(status, str) else status
    placeholders = ",".join("?" for _ in statuses)
    params: list[object] = list(statuses)
    where = f"p.status IN ({placeholders})"
    if topic_slug:
        where += " AND t.slug = ?"
        params.append(topic_slug)
    sql = PROBLEM_VIEW + f" WHERE {where} ORDER BY t.position, pat.position, p.position"
    if limit is not None:
        sql += " LIMIT ? OFFSET ?"
        params += [limit, offset]
    return conn.execute(sql, params).fetchall()


def count_by_status(
    conn: sqlite3.Connection, status: str | tuple[str, ...], topic_slug: str | None = None
) -> int:
    statuses = (status,) if isinstance(status, str) else status
    placeholders = ",".join("?" for _ in statuses)
    params: list[object] = list(statuses)
    where = f"p.status IN ({placeholders})"
    if topic_slug:
        where += " AND t.slug = ?"
        params.append(topic_slug)
    row = conn.execute(
        f"SELECT COUNT(*) AS n FROM problems p "
        f"JOIN patterns pat ON pat.id = p.pattern_id "
        f"JOIN topics t ON t.id = pat.topic_id WHERE {where}",
        params,
    ).fetchone()
    return row["n"]


def topics(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return conn.execute("SELECT * FROM topics ORDER BY position").fetchall()


def pattern(conn: sqlite3.Connection, pattern_id: int) -> sqlite3.Row | None:
    return conn.execute(
        """
        SELECT pat.*, t.name AS topic_name, t.slug AS topic_slug
        FROM patterns pat JOIN topics t ON t.id = pat.topic_id
        WHERE pat.id = ?
        """,
        (pattern_id,),
    ).fetchone()


def pattern_solutions(conn: sqlite3.Connection, pattern_id: int) -> list[sqlite3.Row]:
    """Solved problems of one pattern, in sheet order - the post's section order."""
    return conn.execute(
        PROBLEM_VIEW
        + " WHERE p.pattern_id = ? AND p.status = 'solved' AND p.notebook_path IS NOT NULL"
        " ORDER BY p.position",
        (pattern_id,),
    ).fetchall()


# -------------------------------------------------------------------------- writes


def record_assignment(
    conn: sqlite3.Connection, problem_id: int, day: str, source: str = "daily"
) -> None:
    conn.execute(
        "INSERT OR IGNORE INTO assignments(problem_id, assigned_on, created_at, source) "
        "VALUES (?, ?, ?, ?)",
        (problem_id, day, datetime.now(config.TZ).isoformat(timespec="seconds"), source),
    )
    conn.execute(
        "UPDATE problems SET status = 'assigned', assigned_on = COALESCE(assigned_on, ?) "
        "WHERE id = ? AND status = 'pending'",
        (day, problem_id),
    )


def set_notebook(conn: sqlite3.Connection, problem_id: int, path: str) -> None:
    conn.execute("UPDATE problems SET notebook_path = ? WHERE id = ?", (path, problem_id))


def mark_solved(conn: sqlite3.Connection, problem_id: int, day: str) -> list[sqlite3.Row]:
    """Mark solved and mirror onto the same problem listed under other patterns.

    Returns the mirrored rows so the caller can tell the user what else moved.
    """
    row = problem(conn, problem_id)
    if row is None:
        return []
    conn.execute(
        "UPDATE problems SET status = 'solved', solved_on = COALESCE(solved_on, ?) WHERE id = ?",
        (day, problem_id),
    )
    if not config.MIRROR_DUPLICATES:
        return []
    siblings = conn.execute(
        PROBLEM_VIEW + " WHERE p.lc_slug = ? AND p.id != ? AND p.status != 'solved'",
        (row["lc_slug"], problem_id),
    ).fetchall()
    for sib in siblings:
        conn.execute(
            "UPDATE problems SET status = 'solved', solved_on = COALESCE(solved_on, ?), "
            "mirrored_from = ? WHERE id = ?",
            (day, problem_id, sib["id"]),
        )
    return siblings


def set_published(
    conn: sqlite3.Connection, problem_id: int, post_path: str, anchor: str
) -> None:
    conn.execute(
        "UPDATE problems SET post_path = ?, post_anchor = ?, published_at = ? WHERE id = ?",
        (post_path, anchor, datetime.now(config.TZ).isoformat(timespec="seconds"), problem_id),
    )
    row = problem(conn, problem_id)
    if row is not None:
        # Mirrored siblings point at the same published section.
        conn.execute(
            "UPDATE problems SET post_path = ?, post_anchor = ? WHERE mirrored_from = ?",
            (post_path, anchor, problem_id),
        )


def reset_problem(conn: sqlite3.Connection, problem_id: int) -> None:
    """Put a problem back in the pool (used by /skip and manual corrections)."""
    conn.execute(
        "UPDATE problems SET status = 'pending', assigned_on = NULL, solved_on = NULL, "
        "mirrored_from = NULL WHERE id = ?",
        (problem_id,),
    )
    conn.execute("DELETE FROM assignments WHERE problem_id = ?", (problem_id,))
