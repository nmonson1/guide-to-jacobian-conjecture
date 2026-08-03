"""Independent replay and stage-digest validation."""
from __future__ import annotations

from typing import Any

from .common import CONTRIBUTION_DIR, require, stage_by_id


def validate_replay(manifest: dict[str, Any], summary: dict[str, Any]) -> None:
    require(summary["schema"] == "lane8-independent-raw-support-replay-v1", "unexpected replay schema")
    scripts = [CONTRIBUTION_DIR / "independent_raw_support_replay.py",
               *(CONTRIBUTION_DIR / "lane8_replay").glob("*.py")]
    for path in scripts:
        require("sympy" not in path.read_text(encoding="utf-8").lower(),
                f"{path.name} reintroduced a nonstandard CAS dependency")
    require(all(summary["matches_public_expected"].values()),
            "replay disagrees with public expected digests")
    require(summary["field"] == manifest["field"], "field manifest disagrees with replay")

    replay = manifest["replay"]
    require(summary["truncated"]["minor_determinant_sha256"] == replay["truncated_minor_sha256"],
            "truncated minor digest mismatch")
    require(summary["full"]["final_equation_sha256"] == replay["full_fifteen_sha256"],
            "fifteen-equation digest mismatch")
    require(summary["full"]["terminal_projection"]["sha256"] == replay["terminal_projection_sha256"],
            "terminal-projection digest mismatch")
    require(summary["full"]["terminal_projection"]["zero_based_indices"]
            == replay["selected_zero_based_indices"], "terminal-projection index mismatch")
    require(summary["full"]["equation_manifest"] == replay["equation_manifest"],
            "equation manifest mismatch")
    selected = [replay["equation_manifest"][index] for index in replay["selected_zero_based_indices"]]
    require([row["term_count"] for row in selected] == [52, 52, 23, 75, 75, 75],
            "terminal projection no longer selects the six expected equations")
    require(summary["truncated"]["stage_data"] == replay["truncated_stage_data"],
            "truncated stage data mismatch")
    require(summary["full"]["stage_data"] == replay["full_stage_data"],
            "full stage data mismatch")
    require(summary["full"]["origin_vertex_parameters"] == replay["origin_vertex_parameters"],
            "origin parameter mismatch")
    require(summary["full"]["higher_deficiency_coefficients_projected_away"]
            == replay["higher_deficiency_projection"], "higher-deficiency projection mismatch")

    for root_name in ("truncated", "full"):
        for stage in summary[root_name]["stage_data"]:
            require(stage["inverted_parameter_polynomials"] == [],
                    f"unrecorded variable denominator at {root_name} layer {stage['layer']}")
            require(stage["pivot_unit_count"] == len(stage["pivot_columns"]),
                    f"pivot ledger mismatch at {root_name} layer {stage['layer']}")

    require(summary["truncated"]["macaulay_rank"] == 14, "truncated rank is not 14")
    require(summary["truncated"]["weight_four_monomial_count"] == 14,
            "truncated target is not complete")
    require(summary["full"]["weight_four_is_square"], "layer-four square was not reconstructed")
    require(summary["full"]["vertex_saturation_forces_t11_nonzero"],
            "t1_1 complement was not closed")
    require(summary["full"]["final_equation_counts"] == {"5": 1, "6": 3, "7": 5, "8": 6},
            "unexpected fifteen-equation weight distribution")

    require(stage_by_id(manifest, "S1-TRUNCATED-LAYERS")["evidence"]["stage_data"]
            == summary["truncated"]["stage_data"], "stage S1 does not pin the replayed layer data")
    require(stage_by_id(manifest, "S2-FULL-LAYERS-1-4")["evidence"]["stage_data"]
            == summary["full"]["stage_data"][:4], "stage S2 does not pin layers one through four")
    require(stage_by_id(manifest, "S5-FULL-LAYERS-5-8")["evidence"]["stage_data"]
            == summary["full"]["stage_data"][4:], "stage S5 does not pin layers five through eight")
