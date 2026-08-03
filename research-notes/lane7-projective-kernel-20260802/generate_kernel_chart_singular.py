#!/usr/bin/env python3
"""Generate one Singular computation for a Lane 7 projective-kernel chart."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import sympy as sp

from generate_kernel_chart_input import parse_integral_polynomial, render_polynomial
from generate_macaulay2_input import ROW_DENOMINATOR_LCMS


def render_integer_polynomial(poly: sp.Poly) -> str:
    """Render an integral polynomial without rational-expression overhead."""
    rendered: list[str] = []
    variables = poly.gens
    for exponents, coefficient in poly.terms():
        value = int(coefficient)
        if value == 0:
            continue
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_directory", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--chart", type=int, required=True, choices=range(5))
    parser.add_argument(
        "--characteristic",
        type=int,
        required=True,
        help="0 for QQ; otherwise a prime not killing a row multiplier",
    )
    args = parser.parse_args()

    characteristic = args.characteristic
    if characteristic < 0 or (characteristic != 0 and not sp.isprime(characteristic)):
        raise ValueError("characteristic must be zero or prime")
    if characteristic and any(
        scale % characteristic == 0 for scale in ROW_DENOMINATOR_LCMS
    ):
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

    equations: list[str] = []
    for scale, row in zip(ROW_DENOMINATOR_LCMS, entries):
        parsed = [
            parse_integral_polynomial(entry, scale, parameters, local_symbols)
            for entry in row
        ]
        expression = sum(
            polynomial.as_expr() * coordinate
            for polynomial, coordinate in zip(parsed, kernel_coordinates)
        )
        if characteristic:
            polynomial = sp.Poly(
                expression, *all_chart_variables, modulus=characteristic
            )
            equations.append(render_polynomial(polynomial, characteristic))
        else:
            polynomial = sp.Poly(expression, *all_chart_variables, domain=sp.ZZ)
            equations.append(render_integer_polynomial(polynomial))

    determinant_expression = sp.sympify(determinant, locals=local_symbols)
    if characteristic:
        determinant_poly = sp.Poly(
            determinant_expression, *parameters, modulus=characteristic
        )
        determinant_text = render_polynomial(determinant_poly, characteristic)
        field_tag = f"CHAR_{characteristic}"
    else:
        determinant_poly = sp.Poly(
            determinant_expression, *parameters, domain=sp.QQ
        )
        if any(coefficient.q != 1 for coefficient in determinant_poly.coeffs()):
            raise ValueError("determinant has an uncleared rational coefficient")
        determinant_poly = sp.Poly(
            determinant_poly.as_expr(), *parameters, domain=sp.ZZ
        )
        determinant_text = render_integer_polynomial(determinant_poly)
        field_tag = "QQ"

    variables = [str(variable) for variable in (*all_chart_variables, z)]
    tag = f"KERNEL_CHART_{args.chart}_{field_tag}_SINGULAR"
    ring_characteristic = characteristic if characteristic else 0

    lines = [
        f"ring R = {ring_characteristic},({','.join(variables)}),dp;",
        f"poly d = {determinant_text};",
        "ideal I =\n  " + ",\n  ".join([*equations, "z*d-1"]) + ";",
        f'print("{tag}_BEGIN");',
        "ideal J = slimgb(I);",
        "int dimI = dim(J);",
        "int codimI = nvars(basering)-dimI;",
        f'print("{tag}_DIM="+string(dimI));',
        f'print("{tag}_CODIM="+string(codimI));',
        f'print("{tag}_GB_SIZE="+string(size(J)));',
        f'print("{tag}_END");',
        "exit;",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n\n".join(lines) + "\n", encoding="utf-8")
    field_name = "QQ" if characteristic == 0 else f"F_{characteristic}"
    print(f"wrote Singular chart {args.chart} over {field_name} to {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError, sp.SympifyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
