from __future__ import annotations

import json
import unittest
from pathlib import Path

from lower_face_supports import analyze_document


HERE = Path(__file__).resolve().parent
EXACT_DATA = HERE / "fixtures" / "degree21_exact_data.json"


class LowerFaceSupportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        document = json.loads(EXACT_DATA.read_text(encoding="utf-8"))
        cls.report = analyze_document(document)
        cls.cases = {case["label"]: case for case in cls.report["cases"]}

    def test_leading_face_supports_match_zp_and_z2q(self) -> None:
        for case in self.report["cases"]:
            layers = {layer["r"]: layer for layer in case["layers"]}
            self.assertEqual(layers[0]["a_support"], list(range(1, 9)))
            self.assertEqual(layers[0]["b_support"], list(range(2, 13)))

    def test_archived_normal_depths_are_distinct(self) -> None:
        self.assertEqual(self.cases["truncated"]["minimum_layer"], 0)
        self.assertEqual(self.cases["truncated"]["maximum_layer"], 3)
        self.assertEqual(self.cases["full"]["minimum_layer"], 0)
        self.assertEqual(self.cases["full"]["maximum_layer"], 15)

    def test_full_layer_one_through_four_windows(self) -> None:
        layers = {
            layer["r"]: layer for layer in self.cases["full"]["layers"]
        }
        self.assertEqual(layers[1]["a_support"], list(range(1, 9)))
        self.assertEqual(layers[1]["b_support"], list(range(2, 13)))
        self.assertEqual(layers[2]["a_support"], list(range(0, 9)))
        self.assertEqual(layers[2]["b_support"], list(range(1, 13)))
        self.assertEqual(layers[3]["a_support"], list(range(0, 8)))
        self.assertEqual(layers[3]["b_support"], list(range(0, 13)))
        self.assertEqual(layers[4]["a_support"], list(range(0, 7)))
        self.assertEqual(layers[4]["b_support"], list(range(0, 12)))

    def test_every_case_contains_all_archived_points(self) -> None:
        self.assertEqual(self.cases["truncated"]["P_point_count"], 25)
        self.assertEqual(self.cases["truncated"]["Q_point_count"], 47)
        self.assertEqual(self.cases["full"]["P_point_count"], 61)
        self.assertEqual(self.cases["full"]["Q_point_count"], 125)


if __name__ == "__main__":
    unittest.main()
