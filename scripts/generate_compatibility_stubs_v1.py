#!/usr/bin/env python3
"""Generate noindex compatibility stubs for routes from the earlier guide."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from generate_living_guide_v1 import PUBLIC_DOCS_DIR, load


TOP_LEVEL = {
    "certificate.md": "counterexample.md",
    "chronology-v2.md": "about.md",
    "chronology.md": "about.md",
    "claims-v3.md": "research.md",
    "claims.md": "research.md",
    "contribute.md": "about.md",
    "overview-v2.md": "index.md",
    "stories-v1.md": "research.md",
    "topics-v1.2.md": "research.md",
    "topics-v1.md": "research.md",
}

STORIES = {
    "conjecture-and-counterexample": "counterexample.md",
    "how-the-counterexample-works": "geometry.md",
    "landscape-of-counterexamples": "research.md",
    "neighboring-consequences": "research.md",
    "plane-case": "plane-case.md",
    "simplifying-counterexamples": "research.md",
}

ALIASES = {
    "all-dimensional-image-conjecture-false": "consequences-for-neighboring-conjectures",
    "all-dimensional-vanishing-conjecture-false": "consequences-for-neighboring-conjectures",
    "alpoge-map-constant-jacobian": "base-counterexample-and-immediate-consequences",
    "alpoge-map-triple-collision": "base-counterexample-and-immediate-consequences",
    "binary-cubic-hyperplane-orbits": "double-root-affine-source",
    "counterexample-fiber-stratification": "base-map-fibers-image-and-nonproperness",
    "counterexample-image-and-nonproperness": "base-map-fibers-image-and-nonproperness",
    "counterexample-s3-galois-closure": "base-cover-monodromy-and-deck-group",
    "counterexample-trivial-rational-deck-group": "base-cover-monodromy-and-deck-group",
    "cubic-homogeneous-counterexample-24-variables": "cubic-homogeneous-descendant-construction",
    "degree-three-counterexample-11-variables": "eleven-dimensional-cubic-counterexample",
    "determinant-one-counterexample-every-field": "all-fields-counterexample",
    "dixmier-conjecture-false-dimension-at-least-three": "consequences-for-neighboring-conjectures",
    "double-root-orbit-invariant-triangularization-question": "double-root-orbit-characterization",
    "double-root-resultant-slice-affine-three-space": "double-root-affine-source",
    "exact-finite-field-fiber-counts": "finite-field-fibers",
    "finite-field-s3-fiber-distribution": "finite-field-fibers",
    "gaussian-moments-conjecture-counterexamples": "gaussian-moments-counterexamples",
    "jacobian-conjecture-false-dimension-at-least-three": "base-counterexample-and-immediate-consequences",
    "keller-map-invertibility-properness-equivalence": "keller-invertibility-and-properness",
    "keller-maps-every-generic-degree": "all-generic-degrees-family",
    "kraus-1884-plane-jacobian-conjecture": "kraus-statement-and-proof-gap",
    "kraus-proof-gap-at-infinity": "kraus-statement-and-proof-gap",
    "plane-jacobian-conjecture-open": "plane-jacobian-conjecture",
    "the-jacobian-conjecture": "original-jacobian-conjecture",
    "vitushkin-rational-example-comparison": "vitushkin-rational-comparison",
    "atomic-jc-can-0025": "double-root-orbit-characterization",
}


def _stub(relative: Path, target: str, title: str) -> str:
    target_from_stub = os.path.relpath(target, relative.parent).replace(os.sep, "/")
    return "\n".join(
        [
            "---",
            f'title: "{title}"',
            "robots: noindex, nofollow",
            "search:",
            "  exclude: true",
            "---",
            "",
            "# This page has moved",
            "",
            "This compatibility page preserves an address from an earlier "
            "working draft.",
            "",
            f"[Continue to the current page]({target_from_stub})"
            "{ .md-button .md-button--primary }",
            "",
        ]
    )


def expected(root: Path) -> dict[Path, str]:
    _, pages, _, _, _, _ = load(root)
    docs = root / PUBLIC_DOCS_DIR
    old_docs = root / "docs"
    outputs: dict[Path, str] = {}
    for name, target in TOP_LEVEL.items():
        relative = Path(name)
        outputs[docs / relative] = _stub(
            relative, target, "Earlier Guide Page"
        )
    for slug, target in STORIES.items():
        relative = Path("story-v1") / f"{slug}.md"
        outputs[docs / relative] = _stub(
            relative, target, "Earlier Reading Path"
        )
    for directory in ("claim", "claim-v3", "topic-v1", "topic-v1.2"):
        for old_path in sorted((old_docs / directory).glob("*.md")):
            slug = old_path.stem
            result_slug = ALIASES.get(slug, slug)
            if result_slug in pages:
                target = f"results/{result_slug}.md"
            else:
                target = "research.md"
            relative = Path(directory) / old_path.name
            outputs[docs / relative] = _stub(
                relative, target, "Earlier Technical Route"
            )
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
    outputs = expected(root)
    failures: list[str] = []
    for path, content in sorted(outputs.items()):
        if args.write:
            if path.exists():
                failures.append(f"refusing to overwrite {path.relative_to(root)}")
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        elif not path.is_file():
            failures.append(f"missing compatibility page: {path.relative_to(root)}")
        elif path.read_text(encoding="utf-8") != content:
            failures.append(f"stale compatibility page: {path.relative_to(root)}")
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    action = "Generated" if args.write else "Checked"
    print(f"{action} {len(outputs)} compatibility pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
