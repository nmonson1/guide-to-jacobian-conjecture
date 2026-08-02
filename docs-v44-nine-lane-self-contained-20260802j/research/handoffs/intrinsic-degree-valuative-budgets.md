---
title: "Model research brief — Intrinsic degree and valuative budgets"
description: "A self-contained mathematical handoff for a research model."
---

# Lane 5: Intrinsic degree and valuative budgets

<p class="claim-tag">Lane 5 · Updated 2 August 2026</p>

## Problem and scope

Fix the explicit three-dimensional degree-seven Keller counterexample
`F=(P,Q,R):A^3_(x,y,z)->A^3`. Lane 5 seeks a lower bound for the least
ordinary coordinate degree in its polynomial left--right orbit. A bound in
one coordinate presentation is insufficient; source and target automorphisms
must be controlled.

Here *Keller* means `det DF=1`, and *counterexample* means that `F` is not a
polynomial automorphism. The exact map and its proof/citation boundary are in
[`manuscripts/01-cubic-incidence/main.tex`](../proof-sources/01-cubic-incidence/main.md).

## Setup and notation

The target-independent object is the image algebra

```text
A=C[P,Q,R] subset C[x,y,z].
```

For any exhaustive semidegree `delta` on `C[x,y,z]`, write

```text
F_s^delta A={f in A: delta(f)<=s},
V_d(A)=A intersect C[x,y,z]_(ordinary degree <=d).
```

The certificate semidegree is a particular such filtration; its monomial
weights and the generators of the triangular normalization group are not
currently exposed in the public sources. Consequently the certificate's
full orbit statement is not advertised as ready.

On the discriminant normalization, with coordinates `(c,t)`, let
`partial_P` be the target derivation characterized by
`partial_P(P)=1`, `partial_P(Q)=partial_P(R)=0`, and let the bar denote
pullback to the normalization. In the displayed chart define

```text
N(f)=-1/[4(2-3ct)] * overline(partial_P f).
```

For three functions put

```text
W(f_0,f_1,f_2)=det(D_i(f_j))_(0<=i,j<=2),
(D_0,D_1,D_2)=(partial_t,N,partial_c).
```

If an isomorphism `phi:A->A'` transports the filtrations and normalized
charts and the derivation frames satisfy

```text
(D'_0,D'_1,D'_2)^T=M*(phi D_0 phi^-1,phi D_1 phi^-1,phi D_2 phi^-1)^T
```

for `M in GL_3(Frac(A'))`, call `phi` *frame-admissible*.

## Reusable mathematics

For the certificate semidegree, the recorded exact values are

```text
a=delta(x),  b=delta(y),  h=delta(y+xz/3),
delta(R)=2a+h,
delta(Q)=2a+h+2b,
delta(P)=2a+h+3b.
```

Ramification has `e in {1,3}` and tame inertia excludes `e=3`; the relevant
coordinate-infinity valuations are unramified. Every classified stratum with
`delta(Q)<=9` has an exact certificate proving

```text
trdeg C[V_6(A)] <= 2.
```

Uniform quadratic `z`-shears are closed by explicit minors. Thus any degree-six
representative within this normalization lies in the branch `delta(Q)>=10`.
The determinant of `partial_t`, `N`, and `partial_c` is the Jacobian, giving
the exact conormal/Wronskian bridge.

Proof and computation routes are in the [low-degree](minimum-degree-and-quartic-exclusions.md),
[stable-moduli](stable-moduli.md), and
[plane-boundary](plane-boundary-obstructions.md) dossiers, including
[`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex`](../proof-sources/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.md).

No current proof makes `delta` invariant under arbitrary source changes or
stabilization, and zero Wronskian is unknown when `delta(Q)>=10`.

## Exact live problem

Let `K=Frac(A)`. Characterize the birational changes `phi:K->K'` that carry
the three-dimensional derivation distribution spanned by `(D_0,D_1,D_2)` to
the corresponding distribution on `K'`. Prove that such a change has a
unique frame matrix `M` after bases are fixed and, for every
`f_0,f_1,f_2 in A`, satisfies

```text
W'(phi(f_0),phi(f_1),phi(f_2))=det(M)*phi(W(f_0,f_1,f_2)).
```

Prove the converse under a stated generic-rank hypothesis: preservation of
all Wronskian-zero triples forces preservation of the derivation distribution.
Determine the minimal hypotheses under which this transports vanishing on a
filtered finite-dimensional subspace. Applying it to the particular counterexample
requires the missing semidegree and automorphism table. Once those data are
public, the downstream target is:

> In every normalized unramified branch with `delta(Q)>=10`, the corrected
> normal Wronskian vanishes on `V_6(A)`.

The transformation law is logically prior: without it, the proposed degree
budget is not an orbit invariant.

## Tasks and deliverables

### L5-T1A — Abstract covariance lemma

Status: ready.

Inputs: the displayed definitions of `A`, `K`, `V_d(A)`, `N`, `W`, and the
two rank-three derivation distributions. Work in characteristic zero and
state any generic-rank or separability hypothesis used.

Deliverable: the characterization and converse above, the determinant
transformation law, the exact filtration-transport condition needed for a
subspace such as `V_6(A)`, and a counterexample showing why that condition
cannot simply be omitted.

### L5-T1B — Counterexample-specific transformation law

Status: blocked until the certificate semidegree and normalizing triangular
generators are exposed as public inputs.

Inputs: the future public monomial weights, filtration generators, and exact
source and target triangular-generator table.

Deliverable: compute `M` and the transported filtration for every generator,
then identify the largest proved invariance subgroup.

### L5-T2 — Residual bounded-Wronskian theorem

Status: blocked on L5-T1B.

Inputs: the invariant formulation produced by L5-T1B and the certified
`delta(Q)<=9` classification.

Deliverable: a proof in the `delta(Q)>=10` branch, or an explicit image-algebra
element with nonzero Wronskian and its behavior under allowed shears.

### L5-T3 — Finite exact search

Status: local CAS follow-up; blocked until L5-T2 gives a finite ansatz.

Inputs: the finite ansatz and coefficient ring supplied by L5-T2.

Deliverable: a hash-pinned coefficient space and the exact meaning of a
witness or unit certificate.

## Scope cautions

- A coordinate semidegree is not intrinsically left--right invariant.
- Dimension counts alone do not prove a degree bound.
- The abstract covariance lemma does not identify the counterexample's
  admissible automorphism group.
- Ordinary source degree and a chosen semidegree filtration are distinct.

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
