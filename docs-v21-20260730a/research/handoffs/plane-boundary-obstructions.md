---
title: "Model research brief — Plane Boundary Obstructions"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 6</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 30 July 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v11 · site release <code>living-guide-public-v21-research-import-checkpoint</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }
# Program 6: Plane Boundary Obstructions

**Research state:** mathematical checkpoint 29 July 2026, including the
stored layer-seven exclusion and the exact rational `F_2` jet through order
520. Exact scope, dependencies, and direct proof-body links are stated per
input below.

**Actor guidance:** Newton-chain, chart correspondence, and descent theorems
-> online model; support regeneration and finite certificates -> local
symbolic; Hurwitz and character checks -> independent specialist CAS.

This is the complete public handoff. The linked
[working paper](../../assets/manuscripts/06-plane-boundary-obstructions-2026-07-29-v13.pdf),
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

### Coverage rule

This handoff is execution-complete for the displayed terminal systems and
explicitly incomplete for the global below-125 implication. Each numbered
input states its exact scope, the proof-signature table records dependencies
and exits, and the final column links to the proof body. The open conditional
lower-bound claim is listed only as a dependency.

### Compact glossary

- **Complete chain:** ordered sequence of approximate-root operations and
  Newton rechartings; exhaustiveness is a theorem obligation.
- **Lattice gap:** common exponent divisor imposed by the original
  polynomial lattice; it replaces an ambient cover by the relevant quotient.
- **Normal layer operator `D_r`:** universal linearization of the determinant
  equation at normal order `r`; its left kernel is represented by residues.
- **Support-aware:** preserving the finite Newton windows and the filtered
  approximate-root subgroup, not merely solving a formal equation.
- **Terminal certificate:** proof about a named finite ideal after all
  inputs and branches are fixed; it cannot certify how a global map reached
  that ideal.

### Case and dependency map

```text
hypothetical plane Keller pair
└─ normalized Newton supports
   └─ complete-chain queue (global exhaustiveness open)
      ├─ face equation ── lattice quotient Belyi cover
      ├─ normal layers ── D_r + residue adjoint
      │  ├─ fixed-chart gauge
      │  └─ adjacent-chart transition (k=4 model proved)
      ├─ stored degree-21 terminal branch
      │  └─ rechart + layers 5–7 ── excluded exactly
      └─ F_2 family
         ├─ final face / local jets ── integrable through order 520
         ├─ five-band global ansatz ── excluded
         └─ full two-sided attachment ── open, construction-sensitive
```

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

## 3. Reusable inputs, exact scope, and proof access

| # | Exact input and hypotheses | Claim · direct proof body |
| --- | --- | --- |
| 1 | Over characteristic zero, a primitive monomial Newton-face equation with the endpoint degrees and normalization stated in the paper has the displayed logarithmic derivative; after quotienting by the exponent-lattice gap, its rational function is Belyi with the stated exponent-determined passport. | [`JCG-9276A5DB`](../../claims/JCG-9276A5DB.md) · [proof](../../assets/manuscripts/06-plane-boundary-obstructions-2026-07-29-v13.pdf#page=5) |
| 2 | On one smooth boundary component and before support restrictions, the exact change `(A,B,s) -> (H,W,T)` displayed above conjugates the determinant equation to the rank-one normal form and decouples every normal order. It need not preserve sparse Newton windows. | [`JCG-D5FD24E3`](../../claims/JCG-D5FD24E3.md) · [proof](../../assets/manuscripts/06-plane-boundary-obstructions-2026-07-29-v13.pdf#page=19) |
| 3 | For the full `(8,28)` coefficient windows and the precise operator `D_r^{2,3}`, the normal-layer maps are injective for `r>=5`; for `5<=r<=11`, `dim coker D_r=r-1`. | [`JCG-79E508CE`](../../claims/JCG-79E508CE.md) · [proof](../../assets/manuscripts/06-plane-boundary-obstructions-2026-07-29-v13.pdf#page=22) |
| 4 | Every finite formal two-variable Jacobian-one jet is realized to that order by a polynomial Jacobian-one automorphism generated by linear maps and shears. This is unrestricted finite-jet realization, not realization in the filtered approximate-root subgroup. | [`JCG-D5D87491`](../../claims/JCG-D5D87491.md) · [proof](../../assets/manuscripts/06-plane-boundary-obstructions-2026-07-29-v13.pdf#page=23) |
| 5 | For the stored degree-21 lower-face equation `pq+2zp q'-3zp' q=1`, there are exactly five normalized connected dessin classes; they form one irreducible quintic Galois orbit and each has monodromy `A_21`. | [`JCG-2B32290C`](../../claims/JCG-2B32290C.md) · [proof](../../assets/manuscripts/06-plane-boundary-obstructions-2026-07-29-v13.pdf#page=24) |
| 6 | In the stored terminal face, the one-dimensional layer-four residual direction is the `k=4` complete-chain rechart `Y -> Y+lambda X^-4`, not a fixed-chart automorphism; the adjacent-chart Keller layers force the displayed common approximate root. | [`JCG-9667172F`](../../claims/JCG-9667172F.md) · [proof](../../assets/manuscripts/06-plane-boundary-obstructions-2026-07-29-v13.pdf#page=29) |
| 7 | After that canonical rechart and forced adjacent-chart condition, the complete stored degree-21 layer-five-through-seven support and matching equations have no common zero over the algebraic closure of the specified quintic field. This is one stored terminal system, not queue exhaustiveness. | [`JCG-BCEB7F45`](../../claims/JCG-BCEB7F45.md) · [exact proof](../../assets/manuscripts/06-plane-boundary-obstructions-2026-07-29-v13.pdf#page=30) |
| 8 | For the displayed normalized finite systems, the two exceptional ideals contain `1`, and the selected six-polynomial toric system has exactly the certified 296-point special fiber and no characteristic-zero solution by the recorded lifting argument. No other support system is covered. | [`JCG-8DD6ECB1`](../../claims/JCG-8DD6ECB1.md), [`JCG-8917AD05`](../../claims/JCG-8917AD05.md), [`JCG-E91A93EB`](../../claims/JCG-E91A93EB.md) · [unit-ideal proof](../../assets/manuscripts/06-plane-boundary-obstructions-2026-07-29-v13.pdf#page=27) · [toric proof](../../assets/manuscripts/06-plane-boundary-obstructions-2026-07-29-v13.pdf#page=28) |
| 9 | In the exact `C_5`-invariant `F_2` recurrence with every new kernel coordinate retained, later parameters cancel both apparent external conditions at orders 510 and 520 over `Q`; neither value is a terminal invariant. The sliced order-530 value is likewise not global. | [`JCG-2533E53C`](../../claims/JCG-2533E53C.md) · [exact calculation record](../../assets/manuscripts/07-results-and-research-register-2026-07-29-v13.pdf#page=29) |
| 10 | For the stated Puiseux recurrence, every finite jet over an immersed limit curve extends by one order; the nodal model has the displayed all-orders algebraic-series solution with constant Jacobian. Hence the proposed finite-order three-level rigidity strategy is false. | [`JCG-FD5C0C60`](../../claims/JCG-FD5C0C60.md) · [full archival proof](../../assets/proof-archives/06-plane-boundary-obstructions-2026-07-22-v8.pdf#page=36) |
| 11 | In the analyzed direct slice and graph-pullback routes from the three-dimensional marked-root construction, fixing the transverse parameter yields either a punctured surface with nonconstant-unit Jacobian or a trivial triangular affine-plane sheet; no nontrivial plane counterexample results. | [`JCG-F37D6027`](../../claims/JCG-F37D6027.md) · [full archival proof](../../assets/proof-archives/06-plane-boundary-obstructions-2026-07-22-v8.pdf#page=23) |

The public degree-125 theorem is credited to the prior literature and public
announcement. The project does not claim priority for that bound. Its exact
certificates strengthen and audit specific downstream systems while keeping
the upstream dependency explicit.

**Open dependency—not an accepted result:** the project's implication from
the two normalized alternatives to the below-125 lower bound remains `open`
pending replay and audit of the upstream Newton reduction
([`JCG-9D0BE662`](../../claims/JCG-9D0BE662.md)).

### Proof-signature index

| Inputs | Proof signature / reusable output | Boundary exits |
| --- | --- | --- |
| 1 | Logarithmically differentiate the face ratio; the Jacobian ODE leaves exactly three branch fibers. Divide by the exponent-lattice gap, compute the quotient passport, and use its unique long cycle plus coprime cycle lengths to force transitivity. **Output:** quotient Belyi map and passport, not the ambient overcount. | Complete-chain theory must prove that the stated lattice and face actually occur. |
| 2–4 | Pass to relative variations, then use `W=A_0B_0/(AB)`, `T=sW^(1/S)`, and the logarithmic coordinate `H` to conjugate the full determinant equation to a rank-one connection with decoupled orders. Exact support matrices prove injectivity and cokernel `r-1`; ordinary finite symplectic jets are realized by polynomial shears. **Output:** universal layer complex and unrestricted finite-jet realization. | The triangular conjugation need not preserve Newton support or the approximate-root subgroup. |
| 5 | Solve the degree-21 face equation exactly; the five normalized solutions form one quintic Galois orbit. Passport permutations and an explicit three-cycle/long-cycle argument identify monodromy `A_21`. **Output:** a pinned lower-face cover package. | This is one stored face, not queue exhaustiveness. |
| 6–7 | Identify the layer-four residual vector with the complete-chain operation `Y↦Y+lambda X^-4`; in adjacent coordinates the first Jacobian layers force `L=0`, `F_5=0`, and `P_2=CR^2`, `Q_3=GR^3`. Split on the remaining leading denominator and close both branches with exact Nullstellensatz and weighted-chart certificates through layer seven. **Output:** no gluing for the stored terminal model. | Global use still requires a proof that every candidate reaches this branch. |
| 8 | Reconstruct every terminal equation from principal-part residues, reduce at a good prime over 2053, enumerate the 296-point toric special fiber, and use proper toric compactification plus étale lifting to characteristic zero. **Output:** unit-ideal and toric certificates with residue provenance. | Exact only for the displayed finite systems and their recorded support hypotheses. |
| 9 | Build the `C_5`-invariant Kuranishi recurrence through order 520 while retaining every new kernel coordinate; solve later parameters that cancel the apparent order-510 and order-520 functionals. **Output:** a long exact flexible jet and two explicit false obstructions. | The zero-new-parameter value at order 530 is not invariant. |
| 10 | Derive the Puiseux coefficient recurrence. For an immersed limit curve the new-order operator is surjective; the nodal example integrates to an explicit algebraic series with constant Jacobian. **Output:** a counterexample to all finite-order local-rigidity strategies of this type. | Global finite support, termination, topology, and chart matching remain possible obstructions. |
| 11 | Factor the three-dimensional Jacobian cancellation into a pole from incidence, two source-coordinate poles, and the transverse `x^3` zero. Fixing the transverse parameter produces either a punctured surface with nonconstant unit Jacobian or a trivial triangular affine-plane sheet. **Output:** a precise slice/graph no-go mechanism. | Applies to the analyzed direct descent routes, not every conceivable relation between dimensions two and three. |

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

The new Lane 9 toolkit adds exact Lie-bracket, wall-closure, and
residual-kernel utilities; all six internal tests pass. Its upper-face atlas
uses transcribed counts rather than the actual matrices, the lower operation
subgroup is incomplete, the archived `C9` replay is unavailable, and the
actual `F_2` blocks are absent, so the included `F_2` example is synthetic.
Its averaging lemma is strategically decisive: plain cyclic descent cannot
by itself obstruct the stable-support linear system. F4 therefore needs the
real blocks plus global support, nonlinear coupling, or a stronger descent
condition.

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
- **Synthetic `F_2` blocks certify the actual attachment.** They validate a
  workflow only; recover the real blocks and retain the cyclic-averaging
  warning.

## 6. Tasks

Each item is a task capsule. T1 must maintain a stage manifest with every
branch condition before specialization; T2 must distinguish gauge from
rechart operations. If T3 finds a finite global attachment, stop all
obstruction language and return the candidate pair, support proof, and exact
Jacobian certificate immediately.

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

Treat the Lane 9 bundle as a toolkit, not another terminal receipt. Exact
brackets do not acquire a curvature or global-obstruction interpretation
without the missing comparison theorem and actual data blocks.

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
- Do not infer global geometry from the exact Lane 9 Lie brackets alone.

[Back to the Program 6 overview](../programs/plane-boundary-obstructions.md)
