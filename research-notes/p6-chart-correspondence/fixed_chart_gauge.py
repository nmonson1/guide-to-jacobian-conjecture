#!/usr/bin/env python3
"""Exact fixed-chart gauge quotient for one normal layer.

Let the leading face be

    P_0 = s^{-alpha} A_0(z),   Q_0 = s^{-beta} B_0(z),

and let a layer-r source vector field be

    V_{f,g} = s^r (f(z) partial_z + g(z) s partial_s).

Its action on the leading pair is

    Theta_r(f,g) = (f A_0' - alpha g A_0,
                    f B_0' - beta  g B_0).

Writing

    Psi = alpha A_0 B_0' - beta A_0' B_0,

one has the exact identity

    D_r Theta_r(f,g) = (f Psi)' + (r-alpha-beta) g Psi.

This program turns that identity into a finite support-aware calculation.  It
accepts Laurent exponent windows for f, g, a, and b; imposes both weighted
divergence zero and output-support conditions; computes the fixed-chart gauge
image; and compares it with the complete kernel of D_r on the supplied (a,b)
window.  All arithmetic is over Q.

The program does not infer the complete-chain support windows.  Those are
mathematical input and must be supplied from the chart under study.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from chart_correspondence import (
    Matrix,
    Vector,
    independent_extension,
    matrix_vector_product,
    nullspace,
    q,
    rank_of_vectors,
    rational_string,
    vector_json,
)

Poly = dict[int, Fraction]


def clean(poly: Mapping[int, Fraction]) -> Poly:
    return {
        exponent: coefficient
        for exponent, coefficient in poly.items()
        if coefficient
    }


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
    return clean(
        {exponent: coefficient * value for exponent, value in poly.items()}
    )


def multiply(
    left: Mapping[int, Fraction], right: Mapping[int, Fraction]
) -> Poly:
    result: Poly = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            result[exponent] = (
                result.get(exponent, Fraction(0))
                + left_coefficient * right_coefficient
            )
    return clean(result)


def derivative(poly: Mapping[int, Fraction]) -> Poly:
    return clean(
        {
            exponent - 1: Fraction(exponent) * coefficient
            for exponent, coefficient in poly.items()
            if exponent != 0
        }
    )


def parse_poly(values: Any, *, name: str) -> Poly:
    if not isinstance(values, list):
        raise ValueError(f"{name} must be a list of [exponent, coefficient] pairs")
    result: Poly = {}
    for index, item in enumerate(values):
        if not isinstance(item, list) or len(item) != 2:
            raise ValueError(f"{name}[{index}] must be [exponent, coefficient]")
        exponent, coefficient = item
        if not isinstance(exponent, int) or isinstance(exponent, bool):
            raise ValueError(f"{name}[{index}] exponent must be an integer")
        result[exponent] = result.get(exponent, Fraction(0)) + q(coefficient)
    return clean(result)


def parse_exponents(values: Any, *, name: str) -> list[int]:
    if not isinstance(values, list):
        raise ValueError(f"{name} must be a list of integers")
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in values):
        raise ValueError(f"{name} must contain only integers")
    if len(set(values)) != len(values):
        raise ValueError(f"{name} contains duplicate exponents")
    return list(values)


def poly_json(poly: Mapping[int, Fraction]) -> list[list[Any]]:
    return [
        [exponent, rational_string(coefficient)]
        for exponent, coefficient in sorted(poly.items())
        if coefficient
    ]


def linear_combination(columns: Sequence[Poly], vector: Vector) -> Poly:
    if len(columns) != len(vector):
        raise ValueError("column count does not match vector length")
    return add(*(scale(column, coefficient) for column, coefficient in zip(columns, vector)))


def face_volume(
    alpha: int,
    beta: int,
    A0: Mapping[int, Fraction],
    B0: Mapping[int, Fraction],
) -> Poly:
    return add(
        scale(multiply(A0, derivative(B0)), alpha),
        scale(multiply(derivative(A0), B0), -beta),
    )


def determinant_layer(
    alpha: int,
    beta: int,
    r: int,
    A0: Mapping[int, Fraction],
    B0: Mapping[int, Fraction],
    a: Mapping[int, Fraction],
    b: Mapping[int, Fraction],
) -> Poly:
    return add(
        scale(multiply(a, derivative(B0)), alpha - r),
        scale(multiply(B0, derivative(a)), -beta),
        scale(multiply(A0, derivative(b)), alpha),
        scale(multiply(b, derivative(A0)), r - beta),
    )


def theta(
    alpha: int,
    beta: int,
    A0: Mapping[int, Fraction],
    B0: Mapping[int, Fraction],
    f: Mapping[int, Fraction],
    g: Mapping[int, Fraction],
) -> tuple[Poly, Poly]:
    return (
        add(multiply(f, derivative(A0)), scale(multiply(g, A0), -alpha)),
        add(multiply(f, derivative(B0)), scale(multiply(g, B0), -beta)),
    )


def weighted_divergence(
    alpha: int,
    beta: int,
    r: int,
    psi: Mapping[int, Fraction],
    f: Mapping[int, Fraction],
    g: Mapping[int, Fraction],
) -> Poly:
    return add(
        derivative(multiply(f, psi)),
        scale(multiply(g, psi), r - alpha - beta),
    )


def theta_identity_residual(
    alpha: int,
    beta: int,
    r: int,
    A0: Mapping[int, Fraction],
    B0: Mapping[int, Fraction],
    f: Mapping[int, Fraction],
    g: Mapping[int, Fraction],
) -> Poly:
    psi = face_volume(alpha, beta, A0, B0)
    a, b = theta(alpha, beta, A0, B0, f, g)
    return add(
        determinant_layer(alpha, beta, r, A0, B0, a, b),
        scale(weighted_divergence(alpha, beta, r, psi, f, g), -1),
    )


def columns_to_matrix(columns: Sequence[Poly], exponents: Sequence[int]) -> Matrix:
    return [
        [column.get(exponent, Fraction(0)) for column in columns]
        for exponent in exponents
    ]


def output_vector(
    a: Mapping[int, Fraction],
    b: Mapping[int, Fraction],
    a_support: Sequence[int],
    b_support: Sequence[int],
) -> Vector:
    return [a.get(exponent, Fraction(0)) for exponent in a_support] + [
        b.get(exponent, Fraction(0)) for exponent in b_support
    ]


def output_pair(
    vector: Sequence[Fraction],
    a_support: Sequence[int],
    b_support: Sequence[int],
) -> tuple[Poly, Poly]:
    split = len(a_support)
    if len(vector) != split + len(b_support):
        raise ValueError("output vector has the wrong length")
    a = clean(dict(zip(a_support, vector[:split])))
    b = clean(dict(zip(b_support, vector[split:])))
    return a, b


def independent_vectors(vectors: Sequence[Vector], *, ambient_dimension: int) -> list[Vector]:
    _, added = independent_extension([], vectors, ambient_dimension=ambient_dimension)
    return added


@dataclass(frozen=True)
class FixedChartResult:
    label: str
    alpha: int
    beta: int
    r: int
    psi: Poly
    output_kernel_dimension: int
    admissible_source_dimension: int
    gauge_dimension: int
    stabilizer_dimension: int
    residual_dimension: int
    source_basis: list[Vector]
    gauge_basis: list[Vector]
    residual_representatives: list[Vector]
    a_support: list[int]
    b_support: list[int]
    source_variables: list[list[Any]]
    determinant_target_exponents: list[int]
    constraint_rows: list[list[Any]]
    determinant_operator: Matrix
    source_constraint_matrix: Matrix

    def as_json(self, *, include_matrices: bool = False) -> dict[str, Any]:
        result: dict[str, Any] = {
            "label": self.label,
            "alpha": self.alpha,
            "beta": self.beta,
            "r": self.r,
            "psi": poly_json(self.psi),
            "a_support": self.a_support,
            "b_support": self.b_support,
            "source_variables": self.source_variables,
            "determinant_target_exponents": self.determinant_target_exponents,
            "constraint_rows": self.constraint_rows,
            "output_kernel_dimension": self.output_kernel_dimension,
            "admissible_source_dimension": self.admissible_source_dimension,
            "gauge_dimension": self.gauge_dimension,
            "stabilizer_dimension": self.stabilizer_dimension,
            "residual_dimension": self.residual_dimension,
            "source_basis": [vector_json(vector) for vector in self.source_basis],
            "gauge_basis": [vector_json(vector) for vector in self.gauge_basis],
            "residual_representatives": [
                vector_json(vector) for vector in self.residual_representatives
            ],
        }
        if include_matrices:
            result["determinant_operator"] = [
                [rational_string(value) for value in row]
                for row in self.determinant_operator
            ]
            result["source_constraint_matrix"] = [
                [rational_string(value) for value in row]
                for row in self.source_constraint_matrix
            ]
        return result


def analyze_contract(contract: Mapping[str, Any]) -> FixedChartResult:
    label = contract.get("label", "fixed-chart layer")
    if not isinstance(label, str):
        raise ValueError("label must be a string")
    alpha = contract.get("alpha")
    beta = contract.get("beta")
    r = contract.get("r")
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in (alpha, beta, r)):
        raise ValueError("alpha, beta, and r must be integers")
    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive")

    A0 = parse_poly(contract.get("A0"), name="A0")
    B0 = parse_poly(contract.get("B0"), name="B0")
    if not A0 or not B0:
        raise ValueError("A0 and B0 must be nonzero")
    f_exponents = parse_exponents(contract.get("f_exponents"), name="f_exponents")
    g_exponents = parse_exponents(contract.get("g_exponents"), name="g_exponents")
    a_support = parse_exponents(contract.get("a_support"), name="a_support")
    b_support = parse_exponents(contract.get("b_support"), name="b_support")

    psi = face_volume(alpha, beta, A0, B0)
    if not psi:
        raise ValueError("the boundary-volume polynomial Psi vanishes identically")

    # The complete determinant operator on the requested output window.
    output_basis: list[tuple[str, int]] = [
        *(('a', exponent) for exponent in a_support),
        *(('b', exponent) for exponent in b_support),
    ]
    determinant_columns: list[Poly] = []
    for kind, exponent in output_basis:
        a = monomial(exponent) if kind == "a" else {}
        b = monomial(exponent) if kind == "b" else {}
        determinant_columns.append(
            determinant_layer(alpha, beta, r, A0, B0, a, b)
        )
    determinant_target_exponents = sorted(
        {exponent for column in determinant_columns for exponent in column}
    )
    determinant_operator = columns_to_matrix(
        determinant_columns, determinant_target_exponents
    )
    output_dimension = len(output_basis)
    output_kernel = nullspace(
        determinant_operator,
        ambient_dimension=output_dimension,
    )

    # Candidate source fields and their images.
    source_variables: list[list[Any]] = [
        *(["f", exponent] for exponent in f_exponents),
        *(["g", exponent] for exponent in g_exponents),
    ]
    a_columns: list[Poly] = []
    b_columns: list[Poly] = []
    divergence_columns: list[Poly] = []
    for kind, exponent in source_variables:
        f = monomial(exponent) if kind == "f" else {}
        g = monomial(exponent) if kind == "g" else {}
        residual = theta_identity_residual(alpha, beta, r, A0, B0, f, g)
        if residual:
            raise AssertionError(
                f"Theta identity failed on {(kind, exponent)}: {poly_json(residual)}"
            )
        a, b = theta(alpha, beta, A0, B0, f, g)
        a_columns.append(a)
        b_columns.append(b)
        divergence_columns.append(
            weighted_divergence(alpha, beta, r, psi, f, g)
        )

    allowed_a = set(a_support)
    allowed_b = set(b_support)
    divergence_exponents = sorted(
        {exponent for column in divergence_columns for exponent in column}
    )
    forbidden_a = sorted(
        {
            exponent
            for column in a_columns
            for exponent in column
            if exponent not in allowed_a
        }
    )
    forbidden_b = sorted(
        {
            exponent
            for column in b_columns
            for exponent in column
            if exponent not in allowed_b
        }
    )
    constraint_rows: list[list[Any]] = [
        *(["divergence", exponent] for exponent in divergence_exponents),
        *(["a-outside", exponent] for exponent in forbidden_a),
        *(["b-outside", exponent] for exponent in forbidden_b),
    ]
    source_constraint_matrix: Matrix = []
    for kind, exponent in constraint_rows:
        columns = (
            divergence_columns
            if kind == "divergence"
            else a_columns
            if kind == "a-outside"
            else b_columns
        )
        source_constraint_matrix.append(
            [column.get(exponent, Fraction(0)) for column in columns]
        )

    source_basis = nullspace(
        source_constraint_matrix,
        ambient_dimension=len(source_variables),
    )
    gauge_candidates: list[Vector] = []
    for source_vector in source_basis:
        a = linear_combination(a_columns, source_vector)
        b = linear_combination(b_columns, source_vector)
        if any(exponent not in allowed_a for exponent in a):
            raise AssertionError("source constraints failed to remove an a-support term")
        if any(exponent not in allowed_b for exponent in b):
            raise AssertionError("source constraints failed to remove a b-support term")
        gauge_vector = output_vector(a, b, a_support, b_support)
        image = matrix_vector_product(determinant_operator, gauge_vector)
        if any(image):
            raise AssertionError("a computed gauge vector is not in ker D_r")
        gauge_candidates.append(gauge_vector)

    gauge_basis = independent_vectors(
        gauge_candidates,
        ambient_dimension=output_dimension,
    )
    explained, residual_representatives = independent_extension(
        gauge_basis,
        output_kernel,
        ambient_dimension=output_dimension,
    )
    gauge_dimension = rank_of_vectors(
        gauge_basis,
        ambient_dimension=output_dimension,
    )
    output_kernel_dimension = rank_of_vectors(
        output_kernel,
        ambient_dimension=output_dimension,
    )
    explained_dimension = rank_of_vectors(
        explained,
        ambient_dimension=output_dimension,
    )
    if explained_dimension != output_kernel_dimension:
        raise AssertionError("gauge plus residual representatives do not span ker D_r")

    return FixedChartResult(
        label=label,
        alpha=alpha,
        beta=beta,
        r=r,
        psi=psi,
        output_kernel_dimension=output_kernel_dimension,
        admissible_source_dimension=len(source_basis),
        gauge_dimension=gauge_dimension,
        stabilizer_dimension=len(source_basis) - gauge_dimension,
        residual_dimension=len(residual_representatives),
        source_basis=source_basis,
        gauge_basis=gauge_basis,
        residual_representatives=residual_representatives,
        a_support=a_support,
        b_support=b_support,
        source_variables=source_variables,
        determinant_target_exponents=determinant_target_exponents,
        constraint_rows=constraint_rows,
        determinant_operator=determinant_operator,
        source_constraint_matrix=source_constraint_matrix,
    )


def analyze_document(document: Mapping[str, Any]) -> list[FixedChartResult]:
    layers = document.get("layers")
    if layers is None:
        return [analyze_contract(document)]
    if not isinstance(layers, list):
        raise ValueError("layers must be a list")
    common = {key: value for key, value in document.items() if key != "layers"}
    results: list[FixedChartResult] = []
    for index, layer in enumerate(layers):
        if not isinstance(layer, dict):
            raise ValueError(f"layers[{index}] must be an object")
        contract = {**common, **layer}
        results.append(analyze_contract(contract))
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--include-matrices", action="store_true")
    args = parser.parse_args(argv)
    try:
        document = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(document, dict):
            raise ValueError("input must be a JSON object")
        results = analyze_document(document)
        report = {
            "schema_version": 1,
            "identity": "D_r Theta_r(f,g)=(f Psi)' +(r-alpha-beta)g Psi",
            "results": [
                result.as_json(include_matrices=args.include_matrices)
                for result in results
            ],
        }
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"fixed_chart_gauge: {exc}", file=sys.stderr)
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
