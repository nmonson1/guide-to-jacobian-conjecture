---
title: "Relevant external developments"
description: "A source-based chronological catalogue of external contributions to the counterexample, its verification, direct descendants, and the surviving plane problem."
---

# Relevant external developments

<p class="dek">Our aim is to record every relevant external contribution
known to us. Omissions are mistakes to be corrected, not editorial judgments
that the work was unimportant.</p>

## Scope and reading rules

This ledger covers the history needed to understand the conjecture, the 2026
counterexample and its direct explanations, independent checks, new
counterexample families and normal forms, direct consequences for neighboring
conjectures, and work on the surviving plane problem. It does not attempt to
catalogue every earlier paper on the Jacobian conjecture or every news report.

Dates describe the cited public record. Entries summarize what their sources
claim; inclusion is not a statement that this project has independently
verified every proof. The ledger is current to **7 August 2026**.

## Before July 2026

- **Ludwig Kraus (1884), the plane statement and an attempted proof.** Lázaro
  Orlando Rodríguez Díaz identifies Kraus's statement as the modern plane
  Jacobian conjecture and locates a gap at infinity in the attempted proof.
  [Rodríguez Díaz, “On the origin of the Jacobian conjecture”](https://doi.org/10.5802/crmath.831)
- **Ott-Heinrich Keller (1939), the classical source.** Keller's paper became
  the standard source for the conjecture's name and traditional date.
  [“Ganze Cremona-Transformationen”](https://doi.org/10.1007/BF01695502)
- **Hyman Bass, Edwin Connell, and David Wright (1982), degree reduction and
  formal inverses.** Their stable reduction makes cubic-homogeneous maps a
  central normal form. [Primary source](https://doi.org/10.1090/S0273-0979-1982-15032-7)
- **Ludwik Drużkowski (1983), cubic-linear reduction.** Drużkowski reduced
  further to maps whose nonlinear coordinates are cubes of linear forms, at
  the cost of increasing dimension. [Primary source record](https://eudml.org/doc/163789)
- **Jorge A. Guccione, Juan J. Guccione, Rodrigo Horruitiner, and Christian
  Valqui (2022), plane degree reduction to 108 with one exceptional pair.**
  Their theorem excludes every maximum degree below 125 except the pair
  \((72,108)\), up to order, and reduces that pair to two final support
  configurations. [arXiv:2204.14178](https://arxiv.org/abs/2204.14178)

## The counterexample: 19–21 July 2026

- **Akhil Mathew, Levent Alpöge, and Fable, in distinct roles.** Mathew
  suggested the question to Alpöge; Alpöge put it to Fable; Fable produced the
  work leading to the example; Alpöge announced the map on 19 July Pacific
  time. The technical note posted on 20 July gives the formula, determinant,
  collision, and binary-cubic construction.
  [Announcement](https://x.com/__alpoge__/status/2079028340955197566) ·
  [technical note](https://www.ulam.ai/research/jacobian.pdf)
- **David Speyer and participants in the Secret Blogging Seminar (20 July),
  public structural analysis.** The discussion developed the function-field,
  fiber, nonproperness, and geometric interpretations and corrected early
  guesses as the calculation evolved.
  [Seminar post and discussion](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)
- **Alexis Gallagher and the unbylined Ulam technical note (20 July), two
  constructions realizing every generic degree.** Gallagher gives an
  infinite weighted family and exact reconstruction formulas. The Ulam note
  also presents a different determinant-preserving modification in
  Theorem 5.2 and derives every generic degree at least three in Corollary
  5.3. Their public metadata are seventeen minutes apart and do not establish
  when either construction was first found or circulated.
  [Explanatory article](https://alexisgallagher.com/posts/2026/jacobianfun/) ·
  [pinned source and code](https://github.com/algal/jacobianfun/tree/0a73d4c75bed60660c6e91a56f1595be756cbd59) ·
  [Ulam technical note](https://www.ulam.ai/research/jacobian.pdf)
- **`u/zongshu`, ChatGPT, and Joe Atkins-Turkish (`Spacerat`) (20 July), in
  distinct roles on an 11-variable degree-at-most-three descendant.** The
  pinned artifact credits `u/zongshu` with suggesting cubic degree reduction,
  ChatGPT with generating the explicit construction, simplification, and
  verification code, and Atkins-Turkish with posting and preserving the
  artifact. The resulting map has 52 monomial terms, determinant \(-2\), and
  a rational triple collision; it is not the stricter cubic-homogeneous form.
  [Pinned certificate](https://gist.github.com/Spacerat/08b4a43f6b6ca57178efabc220170ce8/2224dace71e8763a8621a7f557bbc545a53aa820)
- **Paul Lezeau (20 July), Lean formalization.** A determinant-one rescaling
  and characteristic-zero collision were submitted to Formal Conjectures.
  [PR 4474](https://github.com/google-deepmind/formal-conjectures/pull/4474)
- **Alejandro Radisic (July), Lean verification.** The `alpoge-lean`
  development checks the explicit determinant and collision.
  [Pinned revision](https://github.com/alerad/alpoge-lean/tree/b39e3bf3493939db11b0f78c5b369dd028093f0f)
- **Dean Cureton (20 July), an all-characteristics Lean construction.** The
  development uses separate witnesses in characteristic two and away from
  two. [Pinned revision](https://github.com/deancureton/jacobian/tree/0d4a9212d874226ad81ce5a926becddfa94e6a88)
- **`techno-optimist` (21 July), a separate sorry-free Lean refutation over
  \(\mathbf Q\).** The pull request was closed without merge; that repository
  disposition is recorded without treating it as a mathematical verdict.
  [Formal Conjectures PR 4486](https://github.com/google-deepmind/formal-conjectures/pull/4486)
- **William Thompson (21 July), a 24-variable cubic-homogeneous
  counterexample.** Thompson supplies an exact map \(U+H(U)\), with \(H\)
  homogeneous cubic, determinant one, a rational collision, and two verifier
  programs. [Pinned repository](https://github.com/wtho704/explicit-cubic-homogeneous-jacobian-counterexample/tree/45a7616fdf5a20c065564f2676190093722696b9) ·
  [Zenodo](https://doi.org/10.5281/zenodo.21466221)
- **Terence Tao (21 July), a geometric digestion.** Tao reconstructs the map
  from the multiplication of a linear and a quadratic binary form, isolating
  local injectivity, global collision, and the exceptional affine chart.
  [Original essay](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
- **Pablo Nogueira Grossi (22 July), an independent Lean 4 verification.**
  The record kernel-checks the determinant and collision and carefully scopes
  claims about Dixmier and Poisson consequences.
  [Zenodo](https://doi.org/10.5281/zenodo.21514514)
- **Liam Giannini (July), independent exact-arithmetic and geometric
  verification.** The archived note reproduces the core algebra and
  geometric mechanism independently.
  [Zenodo](https://doi.org/10.5281/zenodo.21461572)

## New forms, fields, and geometry: 22 July–5 August 2026

- **Harris Chan (23 July), an independently announced 19-variable
  cubic-homogeneous lift.** Chan obtained the sparse 19-variable endpoint
  from the 11-variable descendant. The original announcement was on X; a
  stable post URL is not currently available to this guide. The project's
  contemporaneous manuscript records the announcement and construction, but
  is a secondary source for Chan's priority.
  [Chan's X profile](https://x.com/SirrahChan) ·
  [pinned contemporaneous manuscript](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/05-homogeneous-descendants/main.tex)
- **Irit Huq-Kuruvilla (23 July), a separable characteristic-two
  counterexample in dimension three.** The map has determinant one, generic
  degree three, and a collision; stabilization covers all higher dimensions.
  [arXiv:2607.20968](https://arxiv.org/abs/2607.20968)
- **Piotr Migus (23 July; revised 30 July), real Keller maps with non-dense
  image.** Migus proves that in every dimension at least three the possible
  generic degrees are exactly the even integers at least four and constructs
  them already in dimension three.
  [arXiv:2607.21572](https://arxiv.org/abs/2607.21572)
- **T. Shaska (22 July; revised 25 July), graded Keller maps.** Shaska studies
  Keller maps compatible with weight gradings and proves automorphism results
  in the stated positive-weight and two-dimensional sign-pattern settings.
  [arXiv:2607.20210](https://arxiv.org/abs/2607.20210)
- **Zbigniew Jelonek (22 July), mappings with Jacobian one.** Jelonek studies
  structural consequences for components and nonproperness in light of the
  new example. [arXiv:2607.20597](https://arxiv.org/abs/2607.20597)
- **Felipe Santibañez-Leal (24 July onward), a versioned exact-computation
  program.** The records independently validate the example and explore
  families, escape geometry, positive-characteristic certificates, and the
  plane terminal program. Later planar records explicitly distinguish the
  machine-supported steps from a remaining simultaneous-certificate step.
  [Foundational record](https://doi.org/10.5281/zenodo.21579022) ·
  [planar program record](https://doi.org/10.5281/zenodo.21584243)
- **Romy Mondello (29 July), a dimension-two characteristic-two
  counterexample to the separable conjecture.** The explicit plane map has
  determinant one and a separable degree-three function-field extension.
  [arXiv:2608.02634](https://arxiv.org/abs/2608.02634)
- **Shuhong Gao (31 July), tangent sweeps and arbitrary large degree in every
  dimension above two.** Gao gives a self-contained geometric mechanism,
  generalizes it to direction fields on hypersurfaces, and supplies five new
  exact examples. [arXiv:2608.00222](https://arxiv.org/abs/2608.00222)

## Direct consequences and neighboring conjectures

- **Liam Giannini (20 July), a disproof of the Chamberland–Meisters
  eigenvalue conjecture.** Combining the counterexample with the classical
  cubic-homogeneous reduction gives, in some finite dimension, a
  noninjective polynomial map whose Jacobian is unipotent everywhere;
  realification gives the stated real \(C^1\) consequence.
  [Zenodo](https://doi.org/10.5281/zenodo.21462020)
- **Christopher D. Long (20 July), Gaussian Moments counterexamples.** Long
  gives a five-term quartic witness in three Gaussian variables and a
  six-term cubic witness in four, with higher-dimensional extensions. The
  examples were prompted by, but not mechanically derived from, the
  Jacobian counterexample. [arXiv:2607.18186](https://arxiv.org/abs/2607.18186)
- **Zihan Zhang (20 July), a consequence ledger.** Zhang records consequences
  for all-dimensional Vanishing and Image conjectures and discusses a
  fixed-dimensional Mathieu claim. The latter requires a dimension-preserving
  implication beyond the cited dimension-varying theorem.
  [Source note](https://zzhang-iu.github.io/papers/direct-consequences-jacobian/)
- **Bin Zhu (20 July), scalar-field interpretation.** The paper uses the map as a
  locally nonsingular but globally noninjective field redefinition with
  distinct vacua in a three-scalar model.
  [arXiv:2607.18166](https://arxiv.org/abs/2607.18166)
- **Fable and William G. P. Mayner (21 July), a Dixmier-conjecture
  consequence.** A Fable-prepared note circulated by Mayner constructs an
  injective, nonsurjective Weyl-algebra endomorphism in dimension three and
  stabilizes it upward.
  [Pinned repository](https://github.com/wmayner/dixmier-counterexample/tree/475cea2a7449230e7d493ff29ea94fc22ce81e61)
- **Sergey Sverchkov (22 July), a five-variable unipotent-Jacobian
  counterexample.** Sverchkov gives a noninjective polynomial self-map of
  \(\mathbf C^5\) whose Jacobian is unipotent at every point and analyzes the
  zero set of the associated gradient field.
  [arXiv:2607.20049](https://arxiv.org/abs/2607.20049)
- **Guowu Meng and Liang Yang (24 July; revised 27 July), a five-variable
  Hessian counterexample.** A one-variable Schur descent from the symmetric
  double gives a degree-14 potential with Hessian determinant 128 and a
  noninjective gradient. Together with earlier positive results, the Hessian
  conjecture is true through dimension three, false from dimension five on,
  and open in dimension four.
  [arXiv:2607.22198](https://arxiv.org/abs/2607.22198)
- **Castañeda, Honorato, and Valenzuela-Henríquez (5 August), a weak
  Markus–Yamabe consequence.** They construct counterexamples in dimensions
  at least 14 using the new Jacobian landscape.
  [arXiv:2608.05392](https://arxiv.org/abs/2608.05392)

## The surviving plane problem

- **ratto3423 (23 July), an announced lower bound 125.** Building on the
  Guccione–Guccione–Horruitiner–Valqui reduction, ratto3423 announces a
  computer-assisted calculation eliminating the remaining \((72,108)\)
  supports. The answer says a full write-up is in preparation and does not
  expose the terminal calculation; the announced conclusion is that degree
  below 125 is impossible, while degree 125 remains possible.
  [MathOverflow answer](https://mathoverflow.net/a/513493)

## Help complete the record

Please send missing papers, public announcements, formalizations,
computations, corrections, and stable links through the
[corrections page](../about/corrections.md). A one-line entry is enough for a
minor contribution once its author, role, date, and source can be stated
accurately.
