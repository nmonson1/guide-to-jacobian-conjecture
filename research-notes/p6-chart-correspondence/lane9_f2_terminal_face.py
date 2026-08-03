#!/usr/bin/env python3
"""Exact reconstruction of the lattice-gap-five F2 terminal quotient face."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Dict, Mapping, MutableMapping, Sequence

Polynomial = Dict[int, Fraction]


def clean(poly: Mapping[int, Fraction]) -> Polynomial:
    return {degree: Fraction(value) for degree, value in sorted(poly.items()) if value}


def add(*polys: Mapping[int, Fraction]) -> Polynomial:
    result: MutableMapping[int, Fraction] = {}
    for poly in polys:
        for degree, value in poly.items():
            result[degree] = result.get(degree, Fraction(0)) + value
    return clean(result)


def scale(poly: Mapping[int, Fraction], scalar: Fraction | int) -> Polynomial:
    c = Fraction(scalar)
    return clean({degree: c * value for degree, value in poly.items()})


def multiply(left: Mapping[int, Fraction], right: Mapping[int, Fraction]) -> Polynomial:
    result: MutableMapping[int, Fraction] = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = result.get(i + j, Fraction(0)) + a * b
    return clean(result)


def derivative(poly: Mapping[int, Fraction]) -> Polynomial:
    return clean({degree - 1: degree * value for degree, value in poly.items() if degree})


def power(poly: Mapping[int, Fraction], exponent: int) -> Polynomial:
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    result: Polynomial = {0: Fraction(1)}
    base = clean(poly)
    n = exponent
    while n:
        if n & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        n //= 2
    return result


def as_strings(poly: Mapping[int, Fraction]) -> dict[str, str]:
    return {str(degree): str(value) for degree, value in sorted(poly.items())}


def linearized_face(
    alpha: Mapping[int, Fraction],
    beta: Mapping[int, Fraction],
    pbar: Mapping[int, Fraction],
    qbar: Mapping[int, Fraction],
    u: Mapping[int, Fraction],
) -> Polynomial:
    """Differential of p*q-3*u*p*q'+5*u*p'*q at (pbar,qbar)."""

    return add(
        multiply(alpha, qbar),
        multiply(pbar, beta),
        scale(
            multiply(
                u,
                add(
                    multiply(alpha, derivative(qbar)),
                    multiply(pbar, derivative(beta)),
                ),
            ),
            -3,
        ),
        scale(
            multiply(
                u,
                add(
                    multiply(derivative(alpha), qbar),
                    multiply(derivative(pbar), beta),
                ),
            ),
            5,
        ),
    )


def build_report() -> dict[str, object]:
    u = {1: Fraction(1)}
    pbar = {0: Fraction(1), 1: Fraction(-1)}
    qbar = {0: Fraction(1, 5), 1: Fraction(-3, 5), 2: Fraction(9, 25)}

    quotient_ode = add(
        multiply(pbar, qbar),
        scale(multiply(u, multiply(pbar, derivative(qbar))), -3),
        scale(multiply(u, multiply(derivative(pbar), qbar)), 5),
    )
    assert quotient_ode == {0: Fraction(1, 5)}

    base = {0: Fraction(5), 1: Fraction(-15), 2: Fraction(9)}
    u_minus_one = {0: Fraction(-1), 1: Fraction(1)}
    numerator = scale(multiply(u, power(u_minus_one, 5)), 729)
    denominator = power(base, 3)
    third_fiber = add(denominator, scale(numerator, -1))
    assert third_fiber == {
        0: Fraction(125),
        1: Fraction(-396),
        2: Fraction(405),
        3: Fraction(-135),
    }

    cross_derivative = add(
        multiply(derivative(numerator), denominator),
        scale(multiply(numerator, derivative(denominator)), -1),
    )
    expected_cross_derivative = scale(
        multiply(power(u_minus_one, 4), power(base, 2)), -3645
    )
    assert cross_derivative == expected_cross_derivative

    # With constants fixed, the true terminal-face tangent block has domain
    # (delta p = a_1*u, delta q = b_1*u+b_2*u^2) and target coefficients
    # (u,u^2).  This is real F2 data, but it is not a normal-neighborhood
    # endpoint block at order 510, 520, or 530.
    variation_columns = [
        linearized_face({1: Fraction(1)}, {}, pbar, qbar, u),
        linearized_face({}, {1: Fraction(1)}, pbar, qbar, u),
        linearized_face({}, {2: Fraction(1)}, pbar, qbar, u),
    ]
    linearization_matrix = [
        [column.get(degree, Fraction(0)) for column in variation_columns]
        for degree in (1, 2)
    ]
    assert linearization_matrix == [
        [Fraction(6, 5), Fraction(-2), Fraction(0)],
        [Fraction(-9, 5), Fraction(-3), Fraction(-5)],
    ]
    integer_matrix = [
        [5 * entry for entry in row] for row in linearization_matrix
    ]
    assert integer_matrix == [
        [Fraction(6), Fraction(-10), Fraction(0)],
        [Fraction(-9), Fraction(-15), Fraction(-25)],
    ]
    kernel_generator = [Fraction(-1), Fraction(-3, 5), Fraction(18, 25)]
    assert all(
        sum((entry * coordinate for entry, coordinate in zip(row, kernel_generator)), Fraction(0)) == 0
        for row in linearization_matrix
    )
    assert linearization_matrix[0][0] * linearization_matrix[1][2] != 0

    # If p=a+b*u and q=c+d*u+e*u^2, coefficient comparison in the
    # quotient ODE gives the three equations below.  The displayed solution
    # is the normalization a=1,b=-1.
    coefficient_equations = [
        "a*c=1/5",
        "a*d=3*b*c",
        "5*a*e=3*b*d",
    ]

    return {
        "schema_version": 1,
        "family": "F_2 terminal complete-chain quotient",
        "lattice_gap": 5,
        "quotient_coordinate": "u=z^5",
        "quotient_ode": "pbar*qbar-3*u*pbar*qbar'+5*u*pbar'*qbar=1/5",
        "coefficient_equations": coefficient_equations,
        "normalized_face": {
            "pbar": "1-u",
            "qbar": "(9*u^2-15*u+5)/25",
            "ode_value": "1/5",
        },
        "terminal_face_linearization": {
            "domain_support_block": ["delta_p:u", "delta_q:u", "delta_q:u^2"],
            "target_support_block": ["u", "u^2"],
            "matrix": [
                [str(entry) for entry in row] for row in linearization_matrix
            ],
            "integer_scaled_matrix_factor": 5,
            "integer_scaled_matrix": [
                [int(entry) for entry in row] for row in integer_matrix
            ],
            "rank": 2,
            "kernel_dimension": 1,
            "kernel_generator": [str(entry) for entry in kernel_generator],
            "kernel_interpretation": (
                "source scaling u->(1+epsilon)u, namely "
                "(delta_p,delta_q)=(u*pbar',u*qbar')"
            ),
        },
        "belyi_map": {
            "tau": "729*u*(u-1)^5/(9*u^2-15*u+5)^3",
            "degree": 6,
            "derivative": "-3645*(u-1)^4/(9*u^2-15*u+5)^4",
            "passport": ["(5,1)", "(3,3)", "(3,1,1,1)"],
            "tau_minus_one_finite_numerator": "135*u^3-405*u^2+396*u-125",
        },
        "cleared_polynomials": {
            "numerator": as_strings(numerator),
            "denominator": as_strings(denominator),
            "denominator_minus_numerator": as_strings(third_fiber),
        },
        "scope": (
            "This reconstructs the real terminal quotient face, its exact "
            "three-to-two tangent matrix, and its degree-six Belyi map.  It is "
            "not a reconstruction of the missing order-520 endpoint matrices "
            "or attachment recurrence."
        ),
        "all_exact_checks_passed": True,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    rendered = json.dumps(build_report(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
