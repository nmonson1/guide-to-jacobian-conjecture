from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH_TOOLS = HERE.parent.parent
sys.path.insert(0, str(RESEARCH_TOOLS))

from filtered_operation_complex.adapters.program5_rank_six_third_order_lift import (  # noqa: E402
    analyze_third_order,
)


class Program5ThirdOrderLiftTests(unittest.TestCase):
    def test_chosen_plane_has_certified_cubic_obstruction(self) -> None:
        result = analyze_third_order()

        self.assertEqual(result["schema_version"], 2)
        self.assertEqual(
            result["source_sha256"],
            "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        )
        self.assertEqual(result["ambient_operation_dimension"], 115)
        self.assertEqual(result["rank_six_tangent_dimension"], 22)
        self.assertEqual(result["quadratic_tangent_freedom_dimension"], 66)
        self.assertEqual(result["direct_effect_columns_verified"], 66)
        self.assertEqual(result["compressed_cubic_equation_count"], 24)
        self.assertEqual(result["cubic_effect_rank"], 15)
        self.assertEqual(result["cubic_augmented_rank"], 16)
        self.assertFalse(result["cubic_lift_solvable"])
        self.assertIsNone(result["cubic_lift_solution_free_dimension"])

        certificate = result["cubic_obstruction_certificate"]
        self.assertEqual(certificate["kind"], "exact left-null witness")
        self.assertEqual(certificate["nonzero_count"], 2)
        self.assertEqual(certificate["pairing_with_rhs"], "-256/3")
        self.assertEqual(
            certificate["witness_sha256"],
            "8fcd1d848258112da813c47f4878cdacbecb59c9dd44ec80f44fb4636390c679",
        )
        self.assertEqual(
            certificate["coordinates"],
            [
                {
                    "parameter_monomial": "v^3",
                    "schur_row_variable": "q",
                    "schur_column_monomial": "a*d*q",
                    "coefficient": 1,
                },
                {
                    "parameter_monomial": "v^3",
                    "schur_row_variable": "k",
                    "schur_column_monomial": "b*d*s",
                    "coefficient": "-8/3",
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()
