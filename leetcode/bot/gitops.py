"""Commit and push generated files.

Only the paths this bot produced are ever staged - never `git add -A` - so
unrelated work in the checkout is left untouched.
"""
from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from . import config


@dataclass
class GitResult:
    ok: bool
    committed: bool
    pushed: bool
    message: str
    commit: str = ""


def _git(*args: str, check: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=config.REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=180,
        check=check,
    )


def current_branch() -> str:
    proc = _git("rev-parse", "--abbrev-ref", "HEAD")
    return proc.stdout.strip() or config.GIT_BRANCH


def remote_url() -> str:
    return _git("remote", "get-url", "origin").stdout.strip()


def has_changes(paths: list[str]) -> bool:
    existing = [p for p in paths if (config.REPO_ROOT / p).exists()]
    if not existing:
        return False
    return bool(_git("status", "--porcelain", "--", *existing).stdout.strip())


def commit_and_push(paths: list[str], message: str, push: bool | None = None) -> GitResult:
    """Stage `paths`, commit, and push when auto-push is on.

    A failed push is reported but never rolls back the commit: the work is safely
    recorded locally and `git push` can be retried by hand or with /push.
    """
    push = config.AUTO_PUSH if push is None else push
    existing = [p for p in paths if (config.REPO_ROOT / p).exists()]
    if not existing:
        return GitResult(False, False, False, "Nothing to commit: no generated files found.")

    add = _git("add", "--", *existing)
    if add.returncode != 0:
        return GitResult(False, False, False, f"git add failed: {add.stderr.strip()}")

    staged = _git("diff", "--cached", "--name-only", "--", *existing).stdout.strip()
    if not staged:
        return GitResult(True, False, False, "No changes to commit (files already up to date).")

    # Pathspec-limited commit: anything else you happen to have staged stays staged.
    commit = _git("commit", "-m", message, "--", *existing)
    if commit.returncode != 0:
        return GitResult(False, False, False, f"git commit failed: {commit.stderr.strip()}")
    sha = _git("rev-parse", "--short", "HEAD").stdout.strip()

    if not push:
        return GitResult(True, True, False, f"Committed {sha} (auto-push off).", sha)

    branch = current_branch()
    pushed = _git("push", "origin", f"HEAD:{branch}")
    if pushed.returncode != 0:
        detail = (pushed.stderr or pushed.stdout).strip().splitlines()
        tail = detail[-1] if detail else "unknown error"
        return GitResult(
            True, True, False,
            f"Committed {sha} but push failed: {tail}\nRun /push to retry.", sha,
        )
    return GitResult(True, True, True, f"Committed {sha} and pushed to {branch}.", sha)


def push_only() -> GitResult:
    """Retry a push after a credential fix, without making a new commit."""
    branch = current_branch()
    proc = _git("push", "origin", f"HEAD:{branch}")
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout).strip().splitlines()
        return GitResult(False, False, False, detail[-1] if detail else "push failed")
    out = (proc.stderr or proc.stdout).strip() or f"Pushed to {branch}."
    return GitResult(True, False, True, out)


def unpushed_count() -> int:
    branch = current_branch()
    proc = _git("rev-list", "--count", f"origin/{branch}..HEAD")
    try:
        return int(proc.stdout.strip())
    except ValueError:
        return 0


def relative(path: Path) -> str:
    return str(Path(path).resolve().relative_to(config.REPO_ROOT))
