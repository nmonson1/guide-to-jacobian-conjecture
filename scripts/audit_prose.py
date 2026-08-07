#!/usr/bin/env python3
"""Report prose habits worth a human editorial pass.

The report is deliberately non-blocking. A phrase can be exactly right in one
place and tiresome in ten; judgment belongs to the editor, not a linter.
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PATTERNS = {
    "negative contrast": re.compile(
        r"\b(?:not|does not|do not|rather than|instead of)\b", re.I
    ),
    "metadiscourse": re.compile(
        r"\b(?:this page|this front|this result|the concrete target|the grouping)\b",
        re.I,
    ),
    "generic heading": re.compile(
        r"^##\s+(?:What is true and why|Precise result|Discussion|"
        r"What it does not prove|Proof source and status)\s*$",
        re.I | re.M,
    ),
}


def main() -> None:
    totals: Counter[str] = Counter()
    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        hits = {
            name: len(pattern.findall(text))
            for name, pattern in PATTERNS.items()
        }
        if any(hits.values()):
            summary = " ".join(
                f"{name}={count}" for name, count in hits.items() if count
            )
            print(path.relative_to(ROOT), summary)
        totals.update(hits)
    print("TOTAL", " ".join(f"{name}={count}" for name, count in totals.items()))


if __name__ == "__main__":
    main()
