#!/usr/bin/env python3
"""Exact blockwise audit for a parameter-complete F2 attachment recurrence.

The input contract is deliberately data-only.  Each order is split into C_g
character blocks.  A block supplies an exact rational matrix, right-hand side,
and variable declarations.  The audit compares the full system with the
non-intrinsic slice obtained by setting fresh parameters to zero.

This utility does not contain or infer the missing public F2 endpoint blocks.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

RationalMatrix = list[list[Fraction]]


def parse_fraction(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise TypeError("booleans are not rational entries")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise TypeError(f"expected integer or rational string, got {type(value).__name__}")


def render_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def transpose(matrix: RationalMatrix, column_count: int) -> RationalMatrix:
    if matrix:
        return [list(column) for column in zip(*matrix)]
    return [[] for _ in range(column_count)]


def rref(matrix: RationalMatrix) -> tuple[RationalMatrix, list[int]]:
    work = [row[:] for row in matrix]
    row_count = len(work)
    column_count = len(work[0]) if work else 0
    if any(len(row) != column_count for row in work):
        raise ValueError("ragged matrix")

    pivots: list[int] = []
    pivot_row = 0
    for pivot_column in range(column_count):
        selected = next(
            (row for row in range(pivot_row, row_count) if work[row][pivot_column]),
            None,
        )
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        pivot = work[pivot_row][pivot_column]
        work[pivot_row] = [entry / pivot for entry in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = work[row][pivot_column]
            if factor:
                work[row] = [
                    work[row][column] - factor * work[pivot_row][column]
                    for column in range(column_count)
                ]
        pivots.append(pivot_column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return work, pivots


def rank(matrix: RationalMatrix) -> int:
    return len(rref(matrix)[1])


def nullspace(matrix: RationalMatrix, column_count: int) -> RationalMatrix:
    width = len(matrix[0]) if matrix else column_count
    reduced, pivots = rref(matrix)
    free_columns = [column for column in range(width) if column not in pivots]
    basis: RationalMatrix = []
    for free in free_columns:
        vector = [Fraction(0) for _ in range(width)]
        vector[free] = Fraction(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free]
        basis.append(vector)
    return basis


def dot(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
    if len(left) != len(right):
        raise ValueError("dot-product dimension mismatch")
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def solve_diagnostics(
    matrix: RationalMatrix,
    rhs: list[Fraction],
    column_count: int | None = None,
) -> dict[str, Any]:
    row_count = len(matrix)
    if matrix:
        inferred_column_count = len(matrix[0])
        if column_count is not None and inferred_column_count != column_count:
            raise ValueError("declared column count does not match matrix")
        column_count = inferred_column_count
    elif column_count is None:
        column_count = 0

    if len(rhs) != row_count:
        raise ValueError("right-hand-side length does not match matrix")
    if any(len(row) != column_count for row in matrix):
        raise ValueError("ragged matrix")

    matrix_rank = rank(matrix)
    augmented = [row + [rhs[index]] for index, row in enumerate(matrix)]
    augmented_rank = rank(augmented)
    consistent = matrix_rank == augmented_rank

    left_kernel = nullspace(
        transpose(matrix, column_count),
        column_count=row_count,
    )
    pairings = [dot(vector, rhs) for vector in left_kernel]
    certificates = [
        {
            "left_null_vector": [render_fraction(entry) for entry in vector],
            "pairing_with_rhs": render_fraction(pairing),
        }
        for vector, pairing in zip(left_kernel, pairings)
        if pairing
    ]

    return {
        "row_count": row_count,
        "column_count": column_count,
        "rank": matrix_rank,
        "augmented_rank": augmented_rank,
        "consistent": consistent,
        "solution_dimension": column_count - matrix_rank if consistent else None,
        "left_nullity": row_count - matrix_rank,
        "nonzero_obstruction_certificates": certificates,
    }


def parse_block(
    block: Mapping[str, Any], modulus: int
) -> tuple[list[dict[str, Any]], RationalMatrix, list[Fraction]]:
    variables = list(block.get("variables", []))
    equations = list(block.get("equations", []))
    matrix_raw = list(block.get("matrix", []))
    rhs_raw = list(block.get("rhs", []))
    character = int(block["character"]) % modulus

    if len(matrix_raw) != len(equations):
        raise ValueError("matrix row count must equal equation count")
    if len(rhs_raw) != len(equations):
        raise ValueError("rhs length must equal equation count")
    if any(len(row) != len(variables) for row in matrix_raw):
        raise ValueError("matrix column count must equal variable count")

    names = [str(variable["name"]) for variable in variables]
    if len(names) != len(set(names)):
        raise ValueError("variable names must be unique within a block")
    for variable in variables:
        if int(variable["character"]) % modulus != character:
            raise ValueError(
                f"variable {variable['name']} has character "
                f"{variable['character']}, but block has character {character}"
            )
        if variable.get("kind") not in {
            "left_correction",
            "right_correction",
            "overlap_correction",
            "fresh_parameter",
            "other",
        }:
            raise ValueError(f"unsupported variable kind for {variable['name']}")

    matrix = [[parse_fraction(entry) for entry in row] for row in matrix_raw]
    rhs = [parse_fraction(entry) for entry in rhs_raw]
    return variables, matrix, rhs


def audit_block(block: Mapping[str, Any], modulus: int) -> dict[str, Any]:
    variables, matrix, rhs = parse_block(block, modulus)
    full = solve_diagnostics(matrix, rhs, column_count=len(variables))

    retained_columns = [
        index
        for index, variable in enumerate(variables)
        if variable["kind"] != "fresh_parameter"
    ]
    fresh_columns = [
        index
        for index, variable in enumerate(variables)
        if variable["kind"] == "fresh_parameter"
    ]
    sliced_matrix = [
        [row[column] for column in retained_columns] for row in matrix
    ]
    fixed_parameter_slice = solve_diagnostics(
        sliced_matrix,
        rhs,
        column_count=len(retained_columns),
    )

    return {
        "name": str(block.get("name", f"character-{block['character']}")),
        "character": int(block["character"]) % modulus,
        "equations": [str(name) for name in block.get("equations", [])],
        "variables": variables,
        "full_parameter_system": full,
        "fresh_parameter_names": [
            variables[index]["name"] for index in fresh_columns
        ],
        "fixed_fresh_parameter_zero_slice": fixed_parameter_slice,
        "slice_dependent_apparent_obstruction": (
            full["consistent"] and not fixed_parameter_slice["consistent"]
        ),
    }


def audit_contract(contract: Mapping[str, Any]) -> dict[str, Any]:
    if int(contract.get("schema_version", 0)) != 1:
        raise ValueError("unsupported schema_version")
    modulus = int(contract.get("cyclic_modulus", 5))
    if modulus <= 0:
        raise ValueError("cyclic_modulus must be positive")

    orders_out: list[dict[str, Any]] = []
    for order_entry in contract.get("orders", []):
        order = int(order_entry["order"])
        blocks = [
            audit_block(block, modulus) for block in order_entry.get("blocks", [])
        ]
        orders_out.append(
            {
                "order": order,
                "block_count": len(blocks),
                "all_full_parameter_blocks_consistent": all(
                    block["full_parameter_system"]["consistent"]
                    for block in blocks
                ),
                "any_slice_dependent_apparent_obstruction": any(
                    block["slice_dependent_apparent_obstruction"]
                    for block in blocks
                ),
                "blocks": blocks,
            }
        )

    instantiated = any(order["block_count"] for order in orders_out)
    return {
        "schema_version": 1,
        "contract_name": str(
            contract.get("name", "unnamed F2 attachment contract")
        ),
        "provenance": contract.get("provenance"),
        "cyclic_modulus": modulus,
        "instantiated": instantiated,
        "orders": orders_out,
        "all_full_parameter_systems_consistent": (
            all(
                order["all_full_parameter_blocks_consistent"]
                for order in orders_out
            )
            if instantiated
            else None
        ),
        "interpretation": (
            "Only the full-parameter system defines an intrinsic finite-order "
            "test. The fresh-parameter-zero calculation is reported solely as "
            "a slice diagnostic."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        contract = json.loads(args.contract.read_text(encoding="utf-8"))
        report = audit_contract(contract)
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        print(f"lane9_f2_attachment_recurrence: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
