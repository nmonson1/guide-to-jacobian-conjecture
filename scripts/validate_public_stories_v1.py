#!/usr/bin/env python3
"""Validate featured public stories and their package references."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
STORY_ROOT = ROOT / "data/stories-v1"
PACKAGE_ROOT = ROOT / "data/packages-v1.2"
FORBIDDEN = {
    "private filesystem path": re.compile(r"/(?:fss|home)/monson/"),
    "private canonical ID": re.compile(r"\bJC-CAN-[0-9]{4,}\b"),
    "public atomic claim ID": re.compile(r"\bJCG-CLAIM-[0-9]{4,}\b"),
    "ChatGPT share URL": re.compile(r"https?://chatgpt\.com/share/", re.I),
}


def schema_errors(schema: dict[str, Any], value: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    return [
        f"{list(error.path)}: {error.message}"
        for error in sorted(
            validator.iter_errors(value),
            key=lambda item: list(item.path),
        )
    ]


def main() -> int:
    failures: list[str] = []
    manifest = json.loads(
        (STORY_ROOT / "manifest.json").read_text(encoding="utf-8")
    )
    schema = json.loads(
        (ROOT / "schemas/public-story-v1.schema.json").read_text(
            encoding="utf-8"
        )
    )
    package_manifest = json.loads(
        (PACKAGE_ROOT / "manifest.json").read_text(encoding="utf-8")
    )
    package_slugs = {
        item["slug"] for item in package_manifest["packages"]
    }

    stories: dict[str, dict[str, Any]] = {}
    expected_files: set[Path] = set()
    for entry in manifest.get("stories", []):
        path = STORY_ROOT / entry["file"]
        expected_files.add(path)
        if not path.is_file():
            failures.append(f"missing story file: {path.relative_to(ROOT)}")
            continue
        content = path.read_bytes()
        if hashlib.sha256(content).hexdigest() != entry["sha256"]:
            failures.append(f"digest mismatch: {path.relative_to(ROOT)}")
        text = content.decode("utf-8")
        for label, pattern in FORBIDDEN.items():
            if pattern.search(text):
                failures.append(f"{path.relative_to(ROOT)}: {label}")
        try:
            story = json.loads(text)
        except json.JSONDecodeError as exc:
            failures.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        failures.extend(
            f"{path.relative_to(ROOT)}: {error}"
            for error in schema_errors(schema, story)
        )
        if entry["id"] != story.get("id"):
            failures.append(f"{path.relative_to(ROOT)}: manifest ID mismatch")
        if entry["slug"] != story.get("slug"):
            failures.append(f"{path.relative_to(ROOT)}: manifest slug mismatch")
        if story.get("id") in stories:
            failures.append(f"duplicate story ID: {story.get('id')}")
        stories[story["id"]] = story
        unknown_packages = sorted(
            set(story["package_slugs"]) - package_slugs
        )
        if unknown_packages:
            failures.append(
                f"{story['id']}: unknown packages {unknown_packages}"
            )

    if manifest.get("story_count") != len(stories):
        failures.append("manifest story_count does not match loaded stories")
    actual_files = set((STORY_ROOT / "stories").glob("*.json"))
    for path in sorted(actual_files - expected_files):
        failures.append(f"unmanifested story file: {path.relative_to(ROOT)}")
    for story in stories.values():
        unknown_related = sorted(
            set(story["related_story_slugs"]) - stories.keys()
        )
        if unknown_related:
            failures.append(
                f"{story['id']}: unknown related stories {unknown_related}"
            )

    if failures:
        print("Public story validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(
        f"Validated {len(stories)} featured stories; all references are public."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
