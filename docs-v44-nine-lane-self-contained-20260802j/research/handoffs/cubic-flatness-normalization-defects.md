---
title: "Model research brief — Cubic flatness and finite normalization defects"
description: "A self-contained mathematical handoff for a research model."
---

# Lane 1: Cubic flatness and finite normalization defects

<p class="claim-tag">Lane 1 · Updated 2 August 2026</p>

## Problem and scope

Let `F:X=A^3_C -> Y=A^3_C` be a Keller map of separable generic degree
three. Put `R=O(Y)`, `S=O(X)`, and let `B` be the integral closure of `R` in
`C(X)`. The problem is:

Here a *Keller map* is a polynomial map with nonzero constant Jacobian
determinant, normalized on this page to `det DF=1`. A *counterexample* means
a noninvertible Keller map.

> Must the finite morphism `Spec(B) -> Y` be flat?

This concerns every degree-three Keller map. It is distinct from recovering
the affine open `X` inside `Spec(B)`; finite flatness alone does not identify
which boundary was deleted.

## Setup and notation

Trace splits `B=R+E`, where `E=ker(Tr_(B/R))` has rank two. Define

```text
Delta_F = Ext^1_R(B,R) = Ext^1_R(E,R).
```

Let `T` be the normalization in the `S_3` Galois closure of `C(X)/C(Y)` and
put `Q=T^(A_3)`. The cyclic cubic part over `Q` has a rank-one reflexive
eigensheaf `L`; `L^[i]` denotes its reflexive powers and `[L_p]` its local
divisor class at a prime `p`. Write `O_F=Y-F(X)` and let `S_F` be the reduced
nonproperness set.

## Reusable mathematics

`B` and `E` are reflexive, `Delta_F` has finite length, and

```text
Supp(Delta_F) = {y : B_y is not free over R_y},
B is finite flat over R  <=>  Delta_F=0.
```

At a closed point `y`, put `A=R_y`. A minimal presentation

```text
0 -> A^b --Phi--> A^(b+2) -> E_y -> 0
```

presents `Delta_(F,y)` by `coker(Phi^dual)`. Here `b` is the minimal number
of relations beyond the generic rank two. After orienting `E_y`, the
resolution is alternating and self-dual. The case `b=1` (the
one-generator defect) is an Artinian complete intersection with Betti
numbers `(1,3,3,1)`.

Units: [`RMU-1A8D0001`](../working-mathematics/units/RMU-1A8D0001.md), [`RMU-1A8D0002`](../working-mathematics/units/RMU-1A8D0002.md). Full proof:
[`manuscripts/01-cubic-incidence/appendices/flatness-defect-repairs.tex`](../proof-sources/01-cubic-incidence/appendices/flatness-defect-repairs.md),
labels `prop:cubic-ext-defect` and `prop:cubic-defect-self-duality`.

After pullback to the affine source,

```text
B tensor_R S = S x C,
```

where the `S`-factor is canonical and `C` is a normal quadratic `S`-algebra.
A chosen trace-zero generator can write `C=S[eta]/(eta^2-D)`; `eta` and `D`
are not canonical. Faithfully flat descent at source points gives

```text
Supp(Delta_F) subset O_F subset Sing(S_F).
```

Unit: [`RMU-1A8D0003`](../working-mathematics/units/RMU-1A8D0003.md); proof label `prop:cubic-source-splitting`.

Over the quadratic resolvent,

```text
T = Q + L + L^[2],     L^[3]=Q,
sigma^*L=L^[2]=L^dual,
Delta_F=Ext^1_R(L,R).
```

Here `L` is also regarded as an `R`-module by restriction of scalars. The
duality calculation in the cited source identifies the displayed Ext
vanishing with `L` being maximal Cohen--Macaulay over `Q`. Thus `B` is flat
over `R` exactly when `L` is maximal Cohen--Macaulay over `Q`. A nonzero
defect forces a height-two singular prime of `Q` carrying
nontrivial three-torsion; an isolated singularity cannot carry it. Units:
[`RMU-1A8D0004`](../working-mathematics/units/RMU-1A8D0004.md), [`RMU-13177F24`](../working-mathematics/units/RMU-13177F24.md).

At `y in Supp(Delta_F)`, the completed normalization has one normal local
factor of rank three. Its finite fibre has scheme length `b+3>=4`.
Conditional on split rational-double-point transverse type, only
`A_(3r-1)` and `E6` carry the required three-torsion. This does not prove the
RDP hypothesis or extension through the closed threefold point. Units:
[`RMU-1A8D0005`](../working-mathematics/units/RMU-1A8D0005.md), [`RMU-1A8D0006`](../working-mathematics/units/RMU-1A8D0006.md). Exact identity checker:
[`manuscripts/01-cubic-incidence/code/verify_ade_matrix_factorizations.py`](../proof-sources/01-cubic-incidence/code/verify_ade_matrix_factorizations.md).

## Optional explicit example

The Alpöge--Fable counterexample is the marked-simple-root cubic cover. In
the normalized frame it is `A(c)=c`, `B(c)=-2`; the general frame is

```text
P_(a,b,c)(T)=A(c)T^3+B(c)T^2+bT-2a,
x=2/P'(t),  y=t-P'(t)/2.
```

The exact frame and reconstruction are in
[`manuscripts/01-cubic-incidence/main.tex`](../proof-sources/01-cubic-incidence/main.md), at labels `eq:frame`, `eq:ab-map`,
and `eq:inverse-cubic`. This example tests the general theory; its formulas
are not hypotheses on arbitrary `F`.

## Exact live problem

Prove or refute:

> Let `F` be any separable generic-degree-three Keller map and form
> `R subset Q subset T` and `L` as above. Can a height-two singular prime of
> `Q` support a nontrivial order-three class `[L_p]` after imposing both the
> multiplication and involution of the normal `S_3`-algebra `T` and the
> global base-change identity `B tensor_R S = S x C`?

A proof gives `Delta_F=0`. A counterexample at the level of local algebra is
also useful: it would identify which additional Keller-origin constraint is
missing, without claiming to come from a global polynomial map.

## Tasks and deliverables

### P1-T1 — Derive a Keller-origin constraint

Status: ready.

Inputs: [`RMU-1A8D0001`](../working-mathematics/units/RMU-1A8D0001.md), [`RMU-1A8D0003`](../working-mathematics/units/RMU-1A8D0003.md), [`RMU-1A8D0004`](../working-mathematics/units/RMU-1A8D0004.md), [`RMU-13177F24`](../working-mathematics/units/RMU-13177F24.md), and
the proof labels above. For a local test model take a complete regular local
complex algebra `R` of dimension three, a finite normal quadratic
`R`-algebra `Q` with its involution, an order-three rank-one reflexive
`Q`-module `L`, multiplication data `L^[i] tensor L^[j] -> L^[i+j]`, and a
normal algebra `T=Q+L+L^[2]` on which the involution exchanges `L` and
`L^[2]`.

Deliverable: either exclude the height-two three-torsion carrier for every
model arising from a global `R -> S`, or construct the complete local algebra
data above and identify exactly which global Keller or source-splitting input
it does not realize. A tuple `(R,Q,L,T)` by itself is not said to satisfy
source splitting because that condition also requires `S` and `B -> S`.

Limit: a local model alone is not a Keller counterexample.

### P1-T2 — Test the explicit marked-root example

Status: ready benchmark; not the general theorem.

Inputs: the explicit frame and reconstruction equations above.

Deliverable: compute its resolvent, eigensheaf, conductor, and different, and
explain why its finite-flat completion has no `Delta_F` defect despite its
omitted values.

### P1-T3 — Recover the affine opening

Status: blocked until a reconstruction category is fixed.

Missing input: a definition of the objects and equivalences being classified,
including whether the completion is a finite flat algebra or a finite cover
with normalization, which ramification divisor is marked, and whether the
deleted boundary is a reduced divisor, a Cartier divisor with multiplicity,
or a conductor subscheme.

Deliverable after that choice: a theorem giving sufficient marked boundary
data for recovering `X`, with counterexamples showing what flatness and the
unmarked completion do not determine.

## Scope cautions

- Normality, reflexivity, and `S_3` monodromy do not imply flatness.
- The canonical source factor does not make a chosen quadratic generator canonical.
- Divisorial ramification data do not decide an isolated finite-length defect.
- The ADE calculation is conditional on the stated transverse type.

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
