# Contact-degree formula

`RMU-77DB7C87` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-77DB7C87` · `proposition`

Suppose coprime integers \(m,n\) satisfy
\[
v_E(P)=-m,\quad v_E(Q)=-n,\qquad
v_D(P)=-ma,\quad v_D(Q)=-na.
\]
Choose \(c,d\in\mathbb Z\) with \(dn-cm=1\) and set
\[
\pi=P^c/Q^d,\qquad \tau=Q^m/P^n.
\]
Assume that in the toric chart \(x=t^{-1}\) up to a unit and that
\[
dP\wedge dQ=x^\kappa\,dx\wedge dy
\]
up to a nonzero \(s\)-unit.  Put
\[
e_*=a(m+n)-\kappa-1.
\]
If \(e_*>0\), then the residue of \(\tau\) on \(D\) is constant.  After
subtracting that constant and removing the lower resonant target shears, the
first non-shear contact degree is
\begin{equation}

e=e_*=a(m+n)-\kappa-1.
\end{equation}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

The Bézout relation gives \(v_D(\pi)=a\) and \(v_D(\tau)=0\).  Direct
differentiation gives
\[
d\pi\wedge d\tau
=-P^{c-n-1}Q^{m-d-1}\,dP\wedge dQ.
\]
The monomial factor has \(t\)-order \(a(m+n+1)\), while the last wedge has
order \(-\kappa-2\).  Thus
\[
\operatorname{ord}_D(d\pi\wedge d\tau)
=a(m+n+1)-\kappa-2=a+e_*-1.
\]
Before assuming that the residue is constant, write
\(\tau=\tau_0(s)+O(t)\).  The coefficient of
\(t^{a-1}dt\wedge ds\) in \(d\pi\wedge d\tau\) is
\(a c(s)\tau_0'(s)\).  Since \(e_*>0\), the displayed wedge order is
strictly greater than \(a-1\), hence \(\tau_0'=0\).  After translating
\(\tau_0\) to zero and removing the lower resonances of
\cref{lem:resonance}, the first remaining term of order \(e\) contributes
wedge order \(a+e-1\).  Equating orders gives
\eqref{eq:contact-degree}.

  - Full source and surrounding context: [`manuscripts/06-plane-boundary/main.tex#prop:contact`](../../proof-sources/06-plane-boundary/main.md#label-prop-contact)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
