from __future__ import annotations

import json
import unittest
from pathlib import Path

from degree21_kernel_decomposition import audit_document


HERE = Path(__file__).resolve().parent
EXACT_DATA = (
    HERE
    / "archive-scan"
    / "selected"
    / "06-plane-boundary-computational-supplement"
    / "computational-supplement"
    / "degree-twenty-one"
    / "exact_data.json"
)


class Degree21KernelDecompositionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        document = json.loads(EXACT_DATA.read_text(encoding="utf-8"))
        cls.report = audit_document(document)

    def test_all_factorizations_and_kernel_odes(self) -> None:
        self.assertTrue(self.report["all_layers_verified"])
        self.assertEqual(len(self.report["layers"]), 24)

    def test_only_arithmetic_resonances_have_exceptional_defect(self) -> None:
        observed = {
            (item["case"], item["r"], item["dimension"])
            for item in self.report["exceptional_layers"]
        }
        expected = {
            (case, r, 1)
            for case in ("truncated", "full")
            for r in (4, 8, 12)
        }
        self.assertEqual(observed, expected)

    def test_layer_four_quotient_is_one_dimensional(self) -> None:
        layer_four = {
            item["case"]: item
            for item in self.report["layers"]
            if item["r"] == 4
        }
        self.assertEqual(layer_four["truncated"]["common_root_dimension"], 3)
        self.assertEqual(layer_four["full"]["common_root_dimension"], 7)
        self.assertEqual(layer_four["truncated"]["exceptional_dimension"], 1)
        self.assertEqual(layer_four["full"]["exceptional_dimension"], 1)
        self.assertEqual(layer_four["truncated"]["resonance_exponent"], 2)
        self.assertEqual(layer_four["full"]["resonance_exponent"], 2)
        self.assertEqual(
            layer_four["truncated"]["normalized_exceptional"]["defect"],
            layer_four["full"]["normalized_exceptional"]["defect"],
        )


if __name__ == "__main__":
    unittest.main()
