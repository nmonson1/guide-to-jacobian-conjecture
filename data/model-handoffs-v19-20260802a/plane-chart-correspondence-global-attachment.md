# Lane 9: Plane chart correspondence and global attachment

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
operations have ranks `(2,3,2,1)`, while the previously encoded fixed-chart
complete-chain operations have ranks `(1,1,2,0)`. These ranks do not identify
the remaining layer-four direction with a particular rechart.

Indeed, in lower-face coordinates `t=Y`, `z=XY^2`, the bare wall shear
`Y'=Y+lambda X^-k` has exact transport

```text
t'=t(1+h),   z'=z(1+h)^2,   h=lambda t^(2k-1)z^-k.
```

Its normal order is `2k-1`; for `k=4` it begins at layer seven, not four, and
no filtration-preserving conjugacy with invertible associated graded lowers
that order. The old direct layer-four/`k=4` identification is superseded.

For `F_2`, the final face and degree-`2m` alternating Belyi map are explicit.
Local finite-support solutions exist, the natural five-band global lift is
impossible, and for `m=3` a `C_5`-invariant jet reaches order 520. Fresh
parameters cancel the apparent order-510 and 520 conditions. The nonzero
order-530 value was computed after setting new parameters to zero and is not
a global obstruction. Units: [`JCG-C42D615F`](../working-mathematics/units/JCG-C42D615F.md), [`JCG-42763317`](../working-mathematics/units/JCG-42763317.md), [`JCG-2533E53C`](../working-mathematics/units/JCG-2533E53C.md).

Through layer 15 the exact `k=4` transports form an additive ambient wall
groupoid. The 186-dimensional coefficient window has a 294-dimensional
minimal saturation; one transported chart meets the old chart in dimension
89, while the all-parameter intersection has dimension 68. The nonlinear
master equation, its differentiated complex, residue-dual functionals and
forcing pairings all transport covariantly. A corrected layer-four candidate
is Hamiltonian and descends to the quotient translation `Q -> Q+16s` on a
degree-eight monomial quotient. It has not been identified with the archived
layer-four residual or the actual adjacent complete-chain chart. Unit:
[`RMU-6C9E0010`](../working-mathematics/units/RMU-6C9E0010.md); exact report and 73-test packet:
[`research-notes/lane9-wall-shear-20260802-v1/`](lane-9-source-packet.md).

The incomplete planar strategy [`RMU-6D8E0011`](../working-mathematics/units/RMU-6D8E0011.md) makes the overlap with Lane 8
explicit: Lane 8 would route every minimal counterexample to a terminal
complete-chain system, while this lane would have to prove simultaneous
two-sided finite support impossible or realize an admissible
complexity-lowering rechart.  The local no-go calculations attached to that
strategy do not prove either global step.

## Exact live problem

Construct the actual adjacent complete-chain chart corresponding to the
finite `k=4` wall saturation, or prove that no chart preserving the current
Newton filtration can realize it. The candidate must reproduce the exact
coefficient and equation transports, inverse and cocycle laws, residue-dual
pairing, and pairwise/triple overlap spaces in [`RMU-6C9E0010`](../working-mathematics/units/RMU-6C9E0010.md). If a changed
filtration or quotient chart is necessary, specify it and determine whether
the quotient translation `Q -> Q+16s` pulls back to the archived layer-four
residual. This task concerns the supplied ambient groupoid; it does not
require the unavailable order-520 `F_2` blocks.

## Tasks and deliverables

### P6-L9A0 — Realize the finite ambient wall groupoid

Status: ready.

Inputs: [`RMU-6C9E0010`](../working-mathematics/units/RMU-6C9E0010.md), all reports, exact transports and tests in
[`research-notes/lane9-wall-shear-20260802-v1/`](lane-9-source-packet.md), and the two normal-
linearization appendices linked above.

Deliverable: an explicit adjacent monomial or quotient chart whose transition
maps induce the supplied finite transports and overlap dimensions, together
with its stabilizer and support windows; or a proof of incompatibility with
the current filtration and the minimal corrected filtration data.

### P6-L9A — Complete-chain subgroup

Status: blocked until the fixed-chart polynomial generators and their
layerwise matrices are publicly exposed.

Inputs: that generator table, its support bounds, and matrices through layers
one to four.

Deliverable after recovery: compute their layer-one-through-four tangent
images, isolate the adjacent-rechart image, and describe the residual
quotient without coordinates.

### P6-L9B — One-wall correspondence

Status: the ambient transport is complete; the actual-chart comparison is
blocked on P6-L9A0 and the fixed-chart subgroup on P6-L9A.

Inputs: the ambient wall groupoid, the classified group, and one actual
adjacent chart produced by P6-L9A0.

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
- The terminal-descent proposal [`RMU-6D8E0011`](../working-mathematics/units/RMU-6D8E0011.md) is an incomplete proof strategy,
  not a proved global attachment theorem.
