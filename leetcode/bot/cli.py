"""Command-line access to the same workflow, for when you are already on the box.

    python -m bot.cli assign 2
    python -m bot.cli open
    python -m bot.cli done 41
    python -m bot.cli republish 41
    python -m bot.cli progress
"""
from __future__ import annotations

import argparse

from . import db, gitops, service, stats
from .util import human_date


def _print_rows(rows) -> None:
    for r in rows:
        mark = {"Easy": "E", "Medium": "M", "Hard": "H"}.get(r["difficulty"], "?")
        print(
            f"#{r['id']:<4} [{mark}] {r['title'][:46]:<46} "
            f"{r['topic_name']} / {r['pattern_name']}"
        )
        if r["notebook_path"]:
            print(f"       {r['notebook_path']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="bot.cli", description="DSA bot, without Telegram.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_assign = sub.add_parser("assign", help="Assign N problems and create notebooks.")
    p_assign.add_argument("count", type=int, nargs="?", default=2)
    p_assign.add_argument("--topic", default=None, help="Restrict to one topic slug.")

    sub.add_parser("open", help="List assigned but unsolved problems.")
    sub.add_parser("today", help="List today's assignment.")
    sub.add_parser("progress", help="Show progress and the projected finish date.")

    p_done = sub.add_parser("done", help="Mark solved, publish the post, commit and push.")
    p_done.add_argument("problem_id", type=int)
    p_done.add_argument("--no-push", action="store_true")

    p_pub = sub.add_parser("republish", help="Re-render a solved problem after editing it.")
    p_pub.add_argument("problem_id", type=int)
    p_pub.add_argument("--no-push", action="store_true")

    p_skip = sub.add_parser("skip", help="Return an assigned problem to the pool.")
    p_skip.add_argument("problem_id", type=int)

    p_find = sub.add_parser("find", help="Search problems by title.")
    p_find.add_argument("term", nargs="+")

    sub.add_parser("push", help="Retry pushing existing commits.")

    args = parser.parse_args(argv)

    with db.session() as conn:
        if args.command == "assign":
            items = service.assign(conn, args.count, source="manual", topic_slug=args.topic)
            if not items:
                print("Nothing left to assign.")
                return 0
            for item in items:
                print(f"#{item.row['id']} {item.row['title']}\n  {item.notebook}")
        elif args.command == "open":
            _print_rows(db.open_problems(conn))
        elif args.command == "today":
            _print_rows(service.batch_for(conn))
        elif args.command == "progress":
            p = stats.compute(conn)
            print(f"{p.solved}/{p.total} solved ({p.percent:.1f}%), {p.remaining} left")
            for t in p.by_topic:
                print(f"  {t['solved']:>3}/{t['total']:<3}  {t['name']}")
            for d in p.by_difficulty:
                print(f"  {d['solved']:>3}/{d['total']:<3}  {d['difficulty']}")
            if p.eta:
                print(f"Projected finish: {human_date(p.eta)} ({p.days_left} days)")
        elif args.command in {"done", "republish"}:
            push = not args.no_push
            fn = service.solve if args.command == "done" else service.republish
            result = fn(conn, args.problem_id, push=push)
            print(result.title)
            print(f"  post: {result.post_path}")
            print(f"  url:  {result.post_url}")
            if result.mirrored:
                print("  also cleared: " + ", ".join(result.mirrored))
            print(f"  git:  {result.git.message}")
        elif args.command == "skip":
            row = service.skip(conn, args.problem_id)
            print(f"{row['title']} returned to the pool." if row else "No such problem.")
        elif args.command == "find":
            _print_rows(db.find_problems(conn, " ".join(args.term)))
        elif args.command == "push":
            print(gitops.push_only().message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
