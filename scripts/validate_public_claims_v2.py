#!/usr/bin/env python3
"""Validate the promoted v2 claim export and its internal references."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = ROOT / "data/claims-v2"
FORBIDDEN = {
    "private filesystem path": re.compile(r"/(?:fss|home)/monson/"),
    "ChatGPT share URL": re.compile(r"https?://chatgpt\.com/share/", re.I),
    "private canonical ID": re.compile(r"\bJC-CAN-[0-9]{4,}\b"),
    "internal contribution source ID": re.compile(r"\bSRC-JCG-C-[0-9]{4,}"),
    "private message field": re.compile(r'"(?:message_id|occurrence_id|private_locator|archive_locator)"\s*:'),
    "archived conversation locator": re.compile(r"\bsnapshot [0-9a-f]{12,}", re.I),
    "archived comment index": re.compile(r"\bcomments\.json;\s*comment\b", re.I),
}


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def tree_digest(files: list[tuple[str, bytes]]) -> str:
    digest = hashlib.sha256()
    for relative, content in sorted(files):
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(content)
        digest.update(b"\0")
    return digest.hexdigest()


def schema_errors(schema: dict[str, Any], value: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{list(error.path)}: {error.message}"
        for error in sorted(validator.iter_errors(value), key=lambda item: list(item.path))
    ]


def main() -> int:
    failures: list[str] = []
    manifest = json.loads((DATA_ROOT / "manifest.json").read_text(encoding="utf-8"))
    claim_schema = json.loads((ROOT / "schemas/public-claim-v2.schema.json").read_text(encoding="utf-8"))
    export_schema = json.loads((ROOT / "schemas/public-export-v2.schema.json").read_text(encoding="utf-8"))
    failures.extend(f"manifest: {item}" for item in schema_errors(export_schema, manifest))

    records: dict[str, dict[str, Any]] = {}
    digest_inputs: list[tuple[str, bytes]] = []
    for entry in manifest.get("files", []):
        path = DATA_ROOT / entry["path"]
        if not path.is_file():
            failures.append(f"missing manifest file: {path.relative_to(ROOT)}")
            continue
        content = path.read_bytes()
        digest_inputs.append((entry["path"], content))
        if digest_bytes(content) != entry["sha256"]:
            failures.append(f"digest mismatch: {path.relative_to(ROOT)}")
        text = content.decode("utf-8")
        for label, pattern in FORBIDDEN.items():
            if pattern.search(text):
                failures.append(f"{path.relative_to(ROOT)}: {label}")
        try:
            record = json.loads(text)
        except json.JSONDecodeError as exc:
            failures.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        public_id = record.get("id")
        if public_id in records:
            failures.append(f"duplicate public claim ID: {public_id}")
        records[public_id] = record
        failures.extend(
            f"{path.relative_to(ROOT)}: {item}" for item in schema_errors(claim_schema, record)
        )

    expected_digest = f"sha256:{tree_digest(digest_inputs)}"
    if manifest.get("content_digest") != expected_digest:
        failures.append("manifest content_digest does not match its claim files")
    if manifest.get("counts", {}).get("total") != len(records):
        failures.append("manifest total does not match loaded claim count")

    role_counts = Counter(record.get("role") for record in records.values())
    assessment_counts = Counter(record.get("assessment", {}).get("state") for record in records.values())
    if manifest.get("counts", {}).get("by_role") != {
        key: role_counts.get(key, 0) for key in ("goal", "standalone", "supporting")
    }:
        failures.append("manifest role counts do not match the claim files")
    if manifest.get("counts", {}).get("by_assessment") != {
        key: assessment_counts.get(key, 0)
        for key in ("open", "proof_offered", "verified", "disproved")
    }:
        failures.append("manifest assessment counts do not match the claim files")

    slugs: set[str] = set()
    for public_id, record in records.items():
        if record["slug"] in slugs:
            failures.append(f"duplicate slug: {record['slug']}")
        slugs.add(record["slug"])
        sources = {item["id"] for item in record["sources"]}
        evidence = {item["id"] for item in record["evidence"]}
        checks = {item["id"] for item in record["verification"]}
        if sum(item["primary_for_display"] for item in record["sources"]) != 1:
            failures.append(f"{public_id}: expected exactly one primary source")
        for credit in record["credited_to"]:
            if credit["basis_source_id"] not in sources:
                failures.append(f"{public_id}: credit refers to an unknown source")
            if credit["entity"]["name"] == "Nathaniel Monson":
                failures.append(f"{public_id}: unexpected Nathaniel Monson claim credit")
        for item in record["evidence"]:
            if not set(item["source_ids"]) <= sources:
                failures.append(f"{public_id}: evidence refers to an unknown source")
            if not set(item["uses_claim_ids"]) <= records.keys():
                failures.append(f"{public_id}: evidence refers to an unknown claim")
        for check in record["verification"]:
            if not set(check["source_ids"]) <= sources:
                failures.append(f"{public_id}: check refers to an unknown source")
            if not set(check["evidence_ids"]) <= evidence:
                failures.append(f"{public_id}: check refers to unknown evidence")
        assessment = record["assessment"]
        if not set(assessment["basis_evidence_ids"]) <= evidence:
            failures.append(f"{public_id}: assessment refers to unknown evidence")
        if not set(assessment["basis_verification_ids"]) <= checks:
            failures.append(f"{public_id}: assessment refers to an unknown check")
        parent = record.get("parent_claim_id")
        if parent and parent not in records:
            failures.append(f"{public_id}: parent claim was not exported")

    actual_claim_files = set((DATA_ROOT / "claims").glob("*.json"))
    manifest_claim_files = {DATA_ROOT / entry["path"] for entry in manifest.get("files", [])}
    for path in sorted(actual_claim_files - manifest_claim_files):
        failures.append(f"unmanifested claim file: {path.relative_to(ROOT)}")

    if failures:
        print("Public claim validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(
        f"Validated {len(records)} public v2 claims; {manifest['content_digest']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
