---
title: "Background reading: enough to start, and what to grab when stuck"
description: "An opinionated guide to books, notes, lectures, and specialist references for readers of the Jacobian-conjecture guide."
---

# Background reading: enough to start, and what to grab when stuck

You do not need to finish Hartshorne before reading this guide. Begin with
the mathematics that interests you. The introductory pages assume basic
algebra, complex analysis, and some comfort with polynomial maps. When a new
idea becomes essential, follow the shortest route that explains why it is
there; move to a systematic text once you want to use it.

For the technical pages, the general prerequisite is compactly stated:

> A solid graduate course in commutative algebra and a serious first course on
> schemes provide enough general background for almost everything in this
> guide.

In practice, that means comfort with localization, integral extensions,
normalization, dimension, flatness, fiber products, finite and étale maps,
free resolutions, and basic \(\operatorname{Tor}\) and
\(\operatorname{Ext}\). More specialized tools—local cohomology, canonical
modules, cotangent complexes, Rees algebras, deformation functors, invariant
theory—can be learned when the problem asks for them.

!!! important "A date warning for classical sources"

    Most books on the Jacobian conjecture were written when the problem was
    open in every dimension. Their mathematics remains useful, while their
    status paragraphs now describe the pre-July-2026 landscape. For the
    current picture, start with [the conjecture](../start/conjecture.md),
    [the counterexample](../start/counterexample.md), and
    [the plane case](plane-case.md).

## A core shelf

The following books cover most of the general machinery used across the site.
They overlap enough that no reader needs all of them at once.

| Resource | Character | Best use here |
| --- | --- | --- |
| [David Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry*](https://link.springer.com/book/10.1007/978-1-4612-5350-1) | The best single match for this guide: broad, geometric, and unusually humane for a large reference. | Integral dependence, dimension, differentials, flatness, resolutions, duality, Gröbner methods, and the algebra--geometry dictionary. Read by topic. |
| [Ravi Vakil, *The Rising Sea*](https://math.stanford.edu/~vakil/216blog/) | A schemes course that repeatedly explains why the next construction is being invented. The exercises carry a substantial part of the course. | A first sustained route through modern algebraic geometry, especially if you learn well from problems and motivation. |
| [Ulrich Görtz and Torsten Wedhorn, *Algebraic Geometry I: Schemes*](https://link.springer.com/book/10.1007/978-3-658-30733-2) | Linear, systematic, and cleanly organized. | Schemes, fiber products, local properties, finite and proper maps, and flatness; also excellent for repairing gaps in a first course. |
| [J. S. Milne, *Algebraic Geometry*](https://www.jmilne.org/math/CourseNotes/ag.html) | Concise notes with direct proofs and unusually little rhetorical overhead. | A second route through varieties and schemes, or a quick reference when the main line of an argument matters more than encyclopedic coverage. |
| [Allen Altman and Steven Kleiman, *A Term of Commutative Algebra*](https://www.centerofmath.org/textbooks/commalgebra/) | Compact, free, and accompanied by solutions. | A smaller foundational course before the heavier homological machinery. |
| [Charles Weibel, *An Introduction to Homological Algebra*](https://doi.org/10.1017/CBO9781139644136) | A precise working reference once derived functors become unavoidable. | Resolutions, \(\operatorname{Tor}\), \(\operatorname{Ext}\), and spectral sequences. |

Eisenbud together with Vakil, Görtz--Wedhorn, or Milne is more than enough
general preparation. Read by live question: a chapter, theorem, or worked
example is usually the useful unit. The subject does not check which ISBN
supplied the background.

## The Jacobian problem itself

The classical literature supplies polynomial automorphisms, reductions,
formal inversion, stabilization, and the geometry of the plane problem.

| Resource | Why read it | Historical caveat |
| --- | --- | --- |
| [Arno van den Essen, *Polynomial Automorphisms and the Jacobian Conjecture*](https://link.springer.com/book/10.1007/978-3-0348-8440-2) | The best first map of the traditional subject and its techniques. | Published in 2000; the all-dimensional status discussion is now historical. |
| [Bass, Connell, and Wright, “The Jacobian conjecture: reduction of degree and formal expansion of the inverse”](https://doi.org/10.1090/S0273-0979-1982-15032-7) | The foundational source for stable degree reduction and cubic-homogeneous normal forms. | Read it when the reduction itself has become your question. |
| [Van den Essen, Kuroda, and Crachiola, *Polynomial Automorphisms and the Jacobian Conjecture: New Results from the Beginning of the 21st Century*](https://link.springer.com/book/10.1007/978-3-030-60535-3) | A useful sequel surveying later classical developments. | Also predates the 2026 counterexample. |
| [Masayoshi Miyanishi, *Lectures on Geometry and Topology of Polynomials—Surrounding the Jacobian Conjecture*](https://arxiv.org/abs/1504.07179) | The geometric route through affine surfaces, topology, and behavior at infinity. | Especially valuable for the surviving plane problem. |
| [The six mathematical-ideas essays](../ideas/index.md) | The fastest orientation to the vocabulary used in this guide. | They prepare a proof route; the linked sources supply the full theory. |

## When one phrase is blocking the argument

A short explanation should come first, a working text second, and a maximal
reference when the theorem and its hypotheses have become precise.

| Phrase | First contact | Working source |
| --- | --- | --- |
| **Finite maps, étale maps, normalization** | [Normalization](../ideas/normalization.md) and [local versus global](../ideas/local-and-global.md) | Vakil or Görtz--Wedhorn; then [the Stacks Project](https://stacks.math.columbia.edu/) for exact statements |
| **Syzygies, resolutions, Betti numbers** | [Roger Wiegand, “What Is a Syzygy?”](https://www.ams.org/notices/200604/what-is.pdf) | Eisenbud; Weibel for the abstract homological machinery |
| **Spectral sequences** | [Timothy Chow, “You Could Have Invented Spectral Sequences”](https://www.ams.org/notices/200601/fea-chow.pdf) | [Vakil, “Spectral Sequences: Friend or Foe?”](https://math.stanford.edu/~vakil/0708-216/216ss.pdf), then Weibel |
| **Cohen--Macaulay, Gorenstein, canonical modules** | [Craig Huneke, “Hyman Bass and Ubiquity: Gorenstein Rings”](https://arxiv.org/abs/math/0209199) | Eisenbud, then [Bruns--Herzog, *Cohen--Macaulay Rings*](https://www.cambridge.org/core/books/cohenmacaulay-rings/938BC2204D8A7C99E2CEBA1695A692A4) |
| **Local cohomology** | [Craig Huneke, *Lectures on Local Cohomology*](https://doi.org/10.1090/conm/436/08404) | Eisenbud or Bruns--Herzog, then Stacks |
| **Integral closure, valuations, conductors, Rees algebras** | [Normalization](../ideas/normalization.md) | Eisenbud, then [Swanson--Huneke, *Integral Closure of Ideals, Rings, and Modules*](https://www.math.purdue.edu/~iswanso/book/index.html) |
| **Deformations and obstructions** | [Brian Osserman, *A Glimpse of Deformation Theory*](https://www.math.ucdavis.edu/~osserman/classes/256A/notes/deform.pdf) | [Hartshorne, *Deformation Theory*](https://link.springer.com/book/10.1007/978-1-4419-1596-2) or Greuel--Lossen--Shustin |
| **The cotangent complex** | [MathOverflow: “What does the cotangent complex measure?”](https://mathoverflow.net/questions/2607/intuition-about-the-cotangent-complex) | [Gabriele Vezzosi's short note](https://arxiv.org/abs/1008.0601), then Stacks and Illusie as needed |
| **Singularities and local algebras** | Work through explicit plane curves and Artinian rings | [Greuel--Lossen--Shustin, *Introduction to Singularities and Deformations*](https://link.springer.com/book/10.1007/978-3-031-86043-0) |
| **Invariant theory and binary forms** | Compute with binary quadratics and cubics | [Igor Dolgachev, *Lectures on Invariant Theory*](https://doi.org/10.1017/CBO9780511615436) |
| **Gröbner bases and exact computation** | [Bernd Sturmfels, “What Is a Gröbner Basis?”](https://math.berkeley.edu/~bernd/what-is.pdf) | Greuel--Pfister or Cox--Little--O'Shea; then [Macaulay2](https://macaulay2.com/) or [SINGULAR](https://www.singular.uni-kl.de/) documentation |
| **Newton polygons and Puiseux series** | [Newton--Puiseux](../ideas/newton-puiseux.md) | Miyanishi and the sources linked from [the plane-case page](plane-case.md) |

The spectral-sequence row illustrates the intended progression. Chow makes the
construction feel inevitable, Vakil shows how an algebraic geometer uses it,
and Weibel supplies the formal convergence machinery. These are different
jobs, and the order matters.

## Free courses worth treating as courses

### Written courses

- [Vakil's final *Rising Sea* notes](https://math.stanford.edu/~vakil/216blog/)
  form a complete graduate algebraic-geometry course. Work a serious sample of
  the exercises; many of the best explanations happen there.
- [Altman--Kleiman](https://www.centerofmath.org/textbooks/commalgebra/)
  provides a compact commutative-algebra course with complete solutions.
- [Johan de Jong's commutative-algebra course](https://www.math.columbia.edu/~dejong/courses/commutative_algebra_old/index.html)
  develops the useful reflex of translating geometry to affine algebra and
  back again.
- [MIT OpenCourseWare 18.725](https://ocw.mit.edu/courses/18-725-algebraic-geometry-fall-2015/)
  includes graduate notes and problem sets on finite morphisms,
  differentials, smoothness, derived functors, and cohomology.
- [Vakil's deformation-course archive](https://math.stanford.edu/~vakil/727/index.html)
  is particularly useful once a concrete deformation problem is already in
  view.

### Video companions

- [Richard Borcherds's commutative-algebra lectures](https://www.youtube.com/playlist?list=PL8yHsr3EFj53rSexSz7vsYt-3rpHPR3HB)
  broadly follow Eisenbud.
- His [varieties course](https://www.youtube.com/playlist?list=PL8yHsr3EFj53j51FG6wCbQKjBgpjKa5PX)
  and [schemes course](https://www.youtube.com/playlist?list=PL8yHsr3EFj50Un2NpfPySgXctRQK7CLG-)
  form a graduate algebraic-geometry sequence.

Video works best with paper nearby. Pause before the lecturer completes a
calculation and try to finish it.

## How to use the famous references

### Hartshorne

Hartshorne remains a common language, a rich source of problems, and a concise
reference. Vakil or Görtz--Wedhorn usually provides more connective tissue for
a first encounter; Hartshorne becomes increasingly valuable as the literature
starts citing it directly.

### Atiyah--Macdonald

*Introduction to Commutative Algebra* is short in pages and large in
exercises. Mastery of those exercises gives excellent foundations. The later
parts of this guide also use resolutions, local cohomology, Cohen--Macaulay
theory, and duality, for which Eisenbud and specialist texts provide the next
stage.

### The Stacks Project and EGA

Use the Stacks Project once your question has a precise noun and a list of
hypotheses. Search for the construction, follow the tags backward, and stop
when the needed implication is secure. EGA is most efficient when a modern
source points to a specific theorem or when the original formulation matters.

### Bruns--Herzog, Huneke--Swanson, and Illusie

These are specialist references. Bruns--Herzog becomes natural when depth,
canonical modules, and local duality recur. Huneke--Swanson becomes natural
when normalization, valuations, conductors, or Rees algebras drive the
argument. Illusie becomes natural after explicit square-zero extensions and
the elementary cotangent-complex examples have made the general theorem
desirable.

### Van den Essen

Van den Essen is the field guide to the classical Jacobian problem. It is the
right place for traditional reductions, polynomial automorphisms, and the
pre-2026 research landscape. General commutative algebra and algebraic
geometry still supply the background language in which those results live.

## Four routes through the material

### Understand the story

Read [the conjecture](../start/conjecture.md),
[the counterexample](../start/counterexample.md),
[three views of the example](../start/three-views.md), and
[the marked-root geometry](marked-root-geometry.md). Then choose the
[idea essay](../ideas/index.md) that answers the question you now have.

### Check technical proofs

Use Eisenbud for commutative algebra, Vakil or Görtz--Wedhorn for schemes, and
Stacks for exact hypotheses. Add van den Essen when a proof uses classical
Jacobian reductions or polynomial-automorphism theory.

### Work on covers, normalization, or boundary geometry

Learn finite and étale maps, normalization, conductors, flatness, and local
cohomology. Huneke--Swanson and Bruns--Herzog are the natural specialist
references; Miyanishi supplies the geometric plane direction.

### Work on deformations or exact computation

Start with Osserman's overview, then use Hartshorne or
Greuel--Lossen--Shustin. Learn one computer algebra system well—usually
Macaulay2 or SINGULAR—and state exactly what each computation certifies.

## A final reading principle

Some sources explain why an idea was invented. Others train you to calculate
with it. A third kind gives the definitive theorem once you already know what
you need. Good mathematical reading consists largely in reaching for the
right kind at the right moment.
