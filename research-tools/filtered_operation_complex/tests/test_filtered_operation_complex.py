from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT))

from filtered_operation_complex import ContractError, analyze_document  # noqa: E402


class FilteredOperationComplexTests(unittest.TestCase):
    def rational_contract(self) -> dict:
        return {
            "schema_version": 1,
            "name": "two-chart rational regression",
            "field": {"kind": "rational"},
            "report_options": {"include_vectors": True},
            "layers": [
                {
                    "id": "C:r4",
                    "deformation_dimension": 4,
                    "equation_dimension": 2,
                    "operator": [[1, 0, 0, 0], [0, 0, 0, 0]],
                    "actions": [
                        {
                            "name": "formal",
                            "role": "formal",
                            "generators": [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
                        },
                        {
                            "name": "polynomial",
                            "role": "polynomial",
                            "parent": "formal",
                            "generators": [[0, 1, 0, 0], [0, 0, 1, 0]],
                        },
                        {
                            "name": "filtered",
                            "role": "filtered",
                            "parent": "polynomial",
                            "generators": [[0, 1, 0, 0]],
                        },
                    ],
                    "gauge_actions": ["filtered"],
                    "recharts": [
                        {"name": "wall", "generators": [[0, 0, 1, 0]]}
                    ],
                    "forcing": [0, 1],
                    "obstruction_functionals": [[0, 1]],
                },
                {
                    "id": "Cprime:r4",
                    "deformation_dimension": 4,
                    "equation_dimension": 2,
                    "operator": [[1, 0, 0, 0], [0, 0, 0, 0]],
                    "actions": [
                        {
                            "name": "formal",
                            "role": "formal",
                            "generators": [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
                        },
                        {
                            "name": "polynomial",
                            "role": "polynomial",
                            "parent": "formal",
                            "generators": [[0, 1, 0, 0], [0, 0, 1, 0]],
                        },
                        {
                            "name": "filtered",
                            "role": "filtered",
                            "parent": "polynomial",
                            "generators": [[0, 0, 1, 0]],
                        },
                    ],
                    "gauge_actions": ["filtered"],
                    "recharts": [
                        {"name": "wall-inverse", "generators": [[0, 1, 0, 0]]}
                    ],
                    "forcing": [0, 1],
                    "obstruction_functionals": [[0, 1]],
                },
            ],
            "transitions": [
                {
                    "name": "swap-wall-coordinates",
                    "from": "C:r4",
                    "to": "Cprime:r4",
                    "deformation_map": [
                        [1, 0, 0, 0],
                        [0, 0, 1, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 1],
                    ],
                    "equation_map": [[1, 0], [0, 1]],
                    "require_isomorphism": True,
                    "operation_span_pairs": [
                        {"from": "formal", "to": "formal"},
                        {"from": "filtered", "to": "filtered"},
                    ],
                    "dual_pairs": [{"from": [0, 1], "to": [0, 1]}],
                    "forcing_pair": {"from": [0, 1], "to": [0, 1]},
                }
            ],
        }

    def test_rational_hierarchy_rechart_and_transport(self) -> None:
        report = analyze_document(self.rational_contract())
        self.assertTrue(report["all_transitions_verified"])
        self.assertFalse(report["all_true_quotients_zero"])
        for layer in report["layers"]:
            self.assertEqual(layer["kernel_dimension"], 3)
            self.assertEqual(layer["cokernel_dimension"], 1)
            self.assertEqual(layer["gauge_dimension"], 1)
            self.assertEqual(layer["rechart_increment"], 1)
            self.assertEqual(layer["unexplained_dimension"], 1)
            self.assertEqual(layer["forcing_pairings"], ["1"])
        transition = report["transitions"][0]
        self.assertTrue(transition["forcing_check"]["dual_pairings_preserved"])
        self.assertEqual(transition["forcing_check"]["pairings"], ["1"])

    def test_number_field_contract(self) -> None:
        contract = {
            "schema_version": 1,
            "field": {
                "kind": "number_field",
                "modulus": [-2, 0, 1],
                "symbol": "u",
            },
            "layers": [
                {
                    "id": "quadratic-field",
                    "deformation_dimension": 2,
                    "equation_dimension": 1,
                    "operator": [[[0, 1], [1, 0]]],
                    "actions": [
                        {
                            "name": "filtered",
                            "role": "filtered",
                            "generators": [[[1, 0], [0, -1]]],
                        }
                    ],
                    "gauge_actions": ["filtered"],
                }
            ],
        }
        report = analyze_document(contract)
        layer = report["layers"][0]
        self.assertEqual(layer["kernel_dimension"], 1)
        self.assertEqual(layer["gauge_dimension"], 1)
        self.assertEqual(layer["unexplained_dimension"], 0)
        self.assertTrue(report["all_true_quotients_zero"])

    def test_rejects_non_kernel_operation(self) -> None:
        contract = self.rational_contract()
        contract["layers"][0]["actions"][2]["generators"] = [[1, 0, 0, 0]]
        with self.assertRaises(ContractError):
            analyze_document(contract)

    def test_rejects_false_parent_inclusion(self) -> None:
        contract = self.rational_contract()
        contract["layers"][0]["actions"][1]["generators"] = [[0, 0, 0, 1]]
        contract["layers"][0]["actions"][0]["generators"] = [[0, 1, 0, 0]]
        with self.assertRaises(ContractError):
            analyze_document(contract)

    def test_json_roundtrip(self) -> None:
        document = json.loads(json.dumps(self.rational_contract()))
        self.assertEqual(analyze_document(document)["schema_version"], 1)


if __name__ == "__main__":
    unittest.main()
