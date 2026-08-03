from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from inventory_active_tree import build_inventory, generated_root  # noqa: E402


class ActiveTreeInventoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.state = {
            "release_id": "release-current",
            "docs_dir": "docs-v3-current",
            "publication": {"data_dir": "publication-v3"},
            "model_briefs": {"data_dir": "handoffs-v3"},
            "expected_counts": {},
        }

    def test_generated_root(self) -> None:
        self.assertEqual(generated_root("docs-v3-current/index.md"), "docs-v3-current")
        self.assertEqual(generated_root("data/handoffs-v3/manifest.json"), "data/handoffs-v3")
        self.assertIsNone(generated_root("scripts/build.py"))

    def test_inventory_separates_selected_and_inactive(self) -> None:
        tracked = [
            "docs-v2-old/index.md",
            "docs-v3-current/index.md",
            "data/publication-v2/manifest.json",
            "data/publication-v3/manifest.json",
            "data/handoffs-v3/manifest.json",
            "scripts/build.py",
        ]
        sizes = {path: index + 1 for index, path in enumerate(tracked)}
        inventory = build_inventory(
            state=self.state,
            commit="abc123",
            tracked_paths=tracked,
            untracked_paths=["docs-v4-candidate", "data/handoffs-v4"],
            sizes=sizes,
        )
        self.assertEqual(inventory["selected"]["tracked_files"], 3)
        self.assertEqual(
            inventory["inactive_tracked"]["roots"],
            ["data/publication-v2", "docs-v2-old"],
        )
        self.assertEqual(
            inventory["untracked_generated_candidates"]["roots"],
            ["data/handoffs-v4", "docs-v4-candidate"],
        )

    def test_inventory_rejects_missing_selected_root(self) -> None:
        with self.assertRaisesRegex(ValueError, "selected generated roots"):
            build_inventory(
                state=self.state,
                commit="abc123",
                tracked_paths=["docs-v3-current/index.md"],
                untracked_paths=[],
            )


if __name__ == "__main__":
    unittest.main()
