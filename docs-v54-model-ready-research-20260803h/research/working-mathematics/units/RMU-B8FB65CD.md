---
title: "The generic Jordan type of \\(\\operatorname{Hess}\\mathcal Q\\) is \\[ (35,2,1). \\]"
description: "The generic Jordan type of \\(\\operatorname{Hess}\\mathcal Q\\) is\n\\[\n(35,2,1).\n\\]"
---

# The generic Jordan type of \(\operatorname{Hess}\mathcal Q\) is \[ (35,2,1). \]

`RMU-B8FB65CD` · `proposition` · statement version `1`

## Exact statement

The generic Jordan type of \(\operatorname{Hess}\mathcal Q\) is
\[
(35,2,1).
\]

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMUB8FB65CD-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

Before the linear twist, the nonlinear Jacobian is
\[
N=
\begin{pmatrix}
A&0\\
\mathcal L&A^T
\end{pmatrix},
\qquad
A=JH(x),\qquad
\mathcal L=\operatorname{Hess}_x(y^TH(x)).
\]
The Hessian of \(\mathcal Q\) is similar to \(N\).

The kernel vectors \eqref{eq:v1}--\eqref{eq:v2} satisfy
\[
D^2H[v_1,v_2]=D^2H[v_2,v_2]=0.
\]
Since they span \(\ker A\) generically, this implies
\(\mathcal Lv_2\in\operatorname{im}A^T\).  In addition to the two kernel
vectors \((0,\ker A^T)\), the matrix \(N\) therefore has a kernel vector
whose first component is \(v_2\).  Hence \(\operatorname{rank}N\le35\).
An exact all-ones specialization has rank 35.

For \(k\ge1\), the lower-left block of \(N^k\) is
\[
\sum_{j=0}^{k-1}(A^T)^j\mathcal L A^{k-1-j}.
\]
Since \(A^{18}=0\), the only possible term for \(k=35\) is
\((A^T)^{17}\mathcal L A^{17}\).  The image of \(A^{17}\) is spanned by
\(v_2\), and \(D^2H[v_2,v_2]=0\), so this term vanishes.  Thus \(N^{35}=0\).
At the all-ones specialization,
\[
(N^{34})_{38,19}=648\ne0.
\]
The nilpotency index is 35 and the rank is 35, so there are three blocks.
The remaining three dimensions split as \(2+1\), proving the result.

[Machine-readable graph](../graph.json)
