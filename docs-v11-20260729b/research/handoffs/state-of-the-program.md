---
title: "Model research brief — State of the Jacobian Research Program"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Cross-program</p>
# State of the Jacobian Research Program

**Research state:** 29 July 2026, Pacific time.

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

## 3. What is proved (statements only; proofs at the locators)

| Program | Current anchor result | Where |
| --- | --- | --- |
| Base map | The known map has generic degree three with fiber sizes `3,1,0` across the discriminant stratification. | [`JCG-55104EF2`](../../claims/JCG-55104EF2.md) |
| 1 | Every generic-degree-three Keller map has a finite normal cubic cover with rank-two reflexive trace-zero module, locally free away from finitely many points; divisorial sheet loss has types `U1/U2/B`. | [`JCG-C04524CF`](../../claims/JCG-C04524CF.md), [`JCG-1D7EF048`](../../claims/JCG-1D7EF048.md) |
| 2 | The three-dimensional minimum ordinary degree satisfies `4 <= D_min <= 7`; broad quartic strata are excluded, while explicit triple-ramification and fixed-component frontiers remain. | [`JCG-6747671C`](../../claims/JCG-6747671C.md), [Program 2 handoff](minimum-degree-and-quartic-exclusions.md) |
| 3 | The degree-seven transverse germ is reduced-isolated and has completed local algebra of length 584; a marked-root model independently reconstructs it through order four. | [`JCG-7A91920F`](../../claims/JCG-7A91920F.md), [`JCG-DD13AC0E`](../../claims/JCG-DD13AC0E.md), [`JCG-E4FFD82B`](../../claims/JCG-E4FFD82B.md) |
| 4 | Cubic-frame stable equivalence is classified by decorated Artin boundary data across all multiplicities; the bounded categorical and fppf quotients are distinct objects. | [`JCG-E48F1FF0`](../../claims/JCG-E48F1FF0.md), [`JCG-66049841`](../../claims/JCG-66049841.md), [`JCG-4D953715`](../../claims/JCG-4D953715.md) |
| 5 | The credited 11-variable input has a 19-variable cubic-homogeneous descendant, a 38-variable Hessian descendant, and a fixed-tensor pairing interval `52 <= N_pair <= 110`; all present the same three-sheeted cover. | [`JCG-38CAAB66`](../../claims/JCG-38CAAB66.md), [`JCG-301AAE68`](../../claims/JCG-301AAE68.md), [`JCG-263402AA`](../../claims/JCG-263402AA.md), [`JCG-8AA6A8C5`](../../claims/JCG-8AA6A8C5.md) |
| 6 | The stored degree-21 terminal model is excluded through layer seven after a necessary adjacent-chart transition; the global interpretation retains an upstream exhaustiveness dependency. | [`JCG-9667172F`](../../claims/JCG-9667172F.md), [`JCG-BCEB7F45`](../../claims/JCG-BCEB7F45.md), [`JCG-9D0BE662`](../../claims/JCG-9D0BE662.md) |

Two cross-program assertions require special caution. The cubic-frame graph
records degree eleven as the first ordinary degree with a positive-dimensional
stable modulus ([`JCG-CA01A7A7`](../../claims/JCG-CA01A7A7.md)); it has proof
offered but no independent review and needs a precise proof locator before
use. The public degree-below-125 plane theorem is credited external context;
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

The public guide separates three fields: mathematical status, proof access,
and independent review. Exact scripts certify identities, ranks, finite
eliminations, or listed certificates. Conventional geometric arguments live
in the papers. Neither field automatically supplies independent review.

The technical release includes complete supplements for all six programs and
focused materials for major continuations. The claim pages carry stable tags
and proof-access status. The handoff pages compress this graph into a working
frontier but introduce no substitute source of truth.

Every returned research result must re-enter through the ordinary intake and
claim-review pipeline before it changes a paper or public claim. Literature
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
  the claim graph and review pipeline.
- Do not announce the working program as independently verified or
  submission-ready.

[Back to the research overview](../index.md)
