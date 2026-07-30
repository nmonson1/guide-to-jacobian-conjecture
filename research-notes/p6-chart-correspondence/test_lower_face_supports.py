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

    def test_leading_face_supports_match_zp_and_z2q(self) -> None:
        for case in self.report["cases"]:
            layers = {layer["r"]: layer for layer in case["layers"]}
            self.assertEqual(layers[0]["a_support"], list(range(1, 9)))
            self.assertEqual(layers[0]["b_support"], list(range(2, 13)))

    def test_all_archived_points_roundtrip(self) -> None:
        for case in self.report["cases"]:
            self.assertGreater(case["P_point_count"], 0)
            self.assertGreater(case["Q_point_count"], 0)
            self.assertEqual(case["minimum_layer"], 0)
            self.assertGreaterEqual(case["maximum_layer"], 4)


if __name__ == "__main__":
    unittest.main()
