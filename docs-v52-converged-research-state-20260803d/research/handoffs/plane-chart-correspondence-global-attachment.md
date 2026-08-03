---
title: "Model research brief — Recovering the actual two-chart attachment chain"
description: "A self-contained mathematical handoff for a research model."
---

# Recovering the actual two-chart attachment chain

<p class="claim-tag">Lane 9 · Updated 3 August 2026</p>

Lane 9 · 2026-08-03

## Scope

Recover the inherited cross-layer relations needed for a parameter-complete
actual $F_2$ attachment. The order-$510$, $520$, and $530$ cancellations
in the retained rational slice are known; rerunning a zero-fresh-parameter
slice is not the frontier.

## Setup and definitions

After the denominator-five shear, write $w=a-J$ and let
$\langle w\rangle_5$ be its residue in $\{0,1,2,3,4\}$. The exact maximal
support windows are

\[
S_P=\{(a,J):-60\le w\le15,\ 0\le J\le60-\langle w\rangle_5,
\ 5a-17J\le3\},
\]

\[
S_Q=\{(a,J):-100\le w\le25,\ 0\le J\le100-\langle w\rangle_5,
\ 5a-17J\le5\}.
\]

With $x=t^{-25}$, $y=t^{17}z$, and $u=z^5$, write

\[
P=t^{-3}\sum_rt^rA_r(z),\qquad
Q=t^{-5}\sum_rt^rB_r(z),
\]

where
$A_r=z^{(1-2r)\bmod5}\bar A_r(u)$ and
$B_r=z^{(-2r)\bmod5}\bar B_r(u)$.
At each order, the parameter-complete attachment equation is
$M_r(x_r,p_r)=b_r$, where $M_r=[C_r\mid P_r]$; a left-null functional of
$C_r$ is intrinsic only if it also annihilates every fresh-parameter column
$P_r$.

## Results to use

- The support counts are exact: $4433$ $P$-coefficients in $981$
  nonempty layers, $12340$ $Q$-coefficients in $1663$ layers, and $2681$
  determinant-output layers. The first target coordinate outside the linear
  image is the constant at order $510$.
- One exact retained rational generator fixes order $10$, cancels
  $\omega_{510}$ at order $260$, and uses an order-$270$ kernel direction
  to cancel $\omega_{520}$.
- The retained multiple-of-ten slice contains $212$ free slots across $52$
  positive layers through order $520$, but only the selected orders
  $10,260,270$ are assigned.
- The earlier nonzero $\omega_{530}$ was obtained with all new coordinates
  fixed to zero. Reopening five order-$280$ RREF coordinates gives
  $\dim\ker\omega_{510}=4$, joint kernel dimension $3$, and a nonzero
  $\omega_{530}$ functional on that joint kernel. An exact fresh direction
  cancels $\omega_{530}$ and the determinant through order $530$.
- This is still a slice: only order $280$ was reopened. The maximal-support
  independent-coefficient enlargement omits inherited cross-layer descent
  relations; the rational generator does not symbolicize all RREF coordinates;
  and no adjacent-chart/global descent is attached.
- Independently, all $73$ ambient wall-groupoid tests replay. The bare $k=4$
  wall begins at normal layer seven and leaves the fixed chart; saturation
  changes the stored deformation dimensions $186\to294$ and equation
  dimensions $257\to300$, and the pairwise/triple overlaps and degree-eight
  quotient flow are exact. These are ambient transports, not the missing
  actual adjacent complete-chain chart.

## Example: fresh order 280

The order-$280$ direction that cancels $\omega_{530}$ is an example of why
fresh coordinates must be retained. It does not prove a parameter-complete
continuation beyond $530$ or supply the missing inherited relations.

## Live problem

Recover the actual-chain relation ideal among the maximal-support coefficients
and export the first genuine parameter-complete order block. The key output is
the relation map itself, not another independent-coefficient recurrence.

## Tasks

### L9-T1 — Recover inherited cross-layer relations

Inputs: the [Lane 8/9 exact recovery package](lane-9-source-packet.md),
its [machine-readable evidence](lane-9-source-packet.md),
the [parameter-complete recurrence theorem](lane-9-source-packet.md),
and the [ambient wall-shear bundle](lane-9-source-packet.md).

Deliverable: an ordered generator set for the inherited relation ideal through
order $530$, a map from actual complete-chain parameters to the $4433+12340$
ambient coefficients, and either the full order-$530$ block or the exact first
relation that cannot be recovered from present inputs.

Dependencies: native complete-chain descent/presentation formulas, including
their first-occurrence orders and $C_5$ characters.

Limits: the present independent-coefficient support bundle does not contain
those formulas, so a parameter-complete actual-chain run is blocked until they
are recovered; do not infer them from the known rational slice alone.

### L9-T2 — Attach the actual adjacent chart

Inputs: L9-T1, the exact coefficient/equation wall transports, and the
degree-eight quotient candidate $Q\mapsto Q+16s$ from the wall bundle, with
the [73-test replay receipt](lane-9-source-packet.md).

Deliverable: forward and inverse coefficient, equation, operation, support,
dual, and forcing maps on the overlap, with cocycle and stabilizer proofs; then
transport the parameter-complete block across it.

Dependencies: L9-T1 and the native adjacent monomial presentation.

Limits: the bare $k=4$ shear starts at normal order seven, not four; the
quotient translation requires a degree-eight Kummer lift and is not yet the
actual adjacent chart.

Alternative connections: constraints from the degree-$125$ support queue in
Lane 8 are welcome if they derive actual relations rather than specialize
fresh parameters to zero.

## Limits

The exact cancellations through $530$ are slice results. They refute the
zero-fresh-coordinate obstruction but do not establish global attachment,
parameter-complete continuation, or a complete-chain descent theorem.

## Direct sources

- [Fresh-order-280 exact program](lane-9-source-packet.md)
- [Parameter-complete solver](lane-9-source-packet.md)
- [Normal-linearization TeX](../proof-sources/06-plane-boundary/appendices/exact-normal-linearization.md)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-9-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
