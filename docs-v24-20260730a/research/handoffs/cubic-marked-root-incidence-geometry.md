---
title: "Model research brief — Cubic Marked-Root Incidence Geometry"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 1</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 30 July 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v12c · site release <code>living-guide-public-v24-github-pr-recovery</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

# Program 1: Cubic Marked-Root Incidence Geometry
**Research state:** mathematical checkpoint 29 July 2026. Exact scope,
dependencies, and direct proof-body links are stated per input below.

**Actor guidance:** structural algebraic geometry -> online model; exact finite
lattice or matrix work -> local symbolic system after the geometric inputs
exist.

This page is the complete public handoff. A model can begin from this URL
alone. The linked [working paper](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-29-v13.pdf),
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

The boundary vocabulary is important. The corrected divisorial taxonomy has
four cases, `U0`, `U1`, `U2`, and `B`; the linked paper statement omitted
`U0`. The other cases respectively include three completed sheets with one
deleted (`U1`), three unramified sheets with two deleted (`U2`), and a
ramified `2+1` fiber with the ramified point deleted (`B`). A deleted
three-cycle is excluded in the Keller setting under analysis. This is a
codimension-one classification, not a classification of the isolated
nonflat points.

The **quadratic resolvent** packages the sign representation of the `S_3`
cover. A cubic defect gives three-torsion data on that resolvent. The current
route asks whether the relevant rank-one reflexive eigensheaf is maximal
Cohen--Macaulay and whether its conormal root can be pushed down globally.
Local models and isolated-singularity restrictions are known; the general
Keller-specific pushdown is not.

### Coverage rule

This page is optimized for choosing and specifying a task, not
proof-self-contained. Each numbered input gives the reusable statement with
its hypotheses; the proof-signature table gives dependencies and boundary
exits; the final column links directly to the proof body. Claim links preserve
stable identity.

### Compact glossary

- **Finite normalization:** normalization of the target in the source
  function field; it is finite but need not be flat.
- **Trace-zero module `E`:** the rank-two reflexive summand in the cubic
  algebra `O ⊕ E`; its nonfree locus is the finite flatness defect.
- **Conductor:** ideal measuring where the normalization and its image fail
  to agree; here it also marks deleted-sheet geometry.
- **Quadratic resolvent:** the double cover carrying the sign character of
  the `S_3` closure; its cubic eigensheaf is the prospective MCM object.
- **MCM:** maximal Cohen--Macaulay; depth three is the missing property that
  would remove the isolated cubic defect.

### Case and dependency map

```text
generic-degree-three Keller map
├─ normalize target in source field
│  ├─ codimension one ── U0 / U1 / U2 / B (corrected)
│  └─ isolated nonflat locus
│     ├─ isolated resolvent singularity ── excluded
│     ├─ smooth cubic axis + extended 3-torsion ── flat
│     ├─ homogeneous minimal defect ── excluded
│     └─ general Keller boundary ── conormal-root/MCM pushdown open
└─ if finite flat
   ├─ universal marked-root cover (conditional conclusion)
   └─ recover affine opening ── boundary completeness still open
```

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

## 3. Reusable inputs, exact scope, and proof access

| # | Exact input and hypotheses | Claim · direct proof body |
| --- | --- | --- |
| 1 | For a polynomial potential `H(T,c)` over a characteristic-zero field, the displayed root-slope substitution has Jacobian `-2` whenever its pole-cancellation conditions make it polynomial; its generic degree equals the root degree of `H`. | [`JCG-0106262F`](../../claims/JCG-0106262F.md) · [proof](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-29-v13.pdf#page=15) |
| 2 | For normalized cubic frames, polynomial left-right equivalence is exactly affine change of `c`, the prescribed scalar relation on `A`, congruence of `B` modulo `A`, and preservation of the marked root. Repeated roots are allowed. | [`JCG-221985FF`](../../claims/JCG-221985FF.md) · [proof](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-29-v13.pdf#page=7) |
| 3 | In the two-block multiplication-incidence construction with `a,b >= 1` and `a+b >= 3`, stable affineness occurs exactly for the unordered pair `{a,b}={1,2}`. | [`JCG-517DA8F4`](../../claims/JCG-517DA8F4.md) · [proof](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-29-v13.pdf#page=11) |
| 4 | For a coprime normalized cubic frame, the inverse cubic is irreducible with nonsquare discriminant, so generic monodromy is `S_3`; the target deck group is trivial. | [`JCG-504733CF`](../../claims/JCG-504733CF.md), [`JCG-5B09E55B`](../../claims/JCG-5B09E55B.md) · [proof](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-29-v13.pdf#page=5) |
| 5 | For the finite normalization attached to a generic-degree-three complex Keller map, the corrected divisorial taxonomy is `U0`, `U1`, `U2`, or `B`; a deleted three-cycle is impossible. The linked statement omits `U0`, so use the audit repair packet for the corrected formulation. This is divisorial only. | [`JCG-1D7EF048`](../../claims/JCG-1D7EF048.md) · [paper statement needing the U0 repair](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-29-v13.pdf#page=19) |
| 6 | The finite cubic normalization splits as `O ⊕ E` with `E` rank-two reflexive, and its nonflat locus is finite and contained in omitted values. Reflexivity alone does not imply flatness. | [`JCG-C04524CF`](../../claims/JCG-C04524CF.md), [`JCG-A5938472`](../../claims/JCG-A5938472.md) · [proof and defect boundary](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-29-v13.pdf#page=13) |
| 7 | If a cubic defect is encoded by the quadratic-resolvent eigensheaf, it cannot be supported only at an isolated resolvent singularity; nontrivial three-torsion is detected at height-two singular primes. | [`JCG-79BDB7F6`](../../claims/JCG-79BDB7F6.md) · [proof](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-29-v13.pdf#page=19) |
| 8 | In the stated smooth cubic-axis hypersurface model, if the transverse three-torsion section extends through the smooth relative torsion group, the eigensheaf is MCM and the cubic normalization is flat. Both hypotheses are essential. | [`JCG-69028659`](../../claims/JCG-69028659.md) · [proof](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-29-v13.pdf#page=20) |
| 9 | Under the algebraic-homogeneity hypotheses, a minimal cubic defect is impossible; in the separately stated smooth leading-cubic jet model, every analyzed normal jet is gauge. | [`JCG-62422786`](../../claims/JCG-62422786.md), [`JCG-717B157D`](../../claims/JCG-717B157D.md) · [full archival proof](../../assets/proof-archives/01-cubic-marked-root-covers-2026-07-22-v8.pdf#page=31) |
| 10 | If the finite cubic normalization is flat, its rank-two trace data pull back from the universal marked-root master cover. Recovering the original affine source additionally requires boundary completeness; flatness does not supply it. | [`JCG-2E563312`](../../claims/JCG-2E563312.md) · [conditional proof](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-29-v13.pdf#page=13) |

### Proof-signature index

| Inputs | Proof signature / reusable output | Boundary exits |
| --- | --- | --- |
| 1 | Normalize the root and slope coordinates; the Jacobian factors as `r/2` times `-4/r`, while clearing the `x`-poles forces the first two coefficient jets. **Output:** a valuation-safe root-slope chart and pole-cancellation test. | Polynomiality must be checked for each potential; the rational chart alone is not a map of affine space. |
| 2–3 | Recover the unique nonplane cusp and plane boundary components, then use cusp stabilizers/covariants to obtain the affine `c` change, scaling, and `B mod A`; for stable affineness, compute the class group of the two-block incidence and eliminate all pairs except `{1,2}` by divisor and motivic invariants. **Output:** frame-equivalence and stable-uniqueness criteria. | Applies to the stated incidence constructions, not arbitrary cubic covers. |
| 4–5 | Irreducibility of the inverse cubic plus nonsquare discriminant gives `S_3`; triviality of the deck group follows from the normalizer of a point stabilizer. Completed valuations of the pullback factors classify inertia and retained sheets; purity excludes an everywhere-cyclic alternative. **Output:** monodromy and corrected `U0/U1/U2/B` taxonomy. | Divisorial only; isolated nonflat points remain. |
| 6–7 | Split the finite cubic algebra by trace; reflexivity confines nonfreeness to codimension three. On the quadratic resolvent, a cubic eigensheaf `L` satisfies `L^[3] ≅ O`; Dao-type torsion-freeness rules out isolated resolvent support and detects any defect at height-two singular primes. **Output:** a finite, boundary-supported defect and its resolvent carrier. | Reflexive is not locally free; the general height-two-to-global pushdown is open. |
| 8–9 | Formally normalize higher terms on a smooth cubic axis, extend the transverse 3-torsion section in the smooth relative torsion group, identify its section module as MCM, and use codimension-two uniqueness to recover the eigensheaf. Separately, a surjective gauge map and Hesse determinant exclude homogeneous minimal defects; the local sign-torsor kernel is `F_3^2`. **Output:** a flat model case and exact residual torsor space. | Smooth axis and extension hypotheses are essential; local torsors need not survive globally. |
| 10 | Flat rank-two trace data are binary-cubic/triple-cover data, hence pull back from the universal factor space. **Output:** the conditional master cover. | Flatness and boundary completeness are two separate antecedents; neither is supplied by this row. |

## 4. The live frontier

**Audit checkpoint, 30 July 2026.** A full external-model audit found the
main spine largely sound and the recovered repair verifier replays. Besides
the `U0` omission, it repairs local gaps in B.1, 3.4(ii), and 6.1. Theorem
C.4 is not proved by the paper: it is a conditional MCM-comparison criterion.
The reported thirteen-commit repair branch is external state, so this page
does not imply that the linked paper already contains those repairs.

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

Each item is a task capsule. Its input list is authoritative: do not invent
the exceptional lattice before T1 produces its geometric data. If an
argument proves only a local, formal, or divisorial statement, stop there and
return that scope plus the exact missing global transition.

**P1-T1 — Prove a conormal-root MCM pushdown theorem.**

Actor: `online_model`. Status: ready.

*Inputs:* this page; the [Program 1 paper](../../assets/manuscripts/01-cubic-marked-root-covers-2026-07-29-v13.pdf), especially the cubic-resolvent defect appendix; the precise claims in F1–F2.

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

Proof access is organized by the direct PDF locators above and stable claim
pages. Start with the
[cubic-normalization defect package](../../collections/cubic-normalization-defect-open-package.md)
and the [resolvent restrictions](../../collections/cubic-resolvent-defect-exclusions.md).
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

[Back to the Program 1 overview](../../research/programs/cubic-marked-root-incidence-geometry.md)

[Back to the Program 1 overview](../programs/cubic-marked-root-incidence-geometry.md)
