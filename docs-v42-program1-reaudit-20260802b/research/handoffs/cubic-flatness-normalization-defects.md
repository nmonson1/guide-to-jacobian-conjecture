---
title: "Model research brief — Cubic flatness and finite normalization defects"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Lane 1</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 2 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v15 · site release <code>living-guide-public-v42-program1-reaudit</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/index.md).

!!! tip "Current proof sources — preferred"
    Use the [current source text and exact labels](../proof-sources/index.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.
# Lane 1: Cubic flatness and finite normalization defects

## Research objective

Let `F:X=A^3_C -> Y=A^3_C` be a Keller map of generic degree three. Let
`R=O(Y)`, `S=O(X)`, and let `B` be the normalization of `R` in `C(X)`.
Lane 1 asks whether `Spec(B) -> Y` is finite flat.

This is a general degree-three Keller question. The named counterexample and
the explicit normalized `A(c),B(c)` family supply examples and boundary
models, but their special formulas are not hypotheses here. Recovering the
original affine source inside the normalization is a separate
boundary-completeness problem; flatness alone does not solve it.

## Reusable mathematics

### 1. The defect is one canonical finite module

Trace gives

```text
B = R + E,               E = ker Tr_(B/R),
Delta_F = Ext^1_R(B,R) = Ext^1_R(E,R).
```

`B` and the rank-two module `E` are reflexive, and `Delta_F` has finite
length. Exactly,

```text
Supp(Delta_F) = {y : B_y is not free over R_y},
B finite flat over R  <=>  Delta_F = 0.
```

At a closed point, with `A=R_y`, a minimal presentation is

```text
0 -> A^b --Phi--> A^(b+2) -> E_y -> 0,
Delta_(F,y) = coker(Phi^dual).
```

After orienting `E_y`, this extends to an alternating self-dual resolution.
Thus the defect is Matlis self-dual and its generator and socle dimensions
are both `b`. If `b=1`, it is an Artinian complete intersection with Koszul
Betti numbers `(1,3,3,1)`.

Retained units: [`RMU-1A8D0001`](../working-mathematics/units/RMU-1A8D0001.md), [`RMU-1A8D0002`](../working-mathematics/units/RMU-1A8D0002.md). Proof source:
[`manuscripts/01-cubic-incidence/appendices/flatness-defect-repairs.tex`](../proof-sources/01-cubic-incidence/appendices/flatness-defect-repairs.md), labels
`prop:cubic-ext-defect` and `prop:cubic-defect-self-duality`.

### 2. Source splitting locates the defect but cannot kill it

Base change to the affine source has a canonical marked factor:

```text
B tensor_R S = S x C.
```

`C` is a normal quadratic `S`-algebra. After choosing a trace-zero generator,
`C=S[eta]/(eta^2-D)`. The `S`-factor is canonical; `eta` and `D` are
choice-dependent. Faithfully flat descent at a source point gives

```text
Supp(Delta_F) subset O_F subset Sing(S_F),
```

where `O_F=Y-F(X)` and `S_F` is the reduced nonproperness set. A defect value
is omitted, so there is no source point there at which to repeat the splitting
argument.

Retained unit: [`RMU-1A8D0003`](../working-mathematics/units/RMU-1A8D0003.md). Proof label:
`prop:cubic-source-splitting`.

### 3. Divisorial anatomy is complete and does not decide isolated defects

At a geometric generic target divisor the complete list is

```text
U0, U1, U2, B.
```

`Ui` means trivial inertia with exactly `i` deleted sheets. `B` means
transposition inertia, with the ramified point deleted and the unramified
point retained. Outside the nonproperness set only `U0` occurs; on a
nonproperness divisor only `U1/U2/B` occur. Three-cycle inertia is excluded,
and generic monodromy is `S3`. This is divisorial information only.

Retained unit: [`RMU-C1DD871B`](../working-mathematics/units/RMU-C1DD871B.md).

### 4. The quadratic resolvent carries exactly the same defect

Let `T` be the normalization in the `S3` Galois closure, put `Q=T^(A3)`, and
let `L` be one nontrivial cubic eigensheaf. Then, after choosing a quadratic
trace-zero generator,

```text
Q = R[w]/(w^2-d),
T = Q + L + L^[2],
L^[3] = Q,
sigma^*L = L^[2] = L^dual.
```

Taking transposition invariants identifies `E` with `L` as an `R`-module.
Consequently

```text
Delta_F = Ext^1_R(L,R),
B flat over R  <=>  L is MCM over Q.
```

This is an equivalence, not merely a sufficient MCM criterion. Dao's theorem
detects a nonzero three-torsion class at a height-two singular prime. Hence a
defect requires a singular curve of the resolvent; an isolated resolvent
singularity cannot carry it.

Retained units: [`RMU-1A8D0004`](../working-mathematics/units/RMU-1A8D0004.md), [`RMU-13177F24`](../working-mathematics/units/RMU-13177F24.md).

### 5. Completed defects and the conditional transverse filter

At a defect point, the completed normalization has one normal local factor of
rank three. Its cubic field is non-Galois with `S3` closure. The finite fibre
is supported at one point and has scheme length

```text
b+3 >= 4.
```

Length four is exactly the one-generator stratum.

Conditional on split rational-double-point transverse type, the subgroup
killed by three is nonzero only for `A_(3r-1)` and `E6`, with at most one
`F_3` coordinate per curve. Both have explicit order-three ideals, two-by-two
matrix factorizations, cyclic covers of type `A_(r-1)` and `D4`, and explicit
transposition quotients.

The exact script
[`manuscripts/01-cubic-incidence/code/verify_ade_matrix_factorizations.py`](../proof-sources/01-cubic-incidence/code/verify_ade_matrix_factorizations.md)
checks the displayed identities. It does not prove the RDP hypothesis or
extension through the closed threefold point.

Retained units: [`RMU-1A8D0005`](../working-mathematics/units/RMU-1A8D0005.md), [`RMU-1A8D0006`](../working-mathematics/units/RMU-1A8D0006.md).

## Named-map and explicit-frame inputs

For the named map, the inverse cubic gives the exact `3/1/0` fibre chart. For
the coprime normalized `A(c),B(c)` family, the completion, deleted boundary,
discriminant, nonproperness set, omission locus, and divisorial examples are
explicit. These are test cases for the general problem; they do not make an
arbitrary cubic normalization an `A,B`-frame member. Do not rederive those
formulas unless a new argument strengthens their scope.

## Exact live problem

At a candidate omitted defect value, extract from the actual normalization:

1. the square class `d` defining the normal quadratic resolvent;
2. every height-two prime of its singular locus;
3. the conductor and different;
4. a fractional-ideal or finite-presentation representative of `L`;
5. the local class vector `([L_p])_p`.

Only then can one test extension of the transverse factorizations through the
closed threefold point or derive a Keller-specific vanishing constraint.


## Useful deliverable

Return one self-contained mathematical artifact that either extracts a
genuine item from the five-part resolvent carrier above, proves that the
available hypotheses do not determine it, extends a transverse MCM model
through a closed threefold point, or supplies a Keller-specific vanishing
mechanism. State every added hypothesis and distinguish a local formal,
codimension-two, or computational conclusion from finite flatness and from
boundary completeness. A rigorous partial result on one carrier component is
useful; it need not close the whole lane.

## Tasks

### P1-T1A — Extract the actual resolvent carrier

Actor: `online_model`. Status: ready.

Produce `d`, all height-two singular primes, conductor/different, a
presentation of `L`, and its local class vector for the actual Keller
configuration. If the current data do not determine an object, prove that
non-determination rather than inventing it.

### P1-T1B — Extend or exclude the transverse MCM models

Actor: `online_model`. Status: blocked on P1-T1A.

Construct a matrix factorization over the full three-dimensional resolvent
whose generic restrictions are the displayed transverse templates, or prove
a Keller-specific condition forcing the class vector to vanish.

### P1-T2 — Compute a finite class or exceptional-lattice obstruction

Actor: `local_symbolic`. Status: blocked on P1-T1A.

The intersection matrix, discrepancy vector, conductor data, and class
coordinates must come from T1A and be hash-pinned before computation.

### P1-T3 — Keep boundary completeness separate

Actor: `online_model`. Status: ready.

State exactly which conclusions follow from finite flatness, which require
recovery of the affine opening, and which use the explicit normalized frame.

## Do not do

- Do not infer flatness from normality, `S3` monodromy, or reflexivity.
- Do not use the stale `U1/U2/B` list without `U0`.
- Do not call the source-pullback generator or polynomial form canonical.
- Do not infer an MCM module from a smooth cubic-axis picture without a depth
  certificate and codimension-two comparison.
- Do not revive theta-commutativity without resolving the Weil-pairing
  commutator.
- Do not run an exceptional-lattice computation before its actual inputs
  exist, and do not infer boundary completeness from flatness.

The retained-unit pages and complete proof-source pages linked above are the public mathematical record for this lane.

[Back to the portfolio hub](state-of-the-program.md)
