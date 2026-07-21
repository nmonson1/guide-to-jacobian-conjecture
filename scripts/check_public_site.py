#!/usr/bin/env python3
"""Fail CI if the curated public guide leaks internal workspace material."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".html", ".css", ".js", ".txt"}
FORBIDDEN = {
    "/fss/monson/",
    "sources/chatgpt-",
    "conversation-turn-index",
    "reproductions/v1/packages",
    "6a5f33",
    "6a5f34",
}


def main() -> int:
    failures: list[str] = []
    files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.resolve() != Path(__file__).resolve()
        and path.suffix.lower() in TEXT_SUFFIXES
        and ".git" not in path.parts
        and "site" not in path.parts
    ]

    for path in files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        for needle in FORBIDDEN:
            if needle in text:
                failures.append(f"{relative}: forbidden internal marker {needle!r}")

        if path.suffix == ".md":
            for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
                target = match.group(1).split("#", 1)[0]
                if not target or "://" in target or target.startswith(("mailto:", "#")):
                    continue
                candidate = (path.parent / target).resolve()
                if not candidate.exists():
                    failures.append(f"{relative}: missing local link target {target!r}")

    if failures:
        print("Public-site checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Public-site checks passed for {len(files)} text files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
