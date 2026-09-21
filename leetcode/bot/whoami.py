"""Capture your Telegram chat id and write it into leetcode/.env.

Run it, send the bot any message, and it fills in TELEGRAM_CHAT_ID for you.
It waits indefinitely by default, so you can start it and get to it later.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request

from . import config


def write_env(chat_id: int) -> bool:
    """Set TELEGRAM_CHAT_ID in leetcode/.env, leaving every other line alone."""
    if not config.ENV_PATH.is_file():
        return False
    text = config.ENV_PATH.read_text(encoding="utf-8")
    line = f"TELEGRAM_CHAT_ID={chat_id}"
    if re.search(r"^TELEGRAM_CHAT_ID=.*$", text, flags=re.M):
        text = re.sub(r"^TELEGRAM_CHAT_ID=.*$", line, text, count=1, flags=re.M)
    else:
        text = text.rstrip("\n") + "\n" + line + "\n"
    config.ENV_PATH.write_text(text, encoding="utf-8")
    config.ENV_PATH.chmod(0o600)
    return True


def listen(deadline: float | None) -> int | None:
    """Return the chat id of the next incoming message, or None on timeout."""
    base = f"https://api.telegram.org/bot{config.BOT_TOKEN}"
    offset = 0
    warned_conflict = False

    while deadline is None or time.time() < deadline:
        try:
            with urllib.request.urlopen(
                f"{base}/getUpdates?timeout=25&offset={offset}", timeout=35
            ) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code == 409:
                if not warned_conflict:
                    print(
                        "Another poller holds this bot (409) - probably the service.\n"
                        "Stop it with: systemctl --user stop dsa-bot\n"
                        "Waiting…",
                        file=sys.stderr,
                    )
                    warned_conflict = True
                time.sleep(5)
                continue
            if exc.code == 401:
                print("Telegram rejected the token (401). Check TELEGRAM_BOT_TOKEN.",
                      file=sys.stderr)
                return None
            print(f"Telegram error {exc.code}; retrying…", file=sys.stderr)
            time.sleep(3)
            continue
        except (urllib.error.URLError, TimeoutError, OSError):
            time.sleep(2)
            continue

        warned_conflict = False
        for update in body.get("result", []):
            offset = update["update_id"] + 1
            message = update.get("message") or update.get("edited_message") or {}
            chat = message.get("chat") or {}
            if chat.get("id"):
                name = chat.get("username") or chat.get("first_name") or "you"
                print(f"Got a message from {name}.", file=sys.stderr)
                return int(chat["id"])
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Capture your Telegram chat id.")
    parser.add_argument("--wait", type=int, default=0,
                        help="Seconds to wait (0 = forever, the default).")
    parser.add_argument("--no-write", action="store_true",
                        help="Print the id instead of writing it to .env.")
    args = parser.parse_args(argv)

    if not config.BOT_TOKEN:
        print("Set TELEGRAM_BOT_TOKEN in leetcode/.env first.", file=sys.stderr)
        return 1

    print("Send your bot any message now (Ctrl-C to stop)…", file=sys.stderr)
    try:
        chat_id = listen(time.time() + args.wait if args.wait else None)
    except KeyboardInterrupt:
        print("\nStopped.", file=sys.stderr)
        return 1

    if chat_id is None:
        print("No message received.", file=sys.stderr)
        return 1

    print(f"\nTELEGRAM_CHAT_ID={chat_id}")
    if args.no_write:
        return 0
    if write_env(chat_id):
        print(f"Written to {config.ENV_PATH}")
        print("Now run:  systemctl --user enable --now dsa-bot")
    else:
        print(f"Could not find {config.ENV_PATH}; add the line above yourself.",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
