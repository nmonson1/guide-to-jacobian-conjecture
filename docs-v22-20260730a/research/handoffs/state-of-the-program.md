---
title: "Model research brief — State of the Jacobian Research Program"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Cross-program</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 30 July 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v11 · site release <code>living-guide-public-v22-research-import-checkpoint</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }
# State of the Jacobian Research Program

**Research state:** mathematical checkpoint 30 July 2026. Exact scope,
dependencies, and direct routes to the program proof bodies are stated below.

**Scope:** complete cross-program orientation for a research model deciding
where its work has the highest leverage. Program-specific handoffs provide
deeper exact statements, proof locators, and optional executable tasks.

This page joins the six research programs without replacing their claim
pages or papers. The [research index](../index.md),
[stable claim catalogue](../../results/all-claims.md),
[working papers](../papers.md), and [proof index](../../evidence/index.md)
provide the authoritative details.

## Research freedom and how to use the nine links

The nine lanes below are **attention coordinates, not cognitive silos**.
Each lane link opens this same complete portfolio handoff at a different
suggested frontier, so a model assigned to one lane still has the proved
results, dead ends, dependencies, and possible connections for all six
programs in context.

The listed problems are our current best judgment about useful next steps,
not a closed or exhaustive queue. Pursue a different problem, stronger
statement, cross-program connection, simplification, counterexample, or new
construction if it appears more mathematically valuable. When departing
from the suggested frontier, state what you are pursuing, why it has higher
leverage, which existing results it uses or might supersede, and what would
count as a meaningful outcome. Then proceed without waiting for approval
unless a genuinely missing input or change of scope requires it.

Exact task capsules deeper in the program handoffs are optional on-ramps.
They are useful when the proposed direction happens to match one; they do
not bound the research. In every direction, preserve hypotheses, provenance,
verification boundaries, and the separation between a calculation and the
global theorem it may support.

Share the whole page, optionally with one of these stable fragments:

1. [Cubic flatness and normalization defect](#lane-1-cubic-flatness)
2. [Boundary completeness and Torelli at infinity](#lane-2-boundary-torelli)
3. [Bounded-degree deformation and modulus onset](#lane-3-deformation-moduli)
4. [The quartic endgame](#lane-4-quartic-endgame)
5. [Intrinsic degree and valuative budgets](#lane-5-degree-budgets)
6. [Homogeneous realization and compression](#lane-6-homogeneous-compression)
7. [Five-dimensional collision geometry](#lane-7-collision-geometry)
8. [Plane Newton queue and terminal certificates](#lane-8-plane-newton-queue)
9. [Plane chart correspondence and global attachment](#lane-9-plane-global-attachment)

## 1. Setup and notation

The project starts from an explicit noninjective polynomial Keller map in
three variables. Its ordinary coordinate degrees are `(7,6,4)`, its generic
fiber degree is three, and the Galois closure has monodromy `S_3`. Ordinary
degree and generic degree are different filtrations and must never be
substituted for one another.

The claim graph organizes 368 public atomic statements into 104 grouped
result/open-problem packages and six paper programs:

1. **Cubic marked-root incidence geometry:** classify the finite cubic cover,
   lost sheets, and normalization defect.
2. **Minimum degree and quartic exclusions:** decide whether an ordinary
   degree-four counterexample exists.
3. **Local rigidity and deformation algebra:** understand the degree-bounded
   germ at the known example and its length-584 Artin algebra.
4. **Stable moduli:** classify inequivalent frames and glue decorated boundary
   data as roots escape to infinity.
5. **Homogeneous descendants:** minimize dimensions and pairing ranks of
   homogeneous presentations and analyze five-dimensional collision strata.
6. **Plane boundary obstructions:** separate exact terminal exclusions from
   the upstream Newton and global-gluing steps in dimension two.

Three complexity measurements recur:

- `D_min`: least ordinary degree of a three-dimensional counterexample;
  currently `4 <= D_min <= 7`.
- `D_mod(G)`: least degree at which every neighborhood of the normalized
  representative `G` meets infinitely many polynomial left-right classes,
  using a pointed-curve definition because ordinary degree is not
  left-right invariant.
- realization complexity of the fixed three-sheeted cover: ordinary degree,
  minimum cubic-homogeneous dimension, and minimum Drużkowski pairing rank.

The finite-cover viewpoint supplies the main bridge. A generic-degree-three
map factors through a finite normal cubic cover. If that cover is flat and
its open boundary is complete, it should be a marked-root cover. Cubic-frame
Torelli then classifies a large explicit locus by decorated boundary data.
Degree budgets would connect that classification to low ordinary degree.

The plane program is related but not a direct specialization. In dimension
two, complete Newton chains and boundary covers impose valuations, passports,
and support constraints absent from a naive slice of the three-dimensional
example.

### Coverage rule

This handoff is **orientation-complete, not proof-self-contained**. Each
anchor gives the shortest reusable mechanism, its boundary exit, and a direct
route to the program handoff where exact hypotheses and page-level proof
links are collected.

### Compact glossary

- **Ordinary degree:** maximum coordinate degree; not generic fiber degree.
- **Generic degree:** degree of the induced function-field extension.
- **Closure / Torelli / opening / budget:** respectively construct the finite
  cover, classify its intrinsic data, recover the affine open, and bound the
  ordinary degree of a realization. None implies the next automatically.
- **Proof signature:** the shortest reusable mechanism chain—normalization,
  invariant or lemma, decisive obstruction, and boundary exits. It is a map
  of a proof, not a replacement for it.
- **Boundary exit:** a hypothesis or exceptional stratum where the cited
  mechanism stops and another theorem or task must take over.

### Case and dependency map

```text
known three-sheeted counterexample
├─ generic-degree-three anatomy (P1)
│  ├─ finite flatness? ── no: defect/MCM frontier
│  └─ flat ── boundary complete? ── yes: marked-root classification
├─ ordinary degree four (P2)
│  ├─ leading span 1 ── excluded
│  ├─ leading span 3 ── excluded
│  └─ leading span 2 ── ramification/fixed-component endgame
├─ bounded germ at degree 7 (P3) ── length 584; degree-8 saturation open
├─ fixed-frame moduli (P4) ── finite-root Torelli; infinity gluing open
├─ alternate presentations (P5) ── 19D → 38D / 110D; lower bounds open
└─ plane case (P6) ── exact terminal exclusions
   └─ global conclusion requires queue exhaustiveness + chart descent
```

## 2. Goal and payoff

The central strategic goal is a **finite closure plus boundary theory**:

```
Keller map
  -> marked finite cover with deleted boundary
  -> intrinsic decorated boundary data
  -> ordinary-degree budget.
```

Each arrow is a separate theorem. Closure records the finite cover. Torelli
asks whether decorated boundary data determine it on a specified locus.
Opening/completeness asks whether the affine open is recoverable. Budget asks
which decorated covers can occur below an ordinary-degree bound.

This architecture would link the strongest present results. Cubic flatness
plus boundary completeness would classify generic-degree-three maps by
marked-root covers. The Program 2 degree-four case tree could then use an
intrinsic degree budget rather than treating only one generic-degree stratum.
Stable-moduli invariants would become coordinates on the closure data.
Homogeneous descendants would become alternate presentations of the same
cover, inviting lower bounds from boundary invariants. Program 6 would serve
as a surface-level testing ground for valuative budgets and chart descent.

The nearer payoff is a disciplined research queue. Several impressive
finite computations are already complete. The next useful work is not to
rerun them, but to clear the reproduction, exhaustiveness, and missing-lemma
gates that determine whether they support global theorems.

## 3. What is proved

| Input | Proof signature / reusable output | Boundary exit | Exact statements and proofs |
| --- | --- | --- | --- |
| Base-map fiber stratification | Write the inverse cubic; simple roots reconstruct source points, its discriminant gives the double-root fiber, and the triple-root curve removes the final affine sheet. **Output:** the exact `3/1/0` fiber chart. | This is the named map, not arbitrary cubic covers. | [`JCG-55104EF2`](../../claims/JCG-55104EF2.md) · [Program 1 proof routes](cubic-marked-root-incidence-geometry.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P1 cubic anatomy | Normalize in the cubic function field; split trace as `O ⊕ E`; use completed valuations and inertia for `U1/U2/B`; reflexivity confines nonflatness to finitely many omitted values. **Output:** trace module plus divisorial sheet taxonomy. | Reflexivity does not kill isolated defects; opening is separate. | [Program 1 exact inputs and proofs](cubic-marked-root-incidence-geometry.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P2 quartic reductions | Expand the scaled determinant arc; stratify by leading target span; use valuations and Hilbert–Burch normal forms to route span two into ramification and fixed-component leaves. The controlling v5 bundle now exactly closes every previously listed degree-three normal-form chart. **Output:** a conditional quartic terminal-leaf synthesis plus exact degree-three certificates. | The global case tree, proof-to-code correspondence, imported complete-specialization claim, and independent reproduction remain open; `D_min >= 5` is not unconditional. | [Program 2 exact inputs and proofs](minimum-degree-and-quartic-exclusions.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P3 length-584 germ | Cut the affine orbit slice; use torus attractors plus a nullcone lemma; match inverse-system and multiplication-matrix bounds; compare source-flow and determinant complexes through order four. **Output:** the length-584 Artin algebra and two compatible presentations. | No all-order source-flow theorem; degree eight has shear components. | [Program 3 exact inputs and proofs](local-rigidity-and-deformation-algebra.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P4 fixed-frame Torelli and quotients | Recover the intrinsic `(c,t)` chart from the relative Jacobian; read multiplicities; recover `(A,B mod A)` and lift by root translation. Separately compute categorical invariants and the `e>=1` fppf rank-one wall. **Output:** decorated Artin data plus noninterchangeable quotient objects. | Fixed-frame locus only. The local graph-closure formulas are candidates pending complete definitions and proof; simultaneous infinity escapes remain open. | [Program 4 exact inputs and proofs](stable-moduli.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P5 descendant ladder | Factor the cubic span and use a Schur complement for the 19D suspension; certify the long nilpotent chain; cotangent-double; bound pairing length by the commutant obstruction and explicit square-zero factorization. **Output:** 19D, 38D, and 110D presentations of one cover. | Bounds are for the fixed tensor; global minimality is open. | [Program 5 exact inputs and proofs](homogeneous-descendants.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P6 stored terminal exclusion | Identify the layer-four kernel as a `k=4` rechart; force a common approximate root in the adjacent chart; close the remaining branches by exact affine/toric certificates. **Output:** no gluing for the stored degree-21 terminal system. | The below-125 implication is **open** pending upstream exhaustiveness. | [Program 6 exact inputs and proofs](plane-boundary-obstructions.md#3-reusable-inputs-exact-scope-and-proof-access) · open dependency [`JCG-9D0BE662`](../../claims/JCG-9D0BE662.md) |

Two cross-program assertions require special caution. The cubic-frame graph
records degree eleven as the first ordinary degree with a positive-dimensional
stable modulus ([`JCG-CA01A7A7`](../../claims/JCG-CA01A7A7.md)); use its
restricted cubic-frame hypotheses and direct locator before relying on it.
The public degree-below-125 plane theorem is credited external context;
the project's terminal certificates do not erase the upstream dependency.

**July 30 research checkpoint.** Eleven new research conversations were read
in full and reduced to scoped result/evidence records. Exact replays
strengthen local inputs—especially the Lane 5 filtered-degree barrier—while
also exposing a Lane 4 verifier failure and missing evidence in Lanes 2, 3,
and 9. None changes a paper or promotes a global theorem. The next audit
campaign is exhaustive source-to-claim reconciliation: extract atomic
occurrences from every message and artifact, group only exact equivalents,
type weaker relations, give every live class one primary paper/register
home, and verify the reverse paper-to-source map. Manuscript-native
derivations remain allowed.

## 4. The live frontier

The nine lanes partition attention, not mathematics. Connections named below
are invitations, not a complete list.

<a id="lane-1-cubic-flatness"></a>
### Lane 1 — Cubic flatness and finite normalization defect

For a generic-degree-three Keller map, prove that the finite normalization
defect vanishes. The available structure is unusually rigid: the trace-zero
module is rank-two reflexive, its nonfree locus is finite and supported at
omitted target values, source splitting gives flatness over every attained
point, and divisorial sheet loss is classified. Promising directions include
the conormal-root/MCM pushdown on the quadratic resolvent, the finite
exceptional-lattice calculation, or a new commutative-algebra argument using
the Keller-specific splitting. A broader anatomy theorem is also valuable
if it keeps branch image, nonproperness, flatness, and classification
logically separate. [Exact Program 1 frontier and proof routes](cubic-marked-root-incidence-geometry.md#4-the-live-frontier).

<a id="lane-2-boundary-torelli"></a>
### Lane 2 — Boundary completeness and Torelli at infinity

Determine when the finite marked-root closure remembers the affine opening,
and extend fixed-frame Torelli across roots escaping to infinity. Program 1
supplies the opening/completeness problem; Program 4 supplies finite-root
classification and local principal-part coordinates, plus graph-closure
candidates whose local identification still needs a self-contained proof.
New exact tests include a recursive principal-parts law, an `m=3`
common-factor atlas, and an `N=3` Cox/fan model; they do not prove global
gluing, and the referenced Rees--Jordan checker remains unavailable.
The high-leverage theorem would give intrinsic boundary data, overlap maps
for simultaneous escapes, cocycle compatibility, and a correctly scoped
reconstruction result. Low-length invariant, Smith/Fitting, and
triple-overlap calculations are useful theorem tests. Do not keep the open
immersion as part of the datum and call reconstruction solved.
[Program 1 frontier](cubic-marked-root-incidence-geometry.md#4-the-live-frontier) ·
[Program 4 frontier](stable-moduli.md#4-the-live-frontier).

<a id="lane-3-deformation-moduli"></a>
### Lane 3 — Bounded-degree deformation and modulus onset

Relate the exact degree-seven local algebra to the first appearance of
genuine stable moduli. Useful next steps include completing the second
orders-seven-and-eight reconstruction, identifying the source-flow and
determinant obstruction complexes at all orders, describing the
degree-eight germ after affine and shear components are included, and
reproducing the Program 4 `q`-separation invariant and scoped degree-eleven
threshold. A stronger synthesis explaining *why* local rigidity breaks when
moduli appear would be more valuable than four isolated calculations.
New exact finite inputs give tangent rank `439`, nullity `44`, and a
28-dimensional residual character; the proposed fixed-shear saturation is
local and lacks its referenced certificate.
Independent reproduction is an audit overlay, not the mathematical
definition of this lane. [Program 3 frontier](local-rigidity-and-deformation-algebra.md#4-the-live-frontier) ·
[Program 4 frontier](stable-moduli.md#4-the-live-frontier).

<a id="lane-4-quartic-endgame"></a>
### Lane 4 — The quartic endgame

Finish the ordinary-degree-four case or find the surviving construction.
The generic degree-three ramification chart, higher-ramification cases, and
fixed-component calculations now replay. The controlling v5 bundle also
closes the supplied generic `F_3/F_4`, `tau=0,-1`, `tau^2+1`, `c=0`,
dependent-syzygy, quadratic-exceptional, and zero-normal charts. Its internal
manifest passes and every stored deterministic output matches a fresh replay.
The sharp work has moved upstream and sideways: write and audit the single
global quartic case tree, map every proof chart to code, check the
complete-specialization theorem imported by the new high-ramification
checker, and reproduce the reconstructed degree-three lineage independently.
In addition, an exact companion/Jordan-chain construction supplies a
degree-specific audit lens: its divisor moments force
`deg gcd(grad(P) cross grad(Q)) >= 4` in the quartic span-two setup, and its
v4 programs route or exclude selected `H=4,5,6` charts. All ten supplied
v2-v4 exact checks replay. The chart results remain conditional, the
foundational sheaf argument remains unchecked outside its original
derivation, and the repository already has stronger closures for the
affected loci. The bundle's terminal-leaf synthesis gives `D_min >= 5` only
conditional on the global routing audit; the unconditional interval remains
`4 <= D_min <= 7`. This lane has the most immediate theorem payoff: the
audit either removes that qualifier or identifies a new quartic candidate.
The exploratory degree-five/six work is chart-local, and its main quartic
verifier fails two assertions; neither changes the theorem status.
Its interaction with Lane 5 may replace some chart work only if the budget
is intrinsic to the full left-right orbit.
[Exact Program 2 frontier and consistency anchors](minimum-degree-and-quartic-exclusions.md#4-the-live-frontier).

<a id="lane-5-degree-budgets"></a>
### Lane 5 — Intrinsic degree and valuative budgets

Build the missing bridge from finite-cover or boundary data to ordinary
degree. Exact filtered calculations now handle every listed source
filtration with `delta(Q)<=9` and give `trdeg A_{<=6}<=2` after regenerating
their omitted bases. The residual frontier is unramified `delta(Q)>=10` plus
a conceptual filtered-conormal, Wronskian, or conductor theorem; this is not
yet full left-right minimality. The target remains an arbitrary-left-right
monotone or a non-degree-increasing canonical normalization.
The companion/Jordan divisor budget is a useful prototype and Program 2
audit tool, but it is tied to a chosen degree and determinant-arc
presentation. Arbitrary polynomial left-right changes need not preserve it,
so it does not solve this lane as stated.
Valuations, conductors, pole divisors, Newton data, and marked boundary
multiplicities are plausible inputs. A successful theory could connect
Lane 1 closure, Lane 2 Torelli, Lane 4 quartic exclusions, and the surface
budgets implicit in Lanes 8–9. A counterexample showing that a proposed
boundary invariant cannot control orbit degree is also a useful result.
Dimension counts alone are specifically disallowed by the known example.

<a id="lane-6-homogeneous-compression"></a>
### Lane 6 — Homogeneous realization and compression

Determine the true realization complexity of the fixed three-sheeted cover,
not merely the complexity of current presentations. The immediate problem is
whether the 19-dimensional cubic-homogeneous suspension can compress to 18
once all 109 row-killing directions and nonlinear target/stable changes are
allowed; the known constant obstruction covers only one six-dimensional
slice. Normal forms, equivariance, boundary invariants, or a smaller exact
coupled elimination are all plausible. The open extension theorem for
collision monoliths and the `sl/sp` dichotomy may provide a conceptual lower
bound. Connections to Lane 5 are welcome if they produce invariants of the
cover rather than of one tensor presentation.
[Exact Program 5 frontier](homogeneous-descendants.md#4-the-live-frontier).

<a id="lane-7-collision-geometry"></a>
### Lane 7 — Five-dimensional collision geometry

Resolve the characteristic-zero geometry of the exact fifteen-equation
collision chart. The staged goal is saturation by the open-locus factors,
radical/component decomposition, dimensions and degrees, and the open-chart
singular locus; previous monolithic Macaulay2 attempts returned no
mathematical result. Once components are known, decide the global
first-normal obstruction in each function field rather than extrapolating
from thirty finite-field points or one residue disk. Persistent components
are possible construction loci, not failed exclusions. A geometric
reformulation that avoids brute-force saturation is encouraged, especially
if it also illuminates homogeneous compression.
[Inputs, failed attempts, and exact Program 5 scope](homogeneous-descendants.md#4-the-live-frontier).

<a id="lane-8-plane-newton-queue"></a>
### Lane 8 — Plane Newton queue and terminal certificates

Certify that the exact stored terminal exclusions occur at the leaves of a
complete Newton/face pipeline. Regenerate lower faces, saturations,
normalizations, deficiency layers, chart transitions, and branch splits
from the two normalized supports, recording hashes and every routing
decision. Support-aware normal coordinates may simplify the calculation
only if the triangular support filtration is transported exactly. An
independent Hurwitz/Belyi and selected-rank reproduction is a useful release
gate, but queue exhaustiveness is the theorem-facing objective. The existing
unit-ideal and toric certificates remain exact for their displayed systems;
they do not by themselves prove the public below-125 implication.
[Exact Program 6 frontier](plane-boundary-obstructions.md#4-the-live-frontier).

<a id="lane-9-plane-global-attachment"></a>
### Lane 9 — Plane chart correspondence and global attachment

Develop the local-to-global theory that the plane terminal computations
currently lack. First distinguish fixed-chart gauge kernels from transitions
to adjacent complete-chain charts and prove how supports and residue
conditions descend. Then treat the `F_2` branch as a genuine two-sided
obstruction/construction problem: retain every fresh kernel parameter and
affine-linear term, solve the band-convolution system, and impose global
polynomial support plus cyclic descent. The local recurrence is integrable
through the checked orders, so a zero-new-parameter order-530 slice is not a
global obstruction. Connections to Lane 2 boundary gluing and Lane 5
valuative budgets may be especially productive.
The Lane 9 toolkit's six tests pass, but the upper-face matrices, actual
`F_2` blocks, and archived `C9` replay are absent. Its averaging lemma shows
plain cyclic descent alone cannot obstruct the stable-support system.
[Exact Program 6 frontier](plane-boundary-obstructions.md#4-the-live-frontier).

## 5. Graveyard (causes of death — read before proposing routes)

- **Generic degree is controlled by ordinary degree.** Bézout gives only a
  broad upper bound. After excluding generic degree three, ordinary degrees
  four through six can still support many generic degrees. Quartic-cover
  classification alone cannot settle every low-ordinary-degree map.
- **Dimension counts prove a degree budget.** The known counterexample
  defeated this style of heuristic. A useful budget must be valuative,
  geometric, or certificate-backed.
- **Frame-minimal equals orbit-minimal.** Minimization over explicit
  `(phi,kappa,B mod A)` frame moves does not cover arbitrary polynomial
  source and target automorphisms.
- **Finite closure already remembers the affine opening.** Keeping an open
  immersion in the object makes reconstruction tautological. Forgetting it
  creates the genuine affine-space recognition problem.
- **An estimate can coexist with an unreconciled registry theorem.** The
  degree-eleven value was once separately estimated while a graph record
  already asserted it as proved. Search and reconcile the graph before
  proposing a numerical claim.
- **Successful finite certificate equals global theorem.** Program 2 needs
  stratum exhaustiveness; Program 5 needs characteristic-zero component
  geometry; Program 6 needs the upstream queue and descent. The same logical
  separation recurs across programs.
- **Negative computation is the only valuable outcome.** Persistent solution
  components are candidate constructions and must be escalated as such.

## 6. Tasks

These are optional exact on-ramps, not assignments that prohibit broader
work. Use them when they match the direction you judge most valuable:

| Lane | Existing exact task capsules |
| --- | --- |
| 1 | Program 1 `P1-T1` conormal-root pushdown, `P1-T2` exceptional lattice |
| 2 | Program 1 `P1-T3` flatness/opening separation; Program 4 `P4-T1` proof hardening, `P4-T2` local graph definition and overlap tests |
| 3 | Program 3 `P3-T1` exact reconstruction, `P3-T2` all-order comparison, `P3-T3` second-system reproduction; Program 4 `P4-T3` modulus-onset verification |
| 4 | Program 2 `P2-T1` global case tree, `P2-T2` independent v5 reproduction, `P2-T3` proof/code correspondence |
| 5 | No capsule yet; formulate an intrinsic full-orbit budget or decisive obstruction to one |
| 6 | Program 5 `P5-T2` nonlinear 19-to-18 coupling |
| 7 | Program 5 `P5-T1` saturated collision components, `P5-T3` obstruction on each component |
| 8 | Program 6 `P6-T1` complete lower-face pipeline plus the independent reproduction frontier |
| 9 | Program 6 `P6-T2` chart correspondence, `P6-T3` full `F_2` attachment |

Before substantial work, briefly record the chosen direction, why it is
high leverage, the inputs being relied on, and the intended mathematical
output. A useful return contains the exact statement reached or refuted, a
proof body or reproducible computation contract, a dependency and
supersession ledger, and explicit distinctions among proved facts,
computational evidence, conjectures, and abandoned routes. If a missing
lemma changes the scope, expose it. If a persistent solution component
appears, preserve it as a construction lead.

## 7. Evidence and replay index

Exact scripts certify identities, ranks, finite eliminations, or listed
certificates. Conventional geometric arguments live in the papers. The
program handoffs above provide the shortest route from each reusable
statement to the relevant proof body.

The technical release includes complete supplements for all six programs and
focused materials for major continuations. The claim pages carry stable tags
and proof-access status. The handoff pages compress this graph into a working
frontier but introduce no substitute source of truth.

Every returned research result must re-enter through the ordinary intake and
claim-integration pipeline before it changes a paper or public claim. Literature
and priority checks must be refreshed immediately before submission or
announcement, especially for the fast-moving low-degree and plane-boundary
claims.

## 8. Do not do

- Do not treat an assigned lane as a silo or the listed tasks as an
  exhaustive research agenda.
- Before committing to an exact program calculation, read its
  program-specific handoff and use the stated inputs and acceptance boundary.
- Do not treat ordinary degree, generic degree, homogeneous dimension, and
  pairing rank as interchangeable.
- Do not call a restricted-frame minimum an intrinsic left-right-orbit
  minimum.
- Do not combine closure, Torelli, opening, and budget into one theorem.
- Do not let a finite computation silently absorb its case-tree or descent
  hypotheses.
- Do not re-run completed generic or finite calculations when the live gate
  is geometric, exhaustive, or independently reproductive.
- Do not promote model output directly into a manuscript; route it through
  the claim graph and integration pipeline.

[Back to the research overview](../index.md)

[Back to the research overview](../index.md)
