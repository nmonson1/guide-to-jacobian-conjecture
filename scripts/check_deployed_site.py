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
FULL_ROW_OBLIGATION_ID = "OBL-P5-FULL-FINITE-ROW-BASE"
FULL_ROW_TASK_ID = "TSK-L6-FULL-ROW-BASE-V3"
LANE6_INTERFACE_MARKERS = (
    "TSK-L6-L9-OBSTRUCTION-GROUPOID-SCHEMA-V3",
    "chain-homotopy",
    "fail-closed obstruction-groupoid interface",
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


def _release_url(base_url: str, route: str, cache_key: str) -> str:
    url = urljoin(base_url, route)
    separator = "&" if "?" in url else "?"
    return f"{url}{separator}release={cache_key}"


def _load_retained_v2(
    base_url: str, metadata: dict[str, Any], cache_key: str
) -> tuple[dict[str, Any], list[str]]:
    failures: list[str] = []
    if machine_route := metadata.get("machine_route"):
        payload = json.loads(
            _fetch(_release_url(base_url, machine_route, cache_key)).decode("utf-8")
        )
        if payload.get("selection_id") != metadata.get("selection_id"):
            failures.append("deployed retained-math v2 selection disagrees")
        return payload, failures

    machine_routes = metadata.get("machine_routes", {})
    graph_route = machine_routes.get("graph")
    if not graph_route:
        return {}, ["expected retained-math v2 metadata lacks a graph route"]
    payload = json.loads(
        _fetch(_release_url(base_url, graph_route, cache_key)).decode("utf-8")
    )
    if payload.get("registry_id") != metadata.get("source_registry_id"):
        failures.append("deployed retained-math v2 registry disagrees")
    if payload.get("counts") != metadata.get("counts"):
        failures.append("deployed retained-math v2 counts disagree")
    return payload, failures


def _check(base_url: str, expected: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    cache_key = quote(str(expected["site_release_id"]), safe="")
    release_url = _release_url(
        base_url, "research/handoffs/release.json", cache_key
    )
    release = json.loads(_fetch(release_url))
    if release != expected:
        failures.append("deployed release.json does not match site-state.json")
    v2 = expected.get("retained_math_v2")
    if v2 is None:
        failures.append("expected release does not name retained-math v2")
    else:
        selection, retained_failures = _load_retained_v2(base_url, v2, cache_key)
        failures.extend(retained_failures)
        obligation_ids = {
            item.get("obligation_id") for item in selection.get("obligations", [])
        }
        task_ids = {item.get("task_id") for item in selection.get("tasks", [])}
        if FULL_ROW_OBLIGATION_ID not in obligation_ids:
            failures.append("deployed retained-math v2 lacks the full-row obligation")
        if FULL_ROW_TASK_ID not in task_ids:
            failures.append("deployed retained-math v2 lacks the current Lane 6 full-row task")

    active_manuscripts = {
        item["filename"] for item in expected["manuscripts"]
    }
    for handoff in expected["handoffs"]:
        route = handoff["route"]
        html = _fetch(_release_url(base_url, route, cache_key)).decode("utf-8")
        if (
            'class="handoff-snapshot"' in html
            or str(expected["site_release_id"]) in html
        ):
            failures.append(f"{route}: obsolete release plumbing remains")
        title_position = html.find("<h1")
        identity_position = html.find('class="claim-tag"')
        if title_position < 0 or identity_position < title_position:
            failures.append(f"{route}: page does not lead with its title")
        linked = set(MANUSCRIPT_LINK_RE.findall(html))
        inactive = linked - active_manuscripts
        if inactive:
            failures.append(
                f"{route}: inactive manuscript link(s): "
                f"{', '.join(sorted(inactive))}"
            )
        if handoff["kind"] == "program":
            graph_marker = f"Open the current {handoff['title']} graph view"
            if graph_marker not in html:
                failures.append(f"{route}: no current mathematical graph view")
        for marker in (
            "Sources and release",
            "Current proof sources",
            "Machine-readable release metadata",
            "proof-sources/",
            "release.json",
        ):
            if marker not in html:
                failures.append(f"{route}: handoff footer lacks {marker!r}")
        if handoff["program_slug"] == "homogeneous-realization-compression":
            for marker in LANE6_INTERFACE_MARKERS:
                if marker not in html:
                    failures.append(f"{route}: current Lane 6 task lacks {marker}")
    source_index = _fetch(
        _release_url(
            base_url, expected["manuscript_sources"]["index_route"], cache_key
        )
    ).decode("utf-8")
    if "Current text proof sources" not in source_index:
        failures.append("deployed text-proof source index is missing")
    exact_source = _fetch(
        _release_url(
            base_url,
            "research/proof-sources/01-cubic-incidence/appendices/"
            "cubic-resolvent-defects/",
            cache_key,
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
