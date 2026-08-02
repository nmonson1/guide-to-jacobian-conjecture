# State of the Jacobian Research Program
**Research state:** mathematical checkpoint 1 August 2026. Exact scope,
dependencies, and direct routes to the program proof bodies are stated below.

**Scope:** complete cross-program orientation for a research model deciding
where its work has the highest leverage. Program-specific handoffs provide
deeper exact statements, proof locators, and optional executable tasks.

## Research freedom and how to use the nine lane pages

The nine lanes below are **attention coordinates, not cognitive silos**.
Each lane page opens a suggested frontier while
preserving the results, dead ends, dependencies, and cross-program context.

The listed problems are our current best judgment about useful next steps,
not a closed or exhaustive queue. Pursue a different problem, stronger
statement, connection, simplification, counterexample, or construction if it
has greater leverage. State the alternative, why it matters, its dependencies,
and what would count as progress; then proceed unless an input is missing.

Exact task capsules are optional on-ramps, not bounds. Preserve hypotheses,
provenance, and the boundary between a calculation and a global theorem.

Share this portfolio hub or one of these focused lane pages:

1. [Cubic flatness and normalization defect](cubic-flatness-normalization-defects.md)
2. [Boundary completeness and Torelli at infinity](boundary-completeness-torelli-at-infinity.md)
3. [Bounded-degree deformation and modulus onset](bounded-degree-deformation-modulus-onset.md)
4. [The quartic endgame](quartic-endgame.md)
5. [Intrinsic degree and valuative budgets](intrinsic-degree-valuative-budgets.md)
6. [Homogeneous realization and compression](homogeneous-realization-compression.md)
7. [Five-dimensional collision geometry](five-dimensional-collision-geometry.md)
8. [Plane Newton queue and terminal certificates](plane-newton-queue-terminal-certificates.md)
9. [Plane chart correspondence and global attachment](plane-chart-correspondence-global-attachment.md)

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
├─ alternate presentations (P5) ── 19D → 38D / 110D; source coupling advanced
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
| Base-map fiber stratification | Write the inverse cubic; simple roots reconstruct source points, its discriminant gives the double-root fiber, and the triple-root curve removes the final affine sheet. **Output:** the exact `3/1/0` fiber chart. | This is the named map, not arbitrary cubic covers. | [`JCG-55104EF2`](../../claims/JCG-55104EF2.md) · [Program 1 proof routes](../../research/handoffs/cubic-marked-root-incidence-geometry.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P1 cubic anatomy | Normalize in the cubic function field; split trace as `O ⊕ E`; use completed valuations and inertia for `U1/U2/B`; reflexivity confines nonflatness to finitely many omitted values. **Output:** trace module plus divisorial sheet taxonomy. | Reflexivity does not kill isolated defects; opening is separate. | [Program 1 exact inputs and proofs](../../research/handoffs/cubic-marked-root-incidence-geometry.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P2 quartic reductions | Expand the scaled determinant arc; stratify by leading target span; use valuations and Hilbert–Burch normal forms to route span two into ramification and fixed-component leaves. The controlling v5 bundle now exactly closes every previously listed degree-three normal-form chart. **Output:** a conditional quartic terminal-leaf synthesis plus exact degree-three certificates. | The global case tree, proof-to-code correspondence, imported complete-specialization claim, and independent reproduction remain open; `D_min >= 5` is not unconditional. | [Program 2 exact inputs and proofs](../../research/handoffs/minimum-degree-and-quartic-exclusions.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P3 length-584 germ | Cut the affine orbit slice; use torus attractors plus a nullcone lemma; match inverse-system and multiplication-matrix bounds; compare source-flow and determinant complexes through order four. **Output:** the length-584 Artin algebra and two compatible presentations. | No all-order source-flow theorem; degree eight has shear components. | [Program 3 exact inputs and proofs](../../research/handoffs/local-rigidity-and-deformation-algebra.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P4 fixed-frame Torelli and quotients | Recover the intrinsic `(c,t)` chart from the relative Jacobian; read multiplicities; recover `(A,B mod A)` and lift by root translation. Separately compute categorical invariants and the `e>=1` fppf rank-one wall. **Output:** decorated Artin data plus noninterchangeable quotient objects. | Fixed-frame locus only. The local graph-closure formulas are candidates pending complete definitions and proof; simultaneous infinity escapes remain open. | [Program 4 exact inputs and proofs](../../research/handoffs/stable-moduli.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P5 descendant ladder | Factor the cubic span and use a Schur complement for the 19D suspension; certify the long nilpotent chain; cotangent-double; bound pairing length by the commutant obstruction and explicit square-zero factorization. **Output:** 19D, 38D, and 110D presentations of one cover. | Bounds are for the fixed tensor; global minimality is open. | [Program 5 exact inputs and proofs](../../research/handoffs/homogeneous-descendants.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P6 stored terminal exclusion | Identify the layer-four kernel as a `k=4` rechart; force a common approximate root in the adjacent chart; close the remaining branches by exact affine/toric certificates. **Output:** no gluing for the stored degree-21 terminal system. | The below-125 implication is **open** pending upstream exhaustiveness. | [Program 6 exact inputs and proofs](../../research/handoffs/plane-boundary-obstructions.md#3-reusable-inputs-exact-scope-and-proof-access) · open dependency [`JCG-9D0BE662`](../../claims/JCG-9D0BE662.md) |

Two cross-program assertions require special caution. The cubic-frame graph
records degree eleven as the first ordinary degree with a positive-dimensional
stable modulus ([`JCG-CA01A7A7`](../../claims/JCG-CA01A7A7.md)); use its
restricted cubic-frame hypotheses and direct locator before relying on it.
The public degree-below-125 plane theorem is credited external context;
the project's terminal certificates do not erase the upstream dependency.

**August 1 PR assimilation.** PRs 2 and 3 were already integrated at source
level. PR 4's five Program 6 proof repairs are now in the canonical
manuscript, while its large-certificate and upstream-queue boundaries remain.
PR 1's exact Program 5 continuation now classifies every finite slope in
the selected rank-six plane through its first intrinsic obstruction. Generic
slopes and the rational exceptional slope `r=4` fail at cubic order. The two
conjugate slopes `r=4+-4 sqrt(-3)` have 17-dimensional cubic-lift fibres but
an intrinsic quartic obstruction, with exact certificate pairing `-1152`.
This remains a selected-plane result, not a classification of the full finite
row-base fibre or stable quotient.

Three other bounded advances are now retained: ordered-composition PRS charts
and block-constant Smith exponents in Lane 2; a five-variable universal
order-six system in Lane 3; and the Program 5 five-dimensional polynomial-gauge
core, whose degree-one obstruction is supported on three explicit surfaces.
Each lane page states the exact remaining hypotheses and next calculation.
None of the four stale generated-site trees was merged. Recovered packets:
[PR 1](https://github.com/nmonson1/guide-to-jacobian-conjecture/pull/1)
[PR 2](https://github.com/nmonson1/guide-to-jacobian-conjecture/pull/2)
[PR 3](https://github.com/nmonson1/guide-to-jacobian-conjecture/pull/3)
[PR 4](https://github.com/nmonson1/guide-to-jacobian-conjecture/pull/4)
are unmerged and qualified.

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
logically separate. [Exact Program 1 frontier and proof routes](../../research/handoffs/cubic-marked-root-incidence-geometry.md#4-the-live-frontier).

<a id="lane-2-boundary-torelli"></a>
### Lane 2 — Boundary completeness and Torelli at infinity

Determine when the finite marked-root closure remembers the affine opening,
and extend fixed-frame Torelli across infinity. A 31 July continuation audit
finds the proposed incidence, empty-boundary, multiplicity, `S_3`, and
one-wall repairs sound at model level. The fixed multigraph is proper and
separated as a coefficient stack, but only its fixed equations commute with
arbitrary base change. Locally the coarse one-root graph is
`Bl_(epsilon^(N+2),y)`; Smith/Fitting tests pass for `N<=3`. Direct and
ordered `N=3` charts differ by `Bl_(u^2,v)`, while the tested triple cocycle
holds only for coprime factors. None proves global or intrinsic stable
gluing. Continue with simultaneous relative-Jacobian flattening, a
noncoprime triple collision, or rigidified family comparison. Do not retain
the open immersion as data and call reconstruction solved.
[Program 1 frontier](../../research/handoffs/cubic-marked-root-incidence-geometry.md#4-the-live-frontier) ·
[Program 4 frontier](../../research/handoffs/stable-moduli.md#4-the-live-frontier).

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
The newest tangent/character packet gives rank `439`, nullity `44`, and a
28-dimensional residual character, correcting the idea that only weights
`-2,-1` remain; its proposed fixed-shear saturation is local and lacks the
referenced certificate.
Independent reproduction is an audit overlay, not the mathematical
definition of this lane. [Program 3 frontier](../../research/handoffs/local-rigidity-and-deformation-algebra.md#4-the-live-frontier) ·
[Program 4 frontier](../../research/handoffs/stable-moduli.md#4-the-live-frontier).

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
An exact companion/Jordan-chain construction now supplies a second,
degree-specific audit lens: its divisor moments force
`deg gcd(grad(P) cross grad(Q)) >= 4` in the quartic span-two setup, and its
controlling v4 programs route or exclude several displayed high-`H` and
`H=4` charts. All ten supplied v2-v4 exact checks replay. This does not move
the frontier past branch exhaustiveness: the chart results are conditional,
the foundational sheaf argument still needs specialist verification, and
the repository already has stronger closures for the affected
higher-ramification and fixed-factor loci.
The bundle's terminal-leaf synthesis gives `D_min >= 5` only conditional on
that global routing audit; the unconditional interval remains
`4 <= D_min <= 7`. This lane has the most immediate theorem payoff: the
audit either removes that qualifier or identifies a new quartic candidate.
An exploratory degree-five/six packet is chart-local, and its main quartic
verifier fails both a `tau=0` expected-resultant assertion and a 28-nonzero-
minor assertion (the exact count is 19); neither fact changes the quartic
theorem status.
The newer structural packet fully replays the squarefree binary-cubic
quintic exclusion and, conditionally, two sextic cores. An aligned quintic
specialization remains open; there is no global degree-five/six exclusion.
Its interaction
with Lane 5 may replace some chart work only if the budget is intrinsic to
the full left-right orbit.
[Exact Program 2 frontier and consistency anchors](../../research/handoffs/minimum-degree-and-quartic-exclusions.md#4-the-live-frontier).

<a id="lane-5-degree-budgets"></a>
### Lane 5 — Intrinsic degree and valuative budgets

Bridge finite-cover or boundary data to ordinary degree. The invariant object
is the embedded inclusion `iota:A=k[u1,u2,u3] -> B=k[x1,x2,x3]`, modulo source
and target automorphisms, not the abstract image algebra. Write `d_LR(iota)`
for the minimum displayed coordinate degree on that full orbit.

For a fixed source automorphism `sigma`, let

```text
F_d^sigma A = {a in A : deg sigma(iota(a)) <= d},
C_d^sigma   = k[F_d^sigma A].
```

The existing `delta(Q) <= 9` certificates concern only the listed normalized
filtrations and should be read as `trdeg_k C_6^sigma <= 2` for those cases.
Their case inventory, `delta(Q)` definition, localizations, and artifact
locators still need a public certificate contract. The unramified
`delta(Q) >= 10` family is a residual family, but closing it alone would not
prove orbit-minimality without a coverage theorem for arbitrary source
coordinate frames.

A new exact criterion makes the missing quantifier explicit: if
`d_LR(iota) <= D`, then `C_D^sigma=A` for some `sigma`, because a degree-`D`
target coordinate frame lies in `F_D^sigma A`. Hence a universal bound
`trdeg_k C_D^sigma <= 2` for every source automorphism would imply
`d_LR(iota) >= D+1`. At `D=6` this would prove orbit-minimal degree seven for
the fixed map, not a lower bound for every Keller counterexample.

There is also an exact valuative minimax formula. For divisorial valuations at
infinity, `delta_v(f)=max(0,-v(f))`, and coordinate frames `x'` and `u'`,

```text
deg_x' iota(u') =
  sup_v max_j delta_v(iota(uj')) / max_i delta_v(xi').
```

Minimizing over source and target frames gives `d_LR(iota)`. All valuations
give equality but are ineffective. The live geometric task is to extract a
smaller source-equivariant family from the embedded finite cover and affine
opening whose resulting lower bound exceeds six. Fixed compactification
valuations must be rejected if triangular shears dilute them.

The focused Lane 5 page now supplies the proof of the orbit criterion, the
valuative formula, a simplex/Rees collapse lemma, mandatory shear tests, and
four exact task capsules. The companion/Jordan divisor budget remains a
presentation-sensitive Program 2 audit lens rather than an orbit invariant.

<a id="lane-6-homogeneous-compression"></a>
### Lane 6 — Homogeneous realization and compression

Determine the true realization complexity of the fixed three-sheeted cover,
not merely current presentations. The newest exact packet controls all 109
source row-killers in a boundary-normal model, with first symbol in
`I^2/I^3`. Moving target gauge kills fixed quartic functionals, but the stored
quartic-null family leaves a degree-five class. Arbitrary target/stable
cancellation is open; the stronger v3 result is not fully rerunnable. The
open extension theorem for
collision monoliths and the `sl/sp` dichotomy may provide a conceptual lower
bound. Connections to Lane 5 are welcome if they produce invariants of the
cover rather than of one tensor presentation.
The independent 115-dimensional equivariant export eliminates one natural
22-dimensional affine tangent enlargement because its quartic functional is
identically \(1\). Its selected second-order rank-six section also stops at
cubic order: the complete 66-parameter quadratic tangent search has ranks
15 and 16 after augmentation. This remains a selected-plane, source-field
calculation, not a result about all tangent planes or the stable quotient.
[Exact Program 5 frontier](../../research/handoffs/homogeneous-descendants.md#4-the-live-frontier).

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
[Inputs, failed attempts, and exact Program 5 scope](../../research/handoffs/homogeneous-descendants.md#4-the-live-frontier).

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
[Exact Program 6 frontier](../../research/handoffs/plane-boundary-obstructions.md#4-the-live-frontier).

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
The Lane 9 toolkit's six tests pass but lacks its matrices, actual `F_2`
blocks, and archived `C9` replay; its averaging lemma gives no obstruction.
[Draft PR 1](https://github.com/nmonson1/guide-to-jacobian-conjecture/pull/1)
separately recovers filtered-operation/Program 6 tooling; at its current
head twelve package tests and the thirty Program 6 research-note tests pass.
It still proves neither complete-chain admissibility nor global attachment.
[Exact Program 6 frontier](../../research/handoffs/plane-boundary-obstructions.md#4-the-live-frontier).

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
| 5 | Lane 5 `L5-T1` certificate contract, `L5-T2` source-frame coverage, `L5-T3` canonical valuation family, `L5-T4` residual unramified theorem |
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

[Back to the research overview](../../research/index.md)
