from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
EXAMPLE = HERE.parent / "examples" / "two_chart_rational.json"
sys.path.insert(0, str(ROOT))

from filtered_operation_complex import ContractError, analyze_document  # noqa: E402


class FilteredOperationComplexTests(unittest.TestCase):
    def rational_contract(self) -> dict:
        return json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def test_rational_hierarchy_rechart_and_transport(self) -> None:
        report = analyze_document(self.rational_contract())
        self.assertTrue(report["all_transitions_verified"])
        self.assertFalse(report["all_true_quotients_zero"])
        self.assertFalse(report["all_forcing_equations_solvable"])
        for layer in report["layers"]:
            self.assertEqual(layer["kernel_dimension"], 3)
            self.assertEqual(layer["cokernel_dimension"], 1)
            self.assertEqual(layer["gauge_dimension"], 1)
            self.assertEqual(layer["rechart_increment"], 1)
            self.assertEqual(layer["unexplained_dimension"], 1)
            self.assertEqual(layer["forcing_pairings"], ["1"])
            self.assertFalse(layer["forcing_solvable"])
            self.assertIsNone(layer["affine_solution_dimension"])
            self.assertEqual(
                layer["complete_left_null_forcing_pairings"],
                ["1"],
            )

            actions = {entry["name"]: entry for entry in layer["actions"]}
            self.assertEqual(
                (
                    actions["formal"]["source_dimension"],
                    actions["formal"]["rank"],
                    actions["formal"]["source_stabilizer_dimension"],
                ),
                (4, 3, 1),
            )
            self.assertEqual(
                (
                    actions["polynomial"]["source_dimension"],
                    actions["polynomial"]["rank"],
                    actions["polynomial"]["source_stabilizer_dimension"],
                ),
                (3, 2, 1),
            )
            self.assertEqual(
                (
                    actions["filtered"]["source_dimension"],
                    actions["filtered"]["rank"],
                    actions["filtered"]["source_stabilizer_dimension"],
                ),
                (2, 1, 1),
            )

        transition = report["transitions"][0]
        self.assertEqual(len(transition["operation_map_checks"]), 3)
        self.assertTrue(
            all(
                item["action_square_verified"]
                and item["source_stabilizer_transport_verified"]
                for item in transition["operation_map_checks"]
            )
        )
        self.assertEqual(
            transition["rechart_span_checks"][0]["transported_rank"],
            1,
        )
        quotient = transition["true_quotient_check"]
        self.assertTrue(quotient["explained_space_transport_verified"])
        self.assertEqual(quotient["induced_quotient_rank"], 1)
        self.assertTrue(quotient["isomorphism_required"])
        self.assertTrue(
            transition["forcing_check"]["dual_pairings_preserved"]
        )
        self.assertEqual(transition["forcing_check"]["pairings"], ["1"])

    def test_solvable_affine_forcing_returns_particular_solution(self) -> None:
        contract = {
            "schema_version": 1,
            "field": {"kind": "rational"},
            "report_options": {"include_vectors": True},
            "layers": [
                {
                    "id": "solvable-affine-layer",
                    "deformation_dimension": 2,
                    "equation_dimension": 1,
                    "operator": [[1, 0]],
                    "forcing": [-2],
                }
            ],
        }
        report = analyze_document(contract)
        layer = report["layers"][0]
        self.assertTrue(report["all_forcing_equations_solvable"])
        self.assertTrue(layer["forcing_solvable"])
        self.assertTrue(layer["forcing_compatibility_verified"])
        self.assertEqual(layer["affine_solution_dimension"], 1)
        self.assertEqual(layer["particular_solution"], ["2", "0"])
        self.assertEqual(layer["complete_left_null_forcing_pairings"], [])

    def test_generator_form_also_reports_source_stabilizer(self) -> None:
        contract = {
            "schema_version": 1,
            "field": {"kind": "rational"},
            "layers": [
                {
                    "id": "dependent-generators",
                    "deformation_dimension": 2,
                    "equation_dimension": 1,
                    "operator": [[1, 0]],
                    "actions": [
                        {
                            "name": "filtered",
                            "role": "filtered",
                            "generators": [[0, 1], [0, 1]],
                        }
                    ],
                    "gauge_actions": ["filtered"],
                }
            ],
        }
        action = analyze_document(contract)["layers"][0]["actions"][0]
        self.assertEqual(action["input_form"], "generators")
        self.assertEqual(action["source_dimension"], 2)
        self.assertEqual(action["rank"], 1)
        self.assertEqual(action["source_stabilizer_dimension"], 1)

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
        self.assertIsNone(report["all_forcing_equations_solvable"])
        self.assertEqual(
            layer["actions"][0]["source_stabilizer_dimension"],
            0,
        )

    def test_rejects_non_kernel_operation(self) -> None:
        contract = self.rational_contract()
        contract["layers"][0]["actions"][2]["action_matrix"][0][0] = 1
        with self.assertRaises(ContractError):
            analyze_document(contract)

    def test_rejects_false_parent_inclusion(self) -> None:
        contract = self.rational_contract()
        contract["layers"][0]["actions"][0] = {
            "name": "formal",
            "role": "formal",
            "source_dimension": 1,
            "source_basis": ["F0"],
            "action_matrix": [[0], [1], [0], [0]],
        }
        with self.assertRaises(ContractError):
            analyze_document(contract)

    def test_rejects_false_operation_transport_square(self) -> None:
        contract = self.rational_contract()
        contract["transitions"][0]["operation_map_pairs"][2]["source_map"] = [
            [0, 0],
            [0, 0],
        ]
        with self.assertRaises(ContractError):
            analyze_document(contract)

    def test_action_requires_exactly_one_input_form(self) -> None:
        contract = self.rational_contract()
        contract["layers"][0]["actions"][0]["generators"] = [[0, 1, 0, 0]]
        with self.assertRaises(ContractError):
            analyze_document(contract)

    def test_json_roundtrip(self) -> None:
        document = json.loads(json.dumps(self.rational_contract()))
        self.assertEqual(analyze_document(document)["schema_version"], 1)


if __name__ == "__main__":
    unittest.main()
