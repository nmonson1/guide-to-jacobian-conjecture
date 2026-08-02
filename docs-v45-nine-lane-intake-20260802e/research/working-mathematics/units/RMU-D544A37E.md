# Face-to-passport formula

`RMU-D544A37E` · `proposition`

## Mathematical record

`RMU-D544A37E` · `proposition`

The rational function \(\tau\) is a degree-\(mnb\) Belyi map and
\begin{equation}

\tau'(z)=z^{n-1}\frac{p(z)^{n-1}}{q(z)^{m+1}}.
\end{equation}
Its passport is
\begin{equation}

\left(n^{mb}\right),\qquad
\left(m^{nb}\right),\qquad
\left((m+n)b-1,1^{mnb-(m+n)b+1}\right).
\end{equation}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Logarithmic differentiation of \eqref{eq:ambient-tau} gives
\[
\tau'
=z^{n-1}\frac{p^{n-1}}{q^{m+1}}
\bigl(npq+nzp'q-mzpq'\bigr).
\]
Equation \eqref{eq:ambient-ode} yields
\eqref{eq:ambient-derivative}.

At \(z=0\), the face equation gives \(np(0)q(0)=1\).  At a zero
\(z_0\) of \(p\), it gives \(nz_0p'(z_0)q(z_0)=1\); hence the root is
simple, nonzero, and not a root of \(q\).  The analogous assertion follows
for roots of \(q\).  Thus the zero fiber of \(\tau\) has one point of
multiplicity \(n\) at zero and \(mb-1\) further points of multiplicity
\(n\).  The pole fiber consists of \(nb\) points of multiplicity \(m\).

The numerator and denominator of \(\tau\) are coprime and both have degree
\(mnb\), so \(\tau(\infty)\in k^\times\).  From
\eqref{eq:ambient-derivative},
\[
\tau'(z)=O\!\left(z^{-(m+n)b}\right)
\quad\text{as }z\longrightarrow\infty.
\]
Therefore
\[
\tau(z)-\tau(\infty)
=O\!\left(z^{-((m+n)b-1)}\right),
\]
with nonzero leading coefficient.  The ramification contributions already
identified total
\begin{align*}
mb(n-1)+nb(m-1)+((m+n)b-2)
=2mnb-2.
\end{align*}
Riemann--Hurwitz leaves no additional critical point.  The rest of the
\(\tau(\infty)\)-fiber is unramified, proving
\eqref{eq:ambient-passport}.

  - Full source and surrounding context: [`manuscripts/06-plane-boundary/main.tex#prop:ambient-passport`](../../proof-sources/06-plane-boundary/main.md#label-prop-ambient-passport)
