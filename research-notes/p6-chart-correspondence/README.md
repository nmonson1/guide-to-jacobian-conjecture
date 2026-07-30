# Program 6 chart correspondence: exact fixed-chart and upper-face diagnostics

**Status:** research intake note, not an integrated claim or manuscript result.

This note develops Program 6 task P6-T2: distinguish fixed-chart gauge
parameters from tangent directions to adjacent complete-chain charts while
transporting finite support and residue conditions exactly.

The work now has two complementary parts:

1. a general fixed-chart formalism and an executable support-window quotient;
2. an independent replay and structural decomposition of the archived
   degree-21 **upper-face** linear complex.

These must not be conflated. The archive fixture `exact_data.json` concerns the
upper-face pair

```text
A0 = R^2,  B0 = R^3,  R = y^7(y-1),  (alpha,beta)=(8,12).
```

Proposition C.9 of the reader manuscript concerns a later **lower-face normal**
complex with

```text
A0 = z p(z),  B0 = z^2 q(z),  (alpha,beta)=(2,3),  Psi=z^2.
```

Both calculations have a distinguished layer numbered four, but they are not
the same vector space or quotient. The upper-face replay below does not by
itself identify the C.9 rechart direction.

The concrete outputs are:

1. determinant-kernel directions are divergence-free rational source fields;
2. elementary wall shears give explicit adjacent-chart tangent directions;
3. Newton support and residue functionals transport by finite exact formulas;
4. `fixed_chart_gauge.py` computes the actual support-aware quotient
   `ker(D_r)/im(Theta_r)` once the four exponent windows are supplied;
5. `chart_correspondence.py` further quotients by proposed adjacent-chart
   tangent vectors;
6. all 24 archived full/truncated upper-face matrices and their recorded
   left/right nullspaces are independently replayed over `Q`;
7. the upper-face kernel has a canonical common-root defect whose only
   polynomial resonance layers are `4, 8, 12`.

## 1. Keller kernel directions are divergence-free source fields

Let `K` be a characteristic-zero field and let

```text
F = (P,Q): Spec A -> A^2
```

be generically etale with `J(F)=det(dF)=c` in `K^*`. Work in a completed
Laurent chart in which all displayed expressions are defined. For a first-order
deformation `delta F=(a,b)`, define the rational source vector field

```text
v = (dF)^(-1) delta F.
```

### Proposition 1 (Keller kernel reduction)

The linearized determinant satisfies

```text
D_F J(delta F) = c div(v).
```

Consequently, the determinant kernel is identified with the divergence-free
rational vector fields `v` whose action `v(F)` lies in the prescribed
coefficient and support window.

#### Proof

Let `phi_t` be the formal flow with tangent vector `v`. The chain rule gives

```text
J(F o phi_t) = (J(F) o phi_t) J(phi_t).
```

Differentiating at `t=0` gives

```text
D_F J(v(F)) = v(J(F)) + J(F) div(v).
```

The first term vanishes because `J(F)=c` is constant. Conversely, every
`delta F` determines the unique rational field `v=(dF)^(-1)delta F`.

Thus P6-T2 is not primarily another determinant calculation. Its hard part is
the classification of divergence-free fields subject to the complete-chain
filtration and finite Newton windows.

A logarithmic chart can have non-Hamiltonian de Rham classes, so
`divergence-free` must not be silently replaced by `Hamiltonian`.

## 2. Elementary wall-shear correspondence

Let `C` be a completed Newton chart with coordinates `(X,Y)`. Suppose an
adjacent chart `C'` is related on the overlap by

```text
phi_lambda(X,Y) = (X, Y + lambda X^(-k)),    k >= 1.
```

The tangent field is

```text
v_k = X^(-k) partial_Y.
```

It has zero divergence. For `k != 1`, it is Hamiltonian with Hamiltonian
`X^(1-k)/(k-1)` under the convention
`X_H=(partial_Y H)partial_X-(partial_X H)partial_Y`.

### Proposition 2 (elementary wall-shear lemma)

Assume:

- `F` is Keller and defined on the overlap of `C` and `C'`;
- the shear is an admissible complete-chain transition;
- `v_k(F)` belongs to the normal-layer support window;
- `v_k` is not in the Lie algebra of fixed-chart admissible source operations.

Then `v_k(F)` is a determinant-kernel vector, is not induced by a fixed-chart
admissible field, and is the tangent direction of the adjacent-chart overlap.

#### Proof

The kernel assertion follows from Proposition 1 and `div(v_k)=0`. The overlap
assertion is the derivative of `phi_lambda` at zero. If a fixed-chart field `u`
induced the same deformation, then `(u-v_k)(P)=(u-v_k)(Q)=0`. Independence of
`dP,dQ` over the fraction field gives `u=v_k`, contradicting fixed-chart
non-admissibility.

This is a sufficient recognition result, not an exhaustive classification.

## 3. Exact support and residue transport

Put `Y=Y'-lambda X^(-k)`. Then

```text
X^i Y^j
  = sum_{t=0}^j binom(j,t) (-lambda)^t
      X^(i-k t) (Y')^(j-t).
```

A finite support set `S` therefore transports into

```text
T_k(S) = {(i-k t,j-t) : (i,j) in S, 0 <= t <= j}.
```

Ordering monomials by decreasing `Y`-degree makes the transition triangular
with diagonal one. On a finite support space closed under this substitution
and its inverse, the overlap map is an exact linear isomorphism.

If a compatibility functional is `Res(lambda Phi)`, pull back both the adjoint
principal part and the forcing form. Formal residue invariance gives

```text
Res(phi^*(lambda Phi)) = Res(lambda Phi).
```

Transporting only the kernel vector is insufficient: the support window,
adjoint element, and lower-layer forcing term must move together.

## 4. The fixed-chart operator

Let a completed normal chart have leading pair

```text
P0 = s^(-alpha) A0(z),
Q0 = s^(-beta)  B0(z).
```

A layer-`r` source field has the form

```text
V_(f,g) = s^r (f(z) partial_z + g(z) s partial_s).
```

Its action on the leading coefficients is

```text
Theta_r(f,g)
  = (f A0' - alpha g A0,
     f B0' - beta  g B0).
```

Put

```text
Psi = alpha A0 B0' - beta A0' B0
```

and

```text
D_r(a,b)
  = (alpha-r)a B0' - beta B0 a'
    + alpha A0 b' + (r-beta)b A0'.
```

### Proposition 3 (weighted-divergence identity)

For all Laurent polynomials `f,g`,

```text
D_r Theta_r(f,g)
  = (f Psi)' + (r-alpha-beta) g Psi.
```

#### Proof

Substitute the two components of `Theta_r` into `D_r`. The `f'` terms combine
to `f' Psi`; the `f` terms combine to `f Psi'`; the two `g'` terms cancel; and
the remaining `g` terms are `(r-alpha-beta)g Psi`.

This is the coefficient form of weighted divergence for the source volume in
the normal chart.

### The degree-21 lower face

For the lower face used in Proposition C.9,

```text
A0 = z p(z),  B0 = z^2 q(z),
pq + 2z p q' - 3z p' q = 1.
```

Therefore

```text
Psi = 2 A0 B0' - 3 A0' B0 = z^2,
```

and Proposition 3 becomes exactly

```text
D_r Theta_r(f,g) = (f z^2)' + (r-5)g z^2.
```

For `r != 5`, a monomial `f=z^j` is weighted-divergence-free precisely with

```text
g = -(j+2)/(r-5) z^(j-1).
```

This formula makes the remaining issue completely finite: which exponents of
`f` and `g` are admissible in the fixed chart, and which induced coefficients
fit the `a` and `b` Newton windows?

## 5. Exact fixed-chart quotient

`fixed_chart_gauge.py` takes as input:

- `alpha,beta,r`;
- exact Laurent coefficients of `A0,B0`;
- candidate exponent windows for `f,g`;
- allowed coefficient exponents for `a,b`.

It then:

1. constructs the complete matrix of `D_r` on the `(a,b)` window;
2. imposes the weighted-divergence equation on `(f,g)`;
3. imposes vanishing of every induced `a` or `b` coefficient outside the
   requested window;
4. computes the admissible source-field space;
5. maps it through `Theta_r` and removes stabilizers;
6. returns

```text
h_r = dim ker D_r,
b_r = dim im Theta_r,
o_r = dim(ker D_r / im Theta_r).
```

The included toy face `A0=z, B0=z^2` has `Psi=z^2`. With the same `(a,b)`
window, a restricted source window leaves residual dimension one, whereas
adding the missing Laurent `g` exponent makes the residual vanish. This is a
small exact illustration of why fixed-chart support must be specified rather
than inferred from formal divergence-freeness.

Once the actual four support windows from C.9 are entered, the program is
intended to reproduce the recorded residual dimensions `(1,2,1,1)` without
using the manuscript's precomputed quotient.

## 6. Quotient by adjacent charts

At layer `r` in chart `C`, put

```text
H_r(C) = ker D_r,
B_r(C) = span of supported fixed-chart gauge vectors,
R_r(C) = span of supported tangents of enumerated adjacent charts.
```

The chart-correspondence diagnostic is

```text
o_r(C) = dim H_r(C) - dim(B_r(C) + R_r(C)).
```

A nonzero `o_r(C)` is not automatically an obstruction. It is an unclassified
kernel direction and may indicate a missing adjacent chart.

`chart_correspondence.py` performs this quotient exactly over `Q`, verifies all
supplied gauge and rechart vectors, returns quotient representatives, and
computes the transported support `T_k(S)`.

## 7. Non-synthetic replay of the archived upper-face layers

The distilled fixture is copied verbatim from

```text
06-plane-boundary-computational-supplement/
  computational-supplement/degree-twenty-one/exact_data.json
```

inside the public Program 6 archive. Its source archive and member hashes are
recorded in `fixtures/degree21_fixture_provenance.json`.

The archived generator used SymPy. `degree21_linear_replay.py` instead uses
only `fractions.Fraction` and reconstructs the matrix from

```text
R = y^7(y-1),    u0 = R^2,    v0 = R^3,

L_r(u,v)
  = (8-r)u v0' - 12u'v0 + 8u0 v' - (12-r)u0'v.
```

For every layer `1 <= r <= 12` in both the truncated and full windows, it
verifies:

- the ordered domain and target dimensions;
- the exact rank;
- every archived right-nullspace vector;
- completeness of the archived right-nullspace basis;
- every archived left-nullspace vector;
- completeness of the archived left-nullspace basis.

All 24 layers pass. In particular, the raw layer-four dimensions are

| window | domain | target | rank | kernel | cokernel |
| --- | ---: | ---: | ---: | ---: | ---: |
| truncated | 7 | 5 | 3 | 4 | 2 |
| full | 15 | 10 | 7 | 8 | 3 |

These are upper-face dimensions. They are not the C.9 fixed-chart residual
dimensions `(1,2,1,1)`.

## 8. Pure-power upper-face factorization

The archived upper-face complex has an additional basis-independent
simplification.

### Proposition 4 (common-root defect factorization)

Let

```text
A0 = R^m,    B0 = R^n,
alpha = d m, beta = d n,
```

with positive integers `d,m,n`, `n >= m`, and nonconstant `R in K[z]`. Define

```text
N = m b - n R^(n-m) a.
```

Then

```text
D_r(a,b)
  = R^(m-1) (d R N' + (r-beta) R' N).
```

#### Proof

Expand

```text
d R^m N'
  = d m R^m b'
    - d n(n-m)R^(n-1)R'a
    - d n R^n a',
```

and add `(r-beta)R^(m-1)R'N`. The coefficient of
`R^(n-1)R'a` becomes

```text
-n[d(n-m)+(r-beta)] = n(alpha-r),
```

while the other three terms are the remaining terms of `D_r`.

### Corollary 5 (arithmetic resonance rule)

If `D_r(a,b)=0`, then

```text
(N^d R^(r-beta))' = 0,
```

so

```text
N^d = c R^(beta-r).
```

If `R` has a simple zero and `N` is polynomial, a nonzero `N` can occur only
when

```text
beta-r is in d Z_{>=0}.
```

In that case `N=c0 R^((beta-r)/d)`. Thus each arithmetic resonance contributes
at most one non-common-root kernel class before support restrictions.

For the archived pair `m=2,n=3,d=4,beta=12`, the possible resonance layers in
`1 <= r <= 12` are exactly

```text
r = 4, 8, 12.
```

`degree21_kernel_decomposition.py` verifies the factorization on every domain
basis vector and the defect equation on every archived kernel vector. In both
support windows, the exceptional defect image has dimension one exactly at
these three layers and is zero elsewhere.

At upper-face layer four,

```text
kappa_4(u,v) = (2v-3Ru)/R^2
```

gives exact sequences

```text
0 -> {kernel vectors with 2v=3Ru}
  -> ker L_4
  -> K
  -> 0.
```

The common-root subspace has dimension `3` in the truncated window and `7` in
the full window. Both have the same normalized exceptional representative

```text
u = -(1/3)R,   v = 0,   kappa_4(u,v)=1.
```

This is a canonical upper-face resonance class. It is **not** identified here
with the lower-face C.9 rechart class. The equality of their layer labels is
insufficient: the leading faces, gradings, and gauge quotients differ.

## 9. Remaining exact bridge to Proposition C.9

The fixed-chart identity is now derived and executable. The remaining inputs
needed for a direct independent replay of C.9 are:

1. the exact coefficient-field model for its chosen degree-21 face `p,q`;
2. the four source windows for `f,g` and coefficient windows for `a,b` at each
   of layers one through four;
3. the explicit `k=4` transition tangent expressed in the same lower-face
   coefficient bases;
4. the old/new support transition matrices;
5. the transported residue-adjoint bases and lower-layer forcing terms.

With items 1--2, `fixed_chart_gauge.py` can test the reported residual sequence
`(1,2,1,1)`. With item 3, a nonzero class in the one-dimensional layer-four
quotient would certify that the chart tangent spans it. Items 4--5 then upgrade
the vector-space identification to the support- and residue-compatible
correspondence required by P6-T2.

Only after that classification should the two-sided `F_2` Laurent/band
attachment system be formed.

## 10. Reproduction

Run:

```bash
python research-notes/p6-chart-correspondence/fixed_chart_gauge.py \
  research-notes/p6-chart-correspondence/fixed_chart_example.json

python research-notes/p6-chart-correspondence/chart_correspondence.py \
  research-notes/p6-chart-correspondence/synthetic_k4_contract.json

python research-notes/p6-chart-correspondence/degree21_linear_replay.py \
  research-notes/p6-chart-correspondence/fixtures/degree21_exact_data.json \
  --output /tmp/degree21-linear-replay.json

python research-notes/p6-chart-correspondence/degree21_kernel_decomposition.py \
  research-notes/p6-chart-correspondence/fixtures/degree21_exact_data.json \
  --output /tmp/degree21-kernel-decomposition.json

python -m unittest discover \
  -s research-notes/p6-chart-correspondence \
  -p 'test_*.py' -v
```

## 11. Scope and provenance

This note proves the Keller kernel reduction, elementary wall-shear lemma,
finite support transport, weighted-divergence identity, pure-power
factorization, and arithmetic resonance rule. It independently replays the
archived upper-face matrices and nullspace data.

It does not independently replay Proposition C.9 or Theorem C.10, classify
every complete-chain transition, prove queue exhaustiveness, or solve global
`F_2` attachment.

AI assistance: GPT-5.6 Thinking was used for theorem formulation, proof
drafting, archive triage, and implementation. A human contributor remains
responsible for checking and integrating every assertion.
