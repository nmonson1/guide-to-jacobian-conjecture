# The cubic incidence open is affine three-space

`RMU-FA7978C0` · `proposition`

## Mathematical record

`RMU-FA7978C0` · `proposition`

For every tangent but nonosculating hyperplane \(H\) in the case
\(\{a,b\}=\{1,2\}\), one has
\[
U_{a,b,H}\simeq\A^3.
\]
This supplies the positive direction of \cref{thm:stable-uniqueness} without
an appeal to an unspecified public construction.

Dependencies:

- `uses` [`RMU-BA2C2F76`](../units/RMU-BA2C2F76.md): Formal statement references thm:stable-uniqueness.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Interchanging the two factors reduces to \((a,b)=(1,2)\).  Write a binary
cubic as
\[
f=A T^3+B S T^2+C S^2T+D S^3.
\]
At the point \([S^3]\) of the rational normal cubic, the tangent line is
spanned by \(S^3,S^2T\), and the osculating plane is spanned by
\(S^3,S^2T,ST^2\).  Hence a tangent nonosculating hyperplane has equation
\[
B+\lambda A=0
\]
after scaling.  The change \(T\mapsto T+\tau S\), which fixes \([S^3]\),
replaces \(B\) by \(B+3\tau A\).  Choosing \(\tau\) appropriately sends
\(H\) to \(V(B)\).  This proves the required transitivity directly.

On the complement of \(V(B)\), a projective product cubic \([LQ]\) has a
unique scalar representative with \(B=-2\).  Thus a point of
\(U_{1,2,H}\) is equivalently a cubic
\[
cT^3-2ST^2+bS^2T-2aS^3
\]
together with a marked linear factor \(L\), such that the residual quadratic
factor \(Q\) is coprime to \(L\).  Coprimality is exactly simplicity of the
marked root.  Therefore \(U_{1,2,H}\) is the marked-simple-root incidence
open \(\widetilde X\setminus R\) for the admissible triple
\[
A(c)=c,\qquad B(c)=-2,\qquad\alpha=0.
\]
Here \(A\) has no zero other than the marked one, so there are no deleted
sections \(E_\beta\) with \(\beta\ne\alpha\).  Applying
\cref{lem:retained-infinity-gluing} gives
\[
U_{1,2,H}=\widetilde X\setminus R\simeq\A^3.
\]

  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/audit-repairs.tex#prop:cubic-positive-internal`](../../proof-sources/01-cubic-incidence/appendices/audit-repairs.md#label-prop-cubic-positive-internal)
