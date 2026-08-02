# Lane 5: Intrinsic degree and valuative budgets

## Research objective

Connect finite-cover or boundary data to ordinary coordinate degree in a way
that survives arbitrary polynomial left-right equivalence. The target is an
intrinsic lower bound on the whole orbit, or a canonical normalization that
does not increase degree.

Fix

```text
A = k[u1,u2,u3],        B = k[x1,x2,x3]
```

and an injective pullback `iota:A -> B`. The degree-bearing object is the
embedded inclusion, not the abstract image algebra. Define

```text
d_LR(iota) =
  min over sigma in Aut(B), tau in Aut(A)
  of max_i deg sigma(iota(tau(ui))).
```

This lane overlaps [Program 2](minimum-degree-and-quartic-exclusions.md),
[Program 4](stable-moduli.md), and
[Program 6](plane-boundary-obstructions.md). It may also constrain
[Lane 6](homogeneous-realization-compression.md).

## Reusable mathematics

For a source automorphism `sigma`, set

```text
F_d^sigma A = {a in A : deg sigma(iota(a)) <= d},
C_d^sigma   = k[F_d^sigma A].
```

If `d_LR(iota)<=D`, then `C_D^sigma=A` for some `sigma`: a degree-`D`
target coordinate frame lies in `F_D^sigma A`. Therefore

```text
trdeg C_D^sigma <= 2 for every sigma
  implies d_LR(iota) >= D+1.
```

For the fixed map, a universal theorem at `D=6` would prove orbit-minimal
degree seven. It would not by itself prove a lower bound for every Keller
counterexample.

### Exact standard and affine theorem

For the displayed inclusion `S=k[P,Q,R] subset k[x,y,z]`, the new exact
common-fiber certificate proves

```text
S intersect B_{<=6} = span_k{1,Q,R}.
```

Thus `C_6=k[Q,R]` has transcendence degree two. Since affine source
automorphisms preserve `B_{<=6}`, for every affine `L`,

```text
L(S) intersect B_{<=6} = span_k{1,L(Q),L(R)}.
```

The certificate uses 84 source monomials, 81 exact rational common-fiber
difference rows, and a nonzero `81 x 81` minor modulo `1000003`.

### The all-elementary-monomial-shear theorem

Let `i!=j`, `N>=2`, and `c in k`. For the source automorphism

```text
sigma(x_i)=x_i+c*x_j^N
```

fixing the third coordinate, one has

```text
sigma(S) intersect B_{<=6}
  = span{1,Q,R}        if c=0;

  = span{1,sigma(R)}   if c!=0 and deg sigma(R)<=6;

  = k                  if c!=0 and deg sigma(R)>6.
```

Consequently every nontrivial single elementary monomial shear satisfies

```text
trdeg k[sigma(S) intersect B_{<=6}] <= 1.
```

No such source change can expose three algebraically independent target
functions of degree at most six.

The proof has three parts.

1. **Finite exact range.** Eighty-one exponent/direction cases below the
   structural thresholds have exact rank-82 or rank-83 common-fiber
   certificates. Ten kernels are `span{1,sigma(R)}` and 71 are `k`.

2. **Infinite weight-separated tails.** The source torus has weights
   `(-1,1,2)` on `(x,y,z)`, while `P,Q,R` have weights `(2,1,-1)`.
   `B_{<=6}` has weights in `[-6,12]`, of width 18. Write a shear as
   `exp(cD)`, with homogeneous derivation `D=x_j^N partial_{x_i}` of weight
   `e`. When `|e|>18`, the terms in `exp(-cD)g` coming from different weight
   components of `g in B_{<=6}` cannot collide. If
   `g in exp(cD)(S)`, every weight component of `g` already lies in `S`;
   the standard theorem reduces `g` to `span{1,Q,R}`. A single exact
   three-point fiber over `(P,Q,R)=(0,1/11,-1320)` shows uniformly in `N`
   that neither `D(Q)` nor `D(R)` belongs to `S`, so only constants remain.
   The thresholds are

   ```text
   z+x^N: 17    y+x^N: 18    x+y^N: 18
   z+y^N: 21    y+z^N: 10    x+z^N: 9.
   ```

3. **All coefficients.** Torus conjugation reduces every nonzero
   nonresonant coefficient to one. The sole resonant family is
   `z -> z+c*y^2`. It preserves the torus grading, so `B_{<=6}` splits into
   19 spaces of dimension at most eight. Thirty-three exact rational minors
   have gcd `1` in every weight except weight one, where the gcd is `c`.
   Hence there are no exceptional nonzero coefficients:
   `sigma_c(S) intersect B_{<=6}=span{1,sigma_c(R)}` for every `c!=0`.

The complete replay is in

```text
research-notes/lane5-degree-budgets/
  all_elementary_monomial_shears.py
  all_elementary_monomial_shears.json
  resonant_weight_certificate.py
  resonant_weight_certificate.json
```

This theorem covers every single elementary monomial shear, all exponents,
and all coefficients. It does not yet cover arbitrary compositions or wild
automorphisms.

### Filtered differential obstruction

For a basis `f1,...,fm` of `F_D^sigma A`, let `J_D^sigma` be the ideal of
the `3 x 3` minors of

```text
(partial fi / partial uj).
```

It is basis independent. In characteristic zero:

- `J_D^sigma=0` exactly when `trdeg C_D^sigma<=2`;
- a degree-`D` target coordinate frame forces `J_D^sigma=A`;
- therefore properness of `J_D^sigma` obstructs such a frame.

The elementary-shear theorem gives the stronger condition
`J_6^sigma=0` for every single elementary monomial source shear.

### Valuative and filtration limits

For divisorial valuations at infinity,

```text
deg_x' iota(u') =
  sup_v max_j delta_v(iota(uj')) / max_i delta_v(xi').
```

Minimizing over source and target frames recovers `d_LR`. This formula is
exact but not effective. Every finite normalized valuation family is diluted
to zero by triangular source shears, so a successful boundary budget must use
an infinite/global object or a canonical source normalization.

Likewise, no exhaustive filtration by finite-dimensional pieces can be
literally invariant under every polynomial automorphism: invariance under
`x1 -> x1+x2^N` would put all powers `x2^N` in one finite piece.

## Live problem

The elementary generators are no longer the immediate obstruction. The
remaining source-frame problem is stability under **composition**.

A useful next theorem would prove one of:

1. the degree-six obstruction is preserved when an elementary monomial shear
   is applied to any inclusion already satisfying an appropriate
   weight-separated or differential-minor condition;
2. every tame source automorphism admits a factorization for which the
   obstruction can be propagated step by step without increasing degree;
3. a bounded-composition theorem, beginning with two elementary shears and
   identifying the first genuine interaction term;
4. a counterexample composition that creates a three-dimensional
   `C_6^sigma`, which would isolate exactly why single-shear control is
   insufficient.

The older `delta(Q)<=9` packet still needs a public definition, case inventory,
localizations, and artifact map before it can be compared to this theorem.

## Useful deliverable

Return one of:

- a composition-stability lemma for `J_6^sigma` or `C_6^sigma`;
- an exact two-shear classification;
- a non-degree-increasing normal form for tame automorphisms;
- an infinite/global boundary norm that survives shear dilution; or
- a concrete composition where the single-shear theorem fails.

State separately what is proved for one presentation, one left-right orbit,
all realizations of the fixed cover, generic-degree-three maps, and arbitrary
Keller maps.
