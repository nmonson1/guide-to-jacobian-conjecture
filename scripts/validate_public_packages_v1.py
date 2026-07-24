#!/usr/bin/env python3
"""Validate the public topic-package export and all cross-references."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = {
    "private filesystem path": re.compile(r"/(?:fss|home)/monson/"),
    "ChatGPT share URL": re.compile(r"https?://chatgpt\.com/share/", re.I),
    "private canonical ID": re.compile(r"\bJC-CAN-[0-9]{4,}\b"),
    "internal contribution source ID": re.compile(r"\bSRC-JCG-C-[0-9]{4,}"),
}


def schema_errors(schema: dict, value: dict) -> list[str]:
    validator = Draft202012Validator(schema)
    return [
        f"{list(error.path)}: {error.message}"
        for error in sorted(
            validator.iter_errors(value),
            key=lambda item: list(item.path),
        )
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--package-version",
        default="v1",
        help="version suffix under data/packages-* (default: v1)",
    )
    args = parser.parse_args()
    data_root = ROOT / f"data/packages-{args.package_version}"

    failures: list[str] = []
    manifest = json.loads(
        (data_root / "manifest.json").read_text(encoding="utf-8")
    )
    schema = json.loads(
        (ROOT / "schemas/public-package-v1.schema.json").read_text(
            encoding="utf-8"
        )
    )
    claim_manifest = json.loads(
        (ROOT / "data/claims-v3/manifest.json").read_text(encoding="utf-8")
    )
    public_claim_ids = {
        Path(entry["path"]).stem for entry in claim_manifest["files"]
    }

    packages: dict[str, dict] = {}
    for entry in manifest.get("packages", []):
        path = data_root / entry["file"]
        if not path.is_file():
            failures.append(f"missing package file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in FORBIDDEN.items():
            if pattern.search(text):
                failures.append(f"{path.relative_to(ROOT)}: {label}")
        try:
            package = json.loads(text)
        except json.JSONDecodeError as exc:
            failures.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        failures.extend(
            f"{path.relative_to(ROOT)}: {error}"
            for error in schema_errors(schema, package)
        )
        slug = package.get("slug")
        if slug in packages:
            failures.append(f"duplicate package slug: {slug}")
        packages[slug] = package
        if entry.get("slug") != slug:
            failures.append(f"{path.relative_to(ROOT)}: manifest slug mismatch")
        if entry.get("id") != package.get("id"):
            failures.append(f"{path.relative_to(ROOT)}: manifest ID mismatch")
        if entry.get("kind") != package.get("kind"):
            failures.append(f"{path.relative_to(ROOT)}: manifest kind mismatch")
        if entry.get("member_count") != len(package.get("members", [])):
            failures.append(
                f"{path.relative_to(ROOT)}: manifest member count mismatch"
            )

    if manifest.get("package_count") != len(packages):
        failures.append("manifest package_count does not match loaded files")
    expected_files = {
        data_root / entry["file"] for entry in manifest.get("packages", [])
    }
    actual_files = set((data_root / "packages").glob("*.json"))
    for path in sorted(actual_files - expected_files):
        failures.append(f"unmanifested package file: {path.relative_to(ROOT)}")

    kind_counts = Counter()
    for slug, package in packages.items():
        kind_counts[package["kind"]] += 1
        member_ids = [
            member["public_claim_id"] for member in package["members"]
        ]
        if len(member_ids) != len(set(member_ids)):
            failures.append(f"{slug}: duplicate member claim")
        if package["lead_public_claim_id"] not in member_ids:
            failures.append(f"{slug}: lead is not a member")
        unknown_claims = sorted(set(member_ids) - public_claim_ids)
        if unknown_claims:
            failures.append(
                f"{slug}: unknown public claims {', '.join(unknown_claims)}"
            )
        for member in package["members"]:
            claim_path = (
                ROOT
                / "data/claims-v3/claims"
                / f"{member['public_claim_id']}.json"
            )
            if not claim_path.is_file():
                continue
            claim = json.loads(claim_path.read_text(encoding="utf-8"))
            if member["title"] != claim["title"]:
                failures.append(
                    f"{slug}/{member['public_claim_id']}: title drift"
                )
            if member["statement"] != claim["statement"]:
                failures.append(
                    f"{slug}/{member['public_claim_id']}: statement drift"
                )
        unknown_topics = sorted(
            set(package["related_package_slugs"]) - packages.keys()
        )
        if unknown_topics:
            failures.append(
                f"{slug}: unknown related topics {', '.join(unknown_topics)}"
            )

    if failures:
        print("Public topic validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    counts = ", ".join(
        f"{kind_counts[key]} {key.replace('_', ' ')}"
        for key in ("result", "open_problem")
    )
    print(
        f"Validated {len(packages)} public topics "
        f"in packages-{args.package_version} ({counts})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
