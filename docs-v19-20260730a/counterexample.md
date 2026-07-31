---
title: "Counterexample"
description: "The complete three-variable map, its two direct checks, its provenance, and what it does—and does not—settle."
---

# The Counterexample

<p class="dek">There is a polynomial map
\(F:\mathbf C^3\to\mathbf C^3\) with nonzero constant Jacobian determinant
that is not injective.</p>

## Statement and direct checks

Put \(A=1+xy\), and define \(F=(P,Q,R)\) by

\[
\begin{aligned}
P&=A^3z+y^2A(4+3xy),\\
Q&=y+3xA^2z+3xy^2(4+3xy),\\
R&=2x-3x^2y-x^3z.
\end{aligned}
\]

Two finite calculations settle the conjecture in dimension three:

\[
\det DF=-2,
\]

and

\[
\begin{aligned}
F(0,0,-1/4)
&=F(1,-3/2,13/2)\\
&=F(-1,3/2,13/2)
=(-1/4,0,0).
\end{aligned}
\]

The determinant condition makes \(F\) locally invertible. The displayed
triple collision shows that \(F\) is not globally injective, hence not a
polynomial automorphism. For \(n>3\), the product
\(F\times\operatorname{id}_{\mathbf C^{n-3}}\) gives the same contradiction
in dimension \(n\).

<div class="evidence-box">
  <strong>Conclusion.</strong> The Jacobian conjecture is false in every
  dimension at least three. The two-dimensional conjecture remains open.
</div>

## Credit and provenance

The source chain used by this guide is: **Akhil Mathew suggested the problem
to Levent Alpöge; Alpöge put the problem to Fable; Fable produced the work
leading to the example; Alpöge announced the resulting map.** More precisely,
Alpöge's announcement and the accompanying note credit Mathew for the question
and Fable for the work leading to the example. The guide records those roles
separately from later proof, exposition, and formalization.

- [Alpöge's announced example and technical note](https://www.ulam.ai/research/jacobian.pdf)
- [Alpöge's announcement](https://x.com/__alpoge__/status/2079028340955197566)
- [Terence Tao's geometric digestion](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)

## The mathematical idea

For an expert, the shortest useful explanation is not a cancellation in a
degree-seven formula. It is a three-sheeted incidence construction. Factor a
binary cubic as a marked linear factor times a quadratic factor and then
forget which simple root was marked. A generic cubic has three roots, so the
forgetful map is generically three-to-one. The resultant-one condition makes
it étale, while a double-root hyperplane slice makes the source unexpectedly
isomorphic to affine three-space.

That geometric picture explains all three essential features at once:
local invertibility comes from keeping the marked root simple; global
noninjectivity comes from the three possible markings; and the explicit
polynomial formula comes from global coordinates on the exceptional affine
slice.

[Follow the construction step by step](geometry.md){ .md-button .md-button--primary }

## Formalizations and independent implementations

Several independent Lean developments encode the displayed calculation or
closely related determinant-one forms. Their scopes differ, so the existence
of a repository is not treated as a blanket machine check of every geometric
claim on this site.

- [Alejandro Radisic's pinned `alpoge-lean` development](https://github.com/alerad/alpoge-lean/tree/b39e3bf3493939db11b0f78c5b369dd028093f0f)
- [Formal Conjectures PR 4474, by Paul Lezeau](https://github.com/google-deepmind/formal-conjectures/pull/4474)
- [Formal Conjectures PR 4486, a sorry-free refutation over \(\mathbf Q\)](https://github.com/google-deepmind/formal-conjectures/pull/4486)
- [Dean Cureton's all-fields formalization](https://github.com/deancureton/jacobian/tree/0d4a9212d874226ad81ce5a926becddfa94e6a88)

## What this does not settle

- It does not settle the Jacobian conjecture in dimension two.
- It does not classify three-dimensional counterexamples.
- It does not prove that degree seven is minimal.
- It does not automatically transfer every earlier equivalence or neighboring
  conjecture without checking that theorem's hypotheses.
- It does not machine-check the geometric interpretation or the working
  research programs merely because the polynomial identity has been
  formalized.

## Continue

- [The Three-Dimensional Counterexample](collections/base-counterexample-and-immediate-consequences.md)
- [A Counterexample Over Every Field](collections/all-fields-counterexample.md)
- [Consequences for Neighboring Conjectures](collections/consequences-for-neighboring-conjectures.md)
- [The Plane Jacobian Conjecture Remains Open](collections/plane-jacobian-conjecture.md)
