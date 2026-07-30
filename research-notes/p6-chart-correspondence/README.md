# Program 6 chart correspondence: exact replay and resonance reduction

**Status:** research intake note, not an integrated claim or manuscript result.

This note develops Program 6 task P6-T2: replace fixed-chart surjectivity by a
support-aware distinction between fixed-chart gauge and tangent directions to
adjacent complete-chain charts. It now contains both a general reduction and a
non-synthetic replay of the archived degree-21 upper-face complex:

1. determinant-kernel directions are divergence-free rational source fields;
2. elementary wall shears give explicit adjacent-chart tangent directions;
3. Newton support and residue functionals transport by finite exact formulas;
4. a rational diagnostic computes `ker(D_r)/(gauge + rechart)`;
5. all 24 archived full/truncated degree-21 layer matrices and their recorded
   left/right nullspaces are independently replayed over `Q`;
6. the raw degree-21 kernel has a canonical common-root defect whose only
   exceptional polynomial classes occur at layers `4, 8, 12`;
7. at layer four the exceptional quotient is one-dimensional in both support
   models and has the same normalized representative.

The last point recovers a basis-independent algebraic precursor of the stored
`k = 4` rechart. It does not independently prove that the exceptional vector is
an admissible complete-chain transition; that still requires the actual chart
map and support transport.

## 1. Kernel directions as divergence-free source fields

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
the classification of divergence-free vector fields subject to the
complete-chain filtration and finite Newton windows.

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

## 4. The finite quotient to compute

At layer `r` in chart `C`, put

```text
H_r(C) = ker D_r,
B_r(C) = span of supported fixed-chart gauge vectors,
R_r(C) = span of supported tangents of enumerated adjacent charts.
```

The diagnostic quantity is

```text
o_r(C) = dim H_r(C) - dim(B_r(C) + R_r(C)).
```

A nonzero `o_r(C)` is not automatically an obstruction. It is an unclassified
kernel direction and may indicate a missing adjacent chart.

`chart_correspondence.py` performs this quotient exactly over `Q`, verifies all
supplied gauge and rechart vectors, returns quotient representatives, and
computes the transported support `T_k(S)`.

## 5. Non-synthetic replay of the archived degree-21 layers

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

These are raw upper-face dimensions. They are not the later specialized
fixed-chart residual dimensions `(1,2,1,1)`.

## 6. Pure-power face factorization

The layer-four phenomenon admits a basis-independent reduction.

### Proposition 3 (common-root defect factorization)

Let

```text
A0 = R^m,    B0 = R^n,
alpha = d m, beta = d n,
```

with positive integers `d,m,n`, `n >= m`, and nonconstant `R in K[z]`. Define

```text
D_r(a,b)
  = (alpha-r)a B0' - beta B0 a'
    + alpha A0 b' + (r-beta)b A0'
```

and the common-root defect

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

and add

```text
(r-beta)R^(m-1)R'N.
```

The coefficient of `R^(n-1)R'a` becomes

```text
-n[d(n-m)+(r-beta)] = n(alpha-r),
```

while the other three terms are exactly the remaining terms of `D_r`.

### Corollary 4 (arithmetic resonance rule)

If `D_r(a,b)=0`, then

```text
(N^d R^(r-beta))' = 0,
```

so

```text
N^d = c R^(beta-r)
```

for a constant `c`. If `R` has a simple zero and `N` is polynomial, a nonzero
`N` can occur only when

```text
beta-r is in d Z_{>=0}.
```

In that case

```text
N = c0 R^((beta-r)/d).
```

Thus, after quotienting by the common-root relation `N=0`, each arithmetic
resonance contributes at most one raw kernel class before support restrictions.

## 7. The degree-21 layer-four class

For the archived degree-21 operator,

```text
m=2, n=3, d=4, beta=12,
N=2v-3Ru,

L_r(u,v) = R(4R N' + (r-12)R'N).
```

The only possible polynomial resonance layers in `1 <= r <= 12` are

```text
r = 4, 8, 12.
```

`degree21_kernel_decomposition.py` verifies the factorization on every domain
basis vector and the defect equation on every archived kernel vector. In both
the truncated and full windows, the exceptional defect image has dimension one
exactly at `r=4,8,12` and is zero elsewhere.

At layer four, define

```text
kappa_4(u,v) = (2v-3Ru)/R^2.
```

The archived windows give exact sequences

```text
0 -> {kernel vectors with 2v=3Ru}
  -> ker L_4
  -> K
  -> 0.
```

The common-root subspace has dimension `3` in the truncated window and `7` in
the full window. Both windows have the same normalized exceptional
representative:

```text
u = -(1/3) R,    v = 0,    kappa_4(u,v)=1.
```

Equivalently, with `R=y^8-y^7`,

```text
u = (1/3)y^7 - (1/3)y^8.
```

This proves that the raw layer-four complex contains a canonical
one-dimensional non-common-root quotient, independent of the nullspace basis
and stable under passage from the truncated to the full support window. The
reader manuscript identifies that unique residual direction with the
`Y -> Y+lambda X^(-4)` complete-chain operation. The replay here verifies the
algebraic uniqueness and representative; it does not independently verify the
geometric chart identification.

The analogous raw classes at layers eight and twelve should be treated as
resonance flags, not automatically as rechart directions.

## 8. Remaining exact bridge to P6-T2

The next required data are now narrower than a full matrix export:

1. the fixed-chart action `Theta_r` in the same ordered degree-21 bases;
2. the support windows for its source-vector-field components;
3. the image of `ker(D_r Theta_r)` inside `ker D_r`;
4. the explicit `k=4` chart tangent in the raw `(u,v)` basis;
5. old/new support transition matrices and residue-adjoint transport.

For layer four, it is enough to show that the chart tangent has
`kappa_4 != 0`. The one-dimensional quotient then forces it to span the
exceptional class. The harder layers one through three require the actual
fixed-chart action: their raw kernels satisfy the common-root relation, but the
recorded fixed-chart residual dimensions are still nonzero.

After this bridge is certified, the same workflow can be applied to every
residual `F_2` layer before forming the two-sided Laurent/band matching system.

## 9. Reproduction

Run:

```bash
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

## 10. Scope and provenance

This note proves the kernel-reduction identity, elementary wall-shear lemma,
finite support-transport formula, pure-power factorization, and arithmetic
resonance rule. It independently replays the displayed degree-21 linear
formula and archived nullspace data.

It does not prove the global chart-correspondence theorem, classify every
complete-chain transition, replay the later layer-five-through-seven no-gluing
certificate, prove queue exhaustiveness, or solve global `F_2` attachment.

AI assistance: GPT-5.6 Thinking was used for theorem formulation, proof
drafting, archive triage, and implementation. A human contributor remains
responsible for checking and integrating every assertion.
