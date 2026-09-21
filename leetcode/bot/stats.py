"""Progress arithmetic: counts, pace and the projected finish date."""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta

from . import config

DIFFICULTY_ORDER = ["Easy", "Medium", "Hard", "Unknown"]


@dataclass
class Progress:
    total: int = 0
    solved: int = 0
    assigned: int = 0
    published: int = 0
    remaining: int = 0
    first_solve: date | None = None
    last_solve: date | None = None
    calendar_days: int = 0
    active_days: int = 0
    per_calendar_day: float = 0.0
    per_active_day: float = 0.0
    eta: date | None = None
    days_left: int | None = None
    by_topic: list[dict] = field(default_factory=list)
    by_difficulty: list[dict] = field(default_factory=list)

    @property
    def percent(self) -> float:
        return (self.solved / self.total * 100) if self.total else 0.0


def _as_date(value: str | None) -> date | None:
    return date.fromisoformat(value) if value else None


def compute(conn: sqlite3.Connection, today: date | None = None) -> Progress:
    """Build the full progress snapshot in a handful of aggregate queries."""
    today = today or datetime.now(config.TZ).date()
    p = Progress()

    row = conn.execute(
        """
        SELECT COUNT(*) AS total,
               SUM(status = 'solved')                      AS solved,
               SUM(status = 'assigned')                    AS assigned,
               SUM(published_at IS NOT NULL)               AS published,
               MIN(solved_on)                              AS first_solve,
               MAX(solved_on)                              AS last_solve
        FROM problems
        """
    ).fetchone()
    p.total = row["total"] or 0
    p.solved = row["solved"] or 0
    p.assigned = row["assigned"] or 0
    p.published = row["published"] or 0
    p.remaining = p.total - p.solved
    p.first_solve = _as_date(row["first_solve"])
    p.last_solve = _as_date(row["last_solve"])

    p.active_days = conn.execute(
        "SELECT COUNT(DISTINCT solved_on) AS n FROM problems WHERE solved_on IS NOT NULL"
    ).fetchone()["n"]

    if p.first_solve:
        p.calendar_days = (today - p.first_solve).days + 1
        p.per_calendar_day = p.solved / p.calendar_days if p.calendar_days else 0.0
        p.per_active_day = p.solved / p.active_days if p.active_days else 0.0
        if p.per_calendar_day > 0 and p.remaining > 0:
            p.days_left = max(1, round(p.remaining / p.per_calendar_day))
            p.eta = today + timedelta(days=p.days_left)
        elif p.remaining == 0:
            p.days_left = 0
            p.eta = p.last_solve

    p.by_topic = [
        dict(r)
        for r in conn.execute(
            """
            SELECT t.name, t.slug,
                   COUNT(*)                 AS total,
                   SUM(p.status = 'solved') AS solved
            FROM problems p
            JOIN patterns pat ON pat.id = p.pattern_id
            JOIN topics   t   ON t.id   = pat.topic_id
            GROUP BY t.id
            ORDER BY t.position
            """
        ).fetchall()
    ]

    rows = {
        r["difficulty"]: dict(r)
        for r in conn.execute(
            """
            SELECT difficulty,
                   COUNT(*)               AS total,
                   SUM(status = 'solved') AS solved
            FROM problems GROUP BY difficulty
            """
        ).fetchall()
    }
    p.by_difficulty = [
        rows.get(name, {"difficulty": name, "total": 0, "solved": 0})
        for name in DIFFICULTY_ORDER
        if rows.get(name, {}).get("total")
    ]
    return p


def recent_days(conn: sqlite3.Connection, limit: int = 14) -> list[dict]:
    """Solve counts per day, most recent first - the streak view."""
    return [
        dict(r)
        for r in conn.execute(
            "SELECT solved_on AS day, COUNT(*) AS n FROM problems "
            "WHERE solved_on IS NOT NULL GROUP BY solved_on ORDER BY solved_on DESC LIMIT ?",
            (limit,),
        ).fetchall()
    ]


def bar(fraction: float, width: int = 12) -> str:
    """Monospace progress bar for Telegram."""
    filled = round(max(0.0, min(1.0, fraction)) * width)
    return "█" * filled + "░" * (width - filled)
