#!/usr/bin/env python3
"""Dependency-free replay of the archived degree-21 upper-face layer maps.

The archive records supports, ordered monomial bases, and claimed left/right
nullspace bases.  The original generator used SymPy.  This script reconstructs
all matrices independently from the displayed bilinear formula using only
``fractions.Fraction`` and audits every recorded rank and nullspace.

This is a replay of the raw upper-face linear complex.  It does not reproduce
the later specialized fixed-chart quotient with residual dimensions
``(1, 2, 1, 1)`` and does not identify the ``k = 4`` rechart vector.
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

from chart_correspondence import (
    Matrix,
    Vector,
    matrix_vector_product,
    parse_vectors,
    q,
    rank,
    rank_of_vectors,
    rational_string,
)

Poly = dict[int, Fraction]


def clean(poly: Mapping[int, Fraction]) -> Poly:
    return {exponent: coefficient for exponent, coefficient in poly.items() if coefficient}


def monomial(exponent: int, coefficient: Fraction | int = 1) -> Poly:
    coefficient = q(coefficient)
    return {} if coefficient == 0 else {exponent: coefficient}


def add(*polys: Mapping[int, Fraction]) -> Poly:
    result: Poly = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            result[exponent] = result.get(exponent, Fraction(0)) + coefficient
    return clean(result)


def scale(poly: Mapping[int, Fraction], coefficient: Fraction | int) -> Poly:
    coefficient = q(coefficient)
    return clean({exponent: coefficient * value for exponent, value in poly.items()})


def multiply(left: Mapping[int, Fraction], right: Mapping[int, Fraction]) -> Poly:
    result: Poly = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            result[exponent] = result.get(exponent, Fraction(0)) + left_coefficient * right_coefficient
    return clean(result)


def derivative(poly: Mapping[int, Fraction]) -> Poly:
    return clean(
        {
            exponent - 1: Fraction(exponent) * coefficient
            for exponent, coefficient in poly.items()
            if exponent != 0
        }
    )


def power(poly: Mapping[int, Fraction], exponent: int) -> Poly:
    if exponent < 0:
        raise ValueError("polynomial exponent must be nonnegative")
    result: Poly = {0: Fraction(1)}
    base = dict(poly)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply(result, base)
        remaining >>= 1
        if remaining:
            base = multiply(base, base)
    return result


# R = y^7(y-1) = y^8-y^7, as in the archived generator.
R: Poly = {8: Fraction(1), 7: Fraction(-1)}
U0: Poly = power(R, 2)
V0: Poly = power(R, 3)
DU0: Poly = derivative(U0)
DV0: Poly = derivative(V0)


def column_image(r: int, kind: str, exponent: int) -> Poly:
    """Image of one ordered domain monomial under the archived L_r formula."""
    basis = monomial(exponent)
    derivative_basis = derivative(basis)
    if kind == "u":
        # (8-r)u v0' - 12u'v0
        return add(
            scale(multiply(basis, DV0), 8 - r),
            scale(multiply(derivative_basis, V0), -12),
        )
    if kind == "v":
        # 8u0 v' - (12-r)u0'v
        return add(
            scale(multiply(U0, derivative_basis), 8),
            scale(multiply(DU0, basis), -(12 - r)),
        )
    raise ValueError(f"unknown domain kind {kind!r}")


def reconstruct_matrix(layer: Mapping[str, Any]) -> Matrix:
    r = layer.get("r")
    basis = layer.get("domain_basis")
    output_exponents = layer.get("output_exponents")
    if not isinstance(r, int):
        raise ValueError("layer r must be an integer")
    if not isinstance(basis, list) or not isinstance(output_exponents, list):
        raise ValueError(f"layer {r}: missing ordered bases")
    if not all(isinstance(value, int) for value in output_exponents):
        raise ValueError(f"layer {r}: output exponents must be integers")

    columns: list[Poly] = []
    for index, item in enumerate(basis):
        if (
            not isinstance(item, list)
            or len(item) != 2
            or not isinstance(item[0], str)
            or not isinstance(item[1], int)
        ):
            raise ValueError(f"layer {r}: invalid domain basis entry {index}")
        columns.append(column_image(r, item[0], item[1]))

    allowed = set(output_exponents)
    outside = sorted(
        {
            exponent
            for column in columns
            for exponent, coefficient in column.items()
            if coefficient and exponent not in allowed
        }
    )
    if outside:
        raise ValueError(f"layer {r}: reconstructed image has omitted exponents {outside}")

    return [
        [column.get(exponent, Fraction(0)) for column in columns]
        for exponent in output_exponents
    ]


def transpose(matrix: Matrix) -> Matrix:
    if not matrix:
        return []
    return [[matrix[row][column] for row in range(len(matrix))] for column in range(len(matrix[0]))]


def matrix_json(matrix: Matrix) -> list[list[str]]:
    return [[rational_string(value) for value in row] for row in matrix]


def matrix_digest(matrix: Matrix) -> str:
    payload = json.dumps(matrix_json(matrix), separators=(",", ":"), ensure_ascii=True).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def vectors_span_kernel(
    matrix: Matrix,
    values: Any,
    *,
    expected_dimension: int,
    name: str,
) -> tuple[list[Vector], bool]:
    ambient_dimension = len(matrix[0]) if matrix else 0
    if not isinstance(values, list):
        raise ValueError(f"{name} must be a list")
    vectors = parse_vectors(values, width=ambient_dimension, name=name)
    for index, vector in enumerate(vectors):
        image = matrix_vector_product(matrix, vector)
        if any(image):
            raise ValueError(
                f"{name}[{index}] is not in the claimed kernel: "
                f"{[rational_string(value) for value in image]}"
            )
    return vectors, rank_of_vectors(vectors, ambient_dimension=ambient_dimension) == expected_dimension


@dataclass(frozen=True)
class LayerAudit:
    case: str
    r: int
    rows: int
    columns: int
    rank: int
    kernel_dimension: int
    cokernel_dimension: int
    matrix_sha256: str
    right_basis_verified: bool
    left_basis_verified: bool
    recorded_dimensions_verified: bool
    matrix: Matrix

    @property
    def verified(self) -> bool:
        return (
            self.right_basis_verified
            and self.left_basis_verified
            and self.recorded_dimensions_verified
        )

    def as_json(self, *, include_matrix: bool) -> dict[str, Any]:
        result: dict[str, Any] = {
            "case": self.case,
            "r": self.r,
            "rows": self.rows,
            "columns": self.columns,
            "rank": self.rank,
            "kernel_dimension": self.kernel_dimension,
            "cokernel_dimension": self.cokernel_dimension,
            "matrix_sha256": self.matrix_sha256,
            "right_basis_verified": self.right_basis_verified,
            "left_basis_verified": self.left_basis_verified,
            "recorded_dimensions_verified": self.recorded_dimensions_verified,
            "verified": self.verified,
        }
        if include_matrix:
            result["operator"] = matrix_json(self.matrix)
        return result


def audit_layer(case: str, layer: Mapping[str, Any]) -> LayerAudit:
    matrix = reconstruct_matrix(layer)
    rows = len(matrix)
    columns = len(matrix[0]) if matrix else int(layer.get("domain_dim", 0))
    computed_rank = rank(matrix)
    kernel_dimension = columns - computed_rank
    cokernel_dimension = rows - computed_rank

    right_vectors, right_complete = vectors_span_kernel(
        matrix,
        layer.get("right_nullspace"),
        expected_dimension=kernel_dimension,
        name=f"{case}.r{layer.get('r')}.right_nullspace",
    )
    left_matrix = transpose(matrix)
    left_vectors, left_complete = vectors_span_kernel(
        left_matrix,
        layer.get("left_nullspace"),
        expected_dimension=cokernel_dimension,
        name=f"{case}.r{layer.get('r')}.left_nullspace",
    )

    # Make the completeness test explicit even when a supplied list has redundant vectors.
    right_complete = right_complete and len(right_vectors) >= kernel_dimension
    left_complete = left_complete and len(left_vectors) >= cokernel_dimension
    recorded_dimensions_verified = (
        layer.get("domain_dim") == columns
        and layer.get("codomain_support_dim") == rows
        and layer.get("rank") == computed_rank
        and layer.get("kernel_dim") == kernel_dimension
        and layer.get("cokernel_dim") == cokernel_dimension
    )
    return LayerAudit(
        case=case,
        r=int(layer["r"]),
        rows=rows,
        columns=columns,
        rank=computed_rank,
        kernel_dimension=kernel_dimension,
        cokernel_dimension=cokernel_dimension,
        matrix_sha256=matrix_digest(matrix),
        right_basis_verified=right_complete,
        left_basis_verified=left_complete,
        recorded_dimensions_verified=recorded_dimensions_verified,
        matrix=matrix,
    )


def audit_document(document: Mapping[str, Any], *, include_matrices: bool = False) -> dict[str, Any]:
    audits: list[LayerAudit] = []
    for case in ("truncated", "full"):
        case_data = document.get(case)
        if not isinstance(case_data, dict):
            raise ValueError(f"missing {case!r} archive data")
        layers = case_data.get("layers")
        if not isinstance(layers, list):
            raise ValueError(f"{case}.layers must be a list")
        seen: set[int] = set()
        for layer in layers:
            if not isinstance(layer, dict):
                raise ValueError(f"{case}: layer entry must be an object")
            audit = audit_layer(case, layer)
            if audit.r in seen:
                raise ValueError(f"{case}: duplicate layer {audit.r}")
            seen.add(audit.r)
            audits.append(audit)
        if seen != set(range(1, 13)):
            raise ValueError(f"{case}: expected layers 1 through 12, found {sorted(seen)}")

    return {
        "schema_version": 1,
        "name": "archived degree-21 upper-face linear replay",
        "scope": (
            "Raw full and truncated upper-face layer maps reconstructed from the "
            "displayed L_r formula; this is not the specialized chart quotient."
        ),
        "formula": (
            "L_r(u,v)=(8-r)u v0' - 12u'v0 + 8u0 v' - (12-r)u0'v; "
            "R=y^7(y-1), u0=R^2, v0=R^3"
        ),
        "layers": [audit.as_json(include_matrix=include_matrices) for audit in audits],
        "all_layers_verified": all(audit.verified for audit in audits),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="archived exact_data.json")
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument(
        "--include-matrices",
        action="store_true",
        help="include every reconstructed matrix in the JSON report",
    )
    args = parser.parse_args(argv)
    try:
        document = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(document, dict):
            raise ValueError("input must be a JSON object")
        report = audit_document(document, include_matrices=args.include_matrices)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"degree21_linear_replay: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0 if report["all_layers_verified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
