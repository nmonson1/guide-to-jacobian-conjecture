---
title: "Plane Case"
description: "What remains open in dimension two, why the three-dimensional construction does not descend directly, and which current directions are established or provisional."
---

# The Plane Case

<p class="dek">The counterexample settles every dimension at least three. It
does not settle dimension two, where the classical Jacobian conjecture remains
open.</p>

## The surviving conjecture

The plane Jacobian conjecture asks whether every polynomial map
\(F:\mathbf C^2\to\mathbf C^2\) with nonzero constant Jacobian determinant is
a polynomial automorphism. The three-variable counterexample does not
contradict this statement, and stabilization only moves upward in dimension.

The plane problem has roots at least as far back as Ludwig Kraus's 1884 paper.
The guide records both the historical statement and the gap in the proposed
argument at infinity; it does not treat the old paper as a proof.

- [The Plane Jacobian Conjecture Remains Open](collections/plane-jacobian-conjecture.md)
- [Kraus's Statement and Proof Gap](collections/kraus-statement-and-proof-gap.md)

## Why direct descent fails

The known counterexample is a three-dimensional marked-root incidence space.
Taking an arbitrary slice does not preserve all three properties needed at
once: an affine-plane source, an everywhere nonzero Jacobian, and more than one
point in a fiber.

The simplest restrictions illustrate the problem. Nonzero fixed slices have
the wrong affine topology; the zero slice contains a trivial affine-plane
sheet; low-degree affine-plane components are excluded; and the natural
one-pole lift cannot keep constant Jacobian. These are obstructions to the
obvious descent mechanisms, not a proof of the plane conjecture.

- [Why Direct Slicing Does Not Produce a Plane Counterexample](collections/dimension-descent-obstructions.md)
- [A Conceptual Plane Obstruction](collections/conceptual-plane-obstruction.md)
- [Puiseux Obstruction and a Failed Extension](collections/puiseux-obstruction-and-failed-extension.md)

## Established boundary versus working research

<div class="label-list">
  <div>
    <strong>Established</strong>
    <span>The plane conjecture is open; the displayed three-dimensional map does not itself descend; published degree bounds and classical reductions retain their stated scopes.</span>
  </div>
  <div>
    <strong>Credited public result</strong>
    <span>The degree-below-125 conclusion is credited to ratto3423. This guide does not replace that work with a concurrent internal derivation.</span>
  </div>
  <div>
    <strong>Working draft</strong>
    <span>The Belyi, dessin, Puiseux, log-geometric, and normal-jet developments are current research notes, not established literature.</span>
  </div>
  <div>
    <strong>Still missing</strong>
    <span>The current program retains explicit upstream completeness and global-attachment gaps; closing a finite terminal system is not yet a proof of the plane conjecture.</span>
  </div>
</div>

## The current boundary program

A hypothetical plane counterexample has complicated behavior at infinity.
The working program translates that behavior through several compatible
languages:

1. Newton faces and Puiseux expansions isolate possible branches.
2. A quotient cover produces a finite Belyi passport problem.
3. Dessins constrain the combinatorics of that cover.
4. A normal-boundary operator propagates compatibility through successive
   jets.
5. Exact arithmetic tests the terminal finite systems.

The attraction of this approach is that it turns a global polynomial problem
into finite, checkable pieces. Its danger is also clear: the reduction is only
conclusive if every upstream alternative is covered and every local boundary
object attaches to one global polynomial map.

[Read the Plane Boundary Obstructions program](research/programs/plane-boundary-obstructions.md){ .md-button .md-button--primary }
[Read the working manuscript, v12](assets/manuscripts/06-plane-boundary-obstructions-2026-07-29-v12.pdf){ .md-button }

## Open frontiers

- [The Global Attachment Problem](collections/f2-global-attachment-problem.md)
- [Six-Sheet Plane Constraints](collections/six-sheet-plane-constraints.md)
- [Three-Dessin Uniqueness](collections/three-dessin-uniqueness.md)
- [Degree Below 125](collections/degree-below-125-theorem.md)
- [Open Problems After the Counterexample](collections/research-agenda.md)
