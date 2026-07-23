---
title: Claims
description: A source-linked inventory of Jacobian-conjecture claims and questions.
---

# Claim inventory

Each row gives the claim, its primary source, concise credit, and current review status. Follow the claim link for evidence, limitations, and full attribution.

!!! info "How to read the status column"
    **Proof offered** means a source supplies an argument; it does not mean this guide has independently verified it. **Verified** is reserved for a qualifying review recorded against the exact statement and source version.

## Counterexample and global geometry

<div class="claim-table" markdown="1">

| Claim | Primary source | Credited to | Status |
|---|---|---|---|
| [The Jacobian conjecture](claim/the-jacobian-conjecture.md)<br>Every polynomial map from complex affine n-space to itself whose Jacobian determinant is a nonzero constant is a polynomial automorphism. | [Ganze Cremona-Transformationen](https://doi.org/10.1007/BF01695502) | O.-H. Keller | Refutation offered — review pending |
| [Constant Jacobian determinant of the Alpöge map](claim/alpoge-map-constant-jacobian.md)<br>The displayed Alpöge polynomial map has Jacobian determinant equal to the constant -2. | [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf) | Levent Alpöge, Akhil Mathew, Alejandro Radisic; AI assistance: Fable; +1 more | Proof offered — review pending |
| [An explicit triple collision](claim/alpoge-map-triple-collision.md)<br>The three distinct rational points (0,0,-1/4), (1,-3/2,13/2), and (-1,3/2,13/2) have the common image (-1/4,0,0) under the Alpöge map. | [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf) | Levent Alpöge, Akhil Mathew, Alejandro Radisic; AI assistance: Fable; +1 more | Proof offered — review pending |
| [Failure of the Jacobian conjecture in dimensions at least three](claim/jacobian-conjecture-false-dimension-at-least-three.md)<br>The Jacobian conjecture is false in every dimension n at least 3. | [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf) | Levent Alpöge, Akhil Mathew, Paul Lezeau; AI assistance: Fable; +1 more | Proof offered — review pending |
| [Invertibility and properness for complex Keller maps](claim/keller-map-invertibility-properness-equivalence.md)<br>For a Keller map over the complex numbers, polynomial invertibility, properness, emptiness of the nonproperness set, and codimension at least 2 of that set are equivalent, with the empty set assigned infinite codimension. | [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf) | Credit not yet assigned | Proof offered — review pending |
| [A determinant-one counterexample over every field](claim/determinant-one-counterexample-every-field.md)<br>For every field k, the determinant-one rescaled construction formalized by Dean Cureton gives a polynomial map from k^3 to k^3 that is not injective. | [jacobian](https://github.com/deancureton/jacobian/tree/0d4a9212d874226ad81ce5a926becddfa94e6a88) | deancureton | Proof offered — review pending |
| [The double-root resultant slice is affine three-space](claim/double-root-resultant-slice-affine-three-space.md)<br>In the binary-form multiplication model of the counterexample, the resultant-one double-root slice is polynomially isomorphic to affine three-space. | [A digestion of the Jacobian conjecture counterexample](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/) | Levent Alpöge, Terence Tao, Andy Jiang; AI assistance: ChatGPT; +6 more | Proof offered — review pending |
| [Three symmetry orbits of dual binary-cubic hyperplanes](claim/binary-cubic-hyperplane-orbits.md)<br>Under the projective linear action, dual binary-cubic hyperplanes have three orbits, indexed by the root partitions (3), (2,1), and (1,1,1). | [A digestion of the Jacobian conjecture counterexample](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/) | Terence Tao | Proof offered — review pending |
| [Comparison with Vitushkin's 1999 rational example](claim/vitushkin-rational-example-comparison.md)<br>Vitushkin's 1999 rational example has an analogous multiplication-map presentation and is generically two-to-one, but its source is a punctured plane, so the resulting map has a pole. | [Terence Tao's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693536) | Terence Tao, Anonymous commenter | Proof offered — review pending |
| [Invariant characterization of the double-root orbit](claim/double-root-orbit-invariant-triangularization-question.md)<br>Is the double-root orbit invariantly the unique orbit whose constraint fiber admits a global polynomial triangularization or trivialization? | [garylangford's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693540) | garylangford | Open |

</div>

## Finite normalization and defect

<div class="claim-table" markdown="1">

| Claim | Primary source | Credited to | Status |
|---|---|---|---|
| [Generic degree and fiber stratification of the counterexample](claim/counterexample-fiber-stratification.md)<br>The Alpöge map has generic degree 3, with affine fiber cardinality 3 off the cubic discriminant, 1 on the discriminant away from the triple-root curve, and 0 on the triple-root curve. | [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf) | Levent Alpöge, Will Sawin, Terence Tao; AI assistance: ChatGPT; +2 more | Proof offered — review pending |
| [Image and nonproperness set of the counterexample](claim/counterexample-image-and-nonproperness.md)<br>The image of the Alpöge map is complex affine 3-space minus the triple-root curve Gamma, while its nonproperness set is the discriminant hypersurface V(Delta). | [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf) | Alejandro Radisic | Proof offered — review pending |
| [Degree-three function-field extension with S3 Galois closure](claim/counterexample-s3-galois-closure.md)<br>The function-field extension induced by the Alpöge map has degree 3 and an S3 Galois closure, as described by the cited explicit cubic model. | [Galois structure of the new counterexample to the Jacobian conjecture: an explicit cubic model with S3 monodromy — is this known?](https://mathoverflow.net/questions/513387/) | dorky | Proof offered — review pending |
| [Trivial rational deck group](claim/counterexample-trivial-rational-deck-group.md)<br>The displayed three-variable map has trivial rational deck group over its target: a rational self-map sigma satisfying F composed with sigma equals F must be the identity. | [Galois structure of the new counterexample to the Jacobian conjecture: an explicit cubic model with S3 monodromy — is this known?](https://mathoverflow.net/questions/513387/) | dorky | Proof offered — review pending |
| [Exact finite-field fiber counts](claim/exact-finite-field-fiber-counts.md)<br>Over every finite field F_q of odd order, every rational fiber has size 0, 1, or 3; writing N_j for the number of targets with j rational preimages, N_1+3N_3=q^3 and N_0=2N_3, with 6N_3=(q-1)(q^2+2) outside characteristic 3 and 6N_3=q^2(q-1) in characteristic 3. | [Alejandro Radisic's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693559) | Alejandro Radisic | Proof offered — review pending |
| [Asymptotic S3 fiber distribution](claim/finite-field-s3-fiber-distribution.md)<br>The normalized finite-field fiber-count distribution (N_0,N_1,N_3)/q^3 tends to (1/3,1/2,1/6), matching the proportions of elements of S3 with 0, 1, and 3 fixed points. | [Alejandro Radisic's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693559) | Alejandro Radisic | Proof offered — review pending |
| [Characteristic-three degeneration](claim/characteristic-three-degeneration.md)<br>In characteristic 3, the translation T=b+S puts the fiber cubic into the form cS^3+S^2+W; the missed curve is empty and the triple-root stratum disappears. | [Alejandro Radisic's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693559) | Alejandro Radisic | Proof offered — review pending |
| [Surjectivity in algebraically closed characteristic three](claim/characteristic-three-surjective-etale-noninjective.md)<br>Over an algebraically closed field of characteristic 3, the map is surjective while remaining étale and noninjective. | [Alejandro Radisic's comment](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/comment-page-1/#comment-693559) | Alejandro Radisic | Proof offered — review pending |

</div>

## Deformations, families, and equivalence

<div class="claim-table" markdown="1">

| Claim | Primary source | Credited to | Status |
|---|---|---|---|
| [Three-dimensional Keller maps of every generic degree](claim/keller-maps-every-generic-degree.md)<br>For every integer d at least 3, there is a nonproper Keller map from complex affine 3-space to itself with generic degree d. | [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf) | algal | Proof offered — review pending |

</div>

## Reductions to special forms

<div class="claim-table" markdown="1">

| Claim | Primary source | Credited to | Status |
|---|---|---|---|
| [An explicit degree-three counterexample in 11 variables](claim/degree-three-counterexample-11-variables.md)<br>The cited map from complex affine 11-space to itself has total degree 3, 52 nonzero monomial terms, constant Jacobian determinant -2, and three displayed distinct rational inputs with one common image. | [11 variable cubic jacobian conjecture counterexample](https://gist.github.com/Spacerat/08b4a43f6b6ca57178efabc220170ce8/2224dace71e8763a8621a7f557bbc545a53aa820) | Spacerat; AI assistance: ChatGPT | Proof offered — review pending |
| [An explicit cubic-homogeneous counterexample in 24 variables](claim/cubic-homogeneous-counterexample-24-variables.md)<br>The cited explicit map has the form G(U)=U+H(U) over Q^24, with every nonzero component of H homogeneous cubic, determinant 1, 54 nonzero cubic monomials, and a displayed collision of two distinct rational points. | [explicit-cubic-homogeneous-jacobian-counterexample](https://github.com/wtho704/explicit-cubic-homogeneous-jacobian-counterexample/tree/45a7616fdf5a20c065564f2676190093722696b9) | William Thompson | Proof offered — review pending |

</div>

## The two-dimensional problem

<div class="claim-table" markdown="1">

| Claim | Primary source | Credited to | Status |
|---|---|---|---|
| [The plane Jacobian conjecture remains open](claim/plane-jacobian-conjecture-open.md)<br>The Jacobian conjecture in dimension 2 remains open. | [A Counterexample to the Jacobian Conjecture](https://www.ulam.ai/research/jacobian.pdf) | Credit not yet assigned | Open |
| [Kraus stated the plane conjecture in 1884](claim/kraus-1884-plane-jacobian-conjecture.md)<br>Ludwig Kraus's 1884 paper states, as its main result, the modern plane Jacobian conjecture rather than merely an earlier adjacent problem. | [On the origin of the Jacobian conjecture](https://doi.org/10.5802/crmath.831) | Lázaro Orlando Rodríguez Díaz | Verified |
| [The gap in Kraus's proposed proof](claim/kraus-proof-gap-at-infinity.md)<br>The final step of Kraus's claimed proof is invalid because the chosen parametrization does not justify the required derivative conclusion at infinity; the unresolved issue is control of ramification at infinity. | [On the origin of the Jacobian conjecture](https://doi.org/10.5802/crmath.831) | Lázaro Orlando Rodríguez Díaz | Verified |

</div>

## Consequences and neighboring conjectures

<div class="claim-table" markdown="1">

| Claim | Primary source | Credited to | Status |
|---|---|---|---|
| [Failure of the all-dimensional Vanishing Conjecture](claim/all-dimensional-vanishing-conjecture-false.md)<br>Zhao's all-dimensional Vanishing Conjecture is false in some finite dimension. | [Direct Consequences of the Three-Dimensional Counterexample to the Jacobian Conjecture](https://zzhang-iu.github.io/papers/direct-consequences-jacobian/) | Zihan Zhang | Proof offered — review pending |
| [Failure of the all-dimensional Image Conjecture](claim/all-dimensional-image-conjecture-false.md)<br>The all-dimensional Image Conjecture is false in some finite dimension. | [Direct Consequences of the Three-Dimensional Counterexample to the Jacobian Conjecture](https://zzhang-iu.github.io/papers/direct-consequences-jacobian/) | Zihan Zhang | Proof offered — review pending |
| [Failure of the Dixmier conjecture in dimensions at least three](claim/dixmier-conjecture-false-dimension-at-least-three.md)<br>The Dixmier conjecture is false for the complex Weyl algebra A_n for every n at least 3. | [dixmier-counterexample](https://github.com/wmayner/dixmier-counterexample/tree/475cea2a7449230e7d493ff29ea94fc22ce81e61) | William G. P. Mayner; AI assistance: Claude Fable 5 | Proof offered — review pending |
| [Small counterexamples to the Gaussian Moments Conjecture](claim/gaussian-moments-conjecture-counterexamples.md)<br>The Gaussian Moments Conjecture is false in every dimension n at least 3: the cited preprint gives a five-term quartic witness in three real Gaussian variables and a six-term cubic witness in four variables. | [Small Counterexamples to the Gaussian Moments Conjecture](https://arxiv.org/abs/2607.18186v1) | Christopher D. Long; AI assistance: ChatGPT 5.6 Sol Pro, Claude Fable 5 | Proof offered — review pending |

</div>
