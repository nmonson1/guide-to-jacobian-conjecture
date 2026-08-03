from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from prepare_living_guide_tree_v1 import copy_static_entry  # noqa: E402


class LivingGuideScaffoldTests(unittest.TestCase):
    def test_copy_static_entry_materializes_directory_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            historical = root / "historical"
            historical.mkdir()
            (historical / "asset.txt").write_text("asset", encoding="utf-8")
            source = root / "current" / "assets"
            source.parent.mkdir()
            source.symlink_to(historical, target_is_directory=True)
            target = root / "candidate" / "assets"

            self.assertEqual(copy_static_entry(source, target), 1)
            self.assertFalse(target.is_symlink())
            self.assertEqual(
                (target / "asset.txt").read_text(encoding="utf-8"), "asset"
            )


if __name__ == "__main__":
    unittest.main()
