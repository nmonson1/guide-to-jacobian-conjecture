---
title: "Model research brief — Plane Boundary Obstructions"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 6</p>
# Program 6: Plane Boundary Obstructions

**Research state:** 29 July 2026, Pacific time, including the stored
layer-seven exclusion and the exact rational `F_2` jet through order 520.

**Actor guidance:** Newton-chain, chart correspondence, and descent theorems
-> online model; support regeneration and finite certificates -> local
symbolic; Hurwitz and character checks -> independent specialist CAS.

This is the complete public handoff. The linked
[working paper](../../assets/manuscripts/06-plane-boundary-obstructions-2026-07-22-v11.pdf),
[stable claims](../../results/all-claims.md), and
[Program 6 technical materials](../../evidence/materials.md#6-plane-boundary-obstructions)
provide proof and replay access without private records.

## 1. Setup and notation

The plane Jacobian conjecture remains open. Program 6 studies what a
hypothetical noninvertible plane Keller pair `(P,Q)` must look like near the
boundary of a compactification. A Newton face produces a one-variable
Jacobian differential equation; after normalization, the corresponding
rational map is Belyi and its ramification passport is determined by the face
exponents.

The **complete-chain** method applies successive approximate-root operations
and weighted rechartings. Fractional uniformizing covers may appear during a
local calculation, but the exponent lattice can force a smaller quotient.
For the first degree-125 family, the ambient degree-30 passport has eleven
classes while the lattice gap selects one degree-six quotient. The first five
quotient problems have degrees `6,10,9,9,16` and class counts `1,1,1,2,2`.

Normal deformations away from a boundary face are governed order by order by
the linear operator

```
D_r(a,b) = (alpha-r)a dB_0 - beta B_0 da
           + alpha A_0 db + (r-beta)b dA_0.
```

Its filtered residue adjoint identifies matrix left kernels with explicit
compatibility functionals. A formal change of variables

```
W = A_0 B_0 / (A B),
T = s W^(1/(alpha+beta)),
H = (alpha log(B/B_0) - beta log(A/A_0))/(alpha+beta)
```

linearizes the unrestricted determinant equation on one smooth boundary
component and decouples normal orders before support restrictions. The
remaining difficulty is not unrestricted formal integration. It is
preserving sparse Newton windows, matching adjacent charts, and realizing
the jet inside the valuation-filtered approximate-root subgroup.

The **stored degree-21 terminal model** is a particular full-support
specialization over an explicit quintic field. Its missing layer-four
operation is the `k=4` complete-chain transition to an adjacent chart. In
that chart the Jacobian equations force a common approximate root, and the
complete layer-five-through-seven system has no solution. This is an exact
theorem about the stored system.

The global below-125 interpretation has an additional upstream dependency:
one must prove that every hypothetical counterexample below the bound is
routed, through all Newton faces, saturations, normalizations, and chart
choices, to one of the displayed terminal systems. Terminal unit ideals do
not prove this exhaustiveness by themselves.

A second branch, the `F_2` complete-chain family, is locally flexible. An
exact `C_5`-invariant Kuranishi calculation constructs a supported jet
through order 520. Later kernel parameters cancel the apparent obstruction
coordinates at orders 510 and 520. A nonzero coordinate at order 530 is
known only after setting all new free coordinates to zero; it is not a
global obstruction.

## 2. Goal and payoff

The main goal is a claim with three independently visible parts:

1. the row-level or terminal finite computation is exact;
2. the queue of rows/faces/charts is exhaustive;
3. descent and gluing from those rows to a global plane Keller map are valid.

Only when all three are certified can a terminal calculation support a
stand-alone global degree theorem. The current project has exceptionally
strong results for displayed terminal systems and a substantial raw-support
reconstruction, but the upstream exhaustiveness and general
chart-correspondence theorem remain the critical gates.

The immediate conceptual goal is to replace the false fixed-chart
surjectivity idea with a general theorem: residual kernel directions may be
complete-chain transitions to adjacent Newton charts. The theorem should
identify when this happens, prove compatibility of the transformed support,
and show how complete chains connect to terminal systems.

The `F_2` goal is deliberately two-sided. Determine whether the locally
consistent terminal model attaches to a finite global polynomial Keller pair.
A proof of impossibility needs the full two-sided band-convolution and chart
gluing problem; a successful attachment would be a candidate plane
counterexample and must be escalated rather than treated as a failed
obstruction search.

## 3. What is proved (statements only; proofs at the locators)

| # | Statement | Where |
| --- | --- | --- |
| 1 | A primitive monomial Newton-face Jacobian equation gives an exact logarithmic derivative and, under the stated hypotheses, a Belyi map with passport determined by the exponents. | [`JCG-9276A5DB`](../../claims/JCG-9276A5DB.md); paper face-to-passport theorem |
| 2 | The exact normal-coordinate change linearizes every normal order before support restrictions. | [`JCG-D5FD24E3`](../../claims/JCG-D5FD24E3.md); exact-normal appendix |
| 3 | For the full `(8,28)` windows, the terminal layer maps are injective from order five onward; through order eleven the cokernel has dimension `r-1`. | [`JCG-79E508CE`](../../claims/JCG-79E508CE.md) |
| 4 | Every finite formal Jacobian-one jet in two variables is realizable by a polynomial Jacobian-one automorphism built from linear maps and shears. This is unrestricted local realization, not approximate-root realization. | [`JCG-D5D87491`](../../claims/JCG-D5D87491.md) |
| 5 | The degree-21 lower-face equation has exactly five normalized solutions in one quintic Galois orbit, and the five dessins have monodromy `A_21`. | [`JCG-2B32290C`](../../claims/JCG-2B32290C.md) |
| 6 | The missing layer-four operation in the stored terminal face is the `k=4` Newton-chart transition; the adjacent chart forces a common approximate root. | [`JCG-9667172F`](../../claims/JCG-9667172F.md) |
| 7 | After that transition, the stored degree-21 terminal layer-five-through-seven system has no solution over the algebraic closure of its quintic coefficient field. | [`JCG-BCEB7F45`](../../claims/JCG-BCEB7F45.md) |
| 8 | The selected full-support obstruction equations have exact characteristic-zero unit-ideal and 296-point toric certificates for the displayed systems. | [`JCG-8DD6ECB1`](../../claims/JCG-8DD6ECB1.md), [`JCG-8917AD05`](../../claims/JCG-8917AD05.md), [`JCG-E91A93EB`](../../claims/JCG-E91A93EB.md) |
| 9 | The apparent `F_2` external conditions at orders 510 and 520 are slice-dependent and can both be cancelled exactly over `Q`; neither is a terminal invariant. | [`JCG-2533E53C`](../../claims/JCG-2533E53C.md) |
| 10 | The proposed finite-order three-level `2:3` Puiseux rigidity lemma is false; the recurrence extends at every finite order and the nodal model has an all-orders algebraic-series solution. | [`JCG-FD5C0C60`](../../claims/JCG-FD5C0C60.md) |
| 11 | Direct slicing or graph pullback of the three-dimensional cubic mechanism does not yield a nontrivial plane counterexample in the analyzed models. | [`JCG-F37D6027`](../../claims/JCG-F37D6027.md) |
| 12 | The current local conditional lower-bound claim remains subject to replaying and auditing the upstream Newton reduction. | [`JCG-9D0BE662`](../../claims/JCG-9D0BE662.md) |

The public degree-125 theorem is credited to the prior literature and public
announcement. The project does not claim priority for that bound. Its exact
certificates strengthen and audit specific downstream systems while keeping
the upstream dependency explicit.

## 4. The live frontier

**(F1) Upstream exhaustiveness audit.** Starting from the two normalized
Newton supports, regenerate every lower face, saturation, normalization,
deficiency layer, chart transition, and branch split. Compare the resulting
systems and hashes with the archived terminal inputs. A raw-support
reconstruction already regenerates the degree-21 face and fifteen equations;
the remaining audit must certify that no branch was lost before or between
those stages and must reconcile the argument with the published reduction.

**(F2) General chart-correspondence/descent theorem.** The `k=4` transition
solves one stored residual kernel. Formulate a theorem explaining when a
kernel of `D_r` is a fixed-chart gauge direction, when it is a transition to
an adjacent complete-chain chart, and how transformed supports and residue
conditions correspond. This theorem must replace fixed-chart surjectivity,
not rename it.

**(F3) Support-aware exact normal coordinates.** In `(H,W,T)` coordinates,
unrestricted normal orders decouple. The fifteen audited residue equations
must be conjugated through that change while tracking the triangular support
map. Determine whether solutions lie in the valuation-filtered
approximate-root subgroup and whether chart overlaps introduce new
conditions.

**(F4) Global `F_2` attachment.** The local recurrence is integrable and the
jet survives through order 520. The next problem is not to test order 530 on
the zero-new-parameter slice. It is to solve the two-sided band-convolution
system with all fresh kernel parameters and affine-linear terms, then impose
global polynomial support and cyclic descent across charts.

**(F5) Independent Hurwitz/CAS reproduction.** Reimplement the character
counts, explicit Belyi checks, and selected terminal ranks in Sage, GAP, or
Magma. This is a release gate separate from F1; it need not duplicate every
large matrix.

Dependencies: F1 certifies the queue, F2 certifies transitions/descent, and
the existing terminal certificates settle the finite row systems. F3 may
simplify the Kuranishi stage but must preserve the admissible support. F4 is
an independent possible-construction branch.

## 5. Graveyard (causes of death — read before proposing routes)

- **Fixed-chart surjectivity.** Layer four supplies a counterexample: the
  residual direction is not a fixed-chart algebraic operation but becomes
  the `k=4` adjacent-chart transition. The correct mechanism is chart
  correspondence.
- **Finite-order Puiseux rigidity.** The proposed three-level lemma is false
  for every immersed limit parametrization, and the nodal model solves the
  recurrence to all orders. A valid obstruction must use finite support,
  global topology, or gluing—not another finite truncation of the same
  recurrence.
- **Orders 510 and 520 are terminal obstructions.** Later kernel parameters
  cancel both exactly. The order-530 value on a zero-new-free-coordinate
  slice has the same logical weakness until all fresh directions are
  considered.
- **Exact normal linearization preserves Newton support.** The formal change
  is triangular and invertible on finite jets, but it does not automatically
  preserve sparse windows or the approximate-root subgroup. That mismatch
  is the frontier.
- **Terminal unit ideal proves upstream exhaustiveness.** A certificate
  proves the ideal it receives. It cannot prove that every global candidate
  reaches that ideal.
- **Finite-field emptiness is characteristic-zero emptiness.** The current
  strongest stored certificates include exact lifting arguments; older
  modular checks remain only cross-checks.
- **Conductor forces polynomial termination.** Conductor information can
  control lattice saturation but cannot make an arbitrary formal solution
  terminate.

## 6. Tasks

**P6-T1 — Regenerate and audit the complete lower-face pipeline.**

Actor: `local_symbolic` plus mathematical audit. Status: ready.

*Inputs:* the public raw-support reconstruction, normalized Newton polygons,
lower-face layer implementation, archived terminal systems, and published
reduction statement.

*Payoff:* certifies the exhaustiveness leg required to interpret terminal
certificates globally.

*Attack:* make a stage manifest; regenerate faces and saturated ideals from
raw supports; record branch conditions before specialization; compare
canonicalized equations and hashes at every boundary.

*Done when:* all faces, normalizations, saturations, transitions, and branches
regenerate, every terminal input has a provenance edge, and no discarded
branch lacks a theorem or exact certificate.

**P6-T2 — Prove a weighted-boundary chart-correspondence theorem.**

Actor: `online_model`. Status: ready.

*Inputs:* the working paper, universal layer operator, complete-chain rules,
and explicit `k=4` transition.

*Payoff:* supplies the descent/gluing leg and prevents future fixed-chart
misclassifications.

*Done when:* a theorem classifies residual kernel directions into gauge and
rechart operations, proves support transformation and overlap compatibility,
and connects complete chains to the terminal systems used by T1.

**P6-T3 — Solve the full `F_2` attachment problem.**

Actor: `online_model` plus `local_symbolic`. Status: ready.

*Inputs:* the exact order-520 certificate and support windows, the
all-`m` final-face formulas, cyclic-descent constraints, and all fresh kernel
directions.

*Payoff:* either kills a long-lived local model for a genuinely global
reason or produces a candidate plane Keller pair.

*Done when:* the two-sided band system is solved with all free coordinates,
and global support/chart attachment is proved possible or impossible.

## 7. Evidence and replay index

The technical release separates the universal normal-form checks, terminal
boundary programs, degree-21 quotient faces, raw-support reconstruction,
unit-ideal certificates, residue provenance, the compact 296-point
certificate, the stored layer-seven suite, and the exact `F_2` order-520
certificate.

The strongest unconditional finite statements are exact for their displayed
systems: stored terminal ideals contain `1`; the fifteen equations have the
claimed residue provenance; the selected toric system has no
characteristic-zero solution; and the stored layer-seven model does not
glue. The exact `F_2` verifier reconstructs every determinant layer through
520 and confirms cancellation of the two apparent external conditions.

The boundary is equally important: none of those finite replays, alone,
proves the upstream literature reduction or global attachment/descent. Use
the [stored terminal package](../../collections/stored-degree-twenty-one-terminal-no-gluing.md),
[filtered finite-jet frontier](../../collections/filtered-finite-jet-realization.md),
and [`F_2` attachment problem](../../collections/f2-global-attachment-problem.md)
as the claim-level entry points.

## 8. Do not do

- Do not revive fixed-chart surjectivity.
- Do not call orders 510, 520, or the sliced order 530 value a terminal
  obstruction.
- Do not infer polynomial termination from a formal or finite-jet solution.
- Do not treat a terminal certificate as an audit of the upstream case tree.
- Do not assume exact normal coordinates preserve sparse Newton support.
- Do not rerun the false finite-order Puiseux rigidity argument.
- Do not merge row-level computation, queue exhaustiveness, and global
  descent into one unlabeled “verified” status.
- Do not treat a successful global `F_2` attachment as merely a failure of
  the obstruction program; it would be a candidate counterexample.

[Back to the Program 6 overview](../programs/plane-boundary-obstructions.md)
