# Universal secondary-boundary transport

`RMU-3AFE6A0C` · `theorem`

## Mathematical record

`RMU-3AFE6A0C` · `theorem`

Let \(a,e\in\mathbb N\) satisfy \(e>a^2\), and put
\(\delta=e-a^2\).  Equation \eqref{eq:transport-equation} has a unique
solution
\[
h(s)=\frac{H_{a,e}(s)}{(s-1)^a}
\]
whose numerator is a polynomial of degree at most \(a\), where
\begin{align}
H_{a,e}(s)
&=\sum_{k=0}^a
\frac{a^k a!}{(a-k)!\prod_{j=0}^k(e-aj)}s^k
\\
&=\frac1e\,{}_2F_1\!\left(-a,1;1-\frac ea;s\right).

\end{align}
It satisfies
\begin{equation}

as(s-1)H'+(e-a^2s)H=1,
\end{equation}
\[
H(0)=\frac1e,\qquad H(1)=\frac1\delta,
\]
and \(H\) is squarefree.

The exceptional ratio
\begin{equation}

W_{a,e}(s)=\frac{(s-1)^\delta H_{a,e}(s)^a}{s^e}
\end{equation}
is a degree-\(e\) Belyi map.  It obeys
\begin{equation}

W_{a,e}'(s)=
\frac{(s-1)^{\delta-1}H_{a,e}(s)^{a-1}}{s^{e+1}},
\end{equation}
and its passport is
\begin{equation}

(a^a,\delta),\qquad(e),\qquad(a+1,1^{e-a-1}).
\end{equation}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Substitute \(h=H/(s-1)^a\) into
\eqref{eq:transport-equation}; since \(c'=-(s-1)^{-2}\), this gives
\eqref{eq:H-ode}.  Writing \(H=\sum h_ks^k\) gives
\[
h_0=\frac1e,\qquad
h_k=\frac{a(a+1-k)}{e-ak}h_{k-1}.
\]
The denominators are nonzero because \(e>a^2\), and the recurrence gives
\eqref{eq:H-sum}.  It also proves uniqueness.  The hypergeometric notation
is the same terminating recurrence.  Evaluation at zero and one gives the
stated endpoint values.  If \(H(s_0)=0\), then
\eqref{eq:H-ode} gives \(as_0(s_0-1)H'(s_0)=1\); hence every root is simple
and avoids \(0,1\).

Logarithmic differentiation of \eqref{eq:secondary-W}, followed by
\eqref{eq:H-ode}, gives
\[
\frac{W'}W=\frac1{s(s-1)H},
\]
which is \eqref{eq:secondary-derivative}.  The numerator and denominator of
\(W\) are coprime of degree \(e\).  Over zero, the \(a\) roots of \(H\)
have multiplicity \(a\) and \(s=1\) has multiplicity \(\delta\).  Over
infinity, \(s=0\) has multiplicity \(e\).  At \(s=\infty\),
\eqref{eq:secondary-derivative} shows that
\(W-W(\infty)\) has order \(a+1\).  Finally,
\[
a(a-1)+(\delta-1)+(e-1)+a=2e-2,
\]
so Riemann--Hurwitz leaves only \(e-a-1\) unramified points in the third
fiber and proves \eqref{eq:secondary-passport}.

  - Full source and surrounding context: [`manuscripts/06-plane-boundary/main.tex#thm:secondary`](../../proof-sources/06-plane-boundary/main.md#label-thm-secondary)
