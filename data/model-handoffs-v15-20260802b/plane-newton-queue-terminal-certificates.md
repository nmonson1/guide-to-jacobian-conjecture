# Lane 8: Plane Newton queue and terminal certificates

## Research objective

Prove that the exact stored terminal exclusions in the plane program occur at
the leaves of a complete Newton/face pipeline.  The terminal certificates are
already exact for their displayed systems; the missing theorem is upstream
exhaustiveness.

Use the [Program 6 dossier](plane-boundary-obstructions.md) for the normalized
supports, complete-chain conventions, Belyi passports, proof links, and exact
certificate inventory.  [Lane 9](plane-chart-correspondence-global-attachment.md)
addresses the complementary local-to-global chart theory.

## Reusable mathematics

A Newton face of a hypothetical plane Keller pair gives a one-variable
Jacobian differential equation.  After normalization, the resulting rational
map is Belyi and its ramification passport is fixed by the face exponents.  In
the first degree-125 family, an ambient degree-30 passport has 11 classes while
the exponent lattice selects one degree-six quotient.  The first five quotient
problems have degrees `6,10,9,9,16` and class counts `1,1,1,2,2`.

For the stored degree-21 full-support specialization over the explicit
quintic field, the missing layer-four operation is the `k=4` transition to an
adjacent complete-chain chart.  There the Jacobian equations force a common
approximate root, and the complete layers five through seven have no solution.
The corresponding affine and toric unit-ideal certificates are exact and
replay for that stored terminal system.

This does not prove that every hypothetical counterexample below degree 125 is
routed to one of the stored terminal systems.  Saturations, normalizations,
face choices, deficiency layers, and chart transitions upstream are logical
dependencies, not implementation details.

## Live problem

Regenerate the queue from the two normalized supports.  For every node, store:

- the support and weight/valuation data;
- the face equation and primitive lattice quotient;
- saturation and normalization operations;
- deficiency-layer equations and all free parameters;
- the precise branch conditions;
- the complete-chain chart and transition used;
- the child identifiers or terminal certificate;
- content hashes for code, input, and output.

Then prove that each branch split is exhaustive over the stated ground field
and open locus.  Support-aware normal coordinates are useful only if the
triangular support filtration and residue adjoint are transported exactly.
Compare selected passport and rank calculations through an independent
derivation, but keep that as a release check rather than a substitute for
queue completeness.

## Failure modes to avoid

- A terminal unit ideal does not prove that the terminal system is reached.
- A fractional uniformizing cover may descend to a smaller lattice quotient;
  passport degree must follow the exponent lattice.
- Saturating too early can delete a boundary branch that needs a new chart.
- Reusing a fixed-chart kernel as a chart transition changes the mathematical
  problem.
- The public below-125 statement is external context until this dependency
  chain is complete.

## Useful deliverable

The best artifact is a finite, inspectable DAG from normalized supports to
terminal systems, accompanied by a proof of every routing rule.  A discovered
uncovered branch is valuable and should be promoted as a new candidate queue
node.  Alternative Newton or valuation organizations are welcome if they give
the same exhaustiveness with fewer branches and retain exact correspondence to
the terminal certificates.
