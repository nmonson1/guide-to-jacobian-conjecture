#!/usr/bin/env python3
"""Regression tests for the exact F2 terminal quotient face."""

from __future__ import annotations

import unittest

import lane9_f2_terminal_face as face


class Lane9F2TerminalFaceTests(unittest.TestCase):
    def test_normalized_face_and_ode(self) -> None:
        report = face.build_report()
        self.assertTrue(report["all_exact_checks_passed"])
        self.assertEqual(report["lattice_gap"], 5)
        self.assertEqual(report["quotient_coordinate"], "u=z^5")
        self.assertEqual(report["normalized_face"]["pbar"], "1-u")
        self.assertEqual(
            report["normalized_face"]["qbar"], "(9*u^2-15*u+5)/25"
        )
        self.assertEqual(report["normalized_face"]["ode_value"], "1/5")

    def test_terminal_face_linearization(self) -> None:
        linearization = face.build_report()["terminal_face_linearization"]
        self.assertEqual(
            linearization["matrix"],
            [["6/5", "-2", "0"], ["-9/5", "-3", "-5"]],
        )
        self.assertEqual(
            linearization["integer_scaled_matrix"],
            [[6, -10, 0], [-9, -15, -25]],
        )
        self.assertEqual(linearization["rank"], 2)
        self.assertEqual(linearization["kernel_dimension"], 1)
        self.assertEqual(
            linearization["kernel_generator"], ["-1", "-3/5", "18/25"]
        )

    def test_degree_six_belyi_data(self) -> None:
        report = face.build_report()
        belyi = report["belyi_map"]
        self.assertEqual(belyi["degree"], 6)
        self.assertEqual(
            belyi["passport"], ["(5,1)", "(3,3)", "(3,1,1,1)"]
        )
        self.assertEqual(
            belyi["tau_minus_one_finite_numerator"],
            "135*u^3-405*u^2+396*u-125",
        )

    def test_coefficient_reconstruction_equations(self) -> None:
        report = face.build_report()
        self.assertEqual(
            report["coefficient_equations"],
            ["a*c=1/5", "a*d=3*b*c", "5*a*e=3*b*d"],
        )


if __name__ == "__main__":
    unittest.main()
