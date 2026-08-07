---
title: "Background reading: enough to start, and what to grab when stuck"
description: "An opinionated guide to books, course notes, lectures, references, and short essays for readers of the Jacobian-conjecture guide."
---

# Background reading: enough to start, and what to grab when stuck

You do **not** need to read Hartshorne before using this site. You do not need
to “finish commutative algebra.” For most pages, the best preparation is to
start reading and follow whatever question catches.

Technical pages are a different story, but the honest prerequisite list is
still fairly short:

> A solid course in commutative algebra, plus a serious first course on
> schemes, is enough general background for almost everything here.

Eisenbud plus Vakil or Görtz--Wedhorn is more than enough. Not every chapter;
not every exercise; certainly not a ceremonial march from page 1 to page 700.
You should be comfortable with localization, integral extensions,
normalization, flatness, dimension, schemes, fiber products, finite and étale
maps, free resolutions, and basic \(\operatorname{Tor}\) and
\(\operatorname{Ext}\).

Everything else can be learned when it becomes useful. Local cohomology,
canonical modules, cotangent complexes, deformation functors, Rees algebras,
and invariant theory are tools, not bouncers at the door.

!!! important "One date warning"

    Almost every classical source below was written when the Jacobian
    conjecture was still described as open in every dimension. It was open
    when the author wrote that sentence. The mathematics remains useful; the
    status paragraph is now history. For the current picture, see the
    [conjecture page](../start/conjecture.md), the
    [three-dimensional counterexample](../start/counterexample.md), and the
    [surviving plane problem](plane-case.md).

## The core shelf

Here is the non-ceremonial version of the standard recommendations.

| Resource | My take | Use it for |
| --- | --- | --- |
| [David Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry*](https://link.springer.com/book/10.1007/978-1-4612-5350-1) | **The best single match for this guide.** Big, humane, geometric, and full of the algebra that actually turns up here. | Integral dependence, dimension, differentials, flatness, resolutions, duality, Gröbner methods, and the algebra--geometry dictionary. Read by topic. |
| [Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*](https://math.stanford.edu/~vakil/216blog/) | **The schemes course I would most readily hand to a motivated reader.** It explains why things are being invented, and it expects you to work. | A full first course in modern algebraic geometry. The free final notes and the published 2025 book have essentially the same mathematical content. |
| [Ulrich Görtz and Torsten Wedhorn, *Algebraic Geometry I: Schemes*](https://link.springer.com/book/10.1007/978-3-658-30733-2) | **More linear and systematic than Vakil.** Often the better choice when you want a clean account rather than a mathematical expedition. | Schemes, fiber products, local properties, finite and proper maps, and flatness. Also a very good place to repair shaky foundations. |
| [Allen Altman and Steven Kleiman, *A Term of Commutative Algebra*](https://www.centerofmath.org/textbooks/commalgebra/) | **Compact, free, and unusually useful.** A much smaller commitment than Eisenbud, with solutions. | The foundational commutative algebra you want before the homological machinery arrives. |
| [Charles Weibel, *An Introduction to Homological Algebra*](https://doi.org/10.1017/CBO9781139644136) | **Keep it nearby; do not feel obliged to consume it whole.** | Derived functors, resolutions, \(\operatorname{Tor}\), \(\operatorname{Ext}\), and spectral sequences when the bookkeeping becomes real. |

If you learned this material elsewhere, that is fine. Mathematics does not
check ISBNs.

## Reading about the Jacobian problem itself

These are the books and papers for the classical subject: polynomial
automorphisms, reductions, inversion, stabilization, and the geometry around
the conjecture.

| Resource | My take | Caveat |
| --- | --- | --- |
| [Arno van den Essen, *Polynomial Automorphisms and the Jacobian Conjecture*](https://link.springer.com/book/10.1007/978-3-0348-8440-2) | **The obvious first specialist book.** It is still the best map of the classical territory. | Published in 2000, so its status discussion predates the counterexample. |
| [Hyman Bass, Edwin Connell, and David Wright, “The Jacobian conjecture: reduction of degree and formal expansion of the inverse”](https://doi.org/10.1090/S0273-0979-1982-15032-7) | **The foundational reduction paper.** Read it when cubic-homogeneous reduction, stabilization, or the formal inverse is actually your problem. | It is a paper, not a warm-up exercise. There is no prize for reading it too early. |
| [Arno van den Essen, Shigeru Kuroda, and Anthony Crachiola, *Polynomial Automorphisms and the Jacobian Conjecture: New Results from the Beginning of the 21st Century*](https://link.springer.com/book/10.1007/978-3-030-60535-3) | **A useful sequel, not a replacement for the first book.** | Also predates 2026. |
| [Masayoshi Miyanishi, *Lectures on Geometry and Topology of Polynomials—Surrounding the Jacobian Conjecture*](https://arxiv.org/abs/1504.07179) | **The geometric route, especially for the plane case and behavior at infinity.** | Less interested in the general reduction industry; much more interested in affine geometry. That is often a virtue. |
| [The six mathematical-ideas essays in this guide](../ideas/index.md) | **The quickest orientation.** | They tell you what the objects are trying to do. They do not replace proofs. |

## When a phrase is stopping you

Do not respond to every unfamiliar noun by assigning yourself a semester-long
course. Try the short thing first. If the idea sticks, move to the working
source. Go to the heavy reference when you have a specific theorem to check.

| The phrase causing trouble | Read this first | Then settle in with |
| --- | --- | --- |
| **Schemes, finite maps, étale maps, normalization** | [Normalization](../ideas/normalization.md) and [local versus global](../ideas/local-and-global.md) in this guide | Vakil or Görtz--Wedhorn; then [the Stacks Project](https://stacks.math.columbia.edu/) when you need the exact theorem and all its hypotheses |
| **Syzygies, resolutions, Betti numbers, \(\operatorname{Ext}\)** | [Roger Wiegand, “What Is a Syzygy?”](https://www.ams.org/notices/200604/what-is.pdf) | Eisenbud; Weibel for the abstract homological machinery; Eisenbud's *The Geometry of Syzygies* if this becomes a main subject rather than a tool |
| **Spectral sequences** | [Timothy Chow, “You Could Have Invented Spectral Sequences”](https://www.ams.org/notices/200601/fea-chow.pdf) | [Vakil, “Spectral Sequences: Friend or Foe?”](https://math.stanford.edu/~vakil/0708-216/216ss.pdf), then Weibel for convergence and formalism |
| **Cohen--Macaulay, Gorenstein, canonical module, local duality** | [Craig Huneke, “Hyman Bass and Ubiquity: Gorenstein Rings”](https://arxiv.org/abs/math/0209199) | Eisenbud first; then [Bruns--Herzog, *Cohen--Macaulay Rings*](https://www.cambridge.org/core/books/cohenmacaulay-rings/938BC2204D8A7C99E2CEBA1695A692A4) when these ideas are doing actual work |
| **Local cohomology** | [Craig Huneke, *Lectures on Local Cohomology*](https://doi.org/10.1090/conm/436/08404) | Eisenbud or Bruns--Herzog, then Stacks for exact formulations |
| **Integral closure, Rees algebras, valuations, conductors** | The [normalization essay](../ideas/normalization.md) | Selected Eisenbud chapters, then [Swanson--Huneke, *Integral Closure of Ideals, Rings, and Modules*](https://www.math.purdue.edu/~iswanso/book/index.html); the author page includes a free version |
| **Deformations and obstructions** | [Brian Osserman, *A Glimpse of Deformation Theory*](https://www.math.ucdavis.edu/~osserman/classes/256A/notes/deform.pdf) | [Hartshorne, *Deformation Theory*](https://link.springer.com/book/10.1007/978-1-4419-1596-2), then Stacks when the setup becomes precise |
| **The cotangent complex** | [MathOverflow: “What does the cotangent complex measure?”](https://mathoverflow.net/questions/2607/intuition-about-the-cotangent-complex) | [Gabriele Vezzosi's short note](https://arxiv.org/abs/1008.0601), then Stacks. Open Illusie when you already know exactly why you are opening Illusie. |
| **Singularities, local algebras, explicit deformations** | Start with examples. Really. | [Greuel--Lossen--Shustin, *Introduction to Singularities and Deformations*](https://link.springer.com/book/10.1007/978-3-031-86043-0), which is both readable and substantial, and connects naturally to SINGULAR |
| **Invariant theory and binary forms** | Compute with binary quadratics, cubics, or sextics before going abstract | [Igor Dolgachev, *Lectures on Invariant Theory*](https://doi.org/10.1017/CBO9780511615436); Mumford--Fogarty--Kirwan if geometric invariant theory becomes central |
| **Gröbner bases and exact computation** | [Bernd Sturmfels, “What Is a Gröbner Basis?”](https://math.berkeley.edu/~bernd/what-is.pdf) | Greuel--Pfister or Cox--Little--O'Shea; then the [Macaulay2](https://macaulay2.com/) or [SINGULAR](https://www.singular.uni-kl.de/) documentation, plus a proof of what the computation actually certifies |
| **Plane geometry at infinity, Newton polygons, Puiseux series** | [Newton--Puiseux](../ideas/newton-puiseux.md) in this guide | Miyanishi, then the original papers linked from the [plane-case page](plane-case.md) |

The spectral-sequence row is a good model for the whole table. Chow explains
why the machine is natural. Vakil shows it in the sort of environment an
algebraic geometer actually meets. Weibel tells you exactly what the machine
is allowed to do. You may eventually need all three, but not in the opposite
order unless you enjoy preventable suffering.

## Free courses that are actually worth treating as courses

### Written courses

- [Vakil's final *Rising Sea* notes](https://math.stanford.edu/~vakil/216blog/)
  are a complete graduate algebraic-geometry course. The exercises are not
  decorative. Skipping all of them is like reading a cookbook while refusing
  to enter the kitchen.
- [Altman--Kleiman](https://www.centerofmath.org/textbooks/commalgebra/) is a
  compact commutative-algebra course with complete solutions. This is a very
  good choice when you want a course, not a 700-page relationship.
- [Johan de Jong's commutative-algebra course](https://www.math.columbia.edu/~dejong/courses/commutative_algebra_old/index.html)
  has the right reflex for this subject: translate geometry into affine
  commutative algebra, solve the algebra, translate back.
- [MIT OpenCourseWare 18.725](https://ocw.mit.edu/courses/18-725-algebraic-geometry-fall-2015/)
  includes graduate notes and problem sets on finite morphisms,
  differentials, smoothness, derived functors, and cohomology.
- [Vakil's deformation-course archive](https://math.stanford.edu/~vakil/727/index.html)
  contains good examples, handouts, and a frank annotated bibliography. It is
  incomplete as a stand-alone text, but excellent when you already have a
  deformation question in hand.

### Video companions

- [Richard Borcherds's commutative-algebra lectures](https://www.youtube.com/playlist?list=PL8yHsr3EFj53rSexSz7vsYt-3rpHPR3HB)
  broadly follow Eisenbud and are useful when the book's explanation has not
  landed on the first try.
- His [varieties course](https://www.youtube.com/playlist?list=PL8yHsr3EFj53j51FG6wCbQKjBgpjKa5PX)
  and [schemes course](https://www.youtube.com/playlist?list=PL8yHsr3EFj50Un2NpfPySgXctRQK7CLG-)
  form a graduate algebraic-geometry sequence.

Videos are companions, not intravenous mathematics. Pause, calculate, and do
some exercises.

## Famous recommendations, translated into English

### Hartshorne's *Algebraic Geometry*

Hartshorne is a common language, not a toll booth. It is concise, powerful,
and packed with exercises from which generations of algebraic geometers have
learned a great deal. It is also not always the nicest first person to ask
“why are we doing this?”

Use Hartshorne as a reference, a source of problems, and a way to communicate
with the literature. Use Vakil or Görtz--Wedhorn when you want more connective
tissue.

### Atiyah--Macdonald

Tiny book; enormous exercises; no wasted motion. If you genuinely know
*Introduction to Commutative Algebra*, your foundations are in good shape.
But it does not carry you through all the resolutions, local cohomology,
Cohen--Macaulay theory, and duality that show up later.

It is a superb book. It is not secretly 130 pages long; the exercises count.

### The Stacks Project and EGA

The Stacks Project is not something you “read.” It is where you go once your
question has become precise enough to have hypotheses. Search for the exact
construction, follow the tags backward, and stop when you have what you need.

EGA is foundational and still worth consulting when a modern source points to
a specific result. Reading EGA straight through is a different hobby from
learning the background for this guide.

### Bruns--Herzog and Huneke--Swanson

These are specialist books, and very good ones. Open Bruns--Herzog when depth,
canonical modules, or local duality have become recurring characters. Open
Huneke--Swanson when normalization, Rees algebras, valuations, or conductors
are no longer a one-page detour.

Do not assign yourself either book merely because one technical page contains
the relevant noun.

### Illusie

Illusie is where the full cotangent-complex theory lives. It is not where the
cotangent complex should first enter your life. Begin with square-zero
extensions, explicit deformation problems, and the elementary cases. Then use
Stacks. Then, when a precise general theorem forces the issue, use Illusie.

### Van den Essen

Van den Essen is the field guide to the classical Jacobian problem and
polynomial automorphisms. It tells you what the traditional landscape looks
like. It does not replace commutative algebra or algebraic geometry, and it
should not be mistaken for a prerequisite to reading the introductory pages
of this site.

## Four plausible routes

### I want to understand the story

Read the [conjecture](../start/conjecture.md), the
[counterexample](../start/counterexample.md), the
[marked-root geometry](marked-root-geometry.md), and then whichever
[mathematical-ideas essay](../ideas/index.md) answers the question you now
have. This route requires curiosity, not a graduate transcript.

### I want to check technical proofs

Use Eisenbud for the commutative algebra, Vakil or Görtz--Wedhorn for schemes,
and Stacks for exact statements. Add van den Essen when the argument touches
the classical Jacobian reductions or polynomial automorphism literature.

### I want to work on covers, normalization, or boundary geometry

Learn finite and étale maps, normalization, conductors, flatness, and local
cohomology. Huneke--Swanson and Bruns--Herzog are the natural specialist
references. Add Miyanishi for the geometric plane direction.

### I want to work on deformations or exact computation

Start with Osserman's short overview, then Hartshorne or
Greuel--Lossen--Shustin. Learn one computer algebra system well—usually
Macaulay2 or SINGULAR—and be painfully explicit about what each computation
proves. A matrix passed a test is not automatically a theorem about every
presentation in nature.

## Where the opinions came from

I used publisher and author pages to check editions, scope, and availability.
I also looked at what mathematicians say when someone asks the more useful
question: “What should I read first?” Community discussions are good evidence
about pedagogy and common use. They are not evidence that a theorem is true.

- [MathOverflow: “Best algebraic geometry textbook other than Hartshorne?”](https://mathoverflow.net/questions/2446/best-algebraic-geometry-textbook-other-than-hartshorne)
- [Mathematics Stack Exchange: “Utilitarian introduction to commutative algebra”](https://math.stackexchange.com/questions/3587399/utilitarian-introduction-to-commutative-algebra)
- [MathOverflow: “Reference book for commutative algebra”](https://mathoverflow.net/questions/16416/reference-book-for-commutative-algebra)
- [Mathematics Stack Exchange: “On the Jacobian Conjecture”](https://math.stackexchange.com/questions/255479/on-the-jacobian-conjecture)
- [Mathematics Stack Exchange: “Idea about syzygy”](https://math.stackexchange.com/questions/2465385/idea-about-syzygy)
- [MathOverflow: “Intuition about the cotangent complex?”](https://mathoverflow.net/questions/2607/intuition-about-the-cotangent-complex)

There is no universally best book here. There are books that explain an idea,
books that train you to use it, and books that tell you the exact theorem once
you already know what you are looking for. The trick is reaching for the
right one at the right time.
