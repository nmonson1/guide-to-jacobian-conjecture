#!/usr/bin/env python3
"""Generate the featured story index and one reader page per story."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


def load(root: Path) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    story_root = root / "data/stories-v1"
    story_manifest = json.loads(
        (story_root / "manifest.json").read_text(encoding="utf-8")
    )
    stories: dict[str, dict[str, Any]] = {}
    for entry in story_manifest["stories"]:
        path = story_root / entry["file"]
        content = path.read_bytes()
        if hashlib.sha256(content).hexdigest() != entry["sha256"]:
            raise ValueError(f"digest mismatch for {path.relative_to(root)}")
        story = json.loads(content)
        stories[story["slug"]] = story

    package_root = root / "data/packages-v1.2"
    package_manifest = json.loads(
        (package_root / "manifest.json").read_text(encoding="utf-8")
    )
    packages: dict[str, dict[str, Any]] = {}
    for entry in package_manifest["packages"]:
        path = package_root / entry["file"]
        package = json.loads(path.read_text(encoding="utf-8"))
        packages[package["slug"]] = package
    return stories, packages


def render_index(stories: dict[str, dict[str, Any]]) -> str:
    lines = [
        "---",
        "title: Mathematical stories",
        "description: Six reader-facing routes through the Jacobian conjecture, its counterexample, and the questions that follow.",
        "---",
        "",
        "# Mathematical stories",
        "",
        "The guide is organized around six questions a reader might naturally ask. "
        "Each story collects externally sourced results and open problems. "
        "Precise claim records remain available deeper in the site for readers "
        "who want sources, evidence, and exact scope.",
        "",
    ]
    for story in stories.values():
        lines.extend(
            [
                f"## [{story['title']}](story-v1/{story['slug']}.md)",
                "",
                story["summary"],
                "",
            ]
        )
    return "\n".join(lines)


def render_page(
    story: dict[str, Any],
    stories: dict[str, dict[str, Any]],
    packages: dict[str, dict[str, Any]],
) -> str:
    lines = [
        "---",
        f"title: {json.dumps(story['title'], ensure_ascii=False)}",
        f"description: {json.dumps(story['summary'], ensure_ascii=False)}",
        "---",
        "",
        f"# {story['title']}",
        "",
        story["summary"],
        "",
        "## Results and open questions",
        "",
    ]
    for slug in story["package_slugs"]:
        package = packages[slug]
        label = "Result" if package["kind"] == "result" else "Open problem"
        count = len(package["members"])
        noun = "technical record" if count == 1 else "technical records"
        lines.extend(
            [
                f"### [{package['title']}](../topic-v1.2/{slug}.md)",
                "",
                package["statement"],
                "",
                f"*{label} · {count} source-linked {noun}.*",
                "",
            ]
        )
    if story["related_story_slugs"]:
        lines.extend(["## Continue reading", ""])
        for slug in story["related_story_slugs"]:
            related = stories[slug]
            lines.append(f"- [{related['title']}]({slug}.md)")
        lines.append("")
    lines.extend(
        [
            "## About the deeper records",
            "",
            "The linked result pages lead to precise statements, sources, credit, "
            "evidence, and limitations. Those technical records are intentionally "
            "excluded from ordinary navigation and site search.",
            "",
            "[Browse the externally sourced result catalogue](../topics-v1.2.md)",
            "",
            "[Back to the mathematical stories](../stories-v1.md)",
            "",
        ]
    )
    return "\n".join(lines)


def expected_outputs(
    root: Path,
    stories: dict[str, dict[str, Any]],
    packages: dict[str, dict[str, Any]],
) -> dict[Path, str]:
    outputs = {root / "docs/stories-v1.md": render_index(stories)}
    for story in stories.values():
        outputs[
            root / "docs/story-v1" / f"{story['slug']}.md"
        ] = render_page(story, stories, packages)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        stories, packages = load(root)
        outputs = expected_outputs(root, stories, packages)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    if args.write:
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        print(
            f"Generated {len(stories)} featured story pages and the story index."
        )
        return 0

    failures: list[str] = []
    for path, expected in outputs.items():
        if not path.is_file():
            failures.append(f"missing generated file: {path.relative_to(root)}")
        elif path.read_text(encoding="utf-8") != expected:
            failures.append(f"stale generated file: {path.relative_to(root)}")
    expected_pages = {
        path for path in outputs if path.parent == root / "docs/story-v1"
    }
    actual_pages = set((root / "docs/story-v1").glob("*.md"))
    for path in sorted(actual_pages - expected_pages):
        failures.append(f"unexpected generated page: {path.relative_to(root)}")
    if failures:
        print("Generated-story check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Generated-story check passed for {len(stories)} stories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
