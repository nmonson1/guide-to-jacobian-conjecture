#!/usr/bin/env python3
"""Generate one localized projective-kernel chart for the Lane 7 matrix.

For a chosen chart ``u_chart = 1``, this writes the ten equations ``M(a)u=0``
in the seven parameter variables, four remaining kernel coordinates, and the
localizer ``z*d-1``.  Coefficients are expanded and reduced in the requested
prime field before they reach the CAS.  This removes rational-expression
parsing and preserves the chart because the packet-specific row multipliers
are units at every accepted prime.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import sympy as sp

from generate_macaulay2_input import ROW_DENOMINATOR_LCMS


def render_polynomial(poly: sp.Poly, characteristic: int) -> str:
    """Render a polynomial with small signed representatives modulo p."""
    rendered: list[str] = []
    variables = poly.gens
    for exponents, coefficient in poly.terms():
        value = int(coefficient) % characteristic
        if value == 0:
            continue
        if value > characteristic // 2:
            value -= characteristic

        factors: list[str] = []
        for variable, exponent in zip(variables, exponents):
            if exponent == 1:
                factors.append(str(variable))
            elif exponent > 1:
                factors.append(f"{variable}^{exponent}")
        monomial = "*".join(factors)

        if not monomial:
            term = str(value)
        elif value == 1:
            term = monomial
        elif value == -1:
            term = f"-{monomial}"
        else:
            term = f"{value}*{monomial}"
        rendered.append(term)

    if not rendered:
        return "0"
    return " + ".join(rendered).replace("+ -", "- ")


def parse_integral_polynomial(
    expression: str,
    scale: int,
    parameters: tuple[sp.Symbol, ...],
    local_symbols: dict[str, sp.Symbol],
) -> sp.Poly:
    polynomial = sp.Poly(
        scale * sp.sympify(expression, locals=local_symbols),
        *parameters,
        domain=sp.QQ,
    )
    if any(coefficient.q != 1 for coefficient in polynomial.coeffs()):
        raise ValueError("row multiplier failed to clear a coefficient denominator")
    return polynomial


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_directory", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--chart", type=int, required=True, choices=range(5))
    parser.add_argument("--characteristic", type=int, required=True)
    args = parser.parse_args()

    characteristic = args.characteristic
    if not sp.isprime(characteristic):
        raise ValueError("kernel-chart certificates require a prime characteristic")
    if any(scale % characteristic == 0 for scale in ROW_DENOMINATOR_LCMS):
        raise ValueError("chosen characteristic kills a denominator-clearing row unit")

    residual = json.loads(
        (args.source_directory / "collision_residual_matrix_M.json").read_text(
            encoding="utf-8"
        )
    )
    factorization = json.loads(
        (args.source_directory / "Hv10_split_matrix_factorization.json").read_text(
            encoding="utf-8"
        )
    )
    entries = residual.get("entries")
    determinant = factorization.get("d")
    if not isinstance(entries, list) or len(entries) != 10:
        raise ValueError("expected a 10 by 5 residual matrix")
    if any(not isinstance(row, list) or len(row) != 5 for row in entries):
        raise ValueError("expected a 10 by 5 residual matrix")
    if not isinstance(determinant, str):
        raise ValueError("factorization artifact does not contain determinant d")

    parameters = sp.symbols("a0:7")
    kernel_variables = sp.symbols("x0:4")
    z = sp.Symbol("z")
    local_symbols = {str(variable): variable for variable in parameters}
    free_coordinates = iter(kernel_variables)
    kernel_coordinates: list[sp.Expr] = [
        sp.Integer(1) if index == args.chart else next(free_coordinates)
        for index in range(5)
    ]
    all_chart_variables = (*parameters, *kernel_variables)

    parsed_rows: list[list[sp.Poly]] = []
    for scale, row in zip(ROW_DENOMINATOR_LCMS, entries):
        parsed_rows.append(
            [
                parse_integral_polynomial(entry, scale, parameters, local_symbols)
                for entry in row
            ]
        )

    equations: list[str] = []
    for row in parsed_rows:
        expression = sum(
            polynomial.as_expr() * coordinate
            for polynomial, coordinate in zip(row, kernel_coordinates)
        )
        reduced = sp.Poly(expression, *all_chart_variables, modulus=characteristic)
        equations.append(render_polynomial(reduced, characteristic))

    determinant_poly = sp.Poly(
        sp.sympify(determinant, locals=local_symbols),
        *parameters,
        modulus=characteristic,
    )
    determinant_text = render_polynomial(determinant_poly, characteristic)

    variables = [str(variable) for variable in (*all_chart_variables, z)]
    tag = f"KERNEL_CHART_{args.chart}_CHAR_{characteristic}"
    equation_block = ",\n  ".join(equations)

    lines = [
        "-- Generated from the hash-checked public Lane 7 source packet.",
        "-- This is an affine chart of the projective kernel incidence.",
        "-- Rational coefficients were cleared by row units and reduced mod p.",
        f"R = ZZ/{characteristic}[{','.join(variables)}, MonomialOrder => GRevLex];",
        f"d = {determinant_text};",
        "kernelEquations = {\n  " + equation_block + "\n};",
        "assert(#kernelEquations == 10);",
        "localizerEquation = z*d - 1;",
        "I = ideal kernelEquations + ideal(localizerEquation);",
        f'print "{tag}_BEGIN";',
        "G = gb I;",
        "unitI = (I == 1);",
        f'print("{tag}_UNIT=" | toString unitI);',
        "if unitI then (",
        f'  print "{tag}_DIM=EMPTY";',
        ") else (",
        "  dimI = dim I;",
        "  codimI = codim I;",
        f'  print("{tag}_DIM=" | toString dimI);',
        f'  print("{tag}_CODIM=" | toString codimI);',
        "  assert(dimI <= 1);",
        "  assert(codimI >= 11);",
        ");",
        f'print "{tag}_END";',
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"wrote chart {args.chart} over F_{characteristic} to {args.output}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError, sp.SympifyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
