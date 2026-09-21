"""Load the workbook into SQLite and enrich each problem from LeetCode.

Safe to re-run: the sheet import is an upsert that preserves solve state, and
metadata enrichment only touches rows still marked Unknown, so an interrupted
run just picks up where it stopped.
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
import time

from . import config, db, leetcode_api
from .sheet import parse_workbook
from .util import lc_slug, slugify


def import_sheet(conn: sqlite3.Connection, verbose: bool = True) -> dict[str, int]:
    """Upsert topics, patterns and problems from the workbook. Solve state survives."""
    topics = parse_workbook(config.XLSX_PATH)
    counts = {"topics": 0, "patterns": 0, "problems": 0, "new_problems": 0}

    for t_pos, topic in enumerate(topics):
        t_slug = slugify(topic.name)
        conn.execute(
            "INSERT INTO topics(name, slug, position) VALUES (?, ?, ?) "
            "ON CONFLICT(slug) DO UPDATE SET name = excluded.name, position = excluded.position",
            (topic.name, t_slug, t_pos),
        )
        topic_id = conn.execute("SELECT id FROM topics WHERE slug = ?", (t_slug,)).fetchone()["id"]
        counts["topics"] += 1

        for p_pos, pattern in enumerate(topic.patterns):
            p_slug = slugify(pattern.name)
            conn.execute(
                """
                INSERT INTO patterns(topic_id, name, slug, position, scenario, clue, post_path)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(topic_id, slug) DO UPDATE SET
                    name = excluded.name, position = excluded.position,
                    scenario = excluded.scenario, clue = excluded.clue
                """,
                (
                    topic_id,
                    pattern.name,
                    p_slug,
                    p_pos,
                    pattern.scenario,
                    pattern.clue,
                    f"content/leetcode/{t_slug}-{p_slug}.md",
                ),
            )
            pattern_id = conn.execute(
                "SELECT id FROM patterns WHERE topic_id = ? AND slug = ?", (topic_id, p_slug)
            ).fetchone()["id"]
            counts["patterns"] += 1

            for q_pos, question in enumerate(pattern.questions):
                slug = lc_slug(question.url) or slugify(question.title)
                conn.execute(
                    """
                    INSERT INTO problems(pattern_id, position, title, slug, url, lc_slug)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(pattern_id, lc_slug) DO UPDATE SET
                        position = excluded.position, title = excluded.title, url = excluded.url
                    """,
                    (pattern_id, q_pos, question.title, slugify(question.title), question.url, slug),
                )
                counts["problems"] += 1
        if verbose:
            print(f"  {topic.name}: {len(topic.patterns)} patterns", file=sys.stderr)

    counts["new_problems"] = conn.execute(
        "SELECT COUNT(*) AS n FROM problems WHERE difficulty = 'Unknown'"
    ).fetchone()["n"]
    return counts


def enrich(conn: sqlite3.Connection, delay: float = 0.6, limit: int | None = None,
           verbose: bool = True) -> dict[str, int]:
    """Fill in difficulty / problem number / paid flag for rows still Unknown.

    One LeetCode request per distinct title-slug, shared across every pattern the
    problem appears under.
    """
    rows = conn.execute(
        "SELECT DISTINCT lc_slug FROM problems WHERE difficulty = 'Unknown' AND lc_slug != ''"
        + (" LIMIT ?" if limit else ""),
        (limit,) if limit else (),
    ).fetchall()

    stats = {"fetched": 0, "failed": 0, "total": len(rows)}
    for index, row in enumerate(rows, 1):
        slug = row["lc_slug"]
        question = leetcode_api.fetch_question(slug)
        if not question:
            stats["failed"] += 1
            if verbose:
                print(f"  [{index}/{len(rows)}] {slug}: unreachable", file=sys.stderr)
        else:
            conn.execute(
                "UPDATE problems SET difficulty = ?, lc_id = ?, paid_only = ?, "
                "title = CASE WHEN ? != '' THEN ? ELSE title END WHERE lc_slug = ?",
                (
                    question.get("difficulty") or "Unknown",
                    question.get("questionFrontendId"),
                    1 if question.get("isPaidOnly") else 0,
                    question.get("title") or "",
                    question.get("title") or "",
                    slug,
                ),
            )
            stats["fetched"] += 1
            if verbose:
                print(
                    f"  [{index}/{len(rows)}] {slug}: {question.get('difficulty')}",
                    file=sys.stderr,
                )
        conn.commit()
        if delay and index < len(rows):
            time.sleep(delay)
    return stats


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Seed the DSA bot database from the workbook.")
    parser.add_argument("--skip-enrich", action="store_true",
                        help="Import the sheet only; leave difficulties Unknown.")
    parser.add_argument("--enrich-only", action="store_true",
                        help="Skip the sheet import and only fetch missing LeetCode metadata.")
    parser.add_argument("--delay", type=float, default=0.6,
                        help="Seconds between LeetCode requests (default: 0.6).")
    parser.add_argument("--limit", type=int, default=None,
                        help="Enrich at most N problems (useful for a quick check).")
    args = parser.parse_args(argv)

    with db.session() as conn:
        db.init(conn)
        if not args.enrich_only:
            print("Importing workbook...", file=sys.stderr)
            counts = import_sheet(conn)
            print(
                f"Imported {counts['topics']} topics, {counts['patterns']} patterns, "
                f"{counts['problems']} problems.",
                file=sys.stderr,
            )
        if not args.skip_enrich:
            print("Fetching LeetCode metadata...", file=sys.stderr)
            stats = enrich(conn, delay=args.delay, limit=args.limit)
            print(
                f"Enriched {stats['fetched']}/{stats['total']} "
                f"({stats['failed']} unreachable).",
                file=sys.stderr,
            )
        total = conn.execute("SELECT COUNT(*) AS n FROM problems").fetchone()["n"]
        unknown = conn.execute(
            "SELECT COUNT(*) AS n FROM problems WHERE difficulty = 'Unknown'"
        ).fetchone()["n"]
        print(f"Database ready: {total} problems, {unknown} still without a difficulty.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
