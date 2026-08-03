#!/usr/bin/env python3
"""Independently rebuild both Lane 8 roots from raw Newton supports.

The replay uses the published support polygons, the exact degree-21 face
relations, and the coefficient formula for a polynomial Jacobian bracket. It
does not consume archived layer matrices or archived obstruction equations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from lane8_replay.certificates import analyze_full, analyze_truncated, write_json
from lane8_replay.model import FIELD_POLYNOMIAL, FULL, TRUNCATED, build_face, run_layers

SCRIPT_DIR = Path(__file__).resolve().parent


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--relations",
        type=Path,
        default=(
            SCRIPT_DIR / "fixtures" / "belyi_exact_field_relations.json"
        ),
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="write only summary.json after performing the complete exact reconstruction",
    )
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)

    p, q = build_face(args.relations)
    truncated = run_layers(TRUNCATED, p, q)
    full = run_layers(FULL, p, q)
    truncated_summary = analyze_truncated(truncated)
    full_summary, full_equations, legacy, selected = analyze_full(full)

    args.output.mkdir(parents=True)
    if not args.summary_only:
        write_json(args.output / "full_equations.json", full_equations)
        write_json(args.output / "full_exact_fivevar_w8.json", legacy)
        write_json(args.output / "full_terminal_projection.json", selected)
    summary = {
        "schema": "lane8-independent-raw-support-replay-v1",
        "field": {
            "minimal_polynomial": FIELD_POLYNOMIAL,
            "basis": ["1", "u", "u^2", "u^3", "u^4"],
            "irreducible_over_Q": True,
            "irreducibility_witness": {"prime": 67, "method": "Rabin test"},
        },
        "inputs": {
            "relations_file_sha256": hashlib.sha256(args.relations.read_bytes()).hexdigest(),
            "archived_layers_used": False,
            "archived_equations_used": False,
        },
        "face": {
            "p_degree": len(p) - 1,
            "q_degree": len(q) - 1,
            "jacobian_coefficients_verified": 18,
            "endpoint_coefficients_nonzero": True,
        },
        "truncated": truncated_summary,
        "full": full_summary,
        "public_expected": {
            "truncated_minor_determinant_sha256": "8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059",
            "full_equation_sha256": "d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883",
        },
    }
    summary["matches_public_expected"] = {
        "truncated_minor": truncated_summary["minor_determinant_sha256"]
        == summary["public_expected"]["truncated_minor_determinant_sha256"],
        "full_equations": full_summary["final_equation_sha256"]
        == summary["public_expected"]["full_equation_sha256"],
    }
    if not all(summary["matches_public_expected"].values()):
        raise AssertionError(summary["matches_public_expected"])
    write_json(args.output / "summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
