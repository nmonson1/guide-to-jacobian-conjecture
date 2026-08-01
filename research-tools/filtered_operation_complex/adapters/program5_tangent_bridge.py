#!/usr/bin/env python3
"""Analyze the two rank-six tangent directions outside the row-zero chart.

The exact public Program 5 compression packet gives two nested tangent spaces
inside the 115-dimensional space of weight-preserving quadratic vector fields:

    K_row  = directions preserving the equations that the a,d,q,h,k rows vanish;
    K_rank = tangent directions to the rank-at-most-six cubic-coordinate locus
             at P0=-d^2 e_a.

Their dimensions are 20 and 22.  This script verifies ``K_row <= K_rank``,
constructs an adapted basis ``K_row + <eta_0,eta_1>``, and restricts the exact
quartic functional Lambda_4(O_4(P)) to

    P = P0 + sum_i s_i K_row[i] + u eta_0 + v eta_1.

The calculation is exact over Q.  It is a tangent-coupling diagnostic, not an
integration theorem for the rank-six determinantal locus and not a quotient by
all polynomial/stable automorphisms.
"""
from __future__ import annotations

import argparse
import json
import sys
from itertools import combinations_with_replacement
from pathlib import Path
from typing import Any, Mapping, Sequence

import sympy as sp

from .program5_compression_export import (
    DEFAULT_SOURCE,
    _basis_index,
    _load_source,
    _monomial_label,
    _q,
    build_export,
)


def _sympy_matrix(values: Sequence[Sequence[Any]]) -> sp.Matrix:
    return sp.Matrix(
        [
            [sp.Rational(value) for value in row]
            for row in values
        ]
    )


def _extend_basis(
    base_columns: Sequence[sp.Matrix],
    candidates: Sequence[sp.Matrix],
) -> tuple[list[sp.Matrix], list[sp.Matrix]]:
    accepted = list(base_columns)
    rank = sp.Matrix.hstack(*accepted).rank() if accepted else 0
    added: list[sp.Matrix] = []
    for candidate in candidates:
        trial = sp.Matrix.hstack(*accepted, candidate)
        trial_rank = trial.rank()
        if trial_rank > rank:
            accepted.append(candidate)
            added.append(candidate)
            rank = trial_rank
    return accepted, added


def _sparse_vector(
    vector: sp.Matrix,
    labels: Sequence[str],
) -> list[dict[str, Any]]:
    return [
        {"coordinate": labels[index], "coefficient": _q(vector[index, 0])}
        for index in range(vector.rows)
        if vector[index, 0] != 0
    ]


def _polynomial_terms(
    expression: sp.Expr,
    variables: Sequence[sp.Symbol],
) -> list[dict[str, Any]]:
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    terms = []
    for exponents, coefficient in polynomial.terms():
        monomial_parts = []
        for variable, exponent in zip(variables, exponents):
            if exponent == 0:
                continue
            monomial_parts.append(
                str(variable) if exponent == 1 else f"{variable}^{exponent}"
            )
        terms.append(
            {
                "exponents": list(exponents),
                "monomial": "*".join(monomial_parts) or "1",
                "coefficient": _q(coefficient),
            }
        )
    return terms


def analyze_bridge(source_path: Path = DEFAULT_SOURCE) -> dict[str, Any]:
    contract, exported = build_export(source_path)
    row_layer, rank_layer = contract["layers"]
    operation_labels = list(row_layer["deformation_basis"])

    row_kernel_matrix = _sympy_matrix(
        row_layer["actions"][0]["action_matrix"]
    )
    rank_kernel_matrix = _sympy_matrix(
        rank_layer["actions"][0]["action_matrix"]
    )
    row_columns = [
        row_kernel_matrix[:, index]
        for index in range(row_kernel_matrix.cols)
    ]
    rank_columns = [
        rank_kernel_matrix[:, index]
        for index in range(rank_kernel_matrix.cols)
    ]
    if row_kernel_matrix.rank() != 20 or rank_kernel_matrix.rank() != 22:
        raise AssertionError("the exported tangent bases lost rank")
    if sp.Matrix.hstack(rank_kernel_matrix, row_kernel_matrix).rank() != 22:
        raise AssertionError("the row-zero tangent is not contained in the rank-six tangent")

    adapted_columns, complement = _extend_basis(row_columns, rank_columns)
    if len(adapted_columns) != 22 or len(complement) != 2:
        raise AssertionError(
            f"expected a two-dimensional tangent excess, found {len(complement)}"
        )
    adapted_matrix = sp.Matrix.hstack(*adapted_columns)

    source, _ = _load_source(source_path)
    V = tuple(source.V)
    Q = sp.Matrix(source.Q)
    C = sp.Matrix(source.C)
    weights = source.weights
    n = len(V)
    quadratic_monomials = [
        sp.prod(V[index] for index in indices)
        for indices in combinations_with_replacement(range(n), 2)
    ]

    def weight(monomial: sp.Expr) -> int:
        exponents = sp.Poly(monomial, *V).monoms()[0]
        return sum(exponents[index] * weights[V[index]] for index in range(n))

    operation_basis: list[tuple[int, sp.Expr]] = []
    for row, variable in enumerate(V):
        for monomial in quadratic_monomials:
            if weight(monomial) == weights[variable]:
                operation_basis.append((row, monomial))
    if len(operation_basis) != 115:
        raise AssertionError("the operation basis no longer has dimension 115")
    reconstructed_labels = [
        f"e_{V[row]}*{_monomial_label(monomial)}"
        for row, monomial in operation_basis
    ]
    if reconstructed_labels != operation_labels:
        raise AssertionError("the operation-basis order changed")

    parameters = sp.symbols("s0:20") + sp.symbols("u v")
    coefficient_vector = adapted_matrix * sp.Matrix(parameters)
    p0_index = _basis_index(operation_basis, 3, source.d**2)
    coefficient_vector[p0_index, 0] -= 1

    P = sp.zeros(n, 1)
    for coefficient, (row, monomial) in zip(coefficient_vector, operation_basis):
        if coefficient:
            P[row, 0] += coefficient * monomial
    P = sp.Matrix([sp.expand(value) for value in P])
    JQ = Q.jacobian(V)
    O4 = (
        C.jacobian(V) * P
        - P.jacobian(V) * C
        + sp.Rational(1, 2) * source.D2_11(Q, P, P)
        - P.jacobian(V) * (JQ * P - P.jacobian(V) * Q)
        - sp.Rational(1, 2) * source.D2_11(P, Q, Q)
    )
    Lambda = sp.expand(
        sum(
            coefficient
            * sp.Poly(sp.expand(O4[row]), *V).coeff_monomial(monomial)
            for row, monomial, coefficient in source.terms
        )
    )
    polynomial = sp.Poly(Lambda, *parameters, domain=sp.QQ)
    if polynomial.total_degree() > 2:
        raise AssertionError("the quartic functional restriction should be quadratic")

    row_parameters = parameters[:20]
    extra_parameters = parameters[20:]
    row_chart_restriction = sp.expand(
        Lambda.subs({parameter: 0 for parameter in extra_parameters})
    )
    if row_chart_restriction != 1:
        raise AssertionError(
            f"Lambda_4 is not constant one on the row-zero slice: {row_chart_restriction}"
        )

    extra_plane_restriction = sp.factor(
        Lambda.subs({parameter: 0 for parameter in row_parameters})
    )
    linear_extra = [
        sp.expand(sp.diff(Lambda, parameter).subs({value: 0 for value in parameters}))
        for parameter in extra_parameters
    ]
    hessian_extra = sp.Matrix(
        [
            [
                sp.expand(
                    sp.diff(Lambda, left, right).subs(
                        {value: 0 for value in parameters}
                    )
                )
                for right in extra_parameters
            ]
            for left in extra_parameters
        ]
    )

    nonconstant = sp.expand(Lambda - 1) != 0
    pure_row_terms = []
    mixed_terms = []
    pure_extra_terms = []
    for term in _polynomial_terms(Lambda - 1, parameters):
        exponents = term["exponents"]
        row_degree = sum(exponents[:20])
        extra_degree = sum(exponents[20:])
        if row_degree and not extra_degree:
            pure_row_terms.append(term)
        elif row_degree and extra_degree:
            mixed_terms.append(term)
        elif extra_degree:
            pure_extra_terms.append(term)
    if pure_row_terms:
        raise AssertionError("pure row-zero tangent terms should vanish")

    rational_cancellation: dict[str, Any] | None = None
    u, v = extra_parameters
    if linear_extra[0] != 0:
        value = sp.factor(-1 / linear_extra[0])
        if sp.expand(extra_plane_restriction.subs({u: value, v: 0})) == 0:
            rational_cancellation = {
                "u": _q(value),
                "v": 0,
                "verification": "Lambda_4=0 on the complement plane",
            }
    if rational_cancellation is None and linear_extra[1] != 0:
        value = sp.factor(-1 / linear_extra[1])
        if sp.expand(extra_plane_restriction.subs({u: 0, v: value})) == 0:
            rational_cancellation = {
                "u": 0,
                "v": _q(value),
                "verification": "Lambda_4=0 on the complement plane",
            }

    summary = exported["summary"]
    return {
        "schema_version": 1,
        "name": "Program 5 row-zero to rank-six tangent bridge",
        "source_file": str(source_path),
        "source_sha256": summary["source_sha256"],
        "ambient_operation_dimension": 115,
        "row_zero_tangent_dimension": 20,
        "rank_six_tangent_dimension": 22,
        "inclusion_rank": 20,
        "tangent_excess_dimension": 2,
        "adapted_basis": {
            "first_20": "the exported row-zero tangent basis",
            "complement": [
                {
                    "name": f"eta_{index}",
                    "vector": _sparse_vector(vector, operation_labels),
                }
                for index, vector in enumerate(complement)
            ],
        },
        "quartic_restriction": {
            "functional": "Lambda_4(O_4(P))",
            "total_degree": polynomial.total_degree(),
            "term_count": len(polynomial.terms()),
            "constant_on_row_zero_slice": True,
            "row_zero_value": 1,
            "nonconstant_on_full_rank_six_tangent_plane": nonconstant,
            "extra_plane_expression": str(extra_plane_restriction),
            "linear_coefficients_in_eta_coordinates": [
                _q(value) for value in linear_extra
            ],
            "extra_hessian": [
                [_q(hessian_extra[row, column]) for column in range(2)]
                for row in range(2)
            ],
            "pure_extra_terms": pure_extra_terms,
            "mixed_row_extra_terms": mixed_terms,
            "full_terms": _polynomial_terms(Lambda, parameters),
            "rational_cancellation_on_complement_plane": rational_cancellation,
        },
        "interpretation_boundary": (
            "The two complement vectors are tangent to the rank-at-most-six "
            "determinantal locus. This calculation does not prove that their "
            "finite affine plane integrates inside that locus, nor that they "
            "survive quotienting by all source, target, and stable operations."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = analyze_bridge(args.source)
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(f"program5_tangent_bridge: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
