---
title: "Rank-one wall obstruction"
description: "Let \\(R\\) be a DVR with uniformizer \\(\\pi\\), let \\(e\\ge 1\\), and let\n\\[\nK_e=\\operatorname{Spec} R[s]/(\\pi^es)\n\\]\nact on \\(\\mathbb A^1_R\\) by translation.  Its fppf orbit sheaf is not an algebraic\nspace, and the quotient stack is not an algebraic stack.  Consequently the\nbounded cubic-frame fppf quotient has the same failure along its generic\none-root wall."
---

# Rank-one wall obstruction

`RMU-428FCD53` · `theorem` · statement version `1`

## Exact statement

Let \(R\) be a DVR with uniformizer \(\pi\), let \(e\ge 1\), and let
\[
K_e=\operatorname{Spec} R[s]/(\pi^es)
\]
act on \(\mathbb A^1_R\) by translation.  Its fppf orbit sheaf is not an algebraic
space, and the quotient stack is not an algebraic stack.  Consequently the
bounded cubic-frame fppf quotient has the same failure along its generic
one-root wall.

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMU428FCD53-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

For an \(R\)-algebra \(B\), one has
\(K_e(B)=\operatorname{Ann}_B(\pi^e)\), so the orbit presheaf is
\[
B/\operatorname{Ann}_B(\pi^e)\simeq\pi^eB.
\]
The image functor \(B\mapsto\pi^eB\) is already an fppf sheaf: faithful
flatness detects membership in the submodule \(\pi^eB\).

Set
\[
A'=A''=R/(\pi^{e+1}),\qquad A=R/(\pi^e),
\]
and form the standard Rim--Schlessinger pushout ring
\[
B=A'\times_AA''.
\]
Then \(F(A')=F(A'')\simeq k\), while \(F(A)=0\).  An element of \(B\) has
components congruent modulo \(\pi^e\); because \(e\ge1\), their residues
agree.  Consequently
\[
F(B)=\pi^eB\longrightarrow
F(A')\times_{F(A)}F(A'')\simeq k\oplus k
\]
has diagonal image and is not surjective.  Thus \(F\) fails the strong
Rim--Schlessinger condition, which algebraic stacks satisfy by
\cite[Lemma 98.18.2, Tag 0CXN]{stacks0CXN}.
The translation action is free, so its fppf quotient stack has trivial
inertia; if it were algebraic, it would be an algebraic space and would
coincide with the orbit sheaf, a contradiction.

For the cubic-frame consequence, restrict to a DVR at the generic point of
the one-root wall and, if needed, pass to an étale splitting extension.
Multiplication by \(z\) has one elementary divisor \(\pi\) and all others
units, so \(Z^N\) has Smith form
\(\operatorname{diag}(1,\ldots,1,\pi^N)\) up to units.  This gives the
rank-one action above with \(e=N\ge1\), times an unaffected affine factor;
the conclusion is only asserted on this generic wall neighborhood.

[Machine-readable graph](../graph.json)
