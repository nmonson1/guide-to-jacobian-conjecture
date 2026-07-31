---
title: "Model research brief — Stable Moduli"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Program 4</p>
# Program 4: Stable Moduli

**Research state:** 29 July 2026, Pacific time.  
**Actor guidance:** quotient, Torelli, and gluing arguments -> online model;
low-length invariant modules and cocycle tests -> local symbolic system;
core invariant reproduction -> independent CAS.

This is the complete public handoff. The linked
[working paper](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-22-v11.pdf),
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
3. **weighted graph closures**, separated finite-type spaces that classify
   degeneration directions near an escape wall.

The third object is not a repaired orbit quotient. It records how an orbit
degenerates, not all fppf equivalences. Likewise the boundary stack
`[U_N/G_m]` is framed or rigidified; it is not automatically the full
unrigidified left-right groupoid.

When one root escapes to infinity, an explicit elementary transition relates
the length-`N` chart to a lower-length chart plus a contracted weight-two
gauge direction. Simultaneous escapes, the nonunit-resultant boundary,
scaling compatibility, and intrinsic relative-Jacobian gluing remain open.

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

## 3. What is proved (statements only; proofs at the locators)

| # | Statement | Where |
| --- | --- | --- |
| 1 | For the quadratic cubic-frame slice with `alpha != 0`, `q=beta/alpha^2` is complete under arbitrary polynomial left-right equivalence and stabilization; `alpha=0` is one separate orbit. | [`JCG-0F9A20C0`](../../claims/JCG-0F9A20C0.md); paper main theorem |
| 2 | For coprime admissible cubic frames, stable equivalence equals ordinary equivalence and is classified by the decorated finite scheme `(Z_A,B|Z_A)`, without a squarefreeness assumption. | [`JCG-B858C93E`](../../claims/JCG-B858C93E.md) |
| 3 | The fixed-frame Torelli theorem extends across multiplicities and common-root strata using the weighted relative-Jacobian divisor. | [`JCG-E48F1FF0`](../../claims/JCG-E48F1FF0.md); all-multiplicity theorem |
| 4 | The rigidified boundary stack `[U_N/G_m]` is smooth Deligne--Mumford of dimension `2N-1` and classifies the stated coprime boundary data. | [`JCG-046E56A8`](../../claims/JCG-046E56A8.md) |
| 5 | One bounded polynomial map presents every degree-preserving root-translation orbit and separates finite-root data from the principal part of roots escaping to infinity. | [`JCG-2F2C2F29`](../../claims/JCG-2F2C2F29.md) |
| 6 | The categorical invariant algebra is a relative differential kernel; its global functions are controlled by the single one-root wall. | [`JCG-66049841`](../../claims/JCG-66049841.md); categorical quotient appendix |
| 7 | The bounded cubic-frame fppf orbit quotient is not algebraic along the generic rank-one wall. | [`JCG-4D953715`](../../claims/JCG-4D953715.md) |
| 8 | Weighted graph closures give separated finite-type spaces for one-root and length-`m` escape directions, with explicit weights. | [`JCG-62905FD2`](../../claims/JCG-62905FD2.md) |
| 9 | A quartic seed family has a two-parameter complete stable invariant `(rho,sigma)`, giving an affine plane of fixed-degree stable moduli. | [`JCG-6B08BDE5`](../../claims/JCG-6B08BDE5.md) |
| 10 | The exceptional `q=-2` member is uniformly detected by multiplicity two in the weighted relative-Jacobian divisor. | [`JCG-7FB01BFA`](../../claims/JCG-7FB01BFA.md) |

The paper and exact checkers support these statements at the indicated
scopes. Independent geometric review remains pending, especially for
normalization lifting, marked-cylinder rigidity, all-multiplicity Torelli,
and the Cohen--Macaulay support argument at the categorical wall.

## 4. The live frontier

**(F1) Global gluing of weighted graph boundaries.** The one-root wall and
length-`m` local principal-part models are explicit. Missing are overlap
maps for simultaneous escapes, cocycle compatibility, the nonunit-resultant
boundary, and scaling. A universal property must describe a functor of
families and prove separatedness/properness claims only to the extent the
construction warrants.

**(F2) Intrinsic stable-equivalence gluing.** Coefficient-space orbit maps,
categorical functions, and graph closures do not prove that stabilized
relative-Jacobian geometry reconstructs equivalence across every infinity
wall. The finite-root Torelli theorem supplies the interior classification;
the frontier is compatibility across changing boundary length and
multiplicity.

**(F3) Low-length overlap tests.** Once a candidate transition law is
written, compute invariant modules, Smith/Fitting data, and triple-overlap
cocycles for small `N`. These tests can refute a proposed universal theorem
quickly. They support a theorem but cannot replace the gluing proof.

**(F4) Targeted verification for `D_mod`.** Independently expand the
two-parameter family, verify its uniform ordinary degree, reproduce the
`q`-separation invariant, and locate the proof of the asserted first
degree-eleven stable modulus in the full cubic-frame family. The relevant
local definition uses pointed curves through `G`; ordinary degree is not an
invariant of an abstract left-right class.

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

**P4-T1 — Give the weighted graph boundary a global universal property.**  
Actor: `online_model`. Status: ready.  
*Inputs:* this page; the [Program 4 paper](../../assets/manuscripts/04-boundary-rigidity-stable-moduli-2026-07-22-v11.pdf);
the categorical quotient and infinity-gluing collections; the explicit
one-root transition in the public technical materials.  
*Payoff:* replaces local wall charts with one representable degeneration
object and makes cross-length Torelli a precise question.  
*Attack:* define the family-valued functor first; write overlap maps for
ordered escape clusters; treat scaling and nonunit resultants; prove the
cocycle before a universal property.  
*Done when:* the local closures glue, represent the stated degeneration
functor, and the theorem explicitly says why it is not the fppf orbit
quotient.

**P4-T2 — Compute low-`N` invariant and overlap tests.**  
Actor: `local_symbolic`. Status: blocked until T1 proposes transitions.  
*Inputs:* the public categorical-wall checker and the exact transition maps
from T1.  
*Done when:* Smith/Fitting invariants, double- and triple-overlap cocycles,
and regression examples either support the maps or exhibit a counterexample,
with exact inputs and hashes.

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
They do not prove normalization lifting, stable-cylinder rigidity,
all-multiplicity component recognition, global gluing, or the
Rim--Schlessinger and support arguments independently. The graph records no
independent specialist review.

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
- Do not infer simultaneous-escape gluing from the one-root chart.
- Do not claim a universal property before defining the functor of families
  and proving overlap cocycles.
- Do not cite the degree-eleven threshold as verified until its locator and
  independent reproduction gate are complete.
- Do not represent symbolic sanity checks as proofs of the geometric gluing
  or stable-cylinder arguments.
- Do not present the working paper as independently reviewed.

[Back to the Program 4 overview](../programs/stable-moduli.md)
