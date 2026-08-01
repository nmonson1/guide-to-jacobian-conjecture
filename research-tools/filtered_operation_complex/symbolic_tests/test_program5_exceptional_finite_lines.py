from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH_TOOLS = HERE.parent.parent
sys.path.insert(0, str(RESEARCH_TOOLS))

from filtered_operation_complex.adapters.program5_rank_six_exceptional_finite_lines import (  # noqa: E402
    analyze_exceptional_finite_lines,
)


class Program5ExceptionalFiniteLineTests(unittest.TestCase):
    def test_all_pairing_ideal_roots_are_specialized_exactly(self) -> None:
        result = analyze_exceptional_finite_lines()

        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(
            result["source_sha256"],
            "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        )
        self.assertEqual(result["exceptional_ratio_count"], 3)
        ratios = result["exceptional_ratios"]
        self.assertEqual(len(ratios), 3)
        self.assertTrue(result["conjugate_rank_profiles_equal"])
        for item in ratios:
            self.assertEqual(
                item["cubic_lift_solvable"],
                item["cubic_effect_rank"]
                == item["cubic_augmented_rank"],
            )
        self.assertEqual(
            result["all_exceptional_finite_ratios_obstructed"],
            all(not item["cubic_lift_solvable"] for item in ratios),
        )
        self.assertEqual(
            result["finite_selected_plane_closed_at_cubic_order"],
            result["all_exceptional_finite_ratios_obstructed"],
        )

        print(
            json.dumps(
                {
                    "generic_pairing_polynomial": result[
                        "generic_pairing_polynomial"
                    ],
                    "exceptional_ratios": [
                        {
                            "label": item["label"],
                            "field": item["field"],
                            "rank": item["cubic_effect_rank"],
                            "augmented_rank": item[
                                "cubic_augmented_rank"
                            ],
                            "solvable": item["cubic_lift_solvable"],
                        }
                        for item in ratios
                    ],
                    "finite_selected_plane_closed": result[
                        "finite_selected_plane_closed_at_cubic_order"
                    ],
                },
                indent=2,
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    unittest.main()
