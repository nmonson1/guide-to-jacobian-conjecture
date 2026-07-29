---
title: "Model research brief — Cubic Marked-Root Incidence Geometry"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 1</p>
# Program 1: Cubic Marked-Root Incidence Geometry

**Research state:** 29 July 2026, Pacific time.

**Actor guidance:** structural algebraic geometry -> online model; exact finite
lattice or matrix work -> local symbolic system after the geometric inputs
exist.

This page is the complete public handoff. A model can begin from this URL
alone. The linked [working paper](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-22-v11.pdf),
[stable claim pages](../../results/all-claims.md), and
[technical materials](../../evidence/materials.md#1-cubic-marked-root-incidence-geometry)
give proof and replay access without private conversations or internal paths.

## 1. Setup and notation

Work over the complex numbers. A **Keller map** is a polynomial map
`F: A^3 -> A^3` with nonzero constant Jacobian determinant. The known
counterexample has generic degree three: over the function field of the
target, a generic fiber consists of three points, and its Galois closure has
group `S_3`.

The main explicit framework is the **cubic frame**. It is built from a marked
root `t`, a slope variable `r`, and a parameter `c`. For a cubic potential
`H(T,c)`, set

```
b = r - H_T(t,c),               2a = H(t,c) + t b.
```

The Jacobian of `(t,r,c) -> (a,b,c)` is `r/2`. Composing with the rational
source coordinates

```
t = y + 1/x,     r = 2/x,       c = w(x,y) - x^3 z
```

produces determinant `-2` whenever pole cancellation makes the formulas
polynomial. For the normalized cubic family one writes

```
H(T,c) = T^3 + 3 A(c) T + B(c).
```

The discriminant surface in the target is the image of the double-root
locus. Its normalization has coordinates `(c,t)`, and the conductor and
deleted boundary remember where sheets disappear. The **finite cubic
normalization** is the normalization of the target in the source function
field. Its trace-zero module has rank two and is reflexive; it is locally free
away from finitely many target points. Flatness is precisely the unresolved
global issue.

The boundary vocabulary is important. Along a target prime divisor, a cubic
normalization can have three completed sheets with one deleted (`U1`), three
unramified sheets with two deleted (`U2`), or a ramified `2+1` fiber with the
ramified point deleted (`B`). A deleted three-cycle is excluded in the Keller
setting under analysis. This is a codimension-one classification, not a
classification of the isolated nonflat points.

The **quadratic resolvent** packages the sign representation of the `S_3`
cover. A cubic defect gives three-torsion data on that resolvent. The current
route asks whether the relevant rank-one reflexive eigensheaf is maximal
Cohen--Macaulay and whether its conormal root can be pushed down globally.
Local models and isolated-singularity restrictions are known; the general
Keller-specific pushdown is not.

## 2. Goal and payoff

The immediate goal is to eliminate the finite nonflat defect of a generic
degree-three Keller normalization. Equivalently, prove the finite cubic
normalization is flat under the Keller hypotheses, then identify it with the
universal marked-root cover once boundary completeness is supplied.

Flatness would connect three parts of the project that are currently only
conditional: the intrinsic finite-cover description, classification by cubic
frames, and the low-degree program. It would turn “the known counterexample
comes from a marked-root construction” into a theorem that every
generic-degree-three Keller map does, subject to the separately stated
boundary-completeness step.

The nearer-term payoff is still useful if full flatness remains out of reach.
A correct conormal-root or MCM theorem can shrink the possible defect support,
identify the exact missing divisor data, and produce a finite lattice problem
for symbolic computation. Negative results should be stated as sharp
hypotheses: a theorem about a smooth axis, an isolated resolvent singularity,
or an algebraically homogeneous defect must not silently become a global
flatness theorem.

## 3. What is proved (statements only; proofs at the locators)

| # | Statement | Where |
| --- | --- | --- |
| 1 | The root-slope construction has Jacobian `-2` after the displayed substitution whenever pole cancellation makes it polynomial, and its generic degree is the root degree of the potential. | [`JCG-0106262F`](../../claims/JCG-0106262F.md); paper root-slope appendix |
| 2 | In the normalized `A,B` family, polynomial left-right equivalence is classified by an affine change of `c`, scalar equality of `A`, congruence of `B` modulo `A`, and preservation of the marked root; repeated roots are allowed. | [`JCG-221985FF`](../../claims/JCG-221985FF.md); paper equivalence theorem |
| 3 | Inside the two-block multiplication-incidence construction, stable affineness occurs only for the unordered pair `{1,2}`. | [`JCG-517DA8F4`](../../claims/JCG-517DA8F4.md); paper stable-uniqueness theorem |
| 4 | Coprime normalized cubic frames have irreducible inverse cubic with nonsquare discriminant, hence generic monodromy `S_3`; their target deck group is trivial. | [`JCG-504733CF`](../../claims/JCG-504733CF.md), [`JCG-5B09E55B`](../../claims/JCG-5B09E55B.md) |
| 5 | Every target prime divisor of a generic-degree-three complex Keller map has one of the retained-sheet types `U1`, `U2`, or `B`; a deleted three-cycle is impossible. | [`JCG-1D7EF048`](../../claims/JCG-1D7EF048.md); cubic-resolvent appendix |
| 6 | The finite normalization has rank-two reflexive trace-zero module and a finite nonflat locus. Flatness needs an additional Cohen--Macaulay conclusion. | [`JCG-C04524CF`](../../claims/JCG-C04524CF.md), [`JCG-A5938472`](../../claims/JCG-A5938472.md) |
| 7 | A cubic defect cannot be supported at an isolated singularity of the quadratic resolvent; its three-torsion is detected at height-two singular primes. | [`JCG-79BDB7F6`](../../claims/JCG-79BDB7F6.md); resolvent-defect appendix |
| 8 | In the stated smooth cubic-axis model, extension of the transverse three-torsion section makes the eigensheaf MCM and the associated cubic normalization flat. | [`JCG-69028659`](../../claims/JCG-69028659.md); smooth-axis theorem |
| 9 | Algebraically homogeneous minimal defects are excluded, while the analyzed smooth leading-cubic normal jets are gauge. | [`JCG-62422786`](../../claims/JCG-62422786.md), [`JCG-717B157D`](../../claims/JCG-717B157D.md) |
| 10 | If the cubic normalization is flat, it is pulled back from the universal marked-root master cover; identifying the affine source also requires boundary completeness. | [`JCG-2E563312`](../../claims/JCG-2E563312.md) |

These are working-paper results with proof offered or exact checks as shown on
their claim pages. None has an independent specialist review recorded.

## 4. The live frontier

**(F1) Keller-specific cubic flatness.** The open claim is not “all normal
`S_3` cubic covers are flat”; that statement is false. The target is narrower:
for the normalization attached to a Keller map, prove that the finite defect
module vanishes. The available structure is unusually rigid: the trace-zero
module is rank-two reflexive; its nonfree locus is finite and lies among
omitted target values; source splitting makes the cover flat over every
attained target point; divisorial sheet loss is classified. The remaining
module is therefore finite and boundary-supported.

**(F2) Conormal-root/MCM pushdown.** On the quadratic resolvent, formulate the
actual eigensheaf and its relation to the elliptic cubic appearing in the
project. The desired theorem must specify the overlap maps, the divisor or
class-group representative of the eigensheaf, and the hypotheses under which
a cube/conormal root becomes MCM. The smooth-axis theorem is a model case, not
the conclusion. A useful result may be conditional if it isolates exact
intersection and discrepancy data that can then be computed.

**(F3) Local torsor survival.** The analyzed minimal smooth defect end has a
local two-dimensional `F_3` sign-torsor space. The torsors algebraize locally,
but no nonzero class is known to survive around the complete global boundary.
Global survival would conflict with the absence of nontrivial finite étale
covers of affine three-space. The missing step is an end-to-global theorem,
not another local calculation.

**(F4) Boundary completeness.** Flatness alone produces the finite marked-root
cover. It does not show that deleting its boundary gives exactly `A^3` in the
required way. Keep this opening/completeness question separate from flatness
and from classification inside the explicit frame.

Dependencies: F2 supplies geometric inputs for a finite exceptional-lattice
calculation; that computation may attack F1. F1 plus F4 gives the conditional
master-cover conclusion. F3 is an alternative obstruction route and should
not be conflated with the MCM route.

## 5. Graveyard (causes of death — read before proposing routes)

- **Theta-commutativity.** The withdrawn argument tried to choose commuting
  lifts of a projective `C[3]` cocycle. Such lifts can have commutator equal
  to the Weil pairing, so projective compatibility does not imply the needed
  linear commutativity. Any replacement must work with the central extension
  or bypass it through conormal/MCM geometry.
- **Normal `S_3` implies flat.** False. An explicit minimal nonflat normal
  cubic algebra supplies a countermodel outside the Keller setting
  ([`JCG-583DA94A`](../../claims/JCG-583DA94A.md)). A successful theorem must
  use Keller-specific source splitting, omitted-value geometry, or another
  hypothesis absent from that countermodel.
- **Reflexive means locally free.** A rank-two reflexive module on a
  threefold can fail to be free at finitely many points. Reflexivity proves
  the defect is small; it does not kill it.
- **Local torsor equals global torsor.** Henselian or formal algebraization at
  one end gives no automatic extension through other boundary components.
  The compatibility problem is the substance.
- **Exceptional lattice before geometry.** No finite lattice computation is
  well posed until the intersection matrix, discrepancy vector, and
  eigensheaf divisor class are specified. Inventing these inputs from a
  schematic diagram would produce a certificate for the wrong problem.

## 6. Tasks

**P1-T1 — Prove a conormal-root MCM pushdown theorem.**

Actor: `online_model`. Status: ready.

*Inputs:* this page; the [Program 1 paper](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-22-v11.pdf), especially the cubic-resolvent defect appendix; the precise claims in F1–F2.

*Payoff:* either eliminates the remaining defect or produces the exact finite
geometric data needed for computation.

*Suggested attack:* write the quadratic resolvent and sign eigensheaf
intrinsically; analyze depth via the conductor and local cohomology; compare
the smooth-axis theorem with the singular height-two primes; keep the central
extension/Weil pairing visible.

*Done when:* a theorem with stated hypotheses applies to the actual elliptic
cubic/resolvent configuration, every sheaf and overlap is defined, and no
theta-commutativity step is used.

**P1-T2 — Compute the exceptional lattice and cohomology obstruction.**

Actor: `local_symbolic`. Status: blocked on T1.

*Inputs:* must be derived by T1: an explicit intersection matrix, discrepancy
vector, and eigensheaf divisor class.

*Payoff:* converts the remaining MCM or `H^1` question into an exact finite
certificate.

*Done when:* the derived inputs are hash-pinned and a rational/integer replay
settles the lattice and cohomology conditions without hidden geometric
assumptions.

**P1-T3 — Separate flatness from boundary completeness.**

Actor: `online_model`. Status: ready.

*Inputs:* [`JCG-2E563312`](../../claims/JCG-2E563312.md) and the normalization
sections of the paper.

*Done when:* a dependency diagram states exactly which conclusion follows
from finite flatness, which requires recovery of the open immersion, and
which uses the explicit frame classification.

## 7. Evidence and replay index

The working paper holds the conventional proofs. The public Program 1
technical supplement checks the normalized `A,B` identities, the
all-multiplicity equivalence formulas, the stable-uniqueness identities and
finite enumerations, root-slope identities, and the smooth-defect model
linear algebra. All arithmetic is exact.

The scripts verify pole-cancellation jets, determinants, discriminants,
transformation identities, selected finite-field counts, and Hesse/Fermat
rank tables. They do not prove normality, lifting through normalization,
purity, Euler integration, the MCM pushdown, or global torsor survival.
Finite-field enumerations support the stable-uniqueness strategy but are not
characteristic-zero proofs.

Proof access is organized by stable claim pages. Start with the
[cubic-normalization defect package](../../collections/cubic-normalization-defect-open-package.md)
and the [resolvent restrictions](../../collections/cubic-resolvent-defect-exclusions.md).
Submission still requires citation-level checking of Blanc--Stampfli,
specialist review of the finite-flat completion and boundary arguments, and
independent review of the codimension-two stable-uniqueness geometry.

A returned argument should include a short dependency ledger. For every
local statement, name whether it uses normality, the Keller source splitting,
the `S_3` action, the conductor, or a smoothness hypothesis. For every global
step, say which boundary components and overlaps are covered. This is not
editorial overhead: the known countermodels show that dropping one of these
hypotheses can change flatness. If a proposed proof produces explicit divisor
or intersection data but stops short of vanishing, preserve those data as the
resolved input specification for P1-T2 rather than presenting the attempt as
an all-or-nothing failure.
State explicitly whether each conclusion is local, divisorial, formal, or
global, and whether it survives base change.

## 8. Do not do

- Do not revive theta-commutativity without explicitly resolving the Weil
  pairing commutator.
- Do not infer flatness from normality, `S_3` monodromy, or reflexivity.
- Do not claim the `U1/U2/B` divisor classification controls isolated
  nonflat points.
- Do not turn the conditional master-cover theorem into an unconditional
  classification; flatness and boundary completeness are separate gates.
- Do not run the exceptional-lattice computation before its divisor and
  intersection inputs have been derived.
- Do not treat exact identity checks as independent verification of the
  algebraic-geometric arguments.
- Do not present the manuscript as refereed or submission-ready.

[Back to the Program 1 overview](../programs/cubic-marked-root-incidence-geometry.md)
