#!/usr/bin/env python3
"""Tests for the public Lane 9 archive recovery utility."""

from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

import recover_lane9_public_archive as recovery


class RecoverLane9ArchiveTests(unittest.TestCase):
    def test_scan_and_extract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / "packet.zip"
            prefix = "bundle/computational-supplement/terminal-boundary/"
            with zipfile.ZipFile(archive, "w") as handle:
                handle.writestr(
                    prefix + "F2_degree125_boundary_seed.md",
                    "F_2 complete-chain seed with C_5 quotient.\n",
                )
                handle.writestr(
                    "bundle/computational-supplement/hidden/order_probe.py",
                    "# fresh parameters at order 520 and a support block\n",
                )
                handle.writestr(
                    "bundle/computational-supplement/hidden/f2_blocks.json",
                    '{"name":"F2 endpoint matrix block"}\n',
                )
                handle.writestr(
                    "bundle/computational-supplement/unrelated/readme.md",
                    "nothing relevant\n",
                )
            output_dir = root / "recovered"
            manifest = root / "manifest.json"
            report = recovery.recover(archive, output_dir, manifest)
            self.assertEqual(report["extracted_member_count"], 3)
            self.assertEqual(report["high_order_endpoint_candidate_count"], 2)
            self.assertTrue(
                (output_dir / "terminal-boundary/F2_degree125_boundary_seed.md").is_file()
            )
            self.assertTrue((output_dir / "hidden/order_probe.py").is_file())
            self.assertTrue((output_dir / "hidden/f2_blocks.json").is_file())

    def test_sha_pin(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / "packet.zip"
            with zipfile.ZipFile(archive, "w") as handle:
                handle.writestr("x.txt", "F2")
            with self.assertRaises(ValueError):
                recovery.recover(
                    archive,
                    root / "out",
                    root / "manifest.json",
                    expected_sha256="0" * 64,
                )


if __name__ == "__main__":
    unittest.main()
