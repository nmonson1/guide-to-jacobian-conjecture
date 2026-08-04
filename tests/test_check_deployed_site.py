from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_deployed_site  # noqa: E402


class DeployedRetainedMathTests(unittest.TestCase):
    def test_live_contract_tracks_current_lane_6_graph_and_handoff(self) -> None:
        state = json.loads((ROOT / "site-state.json").read_text(encoding="utf-8"))
        retained = state["retained_math_v2"]["data_dir"]
        graph = json.loads(
            (ROOT / "data" / retained / "public-graph.json").read_text(
                encoding="utf-8"
            )
        )
        task_ids = {item["task_id"] for item in graph["tasks"]}
        obligation_ids = {
            item["obligation_id"] for item in graph["obligations"]
        }
        self.assertIn(check_deployed_site.FULL_ROW_TASK_ID, task_ids)
        self.assertIn(check_deployed_site.FULL_ROW_OBLIGATION_ID, obligation_ids)

        lane6 = (
            ROOT
            / state["docs_dir"]
            / "research/handoffs/homogeneous-realization-compression.md"
        ).read_text(encoding="utf-8")
        for marker in check_deployed_site.LANE6_INTERFACE_MARKERS:
            self.assertIn(marker, lane6)

    def test_loads_full_graph_machine_route(self) -> None:
        graph = {
            "registry_id": "RETAINED2-test",
            "counts": {"units": 3},
            "obligations": [],
            "tasks": [],
        }
        metadata = {
            "source_registry_id": "RETAINED2-test",
            "counts": {"units": 3},
            "machine_routes": {
                "graph": "research/working-mathematics/graph.json",
                "legacy_compatibility": (
                    "research/working-mathematics/legacy-compatibility.json"
                ),
            },
        }
        with patch.object(
            check_deployed_site,
            "_fetch",
            return_value=json.dumps(graph).encode("utf-8"),
        ) as fetch:
            payload, failures = check_deployed_site._load_retained_v2(
                "https://example.invalid/guide/", metadata, "release-test"
            )

        self.assertEqual(payload, graph)
        self.assertEqual(failures, [])
        fetch.assert_called_once_with(
            "https://example.invalid/guide/research/working-mathematics/graph.json"
            "?release=release-test"
        )

    def test_still_loads_legacy_selection_machine_route(self) -> None:
        selection = {
            "selection_id": "selection-test",
            "obligations": [],
            "tasks": [],
        }
        metadata = {
            "selection_id": "selection-test",
            "machine_route": "research/handoffs/retained-math-v2-pilot.json",
        }
        with patch.object(
            check_deployed_site,
            "_fetch",
            return_value=json.dumps(selection).encode("utf-8"),
        ):
            payload, failures = check_deployed_site._load_retained_v2(
                "https://example.invalid/guide/", metadata, "release-test"
            )

        self.assertEqual(payload, selection)
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
