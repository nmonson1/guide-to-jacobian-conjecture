from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

from hooks.editorial import (
    effective_status,
    load_editorial_state,
    page_url,
    public_approved_urls,
)
from scripts.review_pages import COMMAND_STATUS, update


class EditorialStateTests(unittest.TestCase):
    def test_every_markdown_page_is_tracked_and_placed(self) -> None:
        state, navigation = load_editorial_state()
        markdown = {
            path.relative_to(ROOT / "docs").as_posix()
            for path in (ROOT / "docs").rglob("*.md")
        }
        self.assertEqual(set(state), markdown)
        placed = {
            page["path"]
            for section in navigation["sections"]
            for page in section["pages"]
        }
        placed.add(navigation["review_page"]["path"])
        self.assertEqual(placed, markdown)

    def test_changed_approved_content_invalidates_approval(self) -> None:
        original = hashlib.sha256(b"original").hexdigest()
        record = {"status": "approved", "reviewed_sha256": original}
        self.assertEqual(effective_status(record, original), "approved")
        changed = hashlib.sha256(b"changed").hexdigest()
        self.assertEqual(
            effective_status(record, changed), "changed_since_review"
        )

    def test_nonapproved_statuses_are_preserved(self) -> None:
        for status in ("unread", "needs_revision"):
            with self.subTest(status=status):
                self.assertEqual(
                    effective_status(
                        {"status": status, "reviewed_sha256": None}, "anything"
                    ),
                    status,
                )

    def test_directory_urls_are_stable(self) -> None:
        self.assertEqual(page_url("index.md"), "")
        self.assertEqual(page_url("about/index.md"), "about/")
        self.assertEqual(page_url("start/conjecture.md"), "start/conjecture/")

    def test_all_pages_begin_unapproved_in_this_draft(self) -> None:
        ledger = json.loads(
            (ROOT / "editorial" / "reviews.json").read_text(encoding="utf-8")
        )
        self.assertTrue(ledger["pages"])
        self.assertTrue(
            all(record["status"] == "unread" for record in ledger["pages"].values())
        )

    def test_review_workspace_is_never_publicly_listable(self) -> None:
        state = {
            "index.md": {"approved": True, "url": ""},
            "review/index.md": {"approved": True, "url": "review/"},
        }
        self.assertEqual(
            public_approved_urls(state, "review/index.md"),
            {""},
        )

    def test_review_workspace_cannot_be_approved(self) -> None:
        ledger = {"pages": {"review/index.md": {"status": "unread"}}}
        with self.assertRaisesRegex(SystemExit, "permanently unlisted"):
            update(ledger, "review/index.md", "approved")

    def test_review_cli_commands_map_to_valid_states(self) -> None:
        self.assertEqual(
            COMMAND_STATUS,
            {
                "approve": "approved",
                "needs-revision": "needs_revision",
                "unread": "unread",
            },
        )


if __name__ == "__main__":
    unittest.main()
