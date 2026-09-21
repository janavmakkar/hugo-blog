"""Thin client for LeetCode's public GraphQL endpoint.

Used only to enrich the sheet: difficulty, problem number, topic tags, the Python
stub and the problem statement. Every call degrades to None so seeding and
notebook creation still work offline.
"""
from __future__ import annotations

import html
import json
import re
import urllib.error
import urllib.request

from . import config

_ENDPOINT = "https://leetcode.com/graphql"

_QUESTION_QUERY = """
query questionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    isPaidOnly
    content
    topicTags { name }
    codeSnippets { langSlug code }
  }
}
"""


def _post(query: str, variables: dict) -> dict | None:
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    slug = variables.get("titleSlug", "")
    request = urllib.request.Request(
        _ENDPOINT,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": config.USER_AGENT,
            "Referer": f"https://leetcode.com/problems/{slug}/",
            "Origin": "https://leetcode.com",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=config.HTTP_TIMEOUT) as response:
            body = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
        return None
    return body.get("data") or None


def fetch_question(title_slug: str) -> dict | None:
    """Return the question detail dict, or None when LeetCode is unreachable."""
    if not title_slug:
        return None
    data = _post(_QUESTION_QUERY, {"titleSlug": title_slug})
    return (data or {}).get("question")


def python_stub(question: dict | None) -> str:
    """The python3 starter snippet, falling back to a bare class."""
    for snippet in (question or {}).get("codeSnippets") or []:
        if snippet.get("langSlug") == "python3":
            return snippet.get("code", "").rstrip()
    return "class Solution:\n    pass"


_TAG_RE = re.compile(r"<[^>]+>")
_BLOCK_END_RE = re.compile(r"</(p|div|li|ul|ol|pre|h[1-6])>", re.I)


def statement_to_markdown(question: dict | None, max_chars: int = 4000) -> str:
    """Flatten LeetCode's HTML statement into readable Markdown-ish text.

    Deliberately simple: the statement is context while solving, not published
    output, so a faithful HTML->Markdown conversion would be over-engineering.
    """
    raw = (question or {}).get("content") or ""
    if not raw:
        return ""
    text = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", raw, flags=re.S | re.I)
    text = re.sub(r"<(em|i)>(.*?)</\1>", r"*\2*", text, flags=re.S | re.I)
    text = re.sub(r"<code>(.*?)</code>", r"`\1`", text, flags=re.S | re.I)
    text = re.sub(r"<li>", "- ", text, flags=re.I)
    text = _BLOCK_END_RE.sub("\n", text)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = _TAG_RE.sub("", text)
    text = html.unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = "\n".join(line.rstrip() for line in text.splitlines()).strip()
    if len(text) > max_chars:
        text = text[:max_chars].rsplit("\n", 1)[0] + "\n\n*(statement truncated - see LeetCode)*"
    return text
