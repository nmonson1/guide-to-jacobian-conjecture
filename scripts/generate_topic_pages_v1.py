#!/usr/bin/env python3
"""Generate the topic index and one page per approved mathematical package."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


KIND_LABEL = {
    "result": "Result",
    "open_problem": "Open problem",
}

ROLE_LABEL = {
    "primary_statement": "Primary statement",
    "supporting_result": "Supporting result",
    "supporting_example": "Supporting example",
    "proof_lemma": "Proof ingredient",
    "case": "Case",
    "comparison": "Comparison",
    "historical_statement": "Historical statement",
}


def load(root: Path) -> tuple[dict[str, dict], dict[str, dict]]:
    manifest = json.loads(
        (root / "data/packages-v1/manifest.json").read_text(encoding="utf-8")
    )
    packages = {}
    for entry in manifest["packages"]:
        package = json.loads(
            (root / "data/packages-v1" / entry["file"]).read_text(
                encoding="utf-8"
            )
        )
        packages[package["slug"]] = package

    claim_manifest = json.loads(
        (root / "data/claims-v3/manifest.json").read_text(encoding="utf-8")
    )
    claims = {}
    for entry in claim_manifest["files"]:
        claim = json.loads(
            (root / "data/claims-v3" / entry["path"]).read_text(
                encoding="utf-8"
            )
        )
        claims[claim["id"]] = claim
    return packages, claims


def render_index(packages: dict[str, dict]) -> str:
    lines = [
        "---",
        "title: Guided topics",
        "description: Coherent mathematical entry points assembled from the claim registry.",
        "---",
        "",
        "# Guided topics",
        "",
        "These pages group already published claims into mathematical developments. "
        "A topic page is navigation and exposition: it does not add a claim or "
        "upgrade any claim's review status.",
        "",
        "This first tranche contains only topics whose mathematical components "
        "already have public claim records. More topics will appear as their "
        "component claims are reviewed.",
        "",
    ]
    for kind, heading in (
        ("result", "Results"),
        ("open_problem", "Open problems"),
    ):
        selected = sorted(
            (
                package
                for package in packages.values()
                if package["kind"] == kind
            ),
            key=lambda package: package["title"].casefold(),
        )
        if not selected:
            continue
        lines.extend([f"## {heading}", ""])
        for package in selected:
            count = len(package["members"])
            noun = "claim" if count == 1 else "claims"
            lines.extend(
                [
                    f"### [{package['title']}](topic-v1/{package['slug']}.md)",
                    "",
                    package["statement"],
                    "",
                    f"*{count} linked {noun}.*",
                    "",
                ]
            )
    return "\n".join(lines)


def render_page(
    package: dict,
    packages: dict[str, dict],
    claims: dict[str, dict],
) -> str:
    lines = [
        "---",
        f"title: {json.dumps(package['title'], ensure_ascii=False)}",
        f"description: {json.dumps(package['statement'], ensure_ascii=False)}",
        "---",
        "",
        f"# {package['title']}",
        "",
        package["statement"],
        "",
        f"**Page type:** {KIND_LABEL[package['kind']]}",
        "",
        "## The claims in this development",
        "",
    ]
    for member in package["members"]:
        claim = claims[member["public_claim_id"]]
        role = ROLE_LABEL.get(
            member["role"],
            member["role"].replace("_", " ").title(),
        )
        lines.extend(
            [
                f"### [{claim['title']}](../claim-v3/{claim['slug']}.md)",
                "",
                claim["statement"],
                "",
                f"**Role here:** {role}.  ",
                f"**Claim status:** {claim['assessment']['label']}.",
                "",
            ]
        )
    if package["related_package_slugs"]:
        lines.extend(["## Related topics", ""])
        for slug in package["related_package_slugs"]:
            related = packages[slug]
            lines.append(
                f"- [{related['title']}]({related['slug']}.md)"
            )
        lines.append("")
    lines.extend(
        [
            "## About this page",
            "",
            "This topic page is generated from the public claim registry. "
            "Credit, evidence, limitations, and sources remain attached to "
            "the individual claim pages linked above.",
            "",
            "[Back to guided topics](../topics-v1.md)",
            "",
        ]
    )
    return "\n".join(lines)


def expected_outputs(
    root: Path,
    packages: dict[str, dict],
    claims: dict[str, dict],
) -> dict[Path, str]:
    outputs = {root / "docs/topics-v1.md": render_index(packages)}
    for package in packages.values():
        outputs[
            root / "docs/topic-v1" / f"{package['slug']}.md"
        ] = render_page(package, packages, claims)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="write generated Markdown instead of checking it",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        packages, claims = load(root)
        outputs = expected_outputs(root, packages, claims)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    if args.write:
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        print(
            f"Generated {len(packages)} topic pages and the topic index."
        )
        return 0

    failures = []
    for path, expected in outputs.items():
        if not path.is_file():
            failures.append(
                f"missing generated file: {path.relative_to(root)}"
            )
        elif path.read_text(encoding="utf-8") != expected:
            failures.append(
                f"stale generated file: {path.relative_to(root)}"
            )
    expected_pages = {
        path for path in outputs if path.parent == root / "docs/topic-v1"
    }
    actual_pages = (
        set((root / "docs/topic-v1").glob("*.md"))
        if (root / "docs/topic-v1").is_dir()
        else set()
    )
    for path in sorted(actual_pages - expected_pages):
        failures.append(
            f"unexpected generated page: {path.relative_to(root)}"
        )
    if failures:
        print("Generated-topic check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Generated-topic check passed for {len(packages)} topics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
