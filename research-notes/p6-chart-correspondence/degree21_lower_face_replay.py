#!/usr/bin/env python3
"""Exact replay of the degree-21 lower-face fixed-chart quotient.

The pinned leading-face fixture gives

    A0 = z p(z),  B0 = z^2 q(z)

over a quintic number field.  The pinned Newton support fixture gives the
allowed coefficient exponents in every normal layer.  For each requested
layer this program:

1. builds the exact matrix of D_r^{2,3} over the quintic field;
2. computes its kernel by exact Gaussian elimination;
3. enumerates every Laurent monomial weighted-divergence-free source field
   whose image under Theta_r is contained in the coefficient windows;
4. computes the rank of the resulting fixed-chart gauge image;
5. returns dim ker(D_r)/im(Theta_r).

For Psi=z^2 and r != 5, every Laurent monomial solution has

    f=z^k,  g=-(k+2)/(r-5) z^(k-1).

The search interval is proved finite from the output support bounds and is
reported.  This replays only the linear fixed-chart quotient.  It does not
replay the nonlinear fixed-chart shear argument or identify the surviving
layer-four class with the adjacent complete-chain operation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


class QuinticField:
    """Q[theta]/(f), with coefficients ordered from constant to theta^4."""

    def __init__(self, modulus: Sequence[int | str]) -> None:
        if len(modulus) != 6:
            raise ValueError("the modulus must have degree five")
        self.modulus = tuple(Fraction(int(value)) for value in modulus)
        if self.modulus[5] == 0:
            raise ValueError("the leading modulus coefficient must be nonzero")
        self.zero = FieldElement(self, (Fraction(0),) * 5)
        self.one = FieldElement(
            self, (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0))
        )

    def element(self, value: Any = 0) -> "FieldElement":
        if isinstance(value, FieldElement):
            if value.field.modulus != self.modulus:
                raise ValueError("field mismatch")
            return value
        if isinstance(value, (int, Fraction)):
            return FieldElement(
                self,
                (Fraction(value), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
            )
        values = list(value)
        if len(values) > 5:
            raise ValueError("field element has degree at least five")
        coefficients = [Fraction(item) for item in values]
        coefficients.extend(Fraction(0) for _ in range(5 - len(coefficients)))
        return FieldElement(self, tuple(coefficients))


@dataclass(frozen=True)
class FieldElement:
    field: QuinticField
    coefficients: tuple[Fraction, Fraction, Fraction, Fraction, Fraction]

    def _coerce(self, other: Any) -> "FieldElement":
        return self.field.element(other)

    def __bool__(self) -> bool:
        return any(self.coefficients)

    def __add__(self, other: Any) -> "FieldElement":
        other = self._coerce(other)
        return self.field.element(
            [left + right for left, right in zip(self.coefficients, other.coefficients)]
        )

    __radd__ = __add__

    def __neg__(self) -> "FieldElement":
        return self.field.element([-value for value in self.coefficients])

    def __sub__(self, other: Any) -> "FieldElement":
        return self + (-self._coerce(other))

    def __rsub__(self, other: Any) -> "FieldElement":
        return self._coerce(other) - self

    def __mul__(self, other: Any) -> "FieldElement":
        other = self._coerce(other)
        temporary = [Fraction(0)] * 9
        for left_degree, left in enumerate(self.coefficients):
            for right_degree, right in enumerate(other.coefficients):
                temporary[left_degree + right_degree] += left * right
        modulus = self.field.modulus
        for degree in range(8, 4, -1):
            leading = temporary[degree]
            if leading == 0:
                continue
            temporary[degree] = Fraction(0)
            for index in range(5):
                temporary[degree - 5 + index] -= (
                    leading * modulus[index] / modulus[5]
                )
        return self.field.element(temporary[:5])

    __rmul__ = __mul__

    def inverse(self) -> "FieldElement":
        if not self:
            raise ZeroDivisionError("zero has no inverse")
        field = self.field
        basis = [
            field.element([1 if index == degree else 0 for index in range(5)])
            for degree in range(5)
        ]
        columns = [(self * vector).coefficients for vector in basis]
        matrix = [
            [columns[column][row] for column in range(5)]
            + [Fraction(1 if row == 0 else 0)]
            for row in range(5)
        ]
        for column in range(5):
            pivot = next(
                row for row in range(column, 5) if matrix[row][column] != 0
            )
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            scale = matrix[column][column]
            matrix[column] = [value / scale for value in matrix[column]]
            for row in range(5):
                if row == column:
                    continue
                factor = matrix[row][column]
                if factor:
                    matrix[row] = [
                        matrix[row][entry] - factor * matrix[column][entry]
                        for entry in range(6)
                    ]
        return field.element([matrix[row][5] for row in range(5)])

    def __truediv__(self, other: Any) -> "FieldElement":
        return self * self._coerce(other).inverse()

    def __rtruediv__(self, other: Any) -> "FieldElement":
        return self._coerce(other) * self.inverse()

    def __pow__(self, exponent: int) -> "FieldElement":
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = self.field.one
        base = self
        remaining = exponent
        while remaining:
            if remaining & 1:
                result = result * base
            base = base * base
            remaining //= 2
        return result

    def as_json(self) -> list[dict[str, str]]:
        return [
            {"num": str(value.numerator), "den": str(value.denominator)}
            for value in self.coefficients
        ]


Poly = dict[int, FieldElement]
Vector = list[FieldElement]
Matrix = list[list[FieldElement]]


def clean(poly: Mapping[int, FieldElement]) -> Poly:
    return {exponent: coefficient for exponent, coefficient in poly.items() if coefficient}


def monomial(field: QuinticField, exponent: int, coefficient: Any = 1) -> Poly:
    coefficient = field.element(coefficient)
    return {} if not coefficient else {exponent: coefficient}


def add(field: QuinticField, *polys: Mapping[int, FieldElement]) -> Poly:
    result: Poly = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            result[exponent] = result.get(exponent, field.zero) + coefficient
    return clean(result)


def scale(
    field: QuinticField, poly: Mapping[int, FieldElement], coefficient: Any
) -> Poly:
    coefficient = field.element(coefficient)
    return clean({exponent: coefficient * value for exponent, value in poly.items()})


def multiply(
    field: QuinticField,
    left: Mapping[int, FieldElement],
    right: Mapping[int, FieldElement],
) -> Poly:
    result: Poly = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            result[exponent] = (
                result.get(exponent, field.zero)
                + left_coefficient * right_coefficient
            )
    return clean(result)


def derivative(field: QuinticField, poly: Mapping[int, FieldElement]) -> Poly:
    return clean(
        {
            exponent - 1: field.element(exponent) * coefficient
            for exponent, coefficient in poly.items()
            if exponent != 0
        }
    )


def parse_field_element(field: QuinticField, value: Any) -> FieldElement:
    if not isinstance(value, list) or len(value) != 5:
        raise ValueError("a serialized quintic-field element must have five entries")
    return field.element(
        [Fraction(int(entry["num"]), int(entry["den"])) for entry in value]
    )


def parse_face(path: Path) -> tuple[QuinticField, Poly, Poly]:
    document = json.loads(path.read_text(encoding="utf-8"))
    field = QuinticField(document["minimal_polynomial"])
    p = [parse_field_element(field, value) for value in document["a"]]
    q = [parse_field_element(field, value) for value in document["b"]]
    A0 = {index + 1: coefficient for index, coefficient in enumerate(p) if coefficient}
    B0 = {index + 2: coefficient for index, coefficient in enumerate(q) if coefficient}
    return field, A0, B0


def face_equation(
    field: QuinticField, A0: Mapping[int, FieldElement], B0: Mapping[int, FieldElement]
) -> Poly:
    # For A0=z p and B0=z^2 q, Psi=2 A0 B0' - 3 A0' B0.
    return add(
        field,
        scale(field, multiply(field, A0, derivative(field, B0)), 2),
        scale(field, multiply(field, derivative(field, A0), B0), -3),
    )


def determinant_layer(
    field: QuinticField,
    r: int,
    A0: Mapping[int, FieldElement],
    B0: Mapping[int, FieldElement],
    a: Mapping[int, FieldElement],
    b: Mapping[int, FieldElement],
) -> Poly:
    return add(
        field,
        scale(field, multiply(field, a, derivative(field, B0)), 2 - r),
        scale(field, multiply(field, B0, derivative(field, a)), -3),
        scale(field, multiply(field, A0, derivative(field, b)), 2),
        scale(field, multiply(field, b, derivative(field, A0)), r - 3),
    )


def theta(
    field: QuinticField,
    A0: Mapping[int, FieldElement],
    B0: Mapping[int, FieldElement],
    f: Mapping[int, FieldElement],
    g: Mapping[int, FieldElement],
) -> tuple[Poly, Poly]:
    return (
        add(
            field,
            multiply(field, f, derivative(field, A0)),
            scale(field, multiply(field, g, A0), -2),
        ),
        add(
            field,
            multiply(field, f, derivative(field, B0)),
            scale(field, multiply(field, g, B0), -3),
        ),
    )


def matrix_rank(matrix: Matrix, *, columns: int, field: QuinticField) -> int:
    return len(rref(matrix, columns=columns, field=field)[1])


def rref(
    matrix: Matrix, *, columns: int, field: QuinticField
) -> tuple[Matrix, list[int]]:
    rows = [list(row) for row in matrix]
    if any(len(row) != columns for row in rows):
        raise ValueError("matrix rows have inconsistent length")
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = rows[pivot_row][column].inverse()
        rows[pivot_row] = [entry * inverse for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor:
                rows[row] = [
                    left - factor * right
                    for left, right in zip(rows[row], rows[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return rows, pivot_columns


def nullspace(matrix: Matrix, *, columns: int, field: QuinticField) -> list[Vector]:
    reduced, pivots = rref(matrix, columns=columns, field=field)
    free_columns = [column for column in range(columns) if column not in pivots]
    basis: list[Vector] = []
    for free_column in free_columns:
        vector = [field.zero for _ in range(columns)]
        vector[free_column] = field.one
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column]
        basis.append(vector)
    return basis


def columns_to_matrix(
    field: QuinticField, columns: Sequence[Poly], exponents: Sequence[int]
) -> Matrix:
    return [
        [column.get(exponent, field.zero) for column in columns]
        for exponent in exponents
    ]


def vector_image(matrix: Matrix, vector: Vector, field: QuinticField) -> Vector:
    return [
        sum((entry * value for entry, value in zip(row, vector)), field.zero)
        for row in matrix
    ]


def output_vector(
    field: QuinticField,
    a: Mapping[int, FieldElement],
    b: Mapping[int, FieldElement],
    a_support: Sequence[int],
    b_support: Sequence[int],
) -> Vector:
    return [a.get(exponent, field.zero) for exponent in a_support] + [
        b.get(exponent, field.zero) for exponent in b_support
    ]


def load_full_layers(path: Path, requested: Iterable[int]) -> list[dict[str, Any]]:
    document = json.loads(path.read_text(encoding="utf-8"))
    full = next(case for case in document["cases"] if case["label"] == "full")
    by_layer = {layer["r"]: layer for layer in full["layers"]}
    return [by_layer[layer] for layer in requested]


def serialized_matrix_digest(matrix: Matrix, *, columns: int) -> str:
    payload = {
        "rows": len(matrix),
        "columns": columns,
        "entries": [
            [entry.as_json() for entry in row]
            for row in matrix
        ],
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def source_search_bounds(
    a_support: Sequence[int], b_support: Sequence[int]
) -> tuple[int, int]:
    # Theta(z^k, c z^(k-1)) shifts A0' by k and B0' by k.
    # Two extra degrees on either side safely include every endpoint cancellation.
    minimum = min([*a_support, *(value - 1 for value in b_support)]) - 10
    maximum = max([*a_support, *(value - 1 for value in b_support)]) + 3
    return minimum, maximum


def support_subset(poly: Mapping[int, FieldElement], support: Sequence[int]) -> bool:
    allowed = set(support)
    return all(exponent in allowed for exponent in poly)


def independent_columns(
    field: QuinticField, vectors: Sequence[Vector], ambient_dimension: int
) -> list[Vector]:
    basis: list[Vector] = []
    current_rank = 0
    for vector in vectors:
        trial = basis + [vector]
        matrix = [
            [candidate[column] for candidate in trial]
            for column in range(ambient_dimension)
        ]
        trial_rank = matrix_rank(matrix, columns=len(trial), field=field)
        if trial_rank > current_rank:
            basis.append(vector)
            current_rank = trial_rank
    return basis


def analyze_layer(
    field: QuinticField,
    A0: Mapping[int, FieldElement],
    B0: Mapping[int, FieldElement],
    layer: Mapping[str, Any],
) -> dict[str, Any]:
    r = int(layer["r"])
    if r == 5:
        raise ValueError("the current monomial gauge enumerator treats only r != 5")
    a_support = list(layer["a_support"])
    b_support = list(layer["b_support"])
    output_basis = [
        *(('a', exponent) for exponent in a_support),
        *(('b', exponent) for exponent in b_support),
    ]
    columns: list[Poly] = []
    for kind, exponent in output_basis:
        a = monomial(field, exponent) if kind == "a" else {}
        b = monomial(field, exponent) if kind == "b" else {}
        columns.append(determinant_layer(field, r, A0, B0, a, b))
    target_exponents = sorted(
        {exponent for column in columns for exponent in column}
    )
    operator = columns_to_matrix(field, columns, target_exponents)
    domain_dimension = len(output_basis)
    operator_rank = matrix_rank(operator, columns=domain_dimension, field=field)
    kernel_dimension = domain_dimension - operator_rank
    cokernel_dimension = len(target_exponents) - operator_rank

    minimum_k, maximum_k = source_search_bounds(a_support, b_support)
    gauge_candidates: list[Vector] = []
    allowed_k: list[int] = []
    candidate_supports: list[dict[str, Any]] = []
    for k in range(minimum_k, maximum_k + 1):
        f = monomial(field, k)
        coefficient = -Fraction(k + 2, r - 5)
        g = monomial(field, k - 1, coefficient)
        a, b = theta(field, A0, B0, f, g)
        if not support_subset(a, a_support) or not support_subset(b, b_support):
            continue
        vector = output_vector(field, a, b, a_support, b_support)
        if not any(vector):
            continue
        image = vector_image(operator, vector, field)
        if any(image):
            raise AssertionError(f"layer {r}: gauge monomial k={k} is not in ker D_r")
        allowed_k.append(k)
        gauge_candidates.append(vector)
        candidate_supports.append(
            {
                "k": k,
                "a_support": sorted(a),
                "b_support": sorted(b),
                "g_coefficient": {
                    "num": str(coefficient.numerator),
                    "den": str(coefficient.denominator),
                },
            }
        )

    gauge_basis = independent_columns(field, gauge_candidates, domain_dimension)
    gauge_dimension = len(gauge_basis)
    residual_dimension = kernel_dimension - gauge_dimension
    if residual_dimension < 0:
        raise AssertionError("the gauge rank exceeds the determinant kernel dimension")

    return {
        "r": r,
        "a_support": a_support,
        "b_support": b_support,
        "domain_dimension": domain_dimension,
        "target_exponents": target_exponents,
        "target_dimension": len(target_exponents),
        "rank": operator_rank,
        "kernel_dimension": kernel_dimension,
        "cokernel_dimension": cokernel_dimension,
        "gauge_search_interval": [minimum_k, maximum_k],
        "allowed_gauge_exponents": allowed_k,
        "gauge_candidates": candidate_supports,
        "gauge_dimension": gauge_dimension,
        "residual_dimension": residual_dimension,
        "operator_sha256": serialized_matrix_digest(
            operator, columns=domain_dimension
        ),
    }


def analyze(
    face_path: Path,
    support_path: Path,
    layers: Sequence[int],
) -> dict[str, Any]:
    field, A0, B0 = parse_face(face_path)
    psi = face_equation(field, A0, B0)
    expected_psi = {2: field.one}
    if psi != expected_psi:
        raise ValueError("the reconstructed leading face does not satisfy Psi=z^2")
    results = [
        analyze_layer(field, A0, B0, layer)
        for layer in load_full_layers(support_path, layers)
    ]
    return {
        "schema_version": 1,
        "name": "degree-21 lower-face fixed-chart linear replay",
        "coefficient_field_degree": 5,
        "minimal_polynomial": [str(value) for value in field.modulus],
        "face_identity_verified": True,
        "identity": "D_r Theta_r(f,g)=(f z^2)' +(r-5)g z^2",
        "gauge_model": (
            "all Laurent monomial weighted-divergence-free fields whose "
            "Theta_r image lies in the exact full-support coefficient windows"
        ),
        "layers": results,
        "residual_sequence": [result["residual_dimension"] for result in results],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("face", type=Path)
    parser.add_argument("supports", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument(
        "--layers",
        default="1,2,3,4",
        help="comma-separated normal layers (default: 1,2,3,4)",
    )
    args = parser.parse_args(argv)
    try:
        layers = [int(value) for value in args.layers.split(",") if value]
        report = analyze(args.face, args.supports, layers)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"degree21_lower_face_replay: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
