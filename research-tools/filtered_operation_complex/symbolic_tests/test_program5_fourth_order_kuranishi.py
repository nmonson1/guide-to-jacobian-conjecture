from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH_TOOLS = HERE.parent.parent
sys.path.insert(0, str(RESEARCH_TOOLS))

from filtered_operation_complex.adapters.program5_rank_six_fourth_order_kuranishi import (  # noqa: E402
    analyze_fourth_order_kuranishi,
)


class Program5FourthOrderKuranishiTests(unittest.TestCase):
    def test_complete_cubic_lift_fibre_is_retained_at_order_four(self) -> None:
        result = analyze_fourth_order_kuranishi()

        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(
            result["source_sha256"],
            "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        )
        self.assertEqual(result["rank_six_tangent_dimension"], 22)
        self.assertEqual(result["cubic_effect_rank"], 2)
        self.assertEqual(result["cubic_augmented_rank"], 2)
        self.assertEqual(result["cubic_lift_affine_dimension"], 20)
        self.assertGreater(
            result["deterministic_quartic_residual"]["nonzero_count"],
            0,
        )

        kuranishi = result["quartic_kuranishi"]
        self.assertEqual(kuranishi["source_dimension"], 20)
        self.assertGreater(kuranishi["target_coefficient_rank"], 0)
        self.assertEqual(
            kuranishi["independent_equation_count"],
            len(kuranishi["equations"]),
        )
        for equation in kuranishi["equations"]:
            self.assertLessEqual(equation["total_degree"], 2)
            self.assertGreater(len(equation["terms"]), 0)

        self.assertEqual(
            result["rational_zero_found"],
            result["rational_zero"] is not None,
        )
        if result["rational_zero_found"]:
            self.assertTrue(result["rational_zero_verified"])
            self.assertGreaterEqual(
                result["rational_zero"]["coefficient_count"],
                0,
            )
        else:
            self.assertFalse(result["rational_zero_verified"])

        print(
            json.dumps(
                {
                    "cubic_effect_rank": result["cubic_effect_rank"],
                    "cubic_lift_affine_dimension": result[
                        "cubic_lift_affine_dimension"
                    ],
                    "deterministic_quartic_residual_nonzero_count": result[
                        "deterministic_quartic_residual"
                    ]["nonzero_count"],
                    "quartic_target_coefficient_rank": kuranishi[
                        "target_coefficient_rank"
                    ],
                    "quartic_equations": [
                        {
                            "row_variable": equation[
                                "schur_row_variable"
                            ],
                            "column_monomial": equation[
                                "schur_column_monomial"
                            ],
                            "expression": equation["expression"],
                            "term_count": len(equation["terms"]),
                        }
                        for equation in kuranishi["equations"]
                    ],
                    "rational_zero_found": result["rational_zero_found"],
                    "rational_zero": result["rational_zero"],
                },
                indent=2,
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    unittest.main()
