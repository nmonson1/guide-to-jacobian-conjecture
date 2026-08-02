# For every \(\alpha,\beta\in\C\), the map \(G_{\alpha,\beta}\) is polynomial, \[ \det DG_{\alp…

`RMU-C933C1F1` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-C933C1F1` · `proposition`

For every \(\alpha,\beta\in\C\), the map \(G_{\alpha,\beta}\) is polynomial,
\[
\det DG_{\alpha,\beta}=-2,
\]
and its generic degree is three.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Set
\[
\xi=1+xy,\qquad d=2-3xy-x^2z,
\]
so that \(t=\xi/x\) and \(c=xd\).  Clearing denominators in \(b\) gives
\[
b=
\frac{2+4\xi-3d\xi^2}{x}
-3\alpha d^2\xi^2+8\alpha d\xi
-2\beta x d^2\xi.
\]
The numerator of the displayed fraction vanishes at \(x=0\), hence is
divisible by \(x\).  More explicitly,
\[
2+4\xi-3d\xi^2
=x\bigl(3x^3y^2z+9x^2y^3+6x^2yz+12xy^2+3xz+y\bigr).
\]
Similarly,
\[
2a=
\frac{2\xi-2d\xi^3+2\xi^2}{x^2}
+\frac{4\alpha d\xi^2-2\alpha d^2\xi^3}{x}
-\beta d^2\xi^2.
\]
Here
\[
2\xi-2d\xi^3+2\xi^2
=2x^2(1+xy)
 \bigl(x^2y^2z+3xy^3+2xyz+4y^2+z\bigr),
\]
while the second numerator is
\[
2\alpha d\xi^2(2-d\xi),\qquad
2-d\xi=x\bigl(x^2yz+3xy^2+xz+y\bigr).
\]
Thus \(a\) and \(b\) are polynomial.

On \(x\ne0\), the coordinate changes in \eqref{eq:frame} give
\[
\det\frac{\partial(a,b,c)}{\partial(t,r,c)}=\frac r2,
\qquad
\det\frac{\partial(t,r,c)}{\partial(x,y,z)}=-2x.
\]
Since \(r=2/x\), their product is \(-2\).  Polynomiality extends this
identity across \(x=0\).

For a target point \((a,b,c)\), introduce
\begin{equation}
\label{eq:fiber-cubic-general}
P_{a,b,c}(T)=A(c)T^3+B(c)T^2+bT-2a.
\end{equation}
The construction gives
\[
P_{G_{\alpha,\beta}(x,y,z)}(t)=0,\qquad
P'_{G_{\alpha,\beta}(x,y,z)}(t)=\frac2x.
\]
Conversely, every finite simple root \(t\) reconstructs
\begin{equation}
\label{eq:reconstruct}
x=\frac2{P'(t)},\qquad
y=t-\frac{P'(t)}2,\qquad
z=\frac{2x-3x^2y-c}{x^3}.
\end{equation}
A general cubic \eqref{eq:fiber-cubic-general} has three finite simple roots,
giving three source points.

  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#prop:basic`](../../proof-sources/04-stable-moduli/main.md#label-prop-basic)
