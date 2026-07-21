#!/usr/bin/env python3
"""Validate the chronological contribution and claim records."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTRIBUTION_ID = re.compile(r"JCG-C-(\d{4})$")
CLAIM_ID = re.compile(r"JCG-CLAIM-(\d{4})$")

CONTRIBUTION_FIELDS = {
    "schema_version",
    "id",
    "sequence",
    "title",
    "origin",
    "source_date",
    "recorded_on",
    "lifecycle",
    "publication_state",
    "contributors",
    "artifacts",
    "addresses_claims",
    "guide_relation",
    "attribution_note",
    "ai_assistance",
}

CLAIM_FIELDS = {
    "schema_version",
    "id",
    "statement",
    "posture",
    "introduced_by",
    "dependencies",
    "claimed_implications",
    "does_not_establish",
    "evidence_present",
    "assessment_actions",
    "publication_state",
    "dispute_state",
    "guide_relation",
    "as_of",
    "last_assessed",
}


def read_yaml(path: Path, failures: list[str]) -> dict:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # PyYAML supplies the useful location details.
        failures.append(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
        return {}
    if not isinstance(data, dict):
        failures.append(f"{path.relative_to(ROOT)}: top level must be a mapping")
        return {}
    return data


def require_fields(
    path: Path, data: dict, required: set[str], failures: list[str]
) -> None:
    missing = sorted(required - data.keys())
    if missing:
        failures.append(
            f"{path.relative_to(ROOT)}: missing required fields {', '.join(missing)}"
        )


def main() -> int:
    failures: list[str] = []
    contributions: dict[str, dict] = {}
    contribution_paths: dict[str, Path] = {}

    for path in sorted((ROOT / "contributions").glob("JCG-C-*/metadata.yml")):
        data = read_yaml(path, failures)
        require_fields(path, data, CONTRIBUTION_FIELDS, failures)
        record_id = data.get("id")
        if not isinstance(record_id, str) or not CONTRIBUTION_ID.fullmatch(record_id):
            failures.append(f"{path.relative_to(ROOT)}: invalid contribution id")
            continue
        if path.parent.name != record_id:
            failures.append(f"{path.relative_to(ROOT)}: id does not match directory")
        if record_id in contributions:
            failures.append(f"duplicate contribution id {record_id}")
        contributions[record_id] = data
        contribution_paths[record_id] = path

    ordered = sorted(
        contributions.values(), key=lambda item: item.get("sequence", 10**9)
    )
    sequences = [item.get("sequence") for item in ordered]
    if sequences != list(range(1, len(sequences) + 1)):
        failures.append(
            f"contribution sequences must be consecutive from 1; found {sequences}"
        )
    for item in ordered:
        match = CONTRIBUTION_ID.fullmatch(item["id"])
        if match and item.get("sequence") != int(match.group(1)):
            failures.append(f"{item['id']}: sequence does not match id")

    claims: dict[str, dict] = {}
    claim_paths: dict[str, Path] = {}
    for path in sorted((ROOT / "claims").glob("JCG-CLAIM-*.yml")):
        data = read_yaml(path, failures)
        require_fields(path, data, CLAIM_FIELDS, failures)
        record_id = data.get("id")
        if not isinstance(record_id, str) or not CLAIM_ID.fullmatch(record_id):
            failures.append(f"{path.relative_to(ROOT)}: invalid claim id")
            continue
        if path.stem != record_id:
            failures.append(f"{path.relative_to(ROOT)}: id does not match filename")
        if record_id in claims:
            failures.append(f"duplicate claim id {record_id}")
        claims[record_id] = data
        claim_paths[record_id] = path

    claim_numbers = sorted(int(CLAIM_ID.fullmatch(key).group(1)) for key in claims)
    if claim_numbers != list(range(1, len(claim_numbers) + 1)):
        failures.append(
            f"claim ids must be consecutive from 1; found {claim_numbers}"
        )

    for record_id, data in claims.items():
        path = claim_paths[record_id]
        introduced_by = data.get("introduced_by")
        if introduced_by not in contributions:
            failures.append(
                f"{path.relative_to(ROOT)}: unknown introduced_by {introduced_by!r}"
            )
        elif record_id not in contributions[introduced_by].get("addresses_claims", []):
            failures.append(
                f"{path.relative_to(ROOT)}: introducing contribution does not address claim"
            )
        for dependency in data.get("dependencies", []):
            if dependency not in claims:
                failures.append(
                    f"{path.relative_to(ROOT)}: unknown dependency {dependency!r}"
                )
        list_fields = (
            "dependencies",
            "claimed_implications",
            "does_not_establish",
            "evidence_present",
            "assessment_actions",
        )
        for field in list_fields:
            if not isinstance(data.get(field), list):
                failures.append(f"{path.relative_to(ROOT)}: {field} must be a list")

    for record_id, data in contributions.items():
        path = contribution_paths[record_id]
        for claim_id in data.get("addresses_claims", []):
            if claim_id not in claims:
                failures.append(
                    f"{path.relative_to(ROOT)}: unknown addressed claim {claim_id!r}"
                )

    page_expectations = {
        ROOT / "docs" / "chronology.md": contributions,
        ROOT / "docs" / "claims.md": claims,
    }
    for path, records in page_expectations.items():
        text = path.read_text(encoding="utf-8")
        for record_id in records:
            if record_id not in text:
                failures.append(
                    f"{path.relative_to(ROOT)}: does not expose record {record_id}"
                )

    if failures:
        print("Record validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        f"Validated {len(contributions)} contributions and {len(claims)} claims."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
