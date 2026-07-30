"""Dependency-free exact linear algebra over a supplied field."""
from __future__ import annotations
from typing import Any, Mapping, Sequence
from .fields import ContractError, ExactField

Vector = list[Any]
Matrix = list[Vector]


def parse_vector(field: ExactField, values: Sequence[Any], *, width: int, name: str) -> Vector:
    vector = [field.parse(value) for value in values]
    if len(vector) != width:
        raise ContractError(f"{name} has length {len(vector)}, expected {width}")
    return vector


def parse_matrix(field: ExactField, values: Sequence[Sequence[Any]], *, rows: int, columns: int, name: str) -> Matrix:
    if len(values) != rows:
        raise ContractError(f"{name} has {len(values)} rows, expected {rows}")
    return [parse_vector(field, row, width=columns, name=f"{name}[{index}]") for index, row in enumerate(values)]


def transpose(matrix: Matrix, *, rows: int, columns: int) -> Matrix:
    if len(matrix) != rows or any(len(row) != columns for row in matrix):
        raise ContractError("matrix shape does not match declared dimensions")
    return [[matrix[row][column] for row in range(rows)] for column in range(columns)]


def matrix_vector_product(matrix: Matrix, vector: Vector, field: ExactField) -> Vector:
    return [sum((entry * value for entry, value in zip(row, vector)), field.zero) for row in matrix]


def row_matrix_product(row: Vector, matrix: Matrix, field: ExactField) -> Vector:
    if matrix and len(row) != len(matrix):
        raise ContractError("row/matrix dimensions do not agree")
    columns = len(matrix[0]) if matrix else 0
    return [sum((row[index] * matrix[index][column] for index in range(len(row))), field.zero) for column in range(columns)]


def matrix_product(left: Matrix, right: Matrix, *, left_rows: int, middle: int, right_columns: int, field: ExactField) -> Matrix:
    if len(left) != left_rows or any(len(row) != middle for row in left):
        raise ContractError("left matrix has the wrong shape")
    if len(right) != middle or any(len(row) != right_columns for row in right):
        raise ContractError("right matrix has the wrong shape")
    return [[sum((left[row][index] * right[index][column] for index in range(middle)), field.zero) for column in range(right_columns)] for row in range(left_rows)]


def rref(matrix: Matrix, *, rows: int, columns: int, field: ExactField) -> tuple[Matrix, list[int]]:
    if len(matrix) != rows or any(len(row) != columns for row in matrix):
        raise ContractError("RREF input shape does not match declared dimensions")
    result = [row[:] for row in matrix]
    pivots: list[int] = []
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if result[row][column]), None)
        if pivot is None:
            continue
        result[pivot_row], result[pivot] = result[pivot], result[pivot_row]
        scale = result[pivot_row][column]
        result[pivot_row] = [entry / scale for entry in result[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = result[row][column]
            if factor:
                result[row] = [left - factor * right for left, right in zip(result[row], result[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    return result, pivots


def rank(matrix: Matrix, *, rows: int, columns: int, field: ExactField) -> int:
    return len(rref(matrix, rows=rows, columns=columns, field=field)[1])


def nullspace(matrix: Matrix, *, rows: int, columns: int, field: ExactField) -> list[Vector]:
    reduced, pivots = rref(matrix, rows=rows, columns=columns, field=field)
    pivot_rows = {column: row for row, column in enumerate(pivots)}
    free_columns = [column for column in range(columns) if column not in pivot_rows]
    basis: list[Vector] = []
    for free_column in free_columns:
        vector = [field.zero for _ in range(columns)]
        vector[free_column] = field.one
        for pivot_column, row in pivot_rows.items():
            vector[pivot_column] = -reduced[row][free_column]
        basis.append(vector)
    return basis


def left_nullspace(matrix: Matrix, *, rows: int, columns: int, field: ExactField) -> list[Vector]:
    return nullspace(transpose(matrix, rows=rows, columns=columns), rows=columns, columns=rows, field=field)


def vectors_to_column_matrix(vectors: Sequence[Vector], *, ambient_dimension: int, field: ExactField) -> Matrix:
    if any(len(vector) != ambient_dimension for vector in vectors):
        raise ContractError("vector dimensions do not agree")
    return [[vector[row] for vector in vectors] for row in range(ambient_dimension)]


def rank_of_vectors(vectors: Sequence[Vector], *, ambient_dimension: int, field: ExactField) -> int:
    if not vectors:
        return 0
    matrix = vectors_to_column_matrix(vectors, ambient_dimension=ambient_dimension, field=field)
    return rank(matrix, rows=ambient_dimension, columns=len(vectors), field=field)


def independent_extension(base: Sequence[Vector], candidates: Sequence[Vector], *, ambient_dimension: int, field: ExactField) -> tuple[list[Vector], list[Vector]]:
    accepted = list(base)
    current_rank = rank_of_vectors(accepted, ambient_dimension=ambient_dimension, field=field)
    added: list[Vector] = []
    for candidate in candidates:
        trial = accepted + [candidate]
        trial_rank = rank_of_vectors(trial, ambient_dimension=ambient_dimension, field=field)
        if trial_rank > current_rank:
            accepted.append(candidate)
            added.append(candidate)
            current_rank = trial_rank
    return accepted, added


def vector_in_span(vector: Vector, span: Sequence[Vector], *, ambient_dimension: int, field: ExactField) -> bool:
    return rank_of_vectors([*span, vector], ambient_dimension=ambient_dimension, field=field) == rank_of_vectors(span, ambient_dimension=ambient_dimension, field=field)


def parse_generators(field: ExactField, values: Sequence[Any], *, width: int, name: str) -> tuple[list[str], list[Vector]]:
    labels: list[str] = []
    vectors: list[Vector] = []
    for index, value in enumerate(values):
        if isinstance(value, Mapping):
            label = str(value.get("name", f"{name}-{index}"))
            raw_vector = value.get("vector")
        else:
            label = f"{name}-{index}"
            raw_vector = value
        if not isinstance(raw_vector, list):
            raise ContractError(f"{name}[{index}] must be a vector or named vector")
        labels.append(label)
        vectors.append(parse_vector(field, raw_vector, width=width, name=f"{name}[{index}]"))
    return labels, vectors


def serialize_vector(field: ExactField, vector: Sequence[Any]) -> list[Any]:
    return [field.serialize(value) for value in vector]


def dot(left: Sequence[Any], right: Sequence[Any], field: ExactField) -> Any:
    return sum((a * b for a, b in zip(left, right)), field.zero)
