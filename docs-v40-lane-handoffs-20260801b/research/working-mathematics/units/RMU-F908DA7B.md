# Global geometry of the coprime family

`RMU-F908DA7B` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-F908DA7B` · `theorem`

For an admissible triple satisfying \eqref{eq:coprime}:

\begin{enumerate}[label=(\roman*)]
\item the total space \(\widetilde X\) is smooth, and the projection
\(\pi\colon\widetilde X\to\A^3_{a,b,c}\) is finite flat of degree three;
\item there is an isomorphism
\begin{equation}

\A^3_{x,y,z}\simeq
\widetilde X\setminus
\left(R\cup\bigcup_{\substack{\beta\in Z(A)\\\beta\ne\alpha}}E_\beta\right);
\end{equation}
\item the branch discriminant is
\begin{equation}

\mathcal D=
B(c)^2b^2-4A(c)b^3+8aB(c)^3
-36aA(c)B(c)b-108a^2A(c)^2;
\end{equation}
\item the nonproperness set is
\begin{equation}

S_F=V(\mathcal D)\cup
\bigcup_{\substack{\beta\in Z(A)\\\beta\ne\alpha}}V(c-\beta);
\end{equation}
\item if
\[
T_3=
V\left(3A(c)b-B(c)^2,\,
54A(c)^2a+B(c)^3\right)
\]
and
\[
C_\beta=
V\left(c-\beta,\ b^2+8aB(\beta)\right),
\]
then
\begin{equation}

\A^3\setminus F(\A^3)=
T_3\cup\bigcup_{\beta\ne\alpha}C_\beta
=\Sing(S_F)_{\mathrm{red}}.
\end{equation}
\end{enumerate}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

The equation in \eqref{eq:completion} is a nonzero binary cubic on every
geometric target fiber: at a common zero of \(A\) and \(B\) this could fail,
but \eqref{eq:coprime} excludes such a point.  It therefore defines a
relative effective Cartier divisor of degree three in the trivial
\(\PP^1\)-bundle.  The divisor is proper with zero-dimensional fibers and
hence finite; the constant relative Hilbert polynomial makes it flat of
degree three.

The total space is smooth.  On \(S\ne0\), the partial derivative with
respect to \(a\) is \(-2S^3\).  If \(S=0\), then \(T\ne0\), \(A(c)=0\),
and \(B(c)\ne0\); the partial derivative with respect to \(S\) is
\(B(c)T^2\).

On the chart of finite simple roots, \eqref{eq:reconstruction} identifies
the incidence with the source.  The root at infinity over \(c=\alpha\) is
also simple because \(B(\alpha)=-2\), and
\cref{prop:keller-degree} identifies it with the plane \(x=0\).  At every
other zero \(\beta\) of \(A\), the simple infinity section \(E_\beta\) has
no affine source point.  The explicit inverse and its regular gluing along
the retained infinity section are proved in
\cref{lem:retained-infinity-gluing}; removing the other sections and the
repeated-root divisor gives \eqref{eq:source-open}.

The discriminant of \eqref{eq:inverse-cubic} is
\eqref{eq:discriminant}.  On the chosen-root incidence chart, put
\[
r=P'(t),\qquad
b=r-3A(c)t^2-2B(c)t,\qquad
a=-A(c)t^3-\frac12B(c)t^2+\frac12rt.
\]
Then
\begin{equation}
\label{eq:disc-pullback}
\pi^*\mathcal D
=r^2\left((3A(c)t+B(c))^2-4A(c)r\right).
\end{equation}
Thus \(R=\{r=0\}\simeq\A^2_{t,c}\), and its image is the branch
hypersurface \(V(\mathcal D)\).  Each deleted \(E_\beta\) maps
isomorphically to the plane \(c=\beta\), giving
\eqref{eq:nonproperness}.

A cubic on the branch hypersurface has one double and one simple root away
from \(T_3\); the double root lies in \(R\), while the simple root remains.
At \(T_3\) all three roots coincide and none remains in
\eqref{eq:source-open}.  On \(c=\beta\ne\alpha\), the infinity root is
deleted.  The remaining quadratic has a double root precisely on
\[
b^2+8aB(\beta)=0,
\]
because
\[
\mathcal D|_{c=\beta}
=B(\beta)^2\bigl(b^2+8aB(\beta)\bigr).
\]
This proves the first equality in \eqref{eq:omitted}.

Where \(A(c)\ne0\), depressing the cubic identifies its branch equation
transversely with a cusp; its singular locus is \(T_3\).  Along
\(c=\beta\), the branch hypersurface is smooth because
\[
\left.\frac{\partial\mathcal D}{\partial a}\right|_{A=0}
=8B(\beta)^3\ne0,
\]
and it meets the plane \(c=\beta\) transversely exactly along \(C_\beta\).
The reduced singular locus of the union \eqref{eq:nonproperness} is
therefore the right side of \eqref{eq:omitted}.

  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#thm:AB-global`](../../proof-sources/01-cubic-incidence/main.md#label-thm-ab-global)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
