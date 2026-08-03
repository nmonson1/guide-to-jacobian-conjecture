#!/usr/bin/env python3
"""Regression tests for the Lane 9 Kummer attachment audit."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import lane9_kummer_attachment as audit


class Lane9KummerAttachmentTests(unittest.TestCase):
    def test_exact_report(self) -> None:
        report = audit.build_report()
        self.assertTrue(report["all_exact_checks_passed"])
        self.assertEqual(
            report["lattice_and_stabilizer"]["quotient_coordinates"]["determinant"],
            -8,
        )
        self.assertFalse(
            report["old_window_comparison"][
                "coefficientwise_match_without_overlap_normalization"
            ]
        )
        self.assertEqual(
            report["cyclic_descent"]["parameter_bidegree"], [-3, 4]
        )

    def test_deterministic_json_round_trip(self) -> None:
        report = audit.build_report()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report.json"
            output.write_text(
                json.dumps(report, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            loaded = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(loaded, report)

    def test_bracket_formula(self) -> None:
        result = audit.bracket_checks()["formula"]
        self.assertEqual(
            result["f_11"], "18*c0*z^-4+30*c1*z^-3+42*z^-2"
        )
        self.assertEqual(result["g_11"], "6*c0*z^-5+5*c1*z^-4")


if __name__ == "__main__":
    unittest.main()
