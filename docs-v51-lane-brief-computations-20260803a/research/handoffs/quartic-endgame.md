---
title: "Model research brief — The quartic endgame"
description: "A self-contained mathematical handoff for a research model."
---

# Lane 4: The quartic endgame

<p class="claim-tag">Lane 4 · Updated 3 August 2026</p>

## Problem and scope

For a three-variable Keller map $F=(F_1,F_2,F_3)$, put

$$
D(F)=\max_i\deg F_i,\qquad
D_{\min}=\min\{D(F):F\text{ is noninvertible}\}.
$$

The degree-at-most-three theorem and the known degree-seven example give
$4\le D_{\min}\le7$. Lane 4 asks whether every Keller map of degree four is
invertible.

The repository has many proved reductions and replayable terminal leaves. It
does not yet have a proof that the remaining curve-orbit, chart-complement,
and exceptional-system interfaces route every normalized quartic map to
those leaves.

## Setup and notation

A normalized quartic Keller map satisfies $F(0)=0$, $DF(0)=I$,
$\deg F_i\le4$, and $\det DF=1$. Write $H_4$ for its leading homogeneous
triple. The equation $\det JH_4=0$ forces the projective image of $H_4$ to
have dimension at most one. If the target span of the three coordinates is
three, the image is a nondegenerate integral curve.

For a curve image of degree $e$, the normalization-first factorization is

$$
H_4=G\,h(A,B),\qquad \deg G+e\deg A=4,
$$

where $A,B$ are coprime forms of the same degree and $h$ is the degree-$e$
normalization map of the image curve. The four nondegenerate numerical
leaves are

$$
(e,\deg A,\deg G)=(2,1,2),(2,2,0),(3,1,1),(4,1,0).
$$

This is unit [`RMU-2D4E0012`](../working-mathematics/units/RMU-2D4E0012.md). It replaces the former proof that incorrectly
used relative algebraic closure as a birationality criterion.

A case-tree edge is an exact implication between normalized subcases. An
edge is exhaustive only when every denominator, basepoint locus,
specialization, saturation factor, and rank-drop complement has a child. A
leaf is closed by a conventional proof or an exact finite certificate under
the hypotheses accumulated along its path.

The labels F3 and F4 in the terminal inventory are historical system labels,
not coordinates of $F$. Q4-F4 denotes the surviving weighted-inflection
system described below.

## Reusable mathematics and leaf inventory

The four-loci proposition [`RMU-2D4E0013`](../working-mathematics/units/RMU-2D4E0013.md) now has a complete proof in
[`manuscripts/02-low-degree/main.tex`](../proof-sources/02-low-degree/main.md). At the target-span-two interface, every
leading pair lies in at least one of:

1. a binary quartic pencil, with $R$ binary in the same two linear forms;
2. a quadratic-source pencil;
3. a composition-primitive coprime pencil containing a fourth-power member;
4. a primitive reduced pencil with fixed factor $G$, every component of $G$
   supported on a special fiber.

In the coprime case the residue orders are nonnegative and sum to three,
forcing the fourth-power fiber. In the fixed-component case poles may
cancel; a separate divisorial valuation shows that each component of $G$ is
a special fiber. Do not reuse the coprime nonnegativity assertion after
introducing fixed components.

| Leaf family | Exact scope | Source |
| --- | --- | --- |
| Leading-image entry and numerical leaves | Curve image; target-span-three bridge included | [`RMU-2D4E0012`](../working-mathematics/units/RMU-2D4E0012.md) |
| Four structural leading-pair loci | Target-span-two quartic setup | [`RMU-2D4E0013`](../working-mathematics/units/RMU-2D4E0013.md) |
| Nondegenerate conic and rational-cubic leaves | Stated curve type and normalization | [`manuscripts/02-low-degree/main.tex`](../proof-sources/02-low-degree/main.md) |
| Rational-quartic frontier | Recorded surviving orbit types | [`RMU-99553B20`](../working-mathematics/units/RMU-99553B20.md) and [`RMU-CC15C520`](../working-mathematics/units/RMU-CC15C520.md) |
| Binary ramification degrees zero through five | Includes recorded zero-minor boundaries | [`manuscripts/02-low-degree/appendices/quartic-frontier-and-ramification.tex`](../proof-sources/02-low-degree/appendices/quartic-frontier-and-ramification.md) |
| Fixed fourth-power, line, conic, cubic, and $R=0$ leaves | Their displayed common-factor hypotheses | [`RMU-D6A4C9D6`](../working-mathematics/units/RMU-D6A4C9D6.md) and [`RMU-0616D9BC`](../working-mathematics/units/RMU-0616D9BC.md) |
| High-ramification and dependent-syzygy charts | The exact encoded charts only | [`RMU-2920F7C8`](../working-mathematics/units/RMU-2920F7C8.md) |
| Replayed terminal packet | Listed conic, cubic, high-ramification, and $\tau=-1$ systems | [`RMU-2D4E0010`](../working-mathematics/units/RMU-2D4E0010.md) |

The terminal packet is
[`research-notes/lane4-quartic-endgame-20260802-v1/`](lane-4-source-packet.md). Its case tree,
proof/code crosswalk, and versioned replays close the listed terminal systems
but do not certify all upstream routes.

At an exceptional divisor above a common projective zero of $G,A,B$, unit
[`RMU-2D4E0011`](../working-mathematics/units/RMU-2D4E0011.md) gives a useful partial valuation constraint. If the orders of
$A$ and $B$ agree and the residual ratio is nonconstant away from the zeros
and poles of $\rho$, then $4r=3(g+b)$, hence $4$ divides $g+b$. This excludes
the simple pattern $g=a=b=1$ but does not classify every exceptional
valuation.

## The Q4-F4 input boundary

The surviving Q4-F4 branch is a real mathematical target, but its finite
system is not reconstructible from the currently collected formulas. The
repository lacks one complete artifact containing $q_4(d,\tau)$, the
normalized $P,Q,R$, all allowed coefficients of $H_3,H_2,L$, every gauge
removal, and the full product of inverted chart factors.

The exact fail-closed specification is
[`research-notes/lane4-f4-contract-20260803-v1/F4_INPUT_CONTRACT.md`](lane-4-source-packet.md), with
machine schema `f4-contract.schema.json`. Unit [`RMU-2D4E0014`](../working-mathematics/units/RMU-2D4E0014.md) records the open
question. A proposed obstruction is not a result if it suppresses a
coefficient that remains free after the stated normalizations.

## Exact live problems

There are two independent next problems.

First, complete the rooted case-tree audit beginning with an arbitrary
normalized quartic Keller map, taking [`RMU-2D4E0012`](../working-mathematics/units/RMU-2D4E0012.md) and [`RMU-2D4E0013`](../working-mathematics/units/RMU-2D4E0013.md) as proved
interfaces. Locate the first uncovered curve-orbit, Hilbert--Burch,
localization-complement, or proof-to-code edge.

Second, recover or rederive a complete Q4-F4 contract instance. Only after
that input exists should one solve $D_6$ as a module, test $D_5$ in the
cokernel of every remaining cancellation variable, and saturate by the
complete open product.

## Tasks and deliverables

### P2-L4A — Remaining global edge audit

Status: ready.

Inputs: [`RMU-2D4E0012`](../working-mathematics/units/RMU-2D4E0012.md), [`RMU-2D4E0013`](../working-mathematics/units/RMU-2D4E0013.md), [`RMU-2D4E0010`](../working-mathematics/units/RMU-2D4E0010.md), [`RMU-2D4E0011`](../working-mathematics/units/RMU-2D4E0011.md),
[`research-notes/lane4-quartic-endgame-20260802-v1/`](lane-4-source-packet.md), and the source tree rooted
at [`manuscripts/02-low-degree/main.tex`](../proof-sources/02-low-degree/main.md).

Deliverable: one rooted table in which each edge records its parent
hypotheses, coordinate action, open factors, all vanishing complements,
proof locator, computation locator when applicable, and inherited child
hypotheses. The first unsupported edge becomes an exact candidate normal
form. Do not spend time reproving the leading-image or four-loci interfaces
unless a concrete flaw is found.

### P2-L4B — Construct the Q4-F4 instance

Status: ready as a reconstruction or derivation problem; the elimination is
blocked until the instance is complete.

Inputs: [`RMU-2D4E0014`](../working-mathematics/units/RMU-2D4E0014.md) and every item required by
[`research-notes/lane4-f4-contract-20260803-v1/F4_INPUT_CONTRACT.md`](lane-4-source-packet.md).

Deliverable: one JSON instance accepted by `f4-contract.schema.json`, together
with independent reconstruction checks for $q_4,P,Q,R$, all lower layers,
the gauge table, open product, complement routes, determinant convention,
and two exact samples.

### P2-L4C — Eliminate Q4-F4

Status: blocked on P2-L4B.

Deliverable: an exact characteristic-zero certificate for the fully
localized $D_6/D_5$ system, or a surviving component continued through all
remaining determinant layers. Every factor removed by saturation must have
its own child calculation.

### P2-L4D — Terminal proof/code crosswalk

Status: ready when P2-L4A actually uses a terminal leaf.

Inputs: the terminal packet crosswalk, manifest, and the used leaf.

Deliverable: exact command, source hash, output, and one independent sample
identity. This validates the encoded algebra, not the upstream geometric
route.

## Scope cautions

- The current lower bound is $D_{\min}\ge4$, not $D_{\min}\ge5$.
- A vanishing denominator opens another chart; it never justifies
  specialization into a formula obtained after dividing by it.
- The degree-five/six fixed-factor theorem is a separate result with a
  basepoint-free hypothesis; it is not a missing quartic case-tree edge.
- Terminal exactness does not imply global exhaustiveness.

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
