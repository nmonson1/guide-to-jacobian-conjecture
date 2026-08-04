---
title: "Socle"
description: "The Cohen--Macaulay type is\n\\[\n\\dim_\\mathbb Q\\operatorname{Soc}(R)=60.\n\\]\nThe associated-graded socle dimensions occur as\n\\[\n\\dim\\frac{\\operatorname{Soc}(R)\\cap\\mathfrak m^d}\n{\\operatorname{Soc}(R)\\cap\\mathfrak m^{d+1}}\n=\n\\begin{cases}\n2,&d=5,\\\\\n33,&d=6,\\\\\n22,&d=7,\\\\\n3,&d=8,\\\\\n0,&\\text{otherwise}.\n\\end{cases}\n\\]\nIn particular, \\(R\\) is neither Gorenstein nor level."
---

# Socle

`RMU-AF82754A` · `corollary` · statement version `1`

## Exact statement

The Cohen--Macaulay type is
\[
\dim_\mathbb Q\operatorname{Soc}(R)=60.
\]
The associated-graded socle dimensions occur as
\[
\dim\frac{\operatorname{Soc}(R)\cap\mathfrak m^d}
{\operatorname{Soc}(R)\cap\mathfrak m^{d+1}}
=
\begin{cases}
2,&d=5,\\
33,&d=6,\\
22,&d=7,\\
3,&d=8,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, \(R\) is neither Gorenstein nor level.

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMUAF82754A-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

Macaulay duality gives a perfect pairing
\[
\operatorname{Soc}(R)\times D/\mathfrak mD\longrightarrow\mathbb Q.
\]
The filtered statement follows from
\[
F_dD=(\mathfrak m^{d+1})^\perp
\]
and the top-degree distribution in \cref{thm:inverse}.  Type 60 excludes
Gorensteinness, while the occurrence of socle classes in four distinct
\(\mathfrak m\)-adic degrees excludes levelness.

[Machine-readable graph](../graph.json)
