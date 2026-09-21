"""Paths and environment configuration.

Everything is derived from this file's location, so the checkout can be moved
without editing anything. Secrets and per-machine knobs live in leetcode/.env.
"""
from __future__ import annotations

import os
from pathlib import Path
from zoneinfo import ZoneInfo

BOT_DIR = Path(__file__).resolve().parent
LEETCODE_DIR = BOT_DIR.parent
REPO_ROOT = LEETCODE_DIR.parent

XLSX_PATH = LEETCODE_DIR / "DSA_Patterns.xlsx"
SOLUTIONS_DIR = LEETCODE_DIR / "solutions"
DB_PATH = LEETCODE_DIR / "dsa.db"
ENV_PATH = LEETCODE_DIR / ".env"

CONTENT_DIR = REPO_ROOT / "content" / "leetcode"
STATIC_IMG_DIR = REPO_ROOT / "static" / "posts" / "leetcode"
#: How static/ images are addressed from inside a post.
STATIC_IMG_URL = "/posts/leetcode"

#: Marker the publisher writes into every generated post; solutions are appended below it.
SOLUTIONS_MARKER = "<!-- solutions -->"


def _load_env_file(path: Path) -> None:
    """Load KEY=VALUE lines into os.environ without clobbering the real environment."""
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip("'\"")
        os.environ.setdefault(key, value)


_load_env_file(ENV_PATH)


def _int(name: str, default: int) -> int:
    try:
        return int(os.environ.get(name, "").strip() or default)
    except ValueError:
        return default


def _bool(name: str, default: bool) -> bool:
    raw = os.environ.get(name, "").strip().lower()
    if not raw:
        return default
    return raw in {"1", "true", "yes", "on"}


BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
#: Only this chat may talk to the bot. It can push to git, so this is the security boundary.
OWNER_CHAT_ID = _int("TELEGRAM_CHAT_ID", 0)

TIMEZONE_NAME = os.environ.get("TIMEZONE", "Asia/Kolkata").strip() or "Asia/Kolkata"
TZ = ZoneInfo(TIMEZONE_NAME)

DAILY_HOUR = _int("DAILY_HOUR", 4)
DAILY_MINUTE = _int("DAILY_MINUTE", 0)
DAILY_COUNT = _int("DAILY_COUNT", 2)

SITE_BASE_URL = (os.environ.get("SITE_BASE_URL", "https://janav.in").strip().rstrip("/"))
AUTO_PUSH = _bool("AUTO_PUSH", True)
#: The same problem appears under several patterns; solving it once clears them all.
MIRROR_DUPLICATES = _bool("MIRROR_DUPLICATES", True)
GIT_BRANCH = os.environ.get("GIT_BRANCH", "main").strip() or "main"

#: Cover image reused across every generated pattern post (already in static/posts/).
POST_COVER = os.environ.get("POST_COVER", "posts/otter_basic_dsa.jpg").strip()

HTTP_TIMEOUT = _int("HTTP_TIMEOUT", 20)
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def missing_settings() -> list[str]:
    """Names of required settings that are still unset."""
    missing = []
    if not BOT_TOKEN:
        missing.append("TELEGRAM_BOT_TOKEN")
    if not OWNER_CHAT_ID:
        missing.append("TELEGRAM_CHAT_ID")
    return missing
