from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "degree21_exact_data.json"
PROVENANCE = HERE / "fixtures" / "degree21_fixture_provenance.json"


class Degree21FixtureTests(unittest.TestCase):
    def test_fixture_matches_pinned_archive_member(self) -> None:
        provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
        payload = FIXTURE.read_bytes()
        self.assertEqual(len(payload), provenance["member"]["bytes"])
        self.assertEqual(
            hashlib.sha256(payload).hexdigest(),
            provenance["member"]["sha256"],
        )

    def test_fixture_has_both_twelve_layer_complexes(self) -> None:
        document = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            [layer["r"] for layer in document["truncated"]["layers"]],
            list(range(1, 13)),
        )
        self.assertEqual(
            [layer["r"] for layer in document["full"]["layers"]],
            list(range(1, 13)),
        )


if __name__ == "__main__":
    unittest.main()
