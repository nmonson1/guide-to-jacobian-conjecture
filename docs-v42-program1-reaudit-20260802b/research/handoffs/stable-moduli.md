---
title: "Model research brief — Stable Moduli"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 4</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 2 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v15 · site release <code>living-guide-public-v42-program1-reaudit</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/programs/stable-moduli.md).

!!! tip "Current proof sources — preferred"
    Use the [current source text and exact labels](../proof-sources/04-stable-moduli/main.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.

# Program 4: Stable Moduli
**Research state:** mathematical checkpoint 29 July 2026. Exact scope,
dependencies, and direct proof-body links are stated per input below.

**Actor guidance:** quotient, Torelli, and gluing arguments -> online model;
low-length invariant modules and cocycle tests -> local symbolic system;
core invariant reproduction -> independent CAS.

This is the complete public handoff. The linked
[working paper](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf),
[claim graph](../../results/all-claims.md), and
[Program 4 technical materials](../../evidence/materials.md#4-stable-moduli)
provide deeper proof and replay access. No download bundle or private
conversation is required to understand the tasks.

## 1. Setup and notation

The program studies when explicit nonproper Keller maps remain inequivalent
after arbitrary polynomial source and target automorphisms and after adding
identity coordinates. The central family is the normalized cubic frame

```
A_alpha(c) = c + alpha*c^2,
B_alpha,beta(c) = -2 - 4*alpha*c + beta*c^2.
```

For `alpha != 0`, the ratio

```
q = beta / alpha^2
```

is a complete invariant under polynomial left-right equivalence and affine
stabilization. The line `alpha=0` is one ordinary orbit and is stably
distinct from every nonzero-`alpha` member. Thus the result concerns genuine
fixed-generic-degree moduli, not merely the familiar fact that generic degree
can vary.

The general fixed-frame object is encoded by a pair of polynomials `A(c),
B(c)` with a retained root at infinity. The finite boundary scheme is

```
Z_A = Spec C[c]/(A/c),
```

decorated by the residue class of `B`. Multiplicities and common roots are
recorded by the weighted relative-Jacobian divisor. The all-multiplicity
Torelli statement says that, for admissible cubic frames, equality of this
decorated Artin data up to scaling is equivalent to ordinary and stable
left-right equivalence. It is a theorem on the fixed-frame locus; it is not
a classification of arbitrary Keller maps.

At a coefficient bound `N`, root translations act through a bounded
translation groupoid. A single polynomial map presents its kernel pair. The
program distinguishes three quotient-like objects that must not be merged:

1. the **categorical quotient**, whose invariant algebra is a differential
   kernel and whose global functions are controlled by the one-root wall;
2. the **fppf orbit quotient**, which is not algebraic along a rank-one wall;
3. **candidate weighted graph closures**, intended to give separated
   finite-type spaces of degeneration directions near an escape wall.

If constructed, the third object would not be a repaired orbit quotient. It
would record how an orbit degenerates, not all fppf equivalences. Likewise the boundary stack
`[U_N/G_m]` is framed or rigidified; it is not automatically the full
unrigidified left-right groupoid.

### Provenance and novelty boundary

The marked-simple-root construction itself is public input, not a result of
this program: [Jiang](https://x.com/davikrehalt/status/2079175065695035442)
gave the projective symmetric-product formulation, and
[Lou](https://aaronlou.com/jacobian_counterexample_derivation.pdf) gave an
independent factorization--resultant derivation and explicit affine chart.
[Tao](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
and [Ulam](https://www.ulam.ai/research/jacobian.pdf) developed public
expositions and inverse-cubic/base-map geometry.

Independent base-map results include Giannini's exact degree, image,
discriminant--Jelonek, and `S_3` calculations
([record](https://zenodo.org/records/21461572)); Santibáñez-Leal later gave
another exact validation, an infinite family, and escape analysis
([record](https://zenodo.org/records/21522076)).
[Shaska](https://arxiv.org/abs/2607.20210) studies the graded-equivariant
structure; it is related work, not a prior unrestricted stable left-right
quotient.

The candidate original contribution begins with completeness of `q` under
arbitrary polynomial left-right equivalence and every affine stabilization,
then the fixed-frame decorated-boundary classifications below. A July 30
public-record search found no earlier proof of those statements. That
negative search is not a correctness receipt and cannot exclude private,
unindexed, or later work.

When one root escapes to infinity, an explicit elementary transition relates
the length-`N` chart to a lower-length chart plus a contracted weight-two
gauge direction. Simultaneous escapes, the nonunit-resultant boundary,
scaling compatibility, and intrinsic relative-Jacobian gluing remain open.

### Coverage rule

Each numbered input states its exact scope. The proof-signature table records
dependencies and boundary exits, with direct links to every proof or proposed
construction.

### Compact glossary

- **Decorated Artin boundary:** `(Spec C[c]/(A/c), B mod A)` with scaling;
  multiplicities are retained, not reduced away.
- **Relative-Jacobian blowup:** intrinsic modification of the discriminant
  over the recovered `c`-line; its finite-root chart records the weighted
  divisor used in all-multiplicity Torelli.
- **Categorical quotient:** spectrum of invariant functions; it need not
  represent or separate fppf orbits.
- **fppf orbit sheaf:** sheafification of actual bounded translation orbits;
  it is nonalgebraic at the rank-one wall.
- **Weighted graph closure candidate:** proposed separated space of
  degeneration directions; its local construction still needs a complete
  definition and proof, and it would be neither preceding quotient.

### Case and dependency map

```text
cubic-frame boundary data
├─ all deleted roots finite
│  ├─ coprime/squarefree interior ── decorated-scheme Torelli
│  └─ common roots/multiplicities ── relative-Jacobian Torelli
└─ roots escape to infinity
   ├─ one root ── lower-length chart × contracted gauge line (explicit)
   └─ simultaneous roots / nonunit resultant ── gluing open

bounded translations at a wall
├─ invariant functions ── categorical differential kernel
├─ actual fppf orbits ── nonalgebraic
└─ degeneration directions ── weighted graph closure candidate
```

## 2. Goal and payoff

The immediate goal is to give the local weighted graph boundaries a global
universal property. The theorem should specify a degeneration functor,
prove that the local closures glue on overlaps, and state which information
is retained: orbit class, categorical invariant, or degeneration direction.

A successful gluing theorem would turn the current collection of explicit
walls into a usable compactification of cubic-frame degeneration data. It
would also clarify how the finite-root Torelli invariant behaves as roots
escape to infinity and how different boundary lengths meet.

The larger payoff is an intrinsic boundary-Torelli program. The current
fixed-frame theorem shows that decorated finite boundary data classifies a
large locus. Extending that result beyond the frame would make boundary data
a genuine coordinate system on part of the Keller quotient. This is related
to, but distinct from, recovering the open immersion of affine space from a
finite cover. The latter is an affine-space recognition problem and should
not be hidden inside the definition of a boundary object.

A secondary payoff is the modulus-onset invariant `D_mod`: the least degree
at which every neighborhood of the normalized counterexample meets
infinitely many left-right classes. The public graph asserts a degree-eleven
threshold inside the cubic-frame family, but that assertion needs a proof
locator and targeted independent reproduction before it can support a paper.

## 3. Reusable inputs, exact scope, and proof access

| # | Exact input and hypotheses | Claim · direct proof body |
| --- | --- | --- |
| 1 | In the quadratic cubic-frame slice, for `alpha != 0`, `q=beta/alpha^2` is complete under arbitrary polynomial left-right equivalence and affine stabilization; the entire `alpha=0` line is one separate orbit. | [`JCG-0F9A20C0`](../../claims/JCG-0F9A20C0.md) · [proof](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf#page=2) |
| 2 | For coprime admissible cubic frames with fixed finite boundary length, stable equivalence equals ordinary equivalence and is classified up to scaling by `(Z_A,B|Z_A)`; `A` need not be squarefree. | [`JCG-B858C93E`](../../claims/JCG-B858C93E.md) · [proof](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf#page=12) |
| 3 | For admissible cubic frames with `A/c` nonconstant, the same fixed-frame Torelli conclusion holds across common roots and multiplicities, with the weighted relative-Jacobian divisor recovering the multiplicities. | [`JCG-E48F1FF0`](../../claims/JCG-E48F1FF0.md) · [proof](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf#page=16) |
| 4 | Proposed rigidified model: `[U_N/G_m]` is a smooth Deligne--Mumford stack of dimension `2N-1` whose geometric points classify the stated coprime length-`N` boundary data. It is not the full unrigidified left-right groupoid and is not used as a proved gluing theorem. | [`JCG-046E56A8`](../../claims/JCG-046E56A8.md) · [exact recorded statement](../../assets/proof-archives/04-boundary-rigidity-stable-moduli-2026-07-22-v8.pdf#page=33) |
| 5 | At a fixed coefficient bound `N`, the degree-preserving root-translation relation is the kernel pair of the single bounded map `Theta_N`; its quotient coordinates separate finite-root decoration from the principal part supported at infinity. | [`JCG-2F2C2F29`](../../claims/JCG-2F2C2F29.md) · [proof](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf#page=23) |
| 6 | For a finite projective module `E` and translation kernel `K=ker V(M)`, the categorical invariant algebra is the relative differential kernel displayed in the paper; for the cubic-frame family its homogeneous functions are controlled by the single one-root wall. | [`JCG-66049841`](../../claims/JCG-66049841.md) · [proof](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf#page=23) |
| 7 | Over a DVR and **for `e >= 1`**, the rank-one wall `K_e=Spec R[s]/(pi^e s)` has nonalgebraic fppf orbit sheaf; consequently the bounded cubic-frame fppf quotient fails algebraicity along its generic one-root wall. At `e=0`, `K_0` is trivial and the quotient is algebraic. This result does not apply to the categorical quotient or a graph closure. | [`JCG-4D953715`](../../claims/JCG-4D953715.md) · [v13 theorem; its displayed statement still omits the `e>=1` qualifier](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf#page=24) |
| 8 | **Proposed, not yet proved here:** the expected one-root graph closure is `Bl_(epsilon^(N+2),y)`, and the displayed weighted principal-part projectivization is a candidate for an `m`-fold escape. The current paper does not define the base, generic quotient coordinate, graph map, and family-valued functor sufficiently to audit these assertions. | [`JCG-62905FD2`](../../claims/JCG-62905FD2.md) · [current candidate paragraph](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf#page=24) |
| 9 | In the displayed quartic-frame family, the normalized residual discriminant and conductor recover `(rho,sigma)`; equality of these parameters is exactly stable left-right equivalence, giving an affine plane of fixed-degree stable moduli. This is restricted to that family. | [`JCG-6B08BDE5`](../../claims/JCG-6B08BDE5.md) · [proof record](../../assets/proof-archives/04-boundary-rigidity-stable-moduli-2026-07-22-v8.pdf#page=33) |
| 10 | For the exceptional quadratic member `q=-2`, the weighted relative-Jacobian divisor has intrinsic vertical multiplicity exactly two, which separates the exceptional stratum uniformly. | [`JCG-7FB01BFA`](../../claims/JCG-7FB01BFA.md) · [proof](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf#page=17) |

### Proof-signature index

| Inputs | Proof signature / reusable output | Boundary exits |
| --- | --- | --- |
| 1, 10 | Compute the intrinsic nonproperness divisor `D_q ∪ P`; normalize `D_q` to `A^2_(c,t)` and mark its singular preimage `L_q` and plane intersection `M`. Unique factorization on every affine cylinder forces the pulled-back coordinates and recovers `q`; the `q=-2` incidence is separated by the singular intersection and then by vertical multiplicity two. Explicit source/target shears gauge `alpha=0`. **Output:** stable `q` invariant including the exceptional stratum. | This proves the quadratic slice, not all frames. |
| 2–3 | Compactify roots in projective incidence and divide the cubic discriminant by its coefficient content. Blow up the relative Jacobian; its finite-root chart is `A^2_(c,t)` with divisor `rho(c)H_0(c,t)^3`. Horizontal order `p` and vertical order `d` recover the common multiplicity, then coefficient comparison recovers `A` and `B mod cA`; explicit root translation proves sufficiency. **Output:** all-multiplicity fixed-frame Torelli. | The number of finite roots is fixed; infinity transitions remain outside the theorem. |
| 4 | Parameterize coprime length-`N` coefficient data and quotient the residual scaling action; smoothness and finite stabilizers give the stated rigidified Deligne--Mumford stack. **Output:** a fixed-length framed moduli chart. | It is not the unframed stable left-right quotient. |
| 5 | Divide by the monic coefficient polynomial: uniquely write `P=z^m P_d+Q_d S`. Multiplication by `Z^N` kills exactly the principal part, so one bounded map presents the translation kernel pair. **Output:** finite-root decoration plus escaping principal-part coordinates. | Presentation of bounded translations does not supply a global compactification. |
| 6 | Differentiate invariant polynomials and project to `coker(M^vee)`; conversely integrate coefficientwise along translations. A Cohen--Macaulay support/intersection argument shows the generic invariant algebra is controlled by the one height-one wall. **Output:** one finite syzygy map in every homogeneous degree. | Do not use the withdrawn reflexivity shortcut. |
| 7 | For `e>=1`, reduce the wall to `K_e=Spec R[s]/(pi^e s)` over a DVR. Its orbit functor is `B/Ann_B(pi^e)`; a standard fiber-product test maps diagonally rather than surjectively, violating strong Rim--Schlessinger. **Output:** a rank-one nonalgebraicity witness. | `e=0` is excluded; this says nothing against the categorical quotient or a graph closure. |
| 8 | Candidate signature only: define the generic quotient coordinate and graph map, then test whether its closure is `Bl_(epsilon^(N+2),y)`; for an `m`-fold escape, test the proposed weighted projectivization. | The local identification itself, pairwise/triple overlaps, scaling, and nonunit resultants all require proof. |
| 9 | Normalize the quartic-frame coefficients; singular/cusp and double-double strata of the residual discriminant and the conductor divisor `2L+Q` intrinsically recover `(rho,sigma)`. **Output:** an affine plane of fixed-degree stable moduli. | Restricted quartic family; no claim about the full Keller quotient or modulus-onset threshold. |

## 4. The live frontier

**(F0) Proof hardening after the v13 audit.** A full model-generated audit
found no counterexample to the main stable-classification theorem, but it is
not a human review receipt. A 31 July continuation independently found the
proposed incidence, empty-boundary, `S_3`, and Cohen--Macaulay repairs sound
at model level; the all-multiplicity proof is coherent after making the
intrinsic blowup chart scheme-theoretic. The subsequent recovery pass
integrated the remaining expanded repairs into the working source: the empty
deleted-scheme branch, Rees chart and full multiplicity chain, exact
conductor proof, `S_3` argument, all-order formal induction, and complete
bounded-groupoid, Cohen--Macaulay-support, and Rim--Schlessinger arguments.
A bounded replacement verifier passes all fifteen finite identities, and
Paper 4 passes its recursive source check and a warning-free Tectonic 0.16.9
build. The interrupted version-1 checker did not complete and is not counted
as evidence. The live F0 gate is now specialist review of the geometric
arguments, not another model rewrite.

**(F1) Define the local graph models, then glue them.** The one-root wall and
length-`m` principal-part coordinates are explicit. The recovered fixed
multigraph theorem is valid as a closed coefficient substack of a product of
weighted projective stacks, hence proper and separated; only pullback of its
fixed equations, not recomputed graph closure, commutes with arbitrary base
change. The coarse one-root graph is locally
`Bl_(epsilon^(N+2),y)`, with exact Rees checks through `N=3`.

Two new exact coefficient-side packets now give F1 better test objects. The
Program 4 packet constructs ordered and normalized multigraph models, a
12-equation saturated `N=3` Cox graph, and an `N=3` fan refinement with 66
simplicial cones covering all 28 original cones and retaining all 14 rays;
its portable checks replay. Independent Smith/Fitting tests pass for
`N<=3`; direct and ordered charts differ by `Bl_(u^2,v)`; and the triple
cocycle passes only on the coprime exact overlap. The Lane 2 packet also
replays a recursive principal-parts law and an `m=3` common-factor atlas.
Next prove simultaneous relative-Jacobian flattening or test a noncoprime
triple collision. These are not a stable-quotient or global Rees--Jordan
theorem; the referenced Rees--Jordan checker remains unrecovered.

**(F2) Intrinsic stable-equivalence gluing.** Coefficient-space orbit maps,
categorical functions, and graph closures do not prove that stabilized
relative-Jacobian geometry reconstructs equivalence across every infinity
wall. The finite-root Torelli theorem supplies the interior classification;
the frontier is compatibility across changing boundary length and
multiplicity.

The newest hidden-kernel analysis makes this distinction stricter, not
weaker. Its geometric comparison remains conditional on fixed-frame Torelli
and a boundary exact sequence, while an explicit dual-number hidden
automorphism shows that literal descent for the unrigidified family is false.
Any correct theorem must rigidify or retain that stack structure. A separate
conversation proposes formal left-right inertia and stabilized-automorphism
descriptions, but it has no attached independent proof receipt and belongs in
F0's audit queue.

**(F3) Low-length overlap tests.** Once a candidate transition law is
written, compute invariant modules, Smith/Fitting data, and triple-overlap
cocycles for small `N`. These tests can refute a proposed universal theorem
quickly. They support a theorem but cannot replace the gluing proof.

**(F4) Targeted verification for `D_mod`.** A Macaulay2 re-entry now checks
the two-parameter polynomial formulas, pole cancellation, frame identities,
Jacobian determinant `-2`, component degrees `(11,10,4)`, and the leading
degree inequalities below eleven. It does not prove `q` separation or the
global threshold theorem. The remaining gate is to reproduce the
`q`-separation invariant and pin the full proof of the asserted first
degree-eleven stable modulus in the cubic-frame family. The relevant local
definition uses pointed curves through `G`; ordinary degree is not an
invariant of an abstract left-right class.

**Last formula replay:** `2026-07-30`. The new SymPy audit reproduced
component degrees `(11,10,4)`, formal source-degree triples
`(19,17,19)`, `(37,35,37)`, `(55,53,55)`, and first occurrence of `q` at
formal order two. These are narrow formula checks, not proofs of F0 or F1.

Dependencies: F1 supplies transition maps for F3. F2 then asks whether the
coefficient compactification reflects intrinsic stable equivalence. F4 is a
separate verification gate and should not be bundled into the global gluing
theorem.

## 5. Graveyard (causes of death — read before proposing routes)

- **Reflexivity shortcut for the one-wall theorem.** The earlier inference
  that the relevant module was controlled merely by reflexivity was
  unsupported. The corrected proof uses a Cohen--Macaulay support argument.
  Do not cite the withdrawn shortcut.
- **Categorical quotient equals orbit space.** Invariants can fail to
  separate fppf orbits, and the actual bounded fppf quotient is nonalgebraic
  at the rank-one wall. The categorical quotient answers a functions
  question, not the full moduli question.
- **Graph closure repairs nonalgebraicity.** The graph closure parameterizes
  degeneration directions. It does not become the fppf orbit sheaf by being
  separated and finite type.
- **Framed boundary data are the full LR quotient.** Keeping a marked frame
  or `G_m` rigidification suppresses automorphisms. Any unframed conclusion
  needs a Torelli theorem, not a change of terminology.
- **One-root transition proves simultaneous gluing.** Several roots may
  escape at comparable rates, creating higher overlap conditions absent
  from the elementary wall.
- **Dimension count proves moduli.** Orbit dimensions and coefficient counts
  do not establish inequivalence. Stable separation requires an intrinsic
  invariant such as `q`, decorated boundary data, or a positive-genus
  boundary curve.

## 6. Tasks

Each item is a task capsule. T1 must define the functor before proposing a
space; T2 must wait for explicit overlap maps. If a low-length test breaks a
cocycle or separatedness claim, return the smallest exact counterexample and
the specific failed property instead of patching the theorem informally.

**P4-T1 — Independently harden the v13 proof chain.**

Actor: affine algebraic geometer plus cancellation/affine-geometry
specialist. Status: ready for human review.

*Inputs:* this page; the [Program 4 paper](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf);
the exact audit bundle; and the all-multiplicity, reciprocal-family, and
categorical-boundary appendices.

*Payoff:* supplies an independent correctness receipt for the now-expanded
working proof chain.

*Attack:* audit the projective incidence/open-immersion and proper-boundary
steps, the normalization lift and marked-cylinder cancellation, and the
scheme-theoretic relative-Jacobian reconstruction. Then check the conductor,
formal-recursion, categorical-support, and fppf-wall arguments against their
stated categories. Treat the exact scripts as identity checks, not geometric
proofs.

*Done when:* every theorem has a complete proof locator, every edge case is
owned, and its assumptions, edge cases, and remaining gaps are independently
checked and explicit.

**P4-T2 — Define and test the weighted graph boundary.**

Actor: `online_model` for the construction, then `local_symbolic` for
low-`N` tests. Status: ready for the definition step.

*Inputs:* the bounded root-translation groupoid, the candidate paragraph,
the categorical-wall checker, and the explicit one-root transition.

*Done when:* the base, generic coordinate, graph map, and degeneration
functor are explicit; the one-root blowup identification is proved; and
Smith/Fitting plus double/triple-overlap tests either support the proposed
gluing or exhibit the smallest exact counterexample.

**P4-T3 — Clear the modulus-onset verification gate.**

Actor: `independent_cas` plus proof audit. Status: ready.

*Done when:* the `q` invariant and uniform degree of the explicit family are
independently reproduced, and the degree-eleven threshold claim has an exact
public proof locator with its restricted-class scope visible.

## 7. Evidence and replay index

The Program 4 paper contains the `q` classification, general boundary
Torelli statements, quotient distinctions, and conventional geometric
arguments. The technical release contains exact checks for discriminants,
normalizations, conductor gradients, the exceptional `q=-2` geometry,
weighted-lift invariants, one-root transitions, differential-kernel
formulas, and rank-one wall examples.

Those calculations verify displayed formulas and low-dimensional examples.
They do not replace normalization lifting, stable-cylinder rigidity,
all-multiplicity component recognition, global gluing, or the
Rim--Schlessinger and support arguments used in the proofs.

The replay packet also contains the independent Macaulay2 formula/degree
check described in F4. Its audit contract is deliberately narrower than the
stable-moduli classification: it establishes the displayed formulas and
leading-degree calculation, not completeness of the `q` invariant.

The July 30 proof-audit packet is preserved at
`code/proof-audit-2026-07-30-v1/`. Its ZIP has SHA-256
`ffbcb8a4f8515c3f5c07aa85f870ed1cf736923bc08bcb845d1b5fe85a6932e8`.
The attached SymPy program replays successfully. The prose audit is a
model-generated evidence lead, not a specialist receipt; use it to target
P4-T1 and retain its distinction between definite statement defects,
plausible proof repairs, and unauditable constructions.

The July 30 multigraph/principal-parts calculations are additional design
evidence. They make low-`N` overlap and fan questions executable, but they do
not repair the missing comparison from coefficient geometry to intrinsic
stable equivalence. Preserve the unrecovered Rees--Jordan pair and the
dual-number descent failure as explicit boundary data.

The separate six-obligation packet is recovered on
[draft PR 2](https://github.com/nmonson1/guide-to-jacobian-conjecture/pull/2)
at `3f7abd98be74c078f3aca2641c3af5c7cf41c5c0`. Its nine-file
manifest and symbolic replay pass, and its `N=3` direct/iterated comparison
is a nontrivial blowup. It remains unrefereed and does not identify the
proposed degeneration stack with the full stable orbit quotient.

Use the [all-multiplicity Torelli package](../../collections/all-multiplicity-cubic-frame-torelli.md),
[categorical quotient package](../../collections/categorical-cubic-frame-quotient.md),
and [infinity-gluing frontier](../../collections/cubic-frame-infinity-gluing.md)
as the main proof-access route.

A useful returned gluing proposal should be testable before it is accepted as
a theorem. It should give coordinates on every local wall, explicit formulas
on pairwise overlaps, the action of scaling and finite permutations, and at
least one triple-overlap identity. It should also say which functorial base
changes are allowed and what happens when a resultant becomes a nonunit.
Without those data, “complete weighted collineations” is only an analogy.

Conversely, a low-`N` counterexample should be treated as structural
information: identify whether it breaks cocycle compatibility, separatedness,
finite type, or the proposed relation to intrinsic stable equivalence. A
repaired functor may still exist even when a particular compactification
does not.

The preferred output format is therefore a theorem/proposition pair: first a
precise representability or gluing statement for the degeneration functor,
then a comparison morphism to the categorical and orbit constructions with
its injectivity, surjectivity, and separatedness properties stated
independently. Include the one-root model as a worked local chart and at
least one simultaneous two-root example. If a finite permutation or hidden
automorphism changes the overlap, record it as stack structure rather than
quotienting it away informally. The same discipline applies to `D_mod`:
exhibit a pointed curve through the normalized map, verify its uniform degree,
and prove that its punctured neighborhoods meet infinitely many classes.

## 8. Do not do

- Do not identify categorical, fppf, and graph-closure quotients.
- Do not reuse the withdrawn reflexivity shortcut.
- Do not call a framed boundary stack the full stable left-right quotient.
- Do not descend the unrigidified family through hidden infinitesimal
  automorphisms; rigidify or record the stabilizer as stack structure.
- Do not infer simultaneous-escape gluing from the one-root chart.
- Do not cite the one-root blowup or weighted projectivization as proved
  until the base, coordinate, graph map, closure, and functor are defined.
- Do not omit `e>=1` from the rank-one wall theorem; `e=0` is a literal
  algebraic counterexample to the unqualified statement.
- Do not claim a universal property before defining the functor of families
  and proving overlap cocycles.
- Do not cite the degree-eleven threshold as verified until its locator and
  independent reproduction gate are complete.
- Do not represent symbolic sanity checks as proofs of the geometric gluing
  or stable-cylinder arguments.
- Do not call the exact `N=3` Cox/fan or tested principal-parts identities a
  global stable-quotient theorem.

[Back to the Program 4 overview](../../research/programs/stable-moduli.md)

[Back to the Program 4 overview](../programs/stable-moduli.md)
