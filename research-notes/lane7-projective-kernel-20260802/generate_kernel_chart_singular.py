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
        reduced = sp.Poly(expression, *all_chart_variables, modulus=characteristic)
        equations.append(render_polynomial(reduced, characteristic))

    determinant_poly = sp.Poly(
        sp.sympify(determinant, locals=local_symbols),
        *parameters,
        modulus=characteristic,
    )
    determinant_text = render_polynomial(determinant_poly, characteristic)
    variables = [str(variable) for variable in (*all_chart_variables, z)]
    tag = f"KERNEL_CHART_{args.chart}_CHAR_{characteristic}_SINGULAR"

    lines = [
        f"ring R = {characteristic},({','.join(variables)}),dp;",
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
    print(
        f"wrote Singular chart {args.chart} over F_{characteristic} to {args.output}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError, sp.SympifyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
