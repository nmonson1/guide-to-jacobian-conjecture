#!/usr/bin/env python3
"""Promote the focused Lane 3/Lane 8 computations into the lane briefs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LANE3_SOURCE = "bounded-degree-deformation-modulus-onset.md"
LANE8_SOURCE = "plane-newton-queue-terminal-certificates.md"
HUB_SOURCE = "state-of-the-program.md"
TECHNICAL_MANIFEST_SHA256 = (
    "d483e84f4c6826afc95d4afea0a498725fb9a56cde7c14e9bc5239fa1bdeaf7d"
)
JACOBIAN_SOURCE_COMMIT = "f1b6ed8c9c4f9a3a5dd3dc44b61cf57a70774f6c"
FOCUSED_ARTIFACTS = (
    {
        "filename": "03-direct-order-five-recovery-2026-08-03-v1.zip",
        "sha256": "48ae426de30743ad270b52299e633725153a27ceef20b131d657c682236c78cd",
    },
    {
        "filename": "06-f2-support-windows-order-520-2026-08-03-v1.zip",
        "sha256": "a0017d6537021b80098b78349cd7ad5566f6606d053b7e8f3f1dbd634d14ca64",
    },
)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"expected JSON object: {path}")
    return value


def _replace_once(text: str, old: str, new: str, *, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected one replacement target, found {count}")
    return text.replace(old, new, 1)


def _verify_source(source: Path, manifest: dict[str, Any]) -> None:
    entries = [*manifest["briefs"], *manifest["task_inputs"]]
    expected_names = {entry["source"] for entry in entries}
    actual_names = {path.name for path in source.iterdir() if path.name != "manifest.json"}
    if actual_names != expected_names:
        raise ValueError("source file set does not match its manifest")
    for entry in entries:
        payload = (source / entry["source"]).read_bytes()
        if len(payload) != entry["bytes"] or _sha256(payload) != entry["sha256"]:
            raise ValueError(f"source file does not match manifest: {entry['source']}")


def _update_lane3(text: str) -> str:
    lineage = """The determinant reconstruction and marked-root source-flow complex agree
through order four. The direct lineage reaches order six, reproduces
`H(5)=145`, finds no new quintic equation, and finds the unique primitive
weight-three sextic. Orders seven and eight lack an independent reconstruction.
"""
    recovery = lineage + """

The [recovered direct order-five computation](../../assets/technical-materials/03-direct-order-five-recovery-2026-08-03-v1.zip)
now makes the direct residual cache and an exact replay public. The restricted
loader rebuilds every weighted Macaulay block in parameter degrees two through
five and certifies the degree-five ranks

```text
initial row space       1857
maximal-ideal multiple  2503
full ideal              2538
H(5)                     145
new quintic generators     0.
```

This closes the mechanical recovery and exact rank-replay task. It does not
derive the residual equations independently from the displayed base map and
337-dimensional slice, and it does not supply the marked-root contracting
homotopy or the order-five chain comparison.
"""
    text = _replace_once(text, lineage, recovery, label="Lane 3 recovery insertion")

    start = text.index("## Exact live problems\n")
    independent = text.index("\nIndependently, sharpen", start)
    refreshed_problem = """## Exact live problems

Independently reconstruct the **direct** order-five Kuranishi equations from
the displayed map and slice, then compare the result with the recovered cache.
The public main source gives every coefficient of `F_0`, the eleven
coefficients removed to define the 337-dimensional slice, and the determinant
equation. Starting from those data, compute the rank-327 linearization over
`Q`, choose and record an explicit pivot minor, solve the 327 pivot variables
recursively through parameter order five, and form the Macaulay row space.
The recovered packet supplies a fail-closed comparison target, not a substitute
for this derivation: the independently produced filtered equations and row
spaces must agree before the task is complete.

The target checks are rank 1857, `H(5)=145`, and no new minimal quintic
generator. The root-native contracting homotopy and bases are still absent,
so the marked-root/direct chain-map comparison remains blocked.
"""
    text = text[:start] + refreshed_problem + text[independent:]

    text = _replace_once(
        text,
        """### P3-L3A0 — Direct order-five reconstruction

Status: ready.

Inputs: the normalized base map, the 337-dimensional slice, and the determinant
equation in [`manuscripts/03-local-rigidity/main.tex`](../proof-sources/03-local-rigidity/main.md). The recorded target
invariants and evidence boundary are in
[`manuscripts/03-local-rigidity/appendices/source-flow-reconstruction-progress.tex`](../proof-sources/03-local-rigidity/appendices/source-flow-reconstruction-progress.md)
and [`RMU-C9E196D6`](../working-mathematics/units/RMU-C9E196D6.md).
""",
        """### P3-L3A0 — Independent direct order-five reconstruction

Status: ready; the recovered cache replay is complete and available as an
exact comparison target.

Inputs: the normalized base map, the 337-dimensional slice, and the determinant
equation in [`manuscripts/03-local-rigidity/main.tex`](../proof-sources/03-local-rigidity/main.md). The recorded target
invariants and evidence boundary are in
[`manuscripts/03-local-rigidity/appendices/source-flow-reconstruction-progress.tex`](../proof-sources/03-local-rigidity/appendices/source-flow-reconstruction-progress.md)
and [`RMU-C9E196D6`](../working-mathematics/units/RMU-C9E196D6.md). The
[recovered exact replay](../../assets/technical-materials/03-direct-order-five-recovery-2026-08-03-v1.zip)
is the final cross-check, not an input from which to choose pivots or rows.
""",
        label="Lane 3 task status",
    )
    text = _replace_once(
        text,
        """Status: blocked until the native contracting homotopy, root-native bases, and
the P3-L3A0 direct matrix package are public inputs.
""",
        """Status: blocked until the native contracting homotopy, root-native bases, and
the independently reconstructed P3-L3A0 direct matrix package are public
inputs. The recovered direct-cache replay alone does not clear this gate.
""",
        label="Lane 3 comparison boundary",
    )
    text = _replace_once(
        text,
        """## Scope cautions

- The length-584 result concerns the bounded, quotiented degree-seven slice.
""",
        """## Scope cautions

- The recovered order-five row spaces are exact, but they are not an
  independent derivation from the displayed map and slice.
- The length-584 result concerns the bounded, quotiented degree-seven slice.
""",
        label="Lane 3 scope boundary",
    )
    return text


def _update_lane8(text: str) -> str:
    anchor = """No novelty or priority claim is made for
this bound.
"""
    recovery = anchor + """

For the degree-`125` `F_2` seed, the
[recovered support/order-520 packet](../../assets/technical-materials/06-f2-support-windows-order-520-2026-08-03-v1.zip)
now supplies an exact maximal Newton-bounded outer model. It propagates 4,433
`P` exponents and 12,340 `Q` exponents into 981 and 1,663 nonempty layers,
respectively, and computes all 2,681 determinant-output layers. The first
forcing window outside the linearized image occurs at order 510. In one
`C_5`-invariant weighted slice, fresh parameters cancel the apparent
order-510 and order-520 functionals, and an independent verifier checks the
determinant identity through order 520.

The word *maximal* is essential: this outer model treats its supported
coefficients independently and does not impose every cross-layer relation
inherited from descent through one fixed approximate-root shear. It therefore
does not construct the actual complete-chain chart. Its nonzero order-530
value after setting newly available coordinates to zero is not an obstruction.
"""
    text = _replace_once(text, anchor, recovery, label="Lane 8 recovery insertion")

    start = text.index("## Exact live problem\n")
    tasks = text.index("\n## Tasks and deliverables\n", start)
    refreshed_problem = """## Exact live problem

Refine the recovered maximal Newton-bounded `F_2` model to the actual
degree-`125` complete-chain chart. Starting from the displayed endpoint faces,
the public maximal support windows, and the distinguished double-root shear,
derive every cross-layer coefficient relation inherited from one fixed
approximate-root descent. Impose those relations before deciding the actual
normalized supports, two-point normal-layer windows, and first invariant
obstruction. The recovered model is an exact outer bound and replay surface;
it is not evidence that all 4,433 `P` and 12,340 `Q` coefficients can vary
independently in a complete chain.
"""
    text = text[:start] + refreshed_problem + text[tasks:]

    task_start = text.index("### P6-L8A")
    scope_start = text.index("## Scope cautions", task_start)
    refreshed_tasks = """### P6-L8A — Complete-chain refinement of `F_2` support propagation

Status: ready; the maximal Newton-bounded support propagation is recovered and
exactly replayable, while the inherited complete-chain relations remain open.

Inputs: all exact `F_2` endpoint, common-power, double-root, terminal ODE,
quotient-map and passport data displayed above; the
[recovered support/order-520 packet](../../assets/technical-materials/06-f2-support-windows-order-520-2026-08-03-v1.zip);
[`manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/F2_degree125_boundary_seed.md`](lane-8-source-packet.md);
and [`next_complete_chain_queue.json`](lane-8-source-packet.md). The maximal
support model is a certified outer model, not the desired complete-chain
answer.

Deliverable: derive the cross-layer coefficient relations forced by the fixed
approximate-root shear, impose them on the maximal support sets, and return the
actual normalized support alternatives and two-point windows. If the public
endpoint and shear data still underdetermine a relation, identify the first
missing datum exactly rather than treating coefficients as independent.

### P6-L8B — Machine-readable actual-chain replay

Status: the maximal-model replay is complete; the actual-chain replay is
blocked on P6-L8A.

Deliverable: encode the accepted complete-chain relations, support nodes, and
coordinate edges with content hashes; replay every corner, congruence, and
coefficient-transport check; and compare the resulting windows with the
published maximal outer bounds.

### P6-L8C — Invariant normal-layer obstruction at degree 125

Status: one maximal-model weighted slice is solved through order 520; the
actual-chain obstruction problem is blocked on P6-L8A and P6-L8B.

Deliverable: build the determinant-layer operators and residue adjoints on the
actual recovered windows and locate the first invariant nonzero obstruction,
or prove exact solvability through a stated order while retaining every fresh
kernel parameter. A value obtained by zeroing new coordinates is not an
obstruction certificate.

"""
    text = text[:task_start] + refreshed_tasks + text[scope_start:]
    text = _replace_once(
        text,
        """## Scope cautions

- A terminal unit ideal proves only its pinned system.
""",
        """## Scope cautions

- The recovered `F_2` support windows are a maximal independent-coefficient
  enlargement, not the actual complete-chain chart.
- Cancellation through order 520 is proved only in the selected weighted
  slice of that enlargement.
- The reported zero-new-coordinate order-530 value is not an obstruction.
- A terminal unit ideal proves only its pinned system.
""",
        label="Lane 8 scope boundary",
    )
    return text


def _update_hub(text: str) -> str:
    text = _replace_once(
        text,
        """**3 August mathematical refresh.** The nine focused pages now include the
selectively retained results from the latest lane investigations, link their
proof and computation boundaries, and move each ready task past what is now
known. Lane 8 now begins at the degree-125 boundary after a direct closure of
both strict below-125 support roots. The six program dossiers remain deeper
overlapping views.
""",
        """**3 August mathematical refresh.** The nine focused pages now include the
selectively retained results from the latest lane investigations and the two
recovered focused computations. Lane 3 exposes the exact direct-cache replay
through order five while keeping independent reconstruction and the
marked-root comparison open. Lane 8 exposes the maximal `F_2` support model
and selected weighted-slice cancellation through order 520 while keeping the
actual complete-chain relations and invariant obstruction problem open. The
six program dossiers remain deeper overlapping views.
""",
        label="portfolio refresh",
    )
    text = _replace_once(
        text,
        """Either reconstruct the direct order-five Kuranishi calculation or sharpen the
proved stable-equivalence complexity of the quadratic-modulus family.
""",
        """Independently reconstruct the direct order-five Kuranishi equations and compare
them with the recovered exact row-space replay, or sharpen the proved
stable-equivalence complexity of the quadratic-modulus family.
""",
        label="portfolio Lane 3 frontier",
    )
    text = _replace_once(
        text,
        """Propagate the explicit degree-`125` `F_2` seed through its complete Newton
chain; both strict below-`125` support roots are now closed directly.
""",
        """Refine the recovered maximal degree-`125` `F_2` support model into an
actual complete-chain chart by deriving and imposing the inherited cross-layer
relations; the selected outer-model slice is already verified through order 520.
""",
        label="portfolio Lane 8 frontier",
    )
    text = _replace_once(
        text,
        "| 3 | `P3-L3A0` or `P3-L3D`: direct reconstruction or sharp stable complexity |",
        "| 3 | `P3-L3A0` or `P3-L3D`: independent reconstruction/cache comparison or sharp stable complexity |",
        label="portfolio Lane 3 task",
    )
    text = _replace_once(
        text,
        "| 8 | `P6-L8A`: propagate the degree-125 `F_2` support chain |",
        "| 8 | `P6-L8A`: refine the maximal `F_2` model to the actual complete chain |",
        label="portfolio Lane 8 task",
    )
    text = _replace_once(
        text,
        """The technical release includes complete supplements for all six programs and
focused materials for major continuations. The claim pages carry stable tags
""",
        """The technical release includes complete supplements for all six programs and
focused materials for major continuations. In particular, the
[Lane 3 order-five replay](../../assets/technical-materials/03-direct-order-five-recovery-2026-08-03-v1.zip)
and [Lane 8 `F_2` support/order-520 packet](../../assets/technical-materials/06-f2-support-windows-order-520-2026-08-03-v1.zip)
are linked directly from their focused pages with their evidence boundaries.
The claim pages carry stable tags
""",
        label="portfolio evidence index",
    )
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    args = parser.parse_args()

    source = args.source_dir.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    if output.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")

    manifest_path = source / "manifest.json"
    manifest = _load(manifest_path)
    if manifest.get("schema_version") != 6 or manifest.get("brief_count") != 16:
        raise ValueError("source must be a sixteen-brief schema-v6 handoff release")
    _verify_source(source, manifest)

    transforms = {
        LANE3_SOURCE: _update_lane3,
        LANE8_SOURCE: _update_lane8,
        HUB_SOURCE: _update_hub,
    }
    payloads: dict[str, bytes] = {}
    for path in sorted(source.iterdir()):
        if path.name == "manifest.json":
            continue
        text = path.read_text(encoding="utf-8")
        if path.name in transforms:
            text = transforms[path.name](text)
        payloads[path.name] = text.encode("utf-8")

    output.mkdir()
    for name, payload in payloads.items():
        with (output / name).open("xb") as handle:
            handle.write(payload)

    manifest["release_id"] = args.release_id
    manifest["updated_at"] = args.updated_at
    manifest["base_release"] = {
        "release_id": _load(manifest_path)["release_id"],
        "manifest_sha256": _sha256(manifest_path.read_bytes()),
    }
    manifest["focused_computation_release"] = {
        "jacobian_source_commit": JACOBIAN_SOURCE_COMMIT,
        "technical_manifest_sha256": TECHNICAL_MANIFEST_SHA256,
        "artifacts": list(FOCUSED_ARTIFACTS),
    }
    for entry in manifest["briefs"]:
        payload = payloads[entry["source"]]
        entry["sha256"] = _sha256(payload)
        entry["bytes"] = len(payload)
        entry["words"] = len(payload.decode("utf-8").split())

    manifest_payload = (
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    ).encode("utf-8")
    with (output / "manifest.json").open("xb") as handle:
        handle.write(manifest_payload)
    print(
        json.dumps(
            {
                "output_dir": str(output),
                "release_id": args.release_id,
                "manifest_sha256": _sha256(manifest_payload),
                "updated_briefs": sorted(transforms),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
