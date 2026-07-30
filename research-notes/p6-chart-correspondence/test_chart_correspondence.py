#!/usr/bin/env python3
from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path

from chart_correspondence import analyze_document, nullspace, transport_support


class ExactLinearAlgebraTests(unittest.TestCase):
    def test_nullspace_over_q(self) -> None:
        basis = nullspace([
            [Fraction(1), Fraction(2), Fraction(3)],
            [Fraction(0), Fraction(1), Fraction(1)],
        ])
        self.assertEqual(basis, [[Fraction(-1), Fraction(-1), Fraction(1)]])

    def test_synthetic_k4_contract(self) -> None:
        document = {
            "schema_version": 1,
            "name": "synthetic k=4 contract",
            "layers": [
                {"label": "layer 1", "operator": [[0, 1]], "gauge_vectors": [[1, 0]], "rechart_vectors": []},
                {"label": "layer 2", "operator": [[0, 0, 1]], "gauge_vectors": [[1, 0, 0], [0, 1, 0]], "rechart_vectors": []},
                {"label": "layer 3", "operator": [[1, 0]], "gauge_vectors": [[0, 1]], "rechart_vectors": []},
                {"label": "layer 4", "operator": [[0, 1]], "gauge_vectors": [], "rechart_vectors": [[1, 0]], "support_transport": {"k": 4, "monomials": [[2, 2]]}},
            ],
        }
        result = analyze_document(document)
        self.assertTrue(result["all_kernel_directions_explained"])
        self.assertEqual([layer["kernel_dimension"] for layer in result["layers"]], [1, 2, 1, 1])
        layer_four = result["layers"][3]
        self.assertEqual(layer_four["gauge_dimension"], 0)
        self.assertEqual(layer_four["rechart_increment"], 1)
        self.assertEqual(layer_four["unexplained_dimension"], 0)

    def test_reference_output_is_current(self) -> None:
        root = Path(__file__).resolve().parent
        document = json.loads((root / "synthetic_k4_contract.json").read_text())
        expected = json.loads((root / "synthetic_k4_output.json").read_text())
        self.assertEqual(analyze_document(document), expected)

    def test_rejects_non_kernel_rechart(self) -> None:
        document = {"schema_version": 1, "layers": [{"label": "bad", "operator": [[1, 0]], "gauge_vectors": [], "rechart_vectors": [[1, 0]]}]}
        with self.assertRaisesRegex(ValueError, "not in ker"):
            analyze_document(document)


class SupportTransportTests(unittest.TestCase):
    def test_k4_binomial_closure(self) -> None:
        self.assertEqual(transport_support(4, [[2, 2]]), [[2, 2], [-2, 1], [-6, 0]])

    def test_union_and_deduplication(self) -> None:
        self.assertEqual(transport_support(1, [[0, 1], [-1, 0]]), [[0, 1], [-1, 0]])


if __name__ == "__main__":
    unittest.main()
