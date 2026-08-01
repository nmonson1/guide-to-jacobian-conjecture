---
title: "Model research brief — Plane chart correspondence and global attachment"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Lane 9</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 1 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v13 · site release <code>living-guide-public-v40-lane-handoffs</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/index.md).

!!! tip "Current text proofs — preferred"
    Use the [current TeX source and exact label anchors](../proof-sources/index.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.
# Lane 9: Plane chart correspondence and global attachment

## Research objective

Develop the local-to-global chart theory missing from the plane terminal
computations.  Distinguish gauge inside one complete-chain chart from genuine
transitions to adjacent charts, then decide whether the flexible `F_2` branch
globalizes or is obstructed by support and cyclic descent.

The primary reference is [Program 6](plane-boundary-obstructions.md).  Use
[Lane 8](plane-newton-queue-terminal-certificates.md) for the upstream queue
and terminal-certificate problem.  Boundary-gluing ideas from
[Lane 2](boundary-completeness-torelli-at-infinity.md) and valuative ideas from
[Lane 5](intrinsic-degree-valuative-budgets.md) may transfer, but their objects
are not automatically identical to complete-chain charts.

## Reusable mathematics

Normal deformation at a fixed boundary face is controlled order by order by
the displayed linear operator `D_r`.  Its filtered residue adjoint identifies
matrix left kernels with explicit compatibility functionals.  Without support
restrictions, the formal change of variables `(W,T,H)` linearizes the
determinant equation on one smooth boundary component and decouples normal
orders.  Thus unrestricted formal integration is not the main difficulty.

The `F_2` complete-chain branch has an exact `C_5`-invariant supported jet
through order 520.  Fresh kernel parameters cancel the apparent obstruction
coordinates at orders 510 and 520.  A nonzero coordinate at order 530 is known
only on the slice where all newly available parameters are set to zero.  It is
not a global obstruction.

A separate Lane 9 toolkit has six passing structural tests, but its received
form does not contain the actual `F_2` matrices and blocks or the archived
`C9` replay.  Its averaging lemma alone supplies no obstruction.  Program 5
filtered-operation tools recovered on GitHub PR 1 are useful analogies, not a
proof of complete-chain admissibility or global attachment.

## Live problem

First prove a chart-correspondence theorem.  It should state exactly:

- which kernel directions are internal gauge in a fixed chart;
- which operations change approximate roots or cross to an adjacent chart;
- how Newton support windows, residue conditions, and lattice quotients
  transform;
- how two chart descriptions of the same formal branch are recognized;
- what cocycle condition is required on triple overlaps.

Then return to `F_2` as a two-sided construction/obstruction problem:

1. retain every new kernel parameter and affine-linear term at each order;
2. solve the band-convolution recurrence rather than the zero-new-parameter
   slice;
3. impose the global polynomial support window;
4. impose cyclic descent from the uniformizing cover;
5. match the resulting jet in all adjacent complete-chain charts;
6. if the jet survives, study convergence/algebraization or a finite
   certificate of failure.

The local recurrence can continue indefinitely while global support fails, or
local coordinates can show an apparent obstruction removed by a chart change.
Both phenomena must be visible in the formalism.

## Useful deliverable

A theorem for one nontrivial adjacent-chart transition, including support and
residue transport, would make the later computations interpretable.  A
globally supported `F_2` jet beyond order 520 with all descent checks would be
substantial progress.  So would a parameter-independent compatibility
functional proving failure at a finite order.  Do not treat the order-530
zero-parameter slice as such a functional.

Feel free to replace the current chart language with logarithmic, Rees, or
principal-parts geometry if it reproduces the exact complete-chain operations
and makes global attachment more transparent.

[Back to the portfolio hub](state-of-the-program.md)
