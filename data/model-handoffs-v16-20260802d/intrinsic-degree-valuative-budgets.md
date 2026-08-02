# Lane 5: Intrinsic degree and valuative budgets

## Research objective

Extract a lower bound on ordinary coordinate degree from the finite cover,
image algebra, or boundary data in a way that survives polynomial left-right
equivalence.  A budget for one determinant-arc presentation is not enough.

This lane overlaps the [low-degree program](minimum-degree-and-quartic-exclusions.md),
[stable moduli](stable-moduli.md), and
[plane boundary obstructions](plane-boundary-obstructions.md).  Those deeper
dossiers supply the surrounding proof and computation routes; the focused
page below gives the corrected finite frontier.


## Reusable mathematics

Use the image algebra

```text
A=k[P,Q,R]
```

to remove target-coordinate changes from the problem.  For the chosen source
semidegree, put

```text
a=delta(x),  b=delta(y),  h=delta(y+xz/3).
```

Then the exact identities are

```text
delta(R)=2a+h,
delta(Q)=2a+h+2b,
delta(P)=2a+h+3b.
```

The coordinate identity reduces low-budget filtrations to a finite list.
Ramification has `e in {1,3}`; the tame inertia character eliminates `e=3`.
Thus coordinate-infinity valuations are unramified and the `S_3` closure has
trivial inertia there.

For every classified stratum with `delta(Q)<=9`, exact certificates give

```text
trdeg C[A_(<=6)^delta] <= 2.
```

Uniform quadratic `z`-shears are closed by explicit minors, with the cubic and
quartic support blocks independent of the shear parameter.  Hence any
degree-six left-right representative in this normalization must lie in the
unramified branch `delta(Q)>=10`.

On the discriminant normalization, the corrected normal operator satisfies

```text
N(f)=-1/[4(2-3ct)] * overline(partial_P f).
```

Together with `partial_t` and `partial_c`, its determinant is the Jacobian.
This is the exact conormal/Wronskian bridge needed for the remaining branch.

## What is not known

No proof shows that low-degree functions have zero corrected Wronskian when
`delta(Q)>=10`.  Nor is the semidegree proved invariant under arbitrary
source changes or stabilization.

The proposed simplex filtration is not yet a broader relaxation.  Exact
simplex Hilbert function plus degree-one Rees generation recovers ordinary
coordinate degree; without generation the admissible class is undefined.
The volume-form value `-4` is necessary but not sufficient.

## Exact live problem

Prove or refute the following bounded-Wronskian statement:

> In the unramified `delta(Q)>=10` branch, the corrected normal Wronskian of
> every element of `A_(<=6)^delta` vanishes.

A proof eliminates the last filtration branch.  A counterexample must be
tested for actual membership in the image algebra and for its transformation
under source shears.


## Useful deliverable

Return one self-contained mathematical artifact that advances or sharply
reformulates the exact live problem.  It may solve a listed task, isolate a
smaller exact subproblem, prove that an input is insufficient, produce a
counterexample to the proposed route, or develop a stronger connection with
another lane.  Include the exact statement, a complete argument or
reproducible computation contract, dependencies, and limitations.  A
rigorous partial result is useful; it need not close the whole lane.

## Tasks

### L5-T1 — Transformation law

Actor: `online_model`. Status: ready.

Give the exact behavior of `delta`, `N`, and the Wronskian under source and
target triangular automorphisms and under the chosen normalization.

### L5-T2 — Residual bounded-Wronskian theorem

Actor: `online_model`. Status: blocked on L5-T1.

Use conductor, conormal, or image-algebra arguments to control
`A_(<=6)^delta` when `delta(Q)>=10`.

### L5-T3 — Exact counterexample search

Actor: `local_symbolic`. Status: blocked on a finite formulation from L5-T2.

Search only a hash-pinned finite coefficient space and report the precise
mathematical meaning of either a witness or a unit certificate.

## Do not do

- Do not call a coordinate semidegree an intrinsic invariant without its
  transformation law.
- Do not infer a bound from dimension counts alone.
- Do not call the simplex proposal a relaxation while degree-one generation
  is present.
- Do not treat the volume-form value as sufficient for left-right
  realizability.

The retained-unit and proof-source pages linked above are the public mathematical record for this lane.
