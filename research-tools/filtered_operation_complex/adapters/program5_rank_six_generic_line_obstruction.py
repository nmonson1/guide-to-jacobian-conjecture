#!/usr/bin/env python3
"""Compute the cubic obstruction for every finite line in the selected plane.

Write the finite projective tangent direction as

    theta(r) = theta_v + r theta_u.

The quadratic Kuranishi class vanishes identically on this plane.  This module
constructs, over Q(r), the cubic tangent-effect matrix E(r) and deterministic
cubic residual b(r).  It then computes a primitive polynomial generator of
the left kernel of E(r).  When that generator has coprime coordinates and its
pairing with b(r) is a nonzero constant, it certifies obstruction for every
finite algebraic value of r at once.

The point at infinity theta_u is excluded and is audited separately by
``program5_rank_six_line_formal_arc.py``.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Sequence

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from .program5_compression_export import DEFAULT_SOURCE, _q
from .program5_rank_six_schur_model import build_schur_model
from .program5_rank_six_second_order import _flatten


def _digest(expressions: Sequence[sp.Expr]) -> str:
    payload = [str(sp.factor(expression)) for expression in expressions]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _global_coefficient_denominator(
    expressions: Sequence[sp.Expr],
    variable: sp.Symbol,
) -> int:
    denominator = 1
    for expression in expressions:
        polynomial = sp.Poly(expression, variable, domain=sp.QQ)
        for coefficient in polynomial.all_coeffs():
            denominator = sp.ilcm(
                denominator,
                int(sp.denom(coefficient)),
            )
    return denominator


def _primitive_polynomial_vector(
    vector: sp.Matrix,
    variable: sp.Symbol,
) -> tuple[sp.Matrix, sp.Expr, sp.Expr]:
    fractions = [sp.cancel(value) for value in vector]
    denominator_lcm: sp.Expr = sp.Integer(1)
    for value in fractions:
        denominator_lcm = sp.lcm(
            denominator_lcm,
            sp.denom(value),
        )
    polynomial_entries = [
        sp.Poly(
            sp.cancel(value * denominator_lcm),
            variable,
            domain=sp.QQ,
        ).as_expr()
        for value in fractions
    ]
    nonzero_polynomials = [
        sp.Poly(value, variable, domain=sp.QQ)
        for value in polynomial_entries
        if value != 0
    ]
    if not nonzero_polynomials:
        raise AssertionError("zero left-kernel vector")
    common = nonzero_polynomials[0]
    for polynomial in nonzero_polynomials[1:]:
        common = sp.gcd(common, polynomial)
    common_expression = common.monic().as_expr()
    polynomial_entries = [
        sp.cancel(value / common_expression)
        for value in polynomial_entries
    ]
    coefficient_denominator = _global_coefficient_denominator(
        polynomial_entries,
        variable,
    )
    polynomial_entries = [
        sp.expand(coefficient_denominator * value)
        for value in polynomial_entries
    ]
    integer_coefficients = []
    for value in polynomial_entries:
        integer_coefficients.extend(
            int(coefficient)
            for coefficient in sp.Poly(value, variable, domain=sp.ZZ).all_coeffs()
        )
    content = 0
    for coefficient in integer_coefficients:
        content = sp.igcd(content, abs(coefficient))
    if content > 1:
        polynomial_entries = [
            sp.expand(value / content)
            for value in polynomial_entries
        ]
    first_nonzero = next(value for value in polynomial_entries if value != 0)
    if sp.LC(sp.Poly(first_nonzero, variable, domain=sp.QQ)) < 0:
        polynomial_entries = [-value for value in polynomial_entries]
    primitive = sp.Matrix(polynomial_entries)

    primitive_nonzero = [
        sp.Poly(value, variable, domain=sp.QQ)
        for value in primitive
        if value != 0
    ]
    primitive_gcd = primitive_nonzero[0]
    for polynomial in primitive_nonzero[1:]:
        primitive_gcd = sp.gcd(primitive_gcd, polynomial)
    return primitive, sp.factor(denominator_lcm), primitive_gcd.monic().as_expr()


def analyze_generic_line_obstruction(
    source_path: Path = DEFAULT_SOURCE,
) -> dict[str, Any]:
    model = build_schur_model(source_path)
    r = sp.symbols("r")
    theta = model.theta_v + r * model.theta_u
    theta_block = model.blocks(theta)

    H2 = model.quadratic_forcing(theta_block)
    forcing2 = _flatten(H2)
    residual2 = model.project(forcing2)
    residual2 = residual2.applyfunc(sp.factor)
    if any(value != 0 for value in residual2):
        raise AssertionError("the selected plane lost second-order compatibility")

    coefficients = model.minor_inverse * forcing2[list(model.pivot_rows), :]
    P2 = sp.zeros(model.ambient_operation_dimension, 1)
    for index, column in enumerate(model.pivot_operation_columns):
        P2[column, 0] = sp.factor(coefficients[index, 0])
    if any(
        sp.factor(value) != 0
        for value in model.L * P2 - forcing2
    ):
        raise AssertionError("symbolic quadratic image solution failed")

    P2_block = model.blocks(P2)
    cubic_residual = model.project(
        _flatten(model.cubic_forcing(theta_block, P2_block))
    ).applyfunc(sp.factor)
    tangent_blocks = [model.blocks(vector) for vector in model.tangent_basis]
    effect_columns = [
        model.project(
            _flatten(model.bilinear_effect(tangent_block, theta_block))
        ).applyfunc(sp.factor)
        for tangent_block in tangent_blocks
    ]
    active_rows = sorted(
        {
            row
            for row, value in enumerate(cubic_residual)
            if value != 0
        }
        | {
            row
            for column in effect_columns
            for row, value in enumerate(column)
            if value != 0
        }
    )
    effect_matrix = sp.Matrix(
        [
            [column[row, 0] for column in effect_columns]
            for row in active_rows
        ]
    )
    residual_vector = sp.Matrix(
        [cubic_residual[row, 0] for row in active_rows]
    )

    effect_rank = DomainMatrix.from_Matrix(
        effect_matrix,
        fmt="sparse",
    ).to_field().rank()
    augmented_rank = DomainMatrix.from_Matrix(
        effect_matrix.row_join(residual_vector),
        fmt="sparse",
    ).to_field().rank()
    left_kernel = effect_matrix.T.nullspace()
    if len(left_kernel) != len(active_rows) - effect_rank:
        raise AssertionError("symbolic left-nullity disagrees with rank")
    if len(left_kernel) != 1:
        raise AssertionError(
            "expected a one-dimensional generic left kernel, got "
            f"{len(left_kernel)}"
        )

    witness, cleared_denominator, coordinate_gcd = (
        _primitive_polynomial_vector(left_kernel[0], r)
    )
    if any(
        sp.factor(value) != 0
        for value in witness.T * effect_matrix
    ):
        raise AssertionError("primitive witness does not annihilate E(r)")
    pairing = sp.factor((witness.T * residual_vector)[0, 0])
    pairing_polynomial = sp.Poly(pairing, r, domain=sp.QQ)
    universal = coordinate_gcd == 1 and pairing_polynomial.degree() == 0 and pairing != 0

    witness_coordinates = []
    for local_row, coefficient in enumerate(witness):
        if coefficient == 0:
            continue
        coordinate = model.residual_coordinate(active_rows[local_row])
        witness_coordinates.append(
            {
                **coordinate,
                "coefficient_polynomial": str(sp.factor(coefficient)),
            }
        )

    sample_checks = []
    for value in (-3, -2, -1, 0, 1, 2, 3, 4, 5):
        substitution = {r: sp.Rational(value)}
        specialized_witness = witness.subs(substitution)
        specialized_pairing = sp.factor(pairing.subs(substitution))
        if specialized_witness == sp.zeros(witness.rows, 1):
            raise AssertionError(f"primitive witness vanished at r={value}")
        if specialized_pairing == 0 and universal:
            raise AssertionError(f"constant obstruction vanished at r={value}")
        sample_checks.append(
            {
                "u_over_v": value,
                "witness_nonzero_count": sum(
                    entry != 0 for entry in specialized_witness
                ),
                "pairing": _q(specialized_pairing),
            }
        )

    return {
        "schema_version": 1,
        "name": "Program 5 symbolic finite-ratio cubic obstruction",
        "source_file": str(source_path),
        "source_sha256": model.source_sha256,
        "parameter": "r=u/v",
        "direction": "theta_v + r*theta_u",
        "ambient_operation_dimension": model.ambient_operation_dimension,
        "rank_six_tangent_dimension": len(model.tangent_basis),
        "second_order_residual_identically_zero": True,
        "compressed_cubic_equation_count": len(active_rows),
        "generic_effect_rank_over_Q(r)": effect_rank,
        "generic_augmented_rank_over_Q(r)": augmented_rank,
        "left_kernel_dimension_over_Q(r)": len(left_kernel),
        "primitive_left_kernel": {
            "cleared_denominator": str(cleared_denominator),
            "coordinate_gcd": str(sp.factor(coordinate_gcd)),
            "nonzero_count": len(witness_coordinates),
            "sha256": _digest(list(witness)),
            "coordinates": witness_coordinates,
        },
        "pairing_with_cubic_residual": str(pairing),
        "pairing_degree": pairing_polynomial.degree(),
        "universal_obstruction_for_all_finite_algebraic_ratios": universal,
        "sample_checks": sample_checks,
        "interpretation_boundary": (
            "The certificate concerns all finite lines in this selected "
            "second-order-compatible tangent plane. It does not classify "
            "directions outside the plane or the point at infinity theta_u."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = analyze_generic_line_obstruction(args.source)
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(
            f"program5_rank_six_generic_line_obstruction: {exc}",
            file=sys.stderr,
        )
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
