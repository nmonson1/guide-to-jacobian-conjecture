from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH_TOOLS = HERE.parent.parent
sys.path.insert(0, str(RESEARCH_TOOLS))

from filtered_operation_complex.adapters.program5_rank_six_infinity_fibre_formal_scan import (  # noqa: E402
    analyze_infinity_fibre_formal_scan,
)


class Program5InfinityFibreFormalScanTests(unittest.TestCase):
    def test_coordinate_samples_are_lifted_through_order_four(self) -> None:
        result = analyze_infinity_fibre_formal_scan(max_order=4)

        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(
            result["source_sha256"],
            "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        )
        self.assertEqual(result["infinity_fibre_dimension"], 18)
        self.assertEqual(result["sample_count"], 19)
        self.assertEqual(len(result["samples"]), 19)

        by_name = {item["name"]: item for item in result["samples"]}
        base = by_name["infinity:base"]
        self.assertEqual(base["first_obstructed_order"], 4)
        self.assertEqual(base["maximum_compatible_order"], 3)
        self.assertEqual(base["direct_effect_columns_verified"], 22)
        self.assertEqual(
            base["obstruction_certificate"]["pairing_with_rhs"],
            "1/2",
        )

        xi5 = by_name["infinity:+xi_5"]
        self.assertEqual(xi5["first_obstructed_order"], 3)
        self.assertEqual(xi5["maximum_compatible_order"], 2)

        for sample in result["samples"]:
            obstruction = sample["first_obstructed_order"]
            if obstruction is None:
                self.assertEqual(sample["maximum_compatible_order"], 4)
            else:
                self.assertEqual(
                    sample["maximum_compatible_order"],
                    obstruction - 1,
                )
                self.assertNotEqual(
                    sample["obstruction_certificate"]["pairing_with_rhs"],
                    0,
                )

        print(
            json.dumps(
                {
                    "first_obstruction_histogram": result[
                        "first_obstruction_histogram"
                    ],
                    "survivor_count": result["survivor_count"],
                    "survivors": result[
                        "survivors_through_requested_order"
                    ],
                    "profiles": [
                        {
                            "name": sample["name"],
                            "maximum_compatible_order": sample[
                                "maximum_compatible_order"
                            ],
                            "first_obstructed_order": sample[
                                "first_obstructed_order"
                            ],
                            "fixed_effect_rank": sample[
                                "fixed_tangent_effect_rank"
                            ],
                            "pairing": sample.get(
                                "obstruction_certificate", {}
                            ).get("pairing_with_rhs"),
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
