from __future__ import annotations

import json
import unittest
from pathlib import Path

from degree21_linear_replay import audit_document, reconstruct_matrix


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


class Degree21LinearReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.document = json.loads(EXACT_DATA.read_text(encoding="utf-8"))

    def test_all_archived_layers_replay_exactly(self) -> None:
        report = audit_document(self.document)
        self.assertTrue(report["all_layers_verified"])
        self.assertEqual(len(report["layers"]), 24)

    def test_truncated_layer_four(self) -> None:
        layer = self.document["truncated"]["layers"][3]
        matrix = reconstruct_matrix(layer)
        self.assertEqual(len(matrix), 5)
        self.assertEqual(len(matrix[0]), 7)
        audit = audit_document(self.document)["layers"][3]
        self.assertEqual(
            (audit["rank"], audit["kernel_dimension"], audit["cokernel_dimension"]),
            (3, 4, 2),
        )

    def test_full_layer_four(self) -> None:
        layer = self.document["full"]["layers"][3]
        matrix = reconstruct_matrix(layer)
        self.assertEqual(len(matrix), 10)
        self.assertEqual(len(matrix[0]), 15)
        audits = audit_document(self.document)["layers"]
        audit = next(item for item in audits if item["case"] == "full" and item["r"] == 4)
        self.assertEqual(
            (audit["rank"], audit["kernel_dimension"], audit["cokernel_dimension"]),
            (7, 8, 3),
        )


if __name__ == "__main__":
    unittest.main()
