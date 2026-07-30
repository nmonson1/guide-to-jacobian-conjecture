from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"
PROVENANCE = FIXTURES / "belyi_field_fixture_provenance.json"


class BelyiFieldFixtureTests(unittest.TestCase):
    def test_every_pinned_member_matches_its_archive_hash(self) -> None:
        provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
        for member in provenance["members"]:
            path = HERE / member["fixture_path"]
            payload = path.read_bytes()
            self.assertEqual(len(payload), member["bytes"], path.name)
            self.assertEqual(
                hashlib.sha256(payload).hexdigest(),
                member["sha256"],
                path.name,
            )

    def test_small_primitive_element_has_degree_five(self) -> None:
        relations = json.loads(
            (FIXTURES / "belyi_exact_field_relations.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            relations["minimal_polynomial"],
            "x^5 - x^4 + 3*x^3 + 3*x^2 + 26",
        )
        self.assertEqual(sorted(relations["relations"]), ["2", "3", "4", "5", "6", "7"])


if __name__ == "__main__":
    unittest.main()
