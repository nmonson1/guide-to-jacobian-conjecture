from __future__ import annotations

import unittest

from scripts.check_public_site_v2 import _sensitive


class PublicationBoundaryTests(unittest.TestCase):
    def test_public_https_locator_may_contain_uuid(self) -> None:
        failures: list[str] = []
        _sensitive(
            "[Source](https://example.org/bitstreams/"
            "9ef8e868-5526-4830-b19f-543c0af09e7c/content)",
            "citation",
            failures,
        )
        self.assertEqual(failures, [])

    def test_bare_uuid_remains_forbidden(self) -> None:
        failures: list[str] = []
        _sensitive(
            "private object 9ef8e868-5526-4830-b19f-543c0af09e7c",
            "prose",
            failures,
        )
        self.assertEqual(failures, ["prose: forbidden UUID"])


if __name__ == "__main__":
    unittest.main()
