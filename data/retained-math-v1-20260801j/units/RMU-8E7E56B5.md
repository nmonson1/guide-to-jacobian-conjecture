# Valuation over \(F_{-5}\)

`RMU-8E7E56B5` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-8E7E56B5` · `theorem`

Let \(E_\nu\) be the source divisor defined by \(\nu\).  Its target center is
Borisov's divisor \(F_{-5}\).  The normal ramification index and residue
degree are
\[
(e,f)=(1,21).
\]
Consequently neither surviving Newton support can realize Borisov's
Three-dessin framework.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Set \(t=Y\), so \(x=t^2/z\) in the original source coordinates.  The source
volume form is
\[
dx\wedge dy=t^{-6}z^2\,dt\wedge dz.
\]
After adding the reduced boundary coefficient, the augmented-canonical label
is \(-5\).

The face expansions are
\[
P=t^{-2}zp(z)+\text{higher \(\nu\)-terms},\qquad
Q=t^{-3}z^2q(z)+\text{higher \(\nu\)-terms}.
\]
On the target put
\[
s=\frac P Q,\qquad \lambda=\frac{Q^2}{P^3}.
\]
Then \(s\) is a uniformizer and
\[
dP\wedge dQ=-s^{-6}\lambda^{-3}\,ds\wedge d\lambda,
\]
so the target label is also \(-5\).  Pullback gives
\[
\frac P Q
=t\left(\frac{p(z)}{zq(z)}+O(t)\right),
\]
hence \(e=1\).  The residue of \(\lambda\) is
\[
\operatorname{res}_{E_\nu}(\lambda)
=z\frac{q(z)^2}{p(z)^3}=\tau(z),
\]
so \(f=21\) by \cref{prop:degree21-belyi}.

In Borisov's target coordinates \((y_1,y_2)=(Q,P)\), the divisor
\(F_{-5}\) is characterized by valuations \((-3,-2)\) and by the
nonconstant residual parameter \(y_1^2/y_2^3\).  Those are exactly the
values above.  Later infinitely-near divisors with the same two numerical
orders have constant residue of this parameter, so they are distinguished.

For clarity, the complete dictionary at the generic points is
\[
\begin{array}{c|c|c}
 & E_\nu\text{ on the source} & F_{-5}\text{ on the target}\\ \hline
\text{normal parameter} & t=Y & s=P/Q\\
\text{residual parameter} & z=XY^2 & \lambda=Q^2/P^3\\
\text{orders of }(P,Q) & (-2,-3) & (-2,-3)\\
\text{normal map} & s=t\bigl(p/(zq)+O(t)\bigr) & e=1\\
\text{residue map} & z\longmapsto zq^2/p^3 & f=21
\end{array}
\]
Equivalently, at the completed generic points the map has the form
\[
\operatorname{Spec}k(E_\nu)[[t]]
\ \xrightarrow{\quad s=t\,u(z,t),\ \lambda=\tau(z)+O(t)\quad}\
\operatorname{Spec}k(F_{-5})[[s]],
\]
where \(u(z,0)=p(z)/(zq(z))\) is a unit and
\([k(E_\nu):k(F_{-5})]=\deg\tau=21\).

Borisov's Three-dessin framework gives residue degree \(16\) on its unique
source divisor above \(F_{-5}\) \cite{borisov2020frameworks}.  The forced
divisor has residue degree
\(21\), a contradiction.  This excludes the named framework, not the two
supports themselves.

  - Full source and surrounding context: [`manuscripts/06-plane-boundary/appendices/degree-twenty-one-certificates.tex#thm:borisov-fminusfive`](../../proof-sources/06-plane-boundary/appendices/degree-twenty-one-certificates.md#label-thm-borisov-fminusfive)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
