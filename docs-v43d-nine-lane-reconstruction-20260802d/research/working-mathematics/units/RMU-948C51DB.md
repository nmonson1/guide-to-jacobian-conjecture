# The map \(F_A\colon\A^{110}\to\A^{110}\) is a noninjective Keller map. It is Gorni--Zampieri…

`RMU-948C51DB` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-948C51DB` · `proposition`

The map \(F_A\colon\A^{110}\to\A^{110}\) is a noninjective Keller map.
It is Gorni--Zampieri paired with \(G=I+H\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Choose a right inverse \(C\) of \(B\).  The exact data give \(AC=D\), and
\[
B F_A(Cz)=z+B(Dz)^{*3}=G(z).
\]
By Sylvester's determinant identity,
\begin{align*}
\det JF_A(W)
&=\det\left(I_{110}
+3\operatorname{diag}((AW)^2)DB\right)\\
&=\det\left(I_{19}
+3B\operatorname{diag}((DBW)^2)D\right)\\
&=\det JG(BW)=1.
\end{align*}

If \(G(z_1)=G(z_2)\), put \(u=Cz_1\), \(v=Cz_2\), and
\(\delta=F_A(u)-F_A(v)\).  Then \(B\delta=0\), hence
\(A\delta=DB\delta=0\).  Thus
\[
F_A(v+\delta)=F_A(v)+\delta=F_A(u).
\]
The exact collision certificate verifies \(u\ne v+\delta\).

  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#prop:pair110`](../../proof-sources/05-homogeneous-descendants/main.md#label-prop-pair110)
