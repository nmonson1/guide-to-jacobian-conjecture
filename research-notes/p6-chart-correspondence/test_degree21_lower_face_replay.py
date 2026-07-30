from __future__ import annotations

import unittest
from pathlib import Path

from degree21_lower_face_replay import (
    face_equation,
    parse_face,
)


HERE = Path(__file__).resolve().parent
FACE = HERE / "fixtures" / "exact_belyi_data.json"


class Degree21LowerFaceReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.field, cls.A0, cls.B0 = parse_face(FACE)

    def test_primitive_element_satisfies_the_pinned_modulus(self) -> None:
        theta = self.field.element([0, 1])
        value = self.field.zero
        for coefficient in reversed(self.field.modulus):
            value = value * theta + self.field.element(coefficient)
        self.assertFalse(value)

    def test_field_inversion(self) -> None:
        theta = self.field.element([0, 1])
        value = theta + 3
        self.assertEqual(value * value.inverse(), self.field.one)

    def test_exact_face_identity_is_psi_z_squared(self) -> None:
        self.assertEqual(
            face_equation(self.field, self.A0, self.B0),
            {2: self.field.one},
        )

    def test_leading_degrees_are_seven_and_ten(self) -> None:
        self.assertEqual((min(self.A0), max(self.A0)), (1, 8))
        self.assertEqual((min(self.B0), max(self.B0)), (2, 12))


if __name__ == "__main__":
    unittest.main()
