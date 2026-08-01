from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH_TOOLS = HERE.parent.parent
sys.path.insert(0, str(RESEARCH_TOOLS))

from filtered_operation_complex.adapters.program5_rank_six_line_formal_arc import (  # noqa: E402
    analyze_line_formal_arc,
)


class Program5RankSixLineFormalArcTests(unittest.TestCase):
    def test_theta_u_is_lifted_until_an_exact_obstruction_or_order_eight(self) -> None:
        result = analyze_line_formal_arc(
            ratio=None,
            max_order=8,
            verify_effect=True,
        )

        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(
            result["source_sha256"],
            "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        )
        self.assertEqual(result["direction"], "theta_u")
        self.assertEqual(result["u_over_v"], "infinity")
        self.assertEqual(result["rank_six_tangent_dimension"], 22)
        self.assertEqual(result["direct_effect_columns_verified"], 22)
        self.assertGreaterEqual(result["maximum_compatible_order"], 3)

        first_obstructed = result["first_obstructed_order"]
        if first_obstructed is None:
            self.assertEqual(result["maximum_compatible_order"], 8)
        else:
            self.assertGreaterEqual(first_obstructed, 4)
            self.assertEqual(
                result["maximum_compatible_order"],
                first_obstructed - 1,
            )
            certificate = result["obstruction_certificate"]
            self.assertEqual(certificate["order"], first_obstructed)
            self.assertNotEqual(certificate["pairing_with_rhs"], 0)
            self.assertGreater(certificate["nonzero_count"], 0)

        print(
            json.dumps(
                {
                    "fixed_tangent_effect_rank": result[
                        "fixed_tangent_effect_rank"
                    ],
                    "maximum_compatible_order": result[
                        "maximum_compatible_order"
                    ],
                    "first_obstructed_order": first_obstructed,
                    "order_data": [
                        {
                            "order": item["order"],
                            "compatible": item["compatible"],
                            "effect_rank": item.get("effect_rank"),
                            "augmented_rank": item.get("augmented_rank"),
                            "tangent_adjustment_count": item.get(
                                "tangent_adjustment", {}
                            ).get("coefficient_count"),
                            "correction_nonzero_count": item.get(
                                "finalized_correction", {}
                            ).get("nonzero_count"),
                            "pairing": item.get(
                                "obstruction_certificate", {}
                            ).get("pairing_with_rhs"),
                        }
                        for item in result["orders"]
                    ],
                },
                indent=2,
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    unittest.main()
