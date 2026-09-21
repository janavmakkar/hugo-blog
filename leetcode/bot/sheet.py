"""Read DSA_Patterns.xlsx with the standard library only.

The workbook uses two different layouts for the "Questions" row and both appear
in the same file, so the parser normalises them into one shape:

    Layout A (Arrays, Strings, Binary Search, Recursion, Linked List, Stacks)
        one cell per pattern holding blank-line separated blocks of
        "Title\\nhttps://leetcode.com/problems/..."

    Layout B (Binary Trees, Priority Queues, Dynamic Programming, Graphs)
        one question per cell going down the column, written as
        "Title: https://leetcode.com/problems/..."

Parsing xlsx by hand keeps `seed` dependency-free; openpyxl is never imported.
"""
from __future__ import annotations

import re
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from xml.etree import ElementTree as ET

_MAIN = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
_REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"

_COL_RE = re.compile(r"([A-Z]+)(\d+)")
_URL_LINE_RE = re.compile(r"^(?P<title>.*?)\s*[:–—-]?\s*(?P<url>https?://\S+)\s*$")


@dataclass
class Question:
    title: str
    url: str


@dataclass
class Pattern:
    name: str
    scenario: str = ""
    clue: str = ""
    questions: list[Question] = field(default_factory=list)


@dataclass
class Topic:
    name: str
    patterns: list[Pattern] = field(default_factory=list)


def _col_letters(ref: str) -> str:
    m = _COL_RE.match(ref)
    return m.group(1) if m else ""


def _col_index(letters: str) -> int:
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - 64)
    return n


def _read_grid(zf: zipfile.ZipFile, target: str, shared: list[str]) -> dict[tuple[int, str], str]:
    """Return {(row_number, column_letters): text} for the non-empty cells of a sheet."""
    ws = ET.fromstring(zf.read("xl/" + target.lstrip("/")))
    grid: dict[tuple[int, str], str] = {}
    for row in ws.iter(_MAIN + "row"):
        rnum = int(row.get("r"))
        for cell in row.findall(_MAIN + "c"):
            kind = cell.get("t")
            if kind == "s":
                node = cell.find(_MAIN + "v")
                value = shared[int(node.text)] if node is not None else ""
            elif kind == "inlineStr":
                value = "".join(t.text or "" for t in cell.iter(_MAIN + "t"))
            else:
                node = cell.find(_MAIN + "v")
                value = node.text if node is not None else ""
            if value and value.strip():
                grid[(rnum, _col_letters(cell.get("r")))] = value
    return grid


def _parse_questions(cell_texts: list[str]) -> list[Question]:
    """Turn the raw cell text(s) of one pattern column into ordered questions.

    Handles both workbook layouts plus the mixed cases in between: a title on its
    own line followed by a bare URL, or title and URL joined on a single line.
    """
    questions: list[Question] = []
    pending_title = ""

    def flush() -> None:
        nonlocal pending_title
        if pending_title:
            questions.append(Question(pending_title, ""))
            pending_title = ""

    for text in cell_texts:
        for raw in text.replace("\r\n", "\n").split("\n"):
            line = raw.strip().lstrip("-•").strip()
            if not line:
                continue
            match = _URL_LINE_RE.match(line)
            if not match:
                # A plain title line; the URL should be on the next line.
                flush()
                pending_title = line
                continue
            title = match.group("title").strip()
            url = match.group("url").strip().rstrip(").,;")
            if title:
                flush()
                questions.append(Question(title, url))
            elif pending_title:
                questions.append(Question(pending_title, url))
                pending_title = ""
            else:
                # URL with no title anywhere: fall back to the LeetCode slug.
                slug = url.rstrip("/").rsplit("/", 1)[-1]
                questions.append(Question(slug.replace("-", " ").title(), url))
    flush()

    # Drop exact repeats inside a single pattern while keeping sheet order.
    seen: set[str] = set()
    unique: list[Question] = []
    for q in questions:
        key = (q.url or q.title).lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(q)
    return unique


def parse_workbook(path: Path) -> list[Topic]:
    """Parse every worksheet into Topic -> Pattern -> Question, preserving sheet order."""
    with zipfile.ZipFile(path) as zf:
        shared = [
            "".join(t.text or "" for t in si.iter(_MAIN + "t"))
            for si in ET.fromstring(zf.read("xl/sharedStrings.xml"))
        ]
        workbook = ET.fromstring(zf.read("xl/workbook.xml"))
        rels = {
            r.get("Id"): r.get("Target")
            for r in ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        }

        topics: list[Topic] = []
        for sheet in workbook.find(_MAIN + "sheets"):
            name = sheet.get("name")
            grid = _read_grid(zf, rels[sheet.get(_REL + "id")], shared)
            if not grid:
                continue

            labels = {
                grid[(r, "A")].strip(): r
                for (r, c) in grid
                if c == "A" and grid[(r, "A")].strip()
            }
            header_row = min(r for (r, _c) in grid)
            questions_row = labels.get("Questions")
            if questions_row is None:  # No question block on this sheet.
                continue
            scenario_row = labels.get("Scenarios")
            clue_row = labels.get("Clue")
            last_row = max(r for (r, _c) in grid)

            topic = Topic(name=name)
            columns = sorted(
                {c for (r, c) in grid if r == header_row and c != "A"},
                key=_col_index,
            )
            for col in columns:
                pattern_name = grid[(header_row, col)].strip()
                if not pattern_name:
                    continue
                cells = [
                    grid[(r, col)]
                    for r in range(questions_row, last_row + 1)
                    if (r, col) in grid
                ]
                topic.patterns.append(
                    Pattern(
                        name=pattern_name,
                        scenario=grid.get((scenario_row, col), "").strip() if scenario_row else "",
                        clue=grid.get((clue_row, col), "").strip() if clue_row else "",
                        questions=_parse_questions(cells),
                    )
                )
            topics.append(topic)
    return topics
