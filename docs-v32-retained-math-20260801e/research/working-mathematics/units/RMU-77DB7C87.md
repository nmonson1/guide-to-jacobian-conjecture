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
up to a nonzero \(s\)-unit.  Then the first possible non-shear contact
degree is
\begin{equation}

e=a(m+n)-\kappa-1.
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
order \(-\kappa-2\).  On the other hand, the wedge of
\(\pi\sim t^a\) with \(\tau-\tau|_D\sim t^e\) has order \(a+e-1\).
Equating orders yields \eqref{eq:contact-degree}.

  - Does not establish: Presence in the manuscript is not an independent proof audit.
