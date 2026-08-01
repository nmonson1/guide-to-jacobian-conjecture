from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH_TOOLS = HERE.parent.parent
sys.path.insert(0, str(RESEARCH_TOOLS))

from filtered_operation_complex.adapters.program5_rank_six_first_order_base_scan import (  # noqa: E402
    analyze_first_order_base_scan,
)


class Program5FirstOrderBaseScanTests(unittest.TestCase):
    def test_row_base_coordinate_samples_are_audited(self) -> None:
        result = analyze_first_order_base_scan()

        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(
            result["source_sha256"],
            "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        )
        self.assertEqual(result["finite_fibre_dimension"], 15)
        self.assertEqual(result["infinity_fibre_dimension"], 18)
        self.assertEqual(result["sample_count"], len(result["samples"]))
        self.assertEqual(
            result["second_order_compatible_count"],
            result["sample_count"],
        )
        for sample in result["samples"]:
            self.assertTrue(sample["second_order_compatible"])
            self.assertEqual(
                sample["cubic_lift_solvable"],
                sample["cubic_effect_rank"]
                == sample["cubic_augmented_rank"],
            )

        print(
            json.dumps(
                {
                    "sample_count": result["sample_count"],
                    "cubic_solvable_count": result["cubic_solvable_count"],
                    "cubic_solvable_samples": result[
                        "cubic_solvable_samples"
                    ],
                    "rank_profiles": [
                        {
                            "name": sample["name"],
                            "rank": sample["cubic_effect_rank"],
                            "augmented_rank": sample[
                                "cubic_augmented_rank"
                            ],
                            "solvable": sample["cubic_lift_solvable"],
                        }
                        for sample in result["samples"]
                    ],
                },
                indent=2,
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    unittest.main()
