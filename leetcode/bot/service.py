"""The workflow itself, independent of Telegram.

Every operation the bot exposes lives here so it can also be driven from the
command line (see `python -m bot.cli`) when you are already on the box.
"""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date, datetime

from . import config, db, gitops, notebooks, publish


@dataclass
class Assigned:
    row: sqlite3.Row
    notebook: str
    created: bool


@dataclass
class Published:
    title: str
    post_path: str
    post_url: str
    notebook: str
    git: gitops.GitResult
    mirrored: list[str]


def today(conn: sqlite3.Connection | None = None) -> date:
    return datetime.now(config.TZ).date()


def assign(
    conn: sqlite3.Connection,
    count: int,
    source: str = "daily",
    topic_slug: str | None = None,
    day: date | None = None,
) -> list[Assigned]:
    """Hand out `count` fresh problems and create a notebook for each."""
    day = day or today()
    picked = db.pick_unsolved(conn, count, topic_slug=topic_slug)
    out: list[Assigned] = []
    for row in picked:
        db.record_assignment(conn, row["id"], day.isoformat(), source=source)
        path = notebooks.create_for_problem(conn, row)
        out.append(
            Assigned(
                row=db.problem(conn, row["id"]),
                notebook=str(path.relative_to(config.REPO_ROOT)),
                created=True,
            )
        )
    return out


def batch_for(conn: sqlite3.Connection, day: date | None = None) -> list[sqlite3.Row]:
    return db.problems_on(conn, (day or today()).isoformat())


def solve(
    conn: sqlite3.Connection, problem_id: int, day: date | None = None, push: bool | None = None
) -> Published:
    """Mark solved, render the post, and commit notebook + post (+ any figures)."""
    day = day or today()
    row = db.problem(conn, problem_id)
    if row is None:
        raise ValueError(f"No problem with id {problem_id}")

    mirrored = db.mark_solved(conn, problem_id, day.isoformat())
    result = publish.publish_problem(conn, problem_id)
    row = db.problem(conn, problem_id)

    paths = [result["post_path"]]
    if row["notebook_path"]:
        paths.append(row["notebook_path"])
    image_dir = config.STATIC_IMG_DIR
    if image_dir.exists():
        prefix = f"{row['topic_slug']}-{row['pattern_slug']}-{row['lc_slug']}"
        paths += [
            str(p.relative_to(config.REPO_ROOT))
            for p in sorted(image_dir.glob(f"{prefix}-*.png"))
        ]

    git = gitops.commit_and_push(
        paths,
        f"leetcode: solve {row['title']} ({row['topic_name']} / {row['pattern_name']})",
        push=push,
    )
    return Published(
        title=row["title"],
        post_path=result["post_path"],
        post_url=result["post_url"],
        notebook=row["notebook_path"] or "",
        git=git,
        mirrored=[f"{m['topic_name']} / {m['pattern_name']}" for m in mirrored],
    )


def republish(
    conn: sqlite3.Connection, problem_id: int, push: bool | None = None
) -> Published:
    """Re-render an already-solved problem after editing its notebook."""
    row = db.problem(conn, problem_id)
    if row is None:
        raise ValueError(f"No problem with id {problem_id}")
    if row["status"] != "solved":
        return solve(conn, problem_id, push=push)

    result = publish.publish_problem(conn, problem_id)
    paths = [result["post_path"]]
    if row["notebook_path"]:
        paths.append(row["notebook_path"])
    git = gitops.commit_and_push(
        paths, f"leetcode: update write-up for {row['title']}", push=push
    )
    return Published(
        title=row["title"],
        post_path=result["post_path"],
        post_url=result["post_url"],
        notebook=row["notebook_path"] or "",
        git=git,
        mirrored=[],
    )


def skip(conn: sqlite3.Connection, problem_id: int) -> sqlite3.Row | None:
    """Return an assigned problem to the pool. The notebook file is left in place."""
    row = db.problem(conn, problem_id)
    if row is None:
        return None
    db.reset_problem(conn, problem_id)
    return row


def ensure_notebook(conn: sqlite3.Connection, problem_id: int) -> str:
    row = db.problem(conn, problem_id)
    if row is None:
        raise ValueError(f"No problem with id {problem_id}")
    path = notebooks.create_for_problem(conn, row)
    return str(path.relative_to(config.REPO_ROOT))
