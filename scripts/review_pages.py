#!/usr/bin/env python3
"""Read and update the exact-version editorial review ledger."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LEDGER = ROOT / "editorial" / "reviews.json"
REVIEW_PAGE = "review/index.md"
COMMAND_STATUS = {
    "approve": "approved",
    "needs-revision": "needs_revision",
    "unread": "unread",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(raw: str) -> str:
    candidate = Path(raw)
    if candidate.parts and candidate.parts[0] == "docs":
        candidate = Path(*candidate.parts[1:])
    path = candidate.as_posix()
    if path.startswith("../") or Path(path).is_absolute():
        raise SystemExit(f"page must be under docs/: {raw}")
    return path


def load() -> dict:
    return json.loads(LEDGER.read_text(encoding="utf-8"))


def effective(record: dict, path: Path) -> str:
    if record["status"] != "approved":
        return record["status"]
    return "approved" if record.get("reviewed_sha256") == digest(path) else "changed_since_review"


def show(ledger: dict, selected: str | None = None) -> None:
    for page, record in sorted(ledger["pages"].items()):
        if selected is not None and page != selected:
            continue
        state = effective(record, DOCS / page)
        timestamp = record.get("reviewed_at") or "—"
        print(f"{state:22} {page:48} {timestamp}")


def update(ledger: dict, page: str, status: str) -> None:
    if page not in ledger["pages"]:
        raise SystemExit(f"page is not in editorial/reviews.json: {page}")
    if page == REVIEW_PAGE and status == "approved":
        raise SystemExit("the review workspace is permanently unlisted")
    source = DOCS / page
    if not source.is_file():
        raise SystemExit(f"page does not exist: docs/{page}")
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    record = ledger["pages"][page]
    record["status"] = status
    record["reviewed_at"] = now if status != "unread" else None
    record["reviewed_sha256"] = digest(source) if status == "approved" else None
    LEDGER.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
    print(f"{page}: {status}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("page", nargs="?")
    for command in ("approve", "needs-revision", "unread"):
        child = subparsers.add_parser(command)
        child.add_argument("page")
    args = parser.parse_args()
    ledger = load()
    page = normalize(args.page) if getattr(args, "page", None) else None
    if args.command == "status":
        show(ledger, page)
        return
    update(ledger, page, COMMAND_STATUS[args.command])


if __name__ == "__main__":
    main()
