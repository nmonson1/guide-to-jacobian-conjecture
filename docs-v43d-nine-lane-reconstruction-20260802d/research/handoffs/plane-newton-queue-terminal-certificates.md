---
title: "Model research brief — Plane Newton queue and terminal certificates"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Lane 8</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 2 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v16d · site release <code>living-guide-public-v43d-nine-lane-reconstruction</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/index.md).

!!! tip "Current proof sources — preferred"
    Use the [current source text and exact labels](../proof-sources/index.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.
# Lane 8: Plane Newton queue and terminal certificates

## Research objective

Prove that every branch produced by the normalized plane Newton reduction is
routed exhaustively to an exact terminal theorem.  The terminal certificates
are already strong; the missing theorem is the upstream DAG.

## Reusable mathematics

A primitive Newton-face Jacobian equation is an exact logarithmic derivative
and gives a Belyi map whose passport is determined by face exponents.  The
exponent lattice can be smaller than the fractional uniformizing cover.  In
the first degree-125 family, an ambient degree-30 problem with 11 dessin
classes reduces to one degree-six quotient.  The first five quotient problems
have degrees and class counts

```text
degrees       6,10,9,9,16
class counts  1, 1,1,2, 2.
```

The explicit reduced covers are isolated modulo source scaling.

For the stored degree-21 face,

```text
tau(z)=z*q(z)^2/p(z)^3
```

has passport `(2^10 1),(3^7),(17 1^4)`.  There are exactly five normalized
maps, in one quintic Galois orbit, with monodromy `A_21`.  The corresponding
source valuation has `(e,f)=(1,21)` over Borisov's `F_-5`; this excludes the
named Three-dessin framework, not the two Newton supports.  Relevant units:
[`JCG-34B30410`](../working-mathematics/units/JCG-34B30410.md), [`JCG-2B32290C`](../working-mathematics/units/JCG-2B32290C.md), and [`RMU-8E7E56B5`](../working-mathematics/units/RMU-8E7E56B5.md).

Starting from the pinned normalized supports, the raw-support replay
reconstructs the lower face, all layer matrices, the truncated contradiction,
and the 15 full-support equations.  Every equation has exact filtered-residue
provenance.  Exact conclusions include:

- the vertex-saturated truncated support is empty in characteristic zero;
- both stored exceptional branch ideals are unit ideals by exact
  Nullstellensatz identities;
- the displayed six-polynomial toric system is empty in characteristic zero
  via the 296-point special fibre and Nakayama; and
- after the canonical `k=4` rechart, the stored layer-five-through-seven
  support and chart-matching system has no solution ([`JCG-BCEB7F45`](../working-mathematics/units/JCG-BCEB7F45.md)).

The older 7,121-row Macaulay minor is conditional on verifying that its rows
are the complete target basis containing `1` and that all target rows are
used.  The later branchwise and toric certificates provide stronger exact
interfaces for their displayed systems.

## What is not known

No independent artifact proves that every hypothetical plane counterexample
below degree 125 reaches these two supports and then one of the stored
terminal systems.  Upstream face selection, saturation, normalization,
deficiency layers, branch conditions, and rechart operations are logical
dependencies.  The public below-125 result is credited external context; the
repository does not claim priority for it.

## Exact live problem

Regenerate the complete queue as a finite DAG.  Every node must store:

- support and valuation data;
- face equation and primitive lattice quotient;
- saturation and normalization operations;
- deficiency equations and all free parameters;
- exhaustive branch conditions;
- chart and transition data; and
- child identifiers or an exact terminal locator.

Every edge must have a proof of exhaustiveness over its stated field and open
locus.


## Useful deliverable

Return one self-contained mathematical artifact that advances or sharply
reformulates the exact live problem.  It may solve a listed task, isolate a
smaller exact subproblem, prove that an input is insufficient, produce a
counterexample to the proposed route, or develop a stronger connection with
another lane.  Include the exact statement, a complete argument or
reproducible computation contract, dependencies, and limitations.  A
rigorous partial result is useful; it need not close the whole lane.

## Tasks

### P6-L8A — Queue reconstruction

Actor: `online_model`. Status: ready.

Write the mathematical DAG from the two normalized supports to terminal
systems, identifying every missing edge.

### P6-L8B — Machine-readable routing replay

Actor: `local_symbolic`. Status: blocked on P6-L8A.

Encode every node and edge with content hashes and replay the deterministic
transformations from fresh paths.

### P6-L8C — Independent edge audit

Actor: `online_model`. Status: blocked on P6-L8A.

Re-derive the face, lattice, and branch splits without using stored expected
outputs as premises.

## Do not do

- Do not infer queue exhaustiveness from a terminal unit ideal.
- Do not use the degree of a fractional cover when the exponent lattice gives
  a smaller quotient.
- Do not saturate away a boundary branch without opening its replacement
  chart.
- Do not count the credited below-125 theorem as an internal proof.

The retained-unit and proof-source pages linked above are the public mathematical record for this lane.

[Back to the portfolio hub](state-of-the-program.md)
