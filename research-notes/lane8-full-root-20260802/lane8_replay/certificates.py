"""Exact truncated and full-root certificates derived from reconstructed layers."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from . import algebra
from .algebra import (
    ZERO,
    KElement,
    ParamPoly,
    clean,
    determinant,
    k_expr,
    k_vector,
    normalized,
    polynomial_json,
    rref_transform,
    weighted_degree,
)
from .model import FIELD_POLYNOMIAL, LayerRun


def weight_four_monomials() -> list[tuple[int, int, int, int]]:
    out = []
    for a in range(5):
        for b in range(5):
            for c in range(3):
                for d in range(3):
                    if a + b + 2 * c + 2 * d == 4:
                        out.append((a, b, c, d))
    return out


def analyze_truncated(run: LayerRun) -> dict[str, Any]:
    expected = [
        [1, 19, 18, 17, 2, 0],
        [2, 21, 19, 18, 3, 0],
        [3, 13, 20, 12, 1, 7],
        [4, 0, 20, 0, 0, 18],
        [5, 0, 21, 0, 0, 0],
    ]
    if run.layer_data != expected:
        raise AssertionError(run.layer_data)
    weights = (1, 1, 2, 2, 2, 3)
    for layer, poly in run.equations:
        if weighted_degree(poly, weights) != layer:
            raise AssertionError("unexpected truncated obstruction weight")
        if any(monomial[2] or monomial[5] for monomial in poly):
            raise AssertionError("a split parameter entered a truncated obstruction")

    core = (0, 1, 3, 4)

    def project(poly: ParamPoly) -> ParamPoly:
        return {tuple(monomial[index] for index in core): coefficient for monomial, coefficient in poly.items()}

    weight_three = [project(poly) for layer, poly in run.equations if layer == 3]
    weight_four = [project(poly) for layer, poly in run.equations if layer == 4]
    monomials = weight_four_monomials()
    monomial_index = {monomial: index for index, monomial in enumerate(monomials)}
    rows: list[list[KElement]] = []
    labels: list[tuple[str, int]] = []
    for equation_index, poly in enumerate(weight_four):
        row = [ZERO] * len(monomials)
        for monomial, coefficient in poly.items():
            row[monomial_index[monomial]] = coefficient
        rows.append(row)
        labels.append(("E4", equation_index))
    for variable_index in (0, 1):
        for equation_index, poly in enumerate(weight_three):
            row = [ZERO] * len(monomials)
            for monomial, coefficient in poly.items():
                shifted = list(monomial)
                shifted[variable_index] += 1
                row[monomial_index[tuple(shifted)]] = coefficient
            rows.append(row)
            labels.append((f"t1_{variable_index}*E3", equation_index))

    _, _, pivots = rref_transform(rows)
    if len(pivots) != 14 or len(monomials) != 14:
        raise AssertionError((len(pivots), len(monomials)))
    transpose = [[rows[row][column] for row in range(len(rows))] for column in range(len(monomials))]
    _, _, independent_rows = rref_transform(transpose)
    selected = independent_rows[:14]
    minor = [[rows[row][column] for column in range(14)] for row in selected]
    determinant_value = determinant(minor)
    if determinant_value == ZERO:
        raise AssertionError("truncated Macaulay minor vanished")

    top_p = run.p_solution[2][(8, 16)]
    top_q = run.q_solution[3][(12, 24)]
    if not top_p or not top_q:
        raise AssertionError("a truncated top-vertex coefficient vanished identically")
    if weighted_degree(top_p, weights) != 2 or weighted_degree(top_q, weights) != 3:
        raise AssertionError("unexpected truncated top-vertex weight")
    if any(monomial[2] or monomial[5] for monomial in top_p) or any(
        monomial[2] or monomial[5] for monomial in top_q
    ):
        raise AssertionError("a split parameter entered a truncated top vertex")

    return {
        "support_sizes": {"P": len(run.p_support), "Q": len(run.q_support)},
        "layer_data": run.layer_data,
        "weight_three_equation_count": len(weight_three),
        "weight_four_equation_count": len(weight_four),
        "weight_four_monomial_count": len(monomials),
        "macaulay_rank": len(pivots),
        "selected_rows": [{"row_index": row, "source": list(labels[row])} for row in selected],
        "minor_determinant_nonzero": True,
        "minor_determinant_sha256": hashlib.sha256(
            json.dumps(k_vector(determinant_value), separators=(",", ":")).encode()
        ).hexdigest(),
        "top_vertex_weights": {"P_8_16": 2, "Q_12_24": 3},
        "top_vertex_coefficients_depend_only_on_radical_variables": True,
        "top_vertex_coefficients_vanish_when_the_four_effective_variables_vanish": True,
        "exact_support_requires_both_top_vertices_nonzero": True,
        "conclusion": "vertex-saturated truncated system is empty",
    }


def specialize_full(poly: ParamPoly, alpha: KElement) -> ParamPoly:
    keep = (0, 3, 6, 7, 8)
    out: ParamPoly = {}
    for monomial, coefficient in poly.items():
        reduced = tuple(monomial[index] for index in keep)
        out[reduced] = out.get(reduced, ZERO) + coefficient * alpha**monomial[4]
    return clean(out)


def endpoint_after_square(poly: ParamPoly, alpha: KElement) -> tuple[int, KElement]:
    out: dict[int, KElement] = {}
    for monomial, coefficient in poly.items():
        if any(monomial[index] for index in range(algebra.NVAR) if index not in (1, 4)):
            raise AssertionError("unexpected parameter in a full top-vertex coefficient")
        exponent = monomial[1] + 2 * monomial[4]
        out[exponent] = out.get(exponent, ZERO) + coefficient * alpha**monomial[4]
    out = {exponent: coefficient for exponent, coefficient in out.items() if coefficient != ZERO}
    if len(out) != 1:
        raise AssertionError(out)
    return next(iter(out.items()))


def analyze_full(run: LayerRun):
    expected = [
        [1, 19, 18, 17, 2, 0],
        [2, 21, 19, 18, 3, 0],
        [3, 21, 20, 18, 3, 0],
        [4, 19, 20, 18, 1, 2],
        [5, 17, 21, 17, 0, 2],
        [6, 15, 20, 15, 0, 4],
        [7, 13, 19, 13, 0, 5],
        [8, 11, 18, 11, 0, 6],
    ]
    if run.layer_data != expected:
        raise AssertionError(run.layer_data)
    weights = (1, 1, 2, 2, 2, 3, 3, 3, 4)
    for layer, poly in run.equations:
        if weighted_degree(poly, weights) != layer:
            raise AssertionError("unexpected full obstruction weight")
        if any(monomial[2] or monomial[5] for monomial in poly):
            raise AssertionError("a split parameter entered a full obstruction")

    weight_four: list[ParamPoly] = []
    for layer, poly in run.equations:
        if layer == 4:
            _, candidate = normalized(poly)
            if not any(candidate == old for old in weight_four):
                weight_four.append(candidate)
    if len(weight_four) != 1:
        raise AssertionError(len(weight_four))
    square = weight_four[0]
    if any(any(monomial[index] for index in range(algebra.NVAR) if index not in (1, 4)) for monomial in square):
        raise AssertionError("unexpected square support")
    t22_squared = (0, 0, 0, 0, 2, 0, 0, 0, 0)
    t11_squared_t22 = (0, 2, 0, 0, 1, 0, 0, 0, 0)
    t11_fourth = (0, 4, 0, 0, 0, 0, 0, 0, 0)
    leading = square.get(t22_squared, ZERO)
    middle = square.get(t11_squared_t22, ZERO)
    trailing = square.get(t11_fourth, ZERO)
    if leading == ZERO:
        raise AssertionError("square leading coefficient vanished")
    alpha = -middle / (2 * leading)
    if trailing / leading != alpha**2:
        raise AssertionError("weight-four equation is not the claimed square")

    p_exponent, p_endpoint = endpoint_after_square(run.p_solution[2][(8, 16)], alpha)
    q_exponent, q_endpoint = endpoint_after_square(run.q_solution[3][(12, 24)], alpha)
    if (p_exponent, q_exponent) != (2, 3) or p_endpoint == ZERO or q_endpoint == ZERO:
        raise AssertionError("full top-vertex normalization failed")

    final: list[tuple[int, ParamPoly]] = []
    for layer, poly in run.equations:
        specialized = specialize_full(poly, alpha)
        if not specialized:
            continue
        _, candidate = normalized(specialized)
        if not any(layer == old_layer and candidate == old for old_layer, old in final):
            final.append((layer, candidate))
    counts = {layer: sum(candidate_layer == layer for candidate_layer, _ in final) for layer in (5, 6, 7, 8)}
    if counts != {5: 1, 6: 3, 7: 5, 8: 6}:
        raise AssertionError(counts)

    equations = [{"weight": layer, "terms": polynomial_json(poly)} for layer, poly in final]
    canonical = (json.dumps(equations, sort_keys=True, separators=(",", ":")) + "\n").encode()
    equation_digest = hashlib.sha256(canonical).hexdigest()
    legacy = {
        "field_polynomial": FIELD_POLYNOMIAL,
        "normalization": "p0=q0=p1=1; t1_1=1; t2_2=alpha",
        "variables": ["x", "a", "b", "c", "d"],
        "original_parameter_indices": [0, 3, 6, 7, 8],
        "layer_data": run.layer_data,
        "alpha": k_expr(alpha, symbol="x"),
        "Ptop": k_expr(p_endpoint, symbol="x"),
        "Qtop": k_expr(q_endpoint, symbol="x"),
        "equations": [
            {
                "weight": layer,
                "terms": [
                    {"exp": list(monomial), "coeff": k_expr(coefficient, symbol="x")}
                    for monomial, coefficient in sorted(poly.items())
                ],
            }
            for layer, poly in final
        ],
    }
    selected_indices = [4, 6, 8, 9, 10, 11]
    selected = [equations[index] for index in selected_indices]
    selected_canonical = (json.dumps(selected, sort_keys=True, separators=(",", ":")) + "\n").encode()
    equation_manifest = [
        {
            "index": index,
            "weight": equation["weight"],
            "term_count": len(equation["terms"]),
            "sha256": hashlib.sha256(
                (json.dumps(equation, sort_keys=True, separators=(",", ":")) + "\n").encode()
            ).hexdigest(),
        }
        for index, equation in enumerate(equations)
    ]
    summary = {
        "support_sizes": {"P": len(run.p_support), "Q": len(run.q_support)},
        "layer_data": run.layer_data,
        "weight_four_is_square": True,
        "alpha_basis": k_vector(alpha),
        "top_P_after_square": {"t11_exponent": p_exponent, "coefficient_basis": k_vector(p_endpoint)},
        "top_Q_after_square": {"t11_exponent": q_exponent, "coefficient_basis": k_vector(q_endpoint)},
        "vertex_saturation_forces_t11_nonzero": True,
        "normalization": "t1_1=1; t2_2=alpha; retain t1_0,t2_1,t3_1,t3_2,t4_0",
        "final_equation_counts": counts,
        "final_equation_sha256": equation_digest,
        "equation_manifest": equation_manifest,
        "terminal_projection": {
            "zero_based_indices": selected_indices,
            "equation_count": len(selected),
            "sha256": hashlib.sha256(selected_canonical).hexdigest(),
            "logical_direction": "V(all fifteen) is contained in V(the selected six)",
        },
        "denominator_audit": {
            "layer_matrix_entries": "fixed elements of K0",
            "row_reduction_pivots": "nonzero fixed elements of K0",
            "variable_denominators_introduced_before_normalization": [],
            "only_open_factor": "t1_1",
            "closed_complement": "t1_1=0 contradicts exact top-vertex support",
        },
        "conclusion": "raw full support reduces exactly to fifteen normalized equations",
    }
    return summary, equations, legacy, selected


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
