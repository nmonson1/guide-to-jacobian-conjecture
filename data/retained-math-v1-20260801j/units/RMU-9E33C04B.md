# Injectivity of the terminal layer maps

`RMU-9E33C04B` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-9E33C04B` · `proposition`

Assume \(p,q\) satisfy \eqref{eq:degree21-face}.  For \(r\ge5\), let
\[
a\in k[z]_{\le10-r},\qquad
b\in k[z]_{\le15-r},
\]
where a negative degree bound means the zero space.  Then
\[
\mathscr D_r^{2,3}(a,b)=0
\quad\Longrightarrow\quad
a=b=0.
\]
In particular, for \(5\le r\le11\),
\begin{equation}

\dim\operatorname{coker}\mathscr D_r^{2,3}=r-1.
\end{equation}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

At \(r=5\), put
\[
C=2A_0b-3B_0a.
\]
By resonance,
\(\mathscr D_5(a,b)=dC\).  If this vanishes, then \(C\) is constant; both
terms are divisible by \(z\), so \(C=0\).  Hence
\[
2pb=3zqa.
\]
Equation \eqref{eq:degree21-face} implies
\(\gcd(p,zq)=1\), so \(p\mid a\).  Since
\(\deg a\le5<7=\deg p\), one has \(a=0\), and then \(b=0\).

Now suppose \(r>5\), and set
\[
C=2A_0b-3B_0a,\qquad E=A_0b+B_0a.
\]
The gauge formula and \(\mathscr D_r(a,b)=0\) give
\begin{equation}
\label{eq:828-degree-identity}
E
=zpq\left(
C\frac{M_0'}{M_0}+\frac5{r-5}C'
\right).
\end{equation}
If \(C\ne0\) and \(d=\deg C\), the right side has degree exactly
\(d+17\): its leading coefficient contains the nonzero factor
\[
20+\frac{5d}{r-5}.
\]
On the other hand,
\[
\deg E\le
\max\{\deg A_0+\deg b,\deg B_0+\deg a\}
\le23-r.
\]
Thus \(d\le6-r\).  This is impossible for \(r\ge7\); for \(r=6\) it
forces \(d=0\), whereas \(C\) is divisible by \(z\).  Hence \(C=0\), and
the coprimality and degree argument above again gives \(a=b=0\).

For \(5\le r\le11\), \cref{prop:index} applies to the stated full-support
windows and gives the target-minus-domain dimension \(r-1\).
Injectivity proves \eqref{eq:828-cokernel-dimension}.

  - Full source and surrounding context: [`manuscripts/06-plane-boundary/appendices/exact-normal-linearization.tex#prop:828-layer-injectivity`](../../proof-sources/06-plane-boundary/appendices/exact-normal-linearization.md#label-prop-828-layer-injectivity)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
