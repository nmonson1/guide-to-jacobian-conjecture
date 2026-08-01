#!/usr/bin/env python3
"""Lift coordinate samples of the Program 5 infinity row-base fibre.

At the projective point v=0, u=1, quadratic compatibility fixes

    s3 = 0,  s4 = 1,

and leaves the other eighteen row-zero tangent coordinates free.  The base
section theta_u survives cubic order but is obstructed at order four.  This
adapter tests theta_u and each positive coordinate translate

    theta_u + xi_i,  i not in {3,4},

through order four, always allowing the complete 22-dimensional tangent
freedom in every higher correction.

This coordinate scan is exploratory.  It does not classify the full
18-dimensional infinity fibre; surviving samples are branch candidates for a
subsequent higher-order or symbolic family audit.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from .program5_compression_export import DEFAULT_SOURCE
from .program5_rank_six_formal_lift_engine import lift_formal_direction
from .program5_rank_six_schur_model import build_schur_model


def analyze_infinity_fibre_formal_scan(
    source_path: Path = DEFAULT_SOURCE,
    *,
    max_order: int = 4,
) -> dict[str, Any]:
    model = build_schur_model(source_path)
    infinity_indices = [index for index in range(20) if index not in (3, 4)]
    samples = [
        {
            "name": "infinity:base",
            "row_adjustments": [],
            "theta": model.theta_u,
        }
    ] + [
        {
            "name": f"infinity:+xi_{index}",
            "row_adjustments": [
                {"row_basis_index": index, "coefficient": 1}
            ],
            "theta": model.theta_u + model.row_basis[index],
        }
        for index in infinity_indices
    ]

    results = []
    for sample in samples:
        lift = lift_formal_direction(
            model,
            sample["theta"],
            name=sample["name"],
            max_order=max_order,
            verify_effect=sample["name"] == "infinity:base",
        )
        results.append(
            {
                "name": sample["name"],
                "row_adjustments": sample["row_adjustments"],
                **lift,
            }
        )

    first_obstruction_histogram: dict[str, int] = {}
    survivors = []
    for result in results:
        obstruction = result["first_obstructed_order"]
        key = "none" if obstruction is None else str(obstruction)
        first_obstruction_histogram[key] = (
            first_obstruction_histogram.get(key, 0) + 1
        )
        if obstruction is None:
            survivors.append(result["name"])

    return {
        "schema_version": 1,
        "name": "Program 5 infinity row-base formal coordinate scan",
        "source_file": str(source_path),
        "source_sha256": model.source_sha256,
        "ambient_operation_dimension": model.ambient_operation_dimension,
        "rank_six_tangent_dimension": len(model.tangent_basis),
        "infinity_fibre_dimension": len(infinity_indices),
        "sample_count": len(results),
        "maximum_requested_order": max_order,
        "first_obstruction_histogram": first_obstruction_histogram,
        "survivor_count": len(survivors),
        "survivors_through_requested_order": survivors,
        "samples": results,
        "interpretation_boundary": (
            "The scan tests the base point and eighteen positive coordinate "
            "translates in the infinity fibre. It does not exclude mixed, "
            "negative, rational, or algebraic row-base combinations."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--max-order", type=int, default=4)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = analyze_infinity_fibre_formal_scan(
            args.source,
            max_order=args.max_order,
        )
    except (OSError, ValueError, TypeError, AssertionError) as exc:
        print(
            f"program5_rank_six_infinity_fibre_formal_scan: {exc}",
            file=sys.stderr,
        )
        return 2
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
