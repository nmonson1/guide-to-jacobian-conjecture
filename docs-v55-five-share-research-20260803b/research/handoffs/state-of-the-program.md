---
title: "Model research brief — Current Jacobian research portfolio"
description: "A self-contained mathematical handoff for a research model."
---

# Nine research directions around the Jacobian conjecture

<p class="claim-tag">Portfolio hub · Updated 3 August 2026</p>

Here a **Keller map** is a polynomial self-map of affine space whose
Jacobian determinant is a nonzero constant. The classical Jacobian
conjecture asks whether every Keller map is invertible. An explicit complex
Keller map in dimension three with Jacobian determinant \(-2\) and three
distinct source points having the same image is now known in this project;
adjoining identity coordinates gives counterexamples in every dimension at
least three. The plane case remains open.

The [baseline counterexample](intrinsic-degree-valuative-budgets.md#baseline-counterexample)
is written out with its three rational colliding points and an exact verifier.
The rest of this portfolio starts from that fixed map or studies the still-open
plane problem.

These lanes are overlapping views of one body of mathematics. Each page
defines its objects, separates established inputs from examples and open
work, and directly links the proof source or executable object used by each
substantial result. **Ready** means that at least one advertised task can
begin from the formulas or files on the page. An
**interface-ready** task is a self-contained abstract theorem whose later
geometric application still lacks declared inputs. Non-ready follow-ups
remain visible so that missing data are not mistaken for open calculations.

The lanes serve two connected goals. Lanes 1--7 study the explicit
higher-dimensional counterexample, its geometry and deformations, related
low-degree reductions, and its homogeneous descendants. Lanes 8--9 address
the surviving plane problem through Newton-root closure and global boundary
attachment. Every task advertised as ready starts from its supplied data;
later actual-\(F_2\) work in Lane 9 explicitly depends on the relation packet
being constructed in Lane 8.

The lane numbers are labels, not a sequence to be completed in order. The
only declared dependency between lane tasks is the actual-\(F_2\) passage
from Lane 8 to Lane 9; the other cross-lane links below are invitations.

The listed problems are suggested frontiers, not restrictions. A different
argument or connection is welcome when it states its hypotheses precisely,
uses the known mathematics rather than rederiving it, and returns a reusable
theorem, construction, or exact computation.

## Choose a lane

| Lane | Why it matters | Strongest supplied input | Useful next work | Readiness |
| --- | --- | --- | --- | --- |
| [1. Cubic normalization defects](cubic-flatness-normalization-defects.md) | A cubic Keller normalization can fail to be flat only on one exact finite defect carrier. | Ext/resolvent/Čech equivalence, a zero-defect benchmark, a non-MCM boundary model, and an explicit type-IV test object. | Classify the closed-threefold carrier or exclude a Keller-compatible opening of the type-IV cone. | **Ready:** local theorem and fixed-test-object problems. |
| [2. Projective PRS boundary](boundary-completeness-torelli-at-infinity.md) | The fixed quintic boundary is globally normalized; the frontier is its all-rank merge law and marked Torelli data. | Four-chart normalization, conductor and overlaps, plus a convention-complete adjacent-monomial theorem. | Fill the actual PRS specialization contract and extract a marked-boundary invariant. | **Ready:** exact packets and fail-closed contract supplied. |
| [3. Formal effectivity and complexity](bounded-degree-deformation-modulus-onset.md) | Compatible finite-order equivalences need not algebraize; the intrinsic growth rate is open. | Exact framed \(M-2\) law, stable non-effectivity theorem, unrestricted lower bound, and order-six reconstruction. | Find an unframed invariant improving the complexity bound. | **Ready:** intrinsic-recovery task; chain comparison waits for native data. |
| [4. Quartic endgame](quartic-endgame.md) | One exact case-tree edge can be closed without pretending the whole quartic reduction is complete. | Structural proof strategy for the zero cubic normal branch and a separate exact marked-chart obstruction. | Prove or refute the zero-normal edge theorem. | **Ready:** one edge; full \(Q_4\)-\(F_4\) reconstruction is not ready. |
| [5. Filtered image algebra under tame words](intrinsic-degree-valuative-budgets.md) | Explicit low-weight tame words are the first cases not covered by weight or collision-pole separation. | Exact image algebra, relative-derivation covariance, elementary-shear results, and uniform high-degree word theorems. | Compute the degree-six filtered algebra for a specified mixed-return word and its finite family. | **Ready:** formulas and exact certificate methods supplied. |
| [6. Homogeneous compression](homogeneous-realization-compression.md) | A presentation-stable obstruction is needed before nineteen-variable minimality can even be formulated correctly. | Fixed suspension, restricted obstruction calculations, and an exact filtered-operation interface. | Prove and package the chain-level presentation-groupoid criterion. | **Interface-ready:** abstract theorem; exhaustive geometric application is blocked. |
| [7. Five-dimensional collisions](five-dimensional-collision-geometry.md) | The collision equations reduce to a \(10\times5\) determinantal carrier whose grade and corank loci remain open. | A self-contained exact \(d,M,A,CA,H,C,Q,R\) bundle, its verifier, and one smooth curve germ. | Prove grade six and test the corank-two locus while retaining the Plücker open. | **Ready:** exact determinantal and marking inputs supplied. |
| [8. Newton roots and degree 125](plane-newton-queue-terminal-certificates.md) | The two roots below \(125\) are closed; inherited coefficient relations for the first degree-\(125\) family are the next geometric input. | Direct closure of both \((8,28)\) roots, the explicit \(F_2\) terminal face, and an exact coefficient-transport audit. | Export the complete inherited relation packet for the denominator-five shear. | **Ready:** finite coefficient transport; support uniqueness follows after this packet and a stratification contract. |
| [9. Three-chart attachment](plane-chart-correspondence-global-attachment.md) | Slice conditions become geometric only after fresh parameters and chart transport are included. | Exact support windows, cancellations through order \(530\) in a stated slice, recurrence contract, and ambient wall groupoid. | Prove the obstruction-transport interface; later insert actual \(F_2\) blocks. | **Interface-ready:** the actual \(F_2\) integration is blocked on relation and chart data. |

## Connections worth testing

- Lanes 1 and 5: can an intrinsic filtration constrain the rank-one
  reflexive resolvent module?
- Lanes 2 and 9: can the same explicit groupoid formalism control projective
  PRS overlaps and normal-boundary overlaps?
- Lanes 3 and 6: does formal escaping complexity survive homogeneous
  stabilization through an explicit chain map?
- Lanes 4 and 7: do the quartic marked charts and collision carrier share a
  determinantal or Eagon--Northcott mechanism?
- Lanes 8 and 9: Lane 8 should supply actual normal windows; Lane 9 should
  prove that their local conditions transport across the adjacent chart.

Except for the explicit Lane 8-to-9 actual-\(F_2\) handoff above, these are
invitations rather than dependencies. Any stronger connection is useful if
it preserves the exact scope and produces the deliverable it claims.

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the research overview](../index.md)
