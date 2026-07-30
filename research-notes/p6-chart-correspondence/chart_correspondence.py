#!/usr/bin/env python3
"""Exact diagnostic for Program 6 chart-correspondence layers.

The input is a JSON document containing one or more finite-dimensional layers.
All linear algebra is performed over Q using fractions.Fraction; no external
computer-algebra dependency is required.

This tool does not discover adjacent Newton charts. It audits a proposed
classification once the fixed-chart gauge vectors and adjacent-chart tangent
vectors have been supplied.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence

Vector = list[Fraction]
Matrix = list[Vector]


def q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, bool):
        raise TypeError("booleans are not rational coefficients")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError(f"invalid rational coefficient {value!r}") from exc
    raise TypeError(
        f"coefficient {value!r} has type {type(value).__name__}; "
        "use integers or rational strings"
    )


def parse_matrix(values: Sequence[Sequence[Any]], *, name: str) -> Matrix:
    rows = [[q(value) for value in row] for row in values]
    if not rows:
        return []
    width = len(rows[0])
    if width == 0:
        raise ValueError(f"{name} has an empty row")
    if any(len(row) != width for row in rows):
        raise ValueError(f"{name} is ragged")
    return rows


def parse_vectors(values: Sequence[Sequence[Any]], *, width: int, name: str) -> list[Vector]:
    vectors = [[q(value) for value in vector] for vector in values]
    for index, vector in enumerate(vectors):
        if len(vector) != width:
            raise ValueError(f"{name}[{index}] has length {len(vector)}, expected {width}")
    return vectors


def rref(matrix: Matrix) -> tuple[Matrix, list[int]]:
    if not matrix:
        return [], []
    result = [row[:] for row in matrix]
    row_count = len(result)
    column_count = len(result[0])
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        candidate = next((row for row in range(pivot_row, row_count) if result[row][column]), None)
        if candidate is None:
            continue
        result[pivot_row], result[candidate] = result[candidate], result[pivot_row]
        pivot = result[pivot_row][column]
        result[pivot_row] = [entry / pivot for entry in result[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = result[row][column]
            if factor:
                result[row] = [entry - factor * pivot_entry for entry, pivot_entry in zip(result[row], result[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return result, pivot_columns


def rank(matrix: Matrix) -> int:
    return 0 if not matrix else len(rref(matrix)[1])


def nullspace(matrix: Matrix, *, ambient_dimension: int | None = None) -> list[Vector]:
    if matrix:
        column_count = len(matrix[0])
    elif ambient_dimension is not None:
        column_count = ambient_dimension
    else:
        raise ValueError("ambient_dimension is required for an empty operator")
    reduced, pivot_columns = rref(matrix)
    pivot_rows = {column: row for row, column in enumerate(pivot_columns)}
    free_columns = [column for column in range(column_count) if column not in pivot_rows]
    basis: list[Vector] = []
    for free_column in free_columns:
        vector = [Fraction(0) for _ in range(column_count)]
        vector[free_column] = Fraction(1)
        for pivot_column, row in pivot_rows.items():
            vector[pivot_column] = -reduced[row][free_column]
        basis.append(vector)
    return basis


def matrix_vector_product(matrix: Matrix, vector: Vector) -> Vector:
    return [sum((entry * value for entry, value in zip(row, vector)), Fraction(0)) for row in matrix]


def rank_of_vectors(vectors: Sequence[Vector], *, ambient_dimension: int) -> int:
    if not vectors:
        return 0
    if any(len(vector) != ambient_dimension for vector in vectors):
        raise ValueError("vector dimensions do not agree")
    matrix = [[vectors[column][row] for column in range(len(vectors))] for row in range(ambient_dimension)]
    return rank(matrix)


def independent_extension(base: Sequence[Vector], candidates: Sequence[Vector], *, ambient_dimension: int) -> tuple[list[Vector], list[Vector]]:
    accepted = list(base)
    current_rank = rank_of_vectors(accepted, ambient_dimension=ambient_dimension)
    added: list[Vector] = []
    for candidate in candidates:
        trial = accepted + [candidate]
        trial_rank = rank_of_vectors(trial, ambient_dimension=ambient_dimension)
        if trial_rank > current_rank:
            accepted.append(candidate)
            added.append(candidate)
            current_rank = trial_rank
    return accepted, added


def rational_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def vector_json(vector: Vector) -> list[str]:
    return [rational_string(value) for value in vector]


def transport_support(k: int, monomials: Iterable[Sequence[int]]) -> list[list[int]]:
    """Support closure under Y = Y' - lambda X^(-k)."""
    transported: set[tuple[int, int]] = set()
    for monomial in monomials:
        if len(monomial) != 2:
            raise ValueError(f"invalid monomial exponent pair {monomial!r}")
        i, j = monomial
        if not isinstance(i, int) or not isinstance(j, int):
            raise TypeError("support exponents must be integers")
        if j < 0:
            raise ValueError("the current support transport expects j >= 0")
        for t in range(j + 1):
            transported.add((i - k * t, j - t))
    return [[i, j] for i, j in sorted(transported, key=lambda pair: (-pair[1], pair[0]))]


@dataclass(frozen=True)
class LayerResult:
    label: str
    ambient_dimension: int
    kernel_dimension: int
    gauge_dimension: int
    rechart_increment: int
    explained_dimension: int
    unexplained_dimension: int
    quotient_representatives: list[Vector]
    support_closure: list[list[int]] | None

    def as_json(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "label": self.label,
            "ambient_dimension": self.ambient_dimension,
            "kernel_dimension": self.kernel_dimension,
            "gauge_dimension": self.gauge_dimension,
            "rechart_increment": self.rechart_increment,
            "explained_dimension": self.explained_dimension,
            "unexplained_dimension": self.unexplained_dimension,
            "quotient_representatives": [vector_json(vector) for vector in self.quotient_representatives],
        }
        if self.support_closure is not None:
            result["support_closure"] = self.support_closure
        return result


def analyze_layer(layer: dict[str, Any]) -> LayerResult:
    label = str(layer.get("label", layer.get("r", "unnamed-layer")))
    operator_values = layer.get("operator")
    if not isinstance(operator_values, list):
        raise ValueError(f"{label}: operator must be a list of rows")
    operator = parse_matrix(operator_values, name=f"{label}.operator")
    if operator:
        ambient_dimension = len(operator[0])
    else:
        ambient_dimension = layer.get("ambient_dimension")
        if not isinstance(ambient_dimension, int) or ambient_dimension < 0:
            raise ValueError(f"{label}: ambient_dimension is required for an empty operator")
    gauge_values = layer.get("gauge_vectors", [])
    rechart_values = layer.get("rechart_vectors", [])
    if not isinstance(gauge_values, list) or not isinstance(rechart_values, list):
        raise ValueError(f"{label}: gauge_vectors and rechart_vectors must be lists")
    gauge = parse_vectors(gauge_values, width=ambient_dimension, name=f"{label}.gauge_vectors")
    recharts = parse_vectors(rechart_values, width=ambient_dimension, name=f"{label}.rechart_vectors")
    for kind, vectors in (("gauge", gauge), ("rechart", recharts)):
        for index, vector in enumerate(vectors):
            image = matrix_vector_product(operator, vector)
            if any(image):
                raise ValueError(f"{label}: {kind} vector {index} is not in ker(operator); image={vector_json(image)}")
    kernel_basis = nullspace(operator, ambient_dimension=ambient_dimension)
    gauge_basis, _ = independent_extension([], gauge, ambient_dimension=ambient_dimension)
    explained_basis, rechart_added = independent_extension(gauge_basis, recharts, ambient_dimension=ambient_dimension)
    explained_rank = rank_of_vectors(explained_basis, ambient_dimension=ambient_dimension)
    kernel_rank = len(kernel_basis)
    _, quotient_representatives = independent_extension(explained_basis, kernel_basis, ambient_dimension=ambient_dimension)
    support_closure: list[list[int]] | None = None
    support = layer.get("support_transport")
    if support is not None:
        if not isinstance(support, dict):
            raise ValueError(f"{label}: support_transport must be an object")
        k = support.get("k")
        monomials = support.get("monomials")
        if not isinstance(k, int) or not isinstance(monomials, list):
            raise ValueError(f"{label}: support_transport requires integer k and monomials")
        support_closure = transport_support(k, monomials)
    return LayerResult(label, ambient_dimension, kernel_rank, len(gauge_basis), len(rechart_added), explained_rank, kernel_rank - explained_rank, quotient_representatives, support_closure)


def analyze_document(document: dict[str, Any]) -> dict[str, Any]:
    if document.get("schema_version") != 1:
        raise ValueError("schema_version must equal 1")
    layers = document.get("layers")
    if not isinstance(layers, list) or not layers:
        raise ValueError("layers must be a nonempty list")
    results = [analyze_layer(layer) for layer in layers]
    return {
        "schema_version": 1,
        "name": document.get("name", "chart-correspondence diagnostic"),
        "layers": [result.as_json() for result in results],
        "all_kernel_directions_explained": all(result.unexplained_dimension == 0 for result in results),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON diagnostic contract")
    parser.add_argument("-o", "--output", type=Path, help="write JSON output instead of stdout")
    args = parser.parse_args(argv)
    try:
        document = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(document, dict):
            raise ValueError("top-level JSON value must be an object")
        result = analyze_document(document)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"chart_correspondence: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
