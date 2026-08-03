# Lane 9 exact research source packet

This page exposes the proof notes, computation contracts, programs,
and finite inputs used by the focused lane brief. Each section names
its canonical repository path and source hash. No private checkout or
download is required.

## Included files

- [`research-notes/finite-diagnostics-20260803-v1/verify_lane9_wall_groupoid_packet.py`](#source-d0b4f303a7952bd0) — `e71abf9aa41e4de9dbe78dd103a9c61a8b0c772bf45e3a37e0df18f19112aebc`
- [`research-notes/lane89-mathematical-recovery-20260803-v1/README.md`](#source-38ab8bd19d25aff4) — `d91dea30f97b84627a5f470a62042d7b08113e1099e8a2ceb917d9fe0b3b04ab`
- [`research-notes/lane89-mathematical-recovery-20260803-v1/evidence.json`](#source-ab81932dfb3d4762) — `85f9d954c411ae8c712a5fe3b750438b404395f8783cda56806c966549b24042`
- [`research-notes/lane89-mathematical-recovery-20260803-v1/run_f2_omega530_fresh_parameter.py`](#source-151645a0e17f5aa6) — `9ddebd48cf42375304756cd116248ab0be41d42282018f72d425bc9dc580ee11`
- [`research-notes/lane89-mathematical-recovery-20260803-v1/verify_lane89_recovery.py`](#source-de9fde3d3aea4139) — `97fb0634bccd4ecd863bda23e018156205431ae5e1ebe87d2adb7a75bd6be177`
- [`research-notes/lane9-wall-shear-20260802-v1/LANE9_CONTINUATION_V3_REPORT.md`](#source-971de09272c1e303) — `c95708358a4bb8486d3823d15279e4acec3574fd55d2e5ad49234f032e57d510`
- [`research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/F2_CYCLIC_WALL_DESCENT.md`](#source-fa8ccec644530dcc) — `2485be2f147247108a3c7dd828187a4985d5086d712ccc8ad14b2dd70696cce5`
- [`research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_DUAL_TRIPLE_OVERLAP.md`](#source-bcb444020cf39f50) — `43a45be475ebeadb54f553f88038e446cce9a34d3e7d17e73ae92d48260da3b0`
- [`research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_GRADING_AUDIT.md`](#source-df78139764827f98) — `afeec62e2950cc4a120e9b5280dfbf04d1e1c86135a290c2bc3a1f0df84df745`
- [`research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_OVERLAP_THEOREM.md`](#source-d6c38a4c865ab7c9) — `94d278bd3285f8eadc2d31901a8518b84de8e8f53ec40d0d6cfa86975e412059`
- [`research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_REES_FLOW.md`](#source-c47dc9e578777d37) — `9f763c0acd13a068b96cef1f073b46cf1a2afa9d82fa8fa32426c812648662ab`
- [`research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_jet_transport_audit.py`](#source-b52f970145b7946d) — `4d240c1e6dc80412e1aa29fc55e7b6bf44208fb870577ab4f5ed642e7a758954`
- [`research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_overlap_saturation.py`](#source-054e38ce26bf5835) — `4a3c3d76037ebbae7328fe65a3e35d04ad85c3311fc72566881d5895b0511848`
- [`research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_triple_overlap.py`](#source-2be4880ec062eadd) — `5639081b7a0c4d72c8e4bf80170c9f43fcb45deb01146f323e1a396d65dd5988`
- [`research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/wall_shear_master_covariance.py`](#source-f8b6710dea6c05d9) — `ae914d451e4ec3ab1b583c5f35c2e35c396c5596b9340dd817672961abc460cd`
- [`research-notes/p6-chart-correspondence/LANE9_F2_PARAMETER_COMPLETE_RECURRENCE_V2.md`](#source-89e4eda45b4d5d16) — `77999de9423009feaf0657903607784fed1ae1524ed8a300394f4fe2206ef6a6`
- [`research-notes/p6-chart-correspondence/lane9_f2_attachment_recurrence.py`](#source-2b16e7df7e008983) — `f3c1719ae04ceb10f335b67d6aaa38bfa03c14186c2c8d32d9ba24262046563b`

<a id="source-d0b4f303a7952bd0"></a>

## `research-notes/finite-diagnostics-20260803-v1/verify_lane9_wall_groupoid_packet.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Replay and summarize the exact 73-test Lane 9 ambient groupoid packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents&#91;2&#93;
PACKET = (
    ROOT
    / "research-notes/lane9-wall-shear-20260802-v1"
    / "research-notes/p6-chart-correspondence"
)


def load(name: str) -&gt; dict&#91;str, object&#93;:
    return json.loads((PACKET / name).read_text(encoding="utf-8"))


def main() -&gt; int:
    run = subprocess.run(
        &#91;
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            str(PACKET),
            "-p",
            "test_*.py",
            "-v",
        &#93;,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    transcript = run.stdout + run.stderr
    match = re.search(r"Ran (\d+) tests", transcript)
    if run.returncode != 0 or match is None or int(match.group(1)) != 73:
        raise AssertionError(f"wall-groupoid suite failed or changed:\n{transcript}")

    overlap = load("degree21_k4_overlap_saturation.expected.json")
    triple = load("degree21_k4_triple_overlap.expected.json")
    support = load("degree21_k4_support_audit.expected.json")
    flow = load("wall_shear_rees_hamiltonian_flow.expected.json")
    result = {
        "schema_version": 1,
        "name": "Lane 9 ambient wall-groupoid comparison",
        "status": "pass",
        "test_count": 73,
        "packet_source_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(PACKET.glob("*.py"))
        },
        "support": {
            "bare_k4_first_layer": support&#91;"normal_layer"&#93;,
            "lies_in_fixed_chart_window": support&#91;"lies_in_fixed_chart_window"&#93;,
        },
        "saturation_dimensions": {
            "deformation_old": overlap&#91;"deformation_space"&#93;&#91;"old_dimension"&#93;,
            "deformation_saturated": overlap&#91;"deformation_space"&#93;&#91;"saturated_dimension"&#93;,
            "equation_old": overlap&#91;"equation_space"&#93;&#91;"old_dimension"&#93;,
            "equation_saturated": overlap&#91;"equation_space"&#93;&#91;"saturated_dimension"&#93;,
        },
        "overlap_dimensions": {
            "deformation_pairwise": triple&#91;"deformation_space"&#93;&#91;"pairwise_overlap_dimension"&#93;,
            "deformation_all_parameter": triple&#91;"deformation_space"&#93;&#91;"stable_all_parameter_core_dimension"&#93;,
            "deformation_pairwise_only": triple&#91;"deformation_space"&#93;&#91;"pairwise_only_dimension"&#93;,
            "equation_pairwise": triple&#91;"equation_space"&#93;&#91;"pairwise_overlap_dimension"&#93;,
            "equation_all_parameter": triple&#91;"equation_space"&#93;&#91;"stable_all_parameter_core_dimension"&#93;,
            "equation_pairwise_only": triple&#91;"equation_space"&#93;&#91;"pairwise_only_dimension"&#93;,
        },
        "quotient_flow": flow&#91;"quotient_chart"&#93;,
        "does_not_establish": &#91;
            "that the ambient wall transport is an actual adjacent complete-chain chart",
            "the fixed-chart admissible polynomial subgroup",
            "the archived layer-four residual identification",
            "the missing F2 endpoint blocks or their global attachment",
        &#93;,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result&#91;"certificate_sha256"&#93; = hashlib.sha256(canonical).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-38ab8bd19d25aff4"></a>

## `research-notes/lane89-mathematical-recovery-20260803-v1/README.md`

<pre><code class="language-markdown">
# Lane 8/9 mathematical recovery

This packet records an independent replay and scope audit of two distinct
pieces of the degree-`125` boundary program. It does not update a canonical
graph, research handoff, release selector, or public site.

## Classification

| result | primary lane | connection |
|---|---|---|
| direct closure of the two normalized `(8,28)` roots | Lane 8 | supplies the terminal Newton-root calculation used in the relative below-`125` assembly |
| `F_2` support windows and normal recurrence | Lane 9 | starts from the degree-`125` Lane 8 boundary seed, but is a chart/recurrence and descent problem |

The second item should therefore be described as **Lane 9 primary, with a
Lane 8 connection**. It is not another proof path for the Lane 8 full root.

## Lane 8 direct closure

The tracked full-root packet was replayed from the raw Newton polygons, the
exact quintic face relations, and the Jacobian coefficient formula. It did
not consume archived layer matrices or obstruction equations.

- The truncated root again has Macaulay rank `14` on the complete set of
  fourteen weight-four monomials. Its selected minor has SHA-256
  `8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059`.
- The full root again produces a layer-four square, closes the
  `t1_1=0` complement using the two top vertices, and normalizes the open
  child to fifteen equations. Their canonical SHA-256 is
  `d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883`.
- Zero-based equations `4,6,8,9,10,11` are literally a relaxation of those
  fifteen. The selected-six digest is
  `e4bf0e1842fcd0d3d7c403e6a5ec17fb800914f3208887f0b05d8727b563bb6a`.
  Their emptiness remains an imported exact Program 6 toric theorem.
- The stored adjacent-chart terminal remains empty but unattached and is not
  used in either closure path.

The resulting below-`125` statement has exactly the following scope: it is a
proof assembly relative to the inspected GGHV Newton reduction, its exclusion
of the `(9,27)` case, its routing of `(8,28)` to the two normalized roots, the
imported face orbit, and the imported compact toric terminal. It is not an
independent reproof of those inputs and carries no priority claim.

## Exact `F_2` support windows

After the denominator-five shear, write a monomial as `x^(a/5)y^J`, put
`w=a-J`, and use the terminal direction `(25,-17)`. The exact maximal
Newton-bounded supports are

\&#91;
S_P=\{(a,J):-60\le w\le15,\ 0\le J\le60-\langle w\rangle_5,
\ 5a-17J\le3\},
\&#93;

\&#91;
S_Q=\{(a,J):-100\le w\le25,\ 0\le J\le100-\langle w\rangle_5,
\ 5a-17J\le5\}.
\&#93;

In the terminal chart `x=t^-25`, `y=t^17 z`, `u=z^5`, write

\&#91;
P=t^{-3}\sum_r t^rA_r(z),\qquad
Q=t^{-5}\sum_r t^rB_r(z).
\&#93;

The `C_5` characters are

\&#91;
A_r=z^{(1-2r)\bmod5}\bar A_r(u),\qquad
B_r=z^{-2r\bmod5}\bar B_r(u).
\&#93;

For either coordinate, the exact `u` interval is obtained by intersecting the
raw `J` bounds with the required residue class and then applying the single
top sawtooth correction `J_top &lt;= Y-&lt;w_top&gt;_5`. The verifier checks this
closed formula at every order, not only selected rows.

The regenerated inventory is:

| object | exact count |
|---|---:|
| propagated `P` coefficients | 4,433 |
| nonempty `P` layers | 981 |
| propagated `Q` coefficients | 12,340 |
| nonempty `Q` layers | 1,663 |
| determinant-output layers | 2,681 |

The first target coordinate outside the linearized image is the constant
coefficient at order `510`.

## Orders 510, 520, and 530

The retained exact rational generator fixes the order-10 coordinate, uses an
order-260 kernel coordinate to cancel `omega510`, chooses an order-270
direction in the kernel of that functional, and uses its scalar to cancel
`omega520`. The independent determinant verifier checks all layers `0..520`
and all serialized support bounds. Both values are exactly zero.

The old nonzero `omega530` value is obtained only after every unselected RREF
kernel coordinate is assigned zero. The retained multiple-of-10 slice has
`212` free slots across its `52` positive layers through order `520`, while
the generator explicitly selects only the order-10, order-260, and constrained
order-270 values.

The new exact probe reopens the five order-280 RREF coordinates:

- the kernel of `omega510` on that space has dimension `4`;
- the joint kernel of `omega510` and `omega520` has dimension `3`;
- `omega530` is nonzero as a functional on that joint kernel; and
- one displayed exact rational direction cancels `omega530` and verifies the
  determinant identity through order `530`.

Thus the old order-530 value is decisively a **zero-new-coordinate slice** and
not an obstruction. The new order-530 certificate is still a slice: it reopens
only order `280` and sets all other omitted coordinates to zero.

## Why no parameter-complete Slurm run was submitted

A parameter-complete continuation of the actual `F_2` complete-chain chart is
not runnable from the retained inputs. The public support model is explicitly
the maximal Newton-bounded independent-coefficient enlargement and omits the
inherited cross-layer relations needed to identify the actual chart. The
retained rational generator does not construct the full symbolic family of
all RREF coordinates, and the adjacent-chart/global descent data remain
unattached.

Submitting the rational slice as a “parameter-complete” cluster job would
overstate both the input model and the calculation. No Slurm job was submitted.
The exact order-530 slice replay is small enough to run locally and
is retained at the immutable versioned path recorded in `evidence.json`.

## Verification

Metadata-only validation is portable:

```bash
uv run python \
  research-notes/lane89-mathematical-recovery-20260803-v1/verify_lane89_recovery.py \
  --metadata-only
```

On the internal workspace, the full checker verifies both immutable run
paths, every ZIP member digest, every support-window formula, both determinant
certificates, and optionally regenerates the support and linear-rank JSON:

```bash
uv run python \
  research-notes/lane89-mathematical-recovery-20260803-v1/verify_lane89_recovery.py \
  --regenerate
```

The fresh-parameter order-530 result can be reproduced only at a new,
nonexisting output path:

```bash
uv run python \
  research-notes/lane89-mathematical-recovery-20260803-v1/run_f2_omega530_fresh_parameter.py \
  --bundle /path/to/06-f2-support-windows-order-520-2026-08-03-v1.zip \
  --output-dir /path/to/new-versioned-run
```
</code></pre>

<a id="source-ab81932dfb3d4762"></a>

## `research-notes/lane89-mathematical-recovery-20260803-v1/evidence.json`

<pre><code class="language-json">
{
  "base_commit": "25fd4547397cca49fbff3293e381359930cbdbf0",
  "classification": {
    "f2_recurrence": "lane9_primary_lane8_connection",
    "full_root_closure": "lane8"
  },
  "f2": {
    "P_coefficients": 4433,
    "P_nonempty_layers": 981,
    "Q_coefficients": 12340,
    "Q_nonempty_layers": 1663,
    "determinant_output_layers": 2681,
    "first_external_forcing_window": 510,
    "linear_complex_replay_path": "/path/to/versioned-artifact",
    "order520_certificate_sha256": "8a410747ab17dfaff51756138c795c2667ab3f922318f5aa0e8cc5cd54e810d5",
    "order520_replay_path": "/path/to/versioned-artifact",
    "public_bundle_path": "/path/to/versioned-artifact",
    "public_bundle_sha256": "a0017d6537021b80098b78349cd7ad5566f6606d053b7e8f3f1dbd634d14ca64",
    "support_windows_sha256": "81b7750a8510c00250b508a3b919e62be860e051f72059183ef45ad416d0720f",
    "total_rref_free_slots_in_retained_multiple_of_10_slice_through_520": 212,
    "zero_slice_omega530_mod_1000003": 856714
  },
  "lane8": {
    "full_fifteen_sha256": "d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883",
    "replay_summary_path": "/path/to/versioned-artifact",
    "source_packet": "research-notes/lane8-full-root-closure-20260803-v1",
    "summary_sha256": "8ad4054e2efb8f8a682e67ad6fbe15feccb1eae0bf3181750e6a3fff7d708907",
    "terminal_projection_sha256": "e4bf0e1842fcd0d3d7c403e6a5ec17fb800914f3208887f0b05d8727b563bb6a",
    "truncated_minor_sha256": "8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059"
  },
  "order530": {
    "fresh_parameter_certificate_path": "/path/to/versioned-artifact",
    "certificate_sha256": "c3dc5244862956c4c834d09af43abd0d294d17966e6fa5efb65e4c850a95ddbb",
    "fresh_parameter_scope": {
      "joint_omega510_omega520_kernel_dimension": 3,
      "omega510_kernel_dimension": 4,
      "reopened_order": 280,
      "reopened_rref_coordinates": 5,
      "verified_through": 530
    },
    "parameter_complete_assessment": {
      "reasons": &#91;
        "the maximal support model omits inherited cross-layer descent relations",
        "the retained rational generator assigns unselected RREF kernel coordinates to zero",
        "the adjacent-chart and global descent inputs remain unattached"
      &#93;,
      "runnable": false,
      "slurm_job_submitted": false
    }
  },
  "schema": "lane89-mathematical-recovery-evidence-v1"
}
</code></pre>

<a id="source-151645a0e17f5aa6"></a>

## `research-notes/lane89-mathematical-recovery-20260803-v1/run_f2_omega530_fresh_parameter.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Extend the retained F2 weighted slice through order 530 exactly.

This is deliberately not a parameter-complete complete-chain calculation.
It reopens only the five RREF-kernel coordinates at order 280, finds the
joint kernel of the order-510 and order-520 functionals, and uses one exact
rational direction in that joint kernel to cancel order 530.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
from types import ModuleType
from zipfile import ZipFile


EXPECTED_BUNDLE_SHA256 = (
    "a0017d6537021b80098b78349cd7ad5566f6606d053b7e8f3f1dbd634d14ca64"
)
GENERATOR_MEMBER = "f2_omega520_kuranishi.py"
WINDOW_MEMBER = "f2_support_windows.json"


def sha256_path(path: Path) -&gt; str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_generator(bundle: Path, destination: Path) -&gt; tuple&#91;ModuleType, Path&#93;:
    if sha256_path(bundle) != EXPECTED_BUNDLE_SHA256:
        raise ValueError("unexpected F2 public-bundle SHA-256")
    with ZipFile(bundle) as archive:
        names = set(archive.namelist())
        for member in (GENERATOR_MEMBER, WINDOW_MEMBER):
            if member not in names:
                raise ValueError(f"bundle lacks {member}")
        archive.extract(GENERATOR_MEMBER, destination)
        archive.extract(WINDOW_MEMBER, destination)
    generator_path = destination / GENERATOR_MEMBER
    spec = importlib.util.spec_from_file_location("f2_o520_recovered", generator_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load recovered order-520 generator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, generator_path


def selected_order520_assignments(module: ModuleType) -&gt; tuple&#91;dict, dict&#93;:
    eta = F(1)
    seed = {10: {0: eta}}
    omega510_base = module.omega(510, seed)
    omega510_mu_slope = (
        module.omega(510, {10: {0: eta}, 260: {0: F(1)}})
        - omega510_base
    )
    if not omega510_mu_slope:
        raise AssertionError("order-260 direction does not move omega510")
    mu = -omega510_base / omega510_mu_slope

    nu0_slope = (
        module.omega(510, {10: {0: eta}, 270: {0: F(1)}})
        - omega510_base
    )
    nu1_slope = (
        module.omega(510, {10: {0: eta}, 270: {1: F(1)}})
        - omega510_base
    )
    if not nu1_slope:
        raise AssertionError("second order-270 direction does not move omega510")
    ratio = -nu0_slope / nu1_slope

    def assignments(value: F) -&gt; dict:
        return {
            10: {0: eta},
            260: {0: mu},
            270: {0: value, 1: value * ratio},
        }

    omega520_at_zero = module.omega(520, assignments(F(0)))
    omega520_slope = module.omega(520, assignments(F(1))) - omega520_at_zero
    if not omega520_slope:
        raise AssertionError("order-270 null direction does not move omega520")
    value = -omega520_at_zero / omega520_slope
    selected = assignments(value)
    if module.omega(510, selected) or module.omega(520, selected):
        raise AssertionError("failed to reconstruct the retained order-520 slice")
    audit = {
        "eta": str(eta),
        "mu": str(mu),
        "order270_direction_ratio": str(ratio),
        "lambda": str(value),
    }
    return selected, audit


def combine(vectors: list&#91;list&#91;F&#93;&#93;, coefficients: list&#91;F&#93;) -&gt; list&#91;F&#93;:
    return &#91;
        sum(
            (
                coefficient * vector&#91;index&#93;
                for vector, coefficient in zip(vectors, coefficients)
            ),
            F(0),
        )
        for index in range(len(vectors&#91;0&#93;))
    &#93;


def one_row_kernel(vectors: list&#91;list&#91;F&#93;&#93;, values: list&#91;F&#93;) -&gt; list&#91;list&#91;F&#93;&#93;:
    """Return an exact basis for the kernel of one functional on a basis."""
    pivot = next((index for index, value in enumerate(values) if value), None)
    if pivot is None:
        return vectors
    output: list&#91;list&#91;F&#93;&#93; = &#91;&#93;
    for index in range(len(vectors)):
        if index == pivot:
            continue
        coefficients = &#91;F(0)&#93; * len(vectors)
        coefficients&#91;index&#93; = F(1)
        coefficients&#91;pivot&#93; = -values&#91;index&#93; / values&#91;pivot&#93;
        output.append(combine(vectors, coefficients))
    return output


def with_order280_direction(
    base: dict,
    vector: list&#91;F&#93;,
    scalar: F = F(1),
) -&gt; dict:
    output = {order: dict(values) for order, values in base.items()}
    output&#91;280&#93; = {
        index: scalar * coefficient
        for index, coefficient in enumerate(vector)
        if coefficient
    }
    return output


def fraction_list(values: list&#91;F&#93;) -&gt; list&#91;str&#93;:
    return &#91;str(value) for value in values&#93;


def make_certificate(module: ModuleType) -&gt; dict:
    base, retained_parameters = selected_order520_assignments(module)
    _, _, partial_records = module.solve(base, 280)
    free_dimension = partial_records&#91;-1&#93;&#91;"free_dim"&#93;
    if partial_records&#91;-1&#93;&#91;"r"&#93; != 280 or free_dimension != 5:
        raise AssertionError("unexpected order-280 RREF kernel")

    standard = &#91;
        &#91;F(index == column) for index in range(free_dimension)&#93;
        for column in range(free_dimension)
    &#93;
    omega510_values = &#91;
        module.omega(510, with_order280_direction(base, vector))
        for vector in standard
    &#93;
    kernel510 = one_row_kernel(standard, omega510_values)
    for vector in kernel510:
        if module.omega(510, with_order280_direction(base, vector)):
            raise AssertionError("computed order-510 kernel direction failed")

    omega520_values = &#91;
        module.omega(520, with_order280_direction(base, vector))
        for vector in kernel510
    &#93;
    joint_kernel = one_row_kernel(kernel510, omega520_values)
    for vector in joint_kernel:
        trial = with_order280_direction(base, vector)
        if module.omega(510, trial) or module.omega(520, trial):
            raise AssertionError("computed joint-kernel direction failed")

    zero_slice_omega530 = module.omega(530, base)
    if not zero_slice_omega530:
        raise AssertionError("retained zero-new-coordinate omega530 unexpectedly vanished")
    omega530_values = &#91;
        module.omega(530, with_order280_direction(base, vector))
        - zero_slice_omega530
        for vector in joint_kernel
    &#93;
    pivot = next(
        (index for index, value in enumerate(omega530_values) if value),
        None,
    )
    if pivot is None:
        raise AssertionError("omega530 vanishes on the entire computed joint kernel")
    direction = joint_kernel&#91;pivot&#93;
    scalar = -zero_slice_omega530 / omega530_values&#91;pivot&#93;
    final_assignments = with_order280_direction(base, direction, scalar)
    for order in (510, 520, 530):
        if module.omega(order, final_assignments):
            raise AssertionError(f"omega{order} did not cancel")

    a_layers, b_layers, records = module.solve(final_assignments, 530)
    if module.full_layer(0, a_layers, b_layers) != {0: F(-1)}:
        raise AssertionError("leading determinant layer changed")
    for order in range(1, 531):
        if module.full_layer(order, a_layers, b_layers):
            raise AssertionError(f"nonzero determinant layer {order}")

    return {
        "schema": "f2-omega530-fresh-order280-certificate-v1",
        "model": (
            "F2 maximal Newton-bounded independent-coefficient recursion; "
            "C5-invariant weighted slice"
        ),
        "claim": "exact rational weighted-slice jet through order 530",
        "boundary": (
            "Only the five order-280 RREF-kernel coordinates are reopened. "
            "This is not the all-parameter complete-chain recurrence and does "
            "not restore the omitted inherited descent relations."
        ),
        "base": {
            "A0": {str(exponent): str(value) for exponent, value in module.A0.items()},
            "B0": {str(exponent): str(value) for exponent, value in module.B0.items()},
        },
        "retained_order520_parameters": retained_parameters,
        "fresh_parameter_analysis": {
            "order": 280,
            "free_dimension": free_dimension,
            "omega510_values_on_rref_basis": fraction_list(omega510_values),
            "omega510_kernel_dimension": len(kernel510),
            "omega520_values_on_omega510_kernel": fraction_list(omega520_values),
            "joint_omega510_omega520_kernel_dimension": len(joint_kernel),
            "omega530_values_on_joint_kernel": fraction_list(omega530_values),
            "zero_new_coordinate_omega530": str(zero_slice_omega530),
            "cancelling_joint_kernel_index": pivot,
            "cancelling_direction": fraction_list(direction),
            "cancelling_scalar": str(scalar),
            "final_order280_rref_coordinates": {
                str(index): str(value)
                for index, value in sorted(final_assignments&#91;280&#93;.items())
            },
        },
        "verified": {
            "determinant_layers": "0..530",
            "omega510": "0",
            "omega520": "0",
            "omega530": "0",
            "recorded_positive_layers": len(records),
        },
        "layers": records,
    }


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    bundle = args.bundle.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite {output}")
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="f2-omega530-generator-") as temporary:
        module, _ = load_generator(bundle, Path(temporary))
        certificate = make_certificate(module)

    output.mkdir()
    script_copy = output / Path(__file__).name
    bundle_copy = output / bundle.name
    certificate_path = output / "f2_omega530_fresh_parameter_certificate.json"
    shutil.copyfile(Path(__file__), script_copy)
    shutil.copyfile(bundle, bundle_copy)
    certificate_path.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    files = (script_copy, bundle_copy, certificate_path)
    (output / "SHA256SUMS").write_text(
        "".join(f"{sha256_path(path)}  {path.name}\n" for path in files),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "certificate": str(certificate_path),
                "certificate_sha256": sha256_path(certificate_path),
                "omega510": "0",
                "omega520": "0",
                "omega530": "0",
                "joint_kernel_dimension": certificate&#91;
                    "fresh_parameter_analysis"
                &#93;&#91;"joint_omega510_omega520_kernel_dimension"&#93;,
                "scope": "order-280 fresh-parameter slice, not parameter-complete",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-de9fde3d3aea4139"></a>

## `research-notes/lane89-mathematical-recovery-20260803-v1/verify_lane89_recovery.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Fail-closed verifier for the Lane 8/9 mathematical recovery packet."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile
from typing import Any
from zipfile import ZipFile


PACKET = Path(__file__).resolve().parent
REPOSITORY_ROOT = PACKET.parents&#91;1&#93;
EVIDENCE_PATH = PACKET / "evidence.json"


def require(condition: bool, message: str) -&gt; None:
    if not condition:
        raise AssertionError(message)


def sha256_path(path: Path) -&gt; str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_evidence() -&gt; dict&#91;str, Any&#93;:
    evidence = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))
    require(
        evidence&#91;"schema"&#93; == "lane89-mathematical-recovery-evidence-v1",
        "unexpected evidence schema",
    )
    require(evidence&#91;"base_commit"&#93;.startswith("25fd454"), "wrong private base")
    classification = evidence&#91;"classification"&#93;
    require(
        classification == {
            "full_root_closure": "lane8",
            "f2_recurrence": "lane9_primary_lane8_connection",
        },
        "lane classification changed",
    )
    assessment = evidence&#91;"order530"&#93;&#91;"parameter_complete_assessment"&#93;
    require(assessment&#91;"runnable"&#93; is False, "parameter-complete scope overstated")
    require(assessment&#91;"slurm_job_submitted"&#93; is False, "unexpected Slurm claim")
    require(
        assessment&#91;"reasons"&#93;
        == &#91;
            "the maximal support model omits inherited cross-layer descent relations",
            "the retained rational generator assigns unselected RREF kernel coordinates to zero",
            "the adjacent-chart and global descent inputs remain unattached",
        &#93;,
        "parameter-complete boundary changed",
    )
    return evidence


def verify_lane8_summary(path: Path, expected: dict&#91;str, Any&#93;) -&gt; None:
    require(sha256_path(path) == expected&#91;"summary_sha256"&#93;, "Lane 8 summary SHA-256")
    summary = json.loads(path.read_text(encoding="utf-8"))
    require(summary&#91;"schema"&#93; == "lane8-independent-raw-support-replay-v1", "Lane 8 schema")
    require(summary&#91;"inputs"&#93;&#91;"archived_layers_used"&#93; is False, "Lane 8 used archived layers")
    require(summary&#91;"inputs"&#93;&#91;"archived_equations_used"&#93; is False, "Lane 8 used archived equations")
    require(summary&#91;"truncated"&#93;&#91;"macaulay_rank"&#93; == 14, "truncated rank")
    require(
        summary&#91;"truncated"&#93;&#91;"minor_determinant_sha256"&#93;
        == expected&#91;"truncated_minor_sha256"&#93;,
        "truncated minor digest",
    )
    require(summary&#91;"full"&#93;&#91;"weight_four_is_square"&#93; is True, "full layer-four square")
    require(
        summary&#91;"full"&#93;&#91;"vertex_saturation_forces_t11_nonzero"&#93; is True,
        "full closed complement",
    )
    require(len(summary&#91;"full"&#93;&#91;"equation_manifest"&#93;) == 15, "full equation count")
    require(
        summary&#91;"full"&#93;&#91;"final_equation_sha256"&#93;
        == expected&#91;"full_fifteen_sha256"&#93;,
        "full fifteen digest",
    )
    require(
        summary&#91;"full"&#93;&#91;"terminal_projection"&#93;&#91;"zero_based_indices"&#93;
        == &#91;4, 6, 8, 9, 10, 11&#93;,
        "toric projection indices",
    )
    require(
        summary&#91;"full"&#93;&#91;"terminal_projection"&#93;&#91;"sha256"&#93;
        == expected&#91;"terminal_projection_sha256"&#93;,
        "terminal projection digest",
    )
    require(
        summary&#91;"full"&#93;&#91;"higher_deficiency_coefficients_projected_away"&#93;
        == {
            "cutoff": 8,
            "P": 3,
            "Q": 28,
            "extra_vertices": {"P_(0,8)": 10, "Q_(0,12)": 15},
        },
        "higher-deficiency projection boundary",
    )


def safe_archive_members(archive: ZipFile) -&gt; dict&#91;str, bytes&#93;:
    members: dict&#91;str, bytes&#93; = {}
    for info in archive.infolist():
        path = PurePosixPath(info.filename)
        require(not path.is_absolute() and ".." not in path.parts, "unsafe ZIP member")
        require(not info.is_dir(), f"unexpected directory member {info.filename}")
        members&#91;info.filename&#93; = archive.read(info)
    return members


def verify_file_manifest(members: dict&#91;str, bytes&#93;) -&gt; None:
    manifest = json.loads(members&#91;"FILE_MANIFEST.json"&#93;)
    expected_names = {row&#91;"path"&#93; for row in manifest&#91;"files"&#93;}
    require(expected_names == set(members) - {"FILE_MANIFEST.json"}, "bundle inventory")
    for row in manifest&#91;"files"&#93;:
        payload = members&#91;row&#91;"path"&#93;&#93;
        require(len(payload) == row&#91;"bytes"&#93;, f"bundle size {row&#91;'path'&#93;}")
        require(
            hashlib.sha256(payload).hexdigest() == row&#91;"sha256"&#93;,
            f"bundle digest {row&#91;'path'&#93;}",
        )


def expected_window(data: dict&#91;str, Any&#93;, order: int) -&gt; dict&#91;str, int&#93; | None:
    metadata = data&#91;"metadata"&#93;
    lower = max(
        0,
        -(
            -(
                order
                + 5 * metadata&#91;"initial_weight_min"&#93;
                - metadata&#91;"terminal_weight_max"&#93;
            )
            // 12
        ),
    )
    upper = min(
        metadata&#91;"y_max"&#93;,
        (
            order
            + 5 * metadata&#91;"initial_weight_max"&#93;
            - metadata&#91;"terminal_weight_max"&#93;
        )
        // 12,
    )
    residue = (3 * (order - metadata&#91;"terminal_weight_max"&#93;)) % 5
    u_min = -(-(lower - residue) // 5)
    u_max = (upper - residue) // 5
    if u_min &gt; u_max:
        return None
    top = residue + 5 * u_max
    numerator = metadata&#91;"terminal_weight_max"&#93; + 12 * top - order
    require(numerator % 5 == 0, "window character congruence")
    initial_weight = numerator // 5
    if top &gt; metadata&#91;"y_max"&#93; - initial_weight % 5:
        u_max -= 1
    if u_min &gt; u_max:
        return None
    return {
        "J_min": residue + 5 * u_min,
        "J_max": residue + 5 * u_max,
        "dimension": u_max - u_min + 1,
    }


def verify_all_support_windows(windows: dict&#91;str, Any&#93;, expected: dict&#91;str, Any&#93;) -&gt; None:
    for label in ("P", "Q"):
        support = windows&#91;"support"&#93;&#91;label&#93;
        rows = {int(order): row for order, row in windows&#91;f"{label}_windows"&#93;.items()}
        require(
            support&#91;"propagated_support_size"&#93; == expected&#91;f"{label}_coefficients"&#93;,
            f"{label} support size",
        )
        require(
            len(rows) == expected&#91;f"{label}_nonempty_layers"&#93;,
            f"{label} layer count",
        )
        require(
            sum(row&#91;"dimension"&#93; for row in rows.values())
            == expected&#91;f"{label}_coefficients"&#93;,
            f"{label} coefficient total",
        )
        last_order = support&#91;"summary"&#93;&#91;"last_layer"&#93;
        for order in range(last_order + 1):
            formula = expected_window(support, order)
            serialized = rows.get(order)
            require((formula is None) == (serialized is None), f"{label} window presence {order}")
            if formula is not None and serialized is not None:
                require(
                    {
                        "J_min": serialized&#91;"J_min"&#93;,
                        "J_max": serialized&#91;"J_max"&#93;,
                        "dimension": serialized&#91;"dimension"&#93;,
                    }
                    == formula,
                    f"{label} window formula {order}",
                )
    require(
        len(windows&#91;"full_jacobian_output_windows"&#93;)
        == expected&#91;"determinant_output_layers"&#93;,
        "determinant output layer count",
    )


def parse_poly(data: dict&#91;str, str&#93;) -&gt; dict&#91;int, F&#93;:
    return {int(exponent): F(value) for exponent, value in data.items()}


def derivative(poly: dict&#91;int, F&#93;) -&gt; dict&#91;int, F&#93;:
    return {
        exponent - 1: F(exponent) * value
        for exponent, value in poly.items()
        if exponent and value
    }


def add_product(
    output: dict&#91;int, F&#93;,
    left: dict&#91;int, F&#93;,
    right: dict&#91;int, F&#93;,
    scale: F,
) -&gt; None:
    for left_exponent, left_value in left.items():
        for right_exponent, right_value in right.items():
            exponent = left_exponent + right_exponent
            output&#91;exponent&#93; = (
                output.get(exponent, F(0))
                + scale * left_value * right_value
            )


def determinant_layer(
    order: int,
    a_layers: dict&#91;int, dict&#91;int, F&#93;&#93;,
    b_layers: dict&#91;int, dict&#91;int, F&#93;&#93;,
) -&gt; dict&#91;int, F&#93;:
    output: dict&#91;int, F&#93; = {}
    for left_order in range(order + 1):
        right_order = order - left_order
        a_layer = a_layers.get(left_order, {})
        b_layer = b_layers.get(right_order, {})
        if not a_layer or not b_layer:
            continue
        add_product(output, a_layer, derivative(b_layer), F(3 - left_order))
        add_product(output, derivative(a_layer), b_layer, F(right_order - 5))
    return {exponent: value for exponent, value in output.items() if value}


def allowed_exponents(window: dict&#91;str, Any&#93;) -&gt; set&#91;int&#93;:
    return set(range(window&#91;"J_min"&#93;, window&#91;"J_max"&#93; + 1, 5))


def verify_jet_layers(
    certificate: dict&#91;str, Any&#93;,
    windows: dict&#91;str, Any&#93;,
    through: int,
) -&gt; None:
    p_windows = {int(order): row for order, row in windows&#91;"P_windows"&#93;.items()}
    q_windows = {int(order): row for order, row in windows&#91;"Q_windows"&#93;.items()}
    a_layers = {0: parse_poly(certificate&#91;"base"&#93;&#91;"A0"&#93;)}
    b_layers = {0: parse_poly(certificate&#91;"base"&#93;&#91;"B0"&#93;)}
    seen: set&#91;int&#93; = set()
    for record in certificate&#91;"layers"&#93;:
        order = int(record&#91;"r"&#93;)
        require(order not in seen, f"duplicate jet layer {order}")
        seen.add(order)
        a_layers&#91;order&#93; = parse_poly(record&#91;"A"&#93;)
        b_layers&#91;order&#93; = parse_poly(record&#91;"B"&#93;)
        require(
            set(a_layers&#91;order&#93;).issubset(allowed_exponents(p_windows&#91;order&#93;)),
            f"P support at order {order}",
        )
        require(
            set(b_layers&#91;order&#93;).issubset(allowed_exponents(q_windows&#91;order&#93;)),
            f"Q support at order {order}",
        )
    require(determinant_layer(0, a_layers, b_layers) == {0: F(-1)}, "leading layer")
    for order in range(1, through + 1):
        require(
            determinant_layer(order, a_layers, b_layers) == {},
            f"nonzero determinant layer {order}",
        )


def verify_order520(
    members: dict&#91;str, bytes&#93;,
    windows: dict&#91;str, Any&#93;,
    expected: dict&#91;str, Any&#93;,
) -&gt; None:
    support_payload = members&#91;"f2_support_windows.json"&#93;
    require(
        support_payload == members&#91;"data/f2_support_windows.json"&#93;,
        "two support-window payloads differ",
    )
    require(
        hashlib.sha256(support_payload).hexdigest()
        == expected&#91;"support_windows_sha256"&#93;,
        "support-window digest",
    )
    certificate_payload = members&#91;"f2_omega520_exact_certificate.json"&#93;
    require(
        hashlib.sha256(certificate_payload).hexdigest()
        == expected&#91;"order520_certificate_sha256"&#93;,
        "order-520 certificate digest",
    )
    certificate = json.loads(certificate_payload)
    require(
        sum(record&#91;"free_dim"&#93; for record in certificate&#91;"layers"&#93;)
        == expected&#91;
            "total_rref_free_slots_in_retained_multiple_of_10_slice_through_520"
        &#93;,
        "retained-slice free-coordinate inventory",
    )
    require(certificate&#91;"kuranishi_data"&#93;&#91;"verified_omega510"&#93; == "0", "omega510")
    require(certificate&#91;"kuranishi_data"&#93;&#91;"verified_omega520"&#93; == "0", "omega520")
    require(
        F(certificate&#91;"kuranishi_data"&#93;&#91;"next_zero-slice_constant_omega530"&#93;),
        "zero-new-coordinate omega530 unexpectedly zero",
    )
    require(
        certificate&#91;"mod_1000003_checks"&#93;&#91;"omega530"&#93;
        == expected&#91;"zero_slice_omega530_mod_1000003"&#93;,
        "omega530 modular check",
    )
    verify_jet_layers(certificate, windows, 520)


def verify_order530(
    path: Path,
    windows: dict&#91;str, Any&#93;,
    expected: dict&#91;str, Any&#93;,
) -&gt; None:
    require(sha256_path(path) == expected&#91;"certificate_sha256"&#93;, "order-530 certificate digest")
    certificate = json.loads(path.read_text(encoding="utf-8"))
    require(
        certificate&#91;"schema"&#93; == "f2-omega530-fresh-order280-certificate-v1",
        "order-530 schema",
    )
    analysis = certificate&#91;"fresh_parameter_analysis"&#93;
    require(analysis&#91;"free_dimension"&#93; == 5, "order-280 free dimension")
    require(analysis&#91;"omega510_kernel_dimension"&#93; == 4, "omega510 kernel dimension")
    require(
        analysis&#91;"joint_omega510_omega520_kernel_dimension"&#93; == 3,
        "joint kernel dimension",
    )
    require(F(analysis&#91;"zero_new_coordinate_omega530"&#93;), "zero slice vanished")
    require(
        any(F(value) for value in analysis&#91;"omega530_values_on_joint_kernel"&#93;),
        "omega530 did not move on the joint kernel",
    )
    require(
        certificate&#91;"verified"&#93;
        == {
            "determinant_layers": "0..530",
            "omega510": "0",
            "omega520": "0",
            "omega530": "0",
            "recorded_positive_layers": 53,
        },
        "order-530 verification summary",
    )
    verify_jet_layers(certificate, windows, 530)


def run_checked(command: list&#91;str&#93;, cwd: Path, timeout: int) -&gt; str:
    completed = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )
    require(completed.returncode == 0, completed.stdout&#91;-8000:&#93;)
    return completed.stdout


def regenerate_bundle_artifacts(extracted: Path, temporary: Path) -&gt; None:
    support_output = temporary / "support"
    run_checked(
        &#91;
            sys.executable,
            str(extracted / "scripts" / "f2_support_windows.py"),
            "--outdir",
            str(support_output),
        &#93;,
        extracted,
        120,
    )
    require(
        (support_output / "f2_support_windows.json").read_bytes()
        == (extracted / "data" / "f2_support_windows.json").read_bytes(),
        "support-window regeneration differs",
    )
    run_checked(
        &#91;
            sys.executable,
            str(extracted / "scripts" / "f2_kuranishi_linear.py"),
            "--windows",
            str(support_output / "f2_support_windows.json"),
            "--outdir",
            str(support_output),
        &#93;,
        extracted,
        120,
    )
    for name in ("f2_linear_complexes.json", "f2_linear_complexes_summary.json"):
        require(
            (support_output / name).read_bytes()
            == (extracted / "data" / name).read_bytes(),
            f"linear-complex regeneration differs: {name}",
        )
    run_checked(
        &#91;
            sys.executable,
            str(extracted / "verify_f2_omega520_certificate.py"),
            str(extracted / "f2_omega520_exact_certificate.json"),
        &#93;,
        extracted,
        120,
    )


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata-only", action="store_true")
    parser.add_argument("--lane8-summary", type=Path)
    parser.add_argument("--f2-bundle", type=Path)
    parser.add_argument("--order530-certificate", type=Path)
    parser.add_argument("--regenerate", action="store_true")
    args = parser.parse_args()
    evidence = load_evidence()
    if args.metadata_only:
        print("lane89 recovery metadata validation: PASS")
        return 0

    lane8_summary = (
        args.lane8_summary
        or Path(evidence&#91;"lane8"&#93;&#91;"replay_summary_path"&#93;)
    )
    f2_bundle = args.f2_bundle or Path(evidence&#91;"f2"&#93;&#91;"public_bundle_path"&#93;)
    order530_certificate = (
        args.order530_certificate
        or Path(evidence&#91;"order530"&#93;&#91;"fresh_parameter_certificate_path"&#93;)
    )
    verify_lane8_summary(lane8_summary, evidence&#91;"lane8"&#93;)
    require(sha256_path(f2_bundle) == evidence&#91;"f2"&#93;&#91;"public_bundle_sha256"&#93;, "F2 bundle digest")

    with ZipFile(f2_bundle) as archive:
        members = safe_archive_members(archive)
        verify_file_manifest(members)
        windows = json.loads(members&#91;"f2_support_windows.json"&#93;)
        verify_all_support_windows(windows, evidence&#91;"f2"&#93;)
        verify_order520(members, windows, evidence&#91;"f2"&#93;)
        verify_order530(order530_certificate, windows, evidence&#91;"order530"&#93;)
        if args.regenerate:
            with tempfile.TemporaryDirectory(prefix="lane89-regenerate-") as directory:
                extracted = Path(directory) / "bundle"
                archive.extractall(extracted)
                regenerate_bundle_artifacts(extracted, Path(directory))

    print("lane89 mathematical recovery validation: PASS")
    print("lane8_roots=truncated_closed,full_closed")
    print("below_125=relative_to_imported_GGHV_and_compact_toric_theorems")
    print("f2_support_windows=exact_maximal_newton_bounded_enlargement")
    print("omega510=0 omega520=0 omega530_fresh_order280_slice=0")
    print("parameter_complete_order530=not_runnable_from_retained_inputs")
    print("classification=lane8_full_root;lane9_f2_recurrence_with_lane8_connection")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-971de09272c1e303"></a>

## `research-notes/lane9-wall-shear-20260802-v1/LANE9_CONTINUATION_V3_REPORT.md`

<pre><code class="language-markdown">
# Lane 9 continuation v3 report

## Result

The ambient wall atlas now includes exact residue-dual transport, forcing
pairings, triple-overlap constraints, an operation-space commutator, and
cyclic parameter descent.

## 1. Obstruction duals and forcing transport

For primal density transport

\&#91;
T e_{n,j}
 =\sum_q\binom{n-p+2j}{q}\lambda^q
 e_{n+q(2k-1),j-qk},
\&#93;

the exact contragredient is

\&#91;
U\epsilon_{m,l}
 =\sum_q\binom{p-m-2l-1}{q}\lambda^q
 \epsilon_{m-q(2k-1),l+qk}.
\&#93;

It satisfies

\&#91;
U^\mathsf TT=I.
\&#93;

The formula was checked on every basis vector of the 114-dimensional `P`,
180-dimensional `Q`, and 300-dimensional equation-density wall
saturations. Consequently left-null obstruction functionals and their
pairings with forcing vectors transport exactly through the ambient chain
map.

## 2. Triple overlap adds real conditions

Through layer 15,

\&#91;
T_\lambda=I+\lambda N+\lambda^2N^2/2.
\&#93;

The old chart and one nonzero transported chart overlap in 89 deformation
dimensions. The intersection of the charts at parameters `0`, `1`, and `-1`
is only 68-dimensional and equals the subspace stable under every wall
parameter.

For the equation density, the corresponding dimensions are 216 and 206.
Thus a two-chart check leaves

\&#91;
\boxed{21\text{ deformation directions}}
\&#93;

and

\&#91;
\boxed{10\text{ equation directions}}
\&#93;

that fail triple-overlap compatibility.

The first-order coefficient overflow has rank 97, but all-parameter stability
imposes 118 independent source conditions. The quadratic wall term therefore
adds 21 independent constraints, even though it creates only 11 new ambient
coefficient coordinates.

## 3. Transporting the layer-four candidate forces a layer-eleven term

Let the layer-four support-admissible field be

\&#91;
f_4=c_0+c_1z+z^2,
\qquad g_4=2c_0z^{-1}+3c_1+4z,
\&#93;

and let the `k=4` wall field be

\&#91;
f_7=2z^{-3},
\qquad g_7=z^{-4}.
\&#93;

Their bracket is the layer-eleven field

\&#91;
f_{11}=18c_0z^{-4}+30c_1z^{-3}+42z^{-2},
\&#93;

\&#91;
g_{11}=6c_0z^{-5}+5c_1z^{-4}.
\&#93;

Its action on the degree-21 face has unavoidable top terms

\&#91;
336\operatorname{lead}(A_0)z^5,
\qquad
504\operatorname{lead}(B_0)z^9.
\&#93;

The stored layer-eleven windows allow no `P` coefficient and only `Q`
exponents `0,...,4`. Therefore carrying the layer-four direction across the
wall requires a genuine adjacent-chart layer-eleven operation coordinate.
The old fixed-chart operation space cannot be used unchanged.

## 4. The F2 wall parameter is a character line

For a cyclic quotient `u=z^g`, the order-`q` `k`-wall term shifts cyclic
character by `-qk`. Equivariance requires

\&#91;
\lambda\mapsto\zeta^k\lambda.
\&#93;

For `F_2`, `g=5` and `k=4`. The parameter has `C_5` character four, and an
invariant scalar effect first returns at wall order five, unweighted normal
shift 35.

If one simultaneously tries to reconcile the public layer-four label with
the bare layer-seven wall, the unique required normal weight is `-3`. The
necessary parameter bidegree is therefore

\&#91;
\boxed{(-3,4\bmod5)}.
\&#93;

This negative Rees weight is chart-moving data, not an ordinary fixed-chart
deformation coordinate.


## 5. Parameter weight alone fails the layer-four kernel test

Assigning weight `-3` to the `k=4` wall parameter changes the bookkeeping
layer from seven to four, but the bare source pair then has exact defect

\&#91;
-3z^{-2}
\&#93;

in the ordinary \(D_4\) weighted-divergence identity.  The unique correction
with the same horizontal component changes

\&#91;
g:z^{-4}\longmapsto -2z^{-4}.
\&#93;

This produces the candidate associated-graded rechart field

\&#91;
t^4(2z^{-3}\partial_z-2z^{-4}t\partial_t),
\&#93;

whose degree-21 action exits the old layer-four window only through the
principal parts `A={-3,-2,-1}` and `B={-2,-1}`.  The remaining task is to
construct the Rees/Euler action producing this correction and compare it with
the archived residual vector.


## 6. The corrected candidate is a Kummer Hamiltonian flow

Using the original affine-coordinate dictionary

\&#91;
t=x^4y,\qquad z=x^7y^2,
\&#93;

the corrected associated-graded field becomes

\&#91;
\boxed{
V=-6x^{-11}y^{-4}\partial_x
  +22x^{-12}y^{-3}\partial_y.
}
\&#93;

It has ordinary divergence zero and is Hamiltonian for

\&#91;
H=2x^{-11}y^{-3}.
\&#93;

With

\&#91;
M=x^{-12}y^{-4}=t^4z^{-4},
\&#93;

one has

\&#91;
V(H)=0,\qquad V(M)=-16M^2.
\&#93;

The exact formal flow is therefore

\&#91;
R^8=1+16sM,
\&#93;

\&#91;
\boxed{
x_s=xR^{-3},\qquad y_s=yR^{11},\qquad
t_s=tR^{-1},\qquad z_s=zR.
}
\&#93;

The binomial root exists formally in the deformation parameter.  It is not,
however, rational over \(K(x,y,s)\): the radicand has valuation one at the
prime \(x^{12}y^4+16s\), whereas an eighth power has valuation divisible by
eight.  The generic algebraic flow therefore requires a degree-eight Kummer
extension.

There is an exact quotient-coordinate linearization.  Put

\&#91;
H=2x^{-11}y^{-3}=\frac{2}{tz},
\qquad
Q=x^{12}y^4=\left(\frac zt\right)^4=M^{-1}.
\&#93;

Then

\&#91;
V(H)=0,
\qquad
V(Q)=16,
\&#93;

so the flow on the quotient is simply

\&#91;
\boxed{H_s=H,\qquad Q_s=Q+16s.}
\&#93;

The exponent-lattice determinant of \((x,y)\mapsto(H,Q)\) is \(-8\), and

\&#91;
x^8=\frac{16}{H^4Q^3},
\qquad
y^8=\frac{H^{12}Q^{11}}{4096}.
\&#93;

Thus the Kummer extension is exactly the inverse of a degree-eight monomial
quotient.  For the `F_2` `C_5` assignment, both \(Q\) and the parameter have
character four, so \(Q\mapsto Q+16s\) is equivariant; lifting back to
\((x,y)\) still requires the independent eighth root.

In the adjacent blowdown variables used by the stored proposition,

\&#91;
u=(xy)^{-1},\qquad v=y,
\&#93;

these quotient coordinates are

\&#91;
H=2u^{11}v^8,
\qquad
Q=u^{-12}v^{-8}.
\&#93;

Therefore

\&#91;
\boxed{K(H,Q)=K(u,v^8).}
\&#93;

The degree-eight quotient is exactly the \(\mu_8\)-quotient of the adjacent
blowdown chart.  The corrected field descends to this quotient, while the bare
`k=4` operation is the translation \(v\mapsto v+s\), which is not the same
quotient operation.  This isolates a precise missing lift in the public
correspondence claim.


The corrected layer-four candidate is therefore an ordinary translation on a
concrete degree-eight quotient chart, but not an ordinary same-function-field
rational wall operation.  A successful complete-chain interpretation would
have to identify this quotient—or another filtration-changing model—with the
actual adjacent presentation.


Because

\&#91;
Q=\left(\frac zt\right)^4
\&#93;

has normal \(t\)-exponent \(-4\), translation in \(Q\) naturally has the
missing layer-four label.  This gives the strongest current repaired
correspondence candidate:

&gt; match the stored layer-four residual to the pullback of the quotient
&gt; translation \(Q\mapsto Q+16s\), not to the bare layer-seven translation
&gt; \(v\mapsto v+s\).

The scalar `16` is a parameter normalization.  What remains is an exact
coefficientwise comparison with the archived residual representative.

## 7. Current boundary

These results provide an exact finite ambient wall groupoid with:

- coefficient transport;
- nonlinear equation transport;
- inverse and additive cocycles;
- residue-dual and forcing transport;
- pairwise and triple-overlap dimensions;
- a required operation-map commutator term;
- cyclic eigenparameter descent;
- the exact weight-only defect and unique corrected layer-four vertical term.

They still do not provide the actual complete-chain monomial adjacent chart,
its presentation stabilizer, or the real `F_2` order-by-order matrices. Those
are now the remaining external inputs rather than undefined linear-algebra
steps.

## 8. Validation

The combined bundle contains 73 exact regression tests, all passing.
</code></pre>

<a id="source-fa8ccec644530dcc"></a>

## `research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/F2_CYCLIC_WALL_DESCENT.md`

<pre><code class="language-markdown">
# Cyclic descent of a wall parameter in the F2 quotient

**Status:** exact character and filtration bookkeeping. This identifies the
parameter line required for an equivariant wall family. It does not supply
the missing `F_2` normal support windows or prove that the `k=4` wall is an
allowed complete-chain transition for `F_2`.

## 1. Character shift

Let the lattice quotient be

\&#91;
u=z^g,
\&#93;

with deck action

\&#91;
z\longmapsto\zeta z,
\qquad \zeta^g=1,
\&#93;

and assume the normal parameter is fixed. The order-\(q\) term in the
`k`-wall transport contains

\&#91;
\lambda^q z^{-qk}.
\&#93;

If \(\lambda\) is treated as an invariant scalar, the coefficient character
changes by

\&#91;
\chi_j\longmapsto\chi_{j-qk}.
\&#93;

Thus scalar wall transport mixes the cyclic character sectors.

An equivariant family instead requires

\&#91;
\boxed{
\lambda\longmapsto\zeta^k\lambda.
}
\&#93;

Then

\&#91;
\lambda^qz^{j-qk}
\longmapsto
\zeta^{qk+j-qk}\lambda^qz^{j-qk}
 =\zeta^j\lambda^qz^{j-qk},
\&#93;

so each original character sector is preserved over the eigenparameter
line.

## 2. Scalar descent sees only a return-order power

If the wall parameter must itself be invariant, the first order returning to
the original character is

\&#91;
q_0=\frac{g}{\gcd(g,k)}.
\&#93;

For `F_2`,

\&#91;
g=5,
\qquad k=4,
\&#93;

so

\&#91;
\boxed{q_0=5.}
\&#93;

The unweighted normal shift per wall order is seven, hence the first scalar
return occurs at normal shift

\&#91;
\boxed{5\cdot7=35.}
\&#93;

Equivalently, the invariant quotient parameter is locally represented by

\&#91;
\mu=\lambda^5.
\&#93;

Plain averaging in the coefficient space discards the intermediate
noninvariant wall terms. It therefore does not commute with recharting unless
the eigenparameter line is included in the descent datum.

## 3. Necessary bidegree for a layer-four reconciliation

The bare `k=4` wall starts at normal layer seven. If one tries to interpret
its first term as a layer-four rechart direction, the unique necessary normal
weight of \(\lambda\) is

\&#91;
\boxed{\operatorname{wt}_t(\lambda)=4-7=-3.}
\&#93;

Combined with cyclic equivariance in the `F_2` gap-five cover, the required
parameter bidegree would be

\&#91;
\boxed{
(\operatorname{wt}_t,\chi_{C_5})(\lambda)=(-3,4).
}
\&#93;

With this bookkeeping, one wall order has weighted normal degree four and the
first scalar return \(\lambda^5\) has weighted degree

\&#91;
5\cdot4=20.
\&#93;

The negative normal weight is significant. Such a parameter is not an
ordinary coordinate of the nonnegative `t`-adic Rees deformation base. It is
a localized or chart-moving parameter. Therefore a layer-four repair along
these lines would itself prove that the operation is a rechart rather than
fixed-chart gauge—but the corresponding Rees/groupoid construction still has
to be supplied.


## 4. Weight alone does not restore the layer operator

There is an additional compatibility condition.  The bare wall pair

\&#91;
f=2z^{-3},\qquad g=z^{-4}
\&#93;

is a kernel field for \(D_7\), not \(D_4\).  Reassigning the parameter weight
without changing the field gives

\&#91;
(fz^2)' +(4-5)gz^2=-3z^{-2}.
\&#93;

Thus the bidegree `(-3,4)` is necessary bookkeeping but not a complete
repair.  With the same horizontal component, the unique layer-four vertical
component is

\&#91;
g=-2z^{-4}.
\&#93;

A valid descent theorem must construct the Rees/Euler mechanism that produces
this correction and then transport its operation image across the chart
atlas.

## 5. Consequence for the `F_2` attachment problem

The exact order-520 recurrence uses cyclic invariance, but a wall transition
must be descended together with its parameter line. There are two distinct
questions:

1. solve the invariant coefficient recurrence in one fixed presentation;
2. glue presentations using eigenparameters and then descend the entire
   chart groupoid.

The first cannot replace the second. A scalar Reynolds operator sees only
powers at the return order and can miss the intermediate chart data required
for exact gluing.

## 6. Reproduction

```bash
python research-notes/p6-chart-correspondence/f2_cyclic_wall_descent.py \
  --gap 5 --k 4 --requested-layer 4 \
  --output /tmp/f2-cyclic-wall-descent.json
```
</code></pre>

<a id="source-bcb444020cf39f50"></a>

## `research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_DUAL_TRIPLE_OVERLAP.md`

<pre><code class="language-markdown">
# Wall-shear dual transport and triple-overlap theorem

**Status:** exact finite Laurent-jet theorem through normal layer 15 for the
stored degree-21 support. The theorem supplies coefficient, equation,
obstruction-dual, forcing, inverse, and triple-overlap transport for the
ambient wall atlas. It does not identify the intrinsic complete-chain
stabilizer or prove that the transported Laurent windows are the intended
monomial Newton charts.

## 1. Contragredient residue transport

For a coefficient density of pole order `p`, write

\&#91;
e_{n,j}=t^{n-p}z^j.
\&#93;

The exact `k`-wall transport is

\&#91;
T_{k,\lambda}^{(p)}e_{n,j}
 =\sum_{q\ge0}
 \binom{n-p+2j}{q}\lambda^q
 e_{n+q(2k-1),j-qk}.
\&#93;

Let \(\epsilon_{n,j}\) denote the coefficient dual. At fixed normal layer it
is represented by the residue principal part

\&#91;
\epsilon_{n,j}(w)
 =\operatorname {Res}_{z=0}
   z^{-j-1}w_n(z)\,dz.
\&#93;

The dual functional in the transported chart must satisfy

\&#91;
\langle U_{k,\lambda}^{(p)}\ell,
        T_{k,\lambda}^{(p)}w\rangle
 =\langle\ell,w\rangle.
\&#93;

Since \(T_{k,\lambda}^{-1}=T_{k,-\lambda}\), one has

\&#91;
U_{k,\lambda}^{(p)}
 =\left(T_{k,\lambda}^{(p),-1}\right)^\mathsf T.
\&#93;

A direct coefficient calculation gives the closed formula

\&#91;
\boxed{
U_{k,\lambda}^{(p)}\epsilon_{m,l}
 =\sum_{q\ge0}
 \binom{p-m-2l-1}{q}\lambda^q
 \epsilon_{m-q(2k-1),l+qk}.
}
\&#93;

Indeed, the coefficient before applying the elementary binomial identity is

\&#91;
(-1)^q\binom{m-p+2l+q}{q}
 =\binom{p-m-2l-1}{q}.
\&#93;

The implementation checks \(U^\mathsf TT=I\) on every basis vector of the
complete layer-15 saturations:

| density | saturated dimension | maximum primal terms | maximum dual terms |
| --- | ---: | ---: | ---: |
| `P`, pole order 2 | 114 | 3 | 3 |
| `Q`, pole order 3 | 180 | 3 | 3 |
| equation residual, pole order 4 | 300 | 3 | 3 |

Thus every finite obstruction functional and forcing pairing transports
exactly. In particular, if

\&#91;
D_\lambda T_E=T_WD_0,
\qquad \ell^\mathsf TD_0=0,
\&#93;

then

\&#91;
\ell_\lambda=T_W^{-\mathsf T}\ell
\&#93;

satisfies

\&#91;
\ell_\lambda^\mathsf TD_\lambda=0.
\&#93;

For \(\Phi_\lambda=T_W\Phi\),

\&#91;
\boxed{
\langle\ell_\lambda,\Phi_\lambda\rangle
 =\langle\ell,\Phi\rangle.
}
\&#93;

This is the exact residue/forcing transport required by a chart theorem at
the ambient Laurent-jet level.

## 2. Pairwise overlap is not triple overlap

For `k=4`, the wall shift is seven. Through layer 15,

\&#91;
N_4^3=0,
\qquad
T_\lambda=I+\lambda N_4+\frac{\lambda^2}{2}N_4^2.
\&#93;

Let \(E_0\) be the old coefficient window. A vector common to the charts
with parameters \(0,1,-1\) lies in every transported chart. To see this,
project \(T_\lambda v\) to the coordinates outside \(E_0\). The result is a
polynomial of degree at most two in \(\lambda\). If it vanishes at
\(0,1,-1\), it vanishes identically.

Consequently,

\&#91;
\boxed{
E_0\cap E_1\cap E_{-1}
 =\{v\in E_0:T_\lambda v\in E_0\text{ for every }\lambda\}.
}
\&#93;

This is the maximal all-parameter stable core of the old window. The same
statement holds for the equation-density space.

The exact dimensions are:

| space | old | one pairwise overlap | all-parameter core | pairwise-only |
| --- | ---: | ---: | ---: | ---: |
| `P` | 61 | 15 | 8 | 7 |
| `Q` | 125 | 74 | 60 | 14 |
| total deformation `E` | 186 | 89 | 68 | 21 |
| equation density `W` | 257 | 216 | 206 | 10 |

Thus a two-chart check leaves 21 deformation directions and 10 equation
directions that fail the third-chart condition.

The all-parameter stability constraints split as follows:

| space | first-order external rank | extra rank from `N^2` | total |
| --- | ---: | ---: | ---: |
| `P` | 46 | 7 | 53 |
| `Q` | 51 | 14 | 65 |
| total `E` | 97 | 21 | 118 |
| `W` | 41 | 10 | 51 |

These are source-constraint ranks. The corresponding numbers of new ambient
target directions are smaller:

| space | from `N` | new directions from `N^2` | total saturation increment |
| --- | ---: | ---: | ---: |
| `P` | 46 | 7 | 53 |
| `Q` | 51 | 4 | 55 |
| total `E` | 97 | 11 | 108 |
| `W` | 41 | 2 | 43 |

The difference is important: multiple independent source constraints can
land in the same external coefficient coordinate. Counting overflow
monomials alone does not count triple-overlap conditions.

The eight `P` monomials stable under the entire wall orbit are

\&#91;
(0,1),\ (2,0),\ (2,4),\ (2,5),\ (3,4),\
(9,0),\ (9,1),\ (10,0),
\&#93;

where each pair is `(normal layer, z exponent)`. The implementation records
the analogous 60-dimensional `Q` core and 206-dimensional equation core.

## 3. Exact cocycle

On the stable core, every wall transport remains in the old finite window,
and

\&#91;
T_{b-c}T_{a-b}=T_{a-c},
\qquad T_{-\lambda}=T_\lambda^{-1}.
\&#93;

Therefore the three-chart ambient atlas satisfies the required inverse and
triple-overlap cocycle identities exactly. This is stronger than checking one
transition square, but weaker than a complete-chain chart theorem because the
intrinsic monomial charts and their admissible operation groups remain
unidentified.

## 4. Reproduction

```bash
python research-notes/p6-chart-correspondence/wall_shear_dual_transport.py \
  --k 4 --cutoff 15 \
  --output /tmp/wall-shear-dual.json

python research-notes/p6-chart-correspondence/degree21_k4_triple_overlap.py \
  --k 4 --cutoff 15 \
  --output /tmp/degree21-k4-triple-overlap.json
```
</code></pre>

<a id="source-df78139764827f98"></a>

## `research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_GRADING_AUDIT.md`

<pre><code class="language-markdown">
# Wall-shear grading audit for the degree-21 lower face

**Status:** exact coordinate calculation and regression-tested research note.
It identifies a grading/provenance gap in the current public formulation of the
claimed layer-four/`k=4` correspondence. It does not invalidate the separate
adjacent-chart terminal calculation; it shows that the bridge to that
calculation has not been written in a filtration-compatible form.

**Audited repository state:** draft PR 1, head
`fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0`.

## 1. Coordinate dictionary

The degree-21 lower face uses

\&#91;
t=Y,\qquad z=XY^2,
\&#93;

and

\&#91;
P=t^{-\alpha}\sum_{n\ge 0}t^nA_n(z),\qquad
Q=t^{-\beta}\sum_{n\ge 0}t^nB_n(z),
\qquad (\alpha,\beta)=(2,3).
\&#93;

Consider the elementary wall shear

\&#91;
X'=X,\qquad Y'=Y+\lambda X^{-k},\qquad k\ge 1,
\&#93;

with scalar parameter \(\lambda\). Since \(X=z/t^2\), put

\&#91;
h=\lambda t^{2k-1}z^{-k}.
\&#93;

Then the transport in normal coordinates is the exact identity

\&#91;
\boxed{
 t'=t(1+h),\qquad z'=z(1+h)^2.
}
\&#93;

No series expansion is used here.

## 2. The normal order is \(2k-1\)

Differentiating at \(\lambda=0\) gives

\&#91;
\delta t=t^{2k}z^{-k},\qquad
\delta z=2t^{2k-1}z^{1-k}.
\&#93;

In the source-field convention

\&#91;
V_r=t^r\bigl(f(z)\partial_z+g(z)t\partial_t\bigr),
\&#93;

this is

\&#91;
\boxed{
 r=2k-1,\qquad f=2z^{1-k},\qquad g=z^{-k}.
}
\&#93;

For the lower face \(\Psi=z^2\), the weighted-divergence identity is checked
exactly:

\&#91;
(fz^2)' +(r-5)gz^2
=2(3-k)z^{2-k}+2(k-3)z^{2-k}=0.
\&#93;

Thus the shear tangent lies in the unrestricted determinant kernel at normal
order \(2k-1\).

For \(k=4\),

\&#91;
\boxed{
 r=7,\qquad
 V_4=t^7\bigl(2z^{-3}\partial_z+z^{-4}t\partial_t\bigr).
}
\&#93;

Consequently, under the displayed lower-face grading, the bare `k=4` shear is
the identity on the normal jet through layer six. It cannot itself be a
nonzero vector in the layer-four coefficient space.

In the archived affine coordinates

\&#91;
X=x^{-1},\qquad Y=x^4y,
\&#93;

the same operation is simply

\&#91;
y\longmapsto y+\lambda.
\&#93;

This explains why it is a polynomial source operation globally while changing
the center of the completed Newton chart. It does not alter the \(t\)-adic
order computed above.

## 3. Exact transport of every normal monomial

For a normal basis monomial

\&#91;
t^{n-\alpha}z^j,
\&#93;

one has

\&#91;
\boxed{
(t')^{n-\alpha}(z')^j
 =\sum_{q\ge0}
 \binom{n-\alpha+2j}{q}\lambda^q
 t^{n-\alpha+q(2k-1)}z^{j-qk}.
}
\&#93;

The generalized binomial coefficient is interpreted in the usual way for
negative integral upper index. The first-order basis shift is therefore

\&#91;
(n,j)\longmapsto(n+2k-1,j-k)
\&#93;

with coefficient \(n-\alpha+2j\). Define the infinitesimal transport
operator

\&#91;
N_k e_{n,j}=(n-\alpha+2j)e_{n+2k-1,j-k}.
\&#93;

After one application the coefficient drops by one, so

\&#91;
N_k^q e_{n,j}
=(n-\alpha+2j)_{\underline q}
 e_{n+q(2k-1),j-qk}.
\&#93;

Consequently the exact wall transport is

\&#91;
\boxed{F_\lambda^*=\exp(\lambda N_k).}
\&#93;

This supplies the inverse and composition laws formally:

\&#91;
F_{-\lambda}^*=(F_\lambda^*)^{-1},\qquad
F_\lambda^*F_\mu^*=F_{\lambda+\mu}^*.
\&#93;

On a finite normal jet, \(N_k\) is nilpotent after an ambient cutoff is
chosen. This exact sparse operator, rather than support-set closure alone, is
the transition matrix needed in a chart-correspondence packet.

For `k=4`, every first-order coefficient moves up by exactly seven normal
layers and left by four \(z\)-exponents.

## 4. Full stored-window transport profile

Applying \(N_4\) to all 186 monomial basis elements in the archived full
support gives:

| classification | count |
| --- | ---: |
| internal old-window entries | 55 |
| exits through a stored coefficient wall | 97 |
| terms above the stored layer-15 cutoff | 31 |
| zero first-order entries | 3 |

The componentwise counts are:

| component | dimension | internal | window exit | above cutoff | zero |
| --- | ---: | ---: | ---: | ---: | ---: |
| `P` | 61 | 10 | 46 | 3 | 2 |
| `Q` | 125 | 45 | 51 | 28 | 1 |

On the old-window projection, \(N_4^2\) has rank three and
\(N_4^3=0\). Those three second-order entries are the falling-factorial paths

\&#91;
(0,8)\mapsto(14,0):13\cdot12,
\quad
(0,9)\mapsto(14,1):15\cdot14,
\quad
(1,8)\mapsto(15,0):14\cdot13
\&#93;

in the `Q` component.

The important datum is not the small internal rank. More than half of the
first-order basis vectors leave the old coefficient window. Deleting those
97 entries is not a quotient or a chart transition; they must be expressed in
an explicit adjacent-chart basis.

## 5. First exact support exit for the stored degree-21 face

Write

\&#91;
A_0=zp(z),\qquad B_0=z^2q(z).
\&#93;

At the first nonzero normal layer \(r=2k-1\), the tangent action is

\&#91;
a_r=fA_0'-2gA_0=2z^{2-k}p'(z),
\&#93;

\&#91;
b_r=fB_0'-3gB_0
=z^{2-k}q(z)+2z^{3-k}q'(z).
\&#93;

For `k=4`, this becomes

\&#91;
\boxed{
 a_7=2z^{-2}p'(z),\qquad
 b_7=z^{-2}q(z)+2z^{-1}q'(z).
}
\&#93;

The exact degree-21 face has nonzero coefficients through
\(\deg p=7\) and \(\deg q=10\). Hence

\&#91;
\operatorname{supp}(a_7)=\{-2,-1,0,1,2,3,4\},
\&#93;

\&#91;
\operatorname{supp}(b_7)=\{-2,-1,0,1,2,3,4,5,6,7,8\}.
\&#93;

The archived full fixed-chart layer-seven windows are

\&#91;
\operatorname{supp}(A_7)\subseteq\{0,1,2,3\},\qquad
\operatorname{supp}(B_7)\subseteq\{0,1,2,3,4,5,6,7,8\}.
\&#93;

Therefore the exact forbidden exponents are

\&#91;
\boxed{
 A:\{-2,-1,4\},\qquad B:\{-2,-1\}.
}
\&#93;

This is a clean support certificate that the `k=4` tangent leaves the old
fixed-chart window at layer seven. It is consistent with a rechart there; it
is not a fixed-chart gauge vector.

## 6. Consequence for the public layer-four statement

The current public proposition combines:

1. a one-dimensional residual quotient at normal layer four;
2. the elementary operation \(Y\mapsto Y+\lambda X^{-4}\);
3. a subsequent adjacent-chart terminal calculation.

Items 1 and 2 do not match under the public coordinate dictionary:

\&#91;
\text{wall index }k=4
\quad\Longrightarrow\quad
\text{normal order }r=2k-1=7,
\&#93;

not \(r=4\).

A valid repair must provide at least one of the following and verify it
coefficientwise:

- a different pair of coordinates denoted by \((X,Y)\) in the operation;
- a nonzero filtration degree assigned to \(\lambda\);
- an intervening conjugation whose induced graded map sends order seven to
  the stated layer-four quotient;
- a correction of either the layer label or the operation.

A relabeling by `k` alone is insufficient because the manuscript explicitly
uses the normal-layer operator \(D_r\) and calls the residual a normal
layer-four class.

Until this bridge is supplied, the safe public statement is:

&gt; The stored calculation reports a one-dimensional layer-four residual and a
&gt; separate `k=4` adjacent-chart operation. Their claimed identification has an
&gt; unresolved grading map. The adjacent-chart no-gluing certificate should be
&gt; treated as exact for its displayed transformed system, while its provenance
&gt; from the layer-four quotient remains review-pending.

## 7. A separate layer-four integrability result

The maximal linear support-admissible Laurent calculation at normal layer four
has a one-dimensional source basis with

\&#91;
f(z)=c_0+c_1z+z^2.
\&#93;

In the original affine coordinates \(z=x^7y^2\), the corresponding source
field is Hamiltonian:

\&#91;
D_H=H_y\partial_x-H_x\partial_y,
\qquad
H=x^{10}y^3(c_0+c_1z+z^2).
\&#93;

The highest monomial of \(H\) is \(x^{24}y^7\). Its Hamiltonian derivation
acts on a monomial by

\&#91;
D_{\mathrm{top}}(x^py^q)
 =(7p-24q)x^{p+23}y^{q+6}.
\&#93;

Inductively, the leading term of \(D_H^n(x)\) is

\&#91;
\boxed{
\left(\prod_{m=0}^{n-1}(7+17m)\right)
 x^{1+23n}y^{6n}.
}
\&#93;

Every factor is nonzero in characteristic zero, so \(D_H^n(x)\ne0\) for all
\(n\). Hence this support-admissible polynomial derivation is **not locally
nilpotent** and does not generate an algebraic additive one-parameter shear.

This result does not prove the manuscript's full fixed-chart nonintegrability
claim: arbitrary formal flows and non-group polynomial paths are broader than
\(\mathbb G_a\)-actions. It does prove a useful strict separation:

\&#91;
\text{supported polynomial infinitesimal field}
\not\Longrightarrow
\text{integrable additive complete-chain operation}.
\&#93;

The certificate is replayed by
`degree21_r4_hamiltonian_audit.py`.

## 8. Correct chart-correspondence target

For each chart \(C\) and layer \(r\), distinguish

\&#91;
\mathfrak g^{\mathrm{adm}}_{C,r}
 \xrightarrow{\Theta_{C,r}}
E_{C,r}
 \xrightarrow{D_{C,r}}
W_{C,r}.
\&#93;

The tangent and obstruction spaces are

\&#91;
T_{C,r}=\ker D_{C,r}/\operatorname{im}\Theta_{C,r},
\qquad
O_{C,r}=\operatorname{coker}D_{C,r}.
\&#93;

A chart transition \(\tau:C\to C'\) must include exact maps

\&#91;
T_{\tau,E},\quad T_{\tau,W},\quad T_{\tau,\mathfrak g}
\&#93;

satisfying

\&#91;
D_{C'}T_{\tau,E}=T_{\tau,W}D_C,
\qquad
T_{\tau,E}\Theta_C=\Theta_{C'}T_{\tau,\mathfrak g}.
\&#93;

If coefficient transport is affine,

\&#91;
e'=T_{\tau,E}e+\delta_\tau,
\&#93;

then forcing must satisfy

\&#91;
T_{\tau,W}\Phi_C=\Phi_{C'}+D_{C'}\delta_\tau.
\&#93;

Inverse transitions and triple overlaps must satisfy their corresponding
cocycle identities. Only after these checks is it legitimate to identify two
local tangent classes or to quotient by rechart directions.

## 9. Exact nonlinear master-equation covariance

For a coefficient density of pole order \(p\), define

\&#91;
T^{(p)}_{k,\lambda}(t^nz^j)
=
\sum_{q\ge0}
\binom{n-p+2j}{q}\lambda^q
t^{n+q(2k-1)}z^{j-qk}.
\&#93;

Let

\&#91;
\mathcal R_{\alpha,\beta}(A,B)
=
\alpha AB_z-\beta A_zB
+t(A_zB_t-A_tB_z)-z^2.
\&#93;

The residual density has pole order \(\alpha+\beta-1\), and exact two-form
pullback gives

\&#91;
\boxed{
\mathcal R_{\alpha,\beta}
(T^{(\alpha)}A,T^{(\beta)}B)
=
T^{(\alpha+\beta-1)}
\mathcal R_{\alpha,\beta}(A,B).
}
\&#93;

Differentiation gives the full cumulative-jet chain-map square. Thus the wall
transition now has an exact equation-space map, not merely a coefficient
support closure.

## 10. Minimal transported-window overlap

For the archived full degree-21 support through layer 15, the minimal
`k=4` wall-saturated deformation space has dimension 294:

| component | old | saturated | added |
| --- | ---: | ---: | ---: |
| `P` | 61 | 114 | 53 |
| `Q` | 125 | 180 | 55 |
| total | 186 | 294 | 108 |

For every nonzero wall parameter,

\&#91;
\dim(E_0\cap E_\lambda)=89,\qquad
\dim(E_0+E_\lambda)=283.
\&#93;

The transported chart contributes 97 independent directions beyond the old
window, exactly the first-order wall-exit rank. The corresponding nonlinear
equation-density dimensions are

\&#91;
\dim W_0=257,\quad
\dim W^{\mathrm{sat}}=300,\quad
\dim(W_0\cap W_\lambda)=216,\quad
\dim(W_0+W_\lambda)=298.
\&#93;

The base chart and the two opposite charts span the whole minimal saturation:

\&#91;
E^{\mathrm{sat}}=E_0+E_1+E_{-1},\qquad
W^{\mathrm{sat}}=W_0+W_1+W_{-1}.
\&#93;

This is an exact ambient Laurent-jet chart groupoid. It is not yet the
complete-chain monomial atlas.

## 11. Two consequences

First, a filtration-preserving conjugacy cannot turn the `k=4` shift seven
into shift four. If \(C\) has invertible associated graded, then

\&#91;
\sigma_7(CN_4C^{-1})
=
\operatorname{gr}(C)\sigma_7(N_4)\operatorname{gr}(C)^{-1}\ne0.
\&#93;

Any reconciliation of the public layer-four statement must therefore change
the filtration, reweight the wall parameter, or correct a label.

Second, the exact face

\&#91;
A_0=z+\frac32z^2,\qquad B_0=z^2+z^3
\&#93;

has a `k=4` wall arc

\&#91;
A=A_0+3t^7z^{-2}+\frac32t^{14}z^{-6},
\&#93;

\&#91;
B=B_0+t^7(z^{-2}+3z^{-1})+3t^{14}z^{-5}.
\&#93;

At layer 14 the quadratic forcing is

\&#91;
6z^{-5}-27z^{-4},
\&#93;

and the second wall correction has linear image

\&#91;
-6z^{-5}+27z^{-4}.
\&#93;

They cancel exactly. Setting the second correction to zero creates a false
nonzero residual.

## 12. Reproduction

```bash
python research-notes/p6-chart-correspondence/wall_shear_normal_coordinates.py \
  --k 4 \
  --output /tmp/wall-shear-k4.json

python research-notes/p6-chart-correspondence/degree21_k4_support_audit.py \
  research-notes/p6-chart-correspondence/fixtures/exact_belyi_data.json \
  research-notes/p6-chart-correspondence/lower_face_supports.json \
  --k 4 \
  --output /tmp/degree21-k4-support.json

python research-notes/p6-chart-correspondence/degree21_k4_jet_transport_audit.py \
  research-notes/p6-chart-correspondence/lower_face_supports.json \
  --k 4 \
  --output /tmp/degree21-k4-jet-transport.json

python research-notes/p6-chart-correspondence/degree21_r4_hamiltonian_audit.py \
  research-notes/p6-chart-correspondence/degree21_lower_face_full_gauge.json \
  --output /tmp/degree21-r4-hamiltonian.json

python -m unittest discover \
  -s research-notes/p6-chart-correspondence \
  -p 'test_*wall_shear*.py' -v

python -m unittest discover \
  -s research-notes/p6-chart-correspondence \
  -p 'test_degree21_k4_support_audit.py' -v
```

The six new test modules contain thirty-two exact regression tests.


Additional commands:

```bash
python research-notes/p6-chart-correspondence/wall_shear_master_covariance.py \
  --k 4 --cutoff 15 \
  --output /tmp/wall-master-covariance.json

python research-notes/p6-chart-correspondence/degree21_k4_overlap_saturation.py \
  --k 4 --cutoff 15 \
  --output /tmp/degree21-k4-overlap.json
```


## 13. Exact residue-dual transport

The wall transition on a coefficient density of pole order \(p\) has the
pairing-preserving contragredient

\&#91;
U\epsilon_{m,l}
 =\sum_q\binom{p-m-2l-1}{q}\lambda^q
 \epsilon_{m-q(2k-1),l+qk}.
\&#93;

It satisfies \(U^\mathsf TT=I\).  The formula has been checked on every basis
vector of the 114-dimensional `P`, 180-dimensional `Q`, and 300-dimensional
equation-density wall saturations.  Hence left-null obstruction functionals
and forcing pairings transport exactly through the ambient wall chain map.

## 14. Triple-overlap core

Through layer 15, \(T_\lambda\) is quadratic in \(\lambda\).  The
three-chart intersection at parameters `0`, `1`, and `-1` is therefore the
subspace stable under every wall parameter.  Its exact dimensions are

\&#91;
\dim E^{\mathrm{core}}=68,
\qquad
\dim W^{\mathrm{core}}=206.
\&#93;

A single pairwise overlap has dimensions 89 and 216.  Thus 21 deformation
directions and 10 equation directions pass one overlap but fail the
triple-overlap test.

## 15. Operation commutator and cyclic parameter line

Transporting the maximal support-admissible layer-four source field across the
wall forces a layer-eleven bracket whose action contains nonzero `P` exponent
5 and `Q` exponent 9 terms.  The old layer-eleven windows omit both.  This is
an exact required adjacent-chart operation term.

For the `F_2` quotient `u=z^5`, a `k=4` wall parameter must have `C_5`
character four.  If it is treated as an invariant scalar, the first return to
the original character occurs only at wall order five.  Reconciling the bare
layer-seven wall with a layer-four associated-graded direction would also
require normal weight `-3`; the resulting necessary bidegree is `(-3,4 mod
5)`.  This is localized chart data, not ordinary fixed-chart gauge.


## 16. Parameter weight is necessary but not sufficient

Assigning weight \(w\) to the wall parameter changes the bookkeeping layer
from \(r=2k-1\) to \(r+w\).  If the bare source pair is left unchanged, its
ordinary weighted-divergence defect becomes

\&#91;
(fz^2)' +(r+w-5)gz^2=wz^{2-k}.
\&#93;

For `k=4` and target layer four, \(w=-3\), so the defect is

\&#91;
-3z^{-2}\ne0.
\&#93;

Thus reweighting alone cannot identify the bare wall tangent with a
\(D_4\)-kernel class.  Keeping \(f=2z^{-3}\) uniquely restores the layer-four
identity with

\&#91;
g=-2z^{-4}.
\&#93;

The resulting candidate associated-graded action is

\&#91;
a_4=6z^{-3}p+2z^{-2}p',
\qquad
b_4=10z^{-2}q+2z^{-1}q'.
\&#93;

It exits the old layer-four window through principal parts
`A={-3,-2,-1}`, `B={-2,-1}`.  A complete repair must construct the
Rees/Euler mechanism that produces this correction and match its tangent line
to the archived residual quotient.
</code></pre>

<a id="source-d6c38a4c865ab7c9"></a>

## `research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_OVERLAP_THEOREM.md`

<pre><code class="language-markdown">
# Exact wall-shear overlap and master-equation covariance

**Status:** exact ambient Laurent-jet theorem and degree-21 finite-window
calculation. This constructs a genuine transported-window chart pair. It does
not yet identify the complete-chain presentation stabilizer or prove that the
transported coefficient space is the intended monomial Newton chart.

## 1. Density transport

Let

\&#91;
t'=t(1+h),\qquad z'=z(1+h)^2,\qquad
h=\lambda t^{2k-1}z^{-k}.
\&#93;

For a coefficient density with pole order \(p\), define

\&#91;
T^{(p)}_{k,\lambda}(t^nz^j)
=
\sum_{q\ge0}
\binom{n-p+2j}{q}\lambda^q
t^{n+q(2k-1)}z^{j-qk}.
\&#93;

On any finite normal cutoff this is a finite exact sum. It satisfies

\&#91;
T^{(p)}_{k,\lambda}T^{(p)}_{k,\mu}
=
T^{(p)}_{k,\lambda+\mu},
\qquad
(T^{(p)}_{k,\lambda})^{-1}=T^{(p)}_{k,-\lambda}.
\&#93;

## 2. Exact nonlinear master covariance

Write

\&#91;
\mathcal R_{\alpha,\beta}(A,B)
=
\alpha AB_z-\beta A_zB
+t(A_zB_t-A_tB_z)-z^2.
\&#93;

The coefficient pairs \(A,B\) have pole orders \(\alpha,\beta\). The residual
is a coefficient density of pole order

\&#91;
\gamma=\alpha+\beta-1.
\&#93;

Exact pullback of the determinant two-form gives

\&#91;
\boxed{
\mathcal R_{\alpha,\beta}
\left(T^{(\alpha)}_{k,\lambda}A,
      T^{(\beta)}_{k,\lambda}B\right)
=
T^{(\gamma)}_{k,\lambda}
\mathcal R_{\alpha,\beta}(A,B).
}
\&#93;

Differentiating at any base pair gives the full cumulative-jet chain map

\&#91;
D_{T(A,B)}\mathcal R\circ
\left(T^{(\alpha)}\oplus T^{(\beta)}\right)
=
T^{(\gamma)}\circ D_{(A,B)}\mathcal R.
\&#93;

This supplies the previously missing equation-space map for the ambient wall
overlap, including all lower-triangular normal-layer mixing.

## 3. A canonical transported-window chart pair

Let \(E_0\) be the archived full degree-21 coefficient window through layer
15 and let \(W_0\) be the complete support of its nonlinear master residual.
For nonzero \(\lambda\), put

\&#91;
E_\lambda=T_E(\lambda)E_0,\qquad
W_\lambda=T_W(\lambda)W_0.
\&#93;

Then

\&#91;
\mathcal R(E_\lambda)\subseteq W_\lambda
\&#93;

exactly. Thus \((E_0,W_0)\) and \((E_\lambda,W_\lambda)\) form a genuine
finite-dimensional ambient Laurent-jet chart pair.

The exact dimensions are:

| space | old dimension | minimal wall saturation | added |
| --- | ---: | ---: | ---: |
| \(P\)-coefficients | 61 | 114 | 53 |
| \(Q\)-coefficients | 125 | 180 | 55 |
| total deformation space \(E\) | 186 | 294 | 108 |
| equation density \(W\) | 257 | 300 | 43 |

For every tested nonzero parameter—and, by chainwise diagonal rescaling, for
every nonzero parameter—the old and transported spaces satisfy:

| space | intersection | sum | new independent directions |
| --- | ---: | ---: | ---: |
| \(P\) | 15 | 107 | 46 |
| \(Q\) | 74 | 176 | 51 |
| total \(E\) | 89 | 283 | 97 |
| \(W\) | 216 | 298 | 41 |

The deformation increment \(97=46+51\) is exactly the previously observed
first-order coefficient-wall exit rank. A single transported chart does not
span the whole orbit saturation: it misses 11 deformation coordinates and 2
equation coordinates that occur as independent second-order wall terms.
However,

\&#91;
\boxed{
E^{\mathrm{sat}}=E_0+E_1+E_{-1},
\qquad
W^{\mathrm{sat}}=W_0+W_1+W_{-1}.
}
\&#93;

This gives an exact three-chart finite overlap model.

## 4. Filtered conjugacy cannot lower seven to four

For \(k=4\), the infinitesimal generator has exact \(t\)-adic degree \(7\).
Let \(C\) be a filtration-preserving automorphism with filtration-preserving
inverse and invertible associated-graded map. If \(N\) has nonzero principal
symbol in degree seven, then

\&#91;
\sigma_7(CNC^{-1})
=
\operatorname{gr}(C)\sigma_7(N)\operatorname{gr}(C)^{-1}
\ne0.
\&#93;

Hence \(CNC^{-1}\) still has degree seven. Therefore the displayed wall shear
cannot become a normal layer-four tangent through a filtration-preserving
conjugacy. Any reconciliation must use a filtration-changing birational
coordinate map, assign degree \(-3\) to the wall parameter, or correct one of
the labels.

## 5. An explicit false obstruction removed by the wall arc

Take

\&#91;
A_0=z+\frac32z^2,\qquad B_0=z^2+z^3.
\&#93;

It satisfies

\&#91;
2A_0B_0'-3A_0'B_0=z^2.
\&#93;

The exact \(k=4\), \(\lambda=1\) wall transform through layer 15 is

\&#91;
A=A_0+3t^7z^{-2}+\frac32t^{14}z^{-6},
\&#93;

\&#91;
B=B_0+t^7(z^{-2}+3z^{-1})+3t^{14}z^{-5}.
\&#93;

The layer-seven correction lies in the kernel. At layer 14,

\&#91;
D_{14}(a_{14},b_{14})
=
-6z^{-5}+27z^{-4},
\&#93;

while the quadratic forcing from the layer-seven correction is

\&#91;
\Phi_{14}
=
6z^{-5}-27z^{-4}.
\&#93;

They cancel exactly. Setting the second wall correction to zero creates a
nonzero residual even though the full chart transition is an exact solution.
This is a small exact model of the logical error behind a
zero-new-parameter obstruction slice.

## 6. What remains

The construction solves the ambient coefficient and equation transport
problem. It does not yet determine:

- the intrinsic complete-chain fixed-presentation stabilizer;
- the intended adjacent monomial Newton window;
- the filtration-changing map, if any, connecting the public layer-four
  residual to the \(k=4\) wall;
- the actual `F_2` attachment matrices.

The next useful export is the real adjacent-chart normalization map. It can be
tested against the transported-window space above instead of discarding wall
overflow terms.


## 7. Dual and triple-overlap continuation

The exact obstruction-dual map is

\&#91;
U\epsilon_{m,l}
 =\sum_q\binom{p-m-2l-1}{q}\lambda^q
 \epsilon_{m-q(2k-1),l+qk},
\qquad U^\mathsf TT=I.
\&#93;

Forcing pairings and left-null obstruction spaces therefore transport exactly.

The pairwise deformation overlap has dimension 89, whereas the all-parameter
core detected by the charts `0`, `1`, and `-1` has dimension 68.  The
corresponding equation dimensions are 216 and 206.  Thus triple-overlap
compatibility imposes 21 additional deformation conditions and 10 additional
equation conditions beyond one pairwise transition.

The layer-four support-admissible field also acquires a compulsory
layer-eleven commutator term under the wall.  Finally, in the `F_2` gap-five
quotient the wall parameter is a character-four eigenparameter; scalar cyclic
descent sees its first return only at order five.
</code></pre>

<a id="source-c47dc9e578777d37"></a>

## `research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_REES_FLOW.md`

<pre><code class="language-markdown">
# The corrected layer-four candidate is a Kummer Hamiltonian flow

**Status:** exact coordinate conversion and formal-flow calculation. This
strengthens the Rees-weight audit. It does not construct the missing
complete-chain chart.

## 1. Back to the original affine coordinates

The degree-21 coordinate dictionary is

\&#91;
t=x^4y,\qquad z=x^7y^2.
\&#93;

The unique corrected layer-four pair from the Rees-weight audit is

\&#91;
V=t^4\left(2z^{-3}\partial_z-2z^{-4}t\partial_t\right).
\&#93;

Writing

\&#91;
u=\frac{\delta t}{t},\qquad v=\frac{\delta z}{z},
\&#93;

the logarithmic coordinate equations are

\&#91;
4\frac{\delta x}{x}+\frac{\delta y}{y}=u,
\qquad
7\frac{\delta x}{x}+2\frac{\delta y}{y}=v.
\&#93;

Here

\&#91;
u=-2M,\qquad v=2M,\qquad
M=t^4z^{-4}=x^{-12}y^{-4}.
\&#93;

Consequently

\&#91;
\boxed{
V=-6x^{-11}y^{-4}\partial_x
  +22x^{-12}y^{-3}\partial_y.
}
\&#93;

Its ordinary divergence is zero.

## 2. Hamiltonian form

With the convention

\&#91;
D_H=H_y\partial_x-H_x\partial_y,
\&#93;

the field is Hamiltonian for

\&#91;
\boxed{H=2x^{-11}y^{-3}.}
\&#93;

On Laurent monomials,

\&#91;
V(x^ay^b)=(-6a+22b)x^{a-12}y^{b-4}.
\&#93;

In particular,

\&#91;
V(H)=0,
\qquad
V(M)=-16M^2.
\&#93;

The iterates of \(x\) have nonzero leading coefficient

\&#91;
V^n(x)=
\left(\prod_{j=0}^{n-1}(-6-16j)\right)
 x^{1-12n}y^{-4n},
\&#93;

so this Laurent derivation is not locally nilpotent.

## 3. Exact formal flow

Solving \(\dot M=-16M^2\) gives

\&#91;
M_s=\frac{M}{1+16sM}.
\&#93;

Put

\&#91;
R^8=1+16sM.
\&#93;

Then the exact flow is

\&#91;
\boxed{
 x_s=xR^{-3},\qquad
 y_s=yR^{11},\qquad
 t_s=tR^{-1},\qquad
 z_s=zR.
}
\&#93;

As a formal power series in \(s\), the binomial root \(R\) exists uniquely
with constant term one. Thus the corrected candidate is formally integrable.


## 4. The degree-eight quotient linearizes the flow

Set

\&#91;
\boxed{
H=2x^{-11}y^{-3}=\frac{2}{tz},
\qquad
Q=x^{12}y^4=\left(\frac zt\right)^4=M^{-1}.
}
\&#93;

Then

\&#91;
V(H)=0,
\qquad
V(Q)=16.
\&#93;

Thus on the quotient function field,

\&#91;
\boxed{H_s=H,\qquad Q_s=Q+16s.}
\&#93;

The exponent matrix of the monomial map \((x,y)\mapsto(H/2,Q)\) is

\&#91;
\begin{pmatrix}
-11&amp;-3\\
12&amp;4
\end{pmatrix},
\&#93;

with determinant \(-8\). Hence

\&#91;
&#91;K(x,y):K(H,Q)&#93;=8
\&#93;

generically. Explicitly,

\&#91;
x^8=\frac{16}{H^4Q^3},
\qquad
y^8=\frac{H^{12}Q^{11}}{4096}.
\&#93;

The Kummer root in the original flow is precisely

\&#91;
R^8=\frac{Q+16s}{Q}.
\&#93;

So the corrected field is not mysterious: it is an ordinary translation on
a degree-eight monomial quotient chart. The eighth-root extension is exactly
the inverse lattice-index obstruction to lifting that translation back to
\((x,y)\).


In the adjacent blowdown variables used by the stored proposition,

\&#91;
u=(xy)^{-1},\qquad v=y,
\&#93;

these quotient coordinates are

\&#91;
H=2u^{11}v^8,
\qquad
Q=u^{-12}v^{-8}.
\&#93;

Therefore

\&#91;
\boxed{K(H,Q)=K(u,v^8).}
\&#93;

The degree-eight quotient is exactly the \(\mu_8\)-quotient of the adjacent
blowdown chart.  The corrected field descends to this quotient, while the bare
`k=4` operation is the translation \(v\mapsto v+s\), which is not the same
quotient operation.  This isolates a precise missing lift in the public
correspondence claim.


Because

\&#91;
Q=\left(\frac zt\right)^4
\&#93;

has normal \(t\)-exponent \(-4\), translation in \(Q\) naturally has the
missing layer-four label.  This gives the strongest current repaired
correspondence candidate:

&gt; match the stored layer-four residual to the pullback of the quotient
&gt; translation \(Q\mapsto Q+16s\), not to the bare layer-seven translation
&gt; \(v\mapsto v+s\).

The scalar `16` is a parameter normalization.  What remains is an exact
coefficientwise comparison with the archived residual representative.

## 5. It is not a same-field rational chart operation

Over \(K(x,y,s)\), the radicand is

\&#91;
1+16sx^{-12}y^{-4}.
\&#93;

After multiplication by the Laurent unit \(x^{12}y^4\), its non-monomial
factor is the prime

\&#91;
x^{12}y^4+16s.
\&#93;

The radicand has valuation one at this prime. An eighth power has valuation
divisible by eight. Therefore the radicand is not an eighth power in
\(K(x,y,s)\), and the generic flow requires the degree-eight Kummer
extension

\&#91;
K(x,y,s)\subset K(x,y,s)(R),
\qquad R^8=1+16sM.
\&#93;

Hence the corrected field cannot be identified with an ordinary rational
one-parameter coordinate change on the same function field.

## 6. Compatibility with the F2 cyclic character

For the `F_2` quotient, \(z\) has `C_5` character one and the wall parameter
has character four. Both \(H\) and \(Q\) have character four, so the quotient
translation \(Q\mapsto Q+16s\) is equivariant. Since

\&#91;
M=t^4z^{-4}
\&#93;

has character one, \(sM\) is invariant modulo five. The Kummer radicand and
root equation are therefore compatible with cyclic descent. The independent
eighth-root extension nevertheless remains.

This gives a sharper alternative:

- the bare `k=4` wall is the polynomial translation \(y\mapsto y+s\) and
  occurs at normal layer seven;
- the corrected layer-four candidate is Hamiltonian and formally integrable,
  but algebraically lives on an eighth-root Kummer cover;
- identifying it with a complete-chain rechart requires a root-stack or
  filtration-changing construction, not a same-field polynomial wall shear.
</code></pre>

<a id="source-b52f970145b7946d"></a>

## `research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_jet_transport_audit.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Build the exact first-order k=4 transport on the stored full support.

For a normal basis monomial

    e_(n,j) = t^(n-alpha) z^j,

the derivative at ``lambda=0`` of ``Y -&gt; Y+lambda X^(-k)`` is

    N_k e_(n,j) = (n-alpha+2j) e_(n+2k-1,j-k).

This script applies that formula to every basis monomial in the archived full
support.  It separates internal entries, exits through a coefficient-window
wall, terms beyond the finite stored cutoff, and zero entries.  It also reports
the powers of the projected sparse operator on the old window.

The ambient exact transport is ``exp(lambda N_k)``: after each application the
coefficient drops by one, so

    N_k^q e_(n,j)
      = (n-alpha+2j)_(q) e_(n+q(2k-1),j-qk),

where ``(a)_(q)`` is the falling factorial.  The projected old-window matrix is
a diagnostic only; a genuine chart transition needs the adjacent support
window rather than discarding the reported overflow.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Mapping, Sequence


BasisElement = tuple&#91;int, int&#93;


def full_layers(document: Mapping&#91;str, Any&#93;) -&gt; dict&#91;int, Mapping&#91;str, Any&#93;&#93;:
    cases = document.get("cases")
    if not isinstance(cases, list):
        raise ValueError("support document has no cases list")
    full = next(
        (case for case in cases if isinstance(case, Mapping) and case.get("label") == "full"),
        None,
    )
    if not isinstance(full, Mapping):
        raise ValueError("support document has no full case")
    layers = full.get("layers")
    if not isinstance(layers, list):
        raise ValueError("full support case has no layers list")
    result: dict&#91;int, Mapping&#91;str, Any&#93;&#93; = {}
    for layer in layers:
        if not isinstance(layer, Mapping) or not isinstance(layer.get("r"), int):
            raise ValueError("invalid full support layer")
        result&#91;int(layer&#91;"r"&#93;)&#93; = layer
    return result


def component_supports(
    layers: Mapping&#91;int, Mapping&#91;str, Any&#93;&#93;, component: str
) -&gt; dict&#91;int, list&#91;int&#93;&#93;:
    if component not in {"P", "Q"}:
        raise ValueError("component must be P or Q")
    key = "a_support" if component == "P" else "b_support"
    result: dict&#91;int, list&#91;int&#93;&#93; = {}
    for normal_layer, layer in sorted(layers.items()):
        values = layer.get(key, &#91;&#93;)
        if not isinstance(values, list) or not all(
            isinstance(value, int) and not isinstance(value, bool) for value in values
        ):
            raise ValueError(f"invalid {key} at layer {normal_layer}")
        result&#91;normal_layer&#93; = list(values)
    return result


def projected_operator(
    supports: Mapping&#91;int, Sequence&#91;int&#93;&#93;, pole_order: int, k: int
) -&gt; tuple&#91;list&#91;BasisElement&#93;, dict&#91;BasisElement, tuple&#91;BasisElement, int&#93;&#93;&#93;:
    basis = &#91;
        (normal_layer, exponent)
        for normal_layer in sorted(supports)
        for exponent in supports&#91;normal_layer&#93;
    &#93;
    basis_set = set(basis)
    shift = 2 * k - 1
    operator: dict&#91;BasisElement, tuple&#91;BasisElement, int&#93;&#93; = {}
    for normal_layer, exponent in basis:
        coefficient = normal_layer - pole_order + 2 * exponent
        target = (normal_layer + shift, exponent - k)
        if coefficient != 0 and target in basis_set:
            operator&#91;(normal_layer, exponent)&#93; = (target, coefficient)
    return basis, operator


def projected_power_entries(
    basis: Sequence&#91;BasisElement&#93;,
    operator: Mapping&#91;BasisElement, tuple&#91;BasisElement, int&#93;&#93;,
    power: int,
) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    if power &lt; 1:
        raise ValueError("power must be positive")
    entries: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;
    for source in basis:
        current = source
        coefficient = 1
        for _ in range(power):
            image = operator.get(current)
            if image is None:
                break
            current, factor = image
            coefficient *= factor
        else:
            entries.append(
                {
                    "source_layer": source&#91;0&#93;,
                    "source_exponent": source&#91;1&#93;,
                    "target_layer": current&#91;0&#93;,
                    "target_exponent": current&#91;1&#93;,
                    "coefficient": coefficient,
                }
            )
    return entries


def component_report(
    supports: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    *,
    component: str,
    pole_order: int,
    k: int,
) -&gt; dict&#91;str, Any&#93;:
    maximum_layer = max(supports)
    shift = 2 * k - 1
    internal: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;
    window_exit: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;
    beyond_cutoff: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;
    zero: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;

    for source_layer in sorted(supports):
        for source_exponent in supports&#91;source_layer&#93;:
            coefficient = source_layer - pole_order + 2 * source_exponent
            target_layer = source_layer + shift
            target_exponent = source_exponent - k
            entry = {
                "source_layer": source_layer,
                "source_exponent": source_exponent,
                "coefficient": coefficient,
                "target_layer": target_layer,
                "target_exponent": target_exponent,
            }
            if coefficient == 0:
                zero.append(entry)
            elif target_layer &gt; maximum_layer:
                beyond_cutoff.append(entry)
            elif target_exponent in supports.get(target_layer, &#91;&#93;):
                internal.append(entry)
            else:
                window_exit.append(entry)

    basis, operator = projected_operator(supports, pole_order, k)
    projected_powers: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;
    power = 1
    while True:
        entries = projected_power_entries(basis, operator, power)
        projected_powers.append(
            {
                "power": power,
                "rank": len(entries),
                "entries": entries,
            }
        )
        if not entries:
            break
        power += 1
        if power &gt; len(basis) + 1:
            raise AssertionError("projected operator did not become nilpotent")

    def layer_counts(entries: Sequence&#91;Mapping&#91;str, Any&#93;&#93;) -&gt; list&#91;dict&#91;str, int&#93;&#93;:
        counts = Counter(int(entry&#91;"source_layer"&#93;) for entry in entries)
        return &#91;
            {"source_layer": normal_layer, "count": counts&#91;normal_layer&#93;}
            for normal_layer in sorted(counts)
        &#93;

    return {
        "component": component,
        "pole_order": pole_order,
        "domain_dimension": len(basis),
        "maximum_stored_layer": maximum_layer,
        "first_order_internal_rank": len(internal),
        "first_order_internal_entries": internal,
        "window_exit_count": len(window_exit),
        "window_exit_by_source_layer": layer_counts(window_exit),
        "window_exit_entries": window_exit,
        "beyond_cutoff_count": len(beyond_cutoff),
        "beyond_cutoff_by_source_layer": layer_counts(beyond_cutoff),
        "beyond_cutoff_entries": beyond_cutoff,
        "zero_entry_count": len(zero),
        "zero_entries": zero,
        "projected_operator_powers": projected_powers,
        "projected_nilpotence_index": projected_powers&#91;-1&#93;&#91;"power"&#93;,
    }


def analyze(document: Mapping&#91;str, Any&#93;, k: int) -&gt; dict&#91;str, Any&#93;:
    if not isinstance(k, int) or isinstance(k, bool) or k &lt; 1:
        raise ValueError("k must be a positive integer")
    layers = full_layers(document)
    p_report = component_report(
        component_supports(layers, "P"),
        component="P",
        pole_order=2,
        k=k,
    )
    q_report = component_report(
        component_supports(layers, "Q"),
        component="Q",
        pole_order=3,
        k=k,
    )
    return {
        "schema_version": 1,
        "name": "degree-21 full-window infinitesimal wall transport",
        "k": k,
        "normal_layer_shift": 2 * k - 1,
        "basis_formula": (
            "N_k e_(n,j)=(n-alpha+2j)e_(n+2k-1,j-k)"
        ),
        "ambient_exponential_formula": (
            "F_lambda^*=exp(lambda N_k), with "
            "N_k^q e_(n,j)=(n-alpha+2j)_(q)e_(n+q(2k-1),j-qk)"
        ),
        "components": &#91;p_report, q_report&#93;,
        "total_domain_dimension": (
            p_report&#91;"domain_dimension"&#93; + q_report&#91;"domain_dimension"&#93;
        ),
        "total_first_order_internal_rank": (
            p_report&#91;"first_order_internal_rank"&#93;
            + q_report&#91;"first_order_internal_rank"&#93;
        ),
        "total_window_exit_count": (
            p_report&#91;"window_exit_count"&#93; + q_report&#91;"window_exit_count"&#93;
        ),
        "total_beyond_cutoff_count": (
            p_report&#91;"beyond_cutoff_count"&#93; + q_report&#91;"beyond_cutoff_count"&#93;
        ),
        "total_zero_entry_count": (
            p_report&#91;"zero_entry_count"&#93; + q_report&#91;"zero_entry_count"&#93;
        ),
        "interpretation": (
            "The internal matrix is only the projection to the old fixed-chart "
            "window. The window-exit entries must be transported into an "
            "explicit adjacent-chart basis; deleting them is not a chart "
            "correspondence theorem."
        ),
    }


def main(argv: Sequence&#91;str&#93; | None = None) -&gt; int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("supports", type=Path)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)

    try:
        document = json.loads(args.supports.read_text(encoding="utf-8"))
        if not isinstance(document, Mapping):
            raise ValueError("support input must be a JSON object")
        result = analyze(document, args.k)
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-054e38ce26bf5835"></a>

## `research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_overlap_saturation.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Construct the minimal finite transported-window overlap for degree 21.

The old full-support coefficient spaces are closed under neither the ``k=4``
wall generator nor its exponential.  This program constructs the smallest
layer-15 Laurent support containing the old space and closed under that
generator.  It then compares the old chart with one transported chart and
with the two opposite transported charts.

All ranks are exact over Q and use only the Python standard library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

from wall_shear_master_covariance import generalized_binomial

BasisElement = tuple&#91;int, int&#93;
Support = dict&#91;int, list&#91;int&#93;&#93;
Matrix = list&#91;list&#91;Fraction&#93;&#93;


def full_support_fixture() -&gt; dict&#91;str, Support&#93;:
    p_supports: Support = {
        0: list(range(1, 9)),
        1: list(range(1, 9)),
        2: list(range(0, 9)),
    }
    for layer in range(3, 11):
        p_supports&#91;layer&#93; = list(range(0, 11 - layer))
    for layer in range(11, 16):
        p_supports&#91;layer&#93; = &#91;&#93;

    q_supports: Support = {
        0: list(range(2, 13)),
        1: list(range(2, 13)),
        2: list(range(1, 13)),
        3: list(range(0, 13)),
    }
    for layer in range(4, 16):
        q_supports&#91;layer&#93; = list(range(0, 16 - layer))
    return {"P": p_supports, "Q": q_supports}


def basis_from_support(support: Mapping&#91;int, Sequence&#91;int&#93;&#93;) -&gt; list&#91;BasisElement&#93;:
    return sorted(
        (layer, power)
        for layer, powers in support.items()
        for power in powers
    )


def saturate(
    support: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    *,
    pole_order: int,
    k: int,
    cutoff: int,
) -&gt; list&#91;BasisElement&#93;:
    shift = 2 * k - 1
    result = set(basis_from_support(support))
    while True:
        additions: set&#91;BasisElement&#93; = set()
        for layer, power in result:
            coefficient = layer - pole_order + 2 * power
            target = (layer + shift, power - k)
            if coefficient and target&#91;0&#93; &lt;= cutoff:
                additions.add(target)
        new = additions - result
        if not new:
            return sorted(result)
        result.update(new)


def matrix_rank(matrix: Matrix) -&gt; int:
    if not matrix:
        return 0
    rows = &#91;row&#91;:&#93; for row in matrix&#93;
    columns = len(rows&#91;0&#93;)
    if any(len(row) != columns for row in rows):
        raise ValueError("ragged matrix")
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, len(rows)) if rows&#91;row&#93;&#91;column&#93;),
            None,
        )
        if pivot is None:
            continue
        rows&#91;pivot_row&#93;, rows&#91;pivot&#93; = rows&#91;pivot&#93;, rows&#91;pivot_row&#93;
        scale = rows&#91;pivot_row&#93;&#91;column&#93;
        rows&#91;pivot_row&#93; = &#91;value / scale for value in rows&#91;pivot_row&#93;&#93;
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            factor = rows&#91;row&#93;&#91;column&#93;
            if factor:
                rows&#91;row&#93; = &#91;
                    value - factor * pivot_value
                    for value, pivot_value in zip(rows&#91;row&#93;, rows&#91;pivot_row&#93;)
                &#93;
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def horizontal_join(left: Matrix, right: Matrix) -&gt; Matrix:
    if len(left) != len(right):
        raise ValueError("row counts do not agree")
    return &#91;a + b for a, b in zip(left, right)&#93;


def external_transport_matrix(
    old_basis: Sequence&#91;BasisElement&#93;,
    saturated_basis: Sequence&#91;BasisElement&#93;,
    *,
    pole_order: int,
    k: int,
    parameter: Fraction,
    cutoff: int,
) -&gt; tuple&#91;list&#91;BasisElement&#93;, Matrix&#93;:
    old_set = set(old_basis)
    external = &#91;element for element in saturated_basis if element not in old_set&#93;
    external_index = {element: index for index, element in enumerate(external)}
    matrix = &#91;
        &#91;Fraction(0) for _ in range(len(old_basis))&#93;
        for _ in range(len(external))
    &#93;
    shift = 2 * k - 1
    for column, (layer, power) in enumerate(old_basis):
        wall_order = 1
        while layer + wall_order * shift &lt;= cutoff:
            target = (
                layer + wall_order * shift,
                power - wall_order * k,
            )
            coefficient = generalized_binomial(
                layer - pole_order + 2 * power,
                wall_order,
            )
            if target in external_index and coefficient:
                matrix&#91;external_index&#91;target&#93;&#93;&#91;column&#93; += (
                    coefficient * parameter**wall_order
                )
            wall_order += 1
    return external, matrix


def rational_text(value: Fraction) -&gt; str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def matrix_digest(matrix: Matrix) -&gt; str:
    payload = &#91;
        &#91;rational_text(value) for value in row&#93;
        for row in matrix
    &#93;
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":"), sort_keys=False).encode()
    ).hexdigest()


def added_by_layer(
    old_basis: Sequence&#91;BasisElement&#93;,
    saturated_basis: Sequence&#91;BasisElement&#93;,
) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    old = set(old_basis)
    grouped: defaultdict&#91;int, list&#91;int&#93;&#93; = defaultdict(list)
    for layer, power in saturated_basis:
        if (layer, power) not in old:
            grouped&#91;layer&#93;.append(power)
    return &#91;
        {"layer": layer, "z_exponents": sorted(powers), "count": len(powers)}
        for layer, powers in sorted(grouped.items())
    &#93;


def analyze_space(
    name: str,
    support: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    *,
    pole_order: int,
    k: int,
    cutoff: int,
) -&gt; dict&#91;str, Any&#93;:
    old_basis = basis_from_support(support)
    saturated_basis = saturate(
        support,
        pole_order=pole_order,
        k=k,
        cutoff=cutoff,
    )
    external, plus = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(1),
        cutoff=cutoff,
    )
    _, minus = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(-1),
        cutoff=cutoff,
    )
    _, twice = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(2),
        cutoff=cutoff,
    )
    external_rank = matrix_rank(plus)
    if matrix_rank(twice) != external_rank:
        raise AssertionError("nonzero wall parameters changed the overlap rank")
    opposite_rank = matrix_rank(horizontal_join(plus, minus))

    old_dimension = len(old_basis)
    saturated_dimension = len(saturated_basis)
    sum_dimension = old_dimension + external_rank
    intersection_dimension = old_dimension - external_rank
    opposite_span_dimension = old_dimension + opposite_rank

    return {
        "name": name,
        "pole_order": pole_order,
        "old_dimension": old_dimension,
        "saturated_dimension": saturated_dimension,
        "added_dimension": saturated_dimension - old_dimension,
        "one_nonzero_transported_chart": {
            "external_increment": external_rank,
            "intersection_dimension": intersection_dimension,
            "sum_dimension": sum_dimension,
            "saturation_defect": saturated_dimension - sum_dimension,
            "rank_constant_for_nonzero_parameters_verified_at": &#91;"1", "2", "-1"&#93;,
        },
        "base_plus_opposite_charts": {
            "span_dimension": opposite_span_dimension,
            "spans_minimal_saturation": (
                opposite_span_dimension == saturated_dimension
            ),
        },
        "added_basis_by_layer": added_by_layer(old_basis, saturated_basis),
        "external_basis_dimension": len(external),
        "positive_external_matrix_sha256": matrix_digest(plus),
        "negative_external_matrix_sha256": matrix_digest(minus),
    }


def master_support(
    p_supports: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    q_supports: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    *,
    alpha: int,
    beta: int,
    cutoff: int,
) -&gt; Support:
    result: defaultdict&#91;int, set&#91;int&#93;&#93; = defaultdict(set)
    for left_layer, left_powers in p_supports.items():
        for right_layer, right_powers in q_supports.items():
            layer = left_layer + right_layer
            if layer &gt; cutoff:
                continue
            for left_power in left_powers:
                for right_power in right_powers:
                    coefficient = (
                        alpha * right_power
                        - beta * left_power
                        + right_layer * left_power
                        - left_layer * right_power
                    )
                    if coefficient:
                        result&#91;layer&#93;.add(left_power + right_power - 1)
    result&#91;0&#93;.add(2)
    return {
        layer: sorted(powers)
        for layer, powers in sorted(result.items())
    }


def support_summary(support: Mapping&#91;int, Sequence&#91;int&#93;&#93;) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    return &#91;
        {
            "layer": layer,
            "minimum_exponent": min(powers) if powers else None,
            "maximum_exponent": max(powers) if powers else None,
            "dimension": len(powers),
            "contiguous": (
                not powers
                or len(powers) == max(powers) - min(powers) + 1
            ),
        }
        for layer, powers in sorted(support.items())
    &#93;


def analyze(*, k: int = 4, cutoff: int = 15) -&gt; dict&#91;str, Any&#93;:
    alpha, beta = 2, 3
    supports = full_support_fixture()
    p_report = analyze_space(
        "P coefficients",
        supports&#91;"P"&#93;,
        pole_order=alpha,
        k=k,
        cutoff=cutoff,
    )
    q_report = analyze_space(
        "Q coefficients",
        supports&#91;"Q"&#93;,
        pole_order=beta,
        k=k,
        cutoff=cutoff,
    )
    equation_support = master_support(
        supports&#91;"P"&#93;,
        supports&#91;"Q"&#93;,
        alpha=alpha,
        beta=beta,
        cutoff=cutoff,
    )
    equation_report = analyze_space(
        "master-equation density",
        equation_support,
        pole_order=alpha + beta - 1,
        k=k,
        cutoff=cutoff,
    )

    deformation_old = p_report&#91;"old_dimension"&#93; + q_report&#91;"old_dimension"&#93;
    deformation_saturated = (
        p_report&#91;"saturated_dimension"&#93; + q_report&#91;"saturated_dimension"&#93;
    )
    deformation_external = (
        p_report&#91;"one_nonzero_transported_chart"&#93;&#91;"external_increment"&#93;
        + q_report&#91;"one_nonzero_transported_chart"&#93;&#91;"external_increment"&#93;
    )
    deformation_intersection = (
        p_report&#91;"one_nonzero_transported_chart"&#93;&#91;"intersection_dimension"&#93;
        + q_report&#91;"one_nonzero_transported_chart"&#93;&#91;"intersection_dimension"&#93;
    )
    deformation_sum = deformation_old + deformation_external
    opposite_span = (
        p_report&#91;"base_plus_opposite_charts"&#93;&#91;"span_dimension"&#93;
        + q_report&#91;"base_plus_opposite_charts"&#93;&#91;"span_dimension"&#93;
    )

    report = {
        "schema_version": 1,
        "name": "degree-21 k=4 transported-window overlap",
        "alpha": alpha,
        "beta": beta,
        "k": k,
        "normal_layer_shift": 2 * k - 1,
        "cutoff": cutoff,
        "interpretation": (
            "E_lambda=T_E(lambda)E_0 and W_lambda=T_W(lambda)W_0 form an "
            "exact ambient Laurent-jet chart pair. They are not yet proved "
            "to be the complete-chain monomial adjacent chart or its "
            "presentation stabilizer."
        ),
        "deformation_space": {
            "old_dimension": deformation_old,
            "saturated_dimension": deformation_saturated,
            "added_dimension": deformation_saturated - deformation_old,
            "one_nonzero_transported_chart": {
                "external_increment": deformation_external,
                "intersection_dimension": deformation_intersection,
                "sum_dimension": deformation_sum,
                "saturation_defect": deformation_saturated - deformation_sum,
            },
            "base_plus_opposite_charts": {
                "span_dimension": opposite_span,
                "spans_minimal_saturation": (
                    opposite_span == deformation_saturated
                ),
            },
            "components": &#91;p_report, q_report&#93;,
        },
        "equation_space": equation_report,
        "old_equation_support": support_summary(equation_support),
        "filtered_conjugacy_consequence": {
            "principal_shift": 2 * k - 1,
            "statement": (
                "Conjugation by a filtration-preserving automorphism with "
                "invertible associated graded map preserves this principal "
                "shift. For k=4 it cannot produce a layer-four tangent."
            ),
        },
    }

    expected = {
        "deformation_old": 186,
        "deformation_saturated": 294,
        "deformation_external": 97,
        "deformation_intersection": 89,
        "deformation_sum": 283,
        "equation_old": 257,
        "equation_saturated": 300,
        "equation_external": 41,
        "equation_intersection": 216,
        "equation_sum": 298,
    }
    actual = {
        "deformation_old": deformation_old,
        "deformation_saturated": deformation_saturated,
        "deformation_external": deformation_external,
        "deformation_intersection": deformation_intersection,
        "deformation_sum": deformation_sum,
        "equation_old": equation_report&#91;"old_dimension"&#93;,
        "equation_saturated": equation_report&#91;"saturated_dimension"&#93;,
        "equation_external": equation_report&#91;
            "one_nonzero_transported_chart"
        &#93;&#91;"external_increment"&#93;,
        "equation_intersection": equation_report&#91;
            "one_nonzero_transported_chart"
        &#93;&#91;"intersection_dimension"&#93;,
        "equation_sum": equation_report&#91;
            "one_nonzero_transported_chart"
        &#93;&#91;"sum_dimension"&#93;,
    }
    if k == 4 and cutoff == 15 and actual != expected:
        raise AssertionError({"expected": expected, "actual": actual})
    return report


def main(argv: Sequence&#91;str&#93; | None = None) -&gt; int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--cutoff", type=int, default=15)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)
    report = analyze(k=args.k, cutoff=args.cutoff)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-2be4880ec062eadd"></a>

## `research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_triple_overlap.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact pairwise and triple-overlap structure of the k=4 wall atlas.

Through normal layer 15, the k=4 transport has degree at most two in the wall
parameter because its layer shift is seven.  Thus

    T_lambda = I + lambda*N + lambda^2*N^2/2.

A vector in the old window and in two distinct nonzero transported windows is
therefore in the old window for every wall parameter exactly when the
external parts of both ``N`` and ``N^2`` vanish.  This module computes that
stable all-parameter core for the stored degree-21 P, Q, and equation windows.

The calculation distinguishes two ranks:

* new ambient target coordinates generated by N and N^2;
* independent source constraints imposed by requiring those external terms
  to vanish.

They need not agree because different source combinations may hit the same
external coordinate.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

from degree21_k4_overlap_saturation import (
    basis_from_support,
    external_transport_matrix,
    full_support_fixture,
    horizontal_join,
    master_support,
    matrix_rank,
    saturate,
)
from wall_shear_master_covariance import generalized_binomial

BasisElement = tuple&#91;int, int&#93;
Matrix = list&#91;list&#91;Fraction&#93;&#93;


def vertical_join(top: Matrix, bottom: Matrix) -&gt; Matrix:
    if top and bottom and len(top&#91;0&#93;) != len(bottom&#91;0&#93;):
        raise ValueError("column counts do not agree")
    return &#91;*top, *bottom&#93;


def power_external_matrix(
    old_basis: Sequence&#91;BasisElement&#93;,
    saturated_basis: Sequence&#91;BasisElement&#93;,
    *,
    pole_order: int,
    k: int,
    power: int,
    cutoff: int,
) -&gt; Matrix:
    old_set = set(old_basis)
    external = &#91;item for item in saturated_basis if item not in old_set&#93;
    external_index = {item: index for index, item in enumerate(external)}
    matrix: Matrix = &#91;
        &#91;Fraction(0) for _ in range(len(old_basis))&#93;
        for _ in range(len(external))
    &#93;
    shift = 2 * k - 1
    for column, (layer, exponent) in enumerate(old_basis):
        target = (layer + power * shift, exponent - power * k)
        if target not in external_index or target&#91;0&#93; &gt; cutoff:
            continue
        coefficient = Fraction(1)
        initial = layer - pole_order + 2 * exponent
        for index in range(power):
            coefficient *= initial - index
        if coefficient:
            matrix&#91;external_index&#91;target&#93;&#93;&#91;column&#93; = coefficient
    return matrix


def full_orbit_safe_basis(
    old_basis: Sequence&#91;BasisElement&#93;,
    *,
    pole_order: int,
    k: int,
    cutoff: int,
) -&gt; list&#91;BasisElement&#93;:
    old_set = set(old_basis)
    shift = 2 * k - 1
    result: list&#91;BasisElement&#93; = &#91;&#93;
    for layer, exponent in old_basis:
        initial = layer - pole_order + 2 * exponent
        power = 1
        coefficient = Fraction(initial)
        safe = True
        while layer + power * shift &lt;= cutoff:
            if coefficient and (
                layer + power * shift,
                exponent - power * k,
            ) not in old_set:
                safe = False
                break
            power += 1
            coefficient *= initial - (power - 1)
        if safe:
            result.append((layer, exponent))
    return result


def by_layer(basis: Sequence&#91;BasisElement&#93;) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    layers: dict&#91;int, list&#91;int&#93;&#93; = {}
    for layer, exponent in basis:
        layers.setdefault(layer, &#91;&#93;).append(exponent)
    return &#91;
        {
            "layer": layer,
            "z_exponents": sorted(exponents),
            "dimension": len(exponents),
        }
        for layer, exponents in sorted(layers.items())
    &#93;


def component_report(
    name: str,
    support: Mapping&#91;int, Sequence&#91;int&#93;&#93;,
    *,
    pole_order: int,
    k: int,
    cutoff: int,
) -&gt; dict&#91;str, Any&#93;:
    old_basis = basis_from_support(support)
    saturated_basis = saturate(
        support,
        pole_order=pole_order,
        k=k,
        cutoff=cutoff,
    )
    _, pair_matrix_one = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(1),
        cutoff=cutoff,
    )
    _, pair_matrix_two = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(2),
        cutoff=cutoff,
    )
    _, pair_matrix_minus = external_transport_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        parameter=Fraction(-1),
        cutoff=cutoff,
    )
    first = power_external_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        power=1,
        cutoff=cutoff,
    )
    second = power_external_matrix(
        old_basis,
        saturated_basis,
        pole_order=pole_order,
        k=k,
        power=2,
        cutoff=cutoff,
    )
    first_constraint_rank = matrix_rank(first)
    all_constraint_rank = matrix_rank(vertical_join(first, second))
    first_target_rank = first_constraint_rank
    all_target_rank = matrix_rank(horizontal_join(first, second))
    pairwise_rank = matrix_rank(pair_matrix_one)
    if not (
        matrix_rank(pair_matrix_two)
        == matrix_rank(pair_matrix_minus)
        == pairwise_rank
    ):
        raise AssertionError("pairwise overlap rank depends on nonzero parameter")

    pairwise_dimension = len(old_basis) - pairwise_rank
    stable_core_dimension = len(old_basis) - all_constraint_rank
    safe_basis = full_orbit_safe_basis(
        old_basis,
        pole_order=pole_order,
        k=k,
        cutoff=cutoff,
    )
    if len(safe_basis) != stable_core_dimension:
        raise AssertionError(
            {
                "name": name,
                "safe_basis": len(safe_basis),
                "stable_core_dimension": stable_core_dimension,
            }
        )

    return {
        "name": name,
        "pole_order": pole_order,
        "old_dimension": len(old_basis),
        "saturated_dimension": len(saturated_basis),
        "transport_degree_in_lambda": 2,
        "pairwise_overlap_dimension": pairwise_dimension,
        "stable_all_parameter_core_dimension": stable_core_dimension,
        "pairwise_only_dimension": pairwise_dimension - stable_core_dimension,
        "first_order_external_constraint_rank": first_constraint_rank,
        "second_order_incremental_constraint_rank": (
            all_constraint_rank - first_constraint_rank
        ),
        "total_stability_constraint_rank": all_constraint_rank,
        "first_order_new_target_rank": first_target_rank,
        "second_order_incremental_target_rank": (
            all_target_rank - first_target_rank
        ),
        "total_new_target_rank": all_target_rank,
        "stable_core_is_coordinate_span": True,
        "stable_core_basis_by_layer": by_layer(safe_basis),
        "three_chart_test": (
            "Membership in charts lambda=0,1,-1 is equivalent to membership "
            "in every transported chart through the stated cutoff."
        ),
    }


def analyze(*, k: int = 4, cutoff: int = 15) -&gt; dict&#91;str, Any&#93;:
    if 3 * (2 * k - 1) &lt;= cutoff:
        raise ValueError("this report assumes transport degree at most two")
    supports = full_support_fixture()
    equation_support = master_support(
        supports&#91;"P"&#93;,
        supports&#91;"Q"&#93;,
        alpha=2,
        beta=3,
        cutoff=cutoff,
    )
    p_report = component_report(
        "P coefficients",
        supports&#91;"P"&#93;,
        pole_order=2,
        k=k,
        cutoff=cutoff,
    )
    q_report = component_report(
        "Q coefficients",
        supports&#91;"Q"&#93;,
        pole_order=3,
        k=k,
        cutoff=cutoff,
    )
    w_report = component_report(
        "equation density",
        equation_support,
        pole_order=4,
        k=k,
        cutoff=cutoff,
    )

    deformation = {
        key: p_report&#91;key&#93; + q_report&#91;key&#93;
        for key in (
            "old_dimension",
            "saturated_dimension",
            "pairwise_overlap_dimension",
            "stable_all_parameter_core_dimension",
            "pairwise_only_dimension",
            "first_order_external_constraint_rank",
            "second_order_incremental_constraint_rank",
            "total_stability_constraint_rank",
            "first_order_new_target_rank",
            "second_order_incremental_target_rank",
            "total_new_target_rank",
        )
    }
    expected = {
        "old_dimension": 186,
        "saturated_dimension": 294,
        "pairwise_overlap_dimension": 89,
        "stable_all_parameter_core_dimension": 68,
        "pairwise_only_dimension": 21,
        "first_order_external_constraint_rank": 97,
        "second_order_incremental_constraint_rank": 21,
        "total_stability_constraint_rank": 118,
        "first_order_new_target_rank": 97,
        "second_order_incremental_target_rank": 11,
        "total_new_target_rank": 108,
    }
    if k == 4 and cutoff == 15 and deformation != expected:
        raise AssertionError({"expected": expected, "actual": deformation})

    return {
        "schema_version": 1,
        "name": "degree-21 k=4 pairwise and triple wall overlap",
        "k": k,
        "normal_layer_shift": 2 * k - 1,
        "cutoff": cutoff,
        "transport_polynomial": "T_lambda=I+lambda*N+lambda^2*N^2/2",
        "components": &#91;p_report, q_report&#93;,
        "deformation_space": deformation,
        "equation_space": w_report,
        "triple_overlap_theorem": (
            "Because the external component of T_lambda v is a polynomial "
            "of degree at most two, vanishing at lambda=0,1,-1 forces it to "
            "vanish identically.  Thus the three-chart intersection is the "
            "maximal old-window subspace stable under all wall parameters."
        ),
        "cocycle": (
            "On this stable core, T_(b-c) T_(a-b)=T_(a-c) for all chart "
            "parameters a,b,c, with exact inverse T_(-lambda)."
        ),
        "interpretation": (
            "A two-chart support check leaves 21 deformation directions and "
            "10 equation directions that fail the third-chart test.  Triple "
            "overlap compatibility is therefore a genuine additional gate, "
            "not a formal consequence of one transition square."
        ),
    }


def main(argv: Sequence&#91;str&#93; | None = None) -&gt; int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--cutoff", type=int, default=15)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)
    report = analyze(k=args.k, cutoff=args.cutoff)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-f8b6710dea6c05d9"></a>

## `research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/wall_shear_master_covariance.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact covariance of the normal-boundary master equation under wall shears.

For

    t' = t(1+h),  z' = z(1+h)^2,
    h = lambda * t^(2k-1) * z^(-k),

a coefficient density of pole order ``p`` is transported by

    T_p(t^n z^j)
      = sum_q binom(n-p+2j,q) lambda^q
          t^(n+q(2k-1)) z^(j-qk).

The determinant master residual has density pole order
``alpha + beta - 1``.  The module verifies, exactly over Q,

    R(T_alpha A, T_beta B)
      = T_(alpha+beta-1) R(A,B),

as well as the differentiated chain-map square and an explicit second-order
wall arc.  No computer-algebra dependency is required.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

Exponent = tuple&#91;int, int&#93;
Series = dict&#91;Exponent, Fraction&#93;


def q(value: Any) -&gt; Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, bool):
        raise TypeError("booleans are not rational coefficients")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise TypeError(f"unsupported rational coefficient {value!r}")


def scalar_text(value: Fraction) -&gt; str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def generalized_binomial(exponent: int, order: int) -&gt; Fraction:
    if order &lt; 0:
        return Fraction(0)
    value = Fraction(1)
    for index in range(order):
        value *= Fraction(exponent - index, index + 1)
    return value


def clean(series: Mapping&#91;Exponent, Fraction&#93;) -&gt; Series:
    return {key: value for key, value in series.items() if value}


def add(*series: Mapping&#91;Exponent, Fraction&#93;) -&gt; Series:
    result: defaultdict&#91;Exponent, Fraction&#93; = defaultdict(Fraction)
    for item in series:
        for key, value in item.items():
            result&#91;key&#93; += value
    return clean(result)


def scale(series: Mapping&#91;Exponent, Fraction&#93;, scalar: Fraction | int) -&gt; Series:
    scalar = q(scalar)
    return clean({key: scalar * value for key, value in series.items()})


def multiply(
    left: Mapping&#91;Exponent, Fraction&#93;,
    right: Mapping&#91;Exponent, Fraction&#93;,
    *,
    cutoff: int,
) -&gt; Series:
    result: defaultdict&#91;Exponent, Fraction&#93; = defaultdict(Fraction)
    for (left_layer, left_power), left_value in left.items():
        for (right_layer, right_power), right_value in right.items():
            layer = left_layer + right_layer
            if layer &lt;= cutoff:
                result&#91;(layer, left_power + right_power)&#93; += (
                    left_value * right_value
                )
    return clean(result)


def derivative_z(series: Mapping&#91;Exponent, Fraction&#93;) -&gt; Series:
    return clean(
        {
            (layer, power - 1): value * power
            for (layer, power), value in series.items()
            if power
        }
    )


def t_derivative(series: Mapping&#91;Exponent, Fraction&#93;) -&gt; Series:
    """Return ``t * partial_t(series)``."""

    return clean(
        {
            (layer, power): value * layer
            for (layer, power), value in series.items()
            if layer
        }
    )


def master(
    A: Mapping&#91;Exponent, Fraction&#93;,
    B: Mapping&#91;Exponent, Fraction&#93;,
    *,
    alpha: int,
    beta: int,
    cutoff: int,
) -&gt; Series:
    """The scalar master expression before subtracting ``Psi=z^2``."""

    return add(
        scale(multiply(A, derivative_z(B), cutoff=cutoff), alpha),
        scale(multiply(derivative_z(A), B, cutoff=cutoff), -beta),
        multiply(derivative_z(A), t_derivative(B), cutoff=cutoff),
        scale(
            multiply(t_derivative(A), derivative_z(B), cutoff=cutoff),
            -1,
        ),
    )


def residual(
    A: Mapping&#91;Exponent, Fraction&#93;,
    B: Mapping&#91;Exponent, Fraction&#93;,
    *,
    alpha: int,
    beta: int,
    cutoff: int,
) -&gt; Series:
    return add(
        master(A, B, alpha=alpha, beta=beta, cutoff=cutoff),
        {(0, 2): Fraction(-1)},
    )


def linearization(
    A: Mapping&#91;Exponent, Fraction&#93;,
    B: Mapping&#91;Exponent, Fraction&#93;,
    a: Mapping&#91;Exponent, Fraction&#93;,
    b: Mapping&#91;Exponent, Fraction&#93;,
    *,
    alpha: int,
    beta: int,
    cutoff: int,
) -&gt; Series:
    return add(
        master(a, B, alpha=alpha, beta=beta, cutoff=cutoff),
        master(A, b, alpha=alpha, beta=beta, cutoff=cutoff),
    )


def transport(
    series: Mapping&#91;Exponent, Fraction&#93;,
    *,
    pole_order: int,
    k: int,
    parameter: Fraction | int,
    cutoff: int,
) -&gt; Series:
    """Pull a primed coefficient density back to the unprimed wall chart."""

    if k &lt; 1:
        raise ValueError("k must be positive")
    parameter = q(parameter)
    shift = 2 * k - 1
    result: defaultdict&#91;Exponent, Fraction&#93; = defaultdict(Fraction)
    for (layer, power), value in series.items():
        wall_order = 0
        while layer + wall_order * shift &lt;= cutoff:
            coefficient = generalized_binomial(
                layer - pole_order + 2 * power,
                wall_order,
            )
            if coefficient:
                result&#91;
                    (
                        layer + wall_order * shift,
                        power - wall_order * k,
                    )
                &#93; += value * coefficient * parameter**wall_order
            wall_order += 1
    return clean(result)


def extract_layer(series: Mapping&#91;Exponent, Fraction&#93;, layer: int) -&gt; dict&#91;int, Fraction&#93;:
    return {
        power: value
        for (current_layer, power), value in series.items()
        if current_layer == layer
    }


def polynomial_series(polynomial: Mapping&#91;int, Fraction&#93;, layer: int = 0) -&gt; Series:
    return {(layer, power): value for power, value in polynomial.items() if value}


def determinant_layer(
    A0: Mapping&#91;int, Fraction&#93;,
    B0: Mapping&#91;int, Fraction&#93;,
    a: Mapping&#91;int, Fraction&#93;,
    b: Mapping&#91;int, Fraction&#93;,
    *,
    alpha: int,
    beta: int,
    layer: int,
) -&gt; dict&#91;int, Fraction&#93;:
    """The universal linear layer operator in scalar-coefficient form."""

    A = polynomial_series(A0)
    B = polynomial_series(B0)
    aa = polynomial_series(a)
    bb = polynomial_series(b)
    result = add(
        scale(multiply(aa, derivative_z(B), cutoff=0), alpha - layer),
        scale(multiply(B, derivative_z(aa), cutoff=0), -beta),
        scale(multiply(A, derivative_z(bb), cutoff=0), alpha),
        scale(multiply(bb, derivative_z(A), cutoff=0), layer - beta),
    )
    return extract_layer(result, 0)


def series_json(series: Mapping&#91;Exponent, Fraction&#93;) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    return &#91;
        {
            "layer": layer,
            "z_exponent": power,
            "coefficient": scalar_text(value),
        }
        for (layer, power), value in sorted(series.items())
    &#93;


def polynomial_json(polynomial: Mapping&#91;int, Fraction&#93;) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    return &#91;
        {"z_exponent": power, "coefficient": scalar_text(value)}
        for power, value in sorted(polynomial.items())
    &#93;


def verify_covariance(
    A: Mapping&#91;Exponent, Fraction&#93;,
    B: Mapping&#91;Exponent, Fraction&#93;,
    *,
    alpha: int,
    beta: int,
    k: int,
    parameter: Fraction,
    cutoff: int,
) -&gt; bool:
    transformed_A = transport(
        A,
        pole_order=alpha,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    transformed_B = transport(
        B,
        pole_order=beta,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    left = residual(
        transformed_A,
        transformed_B,
        alpha=alpha,
        beta=beta,
        cutoff=cutoff,
    )
    right = transport(
        residual(A, B, alpha=alpha, beta=beta, cutoff=cutoff),
        pole_order=alpha + beta - 1,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    return left == right


def toy_wall_arc(*, k: int = 4, cutoff: int = 15) -&gt; dict&#91;str, Any&#93;:
    """A nontrivial exact face whose wall arc needs a second-order correction."""

    alpha, beta = 2, 3
    A0: Series = {(0, 1): Fraction(1), (0, 2): Fraction(3, 2)}
    B0: Series = {(0, 2): Fraction(1), (0, 3): Fraction(1)}
    if residual(A0, B0, alpha=alpha, beta=beta, cutoff=cutoff):
        raise AssertionError("the toy face does not satisfy Psi=z^2")

    transformed_A = transport(
        A0, pole_order=alpha, k=k, parameter=1, cutoff=cutoff
    )
    transformed_B = transport(
        B0, pole_order=beta, k=k, parameter=1, cutoff=cutoff
    )
    if residual(
        transformed_A,
        transformed_B,
        alpha=alpha,
        beta=beta,
        cutoff=cutoff,
    ):
        raise AssertionError("the exact wall arc does not solve the master equation")

    shift = 2 * k - 1
    second_layer = 2 * shift
    A0_poly = extract_layer(A0, 0)
    B0_poly = extract_layer(B0, 0)
    a_first = extract_layer(transformed_A, shift)
    b_first = extract_layer(transformed_B, shift)
    a_second = extract_layer(transformed_A, second_layer)
    b_second = extract_layer(transformed_B, second_layer)

    first_linear = determinant_layer(
        A0_poly,
        B0_poly,
        a_first,
        b_first,
        alpha=alpha,
        beta=beta,
        layer=shift,
    )
    second_linear = determinant_layer(
        A0_poly,
        B0_poly,
        a_second,
        b_second,
        alpha=alpha,
        beta=beta,
        layer=second_layer,
    )
    quadratic = extract_layer(
        master(
            polynomial_series(a_first, shift),
            polynomial_series(b_first, shift),
            alpha=alpha,
            beta=beta,
            cutoff=cutoff,
        ),
        second_layer,
    )
    cancellation = add(
        polynomial_series(second_linear),
        polynomial_series(quadratic),
    )

    return {
        "face": {
            "A0": polynomial_json(A0_poly),
            "B0": polynomial_json(B0_poly),
        },
        "first_nonzero_layer": shift,
        "second_wall_layer": second_layer,
        "first_correction": {
            "a": polynomial_json(a_first),
            "b": polynomial_json(b_first),
            "linear_image": polynomial_json(first_linear),
            "kernel_verified": not first_linear,
        },
        "second_correction": {
            "a": polynomial_json(a_second),
            "b": polynomial_json(b_second),
            "linear_image": polynomial_json(second_linear),
            "quadratic_forcing": polynomial_json(quadratic),
            "cancellation_verified": not cancellation,
        },
        "zero_second_correction_slice": {
            "residual": polynomial_json(quadratic),
            "inconsistent_with_exact_wall_arc": bool(quadratic),
        },
    }


def build_report(*, k: int, cutoff: int, parameter: Fraction) -&gt; dict&#91;str, Any&#93;:
    alpha, beta = 2, 3
    sample_A: Series = {
        (0, 1): Fraction(1),
        (0, 2): Fraction(2),
        (1, 0): Fraction(3),
        (4, 3): Fraction(1, 2),
    }
    sample_B: Series = {
        (0, 2): Fraction(1),
        (0, 3): Fraction(1),
        (2, -1): Fraction(2),
        (5, 4): Fraction(-1),
    }
    sample_a: Series = {(0, 0): Fraction(2), (3, 2): Fraction(-1)}
    sample_b: Series = {(1, 1): Fraction(3), (4, -2): Fraction(1)}

    transformed_A = transport(
        sample_A,
        pole_order=alpha,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    transformed_B = transport(
        sample_B,
        pole_order=beta,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    transformed_a = transport(
        sample_a,
        pole_order=alpha,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    transformed_b = transport(
        sample_b,
        pole_order=beta,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )
    left_linear = linearization(
        transformed_A,
        transformed_B,
        transformed_a,
        transformed_b,
        alpha=alpha,
        beta=beta,
        cutoff=cutoff,
    )
    right_linear = transport(
        linearization(
            sample_A,
            sample_B,
            sample_a,
            sample_b,
            alpha=alpha,
            beta=beta,
            cutoff=cutoff,
        ),
        pole_order=alpha + beta - 1,
        k=k,
        parameter=parameter,
        cutoff=cutoff,
    )

    group_left = transport(
        transport(
            sample_A,
            pole_order=alpha,
            k=k,
            parameter=Fraction(2, 3),
            cutoff=cutoff,
        ),
        pole_order=alpha,
        k=k,
        parameter=Fraction(-1, 5),
        cutoff=cutoff,
    )
    group_right = transport(
        sample_A,
        pole_order=alpha,
        k=k,
        parameter=Fraction(7, 15),
        cutoff=cutoff,
    )

    return {
        "schema_version": 1,
        "name": "wall-shear master-equation covariance",
        "alpha": alpha,
        "beta": beta,
        "equation_density_pole_order": alpha + beta - 1,
        "k": k,
        "normal_layer_shift": 2 * k - 1,
        "cutoff": cutoff,
        "parameter": scalar_text(parameter),
        "transport_formula": (
            "T_p(t^n z^j)=sum_q binom(n-p+2j,q) lambda^q "
            "t^(n+q(2k-1)) z^(j-qk)"
        ),
        "master_covariance": (
            "R(T_alpha A,T_beta B)=T_(alpha+beta-1)R(A,B)"
        ),
        "master_covariance_verified": verify_covariance(
            sample_A,
            sample_B,
            alpha=alpha,
            beta=beta,
            k=k,
            parameter=parameter,
            cutoff=cutoff,
        ),
        "linearized_chain_map_verified": left_linear == right_linear,
        "additive_group_law_verified": group_left == group_right,
        "rhs_z_squared_fixed": transport(
            {(0, 2): Fraction(1)},
            pole_order=alpha + beta - 1,
            k=k,
            parameter=parameter,
            cutoff=cutoff,
        )
        == {(0, 2): Fraction(1)},
        "filtered_conjugacy_boundary": {
            "statement": (
                "A filtration-preserving conjugacy with invertible associated "
                "graded map preserves the principal shift 2k-1."
            ),
            "k4_shift": 7 if k == 4 else None,
            "can_become_layer_four_by_filtered_conjugacy": (
                False if k == 4 else None
            ),
        },
        "toy_exact_wall_arc": toy_wall_arc(k=k, cutoff=cutoff),
    }


def main(argv: Sequence&#91;str&#93; | None = None) -&gt; int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--cutoff", type=int, default=15)
    parser.add_argument("--parameter", default="1")
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)

    report = build_report(
        k=args.k,
        cutoff=args.cutoff,
        parameter=Fraction(args.parameter),
    )
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-89e4eda45b4d5d16"></a>

## `research-notes/p6-chart-correspondence/LANE9_F2_PARAMETER_COMPLETE_RECURRENCE_V2.md`

<pre><code class="language-markdown">
# Parameter-complete `F_2` attachment recurrence

**Status:** exact finite-dimensional criterion and executable contract.  The
actual order-`510/520/530` endpoint matrices remain absent from the public
packet, so this note does not report a numerical global-attachment verdict.

## 1. The intrinsic finite-order system

Fix all lower orders.  At normal order `r`, let \(V_r^{\rm corr}\) be the
finite-dimensional space of left-endpoint, right-endpoint, and overlap
corrections, let \(V_r^{\rm fresh}\) be the space of every fresh order-`r`
parameter, and let

\&#91;
W_r
\&#93;

be the finite-dimensional space with one coordinate for every determinant,
overlap, support, presentation, and cyclic-descent equation imposed at that
order.  (This equation space \(W_r\) is unrelated to the scalar formal normal
coordinate called \(W(T)\) in the exact-normal-linearization appendix.)
Collect the unknowns into

```text
X_r=(x_r^L,x_r^R,o_r,p_r).
```

Concatenate:

1. the two endpoint determinant equations;
2. the overlap/normalization equations;
3. the coefficients outside both finite Newton windows;
4. any presentation and cyclic-descent equations.

The complete order-`r` problem is one exact affine system

```text
M_r X_r=b_r.                                  (1.1)
```

Thus \(M_r:V_r^{\rm corr}\oplus V_r^{\rm fresh}\to W_r\) and
\(b_r\in W_r\).  All nonlinear dependence on lower orders is already
evaluated in `b_r` and in any known coefficients of `M_r`.  Once the real
blocks are supplied, finite-order attachment is an exact linear-algebra
problem over the coefficient field.

## 2. Fresh parameters change the obstruction space

Write the full matrix as

```text
M_r=&#91;C_r | P_r&#93;,                              (2.1)
```

where `C_r` contains endpoint and overlap correction columns and `P_r`
contains every fresh-parameter column.  The parameter-zero slice tests only

```text
C_r x_r=b_r.                                  (2.2)
```

The intrinsic obstruction object is the quotient

```text
Ob_r = coker(M_r) = W_r/(im(C_r)+im(P_r)).    (2.3)
```

The obstruction to solving the affine system is the forcing class
`&#91;b_r&#93; in Ob_r`; the system is solvable exactly when this class is zero.
The dual space of obstruction functionals is

```text
Ob_r^* = ker(M_r^T)
       = ker(C_r^T) intersect ker(P_r^T).      (2.4)
```

after bases identify the dual map with matrix transpose.  The
fresh-parameter-zero slice instead has obstruction quotient
`W_r/im(C_r)` and dual functional space `ker(C_r^T)`.

Consequently a left-null vector of `C_r` is an intrinsic obstruction
functional only when it also annihilates every fresh-parameter column.
Equivalently,

```text
b_r in im(C_r)+im(P_r)                        (2.5)
```

is the full compatibility criterion, whereas `b_r in im(C_r)` is merely the
chosen zero-parameter slice.

### Proposition 2.1 — slice-dependent apparent obstruction

Suppose `ell^T C_r=0` and `ell^T b_r` is nonzero.  Then `ell` is a functional
on the slice quotient `W_r/im(C_r)` which detects the nonzero slice forcing
class, so (2.2) is inconsistent.  It descends to a functional on the
intrinsic quotient `Ob_r`—and therefore proves inconsistency of (1.1)—only
if `ell^T P_r=0` as well.  If `ell^T P_r` is nonzero, the condition can be
cancelled by a fresh parameter and is not gauge- or chart-independent.

This is the exact linear-algebra reason that a nonzero order-`530` value
computed after setting new parameters to zero cannot be promoted to a global
obstruction.

## 3. Base field and `C_5` descent

The quotient criterion above is valid over any field.  For the character
decomposition, assume that the coefficient field \(K\) has
`char(K) != 5`, contains a chosen primitive fifth root of unity, and that
the source, equation, correction, fresh-parameter, and forcing data are all
\(C_5\)-equivariant.  If the original field does not contain that root, make
the decomposition after the separable scalar extension \(K(\zeta_5)/K\);
consistency of a finite linear system is unchanged by this field extension.

After equivariant decomposition,

```text
M_r = direct-sum_(chi in Z/5) M_(r,chi),
b_r = direct-sum_(chi in Z/5) b_(r,chi).      (3.1)
```

The full system is feasible exactly when each character block is feasible,
and the obstruction quotient and its dual decompose into the same blocks.
Every variable in a preassembled block must have the block character; known
products of lower-order variables and wall parameters must be moved into the
correct character component before export.

For the `k=4` wall parameter, the parameter character is `4 mod 5`, and a
`q`-th wall term shifts coefficient character by `-4q`.  A scalar invariant
wall effect first returns at wall order five.  This bookkeeping applies to
all correction and support equations, not only to invariant face
coefficients.

## 4. Finite polynomial support

Polynomiality adds rows to (1.1): every coefficient outside the allowed left
or right Newton window is set to zero.  There is no separate infinite
argument at a fixed truncation.  Once the ordered support blocks are supplied,
the exact feasibility calculation is finite.

The support rows must be formed after transporting the entire overlap datum:
coefficient vector, equation density, fixed-presentation operation columns,
rechart columns, fresh parameters, and residue-dual functionals.  Truncating a
transported Laurent vector by itself does not define a chart overlap.

## 5. Executable contract

`lane9_f2_attachment_recurrence.py` reads a rational JSON contract with:

- a cyclic modulus;
- normal orders;
- character blocks;
- named variables and their kinds;
- named equations;
- the exact matrix and right-hand side.

For every block it reports:

```text
rank(M), rank(&#91;M|b&#93;), consistency,
solution dimension, left nullity,
nonzero left-null obstruction certificates,
```

and repeats the calculation after deleting all fresh-parameter columns.  A
block is marked `slice_dependent_apparent_obstruction` precisely when the
full system is consistent but the zero-parameter slice is not.

The included contract

```text
synthetic_f2_parameter_retention_contract.json
```

is explicitly synthetic.  It is a regression fixture demonstrating at orders
`510`, `520`, and `530` how fresh columns remove conditions visible on the
zero-parameter slice.  It is not evidence about the numerical `F_2`
recurrence.

## 6. Data required for the real replay

A real contract must publish, for both endpoints and every relevant order:

1. ordered correction bases and determinant matrices;
2. ordered finite support windows and outside-window rows;
3. overlap and complete-chain normalization matrices;
4. all fresh parameters, first occurrence orders, and `C_5` characters;
5. the lower-order forcing vector in the same equation basis;
6. an archive manifest and hashes sufficient to reproduce the export.

The hash-pinned public Program 6 ZIP contains the terminal face, the degree-30
coefficient recurrence, and related Hurwitz data.  The deterministic Lane 9
scan found no small UTF-8 member matching an order-`510/520/530`,
fresh-parameter, or `F_2` matrix/support-block endpoint packet.  The checker
therefore refuses to synthesize a numerical order-`530` verdict.

## 7. Reproduction

```bash
cd research-notes/p6-chart-correspondence

python -m unittest -v test_lane9_f2_attachment_recurrence.py

python lane9_f2_attachment_recurrence.py \
  synthetic_f2_parameter_retention_contract.json \
  --output /tmp/synthetic-f2-parameter-retention-report.json
```

This utility was recovered from public-site PR #1. It is a reusable exact
contract and regression fixture, not evidence for a numerical endpoint claim;
the actual endpoint export remains the required mathematical input.
</code></pre>

<a id="source-2b16e7df7e008983"></a>

## `research-notes/p6-chart-correspondence/lane9_f2_attachment_recurrence.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact blockwise audit for a parameter-complete F2 attachment recurrence.

The input contract is deliberately data-only.  Each order is split into C_g
character blocks.  A block supplies an exact rational matrix, right-hand side,
and variable declarations.  The audit compares the full system with the
non-intrinsic slice obtained by setting fresh parameters to zero.

This utility does not contain or infer the missing public F2 endpoint blocks.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

RationalMatrix = list&#91;list&#91;Fraction&#93;&#93;


def parse_fraction(value: Any) -&gt; Fraction:
    if isinstance(value, bool):
        raise TypeError("booleans are not rational entries")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise TypeError(f"expected integer or rational string, got {type(value).__name__}")


def render_fraction(value: Fraction) -&gt; str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def transpose(matrix: RationalMatrix, column_count: int) -&gt; RationalMatrix:
    if matrix:
        return &#91;list(column) for column in zip(*matrix)&#93;
    return &#91;&#91;&#93; for _ in range(column_count)&#93;


def rref(matrix: RationalMatrix) -&gt; tuple&#91;RationalMatrix, list&#91;int&#93;&#93;:
    work = &#91;row&#91;:&#93; for row in matrix&#93;
    row_count = len(work)
    column_count = len(work&#91;0&#93;) if work else 0
    if any(len(row) != column_count for row in work):
        raise ValueError("ragged matrix")

    pivots: list&#91;int&#93; = &#91;&#93;
    pivot_row = 0
    for pivot_column in range(column_count):
        selected = next(
            (row for row in range(pivot_row, row_count) if work&#91;row&#93;&#91;pivot_column&#93;),
            None,
        )
        if selected is None:
            continue
        work&#91;pivot_row&#93;, work&#91;selected&#93; = work&#91;selected&#93;, work&#91;pivot_row&#93;
        pivot = work&#91;pivot_row&#93;&#91;pivot_column&#93;
        work&#91;pivot_row&#93; = &#91;entry / pivot for entry in work&#91;pivot_row&#93;&#93;
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = work&#91;row&#93;&#91;pivot_column&#93;
            if factor:
                work&#91;row&#93; = &#91;
                    work&#91;row&#93;&#91;column&#93; - factor * work&#91;pivot_row&#93;&#91;column&#93;
                    for column in range(column_count)
                &#93;
        pivots.append(pivot_column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return work, pivots


def rank(matrix: RationalMatrix) -&gt; int:
    return len(rref(matrix)&#91;1&#93;)


def nullspace(matrix: RationalMatrix, column_count: int) -&gt; RationalMatrix:
    width = len(matrix&#91;0&#93;) if matrix else column_count
    reduced, pivots = rref(matrix)
    free_columns = &#91;column for column in range(width) if column not in pivots&#93;
    basis: RationalMatrix = &#91;&#93;
    for free in free_columns:
        vector = &#91;Fraction(0) for _ in range(width)&#93;
        vector&#91;free&#93; = Fraction(1)
        for row, pivot in enumerate(pivots):
            vector&#91;pivot&#93; = -reduced&#91;row&#93;&#91;free&#93;
        basis.append(vector)
    return basis


def dot(left: Sequence&#91;Fraction&#93;, right: Sequence&#91;Fraction&#93;) -&gt; Fraction:
    if len(left) != len(right):
        raise ValueError("dot-product dimension mismatch")
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def solve_diagnostics(
    matrix: RationalMatrix,
    rhs: list&#91;Fraction&#93;,
    column_count: int | None = None,
) -&gt; dict&#91;str, Any&#93;:
    row_count = len(matrix)
    if matrix:
        inferred_column_count = len(matrix&#91;0&#93;)
        if column_count is not None and inferred_column_count != column_count:
            raise ValueError("declared column count does not match matrix")
        column_count = inferred_column_count
    elif column_count is None:
        column_count = 0

    if len(rhs) != row_count:
        raise ValueError("right-hand-side length does not match matrix")
    if any(len(row) != column_count for row in matrix):
        raise ValueError("ragged matrix")

    matrix_rank = rank(matrix)
    augmented = &#91;row + &#91;rhs&#91;index&#93;&#93; for index, row in enumerate(matrix)&#93;
    augmented_rank = rank(augmented)
    consistent = matrix_rank == augmented_rank

    left_kernel = nullspace(
        transpose(matrix, column_count),
        column_count=row_count,
    )
    pairings = &#91;dot(vector, rhs) for vector in left_kernel&#93;
    certificates = &#91;
        {
            "left_null_vector": &#91;render_fraction(entry) for entry in vector&#93;,
            "pairing_with_rhs": render_fraction(pairing),
        }
        for vector, pairing in zip(left_kernel, pairings)
        if pairing
    &#93;

    return {
        "row_count": row_count,
        "column_count": column_count,
        "rank": matrix_rank,
        "augmented_rank": augmented_rank,
        "consistent": consistent,
        "solution_dimension": column_count - matrix_rank if consistent else None,
        "left_nullity": row_count - matrix_rank,
        "nonzero_obstruction_certificates": certificates,
    }


def parse_block(
    block: Mapping&#91;str, Any&#93;, modulus: int
) -&gt; tuple&#91;list&#91;dict&#91;str, Any&#93;&#93;, RationalMatrix, list&#91;Fraction&#93;&#93;:
    variables = list(block.get("variables", &#91;&#93;))
    equations = list(block.get("equations", &#91;&#93;))
    matrix_raw = list(block.get("matrix", &#91;&#93;))
    rhs_raw = list(block.get("rhs", &#91;&#93;))
    character = int(block&#91;"character"&#93;) % modulus

    if len(matrix_raw) != len(equations):
        raise ValueError("matrix row count must equal equation count")
    if len(rhs_raw) != len(equations):
        raise ValueError("rhs length must equal equation count")
    if any(len(row) != len(variables) for row in matrix_raw):
        raise ValueError("matrix column count must equal variable count")

    names = &#91;str(variable&#91;"name"&#93;) for variable in variables&#93;
    if len(names) != len(set(names)):
        raise ValueError("variable names must be unique within a block")
    for variable in variables:
        if int(variable&#91;"character"&#93;) % modulus != character:
            raise ValueError(
                f"variable {variable&#91;'name'&#93;} has character "
                f"{variable&#91;'character'&#93;}, but block has character {character}"
            )
        if variable.get("kind") not in {
            "left_correction",
            "right_correction",
            "overlap_correction",
            "fresh_parameter",
            "other",
        }:
            raise ValueError(f"unsupported variable kind for {variable&#91;'name'&#93;}")

    matrix = &#91;&#91;parse_fraction(entry) for entry in row&#93; for row in matrix_raw&#93;
    rhs = &#91;parse_fraction(entry) for entry in rhs_raw&#93;
    return variables, matrix, rhs


def audit_block(block: Mapping&#91;str, Any&#93;, modulus: int) -&gt; dict&#91;str, Any&#93;:
    variables, matrix, rhs = parse_block(block, modulus)
    full = solve_diagnostics(matrix, rhs, column_count=len(variables))

    retained_columns = &#91;
        index
        for index, variable in enumerate(variables)
        if variable&#91;"kind"&#93; != "fresh_parameter"
    &#93;
    fresh_columns = &#91;
        index
        for index, variable in enumerate(variables)
        if variable&#91;"kind"&#93; == "fresh_parameter"
    &#93;
    sliced_matrix = &#91;
        &#91;row&#91;column&#93; for column in retained_columns&#93; for row in matrix
    &#93;
    fixed_parameter_slice = solve_diagnostics(
        sliced_matrix,
        rhs,
        column_count=len(retained_columns),
    )

    return {
        "name": str(block.get("name", f"character-{block&#91;'character'&#93;}")),
        "character": int(block&#91;"character"&#93;) % modulus,
        "equations": &#91;str(name) for name in block.get("equations", &#91;&#93;)&#93;,
        "variables": variables,
        "full_parameter_system": full,
        "fresh_parameter_names": &#91;
            variables&#91;index&#93;&#91;"name"&#93; for index in fresh_columns
        &#93;,
        "fixed_fresh_parameter_zero_slice": fixed_parameter_slice,
        "slice_dependent_apparent_obstruction": (
            full&#91;"consistent"&#93; and not fixed_parameter_slice&#91;"consistent"&#93;
        ),
    }


def audit_contract(contract: Mapping&#91;str, Any&#93;) -&gt; dict&#91;str, Any&#93;:
    if int(contract.get("schema_version", 0)) != 1:
        raise ValueError("unsupported schema_version")
    modulus = int(contract.get("cyclic_modulus", 5))
    if modulus &lt;= 0:
        raise ValueError("cyclic_modulus must be positive")

    orders_out: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;
    for order_entry in contract.get("orders", &#91;&#93;):
        order = int(order_entry&#91;"order"&#93;)
        blocks = &#91;
            audit_block(block, modulus) for block in order_entry.get("blocks", &#91;&#93;)
        &#93;
        orders_out.append(
            {
                "order": order,
                "block_count": len(blocks),
                "all_full_parameter_blocks_consistent": all(
                    block&#91;"full_parameter_system"&#93;&#91;"consistent"&#93;
                    for block in blocks
                ),
                "any_slice_dependent_apparent_obstruction": any(
                    block&#91;"slice_dependent_apparent_obstruction"&#93;
                    for block in blocks
                ),
                "blocks": blocks,
            }
        )

    instantiated = any(order&#91;"block_count"&#93; for order in orders_out)
    return {
        "schema_version": 1,
        "contract_name": str(
            contract.get("name", "unnamed F2 attachment contract")
        ),
        "provenance": contract.get("provenance"),
        "cyclic_modulus": modulus,
        "instantiated": instantiated,
        "orders": orders_out,
        "all_full_parameter_systems_consistent": (
            all(
                order&#91;"all_full_parameter_blocks_consistent"&#93;
                for order in orders_out
            )
            if instantiated
            else None
        ),
        "interpretation": (
            "Only the full-parameter system defines an intrinsic finite-order "
            "test. The fresh-parameter-zero calculation is reported solely as "
            "a slice diagnostic."
        ),
    }


def main(argv: Sequence&#91;str&#93; | None = None) -&gt; int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        contract = json.loads(args.contract.read_text(encoding="utf-8"))
        report = audit_contract(contract)
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        print(f"lane9_f2_attachment_recurrence: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

[Back to Lane 9](plane-chart-correspondence-global-attachment.md)
