---
title: "Over \\(\\mathbb Q(Z)\\), the matrix \\(A\\) has Jordan type \\((18,1)\\)."
description: "Over \\(\\mathbb Q(Z)\\), the matrix \\(A\\) has Jordan type \\((18,1)\\)."
---

# Over \(\mathbb Q(Z)\), the matrix \(A\) has Jordan type \((18,1)\).

`RMU-DF26626A` · `proposition` · statement version `1`

## Exact statement

Over \(\mathbb Q(Z)\), the matrix \(A\) has Jordan type \((18,1)\).

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMUDF26626A-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

Exact differentiation gives
\[
Av_1=Av_2=0.
\]
The vectors are generically independent, while the all-ones specialization
of \(A\) has rank 17.  Hence the generic kernel has dimension two.

Let \(e_t\) be the last coordinate vector.  Exact iteration gives
\begin{equation}
\label{eq:long-chain}
A^{17}e_t=18t^{15}x^9y^5z^2v_2\ne0.
\end{equation}
By \cref{thm:intro-suspension}, \(A\) is nilpotent.  A nilpotent
19-by-19 matrix with a two-dimensional kernel has two Jordan blocks, and
\eqref{eq:long-chain} forces the larger block to have size at least 18.
Thus the partition is \((18,1)\).

[Machine-readable graph](../graph.json)
