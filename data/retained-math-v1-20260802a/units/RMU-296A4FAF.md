# Explicit gluing at the marked infinity section

`RMU-296A4FAF` · `lemma`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-296A4FAF` · `lemma`

For an admissible coprime triple, the morphism
\[
\jmath\colon\A^3_{x,y,z}\longrightarrow\widetilde X,
\qquad
(x,y,z)\longmapsto
\bigl(F(x,y,z),[x:1+xy]\bigr)
\]
is an isomorphism onto
\[
\widetilde X\setminus
\left(R\cup\bigcup_{\substack{\beta\in Z(A)\\\beta\ne\alpha}}E_\beta\right).
\]
In particular, this proves the gluing assertion in
\cref{thm:AB-global}(ii), including a neighborhood of \(x=0\).

Dependencies:

- `uses` `RMU-F908DA7B`: Formal statement references thm:AB-global.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

On \(x\ne0\), the marked point has affine coordinate
\[
t=\frac{T}{S}=\frac{1+xy}{x}=y+\frac1x.
\]
Multiplying \(P_{F(x,y,z)}(t)=0\) by \(x^3\) gives the homogeneous incidence
equation, so \(\jmath\) is a morphism; at \(x=0\) its marked point is
\([0:1]\).  On the finite-root chart \(S\ne0\), the inverse is exactly
\eqref{eq:reconstruction}.  It remains to check the neighborhood of the
infinity section \(E_\alpha\).

Work on the chart \(T=1\), and put \(u=S/T\).  The incidence equation is
\begin{equation}
\label{eq:infinity-incidence}
A(c)+B(c)u+bu^2-2au^3=0.
\end{equation}
Set
\[
\delta=-B(c)-2bu+6au^2.
\]
Using \eqref{eq:infinity-incidence} to eliminate \(A(c)\) gives
\[
P'(1/u)=\frac{\delta}{u}.
\]
Consequently the finite-root inverse rewrites as
\begin{equation}
\label{eq:infinity-inverse}
x=\frac{2u}{\delta},\qquad
y=\frac{2+B(c)+2bu-6au^2}{2u}.
\end{equation}
At \(E_\alpha\) one has \(u=0\), \(c=\alpha\), and
\(\delta=-B(\alpha)=2\), so \(\delta\) is a unit.  Moreover,
\eqref{eq:infinity-incidence} says
\[
A(c)=-u\bigl(B(c)+bu-2au^2\bigr).
\]
Since \(A(c)=(c-\alpha)A_\alpha(c)\) with
\(A_\alpha(\alpha)=A'(\alpha)\ne0\), it follows that
\(c-\alpha\in(u)\).  The numerator in the formula for \(y\) is therefore
divisible by \(u\), because \(B(\alpha)=-2\).  Thus both \(x\) and \(y\)
are regular near \(E_\alpha\), and \(x/u\) is a unit.

It remains only to verify regularity of
\[
z=\frac{w(x,y)-c}{x^3}.
\]
Write
\[
A_1=A'(\alpha),\qquad A_2=A''(\alpha),\qquad B_1=B'(\alpha).
\]
Expansion of \eqref{eq:infinity-incidence} modulo \(u^3\), followed by
\eqref{eq:infinity-inverse}, gives in the local ring along \(E_\alpha\)
\begin{align*}
c&\equiv \alpha+\frac{2}{A_1}u+
\left(-\frac b{A_1}-\frac{2A_2}{A_1^3}
-\frac{2B_1}{A_1^2}\right)u^2\pmod{u^3},\\
x&\equiv u+\left(b+\frac{B_1}{A_1}\right)u^2\pmod{u^3},\\
y&\equiv b+\frac{B_1}{A_1}\pmod u.
\end{align*}
Substituting these congruences into the canonical jet
\eqref{eq:w-jet} yields
\[
w(x,y)\equiv c\pmod{u^3}.
\]
Since \(x/u\) is a unit, this is equivalent to
\(w(x,y)-c\in(x^3)\), so \(z\) is regular.

The formulas above define an inverse near \(E_\alpha\), and they agree with
\eqref{eq:reconstruction} on the dense overlap \(u\ne0\).  The finite-root
chart together with this neighborhood covers the claimed open: every point
with \(S=0\) lies on some \(E_\beta\), and all such sections except
\(E_\alpha\) have been removed.  Hence \(\jmath\) is the required
isomorphism.

  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/audit-repairs.tex#lem:retained-infinity-gluing`](../../proof-sources/01-cubic-incidence/appendices/audit-repairs.md#label-lem-retained-infinity-gluing)
