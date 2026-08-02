---
title: "Model research brief — Plane Newton queue and terminal certificates"
description: "A self-contained mathematical handoff for a research model."
---

# Lane 8: Plane Newton queue and terminal certificates

<p class="claim-tag">Lane 8 · Updated 2 August 2026</p>

## Problem and scope

The normalized Newton reduction for a hypothetical plane Keller
counterexample repeatedly chooses a Newton face, passes to its primitive
exponent lattice, normalizes its face equation, introduces deficiency layers,
and branches when coefficients or pivots vanish. Lane 8 asks for a finite
directed acyclic graph proving that this routing is exhaustive and reaches
exact terminal theorems.

A plane Keller map is a polynomial map `(P,Q):A^2->A^2` with nonzero
constant Jacobian determinant; a counterexample would be noninvertible.

The repository already has strong terminal certificates. Their existence
does not prove that every initial map reaches their pinned systems.

## Setup and notation

A queue node records `(support, valuation, chart, equations, open locus)`. An
edge records one exhaustive operation: face selection, primitive-lattice
quotient, saturation plus its complementary chart, normalization, deficiency
layer, coefficient branch, or rechart. A terminal node links to a theorem or
certificate for exactly its stored system.

Two normalized support families are used by the current below-125 reduction.
For coordinates `x^i y^j`, their Newton polygons are:

```text
truncated P: (0,0),(1,0),(8,14),(8,16)
truncated Q: (0,0),(2,1),(12,21),(12,24)
full P:      the truncated P vertices plus (0,8)
full Q:      the truncated Q vertices plus (0,12).
```

Each support consists of every lattice point in the displayed polygon. Its
deficiency is `j-2i+2` for `P` and `j-2i+3` for `Q`. The truncated case has
parameter layers `{1:2,2:3,3:1}` and stops at layer five; the full case has
`{1:2,2:3,3:3,4:1}` and stops at layer eight. The exact public
[raw-support reconstruction input](lane-8-reconstruction-input.md) contains
the field relations and complete reconstruction program that turns these
supports into the lower-face and deficiency-layer equations. The support
polygons alone are not full queue nodes: their coefficient normalizations,
equations, and open loci must be recovered and recorded from that input.
Terminal systems are also described in
[`manuscripts/06-plane-boundary/main.tex`](../proof-sources/06-plane-boundary/main.md) and its appendices. Here “below 125” means the imported reduction for pairs whose
maximum coordinate degree is below 125; completing this DAG audits that
reduction, not an independent proof of its external starting theorem. The degree-21
stored face has

```text
tau(z)=z*q(z)^2/p(z)^3,
passport (2^10 1),(3^7),(17 1^4).
```

The *three-dessin framework* is the source's comparison of the three Belyi
maps obtained from the primitive logarithmic-derivative face equations for
the coordinate pair and Jacobian relation. The degree-21 divisor data exclude
that simultaneous framework, not the two Newton supports themselves.

## Reusable mathematics

A primitive face equation is an exact logarithmic derivative and gives a
Belyi map with passport determined by face exponents. Passing to the
primitive exponent lattice can lower the cover degree. The first five
quotient problems have

```text
degrees       6,10,9,9,16
class counts  1, 1,1,2, 2.
```

For the degree-21 face there are exactly five normalized maps in one quintic
Galois orbit, all with monodromy `A_21`. Units: [`JCG-34B30410`](../working-mathematics/units/JCG-34B30410.md),
[`JCG-2B32290C`](../working-mathematics/units/JCG-2B32290C.md), [`RMU-8E7E56B5`](../working-mathematics/units/RMU-8E7E56B5.md).

From the pinned supports, exact replays reconstruct the lower face, layer
matrices, truncated contradiction, and 15 full-support equations. The
truncated-root result now has a standalone proof packet: the exact field
relations reconstruct the fifteen quintics and open factors, and fourteen
coefficient vectors have a nonzero exact spanning minor (with compact value
`894 mod 2053`). Unit [`RMU-6D8E0010`](../working-mathematics/units/RMU-6D8E0010.md) replaces the former assertion-only
record. Proof and replay inputs:
[`research-notes/lane8-proof-queue-20260802-v1/`](lane-8-source-packet.md). Exact leaves prove:

- the vertex-saturated truncated support is empty in characteristic zero;
- both stored exceptional branch ideals are unit ideals;
- the six-polynomial toric system is empty via its 296-point special fibre
  and Nakayama; and
- after the canonical `k=4` rechart, the stored layer-five-through-seven
  matching system has no solution ([`JCG-BCEB7F45`](../working-mathematics/units/JCG-BCEB7F45.md)).

The older 7,121-row minor remains conditional on completeness of its target
basis. Branchwise certificates are the preferred terminal interfaces.

## Exact live problem

Audit the exact raw-support reconstruction program as mathematics. Starting
from its displayed polygons and pinned quintic-field relations, record every
node that the program actually constructs: normalized coefficients,
equations, valuation/deficiency layer, and open condition. For each program
transition, state the algebraic operation and what it proves. Stop at the
first claimed queue edge for which the program or proof source omits a
complementary branch. This does not ask the model to reconstruct an
unspecified DAG: the executable input is public, and identifying the first
unimplemented routing edge is an acceptable complete deliverable.

## Tasks and deliverables

### P6-L8A — Routing DAG and first missing edge

Status: ready.

Inputs: the two vertex lists, deficiency functions, and layer ranges above;
the exact [raw-support reconstruction input](lane-8-reconstruction-input.md),
[`RMU-6D8E0010`](../working-mathematics/units/RMU-6D8E0010.md) and its reconstruction/certificate packet, the three retained
dessin units, and the linked terminal proof sources.

Deliverable: a node/edge table for the path actually generated by the public
program, with hashes for its starting data, and the first exact point at which
an exhaustive queue edge is absent. A full DAG is required only if every
branch is in fact supplied; otherwise the missing parent, open locus, and
unrouted complement are the result.

### P6-L8B — Machine-readable replay

Status: local CAS task; blocked on P6-L8A.

Deliverable: encode accepted nodes and deterministic edges with content
hashes and replay them from fresh versioned paths.

### P6-L8C — Independent edge proof

Status: blocked on the first gap found by P6-L8A.

Deliverable: rederive that face, lattice, or branch split without using stored
expected output as a premise.

## Scope cautions

- A terminal unit ideal proves only its pinned system.
- Use the primitive exponent lattice, not a larger fractional cover.
- Saturation requires routing its complementary boundary chart.
- The credited below-125 theorem is external context, not an internal proof.

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
