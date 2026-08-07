#!/usr/bin/env python3
"""Validate the hand-authored source tree and editorial manifests."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
sys.path.insert(0, str(ROOT))

from hooks.editorial import load_editorial_state  # noqa: E402


FORBIDDEN_ACTIVE_PATHS = (
    ROOT / "claims",
    ROOT / "contributions",
    ROOT / "events",
    ROOT / "assessments",
    ROOT / "data",
    ROOT / "docs-v56-converged-research-20260804j",
    ROOT / "site-state.json",
)

REQUIRED_CREDIT_TEXT = (
    "Our aim is to record every relevant external contribution known to us. "
    "Omissions are mistakes to be corrected, not editorial judgments that the "
    "work was unimportant."
)

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML front matter")
    pieces = text.split("---\n", 2)
    if len(pieces) != 3:
        raise ValueError("unterminated YAML front matter")
    block = pieces[1]
    values: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def main() -> None:
    failures: list[str] = []
    state, navigation = load_editorial_state()

    for path in sorted(DOCS.rglob("*.md")):
        relative = path.relative_to(ROOT).as_posix()
        try:
            metadata = frontmatter(path)
        except ValueError as exc:
            failures.append(f"{relative}: {exc}")
            continue
        for field in ("title", "description"):
            if not metadata.get(field):
                failures.append(f"{relative}: missing {field} front matter")
        if len(path.read_text(encoding="utf-8").split()) < 45:
            failures.append(f"{relative}: too little authored content to be useful")

        source_key = path.relative_to(DOCS).as_posix()
        if state[source_key]["approved"]:
            for raw_target in MARKDOWN_LINK.findall(
                path.read_text(encoding="utf-8")
            ):
                if "://" in raw_target:
                    continue
                target = (path.parent / raw_target).resolve()
                try:
                    target_key = target.relative_to(DOCS.resolve()).as_posix()
                except ValueError:
                    failures.append(f"{relative}: local link leaves docs/: {raw_target}")
                    continue
                if target_key in state and not state[target_key]["approved"]:
                    failures.append(
                        f"{relative}: approved page links to unapproved {target_key}"
                    )

    for forbidden in FORBIDDEN_ACTIVE_PATHS:
        remains = forbidden.is_file() or (
            forbidden.is_dir() and any(path.is_file() for path in forbidden.rglob("*"))
        )
        if remains:
            failures.append(
                f"legacy/generated path remains active: {forbidden.relative_to(ROOT)}"
            )

    credit_page = (DOCS / "about" / "credit-and-sources.md").read_text(
        encoding="utf-8"
    ).replace("\n", " ")
    if REQUIRED_CREDIT_TEXT not in " ".join(credit_page.split()):
        failures.append("credit policy is missing the required external-contribution promise")

    if navigation.get("review_page", {}).get("path") != "review/index.md":
        failures.append("review workspace is not declared as the unlisted review page")

    if not state:
        failures.append("editorial ledger contains no pages")

    if failures:
        print("Source-tree checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Source-tree checks passed for {len(state)} hand-authored pages.")


if __name__ == "__main__":
    main()
