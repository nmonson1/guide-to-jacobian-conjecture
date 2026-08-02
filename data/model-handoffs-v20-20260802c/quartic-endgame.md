# Lane 4: The quartic endgame

## Problem and scope

For a three-variable Keller map `F=(F_1,F_2,F_3)`, define

```text
D(F)=max_i deg(F_i),
D_min=min{D(F): F is a noninvertible three-variable Keller map}.
```

The known degree-seven example and the degree-at-most-three theorem give

```text
4 <= D_min <= 7.
```

The exact bounded statement and its scope are recorded in [`JCG-6747671C`](../working-mathematics/units/JCG-6747671C.md);
the degree-seven map is displayed in [`manuscripts/01-cubic-incidence/main.tex`](../proof-sources/01-cubic-incidence/main.md).

Lane 4 asks whether every map with `D(F)=4` is invertible. The repository
contains many exact leaves of a quartic classification, but no current source
proves that every quartic map reaches one of them.

## Setup and notation

A *normalized quartic Keller map* here means `F(0)=0`, `DF(0)=I`,
`deg(F_i)<=4`, and `det DF=1`. A *case-tree edge* sends such a map satisfying
explicit structural hypotheses to normalized subcases. A *leaf* is closed by a conventional
theorem or exact finite certificate. An edge is exhaustive only after every
vanishing denominator, basepoint locus, specialization, and saturation
boundary has its own child.

The working classification uses leading homogeneous target span, its plane
curve, binary-pencil ramification, fixed factors, and syzygies. The names
`F_3` and `F_4` in the final inventory are historical branch/system labels in
the Program 2 sources; they are not the third and fourth coordinates of `F`.

## Reusable mathematics and leaf inventory

| Leaf family | Exact scope | Current routes |
| --- | --- | --- |
| Leading-span and leading-image reductions | Recorded rank and image hypotheses | [`RMU-B7B975F2`](../working-mathematics/units/RMU-B7B975F2.md), [`RMU-C41D9892`](../working-mathematics/units/RMU-C41D9892.md) |
| Nondegenerate conic and rational-cubic leaves | Listed curve type and normalization | [`manuscripts/02-low-degree/main.tex`](../proof-sources/02-low-degree/main.md) |
| Rational-quartic frontier | Surviving recorded orbit types | [`RMU-99553B20`](../working-mathematics/units/RMU-99553B20.md), [`RMU-CC15C520`](../working-mathematics/units/RMU-CC15C520.md) |
| Binary-pencil ramification degrees `0,...,5` | Includes zero-minor boundary charts | [`manuscripts/02-low-degree/appendices/quartic-frontier-and-ramification.tex`](../proof-sources/02-low-degree/appendices/quartic-frontier-and-ramification.md) |
| Fixed fourth-power/line/conic/cubic and `R=0` branches | Displayed common-factor hypotheses | [`RMU-D6A4C9D6`](../working-mathematics/units/RMU-D6A4C9D6.md), [`RMU-0616D9BC`](../working-mathematics/units/RMU-0616D9BC.md) |
| High-ramification and dependent-syzygy charts | Exact encoded charts | [`RMU-2920F7C8`](../working-mathematics/units/RMU-2920F7C8.md) and its proof sources |
| Exceptional `F_3/F_4` systems | Pinned local systems, not global routing | [`manuscripts/02-low-degree/appendices/quartic-frontier-and-ramification.tex`](../proof-sources/02-low-degree/appendices/quartic-frontier-and-ramification.md) and [`manuscripts/02-low-degree/appendices/quartic-high-ramification-and-fixed-components.tex`](../proof-sources/02-low-degree/appendices/quartic-high-ramification-and-fixed-components.md) |

The ten high-ramification checkers and 38 manifest groups replay their pinned
systems. At an exceptional divisor over a common projective zero of `G,A,B`,
the fixed-component relation gives the exact valuation constraint in
[`RMU-2D4E0011`](../working-mathematics/units/RMU-2D4E0011.md): if `a=b` and the residual ratio is nonconstant away from the
zeros and poles of `rho`, then `4r=3(g+b)`, hence `4` divides `g+b`. In
particular the simple pattern `g=a=b=1` is impossible. This narrows one
basepoint branch but does not route all exceptional valuations.

The terminal material is now collected in one branchwise proof/code packet:
[`research-notes/lane4-quartic-endgame-20260802-v1/`](lane-4-source-packet.md). Its case-tree table,
session evidence ledger, proof/code crosswalk and versioned replays cover the
listed conic, rational-cubic, high-ramification and `tau=-1` terminal
systems. Unit: [`RMU-2D4E0010`](../working-mathematics/units/RMU-2D4E0010.md). The packet deliberately does not certify the
upstream claim that every quartic map reaches one of these systems.

Terminal exactness does not prove that a normalization reaches the terminal
chart. Complete specialization, later curve-orbit reductions, and proof-code
crosswalks must be checked at each edge.

## Exact live problem

Audit and complete the supplied rooted case tree, beginning at an arbitrary
normalized quartic Keller map. At each edge compare the accumulated
hypotheses with the exact theorem or checker input in the crosswalk. The main
goal is to locate the first genuinely uncovered branch, not to replay already
closed terminal identities.

## Tasks and deliverables

### P2-L4A — Global leaf accounting

Status: ready.

Inputs: the inventory above, [`RMU-2D4E0010`](../working-mathematics/units/RMU-2D4E0010.md), the case tree and crosswalk in
[`research-notes/lane4-quartic-endgame-20260802-v1/`](lane-4-source-packet.md), [`RMU-2D4E0011`](../working-mathematics/units/RMU-2D4E0011.md), and the
complete source tree rooted at [`manuscripts/02-low-degree/main.tex`](../proof-sources/02-low-degree/main.md).

Deliverable: one case-tree table with no edge filled by analogy. Every
uncovered boundary becomes a named candidate normal form. For every edge
record: parent hypotheses; coordinate change; nonvanishing open condition;
children including its vanishing complement; proof or computation locator;
and the hypotheses inherited by each child.

### P2-L4B — Proof-code crosswalk

Status: ready local verification; prioritize only leaves used by P2-L4A.

Inputs: `PROOF_CODE_CROSSWALK.md`, the packet manifest, and the terminal
leaves actually used by the completed table. The core structural, conic and
rational-cubic groups already have a fresh successful replay.

Deliverable: exact commands, input hashes, outputs, and an independent sample
identity for every computational leaf.

### P2-L4C — Resolve the first uncovered branch

Status: blocked on P2-L4A.

Deliverable: a proof or pinned finite system for the first uncovered normal
form. If none remains, assemble the global proof with explicit computation
interfaces.

## Scope cautions

- The current lower bound is `D_min>=4`, not `D_min>=5`.
- A vanishing denominator opens another chart; it does not justify specialization.
- The degree-five/six fixed-factor theorem is a separate higher-degree result;
  its basepoint-free hypothesis is not a missing quartic case-tree edge.
- Multiple wrappers around one formula are not independent certificates.
