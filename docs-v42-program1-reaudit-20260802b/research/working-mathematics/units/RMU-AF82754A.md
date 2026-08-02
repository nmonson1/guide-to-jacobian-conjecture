# Socle

`RMU-AF82754A` · `corollary`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-AF82754A` · `corollary`

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

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

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

  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#cor:socle`](../../proof-sources/03-local-rigidity/main.md#label-cor-socle)
