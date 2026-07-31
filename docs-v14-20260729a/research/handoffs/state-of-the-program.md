---
title: "Model research brief — State of the Jacobian Research Program"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Cross-program</p>
# State of the Jacobian Research Program

**Research state:** mathematical checkpoint 29 July 2026. Exact scope,
dependencies, and direct routes to the program proof bodies are stated below.

**Scope:** cross-program orientation for a model deciding where its work has
the highest leverage. Read the program-specific handoff before attempting a
task.

This page joins the six research programs without replacing their claim
pages or papers. The [research index](../index.md),
[stable claim catalogue](../../results/all-claims.md),
[working papers](../papers.md), and [proof index](../../evidence/index.md)
provide the authoritative details.

## 1. Setup and notation

The project starts from an explicit noninjective polynomial Keller map in
three variables. Its ordinary coordinate degrees are `(7,6,4)`, its generic
fiber degree is three, and the Galois closure has monodromy `S_3`. Ordinary
degree and generic degree are different filtrations and must never be
substituted for one another.

The claim graph organizes 355 public atomic statements into 102 grouped
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

## 3. Reusable anchors and proof routes

| Input | Proof signature / reusable output | Boundary exit | Exact statements and proofs |
| --- | --- | --- | --- |
| Base-map fiber stratification | Write the inverse cubic; simple roots reconstruct source points, its discriminant gives the double-root fiber, and the triple-root curve removes the final affine sheet. **Output:** the exact `3/1/0` fiber chart. | This is the named map, not arbitrary cubic covers. | [`JCG-55104EF2`](../../claims/JCG-55104EF2.md) · [Program 1 proof routes](cubic-marked-root-incidence-geometry.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P1 cubic anatomy | Normalize in the cubic function field; split trace as `O ⊕ E`; use completed valuations and inertia for `U1/U2/B`; reflexivity confines nonflatness to finitely many omitted values. **Output:** trace module plus divisorial sheet taxonomy. | Reflexivity does not kill isolated defects; opening is separate. | [Program 1 exact inputs and proofs](cubic-marked-root-incidence-geometry.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P2 quartic reductions | Expand the scaled determinant arc; stratify by leading target span; use valuations and Hilbert–Burch normal forms to route span two into ramification and fixed-component leaves. **Output:** an explicit quartic case tree. | Higher ramification, fixed components, and exceptional `F_4` compatibility remain. | [Program 2 exact inputs and proofs](minimum-degree-and-quartic-exclusions.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P3 length-584 germ | Cut the affine orbit slice; use torus attractors plus a nullcone lemma; match inverse-system and multiplication-matrix bounds; compare source-flow and determinant complexes through order four. **Output:** the length-584 Artin algebra and two compatible presentations. | No all-order source-flow theorem; degree eight has shear components. | [Program 3 exact inputs and proofs](local-rigidity-and-deformation-algebra.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P4 fixed-frame Torelli and quotients | Recover the intrinsic `(c,t)` chart from the relative Jacobian; read multiplicities; recover `(A,B mod A)` and lift by root translation. Separately compute categorical invariants and the fppf rank-one wall. **Output:** decorated Artin data plus noninterchangeable quotient objects. | Fixed-frame locus only; simultaneous infinity escapes remain. | [Program 4 exact inputs and proofs](stable-moduli.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P5 descendant ladder | Factor the cubic span and use a Schur complement for the 19D suspension; certify the long nilpotent chain; cotangent-double; bound pairing length by the commutant obstruction and explicit square-zero factorization. **Output:** 19D, 38D, and 110D presentations of one cover. | Bounds are for the fixed tensor; global minimality is open. | [Program 5 exact inputs and proofs](homogeneous-descendants.md#3-reusable-inputs-exact-scope-and-proof-access) |
| P6 stored terminal exclusion | Identify the layer-four kernel as a `k=4` rechart; force a common approximate root in the adjacent chart; close the remaining branches by exact affine/toric certificates. **Output:** no gluing for the stored degree-21 terminal system. | The below-125 implication is **open** pending upstream exhaustiveness. | [Program 6 exact inputs and proofs](plane-boundary-obstructions.md#3-reusable-inputs-exact-scope-and-proof-access) · open dependency [`JCG-9D0BE662`](../../claims/JCG-9D0BE662.md) |

Two cross-program assertions require special caution. The cubic-frame graph
records degree eleven as the first ordinary degree with a positive-dimensional
stable modulus ([`JCG-CA01A7A7`](../../claims/JCG-CA01A7A7.md)); use its
restricted cubic-frame hypotheses and direct locator before relying on it.
The public degree-below-125 plane theorem is credited external context;
the project's terminal certificates do not erase the upstream dependency.

## 4. The live frontier

**(F1) Targeted reproduction gate.** Independently reproduce the Program 3
degree-seven radical/reduced-rigidity certificate, the Program 4
`q`-separation invariant, the uniform ordinary degree of the explicit
two-parameter stable-moduli family, and the degree-eleven threshold. These
are targeted checks, not a demand to duplicate every project calculation.

**(F2) Cubic closure and anatomy.** Assemble a correctly scoped anatomy
theorem for any generic-degree-three Keller map: degree-three finite cover,
`S_3` monodromy, ramification confined to the deleted boundary, branch image
contained in (not necessarily equal to) the nonproperness set, finite nonflat
locus inside omitted values, and candidate conductor/inertia decoration.
Classifying that decoration is a Torelli theorem, not part of anatomy.

**(F3) Cubic flatness and boundary completeness.** Prove the finite defect
module vanishes using the rank-two reflexive trace-zero module, source
splitting, and omitted-value support. Separately prove the boundary opening
is complete. Together they connect generic-degree-three maps to the explicit
frame classification.

**(F4) Intrinsic orbit-minimum/degree-budget lemma.** Minimizing ordinary
degree among explicit cubic-frame moves is only a restricted-class theorem.
The master low-degree implication needs a lower bound over the full
polynomial left-right orbit, or a normalization procedure that reaches the
canonical frame without increasing degree. This is the missing arrow from
classification to degree bounds.

**(F5) Program 2 degree-four endgame.** Finish exceptional `F_4`
compatibility, higher ramification, fixed-component boundaries, and the
case-tree audit. This remains the main theorem-facing priority because it
would prove `D_min >= 5` or expose a new construction.

**(F6) Plane queue plus descent.** Certify the complete row/face queue,
prove the general chart-correspondence theorem, and keep these separate from
the already-exact terminal certificates. Continue the `F_2` attachment as a
two-sided obstruction/construction search.

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

Each item below is a **task capsule**: inputs are complete unless it says
blocked; “done when” is the acceptance contract. Stop and return an explicit
dependency ledger if a missing lemma changes the scope, and escalate any
persistent solution component as a construction lead rather than erasing it.

**X-T1 — Clear the targeted reproduction gate.**

Actor: `independent_cas` plus proof audit. Status: ready.

*Inputs:* the public Program 3 and 4 equations, stable claim pages, and
working-paper locators.

*Done when:* the degree-seven radical, `q` separation, uniform family degree,
and degree-eleven threshold are independently checked and each has an exact
public locator and scope.

**X-T2 — Write the generic-degree-three anatomy theorem.**

Actor: `online_model`. Status: ready after a literature refresh.

*Inputs:* Program 1 handoff and paper; classical finite-cover and Jelonek
statements, rechecked against primary sources before citation.

*Done when:* anatomy, Torelli, opening, and budget conclusions are visibly
separated; branch image is stated as contained in the nonproperness set; the
finite nonflat locus and source-splitting facts are included.

**X-T3 — Formulate the intrinsic degree-budget lemma.**

Actor: `online_model`. Status: ready as a formulation task.

*Payoff:* supplies the missing implication from canonical-frame degree to a
full left-right-orbit lower bound.

*Done when:* the statement quantifies over arbitrary polynomial source and
target automorphisms, identifies a valuative monotone or normalization
procedure, and makes no dimension-count inference.

**X-T4 — Execute program-specific priority work.**

Order: Program 2 degree-four endgame; Program 5 staged collision saturation;
Program 6 upstream audit/chart theorem; Program 1 cubic flatness externalized
as a local commutative-algebra problem; Program 3 degree-eight saturation as
a separately scoped follow-on.

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

- Do not start a task before reading its program-specific handoff.
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
