#!/usr/bin/env python3
"""Decompose the archived degree-21 kernels by the common-root defect.

For the leading pair ``u0=R^2`` and ``v0=R^3`` with x-degrees 8 and 12,
put

    N(u,v) = 2 v - 3 R u.

A direct calculation factors the archived layer operator as

    L_r(u,v) = R * (4 R N' + (r-12) R' N).

Hence a nonzero polynomial defect can occur only when ``12-r`` is divisible
by four, in which case it is a scalar multiple of ``R^((12-r)/4)``.  This
script verifies the factorization and this decomposition on every archived
right-nullspace vector.  It does not by itself prove that an exceptional class
is an admissible adjacent-chart transition; that geometric identification is
a separate step.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

from chart_correspondence import Vector, parse_vectors, rank_of_vectors, rational_string
from degree21_linear_replay import (
    Poly,
    R,
    add,
    clean,
    column_image,
    derivative,
    multiply,
    ordered_bases,
    power,
    scale,
)


def polynomial_json(poly: Mapping[int, Fraction]) -> list[dict[str, Any]]:
    return [
        {"exponent": exponent, "coefficient": rational_string(coefficient)}
        for exponent, coefficient in sorted(poly.items())
        if coefficient
    ]


def vector_json(vector: Vector) -> list[str]:
    return [rational_string(value) for value in vector]


def vector_to_variation(
    layer: Mapping[str, Any], vector: Vector
) -> tuple[Poly, Poly]:
    _, basis, _ = ordered_bases(layer)
    if len(vector) != len(basis):
        raise ValueError("kernel vector length does not match the domain basis")
    u: Poly = {}
    v: Poly = {}
    for coefficient, item in zip(vector, basis):
        if coefficient == 0:
            continue
        target = u if item[0] == "u" else v
        exponent = int(item[1])
        target[exponent] = target.get(exponent, Fraction(0)) + coefficient
    return clean(u), clean(v)


def common_root_defect(u: Mapping[int, Fraction], v: Mapping[int, Fraction]) -> Poly:
    return add(scale(v, 2), scale(multiply(R, u), -3))


def ode_residual(r: int, defect: Mapping[int, Fraction]) -> Poly:
    return add(
        scale(multiply(R, derivative(defect)), 4),
        scale(multiply(derivative(R), defect), r - 12),
    )


def layer_factorization_residual(
    r: int, kind: str, exponent: int
) -> Poly:
    u = {exponent: Fraction(1)} if kind == "u" else {}
    v = {exponent: Fraction(1)} if kind == "v" else {}
    defect = common_root_defect(u, v)
    factored = multiply(R, ode_residual(r, defect))
    return add(column_image(r, kind, exponent), scale(factored, -1))


def scalar_multiple(
    value: Mapping[int, Fraction], template: Mapping[int, Fraction]
) -> Fraction | None:
    value = clean(value)
    template = clean(template)
    if not value:
        return Fraction(0)
    if not template:
        return None
    pivot = next(iter(sorted(template)))
    if pivot not in value:
        return None
    scalar = value[pivot] / template[pivot]
    return scalar if value == scale(template, scalar) else None


def polynomial_rank(polys: Sequence[Mapping[int, Fraction]]) -> int:
    exponents = sorted({exponent for poly in polys for exponent in poly})
    vectors = [
        [poly.get(exponent, Fraction(0)) for exponent in exponents]
        for poly in polys
    ]
    return rank_of_vectors(vectors, ambient_dimension=len(exponents))


def normalized_exceptional(
    layer: Mapping[str, Any],
    vectors: Sequence[Vector],
    defects: Sequence[Poly],
    template: Mapping[int, Fraction],
) -> dict[str, Any] | None:
    for vector, defect in zip(vectors, defects):
        scalar = scalar_multiple(defect, template)
        if scalar is None or scalar == 0:
            continue
        normalized_vector = [value / scalar for value in vector]
        u, v = vector_to_variation(layer, normalized_vector)
        normalized_defect = common_root_defect(u, v)
        if normalized_defect != clean(template):
            raise ValueError("failed to normalize an exceptional kernel vector")
        return {
            "coordinates": vector_json(normalized_vector),
            "u": polynomial_json(u),
            "v": polynomial_json(v),
            "defect": polynomial_json(normalized_defect),
        }
    return None


def audit_layer(case: str, layer: Mapping[str, Any]) -> dict[str, Any]:
    r, basis, _ = ordered_bases(layer)
    for kind, exponent in basis:
        residual = layer_factorization_residual(r, kind, exponent)
        if residual:
            raise ValueError(
                f"{case}.r{r}: factorization fails on {(kind, exponent)}: "
                f"{polynomial_json(residual)}"
            )

    values = layer.get("right_nullspace")
    if not isinstance(values, list):
        raise ValueError(f"{case}.r{r}.right_nullspace must be a list")
    vectors = parse_vectors(
        values,
        width=len(basis),
        name=f"{case}.r{r}.right_nullspace",
    )
    defects: list[Poly] = []
    for index, vector in enumerate(vectors):
        u, v = vector_to_variation(layer, vector)
        defect = common_root_defect(u, v)
        residual = ode_residual(r, defect)
        if residual:
            raise ValueError(
                f"{case}.r{r}: kernel vector {index} violates the defect ODE"
            )
        defects.append(defect)

    exponent: int | None = None
    template: Poly = {}
    if 12 - r >= 0 and (12 - r) % 4 == 0:
        exponent = (12 - r) // 4
        template = power(R, exponent)
        for index, defect in enumerate(defects):
            if scalar_multiple(defect, template) is None:
                raise ValueError(
                    f"{case}.r{r}: defect {index} is not a multiple of R^{exponent}"
                )
    elif any(defects):
        raise ValueError(
            f"{case}.r{r}: a nonzero polynomial defect occurs off resonance"
        )

    exceptional_dimension = polynomial_rank(defects)
    kernel_dimension = int(layer["kernel_dim"])
    common_root_dimension = kernel_dimension - exceptional_dimension
    if common_root_dimension < 0:
        raise ValueError(f"{case}.r{r}: defect rank exceeds kernel dimension")

    return {
        "case": case,
        "r": r,
        "kernel_dimension": kernel_dimension,
        "common_root_dimension": common_root_dimension,
        "exceptional_dimension": exceptional_dimension,
        "resonance_exponent": exponent,
        "factorization_verified": True,
        "defect_ode_verified": True,
        "normalized_exceptional": (
            normalized_exceptional(layer, vectors, defects, template)
            if exceptional_dimension
            else None
        ),
    }


def audit_document(document: Mapping[str, Any]) -> dict[str, Any]:
    layers: list[dict[str, Any]] = []
    for case in ("truncated", "full"):
        case_data = document.get(case)
        if not isinstance(case_data, dict) or not isinstance(case_data.get("layers"), list):
            raise ValueError(f"missing {case}.layers")
        layers.extend(audit_layer(case, layer) for layer in case_data["layers"])

    exceptional = [
        {"case": item["case"], "r": item["r"], "dimension": item["exceptional_dimension"]}
        for item in layers
        if item["exceptional_dimension"]
    ]
    return {
        "schema_version": 1,
        "name": "degree-21 common-root defect decomposition",
        "identity": "L_r(u,v)=R*(4R*N'+(r-12)R'*N), N=2v-3Ru",
        "polynomial_resonance_rule": "N^4=c*R^(12-r)",
        "scope": (
            "Exact decomposition of the archived raw upper-face kernels. "
            "Geometric recognition of an exceptional class as a rechart remains separate."
        ),
        "layers": layers,
        "exceptional_layers": exceptional,
        "all_layers_verified": all(
            item["factorization_verified"] and item["defect_ode_verified"]
            for item in layers
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)
    try:
        document = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(document, dict):
            raise ValueError("input must be a JSON object")
        report = audit_document(document)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"degree21_kernel_decomposition: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0 if report["all_layers_verified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
