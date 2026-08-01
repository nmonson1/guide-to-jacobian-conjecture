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

        self.assertEqual(result["schema_version"], 2)
        self.assertEqual(
            result["source_sha256"],
            "a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8",
        )
        self.assertTrue(result["second_order_residual_identically_zero"])
        self.assertEqual(result["rank_six_tangent_dimension"], 22)
        self.assertEqual(result["left_kernel_dimension_over_Q(r)"], 2)
        self.assertEqual(
            result["generic_augmented_rank_over_Q(r)"],
            result["generic_effect_rank_over_Q(r)"] + 1,
        )

        basis = result["primitive_left_kernel_basis"]
        self.assertEqual(len(basis), 2)
        for witness in basis:
            self.assertEqual(witness["coordinate_gcd"], "1")
            self.assertGreater(witness["nonzero_count"], 0)

        pairing_ideal = result["pairing_ideal"]
        self.assertNotEqual(pairing_ideal["generator"], "0")
        certificate = result["combined_bezout_certificate"]
        self.assertGreater(certificate["nonzero_count"], 0)
        self.assertNotEqual(certificate["pairing_with_cubic_residual"], "0")
        self.assertEqual(
            result["universal_obstruction_for_all_finite_algebraic_ratios"],
            pairing_ideal["degree"] == 0,
        )

        samples = result["sample_checks"]
        self.assertEqual(len(samples), 9)
        for sample in samples:
            self.assertFalse(sample["cubic_lift_solvable"])
            self.assertGreater(
                sample["augmented_rank"],
                sample["effect_rank"],
            )
        if result["universal_obstruction_for_all_finite_algebraic_ratios"]:
            self.assertEqual(certificate["pairing_degree"], 0)
            for sample in samples:
                self.assertNotEqual(sample["combined_pairing"], 0)

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
                    "left_kernel_dimension": result[
                        "left_kernel_dimension_over_Q(r)"
                    ],
                    "basis_pairings": [
                        witness["pairing_with_cubic_residual"]
                        for witness in basis
                    ],
                    "pairing_ideal_generator": pairing_ideal["generator"],
                    "pairing_ideal_degree": pairing_ideal["degree"],
                    "combined_witness_nonzero_count": certificate[
                        "nonzero_count"
                    ],
                    "combined_witness_sha256": certificate["sha256"],
                    "combined_pairing": certificate[
                        "pairing_with_cubic_residual"
                    ],
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
