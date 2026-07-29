---
title: "Model research brief — Local Rigidity and Deformation Algebra"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 3</p>
# Program 3: Local Rigidity and Deformation Algebra

**Research state:** content checkpoint 29 July 2026, including the exact
rational order-six reconstruction. Verification and review status is stated
per input below.

**Actor guidance:** conceptual filtered deformation theory -> online model;
large exact row-space and rank calculations -> local symbolic system;
independent reproduction -> a genuinely separate CAS.

This is the complete public handoff. The [working paper](../../assets/manuscripts/03-filtered-rigidity-2026-07-22-v11.pdf),
[stable claim catalogue](../../results/all-claims.md), and
[Program 3 technical materials](../../evidence/materials.md#3-local-rigidity-and-deformation-algebra)
are linked for proof and replay access. No private transcript is needed.

## 1. Setup and notation

Let `K_{3,7}` be the finite-type coefficient scheme of normalized polynomial
maps `H: A^3 -> A^3` satisfying

```
deg H <= 7,      H(0)=0,      JH(0)=I,      det JH=1.
```

Fix the normalized degree-seven counterexample `G`. The normalized affine
source action has dimension eleven. Eleven coefficient conditions cut a
torus-stable affine slice `S` transverse to that orbit; its completed local
ring at `G` is denoted `R`. The theorem is about this **degree-bounded,
affine-quotiented transverse germ**. It is not a claim that every formal
deformation of `G` is absent, nor that no degree-increasing family exists.

The determinant differential leaves a ten-dimensional transverse tangent
space with weights

```
(-1, 2, -3, -2, -1, 0, 1, 1, 2, 3).
```

The Kuranishi equations are the higher compatibility conditions obtained by
expanding `det J(G+H)=1` in these parameters. Because the torus weights mix
signs, the tangent cone alone does not prove isolation. The reduced theorem
uses separate exact calculations on the positive attractor, negative
attractor, and fixed locus, followed by a torus-nullcone lemma.

Scheme-theoretically the point is highly nonreduced. The completed Artin
algebra has length `584`, Hilbert function

```
(1, 10, 44, 108, 157, 145, 86, 30, 3),
```

and maximal ideal `m` satisfying `m^9=0` and `m^8 != 0`. Length 584 is a
transverse intersection multiplicity, not a count of 584 nearby polynomial
maps. A Macaulay inverse system gives a dual description; its 60 minimal
contraction generators show that `R` has Cohen--Macaulay type 60 and is not
Gorenstein, level, or a complete intersection.

There are two constructions of the equations. The **direct determinant
model** expands the bounded coefficient scheme. The **marked-root source-flow
or root/Rees model** begins with the marked-root volume form and a
weighted-divergence equation. They agree exactly through parameter order
four. The second direct implementation is exact through order six and
extracts the unique new sextic initial class, but the root/Rees comparison
has not yet reached orders five through eight.

Degree eight is a separate frontier. Source quadratic `z`-shears already
give genuine degree-eight families, and target shears add known components.
After quotienting those directions, a residual weight `-1` sector survives
to fourth order. The appropriate question is orbit saturation of the reduced
germ by the known shear and affine components, not whether the reduced germ
is a single point.

### Coverage rule

This handoff specifies the moduli problem, accepted calculations, and next
tasks. “Accepted as project input” permits using an exact cited result at its
scope; it does not turn a certificate into peer review. No Program 3 claim
below has independent review recorded, and related Python/SymPy/FLINT
implementations are not an independent-CAS reproduction.

### Compact glossary

- **Transverse slice:** eleven affine orbit conditions removed from the
  degree-bounded coefficient scheme; every rigidity claim here refers to
  this chosen quotient problem.
- **Reduced isolation:** the radical local germ is a point; it does not say
  the local ring is reduced.
- **Kuranishi ideal:** compatibility equations in the ten transverse tangent
  parameters after gauge is removed.
- **Inverse system:** contraction-stable dual module giving a lower bound on
  the Artin-algebra length and its type.
- **Border presentation:** standard monomials plus multiplication matrices;
  it supplies the matching upper bound when the matrices commute.

### Case and dependency map

```text
formal deformations of G
├─ unrestricted degree ── formally right-trivial
└─ degree-bounded coefficient scheme
   ├─ degree 7 transverse slice
   │  ├─ reduced germ ── point (torus attractors + nullcone)
   │  └─ nonreduced algebra ── length 584
   │     ├─ direct determinant model ── complete
   │     ├─ second direct reconstruction ── exact through order 6
   │     └─ root/Rees source-flow model ── matched through order 4
   └─ degree 8
      ├─ affine/source/target shear components ── known
      └─ residual weight -1 saturation ── open over characteristic zero
```

## 2. Goal and payoff

The principal goal is an independent conceptual and computational
reconstruction of the length-584 algebra. A successful all-order
source-flow theorem would explain why the determinant equations have their
observed weights and generators instead of merely reproducing a large exact
matrix calculation.

The next finite goal is to continue the second exact reconstruction through
orders seven and eight. That would give a second complete rational route to
the length and terminal layers. A separate, genuinely independent CAS pass
over the degree-seven radical/reduced-rigidity certificate is a release gate:
the existing exact programs are strong but belong to one related
Python/SymPy/FLINT computational family.

The broader payoff is a precise **modulus-onset** problem. Degree seven is
reduced-rigid after the affine quotient; degree eight already contains
coordinate families; by degree eleven a positive-dimensional stable modulus
is asserted elsewhere in the graph but needs a proof locator and independent
verification. Understanding the degree-eight saturated germ is the difficult
lower-bound side of that transition.

## 3. What is proved and accepted as project input

Items 1 and 7 are `proof offered`; 2, 4, 8, and 9 are `certificate
offered`; 3, 5, and 6 are `recorded`; item 10 is `evidence only`. These are
project evidence labels, not independent review.

| # | Statement | Where |
| --- | --- | --- |
| 1 | Every unrestricted formal Keller deformation of `G` is formally right-trivial; degree-bounded obstructions come from the degree filtration. | [`JCG-30FC31CC`](../../claims/JCG-30FC31CC.md); paper formal-orbit section |
| 2 | In the specified degree-seven transverse slice, an exact standard-basis calculation makes the local ideal `m`-primary, so the reduced formal/analytic germ is a point. | [`JCG-7A91920F`](../../claims/JCG-7A91920F.md); paper reduced-rigidity theorem |
| 3 | The completed local algebra has length 584, Hilbert function `(1,10,44,108,157,145,86,30,3)`, and Loewy length nine. | [`JCG-DD13AC0E`](../../claims/JCG-DD13AC0E.md); paper local-algebra theorem |
| 4 | An exact border presentation has 584 standard monomials, 2,654 border relations, and ten commuting rational multiplication matrices. | [`JCG-F4C59FA0`](../../claims/JCG-F4C59FA0.md) |
| 5 | The inverse system has 60 minimal contraction generators; the algebra has type 60 and is neither Gorenstein, level, nor a complete intersection. | [`JCG-6FA7D42B`](../../claims/JCG-6FA7D42B.md) |
| 6 | The minimal Kuranishi ideal has 36 generators: 11 quadratic, 13 cubic, 11 quartic, and one sextic. | [`JCG-525A42DB`](../../claims/JCG-525A42DB.md) |
| 7 | The independent marked-root source-flow construction agrees with the direct determinant complex through order four, reproducing the Hilbert prefix and generator counts. | [`JCG-E4FFD82B`](../../claims/JCG-E4FFD82B.md); source-flow appendix |
| 8 | The exact rational second direct calculation gives `H(5)=145`, `H(6)=86`, and order seven contribution 30; the order-six calculation isolates the unique new weight-three sextic class. | [`JCG-D1903700`](../../claims/JCG-D1903700.md), [`JCG-525A42DB`](../../claims/JCG-525A42DB.md); order-six appendix |
| 9 | At degree eight the tangent kernel has dimension 44, leaving 33 directions after the affine orbit, including three source quadratic-shear and two target-shear families. | [`JCG-891B0275`](../../claims/JCG-891B0275.md); degree-eight appendix |
| 10 | In the residual degree-eight slice, weight `-2` is eliminated over `Q`; weight `-1` survives to fourth order and has only modular death evidence later. | [`JCG-D3F76EBC`](../../claims/JCG-D3F76EBC.md) |

The exact calculations establish their named algebraic facts. They do not by
themselves validate the choice of moduli problem, the slice interpretation,
or the passage from a modular rank to a characteristic-zero theorem unless a
separate rational certificate is stated.

### Proof-signature index

| Inputs | Proof signature / reusable output | Boundary exits |
| --- | --- | --- |
| 1 | Use the formal étale inverse of `G`: for a Keller deformation `H`, set `phi=G^{-1}∘H`; then `H=G∘phi` and `det Dphi=1`. **Output:** formal right-triviality before imposing a degree filtration. | `phi` may have unbounded degree, so this does not settle the bounded slice. |
| 2 | Recover the affine stabilizer from the omitted curve and trivial cubic deck group; certify an eleven-by-eleven orbit minor; apply an étale-slice argument. On the ten torus weights, compute exact positive, negative, and fixed ideals containing pure powers/nonzero cubics; a torus-nullcone lemma excludes every mixed branch. **Output:** reduced isolation in the named slice. | Slice choice and affine quotient are hypotheses, not outputs of the certificate. |
| 3–4 | Build 584 standard monomials and commuting rational multiplication matrices for the upper bound. Independently construct exact rational dual classes/inverse-system contraction closure for the lower bound; order-nine determinants kill further layers. **Output:** length 584, Hilbert function, and a replayable algebra representation. | A modular minor proves only the rank direction it supports; deficient blocks need rational relations. |
| 5–6 | Start from 60 divided-power generators, close under contraction, and apply Nakayama to get type 60. Filter exact Kuranishi classes and use first Koszul homology to minimize them to `11+13+11+1` generators. **Output:** inverse-system type and the 36-generator profile. | These describe the completed transverse algebra, not global families of maps. |
| 7 | Express marked-root coordinates and the volume form, linearize by weighted divergence, and filter through the Rees degree. Build determinant and source-flow row spaces independently and identify them through order four; native homotopies, not frozen representatives, give the matching gauge. **Output:** a geometric model of the first Kuranishi layers. | Agreement through order four is not an all-order equivalence theorem. |
| 8 | Decompose orders five and six by weight; certify full-rank blocks with modular maximal minors and deficient blocks with exact rational relations. The quotient `I/mI` gains one weight-three sextic. **Output:** exact Hilbert values 145 and 86 plus the unique sextic class. | Orders seven and eight still need a second direct reconstruction. |
| 9–10 | Exhibit genuine degree-eight `z`-shears, quotient their tangent directions, and eliminate residual weight `-2` exactly. For weight `-1`, exact low-order elimination stops at fourth order; later death exists only as modular evidence. **Output:** the correct saturation problem and its surviving sector. | Do not promote modular death or a restricted slice to a characteristic-zero saturation theorem. |

## 4. The live frontier

**(F1) Orders seven and eight in the second direct reconstruction.** Order
six is no longer open. The residual cache, weight decomposition, full-rank
maximal minors, exact deficient-block nullspaces, and the unique sextic class
are present. Continue in the evolving standard-monomial space; do not freeze
the order-five basis when a sextic generator changes the quotient. The target
is exact rational rank/reduction data for the final two Hilbert layers 30 and
3.

**(F2) Root/Rees comparison beyond order four.** The conceptual model and
direct determinant equations currently agree through quartic parameter
order. The direct model is exact through six. The missing theorem should
identify the filtered complexes and their obstruction maps at every order,
or at minimum extend the exact row-space comparison through order six.
Merely matching Hilbert numbers is insufficient: the comparison must map
generators and syzygies.

**(F3) Independent reproduction.** Recompute the targeted degree-seven
radical certificate and enough of the local algebra in Singular or
Macaulay2 to avoid a shared implementation lineage. A useful first target is
reduced rigidity, followed by the order-six Hilbert value and unique sextic.
Total reconstruction of every 584-by-584 matrix is not required before a
meaningful independent gate can clear.

**(F4) Degree-eight orbit saturation.** The reduced degree-eight germ cannot
be a point because known shears give components. The correct statement is
that its reduced germ equals the union swept out by the affine orbit and
known source/target shear components. The residual weight `-1` sector must
be treated exactly over characteristic zero, including arcs that bend out of
the previously analyzed slice.

Dependencies: F1 supplies a second complete finite reconstruction; F2 turns
that agreement into a conceptual theorem; F3 is an external verification
gate; F4 is a separate follow-on project and should not be sold as a cheap
consequence of degree-seven rigidity.

## 5. Graveyard (causes of death — read before proposing routes)

- **Formal right-triviality implies bounded affine rigidity.** Formal
  étaleness allows source automorphisms of unbounded degree. The bounded
  coefficient scheme retains a nonreduced transverse intersection. These
  are compatible statements, not competing proofs.
- **Tangent dimension counts components.** The ten-dimensional tangent
  space and the degree-eight 33-dimensional quotient are first-order data.
  They do not determine the reduced germ or number of components.
- **A restricted five-dimensional slice proves full isolation.** False:
  higher-order arcs can bend out of the slice
  ([`JCG-02C45EB8`](../../claims/JCG-02C45EB8.md)). Any saturation argument
  must control the full residual sector.
- **The old length 656 is the local algebra.** It was a six-jet initial
  monomial quotient, not the completed ring. The exact completed length is
  584.
- **Two-prime agreement is a rational upper bound.** Good-prime ranks give
  characteristic-zero lower bounds on matrix rank. Deficient blocks require
  exact rational relations for the complementary inequality. The current
  order-six result has those relations; do not generalize that status to an
  unfinished order.
- **Degree-eight rigidity means a point.** Explicit quadratic source shears
  disprove this formulation. Use orbit saturation.

## 6. Tasks

Each item is a task capsule. Preserve the evolving quotient basis, coefficient
domain, and both rank inequalities at every order. If a new generator changes
the standard monomials, stop and update the basis before doing the next
matrix calculation; a total Hilbert number without that ledger is not an
acceptable return.

**P3-T1 — Continue the exact reconstruction through orders seven and eight.**

Actor: `local_symbolic`. Status: ready.

*Inputs:* the public Program 3 supplement; the exact order-six residual
description and sextic generator; the existing length-584 basis metadata.

*Payoff:* a second exact route to the terminal Hilbert layers and total
length.

*Attack:* update standard monomials after the sextic; split rows by torus
weight; use modular maximal minors for full-rank lower bounds and rational
nullspaces checked against every row for deficient blocks.

*Done when:* order-seven and order-eight ranks, quotient bases, reductions,
and hashes are replayable over `Q`, and their cumulative dimensions agree
with 581 and 584 without importing the original completed matrices as an
oracle.

**P3-T2 — Prove all-order source-flow/determinant equivalence.**

Actor: `online_model`. Status: ready.

*Inputs:* the working paper, source-flow appendix, and exact comparison
through order four.

*Payoff:* explains the Kuranishi algebra through marked-root geometry and
may make later calculations structural rather than brute force.

*Done when:* a filtered theorem defines both complexes, constructs the map,
proves compatibility of differentials and gauge, and states exactly what
hypotheses identify obstruction spaces at every order.

**P3-T3 — Targeted second-system reproduction.**

Actor: `independent_cas`. Status: ready.

*Done when:* a separate CAS reproduces the degree-seven radical certificate,
the order-six Hilbert value, and the uniqueness of the sextic initial class,
with inputs derived independently from the published equations.

## 7. Evidence and replay index

The public supplement contains the reduced slice and torus-attractor
calculations, order-eight data, order-nine integrability certificate,
inverse-system verifiers, border basis, exact multiplication matrices, and
the order-six rational-block certificates. The paper records which results
are exact rational, which use good-prime maximal minors, and which remain
modular evidence.

For the length theorem, the inverse-system contraction closure gives a lower
bound 584 and the commuting multiplication representation gives the matching
upper bound. Order nine is killed by exact nonzero determinants in every
possible weight. For order six, the deficient weights have rational
nullspaces verified against every original row; the full-rank weights have
nonzero minors modulo two good primes.

The key boundary is interpretive: these files certify the stated polynomial
and linear-algebra identities. They do not independently prove that the
chosen slice is the correct quotient of the moduli problem, nor do they
constitute an independent-CAS reproduction. The [proof index](../../evidence/index.md)
and stable claim pages keep those fields separate.

For new computations, preserve the weight-by-weight audit trail rather than
only the total Hilbert value. A certificate should state the coefficient
domain, row and column bases, rank direction proved by each modular minor or
rational relation, and how the quotient basis changes when a new generator
appears. This metadata is what permits an independent implementation to
compare mathematics rather than file formats.
Retain failed ranks and exceptional weights as first-class outputs.
Record them permanently.

## 8. Do not do

- Do not recompute order six as though it were still open.
- Do not call length 584 a number of nearby maps.
- Do not infer full bounded rigidity from formal right-triviality.
- Do not infer characteristic-zero deficiency from modular nullity without
  exact rational relations.
- Do not hold the standard-monomial basis fixed after a new generator enters.
- Do not formulate degree-eight saturation as “the reduced germ is a point.”
- Do not claim the source-flow construction already recovers the complete
  algebra; exact comparison currently stops at order four.
- Do not present one computational family as independent reproduction merely
  because it uses a different Python library.

[Back to the Program 3 overview](../programs/local-rigidity-and-deformation-algebra.md)
