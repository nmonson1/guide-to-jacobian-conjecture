---
title: "Corrected divisorial classification"
description: "At the geometric generic point of every prime divisor \\(H\\subset Y\\), exactly\none of the following types occurs:\n\\begin{enumerate}[label=\\(U_\\arabic*\\),start=0]\n\\item all three sheets are unramified and retained;\n\\item all three sheets are unramified and exactly one is deleted;\n\\item all three sheets are unramified and exactly two are deleted;\n\\end{enumerate}\nor\n\\begin{description}\n\\item[\\(B\\)] the inertia is a transposition, the ramified point is deleted,\nand the unramified point is retained.\n\\end{description}\nOutside \\(S_F\\) only \\(U_0\\) occurs, while at the generic point of a divisor\ncontained in \\(S_F\\) only \\(U_1,U_2,B\\) occur.  In particular, a deleted\nthree-cycle cannot occur.  The Galois closure of the generic cubic extension\nhas group \\(S_3\\)."
---

# Corrected divisorial classification

`RMU-C1DD871B` · `proposition` · statement version `2`

## Exact statement

At the geometric generic point of every prime divisor \(H\subset Y\), exactly
one of the following types occurs:
\begin{enumerate}[label=\(U_\arabic*\),start=0]
\item all three sheets are unramified and retained;
\item all three sheets are unramified and exactly one is deleted;
\item all three sheets are unramified and exactly two are deleted;
\end{enumerate}
or
\begin{description}
\item[\(B\)] the inertia is a transposition, the ramified point is deleted,
and the unramified point is retained.
\end{description}
Outside \(S_F\) only \(U_0\) occurs, while at the generic point of a divisor
contained in \(S_F\) only \(U_1,U_2,B\) occur.  In particular, a deleted
three-cycle cannot occur.  The Galois closure of the generic cubic extension
has group \(S_3\).

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMUC1DD871B-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

The omitted set has codimension at least two by the elementary argument in the
proof of \cref{thm:omitted-singular}.  Hence the geometric generic point of
\(H\) has at least one preimage in \(X\).  Because \(F\) is étale, any
retained branch is unramified.  In the permutation action on the three sheets,
the divisorial inertia group must therefore fix a sheet.  Its only
possibilities are the trivial group and a transposition.

For trivial inertia all three sheets are unramified, and at least one is
retained; this gives \(U_0,U_1,U_2\).  For transposition inertia, the orbit of
size two is ramified and therefore cannot meet \(X\), whereas the fixed sheet
must be retained because the generic point of \(H\) is not omitted.  This is
type \(B\).  A three-cycle has no fixed sheet and is impossible.  Moreover,
\(H\not\subset S_F\) precisely when no sheet is generically deleted and no
ramification occurs, which is type \(U_0\).

The cubic field extension has transitive Galois group, hence its Galois
closure group is either \(C_3\) or \(S_3\).  If it were \(C_3\), every
nontrivial inertia group would be a three-cycle, which was just excluded.
Thus the finite normalization would be unramified in codimension one.  Purity
of the branch locus (Stacks Project, Lemma 58.21.4, Tag
\href{https://stacks.math.columbia.edu/tag/0BMB}{0BMB}) would make it finite
étale over \(\A^3\).  By comparison with the simply connected analytic
space \(\C^3\), affine three-space has no nontrivial connected finite
étale cover.  This contradicts the degree-three field extension.
Therefore the Galois group is \(S_3\).

[Machine-readable graph](../graph.json)
