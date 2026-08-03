---
title: "Contact-degree formula"
description: "Suppose coprime integers \\(m,n\\) satisfy\n\\[\nv_E(P)=-m,\\quad v_E(Q)=-n,\\qquad\nv_D(P)=-ma,\\quad v_D(Q)=-na.\n\\]\nChoose \\(c,d\\in\\mathbb Z\\) with \\(dn-cm=1\\) and set\n\\[\n\\pi=P^c/Q^d,\\qquad \\tau=Q^m/P^n.\n\\]\nAssume that in the toric chart \\(x=t^{-1}\\) up to a unit and that\n\\[\ndP\\wedge dQ=x^\\kappa\\,dx\\wedge dy\n\\]\nup to a nonzero \\(s\\)-unit.  Put\n\\[\ne_*=a(m+n)-\\kappa-1.\n\\]\nIf \\(e_*>0\\), then the residue of \\(\\tau\\) on \\(D\\) is constant.  After\nsubtracting that constant and removing the lower resonant target shears, the\nfirst non-shear contact degree is\n\\begin{equation}\n\ne=e_*=a(m+n)-\\kappa-1.\n\\end{equation}"
---

# Contact-degree formula

`RMU-77DB7C87` · `proposition` · statement version `2`

## Exact statement

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

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMU77DB7C87-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

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

[Machine-readable graph](../graph.json)
