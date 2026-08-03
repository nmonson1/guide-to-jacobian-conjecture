#!/usr/bin/env python3
"""Generate one localized projective-kernel chart for the Lane 7 matrix.

For a chosen chart ``u_chart = 1``, this writes the ten equations ``M(a)u=0``
in the seven parameter variables, four remaining kernel coordinates, and the
localizer ``z*d-1``. The resulting affine scheme is one of the five standard
charts covering ``P(ker M)`` on ``D(d)``.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from generate_macaulay2_input import m2_expression, m2_matrix, scaled_rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_directory", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--chart", type=int, required=True, choices=range(5))
    parser.add_argument("--characteristic", type=int, required=True)
    args = parser.parse_args()

    if args.characteristic <= 0:
        raise ValueError("kernel-chart certificates require a positive characteristic")

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

    matrix_entries = scaled_rows(entries, clear_denominators=True)
    free_coordinates = iter([f"x{i}" for i in range(4)])
    kernel_coordinates = [
        "1" if index == args.chart else next(free_coordinates)
        for index in range(5)
    ]
    variables = [f"a{i}" for i in range(7)] + [f"x{i}" for i in range(4)] + ["z"]
    tag = f"KERNEL_CHART_{args.chart}_CHAR_{args.characteristic}"

    lines = [
        "-- Generated from the hash-checked public Lane 7 source packet.",
        "-- This is an affine chart of the projective kernel incidence.",
        f"R = ZZ/{args.characteristic}[{','.join(variables)}, MonomialOrder => GRevLex];",
        f"d = {m2_expression(determinant)};",
        f"M = {m2_matrix(matrix_entries)};",
        "assert(numrows M == 10 and numcols M == 5);",
        "-- Nonzero row scalings clear rational denominators and preserve rank loci.",
        "kernelVector = transpose matrix{{" + ", ".join(kernel_coordinates) + "}};",
        "kernelEquations = flatten entries (M * kernelVector);",
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
        f"wrote chart {args.chart} over F_{args.characteristic} to {args.output}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
