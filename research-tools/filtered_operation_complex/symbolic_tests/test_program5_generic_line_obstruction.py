from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH_TOOLS = HERE.parent.parent
sys.path.insert(0, str(RESEARCH_TOOLS))

from filtered_operation_complex.adapters.program5_rank_six_generic_line_obstruction import (  # noqa: E402
    analyze_generic_line_obstruction,
)


class Program5GenericLineObstructionTests(unittest.TestCase):
    def test_finite_ratio_obstruction_is_computed_symbolically(self) -> None:
        result = analyze_generic_line_obstruction()

        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(
            result["source_sha256"],
            "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        )
        self.assertTrue(result["second_order_residual_identically_zero"])
        self.assertEqual(result["rank_six_tangent_dimension"], 22)
        self.assertEqual(result["left_kernel_dimension_over_Q(r)"], 1)
        self.assertEqual(
            result["generic_augmented_rank_over_Q(r)"],
            result["generic_effect_rank_over_Q(r)"] + 1,
        )
        primitive = result["primitive_left_kernel"]
        self.assertEqual(primitive["coordinate_gcd"], "1")
        self.assertGreater(primitive["nonzero_count"], 0)
        self.assertEqual(len(result["sample_checks"]), 9)

        print(
            json.dumps(
                {
                    "compressed_cubic_equation_count": result[
                        "compressed_cubic_equation_count"
                    ],
                    "effect_rank": result["generic_effect_rank_over_Q(r)"],
                    "augmented_rank": result[
                        "generic_augmented_rank_over_Q(r)"
                    ],
                    "primitive_witness_nonzero_count": primitive[
                        "nonzero_count"
                    ],
                    "primitive_witness_sha256": primitive["sha256"],
                    "pairing": result["pairing_with_cubic_residual"],
                    "pairing_degree": result["pairing_degree"],
                    "universal": result[
                        "universal_obstruction_for_all_finite_algebraic_ratios"
                    ],
                },
                indent=2,
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    unittest.main()
