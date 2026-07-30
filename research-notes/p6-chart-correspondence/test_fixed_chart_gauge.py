from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path

from fixed_chart_gauge import (
    analyze_contract,
    analyze_document,
    face_volume,
    theta_identity_residual,
)


HERE = Path(__file__).resolve().parent
EXAMPLE = HERE / "fixed_chart_example.json"


class FixedChartGaugeTests(unittest.TestCase):
    def test_theta_identity_for_laurent_fields(self) -> None:
        A0 = {-1: Fraction(2), 0: Fraction(1), 2: Fraction(3)}
        B0 = {0: Fraction(-1), 1: Fraction(4), 3: Fraction(2)}
        f = {-2: Fraction(3, 5), 1: Fraction(-7, 3)}
        g = {-1: Fraction(11, 2), 2: Fraction(5, 7)}
        residual = theta_identity_residual(2, 3, 4, A0, B0, f, g)
        self.assertEqual(residual, {})

    def test_boundary_face_has_psi_z_squared(self) -> None:
        # The toy face p=q=1 satisfies pq+2zp q'-3zp'q=1.
        A0 = {1: Fraction(1)}
        B0 = {2: Fraction(1)}
        self.assertEqual(face_volume(2, 3, A0, B0), {2: Fraction(1)})

    def test_residual_dimension_depends_on_source_window(self) -> None:
        document = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        restricted, extended = analyze_document(document)

        self.assertEqual(restricted.output_kernel_dimension, 2)
        self.assertEqual(restricted.admissible_source_dimension, 1)
        self.assertEqual(restricted.gauge_dimension, 1)
        self.assertEqual(restricted.stabilizer_dimension, 0)
        self.assertEqual(restricted.residual_dimension, 1)

        self.assertEqual(extended.output_kernel_dimension, 2)
        self.assertEqual(extended.admissible_source_dimension, 2)
        self.assertEqual(extended.gauge_dimension, 2)
        self.assertEqual(extended.stabilizer_dimension, 0)
        self.assertEqual(extended.residual_dimension, 0)

    def test_restricted_generator_is_weighted_divergence_free(self) -> None:
        document = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        restricted = analyze_document(document)[0]
        self.assertEqual(
            restricted.source_variables,
            [["f", 0], ["f", 1], ["g", 0], ["g", 1]],
        )
        self.assertEqual(len(restricted.source_basis), 1)
        # Up to scale: f=z and g=3, since (fz^2)'-g z^2=0 at r=4.
        vector = restricted.source_basis[0]
        self.assertEqual(vector[0], 0)
        self.assertEqual(vector[3], 0)
        self.assertNotEqual(vector[1], 0)
        self.assertEqual(vector[2], 3 * vector[1])

    def test_resonant_layer_separates_f_and_g_freedoms(self) -> None:
        result = analyze_contract(
            {
                "label": "toy resonant layer",
                "alpha": 2,
                "beta": 3,
                "r": 5,
                "A0": [[1, 1]],
                "B0": [[2, 1]],
                "f_exponents": [-2, 0],
                "g_exponents": [0],
                "a_support": [-2, 1],
                "b_support": [-1, 2],
            }
        )
        # At r=alpha+beta the divergence equation is (f Psi)'=0;
        # f=z^-2 and g=1 are independent admissible source directions.
        self.assertEqual(result.admissible_source_dimension, 2)
        self.assertEqual(result.gauge_dimension, 2)
        self.assertEqual(result.output_kernel_dimension, 3)
        self.assertEqual(result.residual_dimension, 1)


if __name__ == "__main__":
    unittest.main()
