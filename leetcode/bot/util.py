"""Small shared helpers: slugs, dates, text tidying."""
from __future__ import annotations

import re
import unicodedata
from datetime import date, datetime

_SLUG_STRIP = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Lowercase, ASCII-only, hyphen-separated slug suitable for paths and anchors."""
    text = unicodedata.normalize("NFKD", text or "")
    text = text.encode("ascii", "ignore").decode("ascii")
    return _SLUG_STRIP.sub("-", text.lower()).strip("-") or "untitled"


def lc_slug(url: str) -> str:
    """Extract the LeetCode title-slug from a problem URL."""
    m = re.search(r"leetcode\.com/problems/([^/?#]+)", url or "")
    return m.group(1) if m else ""


def today(tz) -> date:
    return datetime.now(tz).date()


def human_date(d) -> str:
    if isinstance(d, str):
        d = date.fromisoformat(d)
    return d.strftime("%d %b %Y")


def esc(text: str) -> str:
    """Escape for Telegram HTML parse mode."""
    return (text or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def plural(n: int, one: str, many: str | None = None) -> str:
    return one if n == 1 else (many or one + "s")
