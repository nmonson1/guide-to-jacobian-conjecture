#!/usr/bin/env python3
"""Compute the intrinsic fourth-order Kuranishi map for ``theta_u``.

The first-order direction

    theta_u = eta_0 + xi_4

has a solvable cubic lifting equation.  That equation has rank two on the
22-dimensional tangent kernel, so its quadratic correction is not unique: it
has a 20-dimensional affine family.  A quartic failure obtained after setting
those twenty free parameters to zero is therefore only branch-specific.

This adapter retains the complete cubic-lift fibre.  It constructs a
particular quadratic correction, a basis N_0,...,N_19 of the homogeneous
cubic-compatible quadratic corrections, and the exact degree-at-most-two map

    kappa_4(z_0,...,z_19)

obtained by projecting the fourth-order forcing modulo both the rank-six
tangent image and the order-three tangent-effect image.  It also searches for
a rational zero of the displayed polynomial system.

This is a formal local rank-at-most-six calculation.  It does not impose the
quartic compression functional, classify the full infinity first-order fibre,
or prove convergence/algebraization.
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
from .program5_rank_six_second_order import (
    _flatten,
    _independent_rows_and_columns,
)


def _digest(vector: sp.Matrix) -> str:
    payload = [str(sp.factor(sp.cancel(value))) for value in vector]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _nonzero_count(vector: sp.Matrix) -> int:
    return sum(sp.factor(sp.cancel(value)) != 0 for value in vector)


def _deterministic_solution(
    matrix: sp.Matrix,
    rhs: sp.Matrix,
) -> tuple[sp.Matrix, int]:
    solution_tuple = next(iter(sp.linsolve((matrix, rhs))))
    free_symbols = sorted(
        set().union(*(entry.free_symbols for entry in solution_tuple)),
        key=str,
    )
    substitution = {symbol: 0 for symbol in free_symbols}
    solution = sp.Matrix(
        [
            sp.factor(sp.cancel(entry.subs(substitution)))
            for entry in solution_tuple
        ]
    )
    error = (matrix * solution - rhs).applyfunc(
        lambda value: sp.factor(sp.cancel(value))
    )
    if any(value != 0 for value in error):
        raise AssertionError("deterministic affine solution failed")
    return solution, len(free_symbols)


def _project_modulo_image(
    vector: sp.Matrix,
    matrix: sp.Matrix,
) -> tuple[sp.Matrix, tuple[int, ...], tuple[int, ...]]:
    pivot_rows, pivot_columns = _independent_rows_and_columns(matrix)
    minor = matrix[pivot_rows, pivot_columns]
    inverse = minor.inv()
    coefficients = inverse * vector[list(pivot_rows), :]
    residual = (
        vector - matrix[:, list(pivot_columns)] * coefficients
    ).applyfunc(lambda value: sp.factor(sp.cancel(value)))
    if any(residual[row, 0] != 0 for row in pivot_rows):
        raise AssertionError("secondary cokernel projection kept a pivot row")
    return residual, tuple(pivot_rows), tuple(pivot_columns)


def _polynomial_terms(
    expression: sp.Expr,
    variables: Sequence[sp.Symbol],
) -> list[dict[str, Any]]:
    polynomial = sp.Poly(expression, *variables, domain=sp.QQ)
    terms = []
    for exponents, coefficient in polynomial.terms():
        monomial_factors = []
        for variable, exponent in zip(variables, exponents):
            if exponent == 1:
                monomial_factors.append(str(variable))
            elif exponent > 1:
                monomial_factors.append(f"{variable}^{exponent}")
        terms.append(
            {
                "monomial": "*".join(monomial_factors) or "1",
                "exponents": list(exponents),
                "coefficient": _q(coefficient),
            }
        )
    return terms


def _rational_single_coordinate_solution(
    equations: Sequence[sp.Expr],
    variables: Sequence[sp.Symbol],
) -> dict[sp.Symbol, sp.Rational] | None:
    t = sp.symbols("t")
    zero_substitution = {variable: 0 for variable in variables}
    if all(sp.factor(expression.subs(zero_substitution)) == 0 for expression in equations):
        return {variable: sp.Rational(0) for variable in variables}

    for variable in variables:
        substitution = {
            other: (t if other == variable else 0)
            for other in variables
        }
        polynomials = [
            sp.Poly(
                sp.factor(expression.subs(substitution)),
                t,
                domain=sp.QQ,
            )
            for expression in equations
        ]
        nonzero = [polynomial for polynomial in polynomials if not polynomial.is_zero]
        if not nonzero:
            return {
                other: (sp.Rational(1) if other == variable else sp.Rational(0))
                for other in variables
            }
        common = nonzero[0]
        for polynomial in nonzero[1:]:
            common = sp.gcd(common, polynomial)
        for root in sp.roots(common.as_expr(), t):
            if root.is_Rational:
                candidate = {
                    other: (sp.Rational(root) if other == variable else sp.Rational(0))
                    for other in variables
                }
                if all(
                    sp.factor(expression.subs(candidate)) == 0
                    for expression in equations
                ):
                    return candidate

    for fixed_index, fixed_variable in enumerate(variables):
        for fixed_value in (sp.Rational(1), sp.Rational(-1)):
            for solved_variable in variables[fixed_index + 1 :]:
                substitution = {
                    variable: (
                        fixed_value
                        if variable == fixed_variable
                        else (t if variable == solved_variable else 0)
                    )
                    for variable in variables
                }
                polynomials = [
                    sp.Poly(
                        sp.factor(expression.subs(substitution)),
                        t,
                        domain=sp.QQ,
                    )
                    for expression in equations
                ]
                nonzero = [
                    polynomial
                    for polynomial in polynomials
                    if not polynomial.is_zero
                ]
                if not nonzero:
                    candidate = {
                        variable: (
                            fixed_value
                            if variable == fixed_variable
                            else (
                                sp.Rational(0)
                                if variable != solved_variable
                                else sp.Rational(0)
                            )
                        )
                        for variable in variables
                    }
                    return candidate
                common = nonzero[0]
                for polynomial in nonzero[1:]:
                    common = sp.gcd(common, polynomial)
                for root in sp.roots(common.as_expr(), t):
                    if root.is_Rational:
                        candidate = {
                            variable: (
                                fixed_value
                                if variable == fixed_variable
                                else (
                                    sp.Rational(root)
                                    if variable == solved_variable
                                    else sp.Rational(0)
                                )
                            )
                            for variable in variables
                        }
                        if all(
                            sp.factor(expression.subs(candidate)) == 0
                            for expression in equations
                        ):
                            return candidate
    return None


def analyze_fourth_order_kuranishi(
    source_path: Path = DEFAULT_SOURCE,
) -> dict[str, Any]:
    model = build_schur_model(source_path)
    theta = model.theta_u
    theta_block = model.blocks(theta)
    tangent_matrix = sp.Matrix.hstack(*model.tangent_basis)
    tangent_blocks = [model.blocks(vector) for vector in model.tangent_basis]

    H2 = model.quadratic_forcing(theta_block)
    if any(value != 0 for value in model.project(_flatten(H2))):
        raise AssertionError("theta_u lost second-order compatibility")
    P2_image_particular = model.solve_image(H2)

    cubic_residual = model.project(
        _flatten(
            model.cubic_forcing(
                theta_block,
                model.blocks(P2_image_particular),
            )
        )
    )
    effect_columns = [
        model.project(
            _flatten(model.bilinear_effect(tangent_block, theta_block))
        )
        for tangent_block in tangent_blocks
    ]
    effect_matrix = sp.Matrix.hstack(*effect_columns)
    effect_rank = DomainMatrix.from_Matrix(
        effect_matrix,
        fmt="sparse",
    ).rank()
    augmented_rank = DomainMatrix.from_Matrix(
        effect_matrix.row_join(-cubic_residual),
        fmt="sparse",
    ).rank()
    if effect_rank != augmented_rank:
        raise AssertionError("theta_u cubic lift became obstructed")

    tangent_coordinates, reported_free_dimension = _deterministic_solution(
        effect_matrix,
        -cubic_residual,
    )
    tangent_particular = tangent_matrix * tangent_coordinates
    P2_base = P2_image_particular + tangent_particular
    cubic_check = model.project(
        _flatten(model.cubic_forcing(theta_block, model.blocks(P2_base)))
    )
    if any(value != 0 for value in cubic_check):
        raise AssertionError("particular quadratic correction did not kill cubic forcing")

    kernel_coordinates = effect_matrix.nullspace()
    if len(kernel_coordinates) != len(model.tangent_basis) - effect_rank:
        raise AssertionError("cubic-effect nullity changed")
    if reported_free_dimension != len(kernel_coordinates):
        raise AssertionError("linsolve free dimension disagrees with nullspace")
    homogeneous_directions = [
        tangent_matrix * coordinates
        for coordinates in kernel_coordinates
    ]

    _, effect_pivot_rows, effect_pivot_columns = _project_modulo_image(
        sp.zeros(effect_matrix.rows, 1),
        effect_matrix,
    )
    effect_minor = effect_matrix[effect_pivot_rows, effect_pivot_columns]
    effect_minor_inverse = effect_minor.inv()

    def project_effect(vector: sp.Matrix) -> sp.Matrix:
        coefficients = effect_minor_inverse * vector[list(effect_pivot_rows), :]
        residual = (
            vector
            - effect_matrix[:, list(effect_pivot_columns)] * coefficients
        ).applyfunc(lambda value: sp.factor(sp.cancel(value)))
        if any(residual[row, 0] != 0 for row in effect_pivot_rows):
            raise AssertionError("order-three cokernel projection kept a pivot row")
        return residual

    def forcing_through_four(P2: sp.Matrix) -> sp.Matrix:
        block1 = theta_block
        block2 = model.blocks(P2)
        G0 = model.G0
        G1 = -G0 * block1["A"] * G0
        G2 = -G0 * (
            block1["A"] * G1 + block2["A"] * G0
        )

        H3 = (
            block1["C"] * G0 * block2["B"]
            + block1["C"] * G1 * block1["B"]
            + block1["C"] * G2 * model.B0
            + block2["C"] * G0 * block1["B"]
            + block2["C"] * G1 * model.B0
        ).applyfunc(lambda value: sp.factor(sp.cancel(value)))
        if any(value != 0 for value in model.project(_flatten(H3))):
            raise AssertionError("quadratic correction left cubic forcing")
        P3 = model.solve_image(H3)
        block3 = model.blocks(P3)
        G3 = -G0 * (
            block1["A"] * G2
            + block2["A"] * G1
            + block3["A"] * G0
        )

        blocks = {1: block1, 2: block2, 3: block3}
        inverses = {0: G0, 1: G1, 2: G2, 3: G3}
        B_series = {0: model.B0, 1: block1["B"], 2: block2["B"], 3: block3["B"]}
        H4 = sp.zeros(len(model.zero_rows), len(model.nonpivot_columns))
        for i_order in range(1, 4):
            for j_order in range(0, 4 - i_order + 1):
                k_order = 4 - i_order - j_order
                if k_order in B_series:
                    H4 += (
                        blocks[i_order]["C"]
                        * inverses[j_order]
                        * B_series[k_order]
                    )
        residual4 = model.project(_flatten(H4))
        return project_effect(residual4)

    q0 = forcing_through_four(P2_base)
    plus_values = []
    minus_values = []
    linear_coefficients = []
    diagonal_coefficients = []
    for direction in homogeneous_directions:
        plus = forcing_through_four(P2_base + direction)
        minus = forcing_through_four(P2_base - direction)
        plus_values.append(plus)
        minus_values.append(minus)
        linear_coefficients.append(
            ((plus - minus) / 2).applyfunc(
                lambda value: sp.factor(sp.cancel(value))
            )
        )
        diagonal_coefficients.append(
            ((plus + minus - 2 * q0) / 2).applyfunc(
                lambda value: sp.factor(sp.cancel(value))
            )
        )

    off_diagonal_coefficients: dict[tuple[int, int], sp.Matrix] = {}
    for left in range(len(homogeneous_directions)):
        for right in range(left + 1, len(homogeneous_directions)):
            value = forcing_through_four(
                P2_base
                + homogeneous_directions[left]
                + homogeneous_directions[right]
            )
            off_diagonal_coefficients[(left, right)] = (
                value - plus_values[left] - plus_values[right] + q0
            ).applyfunc(lambda entry: sp.factor(sp.cancel(entry)))

    coefficient_vectors = [q0]
    coefficient_labels = ["1"]
    coefficient_vectors.extend(linear_coefficients)
    coefficient_labels.extend(
        f"z_{index}" for index in range(len(homogeneous_directions))
    )
    coefficient_vectors.extend(diagonal_coefficients)
    coefficient_labels.extend(
        f"z_{index}^2" for index in range(len(homogeneous_directions))
    )
    for (left, right), vector in off_diagonal_coefficients.items():
        coefficient_vectors.append(vector)
        coefficient_labels.append(f"z_{left}*z_{right}")

    coefficient_matrix = sp.Matrix.hstack(*coefficient_vectors)
    coefficient_rank = DomainMatrix.from_Matrix(
        coefficient_matrix,
        fmt="sparse",
    ).rank()
    _, independent_equation_rows = coefficient_matrix.T.rref()
    independent_equation_rows = list(independent_equation_rows)
    variables = sp.symbols(f"z0:{len(homogeneous_directions)}")
    equations = []
    for row in independent_equation_rows:
        expression = q0[row, 0]
        for index, vector in enumerate(linear_coefficients):
            expression += vector[row, 0] * variables[index]
        for index, vector in enumerate(diagonal_coefficients):
            expression += vector[row, 0] * variables[index] ** 2
        for (left, right), vector in off_diagonal_coefficients.items():
            expression += vector[row, 0] * variables[left] * variables[right]
        expression = sp.factor(expression)
        coordinate = model.residual_coordinate(row)
        equations.append(
            {
                "residual_row": row,
                **coordinate,
                "expression": str(expression),
                "total_degree": sp.Poly(expression, *variables).total_degree(),
                "terms": _polynomial_terms(expression, variables),
            }
        )

    equation_expressions = [
        sp.sympify(equation["expression"], locals={str(v): v for v in variables})
        for equation in equations
    ]
    rational_solution = _rational_single_coordinate_solution(
        equation_expressions,
        variables,
    )
    solution_record = None
    verified_rational_zero = False
    if rational_solution is not None:
        verified_rational_zero = all(
            sp.factor(expression.subs(rational_solution)) == 0
            for expression in equation_expressions
        )
        if not verified_rational_zero:
            raise AssertionError("reported rational quartic zero did not verify")
        free_adjustment = sp.zeros(model.ambient_operation_dimension, 1)
        coefficients = []
        for index, variable in enumerate(variables):
            coefficient = rational_solution[variable]
            if coefficient:
                free_adjustment += coefficient * homogeneous_directions[index]
                coefficients.append(
                    {
                        "cubic_fibre_basis_index": index,
                        "coefficient": _q(coefficient),
                    }
                )
        P2_solution = P2_base + free_adjustment
        residual_solution = forcing_through_four(P2_solution)
        if any(value != 0 for value in residual_solution):
            raise AssertionError("rational zero left a quartic residual")
        solution_record = {
            "coefficient_count": len(coefficients),
            "coefficients": coefficients,
            "free_adjustment_nonzero_count": _nonzero_count(free_adjustment),
            "free_adjustment_sha256": _digest(free_adjustment),
            "quadratic_correction_nonzero_count": _nonzero_count(P2_solution),
            "quadratic_correction_sha256": _digest(P2_solution),
        }

    return {
        "schema_version": 1,
        "name": "Program 5 intrinsic fourth-order Kuranishi map at theta_u",
        "source_file": str(source_path),
        "source_sha256": model.source_sha256,
        "first_order_direction": "theta_u = eta_0 + xi_4",
        "ambient_operation_dimension": model.ambient_operation_dimension,
        "rank_six_tangent_dimension": len(model.tangent_basis),
        "cubic_effect_rank": effect_rank,
        "cubic_augmented_rank": augmented_rank,
        "cubic_lift_affine_dimension": len(kernel_coordinates),
        "quadratic_image_particular": {
            "nonzero_count": _nonzero_count(P2_image_particular),
            "sha256": _digest(P2_image_particular),
        },
        "quadratic_tangent_particular": {
            "nonzero_count": _nonzero_count(tangent_particular),
            "sha256": _digest(tangent_particular),
        },
        "deterministic_quartic_residual": {
            "nonzero_count": _nonzero_count(q0),
            "sha256": _digest(q0),
        },
        "quartic_kuranishi": {
            "source_dimension": len(homogeneous_directions),
            "target_coefficient_rank": coefficient_rank,
            "independent_equation_count": len(equations),
            "coefficient_label_count": len(coefficient_labels),
            "equations": equations,
        },
        "rational_zero_found": rational_solution is not None,
        "rational_zero_verified": verified_rational_zero,
        "rational_zero": solution_record,
        "interpretation_boundary": (
            "The map saturates every quadratic correction compatible with "
            "the cubic equation for theta_u. A zero lifts this one first-order "
            "direction through order four; a nonzero map without a solved zero "
            "is not by itself an obstruction theorem over an algebraic closure."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = analyze_fourth_order_kuranishi(args.source)
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(
            f"program5_rank_six_fourth_order_kuranishi: {exc}",
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
