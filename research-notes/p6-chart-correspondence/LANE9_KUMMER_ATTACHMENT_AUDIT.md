# Lane 9: Kummer attachment audit and the finite index-eight obstruction

**Status:** exact research note, not a global attachment theorem and not a proof
of the plane Jacobian conjecture.

This note attempts every item in the public Lane 9 checklist.  It separates
three logically different objects:

1. exact transport in an ambient Laurent-jet space;
2. operations preserving a fixed complete-chain presentation;
3. arrows to genuinely different chart presentations.

The main new conclusion is negative but finite.  The corrected layer-four
candidate does integrate, and in quotient coordinates its flow is the
translation `Q -> Q+16s`.  However, the quotient has exponent-lattice index
`8`, its generic lift requires an eighth root, and its infinitesimal action has
unavoidable principal parts outside the archived layer-four coefficient
window.  Consequently it is **not** an ordinary same-function-field monomial
chart and does **not** match the archived residual coefficientwise without an
additional overlap-normalization map.  It becomes a valid object only after
enlarging the atlas to Kummer/root-cover charts with deck group `mu_8`.

The standard-library checker

```text
lane9_kummer_attachment.py
```

verifies all displayed finite identities and writes
`lane9_kummer_attachment.json`.  The companion recovery program
`recover_lane9_public_archive.py` scans the hash-pinned public Program 6 ZIP,
extracts the small Lane 9/F2 text packet that is really present, and records
what is absent without synthesizing matrices.

## 1. Inputs and claim boundary

The exact degree-21 lower-face data used below are

```text
alpha=2, beta=3,
A0=z*p(z), B0=z^2*q(z),
p*q+2*z*p*q'-3*z*p'*q=1,
deg(p)=7, deg(q)=10.
```

In particular `p_0*q_0=1`.  The reconstructed full-support layer-four window
is

```text
a in span{1,z,...,z^6},
b in span{1,z,...,z^11}.
```

The exact layer operator and source-action map satisfy

```text
D_r Theta_r(f,g)=(f*z^2)' +(r-5)*g*z^2.       (1.1)
```

The branch artifacts independently give, at layers one through four,

| space | ranks |
|---|---:|
| determinant kernel | `(2,3,3,1)` |
| maximal support-admissible Laurent source image | `(2,3,3,1)` |
| affine-polynomial source image | `(2,3,2,1)` |
| previously recorded complete-chain fixed-presentation image | `(1,1,2,0)` |

The last row remains imported input: the public packet still does not contain
the complete approximate-root generator table from which it could be rebuilt.
The first three rows are exact reconstructions in this PR.

Nothing in this note identifies every determinant-kernel vector with an
admissible operation.  In particular, the unrestricted Laurent source module
is too large: in the reconstructed full window it already spans the whole
kernel.

## 2. Ambient Laurent-jet transport is retained exactly

The ambient transport theorem is useful and correct independently of any
complete-chain interpretation.  For the elementary `k`-wall substitution,
the supplied density basis transforms by

```text
T_lambda e_(n,j)
  = sum_q binom(n-p+2*j,q) lambda^q
      e_(n+q*(2*k-1), j-q*k),                 (2.1)
```

while the exact contragredient basis transforms by

```text
U_lambda epsilon_(m,l)
  = sum_q binom(p-m-2*l-1,q) lambda^q
      epsilon_(m-q*(2*k-1), l+q*k).           (2.2)
```

On any finite saturated Laurent window these satisfy

```text
U_lambda^T T_lambda=I,
T_lambda T_mu=T_(lambda+mu),
U_lambda U_mu=U_(lambda+mu).                  (2.3)
```

Hence kernel vectors, equation densities, adjoint principal parts, forcing
terms, and their residue pairings transport together.  This is an exact
finite-dimensional groupoid after saturating the exponent window.

The theorem does **not** imply that a transported Laurent vector preserves a
chosen Newton polygon, approximate-root normalization, or complete-chain
presentation.  Those are extra finite support and admissibility conditions.
All conclusions below preserve this distinction.

## 3. The bare `k=4` wall remains layer seven

With lower-face coordinates

```text
t=Y, z=X*Y^2,
```

the bare wall shear `Y'=Y+lambda*X^-k` is

```text
t'=t*(1+h),
z'=z*(1+h)^2,
h=lambda*t^(2*k-1)*z^-k.                     (3.1)
```

Its first normal order is `2*k-1`.  For `k=4` it therefore begins at order
`7`, not order `4`.  A filtration-preserving conjugacy with invertible
associated graded cannot change the first nonzero order.

At layer four, fixing the horizontal component `f=2*z^-3`, the bare vertical
component `g=z^-4` has defect

```text
(f*z^2)' +(4-5)*g*z^2=-3*z^-2.               (3.2)
```

The unique correction with the same horizontal monomial is

```text
f=2*z^-3, g=-2*z^-4,                          (3.3)
```

for which the defect in (3.2) is zero.  Thus the corrected associated-graded
tangent is

```text
E4=t^4*(2*z^-3*d_z-2*z^-4*t*d_t).            (3.4)
```

This is a determinant-kernel Laurent field.  It is not yet a fixed-chart
operation or an adjacent complete-chain chart.

## 4. Exact coefficientwise comparison with the archived layer-four window

Apply (3.3) to the leading pair.  Direct calculation gives

```text
Theta_4(E4)_P
  = 6*z^-3*p+2*z^-2*p'
  = sum_i 2*(i+3)*p_i*z^(i-3),                (4.1)

Theta_4(E4)_Q
  = 10*z^-2*q+2*z^-1*q'
  = sum_i 2*(i+5)*q_i*z^(i-2).                (4.2)
```

The principal parts outside the archived window are therefore

```text
P: 6*p_0*z^-3 + 8*p_1*z^-2 + 10*p_2*z^-1,
Q: 10*q_0*z^-2 + 12*q_1*z^-1.                (4.3)
```

Because `p_0*q_0=1`, the coefficients `6*p_0` and `10*q_0` are nonzero.
This proves:

### Proposition 4.1 — direct mismatch

The corrected layer-four tangent is not an element of the archived
coefficient space

```text
U_4=K[z]_[0,6] direct-sum K[z]_[0,11].
```

Consequently it cannot equal the archived one-dimensional residual
coefficientwise in the archived basis.  The comparison is not merely
unknown; without an overlap-normalization map it is ill-typed.

### Why truncation is not a repair

Discarding the five principal-part coefficients in (4.3) is not an intrinsic
projection.  Truncation need not commute with `D_4`, with the nonlinear
support map, or with residue-adjoint transport.  A legitimate comparison must
supply an adjacent chart whose normalization absorbs (4.3), together with the
induced map on the old polynomial window and its dual.  No such map is present
in the public packet.

The archived old-window kernel is one-dimensional, with deterministic
coordinate `t4_0`, and the recorded complete-chain fixed-presentation rank at
that layer is zero.  Thus the archived residual is the whole old-window
kernel.  Proposition 4.1 shows that the quotient candidate is not itself that
vector.  It could represent the same geometric direction only after a new
chart-overlap map is specified and checked.

This resolves the requested coefficientwise test for the data currently
available: **the direct match fails**.

## 5. Affine form, Hamiltonian, and exact flow

Using

```text
t=x^4*y, z=x^7*y^2,
```

(3.4) becomes

```text
V=-6*x^-11*y^-4*d_x+22*x^-12*y^-3*d_y.       (5.1)
```

It is Hamiltonian for the standard area form:

```text
H=2*x^-11*y^-3,
V=(dH/dy)*d_x-(dH/dx)*d_y.                    (5.2)
```

Set

```text
M=x^-12*y^-4, Q=M^-1=x^12*y^4.               (5.3)
```

Then

```text
V(H)=0, V(M)=-16*M^2, V(Q)=16.                (5.4)
```

The unique formal flow with identity constant term is

```text
R^8=1+16*s*M,
x_s=x*R^-3,
y_s=y*R^11,
t_s=t*R^-1,
z_s=z*R,                                     (5.5)
```

and in the invariant coordinates

```text
H_s=H, Q_s=Q+16*s.                            (5.6)
```

Thus the proposed quotient translation is exact, not only infinitesimal.

## 6. The finite Kummer-index obstruction

The exponent rows of `(H,Q)` in `(x,y)` are

```text
[-11,-3],
[ 12, 4].                                    (6.1)
```

Their determinant is `-8`; the Smith invariants are `(1,8)`.  Therefore

```text
[K(x,y):K(H,Q)]=8                             (6.2)
```

generically.  More explicitly, in adjacent blowdown coordinates

```text
u=(x*y)^-1, v=y,
```

one has

```text
H=2*u^11*v^8,
Q=u^-12*v^-8,
K(H,Q)=K(u,v^8).                              (6.3)
```

The deck group is

```text
mu_8: (u,v)->(u,zeta*v),
      (x,y)->(zeta^-1*x,zeta*y).              (6.4)
```

### Proposition 6.1 — no ordinary monomial chart

The quotient `(H,Q)` is not a same-function-field monomial chart.  The
absolute determinant of the exponent map is `8`, whereas a birational torus
recharting has determinant `1` in absolute value.  Multiplication on either
side by unimodular exponent matrices preserves this index.  Hence no sequence
of ordinary monomial rechartings converts this quotient into a unimodular
chart.

### Proposition 6.2 — no same-field rational realization of this flow

Over `K(x,y,s)`, the radicand

```text
R^8=(Q+16*s)/Q                               (6.5)
```

has valuation `1` at the prime divisor `Q+16*s=0`.  An eighth power has
valuation divisible by `8`, so `R` is not rational.  In fact the Kummer
extension has generic degree `8`.  Since `t_s/t=R^-1`, the time-`s` map in
(5.5) is not a rational self-map over the original function field.

If a rational same-field chart conjugated this flow to the translation
(5.6), conjugating the rational translation back would produce a rational
flow, contradicting (6.5).  Therefore this exact repair candidate cannot be
realized by any ordinary same-field rational chart, not just by the displayed
monomial coordinates.

The obstruction is finite and chart-independent under ordinary birational
monomial changes: it is the index-eight character-lattice defect, equivalently
the valuation-one Kummer defect in (6.5).  It obstructs this repair candidate,
not all possible repairs and not a polynomial Keller pair.

## 7. Category decision and presentation stabilizer

The quotient is not an allowed object in the current ordinary atlas if chart
objects are required to be same-function-field monomial charts.  There are two
mathematically coherent enlargements:

1. retain the root cover `K(u,v)` and its `mu_8` deck action;
2. use the quotient/root-stack presentation with invariant field
   `K(H,Q)=K(u,v^8)` and remember the eight character modules.

In either formulation the presentation stabilizer is exactly `mu_8`, acting
as in (6.4).  This answers the stabilizer question for the candidate chart.
It does not recover the missing nonlinear stabilizer of the original
complete-chain presentation.

On the quotient, translations form a strict additive groupoid:

```text
tau_s(H,Q)=(H,Q+16*s),
tau_s*tau_t=tau_(s+t), tau_s^-1=tau_-s.       (7.1)
```

For a root lift, write

```text
R_s(Q)^8=(Q+16*s)/Q.                          (7.2)
```

Then

```text
R_s(Q)^8*R_t(Q+16*s)^8
  =(Q+16*(s+t))/Q.                            (7.3)
```

In formal power series there is a unique eighth root with constant term `1`,
so (7.3) gives a strict pairwise and triple cocycle.  Over the generic
algebraic field, choices of eighth root differ by `mu_8`; the intrinsic
algebraic cocycle is therefore a `mu_8`-valued Kummer cocycle.  This is exactly
the information lost by treating `(H,Q)` as an ordinary chart.

## 8. Support and residue transport

### Theorem 8.1 — ordinary monomial charts

Let a toric monomial transition induce `A in GL_2(Z)` on the character
lattice.  For every finite exponent window `S`, the transported support is the
finite window `A(S)`, and `A:S->A(S)` is a bijection.  Pulling adjoint
functionals back by the inverse transpose gives an exact contragredient map.
The coefficient pairing, and therefore every residue obstruction pairing, is
preserved.  Pairwise and triple overlap cocycles follow from matrix
composition.

This is the intrinsic monomial-chart version of the ambient transport theorem.
It requires the support window, equation-density window, adjoint window, and
forcing term to move together.

### Theorem 8.2 — the index-eight quotient

For the quotient lattice in (6.1), the old Laurent algebra decomposes as

```text
K[u^+-1,v^+-1]
  = direct-sum_(chi in Z/8) A_chi,             (8.1)
```

where `A_0=K[H^+-1,Q^+-1]` is the invariant subalgebra.  A finite old-chart
support window therefore transports to eight finite character windows, not
to one ordinary invariant window.  The residue pairing is characterwise,
pairing character `chi` with the dual character `-chi`.

Hence exact support and residue transport exists in the Kummer category, but
not after forgetting the seven nontrivial character blocks.  Any proposed
complete-chain attachment through `(H,Q)` must publish these blocks and their
normalization maps.

## 9. The forced admissible operation module

The correct object is a filtered **Lie algebroid over the chart groupoid**, not
a single unrestricted Laurent Lie algebra.  Define the minimal Rees-Kummer
admissible algebroid to be the smallest system satisfying all of the following:

1. on each chart it consists of divergence-free derivations preserving the
   nonlinear Newton-support ideal;
2. it is graded by normal order and by the `C_5` character;
3. on Kummer objects it is `mu_8`-equivariant and retains all character
   modules in (8.1);
4. it contains every verified fixed-presentation complete-chain generator;
5. it contains the Kummer chart arrow (3.4) and the bare layer-seven wall
   arrow;
6. it is closed under overlap transport and Lie brackets.

This is a precise construction, although equality with the unknown full
complete-chain algebroid cannot be proved until the original generator table
is supplied.

The closure requirement is substantive.  A general support-admissible
layer-four field is

```text
f4=c0+c1*z+z^2,
g4=2*c0*z^-1+3*c1+4*z.                       (9.1)
```

Bracket it with the bare layer-seven wall field

```text
f7=2*z^-3, g7=z^-4.                           (9.2)
```

The exact layer-eleven bracket is

```text
f11=18*c0*z^-4+30*c1*z^-3+42*z^-2,
g11= 6*c0*z^-5+ 5*c1*z^-4.                   (9.3)
```

Acting on the degree-21 leading face, the top terms are

```text
336*lead(A0)*z^5,
504*lead(B0)*z^9.                             (9.4)
```

The stored layer-eleven window allows no `P` correction and only `Q`
exponents `0,...,4`.  Thus carrying a layer-four direction through the wall
forces a new adjacent-chart operation coordinate at layer eleven.  The old
fixed-chart operation module cannot be transported unchanged.

This explains both failures of the naive choices:

- unrestricted Laurent operations erase the lower-face residual completely;
- affine polynomial operations omit required chart-moving and bracket-closure
  directions.

## 10. `C_5`-equivariant descent

For the `F_2` lattice quotient `u=z^5`, a `q`-th term of a `k`-wall shifts
character by `-q*k`.  Consequently the wall parameter has character `k`.
For `k=4`:

```text
character(lambda)=4 mod 5.                   (10.1)
```

A scalar invariant wall effect first appears at wall order `5`, and the
corresponding unweighted normal shift is

```text
5*(2*4-1)=35.                                (10.2)
```

Reconciling the layer-seven bare wall with the layer-four corrected quotient
requires Rees normal weight `-3`.  The chart-moving parameter therefore has
bidegree

```text
(normal Rees weight, C5 character)=(-3,4).   (10.3)
```

This is not the degree of an ordinary fixed-chart deformation.  It is the
grade of a chart arrow.  Equivariant descent must be imposed on the entire
chart groupoid and all eight Kummer character modules, not only on invariant
coefficient polynomials.

## 11. Public `F_2` artifact recovery and recurrence

The public ZIP contains genuine terminal-boundary `F_2` source material,
including the degree-125 boundary seed, the degree-30 coefficient-system
generator, the cyclic quotient/dessin calculation, and related terminal
program notes.  The deterministic recovery script extracts the files actually
present and writes their byte counts and SHA-256 hashes to

```text
lane9_public_archive_recovery.json.
```

It also searches every small UTF-8 member for order `510`, `520`, or `530`,
fresh-parameter declarations, wall/chart code, and matrix/support-block
language.  The generated manifest is the evidence boundary: files listed
there are recovered; unlisted high-order blocks are not invented.

The exact parameter-complete recurrence that must be instantiated is

```text
D_r^L x_r^L=-Phi_r^L(x_<r^L,p_<=r),
D_r^R x_r^R=-Phi_r^R(x_<r^R,p_<=r),           (11.1)
```

with overlap equations

```text
x_r^R=T_r(lambda)x_r^L
      + explicit lower-order transport terms, (11.2)
```

all fresh parameters retained, all `C_5` characters declared, and every
coefficient outside both finite Newton windows set to zero.  The equations
split into finite character blocks by (10.1).

Without the ordered high-order endpoint matrices, fresh-parameter ranges, and
normalization/overlap matrices, (11.1)--(11.2) cannot be numerically replayed.
In particular, no valid order-530 obstruction can be obtained by setting new
parameters to zero.  The present contribution publishes the exact schema and
recovery audit, not a fabricated recurrence instance.

Finite global polynomial support is then an ordinary finite feasibility
problem for each supplied truncation: concatenate both endpoint equations,
overlap equations, character projections, and outside-window zero rows.  The
same data are required before one can decide feasibility or match every
neighboring complete-chain chart.

## 12. Algebraization and obstruction conclusions

The formal unit-root flow (5.5) algebraizes as a finite degree-eight Kummer
cover.  It does **not** algebraize as a rational self-map of `K(x,y)`, and a
fortiori not as a polynomial automorphism of the affine plane.  This is a
complete algebraization verdict for the proposed repair candidate.

It is not a verdict for an arbitrary surviving `F_2` formal solution, because
the high-order recurrence has not been instantiated.  Ordinary finite-jet
area-preserving algebraization theorems do not resolve this point: they do not
preserve the complete-chain Newton filtration or the Kummer character data.

The finite chart-independent obstruction obtained here is

```text
Kummer index = 8,                             (12.1)
```

equivalently the valuation-one failure of the radicand in (6.5) to be an
eighth power.  It rules out the corrected quotient translation as an arrow in
the ordinary same-field atlas.  It does not rule out:

- a different same-field adjacent chart with another tangent;
- a Kummer/root-stack enlargement of the atlas;
- a global polynomial Keller pair by any unrelated argument.

## 13. Checklist disposition

| # | Checklist item | Result of this attempt | Remaining boundary |
|---:|---|---|---|
| 1 | Correct public layer-four/`k=4` identification | Verified: bare `k=4` begins at layer seven. | None for the grading correction. |
| 2 | Preserve ambient Laurent-jet theorem | Retained as (2.1)--(2.3), separately from admissibility. | Intrinsic chart realization remains separate. |
| 3 | Compare archived residual with corrected candidate | Direct coefficientwise match fails: (4.3) is outside `U_4`. | Requires a published overlap-normalization map for any indirect comparison. |
| 4 | Test `Q->Q+16s` against the residual | Exact translation proved, but it is not an old-window vector. | Same missing overlap map. |
| 5 | Publish adjacent normalization map | Published the exact Kummer quotient `(x,y)->(H,Q)` and inverse root formulas. | It is not an ordinary complete-chain chart; another ordinary chart is not found. |
| 6 | Identify presentation stabilizer | Candidate stabilizer is `mu_8`; reconstructed linear source stabilizers are zero in the maximal layers. | Original nonlinear complete-chain stabilizer table remains absent. |
| 7 | Construct `g_adm` | Minimal forced Rees-Kummer Lie algebroid defined; layer-eleven closure proved. | Equality with the actual complete-chain algebroid is unproved. |
| 8 | Support/residue transport for monomial charts | Proved for `GL_2(Z)` charts and characterwise for the index-eight quotient. | Concrete F2 windows still need the missing blocks. |
| 9 | Pairwise/triple cocycles | Strict on quotient and formal unit-root lift; `mu_8` ambiguity algebraically. | Full neighboring-chart atlas not enumerated. |
| 10 | Decide whether Kummer quotient is allowed | No in the ordinary same-field atlas; yes after Kummer/root-stack enlargement. | Repository must choose and formalize the enlarged category. |
| 11 | Publish real `F_2` matrices/support blocks | Public archive recovery is hash-pinned and automated. | High-order endpoint blocks not present in the recovered packet are not replaced. |
| 12 | Recompute `F_2` recurrence with all parameters | Exact full-parameter schema (11.1)--(11.2) supplied. | Numerical replay blocked by missing ordered matrices/parameter ranges. |
| 13 | Impose `C_5` descent | Character law, first invariant order, and bidegree `(-3,4)` proved. | Must be applied to the missing full groupoid recurrence. |
| 14 | Impose finite global polynomial support | Reduced to a finite block feasibility problem. | No instance can be solved without the high-order blocks. |
| 15 | Match every neighboring chart | This candidate cannot match any ordinary same-field chart. | Other charts are not classified; Kummer atlas not globally assembled. |
| 16 | Algebraize a surviving formal solution | Candidate algebraizes only on a degree-eight Kummer cover, not rationally/polynomially on the original plane. | General F2 formal solutions unavailable. |
| 17 | Produce chart-independent finite obstruction | Index-eight/valuation obstruction proved for this repair candidate. | It is not a global obstruction to all attachments or Keller pairs. |

## 14. Reproduction

From the repository root:

```bash
python research-notes/p6-chart-correspondence/lane9_kummer_attachment.py \
  --output /tmp/lane9-kummer.json

python -m unittest -v \
  research-notes/p6-chart-correspondence/test_lane9_kummer_attachment.py \
  research-notes/p6-chart-correspondence/test_recover_lane9_public_archive.py

python research-notes/p6-chart-correspondence/recover_lane9_public_archive.py \
  docs-v7-20260726c/assets/technical-materials/06-plane-boundary-computational-supplement.zip \
  --expected-sha256 4238149caa6e8a73723368e997b8c714a99258600268f14a008c5e514ecea585 \
  --output-dir /tmp/lane9-recovered \
  --manifest /tmp/lane9-recovery.json
```

## 15. Provenance

GPT-5.6 Pro performed the source audit, mathematical derivations, exact checker
design, archive-recovery design, and drafting.  The results are unrefereed.
A human maintainer remains responsible for checking every assertion before it
is promoted into the manuscript, claim graph, or canonical handoff.
