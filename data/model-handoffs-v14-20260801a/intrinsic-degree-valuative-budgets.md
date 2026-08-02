# Lane 5: Intrinsic degree and valuative budgets

## Research objective

Connect finite-cover or boundary data to ordinary coordinate degree in a way
that survives arbitrary polynomial left-right equivalence.  The target is an
intrinsic lower bound on the whole orbit, or a canonical normalization that
does not increase degree, rather than a budget for one determinant-arc
presentation.

Fix polynomial rings

```text
A = k[u1,u2,u3],        B = k[x1,x2,x3]
```

and the injective pullback `iota:A -> B` of a dominant polynomial map.  The
object that can carry degree information is the **embedded inclusion**
`iota:A -> B`, not the abstract image algebra: abstractly `iota(A)` is again a
polynomial ring.  A target automorphism changes the coordinate frame of `A`
without changing the subalgebra `iota(A)`, while a source automorphism moves
that subalgebra inside `B`.

Define the left-right orbit degree by

```text
d_LR(iota) =
  min over sigma in Aut(B), tau in Aut(A)
  of max_i deg_x sigma(iota(tau(ui))).
```

A Lane 5 budget should be a quantity `b(iota)` with

```text
b(sigma o iota o tau) = b(iota),        b(iota) <= d_LR(iota),
```

or it should arise from a canonicalization procedure whose output degree never
exceeds the input degree.

This lane overlaps [Program 2](minimum-degree-and-quartic-exclusions.md),
[Program 4](stable-moduli.md), and
[Program 6](plane-boundary-obstructions.md).  It may also constrain the
realization problem in [Lane 6](homogeneous-realization-compression.md).

## Scope repair for the existing filtration calculation

For a fixed source automorphism `sigma`, define

```text
F_d^sigma A = {a in A : deg_x sigma(iota(a)) <= d},
C_d^sigma   = k[F_d^sigma A].
```

The first object is a filtered vector space, not generally a subalgebra.  Thus
the precise interpretation of the former notation
`trdeg A_(<=6) <= 2` is

```text
trdeg_k C_6^sigma <= 2.
```

The current program records exact certificates for the **listed** normalized
source filtrations with `delta(Q) <= 9`.  Until the definition of `delta(Q)`,
the complete case inventory, the localizations and saturations, and direct
artifact locators are published, retain only the following scoped statement:

> For every filtration explicitly represented in that certificate packet,
> `trdeg_k C_6^sigma <= 2`.

This does not quantify over arbitrary polynomial source automorphisms.  The
unramified `delta(Q) >= 10` family is a stated residual family, but closing it
would still not prove full orbit-minimality unless every source coordinate
frame is first routed to the listed cases or to that residual family without
increasing degree.

The companion/Jordan moment budget in Program 2 remains a useful
degree-specific model and audit lens.  Its hypotheses refer to one scaled
determinant arc and are not known to be left-right invariant.

## Exact orbit-degree criterion

**Lemma.** Let `D >= 0`.  If `d_LR(iota) <= D`, then for some source
automorphism `sigma`,

```text
C_D^sigma = A.
```

In particular, `trdeg_k C_D^sigma = 3`.

**Proof.** Choose `sigma` and `tau` realizing a presentation of degree at most
`D`.  The three elements `tau(u1),tau(u2),tau(u3)` lie in `F_D^sigma A`.
They form a polynomial coordinate frame of `A`, so they generate `A` as a
`k`-algebra.  Therefore `C_D^sigma=A`.  ∎

Consequently,

```text
if trdeg_k C_D^sigma <= 2 for every sigma in Aut(B),
then d_LR(iota) >= D+1.
```

For the fixed map with displayed maximum degree seven, a universal theorem at
`D=6` would prove `d_LR(iota)=7` for that left-right orbit.  It would not by
itself prove that every Keller counterexample has degree at least seven, nor
that every affine realization of the same finite normalization has the same
minimum degree.

This lemma isolates the missing quantifier: the existing certificates concern
named filtrations; the orbit theorem requires all source coordinate frames or
a proved non-degree-increasing reduction to a complete normal-form list.

## A valuative minimax formula

Let `V_infty(B)` be the divisorial valuations of `Frac(B)`, trivial on `k`,
that have a pole on `B`.  For `v in V_infty(B)`, write

```text
delta_v(f) = max(0,-v(f)).
```

For a source coordinate frame `x'=(x1',x2',x3')` of `B` and a target
coordinate frame `u'=(u1',u2',u3')` of `A`, put

```text
M_v(x')       = max_i delta_v(xi'),
M_v(iota(u')) = max_j delta_v(iota(uj')).
```

**Proposition.** For every pair of coordinate frames,

```text
deg_x' iota(u')
  = sup over v in V_infty(B) of M_v(iota(u')) / M_v(x').
```

**Proof.** If a polynomial `p` has `x'`-degree at most `d`, the valuation
inequality applied to its monomials gives

```text
delta_v(p) <= d M_v(x')
```

for every `v`.  This proves the upper bound.  For the reverse inequality, use
the divisorial valuation of the hyperplane at infinity in the projective
compactification defined by the coordinate frame `x'`.  It satisfies
`delta_v(p)=deg_x'(p)` and `M_v(x')=1`.  Taking the maximum over the target
coordinates gives equality.  ∎

Therefore the orbit degree has the exact, though initially tautological,
description

```text
d_LR(iota) =
  min over source frames x' and target frames u'
  sup over v in V_infty(B)
  M_v(iota(u')) / M_v(x').
```

This advances the valuative route by identifying the precise replacement
problem.  The family of all valuations gives equality but is not effective.
A useful theorem must extract a smaller computable family from the finite
cover, conductor, relative-Jacobian divisor, or marked boundary while
preserving a lower bound after minimization over all coordinate frames.

More precisely, suppose a family `W(iota) subset V_infty(B)` satisfies the
source-equivariance rule

```text
W(sigma o iota o tau) = sigma_* W(iota)
```

and is unchanged by merely replacing target coordinates.  Then

```text
b_W(iota) =
  inf over source frames x' and target frames u'
  sup over v in W(iota)
  M_v(iota(u')) / M_v(x')
```

is left-right invariant and satisfies `b_W(iota) <= d_LR(iota)`.  The concrete
Lane 5 target is now:

```text
construct W(iota) canonically and prove b_W(iota) > 6
for the fixed three-sheeted inclusion.
```

## Mandatory shear test

A fixed compactification valuation is not enough.  For the standard
hyperplane-at-infinity valuation and the triangular coordinate frame

```text
(x, y + x^N, z),
```

one has

```text
M_v(x, y + x^N, z) = N.
```

Thus a budget based on a fixed valuation can be diluted by source shears unless
the valuation family transports with the embedded cover or a canonical
normalization prevents the shear.  Every proposed `W(iota)` should be tested
against:

1. source and target shears;
2. triangular automorphisms of unbounded degree;
3. stabilization by identity variables;
4. the known degree-seven presentation; and
5. at least one nontrivially changed presentation of the same orbit.

A counterexample to a candidate family is a useful Lane 5 result.

## Simplex/Rees collapse lemma

The proposed “simplex-bounded” relaxation needs explicit axioms.  The
following obstruction is exact.

**Lemma.** Let `G_d B` be an exhaustive separated multiplicative filtration
with finite-dimensional pieces and `G_0 B=k`.  Suppose, for every `d >= 0`,

```text
dim_k G_d B = binomial(d+3,3),
```

and `gr_G B` is generated in degree one.  Then there are polynomial
coordinates `g1,g2,g3` on `B` for which `G_d B` is exactly the ordinary
degree-at-most-`d` space.

**Proof.** The degree-one part of `gr_G B` has dimension three, so degree-one
generation gives a graded surjection
`k[T1,T2,T3] -> gr_G B`.  The displayed dimensions give the same Hilbert
function on both sides, hence the surjection is an isomorphism.  Lifting the
three degree-one generators and inducting on the filtration shows
`B=k[g1,g2,g3]` and that `G_d B` is their ordinary degree filtration.  ∎

Thus exact simplex dimensions in every degree plus degree-one generation do
not define a broader class.  If generation is allowed in higher degrees, the
admissible class still needs finite-generation, functoriality, normalization,
and degree-comparison axioms, together with a concrete example not equivalent
to ordinary degree.

The source volume-form value `-4` remains only a necessary anchor.  It does not
recover coordinate pole orders, the value semigroup, the associated graded
algebra, or the affine opening.  Dimension counts alone do not define a degree
relaxation.

## Live tasks

**L5-T1 — Publish and audit the filtration packet.**  Define `delta(Q)`, list
every `delta(Q) <= 9` case, state the coefficient fields, localizations,
saturations, and extraction lemma, and attach hash-pinned replay commands.
Done when an independent reader can verify exactly which `sigma` are covered
and why each certificate implies `trdeg_k C_6^sigma <= 2`.

**L5-T2 — Prove source-frame coverage or find a counterexample.**  Route every
polynomial source coordinate frame, without increasing degree, to an indexed
case or the residual unramified family.  Stop and preserve any triangular
shear or wild frame outside the classification.

**L5-T3 — Build a canonical valuation family.**  Extract `W(iota)` from the
embedded finite cover and affine opening, prove the equivariance rule above,
and compute `b_W` on the fixed map and changed presentations.  A value greater
than six proves orbit-minimal degree seven for the fixed map.

**L5-T4 — Residual theorem.**  After L5-T2 has established coverage, prove the
filtered conormal, Wronskian, or conductor theorem for unramified
`delta(Q) >= 10`.

## Useful deliverable

Return one of:

- a complete certificate contract plus source-frame coverage theorem;
- a canonical valuation family with its transformation law and a computed
  degree consequence;
- a non-degree-increasing canonicalization procedure; or
- a decisive shear or stabilization counterexample to a proposed budget.

State separately what is proved for named presentations, the fixed
left-right orbit, all realizations of the fixed cover, generic-degree-three
maps, and arbitrary Keller maps.
