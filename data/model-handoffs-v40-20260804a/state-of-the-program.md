# Nine research directions around the Jacobian conjecture

Updated 4 August 2026

Here a **Keller map** is a polynomial self-map of affine space whose
Jacobian determinant is a nonzero constant. The classical Jacobian
conjecture asks whether every Keller map is invertible. An explicit complex
Keller map in dimension three with Jacobian determinant \(-2\) and three
distinct source points having the same image is now known in this project;
adjoining identity coordinates gives counterexamples in every dimension at
least three. The plane case remains open.

The displayed three-dimensional example is the Alpöge--Fable map. Its
Jacobian and three collision identities are exact symbolic identities checked
by the [public verifier](lane-5-source-packet.md#source-9ec82063f46b1a95);
the [Lane 5 statement](intrinsic-degree-valuative-budgets.md#baseline-counterexample)
writes out the map and colliding points. The project treats those equations
and their direct check as mathematical input; it makes no literature-priority
claim for the example.

For provenance, Alpöge's [primary announcement](https://x.com/__alpoge__/status/2079028340955197566)
displays the map and thanks “akhil” for asking about it and “fable” for working
on it; Joe Atkins--Turkish's [public source](https://gist.github.com/Spacerat/08b4a43f6b6ca57178efabc220170ce8)
supplies the eleven-variable degree-at-most-three descendant used in Lane 6.
Shaska's [graded Keller-map preprint](https://arxiv.org/abs/2607.20210)
provides a stable scholarly discussion of the announced map and its grading.
Those links record credit and context; the exact verifier above is the evidence
for the determinant and collision identities. The portfolio also includes
independent low-degree, boundary, deformation, and minimal-dimension problems
whose relevance is methodological rather than descent from this fixed map.

These lanes are overlapping views of one body of mathematics. Each page
defines its objects, separates established inputs from examples and open
work, and directly links the proof source or executable object used by each
substantial result. Task cards are compiled from the retained mathematical
graph. **Ready now** means that every input needed to begin the stated proof,
calculation, or exploration is public. **Blocked** means that the card names
the exact missing mathematical input and, when one exists in the present
graph, the task that should supply it.
Effort labels distinguish bounded calculations from sustained or open-ended
research; they do not encode confidence in the mathematics.

The lanes serve several related goals. Lanes 1, 5, and 6 use the explicit
higher-dimensional counterexample or one of its descendants. Lanes 2--4 and
7 are independent boundary, deformation, low-degree, or minimal-dimension
test beds for Keller-map methods. Lanes 8--9 address the surviving plane
problem through Newton-root closure and global boundary attachment. Every
task advertised as ready starts from its supplied data;
later actual-\(F_2\) work in Lane 9 can use Lane 8's completed linear descent
packet but still depends on its nonlinear actual-support and adjacent-chart
data.

The object genealogy has three main branches. The Alpöge--Fable map is a
zero-defect benchmark for Lane 1 and the filtered image-algebra test object in
Lane 5; Lane 1's unresolved defect problem concerns other generic-degree-three
Keller maps. Lane 3 is mixed: its formal-effectivity thread studies the
normalized degree-seven Alpöge--Fable map, while its finite-level complexity
thread is a separate deformation-algebra question. A public eleven-variable
polynomial-degree-three descendant of the fixed map supplies the
nineteen-variable homogeneous suspension in Lane 6. Lane 7 instead asks the
independent minimization question: dimension five is the first possible
dimension for a cubic-homogeneous counterexample. Lanes 2 and 4 study separate
projective-boundary and quartic-reduction objects, while Lanes 8--9 form the
plane Newton-boundary branch. Task cards also record several within-lane
dependencies and the shared Lane 6/9 certificate infrastructure.

The lane numbers are labels, not a sequence to be completed in order. The
actual-\(F_2\) data handoff from Lane 8 to Lane 9 is the only declared
inter-lane data supply; the other cross-lane links below are invitations or
shared abstract interfaces.

The listed problems are suggested frontiers, not restrictions. A different
argument or connection is welcome when it states its hypotheses precisely,
uses the known mathematics rather than rederiving it, and returns a reusable
theorem, construction, or exact computation.

The graph-compiled [current research-task roadmap](../tasks/index.md) is a
compact index of the same tasks, readiness, dependencies, and blockers. Each
linked lane card supplies the complete public inputs, completion criterion,
and mathematical limits.

## Choose a lane

| Lane | Why it matters | Strongest supplied input | Useful next work | Readiness |
| --- | --- | --- | --- | --- |
| [1. Cubic normalization defects](cubic-flatness-normalization-defects.md) | A cubic Keller normalization can fail to be flat only on one exact finite defect carrier. | Ext/resolvent/Čech equivalence, a zero-defect benchmark, a non-MCM boundary model, and an explicit type-IV test object. | Find a genuinely Keller-specific MCM criterion or an actual Keller realization; separately test the fixed type-IV gate. | **Ready now — proof/exploration.** |
| [2. Projective PRS boundary](boundary-completeness-torelli-at-infinity.md) | The fixed quintic boundary is globally normalized; the frontier is its all-rank merge law and nontrivial marked families. | Four-chart normalization, conductor and overlaps, plus a convention-complete adjacent-monomial theorem. | Construct a non-isotrivial PRS-boundary family with fixed combinatorial type; separately recover the missing primitive pivot and transfer packet. | **Ready now — structural family construction;** actual-PRS specialization and the later Torelli test are blocked. |
| [3. Formal effectivity and complexity](bounded-degree-deformation-modulus-onset.md) | Compatible finite-order equivalences need not algebraize; the intrinsic growth rate is open. | Exact framed \(M-2\) law, stable non-effectivity theorem, unrestricted lower bound, order-six reconstruction, and \(\beta_2=354\) over \(\mathbf Q\). | Find a non-tautological unframed invariant and first build the complete rational-Betti queue contract. | **Ready now — proof and bounded queue construction;** \(\beta_3,\ldots,\beta_9\) are blocked on that coverage proof. |
| [4. Quartic endgame](quartic-endgame.md) | One exact case-tree edge can be closed without pretending the whole quartic reduction is complete. | Structural proof strategy for the zero cubic normal branch and a separate exact marked-chart obstruction. | Prove or refute the zero-normal edge theorem. | **Ready now — proof;** full \(Q_4\)-\(F_4\) recovery is blocked on named historical data. |
| [5. Filtered image algebra under tame words](intrinsic-degree-valuative-budgets.md) | The first low-weight mixed-return family is now exactly closed; the broader resonant transformation law is open. | Exact image algebra, covariance, elementary and high-degree word theorems, and the complete \(25\)-case mixed-return table. | Explain all 25 cases structurally or prove a theorem for a genuinely larger resonant word class. | **Ready now — exploration, proof, and bounded computation.** |
| [6. Homogeneous compression](homogeneous-realization-compression.md) | A presentation-stable obstruction is needed before nineteen-variable minimality can be formulated correctly. | Fixed suspension, restricted obstruction calculations, exact row-base adapters, and a filtered-operation interface. | Classify the full row-base fibres; separately build the shared fail-closed certificate infrastructure. | **Ready now — geometric and reusable-interface work;** the ambient benchmark and exhaustive presentation application are blocked. |
| [7. Five-dimensional collisions](five-dimensional-collision-geometry.md) | The collision equations reduce to a \(10\times5\) determinantal carrier whose grade, marking open, and corank locus are separate questions. | A self-contained exact matrix bundle plus a six-minor grade witness, fifty-minor corank filter, and five four-equation collinearity charts. | Try the smaller exact-Q tests first; retain full chart dimensions and exhaustive decomposition as fallback or optional structural work. | **Ready now — sustained proof/computation.** |
| [8. Newton roots and degree 125](plane-newton-queue-terminal-certificates.md) | The two roots below \(125\) are closed; the nonlinear actual-support locus for the first degree-\(125\) family is the next geometric input. | Direct closure of both \((8,28)\) roots and an exact 202-block parametrization replacing \(14{,}800\) inherited linear equations by \(1{,}973\) coordinates. | Define the exhaustive support and equivalence contract first; then build its nonlinear packet and actual locus. | **Ready now — support-contract proof;** nonlinear equations and the full locus are blocked on it. |
| [9. Three-chart attachment](plane-chart-correspondence-global-attachment.md) | Slice conditions become geometric only after fresh parameters and chart transport are included. | Exact ambient coefficient windows, cancellations through order \(530\) in a stated slice, recurrence contract, and ambient wall groupoid. | Build the shared fail-closed certificate infrastructure; then certify the ambient atlas and attach Lane 8's actual blocks. | **Ready now — certificate-infrastructure work;** the ambient certificate and actual \(F_2\) application are blocked. |

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

---
[Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
