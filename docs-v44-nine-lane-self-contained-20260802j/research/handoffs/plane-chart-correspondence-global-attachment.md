---
title: "Model research brief — Plane chart correspondence and global attachment"
description: "A self-contained mathematical handoff for a research model."
---

# Lane 9: Plane chart correspondence and global attachment

<p class="claim-tag">Lane 9 · Updated 2 August 2026</p>

## Problem and scope

Lane 9 separates three kinds of normal-layer direction in the plane Newton
construction: operations inside one fixed chart, rechartings to an adjacent
complete Newton chain, and genuine attachment parameters. The eventual goal
is the two-sided global attachment problem for the branch called `F_2` in the
recorded terminal-boundary analysis. Here `F_2` is a historical branch label,
not a coordinate of a polynomial map.

The actual `F_2` matrices, fixed-chart polynomial-generator table, and
archived replay are not in the current public bundle. Full attachment and the
chart-specific subgroup classification are blocked. The ready problem below
is the coordinate-free finite-dimensional duality on which that future
classification rests.

## Setup and notation

On one smooth boundary component, `S` is its tangential weight, `r` is the
normal order, `M_0` is the leading monomial, and `omega` is the fixed area
form. The invertible change to `(H,W,T)` coordinates sends the order-`r`
determinant equation to

```text
S(d+(r/S)dlog M_0)h_r=((S-r)/S)w_r*omega.
```

The *determinant kernel* consists of normal corrections solving the homogeneous
equation. A *fixed-chart operation* is induced by an allowed
valuation-filtered polynomial automorphism preserving the chosen
approximate-root chart. An *adjacent rechart* changes the approximate root
and is an overlap arrow, not fixed-chart gauge. The *residue adjoint*
represents the dual cokernel by principal parts.

For the stored `(8,28)` face, complete-chain conventions and support windows
are defined in [`manuscripts/06-plane-boundary/appendices/exact-normal-linearization.tex`](../proof-sources/06-plane-boundary/appendices/exact-normal-linearization.md)
and [`manuscripts/06-plane-boundary/appendices/gauge-filtered-residues.tex`](../proof-sources/06-plane-boundary/appendices/gauge-filtered-residues.md).
At a fixed order, let `U_r` be the finite vector space of corrections in the
stated Newton window, `V_r` the finite vector space of determinant residuals,
and `D_r:U_r->V_r` the displayed normal operator. The residue pairing in the
second appendix is a perfect pairing on these finite windows and defines the
transpose `D_r^*`.

## Reusable mathematics

Normal orders decouple over the function field; nonlinearity lies in the
triangular return to finite Newton windows. Matrix left-null vectors and
residue functionals give the same cokernel coordinates. Units:
[`RMU-D25775A5`](../working-mathematics/units/RMU-D25775A5.md), [`JCG-3AE328D9`](../working-mathematics/units/JCG-3AE328D9.md), [`JCG-D44F2B27`](../working-mathematics/units/JCG-D44F2B27.md), [`RMU-9E33C04B`](../working-mathematics/units/RMU-9E33C04B.md).

At layers `1,...,4`, determinant-kernel dimensions are `(2,3,3,1)`.
Maximal support-admissible Laurent operations fill them. Affine polynomial
operations have ranks `(2,3,2,1)`, while fixed-chart complete-chain
operations have ranks `(1,1,2,0)`. The layer-four residual is the rechart

```text
Y -> Y+lambda*X^-4.
```

After separating it, unclassified quotient dimensions are `(1,2,1,0)`.
They are not established moduli or obstructions.

For `F_2`, the final face and degree-`2m` alternating Belyi map are explicit.
Local finite-support solutions exist, the natural five-band global lift is
impossible, and for `m=3` a `C_5`-invariant jet reaches order 520. Fresh
parameters cancel the apparent order-510 and 520 conditions. The nonzero
order-530 value was computed after setting new parameters to zero and is not
a global obstruction. Units: [`JCG-C42D615F`](../working-mathematics/units/JCG-C42D615F.md), [`JCG-42763317`](../working-mathematics/units/JCG-42763317.md), [`JCG-2533E53C`](../working-mathematics/units/JCG-2533E53C.md).

## Exact live problem

For each finite window in the linked appendices, place the determinant map
`D_r`, an abstract fixed-chart operation map `G_r:W_r->ker(D_r)`, and an
abstract rechart map `R_r:C_r->ker(D_r)` in one basis-free exact diagram.
Prove directly from the residue pairing that

```text
(coker D_r)^dual = ker(D_r^*)
```

and identify the dual of
`ker(D_r)/(im(G_r)+im(R_r))` as an explicit annihilator quotient. Prove that
the whole diagram and quotient are unchanged by basis changes and by replacing
`W_r` or `C_r` with a different presentation having the same image. Then
state exactly which matrix a future list of admissible polynomial operations
must supply. This theorem does not classify the missing fixed-chart subgroup,
but it defines the invariant attachment quotient that classification must hit.

## Tasks and deliverables

### P6-L9A0 — Residue-dual quotient theorem

Status: ready.

Inputs: the displayed finite-dimensional complex `D_r:U_r->V_r`, abstract
maps `G_r` and `R_r` with the indicated codomain, the perfect residue pairing
and adjoint defined above, the two linked appendices, and
[`RMU-D25775A5`](../working-mathematics/units/RMU-D25775A5.md), [`JCG-D44F2B27`](../working-mathematics/units/JCG-D44F2B27.md), [`RMU-9E33C04B`](../working-mathematics/units/RMU-9E33C04B.md).

Deliverable: the exact diagram, dual-cokernel and annihilator identifications,
their presentation-independence laws, and a precise interface for the future
fixed-chart and adjacent-rechart matrices.

### P6-L9A — Complete-chain subgroup

Status: blocked until the fixed-chart polynomial generators and their
layerwise matrices are publicly exposed.

Inputs: that generator table, its support bounds, and matrices through layers
one to four.

Deliverable after recovery: compute their layer-one-through-four tangent
images, isolate the adjacent-rechart image, and describe the residual
quotient without coordinates.

### P6-L9B — One-wall correspondence

Status: blocked on P6-L9A.

Inputs: the classified group and one stored adjacent chart.

Deliverable: transport support windows, determinant operator, forcing term,
operation image, rechart tangent, and residue-adjoint functionals.

### P6-L9C — Full `F_2` attachment

Status: blocked until the actual `F_2` blocks are publicly recovered.

Inputs: both endpoint blocks, overlap maps, fresh-parameter ranges, and the
archived replay manifest.

Deliverable after recovery: the full two-sided Laurent or block-Toeplitz
system with both endpoints, every fresh parameter, `C_5` characters, and
cyclic descent.

## Scope cautions

- A divergence-free Laurent field is not automatically an admissible operation.
- An adjacent rechart is not fixed-chart gauge.
- Synthetic wall tests do not establish a theorem about missing `F_2` blocks.
- Setting fresh parameters to zero cannot yield a global obstruction.

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
