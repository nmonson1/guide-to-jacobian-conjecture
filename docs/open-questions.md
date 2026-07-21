---
title: What remains open
description: Research directions surviving the three-dimensional counterexample.
---

# What remains open

The failure of the conjecture in dimension three changes the research program;
it does not erase it. These are directions rather than claims of novelty. A
serious project should begin with a fresh literature and priority review.

## 1. The plane Jacobian conjecture

The central surviving case asks whether every Keller map

\[
F:\mathbb C^2\longrightarrow\mathbb C^2
\]

is a polynomial automorphism. The three-dimensional root-incidence mechanism
does not directly produce a plane map. Classical Newton polygon, valuation,
boundary, and approximate-root programs therefore remain active and relevant.

<span class="status status-open">OPEN</span>

## 2. Minimum coordinate degree in dimension three

The known counterexample has coordinate degrees ((7,6,4)). Vistoli’s
degree-at-most-three theorem supplies the current interval

\[
4\le D_{\min}\le7.
\]

Can a counterexample have coordinate degree four, five, or six? Can the
degree-seven map be lowered by polynomial changes of source and target
coordinates? Restricted computations do not answer the unrestricted problem.

<span class="status status-open">OPEN</span>

## 3. Classify the three-sheeted mechanism

The base map is the simple-root locus of a binary cubic. Natural questions
include:

- Which finite cubic covers admit an affine simple-root open isomorphic to
  \\(\mathbb A^3\\)?
- Which nonproperness and omitted-locus configurations can occur?
- How rigid is the base construction under polynomial or stable equivalence?
- Which boundary data are intrinsic rather than artifacts of coordinates?

Some same-week computations suggest both rigidity in narrow normal forms and
variation in broader families. Those must be kept separate.

<span class="status status-review">UNDER REVIEW</span>

## 4. Consequences for neighboring conjectures

Classical implication chains relate finite-dimensional Jacobian statements to
Poisson and Dixmier conjectures. Precise per-dimension formulations are being
developed in [Formal Conjectures issue
#4489](https://github.com/google-deepmind/formal-conjectures/issues/4489), with
the associated pull requests still under review at this guide’s status date.

The useful work is not merely to repeat “there are consequences,” but to state
the dimensions, characteristic assumptions, and implication directions
without ambiguity.

<span class="status status-review">UNDER REVIEW</span>

## 5. Formalize the geometry, not only the collision

The determinant-and-collision certificate is short. A more explanatory Lean
development could formalize:

- the projective-root incidence model;
- the inverse formulas on both projective charts;
- the (3/1/0) fiber classification;
- the discriminant and triple-root locus;
- the image and nonproperness statements.

That is substantially more work than checking two polynomial identities, but
it would turn the geometric explanation into a reusable formal object.

<span class="status status-open">OPEN</span>

## How to add a problem

An open question should identify its exact hypotheses, explain its relation to
known results, and name the smallest certificate that would materially advance
it. Use the [mathematical claim issue template](https://github.com/nmonson1/guide-to-jacobian-conjecture/issues/new?template=claim.yml)
or read [how to contribute](contribute.md).

