# A full-rank square-zero pairing is stably right-equivalent

`RMU-A93DB097` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-A93DB097` · `proposition`

Suppose
\[
H(z)=B(Dz)^{*3},\qquad BD=0,
\]
where $B:W\to V$ is surjective and $D:V\to W$ is injective.  Put $A=DB$ and
$F_A(w)=w+(Aw)^{*3}$.  Choose a right inverse $C$ of $B$ and write
$W=C(V)\oplus E$, where $E=\ker B$.  Set
\[
\rho(z)=(Dz)^{*3}-CH(z)\in E.
\]
In the coordinates $w=Cz+\eta$, one has
\[
F_A(z,\eta)=\bigl(G(z),\eta+\rho(z)\bigr),
\qquad G=I+H.
\]
Precomposition by $(z,\eta)\mapsto(z,\eta-\rho(z))$ therefore changes $F_A$
into $G\times\id_E$.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md)
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
