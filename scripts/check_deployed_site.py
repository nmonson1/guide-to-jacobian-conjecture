#!/usr/bin/env python3
"""Verify that GitHub Pages serves the selected handoff release."""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import quote, urljoin

from generate_living_guide_v2 import build_release_metadata


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT_LINK_RE = re.compile(
    r"""assets/manuscripts/(?P<filename>[^"'?&#\s]+\.pdf)"""
)


def _fetch(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "jacobian-guide-release-check/1"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        if response.status != 200:
            raise RuntimeError(f"{url}: HTTP {response.status}")
        return response.read()


def _check(base_url: str, expected: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    cache_key = quote(str(expected["site_release_id"]), safe="")
    release_url = urljoin(
        base_url, f"research/handoffs/release.json?release={cache_key}"
    )
    release = json.loads(_fetch(release_url))
    if release != expected:
        failures.append("deployed release.json does not match site-state.json")
    v2 = expected.get("retained_math_v2")
    if v2 is None:
        failures.append("expected release does not name retained-math v2")
    else:
        selection = json.loads(
            _fetch(urljoin(base_url, v2["machine_route"])).decode("utf-8")
        )
        if selection.get("selection_id") != v2["selection_id"]:
            failures.append("deployed retained-math v2 selection disagrees")

    active_manuscripts = {
        item["filename"] for item in expected["manuscripts"]
    }
    for handoff in expected["handoffs"]:
        route = handoff["route"]
        html = _fetch(urljoin(base_url, route)).decode("utf-8")
        if 'class="handoff-snapshot"' not in html:
            failures.append(f"{route}: canonical snapshot is missing")
        if str(expected["site_release_id"]) not in html:
            failures.append(f"{route}: selected release ID is missing")
        linked = set(MANUSCRIPT_LINK_RE.findall(html))
        inactive = linked - active_manuscripts
        if inactive:
            failures.append(
                f"{route}: inactive manuscript link(s): "
                f"{', '.join(sorted(inactive))}"
            )
        if handoff["kind"] == "program" and not linked:
            failures.append(f"{route}: no active manuscript link")
        if (
            "Current proof sources — preferred" not in html
            or "proof-sources/" not in html
        ):
            failures.append(f"{route}: current text-proof link is missing")
        if handoff["program_slug"] == "homogeneous-realization-compression":
            for marker in (
                "Compiler-owned retained result",
                "ARG-RMU5D8E0003-FINITE-PLANE",
                "OBL-P5-FULL-FINITE-ROW-BASE",
                "TSK-P5-FULL-FINITE-ROW-BASE",
                "-1152",
            ):
                if marker not in html:
                    failures.append(f"{route}: retained-math v2 lacks {marker}")
    source_index = _fetch(
        urljoin(base_url, expected["manuscript_sources"]["index_route"])
    ).decode("utf-8")
    if "Current text proof sources" not in source_index:
        failures.append("deployed text-proof source index is missing")
    exact_source = _fetch(
        urljoin(
            base_url,
            "research/proof-sources/01-cubic-incidence/appendices/"
            "cubic-resolvent-defects/",
        )
    ).decode("utf-8")
    if 'id="label-prop-cubic-divisorial-trichotomy"' not in exact_source:
        failures.append("deployed corrected Program 1 proof anchor is missing")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--attempts", type=int, default=12)
    parser.add_argument("--delay-seconds", type=float, default=5)
    args = parser.parse_args()
    if args.attempts < 1:
        parser.error("--attempts must be positive")
    if args.delay_seconds < 0:
        parser.error("--delay-seconds cannot be negative")

    base_url = args.base_url.rstrip("/") + "/"
    expected = build_release_metadata(ROOT)
    last_error = ""
    for attempt in range(1, args.attempts + 1):
        try:
            failures = _check(base_url, expected)
        except (
            json.JSONDecodeError,
            RuntimeError,
            TimeoutError,
            UnicodeDecodeError,
            urllib.error.URLError,
        ) as exc:
            failures = [str(exc)]
        if not failures:
            print(
                "Deployed handoff release verified: "
                f"{expected['site_release_id']} at {base_url}"
            )
            return 0
        last_error = "; ".join(failures)
        if attempt < args.attempts:
            print(
                f"Deployment verification attempt {attempt} failed: {last_error}",
                file=sys.stderr,
            )
            time.sleep(args.delay_seconds)

    print(
        f"Deployed handoff release verification failed: {last_error}",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
