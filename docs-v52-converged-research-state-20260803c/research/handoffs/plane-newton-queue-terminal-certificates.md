---
title: "Model research brief — The first Newton queue at and beyond degree 125"
description: "A self-contained mathematical handoff for a research model."
---

# The first Newton queue at and beyond degree 125

<p class="claim-tag">Lane 8 · Updated 3 August 2026</p>

Lane 8 · 2026-08-03

## Scope

Start at the first unsolved post-bound queue root. Both normalized
$(8,28)$ roots and the characteristic-zero below-$125$ conclusion relative
to the cited literature and compact terminal theorem are already known.

## Setup and definitions

For a polynomial Keller pair, a Newton root is an exact pair of support
polygons together with nonzero vertex conditions and a normalized lower face.
A queue edge must send every parent point to its listed children; a terminal
certificate proves emptiness only for its pinned finite system.

At maximum degree $125$, family $F_2$ begins with

\[
A_0=(5,20),\quad A_0'=(1,0),\quad A_1=(7/5,2),\quad(m,n)=(3,5).
\]

The primitive edge direction is $(5,-1)$. With $z=x^{1/5}y$ and
$w=z^5=xy^5$, the common-root polynomial is a quartic $S(w)$ with a
distinguished nonzero double root.

## Results to use

- The truncated $(8,28)$ root has $25$ $P$- and $47$ $Q$-support
  monomials. Its weighted-degree-four obstruction matrix has rank $14/14$,
  so its required top vertices vanish and the exact root is empty.
- The full root has $61$ and $125$ support monomials. Its layer-four
  condition is a square; the closed $t_{1,1}=0$ child loses the required top
  vertices. On $t_{1,1}\ne0$, fifteen equations arise, and the six equations
  with zero-based indices $4,6,8,9,10,11$ are literally the imported compact
  toric empty system. Hence the full root is empty.
- Combining those exclusions with the inspected literature route excluding
  $(9,27)$ and reducing $(8,28)$ to the two roots proves, relative to those
  imports, that no characteristic-zero plane Keller counterexample has
  maximum coordinate degree strictly below $125$. No novelty or priority
  claim is made.
- For $F_2$, the reduced terminal quotient is already fixed:
  $\bar p=1-u$,
  $\bar q=1/5-3u/5+9u^2/25$, with degree-six passport
  $(5,1),(3^2),(3,1^3)$. The intervening normalized supports and two-point
  normal windows are not fixed.

## Example: the two closed (8,28) roots

The truncated rank-$14$ certificate and the full six-equation toric
projection are examples of complete terminal closure. They are not templates
that determine the degree-$125$ intermediate supports automatically.

## Live problem

Propagate the entire $F_2$ polynomial support through its distinguished
double-root shear, return to the quotient coordinate $u=z^5$, and determine
every intervening support, nonzero coefficient, and finite two-point normal
window.

## Tasks

### L8-T1 — Propagate the degree-125 F2 support

Inputs: the [degree-125 boundary seed](lane-8-source-packet.md),
the [exact seed checker](lane-8-source-packet.md),
the [terminal quotient program](lane-8-source-packet.md),
and the [face-rigidity program](lane-8-source-packet.md).

Deliverable: the finite list of normalized support polygons from the initial
$(5,20)$ edge through the $(7/5,2)$ terminal face, with every monomial map,
support inequality, gap-five congruence, required nonzero coefficient, and
normal-layer source/target window. If uniqueness fails, report all finite
alternatives and the first underdetermined choice.

Dependencies: the standard complete-chain corner formulas and the explicit
degree-six quotient face.

Limits: do not reprove the closed below-$125$ roots; no support point may be
discarded without an inequality, congruence, or routed complement.

### L8-T2 — Build the first post-bound obstruction operator

Inputs: L8-T1 and the exact terminal quotient.

Deliverable: the determinant layer operators and pole-filtered residue
adjoints on the recovered two-point windows, retaining every fresh kernel
parameter; locate the first nonzero obstruction or prove solvability through a
stated order.

Dependencies: L8-T1.

Limits: attachment across a second chart belongs to Lane 9 unless a full
overlap theorem is supplied.

Alternative connections: an actual-chain relation recovered in Lane 9 is
welcome if it constrains, rather than assumes, the L8-T1 support list.

## Limits

The below-$125$ statement is a proof assembly with imported reduction and
toric theorem. The proposed terminal descent beyond this point is a
**proof strategy — incomplete**; it is not used in the direct root closure.

## Direct sources

- [Direct closure proof](lane-8-source-packet.md)
- [Independent raw-support replay](lane-8-source-packet.md)
- [Lane 8/9 recovery summary](lane-8-source-packet.md)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-8-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
