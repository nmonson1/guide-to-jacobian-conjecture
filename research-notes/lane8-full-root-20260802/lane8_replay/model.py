"""Raw Newton-support and Jacobian-layer reconstruction for Lane 8."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Iterable

from sympy import Poly, QQ, Symbol

from .algebra import (
    K,
    ONE,
    U,
    ZERO,
    ParamPoly,
    add,
    constant,
    multiply,
    negate,
    rref_transform,
    scale,
    set_parameter_count,
    transform_polynomials,
    variable,
)

FIELD_POLYNOMIAL = "u^5-u^4+3*u^3+3*u^2+26"
RawTerm = tuple[int, int]


@dataclass(frozen=True)
class SupportCase:
    name: str
    p_vertices: list[RawTerm]
    q_vertices: list[RawTerm]
    parameter_count: int
    parameters_by_layer: dict[int, list[int]]
    last_layer: int


TRUNCATED = SupportCase(
    "truncated",
    [(0, 0), (1, 0), (8, 14), (8, 16)],
    [(0, 0), (2, 1), (12, 21), (12, 24)],
    6,
    {1: [0, 1], 2: [2, 3, 4], 3: [5]},
    5,
)
FULL = SupportCase(
    "full",
    [(0, 0), (1, 0), (8, 14), (8, 16), (0, 8)],
    [(0, 0), (2, 1), (12, 21), (12, 24), (0, 12)],
    9,
    {1: [0, 1], 2: [2, 3, 4], 3: [5, 6, 7], 4: [8]},
    8,
)


@dataclass
class LayerRun:
    case: SupportCase
    p_support: list[RawTerm]
    q_support: list[RawTerm]
    p_layers: defaultdict[int, list[RawTerm]]
    q_layers: defaultdict[int, list[RawTerm]]
    p_solution: dict[int, dict[RawTerm, ParamPoly]]
    q_solution: dict[int, dict[RawTerm, ParamPoly]]
    equations: list[tuple[int, ParamPoly]]
    layer_data: list[list[int]]


def hull(points: Iterable[RawTerm]) -> list[RawTerm]:
    points = sorted(set(points))

    def cross(origin: RawTerm, left: RawTerm, right: RawTerm) -> int:
        return (left[0] - origin[0]) * (right[1] - origin[1]) - (left[1] - origin[1]) * (right[0] - origin[0])

    lower: list[RawTerm] = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper: list[RawTerm] = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def inside(point: RawTerm, vertices: list[RawTerm]) -> bool:
    boundary = hull(vertices)
    crosses = [
        (right[0] - left[0]) * (point[1] - left[1]) - (right[1] - left[1]) * (point[0] - left[0])
        for left, right in zip(boundary, boundary[1:] + boundary[:1])
    ]
    return all(value >= 0 for value in crosses) or all(value <= 0 for value in crosses)


def lattice_points(vertices: list[RawTerm]) -> list[RawTerm]:
    return sorted(
        (x, y)
        for x in range(max(x for x, _ in vertices) + 1)
        for y in range(max(y for _, y in vertices) + 1)
        if inside((x, y), vertices)
    )


def support_layers(case: SupportCase):
    p_support = lattice_points(case.p_vertices)
    q_support = lattice_points(case.q_vertices)
    p_layers: defaultdict[int, list[RawTerm]] = defaultdict(list)
    q_layers: defaultdict[int, list[RawTerm]] = defaultdict(list)
    for x, y in p_support:
        p_layers[y - 2 * x + 2].append((x, y))
    for x, y in q_support:
        q_layers[y - 2 * x + 3].append((x, y))
    return p_support, q_support, p_layers, q_layers


def build_face(relation_path: Path):
    data = json.loads(relation_path.read_text(encoding="utf-8"))
    displayed = data["minimal_polynomial"].replace(" ", "").replace("x", "u")
    if displayed != FIELD_POLYNOMIAL:
        raise AssertionError(displayed)
    u = Symbol("u")
    if not Poly(u**5 - u**4 + 3 * u**3 + 3 * u**2 + 26, u, domain=QQ).is_irreducible:
        raise AssertionError("the displayed quintic is reducible over Q")

    p = [ONE, ONE]
    for degree in range(2, 8):
        relation = data["relations"][str(degree)]
        numerator = sum((K.convert(relation[index]) * U**index for index in range(5)), ZERO)
        p.append(-numerator / relation[5])
    q = [ONE]
    for degree in range(1, 11):
        total = ZERO
        for p_degree in range(1, min(7, degree) + 1):
            total += (1 + 2 * degree - 5 * p_degree) * p[p_degree] * q[degree - p_degree]
        q.append(-total / (1 + 2 * degree))

    for degree in range(18):
        total = ZERO
        for p_degree in range(max(0, degree - 10), min(7, degree) + 1):
            q_degree = degree - p_degree
            total += (1 + 2 * q_degree - 3 * p_degree) * p[p_degree] * q[q_degree]
        total -= ONE if degree == 0 else ZERO
        if total != ZERO:
            raise AssertionError(("face residual", degree, total))
    if p[-1] == ZERO or q[-1] == ZERO:
        raise AssertionError("face endpoint")
    return p, q


def bracket(p_terms: dict[RawTerm, ParamPoly], q_terms: dict[RawTerm, ParamPoly]):
    out: dict[RawTerm, ParamPoly] = {}
    for (i, j), p_coefficient in p_terms.items():
        for (k, ell), q_coefficient in q_terms.items():
            target = (i + k - 1, j + ell - 1)
            out[target] = add(
                out.get(target, {}),
                scale(i * ell - j * k, multiply(p_coefficient, q_coefficient)),
            )
    return out


def run_layers(case: SupportCase, p_coefficients, q_coefficients) -> LayerRun:
    set_parameter_count(case.parameter_count)
    p_support, q_support, p_layers, q_layers = support_layers(case)
    p_solution = {0: {(degree + 1, 2 * degree): constant(value) for degree, value in enumerate(p_coefficients)}}
    q_solution = {0: {(degree + 2, 2 * degree + 1): constant(value) for degree, value in enumerate(q_coefficients)}}
    equations: list[tuple[int, ParamPoly]] = []
    layer_data: list[list[int]] = []

    def target_rows(layer: int) -> list[RawTerm]:
        rows: set[RawTerm] = set()
        for p_layer in range(layer + 1):
            for i, j in p_layers.get(p_layer, []):
                for k, ell in q_layers.get(layer - p_layer, []):
                    rows.add((i + k - 1, j + ell - 1))
        return sorted(rows)

    for layer in range(1, case.last_layer + 1):
        rows = target_rows(layer)
        row_index = {term: index for index, term in enumerate(rows)}
        columns = [("P", term) for term in p_layers.get(layer, [])] + [("Q", term) for term in q_layers.get(layer, [])]
        matrix = [[ZERO] * len(columns) for _ in rows]
        for column_index, (kind, term) in enumerate(columns):
            if kind == "P":
                i, j = term
                for (k, ell), coefficient_poly in q_solution[0].items():
                    matrix[row_index[(i + k - 1, j + ell - 1)]][column_index] += (i * ell - j * k) * next(iter(coefficient_poly.values()))
            else:
                k, ell = term
                for (i, j), coefficient_poly in p_solution[0].items():
                    matrix[row_index[(i + k - 1, j + ell - 1)]][column_index] += (i * ell - j * k) * next(iter(coefficient_poly.values()))

        forcing = {row: {} for row in rows}
        for p_layer in range(1, layer):
            q_layer = layer - p_layer
            if p_layer not in p_solution or q_layer not in q_solution:
                continue
            for row, poly in bracket(p_solution[p_layer], q_solution[q_layer]).items():
                forcing[row] = add(forcing[row], poly)
        right_hand_side = [negate(forcing[row]) for row in rows]

        if not columns:
            equations.extend((layer, poly) for poly in forcing.values() if poly)
            layer_data.append([layer, 0, len(rows), 0, 0, sum(bool(poly) for poly in forcing.values())])
            continue

        reduced, transform, pivots = rref_transform(matrix)
        transformed_rhs = transform_polynomials(transform, right_hand_side)
        compatibility = transformed_rhs[len(pivots):]
        equations.extend((layer, poly) for poly in compatibility if poly)
        free_columns = [index for index in range(len(columns)) if index not in pivots]
        kernel: list[list] = []
        for free in free_columns:
            vector = [ZERO] * len(columns)
            vector[free] = ONE
            for pivot_row, pivot_column in enumerate(pivots):
                vector[pivot_column] = -reduced[pivot_row][free]
            kernel.append(vector)
        expected_parameters = case.parameters_by_layer.get(layer, [])
        if len(kernel) != len(expected_parameters):
            raise AssertionError((case.name, layer, len(kernel), len(expected_parameters)))

        solution = [{} for _ in columns]
        for pivot_row, pivot_column in enumerate(pivots):
            solution[pivot_column] = transformed_rhs[pivot_row]
        for parameter_index, vector in zip(expected_parameters, kernel):
            for column_index, coefficient in enumerate(vector):
                solution[column_index] = add(solution[column_index], scale(coefficient, variable(parameter_index)))
        p_solution[layer] = {}
        q_solution[layer] = {}
        for poly, (kind, term) in zip(solution, columns):
            (p_solution if kind == "P" else q_solution)[layer][term] = poly
        layer_data.append(
            [layer, len(columns), len(rows), len(pivots), len(kernel), sum(bool(poly) for poly in compatibility)]
        )

    return LayerRun(case, p_support, q_support, p_layers, q_layers, p_solution, q_solution, equations, layer_data)
