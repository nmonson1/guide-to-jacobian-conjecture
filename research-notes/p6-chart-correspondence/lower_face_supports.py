#!/usr/bin/env python3
"""Convert the archived Newton supports to lower-face normal-layer windows.

In the lower-face chart

    t = Y,   z = X Y^2,

one has

    X^i Y^j = z^i t^(j-2i).

The degree-21 leading forms are written

    P = t^-2 (A_0(z) + t A_1(z) + ...),
    Q = t^-3 (B_0(z) + t B_1(z) + ...).

Therefore a P-support point (i,j) belongs to normal layer

    r_P = j - 2i + 2,

and a Q-support point belongs to

    r_Q = j - 2i + 3.

This script performs that exact combinatorial conversion for the full and
truncated support sets in the pinned degree-21 fixture.  It does not infer the
source-automorphism windows used in Proposition C.9.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Mapping, Sequence


def parse_points(values: Any, *, name: str) -> list[tuple[int, int]]:
    if not isinstance(values, list):
        raise ValueError(f"{name} must be a list")
    points: list[tuple[int, int]] = []
    for index, value in enumerate(values):
        if (
            not isinstance(value, list)
            or len(value) != 2
            or not all(isinstance(entry, int) and not isinstance(entry, bool) for entry in value)
        ):
            raise ValueError(f"{name}[{index}] must be an integer pair")
        point = (value[0], value[1])
        if point in points:
            raise ValueError(f"{name} contains duplicate point {point}")
        points.append(point)
    return points


def slice_support(
    points: Sequence[tuple[int, int]], *, pole_order: int
) -> dict[int, list[int]]:
    layers: dict[int, list[int]] = defaultdict(list)
    for i, j in points:
        layer = j - 2 * i + pole_order
        layers[layer].append(i)
    return {
        layer: sorted(exponents)
        for layer, exponents in sorted(layers.items())
    }


def roundtrip_points(
    layers: Mapping[int, Sequence[int]], *, pole_order: int
) -> list[tuple[int, int]]:
    return sorted(
        (i, 2 * i - pole_order + layer)
        for layer, exponents in layers.items()
        for i in exponents
    )


def analyze_case(label: str, data: Mapping[str, Any]) -> dict[str, Any]:
    p_points = parse_points(data.get("P_support"), name=f"{label}.P_support")
    q_points = parse_points(data.get("Q_support"), name=f"{label}.Q_support")
    p_layers = slice_support(p_points, pole_order=2)
    q_layers = slice_support(q_points, pole_order=3)
    if roundtrip_points(p_layers, pole_order=2) != sorted(p_points):
        raise AssertionError(f"{label}: P support roundtrip failed")
    if roundtrip_points(q_layers, pole_order=3) != sorted(q_points):
        raise AssertionError(f"{label}: Q support roundtrip failed")

    all_layers = sorted(set(p_layers) | set(q_layers))
    return {
        "label": label,
        "P_point_count": len(p_points),
        "Q_point_count": len(q_points),
        "minimum_layer": min(all_layers) if all_layers else None,
        "maximum_layer": max(all_layers) if all_layers else None,
        "layers": [
            {
                "r": layer,
                "a_support": p_layers.get(layer, []),
                "b_support": q_layers.get(layer, []),
                "a_dimension": len(p_layers.get(layer, [])),
                "b_dimension": len(q_layers.get(layer, [])),
            }
            for layer in all_layers
        ],
    }


def analyze_document(document: Mapping[str, Any]) -> dict[str, Any]:
    results = []
    for label in ("truncated", "full"):
        data = document.get(label)
        if not isinstance(data, dict):
            raise ValueError(f"missing {label} support data")
        results.append(analyze_case(label, data))
    return {
        "schema_version": 1,
        "coordinates": {"t": "Y", "z": "X Y^2"},
        "layer_formulas": {
            "P": "r=j-2i+2",
            "Q": "r=j-2i+3",
        },
        "cases": results,
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
        report = analyze_document(document)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"lower_face_supports: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
