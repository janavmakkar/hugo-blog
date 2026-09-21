"""Run SQL against dsa.db without needing the sqlite3 CLI installed.

    python -m bot.sql "SELECT title, difficulty FROM problems LIMIT 5"
    python -m bot.sql --csv "SELECT * FROM topics" > topics.csv
    echo "SELECT COUNT(*) FROM problems" | python -m bot.sql

Writes are allowed and committed; read-only mode is a flag away with --readonly.
"""
from __future__ import annotations

import argparse
import csv
import sqlite3
import sys

from . import config, db


def _render_table(rows: list[sqlite3.Row], columns: list[str]) -> str:
    widths = [len(c) for c in columns]
    cells: list[list[str]] = []
    for row in rows:
        rendered = ["" if row[c] is None else str(row[c]) for c in columns]
        widths = [max(w, len(v)) for w, v in zip(widths, rendered)]
        cells.append(rendered)
    widths = [min(w, 60) for w in widths]

    def line(values: list[str]) -> str:
        return "  ".join(
            (v if len(v) <= w else v[: w - 1] + "…").ljust(w)
            for v, w in zip(values, widths)
        ).rstrip()

    out = [line(columns), "  ".join("-" * w for w in widths)]
    out += [line(c) for c in cells]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run SQL against the bot database.")
    parser.add_argument("sql", nargs="*", help="SQL to run (or pipe it on stdin).")
    parser.add_argument("--csv", action="store_true", help="Emit CSV instead of a table.")
    parser.add_argument("--readonly", action="store_true", help="Refuse to modify anything.")
    args = parser.parse_args(argv)

    statement = " ".join(args.sql).strip() or sys.stdin.read().strip()
    if not statement:
        parser.error("no SQL given")

    if args.readonly:
        conn = sqlite3.connect(f"file:{config.DB_PATH}?mode=ro", uri=True)
        conn.row_factory = sqlite3.Row
    else:
        conn = db.connect()

    try:
        cursor = conn.execute(statement)
        rows = cursor.fetchall()
        if cursor.description:
            columns = [d[0] for d in cursor.description]
            if not rows:
                print("(no rows)", file=sys.stderr)
            elif args.csv:
                writer = csv.writer(sys.stdout)
                writer.writerow(columns)
                writer.writerows([[r[c] for c in columns] for r in rows])
            else:
                print(_render_table(rows, columns))
                print(f"\n{len(rows)} row{'' if len(rows) == 1 else 's'}", file=sys.stderr)
        else:
            conn.commit()
            print(f"{cursor.rowcount} row(s) affected.", file=sys.stderr)
    except sqlite3.Error as exc:
        print(f"SQL error: {exc}", file=sys.stderr)
        return 1
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
