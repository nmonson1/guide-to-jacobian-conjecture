#!/usr/bin/env python3
"""Regression tests for the parameter-complete F2 recurrence auditor."""

from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path

import lane9_f2_attachment_recurrence as recurrence

HERE = Path(__file__).resolve().parent


class Lane9F2AttachmentRecurrenceTests(unittest.TestCase):
    def test_synthetic_slice_dependence(self) -> None:
        contract = json.loads(
            (HERE / "synthetic_f2_parameter_retention_contract.json").read_text(
                encoding="utf-8"
            )
        )
        report = recurrence.audit_contract(contract)
        self.assertTrue(report["all_full_parameter_systems_consistent"])
        self.assertEqual(
            [order["order"] for order in report["orders"]],
            [510, 520, 530],
        )
        self.assertTrue(
            all(
                order["any_slice_dependent_apparent_obstruction"]
                for order in report["orders"]
            )
        )

    def test_exact_obstruction_certificate(self) -> None:
        diagnostic = recurrence.solve_diagnostics(
            [[Fraction(0)]],
            [Fraction(1)],
            column_count=1,
        )
        self.assertFalse(diagnostic["consistent"])
        self.assertEqual(
            diagnostic["nonzero_obstruction_certificates"][0][
                "pairing_with_rhs"
            ],
            "1",
        )

    def test_character_validation(self) -> None:
        bad_contract = {
            "schema_version": 1,
            "cyclic_modulus": 5,
            "orders": [
                {
                    "order": 1,
                    "blocks": [
                        {
                            "character": 0,
                            "variables": [
                                {
                                    "name": "p",
                                    "kind": "fresh_parameter",
                                    "character": 1,
                                }
                            ],
                            "equations": ["e"],
                            "matrix": [[1]],
                            "rhs": [0],
                        }
                    ],
                }
            ],
        }
        with self.assertRaises(ValueError):
            recurrence.audit_contract(bad_contract)

    def test_zero_equation_block_retains_variable_dimension(self) -> None:
        contract = {
            "schema_version": 1,
            "cyclic_modulus": 5,
            "orders": [
                {
                    "order": 1,
                    "blocks": [
                        {
                            "character": 2,
                            "variables": [
                                {
                                    "name": "p",
                                    "kind": "fresh_parameter",
                                    "character": 2,
                                }
                            ],
                            "equations": [],
                            "matrix": [],
                            "rhs": [],
                        }
                    ],
                }
            ],
        }
        block = recurrence.audit_contract(contract)["orders"][0]["blocks"][0]
        self.assertEqual(
            block["full_parameter_system"]["solution_dimension"], 1
        )


if __name__ == "__main__":
    unittest.main()
