from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH_TOOLS = HERE.parent.parent
sys.path.insert(0, str(RESEARCH_TOOLS))

from filtered_operation_complex.adapters.program5_rank_six_algebraic_fourth_order_kuranishi import (  # noqa: E402
    analyze_algebraic_fourth_order_kuranishi,
)


class Program5AlgebraicFourthOrderKuranishiTests(unittest.TestCase):
    def test_complete_algebraic_cubic_lift_fibre_is_retained(self) -> None:
        result = analyze_algebraic_fourth_order_kuranishi()

        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(
            result["source_sha256"],
            "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        )
        self.assertEqual(result["coefficient_field"], "Q(sqrt(-3))")
        self.assertTrue(
            result["conjugate_result_follows_by_Q_galois_symmetry"]
        )
        self.assertEqual(result["rank_six_tangent_dimension"], 22)
        self.assertEqual(result["cubic_effect_rank"], 5)
        self.assertEqual(result["cubic_augmented_rank"], 5)
        self.assertEqual(result["cubic_lift_affine_dimension"], 17)

        order_four = result["order_four_map"]
        self.assertEqual(order_four["source_dimension"], 17)
        self.assertEqual(order_four["linear_coefficient_count"], 17)
        self.assertEqual(
            order_four["diagonal_quadratic_coefficient_count"],
            17,
        )
        self.assertEqual(
            order_four["off_diagonal_quadratic_coefficient_count"],
            136,
        )
        self.assertGreater(order_four["active_target_coordinate_count"], 0)
        self.assertEqual(
            result["intrinsic_order_four_obstruction"],
            order_four[
                "constant_term_outside_variable_coefficient_span"
            ],
        )
        if result["intrinsic_order_four_obstruction"]:
            self.assertGreater(
                order_four["constant_augmented_rank"],
                order_four["variable_coefficient_rank"],
            )
            certificate = result["obstruction_certificate"]
            self.assertIsNotNone(certificate)
            self.assertNotEqual(
                certificate["pairing_with_constant_term"],
                "0",
            )
            self.assertGreater(certificate["nonzero_count"], 0)
        else:
            self.assertEqual(
                order_four["constant_augmented_rank"],
                order_four["variable_coefficient_rank"],
            )
            self.assertIsNone(result["obstruction_certificate"])

        print(
            json.dumps(
                {
                    "audited_ratio": result["audited_ratio"],
                    "conjugate_ratio": result["conjugate_ratio"],
                    "cubic_effect_rank": result["cubic_effect_rank"],
                    "cubic_lift_affine_dimension": result[
                        "cubic_lift_affine_dimension"
                    ],
                    "constant_nonzero_count": order_four[
                        "constant_nonzero_count"
                    ],
                    "active_target_coordinate_count": order_four[
                        "active_target_coordinate_count"
                    ],
                    "variable_coefficient_rank": order_four[
                        "variable_coefficient_rank"
                    ],
                    "constant_augmented_rank": order_four[
                        "constant_augmented_rank"
                    ],
                    "intrinsic_order_four_obstruction": result[
                        "intrinsic_order_four_obstruction"
                    ],
                    "certificate_pairing": (
                        result["obstruction_certificate"] or {}
                    ).get("pairing_with_constant_term"),
                    "certificate_nonzero_count": (
                        result["obstruction_certificate"] or {}
                    ).get("nonzero_count"),
                },
                indent=2,
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    unittest.main()
