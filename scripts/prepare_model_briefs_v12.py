#!/usr/bin/env python3
"""Prepare a write-once sanitized model-brief release from private handoffs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_BASE = "https://nmonson1.github.io/guide-to-jacobian-conjecture/"
MANUSCRIPT_LINK_RE = re.compile(
    r"(?P<prefix>\.\./\.\./assets/manuscripts/)"
    r"(?P<sequence>0[1-7])-[^)\s]+\.pdf"
)
FRESHNESS_RE = re.compile(r"^\*\*Freshness:\*\*.*\n\n", re.MULTILINE)

SOURCE_MAP = {
    "state-of-the-program": "state-of-the-program.md",
    "cubic-marked-root-incidence-geometry": (
        "cubic-marked-root-incidence-geometry.md"
    ),
    "minimum-degree-and-quartic-exclusions": "02-low-degree.md",
    "local-rigidity-and-deformation-algebra": (
        "local-rigidity-and-deformation-algebra.md"
    ),
    "stable-moduli": "stable-moduli.md",
    "homogeneous-descendants": "homogeneous-descendants.md",
    "plane-boundary-obstructions": "plane-boundary-obstructions.md",
}

PUBLIC_REPLACEMENTS = (
    ("linked v12 paper statement", "linked paper statement"),
    ("linked v12 statement", "linked statement"),
    (
        "The claim graph organizes 354 public atomic statements into 94 grouped",
        "The claim graph organizes 368 public atomic statements into 104 grouped",
    ),
    (
        "the foundational sheaf argument has no independent specialist review",
        "the foundational sheaf argument still needs specialist verification",
    ),
    (
        "Chern-character proof still needs independent specialist review",
        "Chern-character proof still needs specialist verification",
    ),
    ("**(F1) Global case-tree and proof-to-code audit.** Last audited:",
     "**(F1) Global case-tree and proof-to-code audit.** Evidence checkpoint:"),
    (
        "and the result carries an independent review receipt with any\n"
        "remaining gaps explicit.",
        "and its assumptions, edge cases, and remaining gaps are independently\n"
        "checked and explicit.",
    ),
)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _validate_public(text: str) -> str:
    forbidden = (
        "/fss/",
        "/home/",
        "chatgpt.com/share",
        "INTAKE-",
        "review status",
        "audit status",
        "last audited",
        "independent review",
        "independent specialist review",
    )
    lowered = text.casefold()
    found = [marker for marker in forbidden if marker.casefold() in lowered]
    if found:
        raise ValueError(f"public brief retains forbidden markers: {found}")
    if "assets/manuscripts/" in text:
        literal = re.search(r"assets/manuscripts/[^)\s]+\.pdf", text)
        if literal:
            raise ValueError(
                f"literal manuscript filename remains: {literal.group(0)}"
            )
    return text


def _publicize(text: str, *, cross_program: bool) -> str:
    text, count = FRESHNESS_RE.subn("", text, count=1)
    if count != 1:
        raise ValueError("source brief has no single freshness header")
    text = text.replace(PUBLIC_BASE, "../../")
    text = MANUSCRIPT_LINK_RE.sub(
        lambda match: (
            f"{match.group('prefix')}{{{{MANUSCRIPT_"
            f"{match.group('sequence')}}}}}"
        ),
        text,
    )
    if not cross_program:
        text = text.replace(
            "## 3. What is proved",
            "## 3. Reusable inputs, exact scope, and proof access",
            1,
        )
    for old, new in PUBLIC_REPLACEMENTS:
        text = text.replace(old, new)
    return _validate_public(text)


def _replace_once(text: str, old: str, new: str, *, label: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"{label}: expected exactly one source block")
    return text.replace(old, new, 1)


def _update_program_2(text: str) -> str:
    text = _replace_once(
        text,
        """**Research state:** mathematical checkpoint 30 July 2026. Every previously
listed degree-three normal-form calculation now has an exact successful
replay. The remaining gate is the global case-tree and independent
proof-to-code audit; the quartic synthesis is still conditional.""",
        """**Research state:** mathematical checkpoint 30 July 2026. Every previously
listed degree-three normal-form calculation now has an exact successful
replay. A fresh paper audit and scoped degree-five/six packet sharpen the
boundaries below. The global case-tree remains open and the quartic synthesis
is still conditional.""",
        label="Program 2 research state",
    )
    text = _replace_once(
        text,
        """| 2 | No quartic Keller map in three variables has a nondegenerate conic as its projective leading image. The conclusion uses all seven quadratic-factor orbits: four invariant-field orbits and three separate later orbit arguments; the four-orbit theorem alone is insufficient. | [`JCG-24A6190A`](../../claims/JCG-24A6190A.md), [`JCG-80F5587E`](../../claims/JCG-80F5587E.md), [`JCG-244F8A2E`](../../claims/JCG-244F8A2E.md) · [proof and exact terminal calculation](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=10) |""",
        """| 2 | The claim graph packages a nondegenerate-conic exclusion using all seven quadratic-factor orbits: four invariant-field orbits and three separate later arguments. The 30 July paper audit found direct support for the four original orbits but not complete proof access for the other three, so retain the full claim package while treating the seven-orbit synthesis as a proof-access gap. | [`JCG-24A6190A`](../../claims/JCG-24A6190A.md), [`JCG-80F5587E`](../../claims/JCG-80F5587E.md), [`JCG-244F8A2E`](../../claims/JCG-244F8A2E.md) · [four-orbit proof and exact terminal calculation](../../assets/manuscripts/{{MANUSCRIPT_02}}#page=10) |""",
        label="Program 2 conic boundary",
    )
    text = _replace_once(
        text,
        """The current unconditional public interval remains `4 <= D_min <= 7`.

### Proof-signature index""",
        """The current unconditional public interval remains `4 <= D_min <= 7`.

**Paper-audit checkpoint.** The rank-one proof and verifier survive, as do
the four conic certificates and the recovered tricuspidal, syzygy, and count
checks. Corollary A.2's exact target-span-two conclusion is not established
by the active paper because three conic orbits and the rational-cubic
exclusion lack complete proof access. B.4 is incomplete; C.2, C.3, and D.2
are not publication-grade. These are audit findings, not withdrawals of
later chart calculations.

### Proof-signature index""",
        label="Program 2 paper audit",
    )
    text = _replace_once(
        text,
        """**New computation checkpoint.** Nine additional exact calculations replay on
the displayed generic, `c=0`, `tau=0` rank-open, `tau=-1`, and zero-normal
charts, strengthening local evidence but not global placement. Exploratory
degree-five/six calculations are chart-local. Their main quartic verifier is
not wholly passing: its `tau=0` expected resultant differs from the computed
one by `16/(b0^2 c0^2)`, and its generic rank-divisor section also fails the
asserted 28-nonzero-minor count. A separate exact diagnostic gives 19
nonzero minors on the generic and `tau=0` charts and 14 on the
minimal-syzygy chart, with the expected rank-divisor gcds recovered up to
units; it does not repair the received script. Separately, regenerated
filtered bases make every listed `delta(Q)<=9` certificate pass and give
`trdeg A_{<=6}<=2`; the residual full-orbit frontier is unramified
`delta(Q)>=10` plus a conceptual filtered-conormal, Wronskian, or conductor
theorem.""",
        """**Computation checkpoints.** The earlier exploratory packet remains
chart-local and not wholly passing: its `tau=0` expected resultant is off by
`16/(b0^2 c0^2)`, and it asserts 28 nonzero maximal minors where exact counts
are 19 generically and on `tau=0`, and 14 on the minimal-syzygy chart. A
newer structural packet has eight self-contained successful replays. It
routes a primitive coprime quintic line image to binary or aligned
`(L^5,L^4)`, excludes the squarefree binary-cubic conic branch, and leaves an
aligned nonbinary specialization open. Under
`ker Jac(A,B,-)=k[A,B]`, it excludes primitive sextic conic and weighted
`(2,3)` cores. This is not a global degree-five/six exclusion. Separately,
every listed `delta(Q)<=9` certificate passes and gives
`trdeg A_{<=6}<=2`; the residual full-orbit frontier is unramified
`delta(Q)>=10` plus a conceptual filtered-conormal, Wronskian, or conductor
theorem.""",
        label="Program 2 computation checkpoint",
    )
    text = _replace_once(
        text,
        """The earlier degree-three archive adds the displayed `F_3/F_4`
parametrizations and arbitrary-lower-term determinant calculation. Its
77-file manifest and all checkers passed; thirteen outputs reproduced
byte-for-byte. At that version, branch discovery remained incomplete.

""",
        "",
        label="Program 2 superseded archive paragraph",
    )
    text = _replace_once(
        text,
        """For the companion/Jordan budget, the v3 bundle embeds the v2 foundation and
fixed-component correction, while v4 controls earlier chart prose. The
v2-v4 manifests pass; all four v2 programs, the v3 correction, and all five
v4 programs replay. The old v2 global `r=4` assertion is withdrawn, and the
correct fixed-component Wronskian contains `2B_0`. These ten checks are one
SymPy lineage, not independent verification of the conventional proof.

""",
        "",
        label="Program 2 duplicated Jordan evidence",
    )
    return _validate_public(text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--base-manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    args = parser.parse_args()

    output_dir = args.output_dir.resolve()
    if output_dir.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output_dir}")
    if output_dir.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")

    base = json.loads(args.base_manifest.read_text(encoding="utf-8"))
    if base.get("brief_count") != 7 or len(base.get("briefs", [])) != 7:
        raise ValueError("base manifest must describe exactly seven briefs")

    prepared: list[tuple[Path, str, dict[str, object]]] = []
    for item in base["briefs"]:
        slug = item["program_slug"]
        source_name = SOURCE_MAP.get(slug)
        if source_name is None:
            raise ValueError(f"unexpected model brief slug: {slug}")
        if slug == "minimum-degree-and-quartic-exclusions":
            source = args.base_manifest.parent / item["source"]
            text = _update_program_2(source.read_text(encoding="utf-8"))
        else:
            source = args.source_dir / source_name
            text = _publicize(
                source.read_text(encoding="utf-8"),
                cross_program=item["kind"] == "cross_program",
            )
        payload = text.encode("utf-8")
        words = len(text.split())
        if not 2_000 <= words <= 4_000:
            raise ValueError(f"{slug}: word count {words} is outside 2000–4000")
        out_name = item["source"]
        prepared.append(
            (
                output_dir / out_name,
                text,
                {
                    **item,
                    "sha256": _sha256(payload),
                    "bytes": len(payload),
                    "words": words,
                },
            )
        )

    output_dir.mkdir()
    for path, text, _ in prepared:
        path.write_text(text, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "release_id": args.release_id,
        "updated_at": args.updated_at,
        "brief_count": len(prepared),
        "briefs": [item for _, _, item in prepared],
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output_dir": str(output_dir),
                "release_id": args.release_id,
                "brief_count": len(prepared),
                "manifest_sha256": _sha256(
                    (output_dir / "manifest.json").read_bytes()
                ),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
