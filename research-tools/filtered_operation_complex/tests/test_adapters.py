from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH_TOOLS = HERE.parent.parent
sys.path.insert(0, str(RESEARCH_TOOLS))

from filtered_operation_complex.adapters.program5_row_killing import (  # noqa: E402
    analyze_packet,
)
from filtered_operation_complex.adapters.program6_legacy import (  # noqa: E402
    analyze_legacy_document,
)


class AdapterTests(unittest.TestCase):
    def test_program6_legacy_k4_shape(self) -> None:
        legacy = {
            "schema_version": 1,
            "name": "legacy synthetic k4",
            "layers": [
                {
                    "label": "layer 1",
                    "operator": [[0, 1]],
                    "gauge_vectors": [[1, 0]],
                    "rechart_vectors": [],
                },
                {
                    "label": "layer 2",
                    "operator": [[0, 0, 1]],
                    "gauge_vectors": [[1, 0, 0], [0, 1, 0]],
                    "rechart_vectors": [],
                },
                {
                    "label": "layer 3",
                    "operator": [[1, 0]],
                    "gauge_vectors": [[0, 1]],
                    "rechart_vectors": [],
                },
                {
                    "label": "layer 4",
                    "operator": [[0, 1]],
                    "gauge_vectors": [],
                    "rechart_vectors": [[1, 0]],
                    "support_transport": {"k": 4, "monomials": [[2, 2]]},
                },
            ],
        }
        report = analyze_legacy_document(legacy)
        self.assertTrue(report["all_true_quotients_zero"])
        self.assertEqual(
            [layer["kernel_dimension"] for layer in report["layers"]],
            [1, 2, 1, 1],
        )
        self.assertEqual(report["layers"][3]["gauge_dimension"], 0)
        self.assertEqual(report["layers"][3]["rechart_increment"], 1)
        closure = report["adapter_metadata"]["support_closures"][0]["closure"]
        self.assertEqual(closure, [[2, 2], [-2, 1], [-6, 0]])

    def test_program5_template(self) -> None:
        packet = json.loads(
            (HERE.parent / "examples" / "program5_row_killing_template.json").read_text(
                encoding="utf-8"
            )
        )
        report = analyze_packet(packet)
        layer = report["layers"][0]
        self.assertEqual(layer["kernel_dimension"], 4)
        self.assertEqual(layer["gauge_dimension"], 3)
        self.assertEqual(layer["rechart_increment"], 1)
        self.assertEqual(layer["unexplained_dimension"], 0)
        self.assertEqual(layer["forcing_pairings"], ["-1"])


if __name__ == "__main__":
    unittest.main()
