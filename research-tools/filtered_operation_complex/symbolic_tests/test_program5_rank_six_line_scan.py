from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH_TOOLS = HERE.parent.parent
sys.path.insert(0, str(RESEARCH_TOOLS))

from filtered_operation_complex.adapters.program5_rank_six_line_scan import (  # noqa: E402
    analyze_line_scan,
)


class Program5RankSixLineScanTests(unittest.TestCase):
    def test_selected_projective_lines_are_audited_exactly(self) -> None:
        ratios = (-2, -1, 0, 1, 2, 3, 4, 5)
        result = analyze_line_scan(ratios=ratios, verify_axes=True)

        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(
            result["source_sha256"],
            "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        )
        self.assertEqual(result["ambient_operation_dimension"], 115)
        self.assertEqual(result["rank_six_tangent_dimension"], 22)

        directions = result["finite_ratio_results"] + [result["infinity_result"]]
        self.assertEqual(len(directions), len(ratios) + 1)
        for direction in directions:
            self.assertTrue(direction["second_order_compatible"])
            self.assertEqual(direction["quadratic_tangent_freedom_dimension"], 22)
            self.assertEqual(
                direction["cubic_lift_solvable"],
                direction["cubic_effect_rank"]
                == direction["cubic_augmented_rank"],
            )
            if direction["cubic_lift_solvable"]:
                self.assertEqual(direction["maximum_compatible_order"], 3)
                self.assertIsNotNone(
                    direction["cubic_lift_solution_free_dimension"]
                )
            else:
                self.assertEqual(direction["first_obstructed_order"], 3)
                certificate = direction["cubic_obstruction_certificate"]
                self.assertNotEqual(certificate["pairing_with_rhs"], 0)
                self.assertGreater(certificate["nonzero_count"], 0)

        ratio_zero = next(
            item
            for item in result["finite_ratio_results"]
            if item["u_over_v"] == 0
        )
        self.assertEqual(ratio_zero["direct_effect_columns_verified"], 22)
        self.assertEqual(
            result["infinity_result"]["direct_effect_columns_verified"],
            22,
        )

        print(
            json.dumps(
                {
                    "finite": [
                        {
                            "u_over_v": str(item["u_over_v"]),
                            "rank": item["cubic_effect_rank"],
                            "augmented_rank": item["cubic_augmented_rank"],
                            "solvable": item["cubic_lift_solvable"],
                            "pairing": item.get(
                                "cubic_obstruction_certificate", {}
                            ).get("pairing_with_rhs"),
                            "witness_sha256": item.get(
                                "cubic_obstruction_certificate", {}
                            ).get("witness_sha256"),
                        }
                        for item in result["finite_ratio_results"]
                    ],
                    "infinity": {
                        "rank": result["infinity_result"]["cubic_effect_rank"],
                        "augmented_rank": result["infinity_result"][
                            "cubic_augmented_rank"
                        ],
                        "solvable": result["infinity_result"][
                            "cubic_lift_solvable"
                        ],
                        "pairing": result["infinity_result"].get(
                            "cubic_obstruction_certificate", {}
                        ).get("pairing_with_rhs"),
                    },
                },
                indent=2,
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    unittest.main()
