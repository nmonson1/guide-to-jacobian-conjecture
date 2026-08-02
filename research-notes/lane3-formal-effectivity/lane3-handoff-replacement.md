# Lane 3: Bounded-degree deformation, orbit saturation, and modulus onset

## Research objective

Relate three distinct filtered quotient problems without identifying them
prematurely:

1. the degree-at-most-seven coefficient slice modulo the eleven-dimensional
   normalized affine orbit;
2. the degree-eight coefficient germ after affine, source-shear, target-shear,
   and intersection components are included; and
3. the stable polynomial left-right quotient on the cubic-frame locus.

The first has a length-584 Artin algebra.  The second still lacks a global
characteristic-zero orbit-saturation theorem.  In the third, the current
cubic-frame theorem proves that ordinary degree eleven is the first degree
carrying genuine positive-dimensional stable moduli.  Assuming the current
reduced-rigidity and stable-classification theorems, the claim graph records
only the pointed global interval

```text
8 <= D_mod(G) <= 11,
```

with equality at eleven proved inside the cubic-frame locus.  No current
result upgrades that scoped equality to the unrestricted polynomial
left-right quotient.

This lane overlaps [Program 3](local-rigidity-and-deformation-algebra.md) and
[Program 4](stable-moduli.md).  The newest exact degree-eight units are the
[two order-six lower-jet exclusions](../working-mathematics/units/RMU-3D8E0001.md)
and the [five-variable universal reduction](../working-mathematics/units/RMU-3D8E0002.md).

## Reusable mathematics

In the normalized degree-at-most-seven coefficient scheme, an eleven-condition
affine slice transverse to the source orbit has a length-584 completed Artin
algebra.  Its Hilbert function is

```text
(1,10,44,108,157,145,86,30,3),
```

its maximal ideal has nilpotence index nine, and its Cohen--Macaulay type is
60.  Torus attractors and the fixed locus prove reduced isolation in this
bounded transverse germ.  This does not exclude degree-increasing families,
known degree-eight shear components, or moduli in an unrestricted quotient.

At the selected exceptional first-normal direction in degree eight, the full
exact characteristic-zero order-six systems at two lower jets—the base and
`c_0=1`—have unit obstruction ideal after all 24 order-five bendings are
included.  Over `F_1000033`, the complete 22-parameter lower-jet calculation
has a fixed 24-dimensional order-five kernel.  All lower-order correction
columns lie in one fixed five-dimensional image, and projection to its
three-dimensional cokernel produces three polynomials in only

```text
c_14, c_19, c_26, t_8, t_15.
```

The corrected universal assembly reproduces all 325 base columns.  An earlier
assembly overflowed because a negative determinant sign was represented as
`p-1` before integer multiplication; do not reuse that version.

The fixed-image containment is proved only modulo `1000033`.  Rank five has
not been proved everywhere, the three polynomials are not yet known to
generate the unit ideal universally, and the result is not a global
degree-eight theorem.

The Program 4 source already supplies two exact bridges to this lane:

- `thm:cubic-frame-degree-threshold` proves the degree-eleven threshold inside
  the full cubic frame; and
- `prop:formal-stable-separation` proves that every pointed `q`-arc is
  coefficientwise formally source-trivial although its punctured fibers
  remain stably separated.

For the same pointed family

```text
A_s(c)   = c*(1+s*c),
B_s,q(c) = -2 - 4*s*c + q*s^2*c^2,
```

there is a sharper explicit calculation in the framed conductor groupoid.
A root translation by `phi(c) in c R[c]` changes `B`
by `3*A*phi`.  Over `R_M=C[s]/(s^M)`, `M>=3`, the unique translation from
`q` to `q'` is

```text
phi_M(c) = (q'-q)/3 * s^2*c * sum_{j=0}^{M-3} (-s*c)^j.
```

Hence

```text
deg_c(phi_M) = M-2.
```

The compatible formal gauge is

```text
phi_infty(c) = (q'-q)/3 * s^2*c/(1+s*c).
```

For `q != q'` it is not polynomial over `C[s,c]`; its pole is the deleted
root `c=-1/s`, where `B_s,q(-1/s)=q+2`.  After writing `phi=c*psi`, the exact polynomial-orbit obstruction is

```text
(q'-q)/3 * s^2 mod (1+s*c)
```

in `C[s,c]/(1+s*c)`.  Its principal-part lift is

```text
(q'-q)/3 * [s^2*c/(1+s*c)]
```

in `H^1_(1+s*c)(C[s,c])`.  Both modules have zero `s`-adic completion because
`1+s*c` is a unit modulo every power of `s`.  Thus formal invisibility and
global stable separation are compatible for a concrete support-theoretic
reason.

The calculation has an exact coefficient-ring form.  For
`A_alpha=c*(1+alpha*c)` and `delta=q'-q`, a framed translation of `c`-degree
at most `D` exists exactly when

```text
delta * alpha^(D+2) = 0.
```

Its residual before imposing that annihilator is the single staircase term

```text
(-1)^D * delta * alpha^(D+2) * c^(D+2).
```

Thus for a ramified Artin arc `alpha=s^e*u(s)` over `C[s]/(s^M)`, the exact
translation degree is

```text
max(0, ceil(M/e)-2).
```

The same lower bound survives every residual affine change
`C=u*c+v, T=nu*t+h(c)` allowed by the normalized frame equations: they force
`v=0`, `alpha*(u-1)=0`, and the same rational root translation, up to a unit.
For the unramified arc, the canonical source and target gauges have degrees

```text
source: 4*(M-2),       target: M-1.
```

There is also an unrestricted theorem.  For `q != q'`, every pair of Artin
reductions of the two pointed families is compatibly ordinarily left-right
equivalent, but the complete maps over `C[[s]]` are not even stably
polynomially left-right equivalent.  A hypothetical complete-base equivalence
would give a generic-fiber stable equivalence between normalized `G_q` and
`G_q'`, contradicting the Program 4 classification.  The compatible limit
lives in `C[x,y,z][[s]]` and has unbounded spatial degree; it does not lie in
`C[[s]][x,y,z]`.

Consequently completion and the bounded-degree filtration do not commute:

```text
lim_M colim_D Isom_D(C[s]/s^M)  is nonempty,
colim_D lim_M Isom_D(C[s]/s^M)  is empty.
```

This proves failure of formal effectivity for the full stable left-right
isomorphism functor at the two arcs.  It also rules out an exact algebraic
moduli stack with affine diagonal locally of finite presentation: its affine
finite-presentation isomorphism space would turn the compatible Artin points
into a `C[[s]]`-point.

There is now an effective unrestricted complexity theorem that does not
assume the frame is recovered.  Suppose an equivalence modulo `s^M` uses `m`
stabilization variables, and the source and target automorphisms and their
inverses all have degree at most `b`.  Put

```text
n = 3+m,
N = 4*n*binomial(n+b,n),
d = max(b+1,11).
```

Encoding the four maps and their inverse identities gives a coefficient
scheme with `N` variables whose equations have coefficient degree at most `d`
and `s`-degree at most `2*b`.  Generic-fiber `q`-separation makes this scheme
empty over `C(s)`.  After reducing to `N+1` generic constant combinations, the
parametric effective Nullstellensatz gives a nonzero elimination polynomial
`alpha_(m,b)(s)` of degree at most

```text
2*b*(N+1)*d^N.
```

An equivalence modulo `s^M` forces `s^M` to divide this polynomial.  Therefore

```text
M <= 2*b*(N+1)*d^N.
```

For fixed `m`, the least possible degree obeys

```text
b_(M,m) >= ((3+m)!/4 * log(M)/log(log(M)))^(1/(3+m)) * (1-o(1)).
```

If `kappa_M(q,q')` is the minimum of the maximum of stabilization dimension
and the four automorphism degrees, then

```text
liminf kappa_M(q,q')/log(log(M)) >= 1/log(4).
```

Equivalently,

```text
kappa_M(q,q') >= log(log(M))/log(4) - O(log(log(log(M)))).
```

This is a fully unframed rate.  The explicit framed construction gives the
upper bound `kappa_M <= 4*M-8`.  A separate intrinsic-recovery theorem over
Artin bases is still required only for the **sharp linear rate**: proving that
`M-2` and `4*M-8` are lower bounds for every unframed polynomial equivalence.

## High-priority next calculations

1. Define the nested spaces currently called the fixed five-dimensional
   correction image and the fixed two-dimensional tangent image: specify the
   ambient module, maps, bases, and quotient.  Only then compute the proposed
   `3 x 3` determinant `Delta_H(c_14,c_19,c_26)`.  A nonzero constant proves
   constant rank; factors give the exact rank-drop strata.
2. Form the `3 x 6` coefficient matrix of the three obstruction polynomials
   against `1,t_8,t_15,t_8^2,t_8*t_15,t_15^2` and find a unit minor or its
   factorization.
3. Reconstruct the sparse modular identities at several good primes and
   verify them directly over `Q`; repeat only on the resulting exceptional
   divisors.
4. Cover the other first-normal strata, the quadratic source-shear parameter,
   target-shear components, and all source/target intersections before making
   an orbit-saturation statement.
5. Prove that an arbitrary polynomial left-right equivalence over an Artin
   base intrinsically recovers enough of the projective escaping section to
   inherit the sharp framed linear degree law.  Formal non-effectivity and an
   explicit double-logarithmic unrestricted rate no longer depend on this
   step; only the optimal linear rate does.
6. Complete the source-flow/determinant comparison at orders five through
   eight.  Its role is to explain the bounded coefficient germ, not to recover
   `q` from a finite tangent character.

The newest tangent packet has rank 439, nullity 44, and a 28-dimensional
residual character; an older claim that only weights `-2,-1` remain is not
current.

## Useful deliverable

The immediate degree-eight deliverable remains a characteristic-zero unit
certificate or a finite stratification of its failure locus, with the
bounded-degree and quotient scope explicit.  On the moduli side, formal
non-effectivity and a fully unframed double-logarithmic lower rate are now
proved; the remaining theorem-facing deliverable is a projective Artin-base
recovery statement upgrading the exact framed linear **degree rate** to all
unframed polynomial equivalences.  Do not describe the
degree-eleven family as a newly discovered failure of finite-order local
rigidity: the current Program 4 manuscript already proves all-order formal
source triviality, and the new result identifies the stronger obstruction as
failure of polynomial effectivity at unbounded spatial degree.
