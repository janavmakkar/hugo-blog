"""Bot entrypoint: wires handlers, schedules the daily prompt, starts long polling.

Long polling is deliberate - it needs no domain, no TLS and no inbound firewall
rule on the VPS, which is the whole reason a webhook would be more work here.
"""
from __future__ import annotations

import logging
import sys
from datetime import time as dtime

from telegram.ext import (
    Application,
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    filters,
)

from . import config, db, handlers

LOG = logging.getLogger("dsa-bot")

COMMANDS = [
    ("start", handlers.start),
    ("help", handlers.help_command),
    ("today", handlers.today),
    ("more", handlers.more),
    ("open", handlers.open_list),
    ("done", handlers.done),
    ("skip", handlers.skip),
    ("republish", handlers.republish),
    ("progress", handlers.progress),
    ("topics", handlers.topics),
    ("solved", handlers.solved),
    ("unsolved", handlers.unsolved),
    ("find", handlers.find),
    ("push", handlers.push),
    ("status", handlers.status),
]


def _configure_logging() -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        level=logging.INFO,
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("telegram.ext.Application").setLevel(logging.WARNING)


def build_application() -> Application:
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()

    # The bot can push to git, so it answers exactly one chat and ignores the rest.
    only_owner = filters.Chat(config.OWNER_CHAT_ID)
    for name, callback in COMMANDS:
        app.add_handler(CommandHandler(name, callback, filters=only_owner))
    app.add_handler(CallbackQueryHandler(handlers.on_callback))
    app.add_error_handler(handlers.on_error)

    app.job_queue.run_daily(
        handlers.daily_job,
        time=dtime(hour=config.DAILY_HOUR, minute=config.DAILY_MINUTE, tzinfo=config.TZ),
        name="daily-prompt",
    )
    return app


def main() -> int:
    _configure_logging()

    missing = config.missing_settings()
    if missing:
        print(
            "Missing required settings: " + ", ".join(missing) + f"\nSet them in {config.ENV_PATH}",
            file=sys.stderr,
        )
        return 1
    if not config.DB_PATH.exists():
        print(
            f"No database at {config.DB_PATH}. Run: python -m bot.seed",
            file=sys.stderr,
        )
        return 1

    with db.session() as conn:
        total = conn.execute("SELECT COUNT(*) AS n FROM problems").fetchone()["n"]
    LOG.info(
        "Starting with %d problems; daily prompt at %02d:%02d %s",
        total,
        config.DAILY_HOUR,
        config.DAILY_MINUTE,
        config.TIMEZONE_NAME,
    )

    build_application().run_polling(drop_pending_updates=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
