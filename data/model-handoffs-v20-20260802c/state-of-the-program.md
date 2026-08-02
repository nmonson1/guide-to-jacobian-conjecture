# State of the Jacobian Research Program
**Research state:** mathematical checkpoint 2 August 2026. Exact scope,
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


**2 August mathematical refresh.** The nine focused pages now include the
selectively retained results from the latest lane investigations, link their
proof and computation boundaries, and move each ready task past what is now
known.  The six program dossiers remain deeper overlapping views.

## 4. The live frontier

The nine lanes partition attention, not mathematics.  The focused pages are
the current research briefs; the summaries here only identify each lane's
present gate.  Follow the focused page for its exact known mathematics,
hypotheses, dependencies, and deliverable contract.

Here *ready* means that the starting objects are displayed on the page or a
direct public input page and that the deliverable can be attempted without an
unpublished artifact.  *Blocked* names the missing input or mathematical
dependency.  In task IDs, `P` identifies the owning program and `L` the lane;
programs and lanes are overlapping views rather than the same numbering.

<a id="lane-1-cubic-flatness"></a>
### Lane 1 — [Cubic flatness and finite normalization defect](cubic-flatness-normalization-defects.md)

Compute the closed-point standard-isotypic saturation of the actual three
source-chart collision complex.  Vanishing is equivalent to cubic flatness.

<a id="lane-2-boundary-torelli"></a>
### Lane 2 — [Boundary completeness and Torelli at infinity](boundary-completeness-torelli-at-infinity.md)

Complete the exact quintic outer normalization on the two projective-infinity
charts over `T=0`; the finite charts and all-rank PRS theorem are supplied.

<a id="lane-3-deformation-moduli"></a>
### Lane 3 — [Bounded-degree deformation and modulus onset](bounded-degree-deformation-modulus-onset.md)

Either reconstruct the direct order-five Kuranishi calculation or sharpen the
proved stable-equivalence complexity of the quadratic-modulus family.

<a id="lane-4-quartic-endgame"></a>
### Lane 4 — [The quartic endgame](quartic-endgame.md)

Audit the supplied proof/code case tree and expose the first genuinely
uncovered quartic branch; the core terminal packets already replay.

<a id="lane-5-degree-budgets"></a>
### Lane 5 — [Intrinsic degree and valuative budgets](intrinsic-degree-valuative-budgets.md)

Prove the frame-covariance lemma and extend the supplied elementary and
separated-word degree-six exclusions to the next operation class.

<a id="lane-6-homogeneous-compression"></a>
### Lane 6 — [Homogeneous realization and compression](homogeneous-realization-compression.md)

Upgrade the exact transverse and 60-direction tame source obstruction to the
missing target and stable-presentation quotient.

<a id="lane-7-collision-geometry"></a>
### Lane 7 — [Five-dimensional collision geometry](five-dimensional-collision-geometry.md)

Prove corank-two exclusion or grade six for the exact residual `10 x 5`
matrix, retaining the intrinsic Pluecker open for genuine markings.

<a id="lane-8-plane-newton-queue"></a>
### Lane 8 — [Plane Newton queue and terminal certificates](plane-newton-queue-terminal-certificates.md)

Route the full-support root of the exact public reconstruction program; the
truncated root is closed, while the stored transformed certificate lacks a
proved chart bridge.

<a id="lane-9-plane-global-attachment"></a>
### Lane 9 — [Plane chart correspondence and global attachment](plane-chart-correspondence-global-attachment.md)

Realize the supplied finite wall groupoid as an actual adjacent complete-chain
chart, or prove that its grading requires a corrected filtration or quotient.

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

| Lane | Current exact on-ramp |
| --- | --- |
| 1 | `P1-T1`: compute the actual collision saturation |
| 2 | `P4-L2A0`: projective completion of the quintic outer graph |
| 3 | `P3-L3A0` or `P3-L3D`: direct reconstruction or sharp stable complexity |
| 4 | `P2-L4A`: audit the supplied global leaf accounting |
| 5 | `L5-T1A`: abstract frame-covariance lemma |
| 6 | `P5-L6A0`: upgrade the 60-direction obstruction |
| 7 | `P5-L7A`: corank-two exclusion with the genuine-marking open |
| 8 | `P6-L8A`: route the full-support root and expose its first gap |
| 9 | `P6-L9A0`: realize the finite ambient wall groupoid |

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
