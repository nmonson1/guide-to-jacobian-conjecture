---
title: "Model research brief — Intrinsic degree and valuative budgets"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Lane 5</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 2 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v15 · site release <code>living-guide-public-v42-program1-reaudit</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/index.md).

!!! tip "Current proof sources — preferred"
    Use the [current source text and exact labels](../proof-sources/index.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.
# Lane 5: Intrinsic degree and valuative budgets

## Research objective

Connect finite-cover or boundary data to ordinary coordinate degree in a way
that survives arbitrary polynomial left-right equivalence.  The target is an
intrinsic lower bound or monotone, not merely a budget for one determinant-arc
presentation.

This lane overlaps [Program 2](minimum-degree-and-quartic-exclusions.md),
[Program 4](stable-moduli.md), and
[Program 6](plane-boundary-obstructions.md).  It may also constrain the
realization problem in [Lane 6](homogeneous-realization-compression.md).

## Reusable mathematics

For the listed source filtrations with `delta(Q) <= 9`, exact certificates
give

```text
trdeg A_(<=6) <= 2,
```

where `A=k[P,Q,R]` is the image subalgebra in the stated normalization.  The
remaining filtered case is unramified `delta(Q) >= 10`, together with the need
for a conceptual filtered-conormal, Wronskian, or conductor theorem.  The
companion/Jordan moment budget in Program 2 is a useful degree-specific model,
but its hypotheses refer to one scaled determinant arc and are not known to be
left-right invariant.

Target-coordinate changes are absorbed by the image subalgebra.  By contrast,
the source volume-form value `-4` is only a necessary anchor and not a complete
orbit invariant.  Dimension counts alone do not define a degree relaxation.

One tempting proposal—call a presentation simplex-bounded—has not yet produced
a broader search class.  Exact simplex dimensions plus degree-one Rees
generation force ordinary coordinate degree; if the generation axiom is
removed, the admissible class is undefined.  The SAGBI and
Abhyankar--Moh analogies therefore remain heuristics until the valuation and
generation axioms are stated.

## Live problem

Choose one of three concrete routes:

1. Prove the residual conormal/Wronskian theorem for unramified
   `delta(Q) >= 10`.
2. Define and test a higher-generated Rees filtration that is strictly broader
   than ordinary degree but still functorial under the intended equivalence.
3. Translate Program 6 conductor and Newton-boundary data into a three-variable
   valuative budget, with a proof that it depends on the finite cover or image
   algebra rather than the chosen coordinates.

Plausible inputs include divisorial valuations, pole divisors, marked boundary
multiplicities, Newton data, and relative-Jacobian divisors.  A candidate
budget should be tested immediately against source shears, target shears,
triangular automorphisms, stabilization, and the known explicit map.  A
counterexample to a natural budget is useful because it prevents a long search
inside a non-invariant class.

## Useful deliverable

Give a definition, prove its transformation law, compute it on the fixed
three-sheeted cover and at least one changed presentation, and state the exact
degree consequence.  If full invariance is too strong, identify the weakest
canonical normalization that makes the quantity monotone without increasing
degree.  Feel free to replace the current filtration language with a better
geometric invariant if it advances the same objective.

[Back to the portfolio hub](state-of-the-program.md)
