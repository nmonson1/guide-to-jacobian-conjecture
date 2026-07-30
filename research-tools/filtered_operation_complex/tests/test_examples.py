from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH_TOOLS = HERE.parent.parent
sys.path.insert(0, str(RESEARCH_TOOLS))

from filtered_operation_complex import analyze_document  # noqa: E402


class ExampleTests(unittest.TestCase):
    def test_two_chart_example_is_current(self) -> None:
        document = json.loads(
            (HERE.parent / "examples" / "two_chart_rational.json").read_text(
                encoding="utf-8"
            )
        )
        report = analyze_document(document)
        self.assertTrue(report["all_transitions_verified"])
        self.assertEqual(
            [layer["unexplained_dimension"] for layer in report["layers"]],
            [1, 1],
        )


if __name__ == "__main__":
    unittest.main()
