from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from inventory_generated_recoverability import directory_record  # noqa: E402
from archive_generated_candidates import archive  # noqa: E402


class GeneratedRecoverabilityTests(unittest.TestCase):
    def test_directory_record_is_stable_and_path_relative(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "nested").mkdir()
            (root / "a.txt").write_text("alpha", encoding="utf-8")
            (root / "nested" / "b.txt").write_text("beta", encoding="utf-8")
            result = directory_record(root)
        expected = hashlib.sha256(
            (
                "a.txt\x00file\x005\x00"
                + hashlib.sha256(b"alpha").hexdigest()
                + "\nnested/b.txt\x00file\x004\x00"
                + hashlib.sha256(b"beta").hexdigest()
                + "\n"
            ).encode()
        ).hexdigest()
        self.assertEqual(
            result,
            {
                "file_count": 2,
                "symlink_count": 0,
                "apparent_size_bytes": 9,
                "content_tree_sha256": expected,
            },
        )

    def test_archive_copies_only_unique_roots_and_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            (source / "docs-v1").mkdir(parents=True)
            (source / "docs-v2").mkdir()
            (source / "docs-v1" / "index.md").write_text("one", encoding="utf-8")
            (source / "docs-v1" / "current.md").symlink_to("index.md")
            (source / "docs-v2" / "index.md").write_text("two", encoding="utf-8")
            inventory = root / "inventory.json"
            inventory.write_text(
                """{
                  "baseline_commit": "abc123",
                  "inventory_id": "test-inventory",
                  "untracked_generated": {
                    "unique_root_count": 1,
                    "roots": [
                      {"path": "docs-v1", "requires_external_archive_before_removal": true},
                      {"path": "docs-v2", "requires_external_archive_before_removal": false}
                    ]
                  }
                }""",
                encoding="utf-8",
            )
            destination = root / "archive"
            manifest = archive(
                inventory_path=inventory,
                source_root=source,
                destination=destination,
            )
            self.assertEqual(manifest["copied_roots"], ["docs-v1"])
            self.assertTrue((destination / "docs-v1" / "index.md").is_file())
            self.assertTrue((destination / "docs-v1" / "current.md").is_symlink())
            self.assertEqual((destination / "docs-v1" / "current.md").readlink(), Path("index.md"))
            self.assertFalse((destination / "docs-v2").exists())
            with self.assertRaises(FileExistsError):
                archive(
                    inventory_path=inventory,
                    source_root=source,
                    destination=destination,
                )


if __name__ == "__main__":
    unittest.main()
