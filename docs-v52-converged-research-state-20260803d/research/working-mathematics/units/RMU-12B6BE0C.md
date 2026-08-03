---
title: "Bounded orbit map"
description: "The degree-preserving root translations form the kernel pair of the map\n\\[\n\\Theta_N\\colon\\operatorname{Tot}(E_N)\\longrightarrow\n\\operatorname{Tot}(E_N),\n\\qquad\n(\\widehat Q,P)\\longmapsto(\\widehat Q,Z^NP).\n\\]\nIf \\(\\widehat Q=z^mQ_d\\), with \\(Q_d(0)\\ne0\\), then uniquely\n\\[\nP=z^mP_d+Q_dS,\\qquad \\deg P_d<d,\\quad\\deg S<m.\n\\]\nThe finite-root decoration is \\(P_d\\); root translation removes precisely\nthe principal part \\(S/z^m\\) supported at infinity."
---

# Bounded orbit map

`RMU-12B6BE0C` · `proposition` · statement version `1`

## Exact statement

The degree-preserving root translations form the kernel pair of the map
\[
\Theta_N\colon\operatorname{Tot}(E_N)\longrightarrow
\operatorname{Tot}(E_N),
\qquad
(\widehat Q,P)\longmapsto(\widehat Q,Z^NP).
\]
If \(\widehat Q=z^mQ_d\), with \(Q_d(0)\ne0\), then uniquely
\[
P=z^mP_d+Q_dS,\qquad \deg P_d<d,\quad\deg S<m.
\]
The finite-root decoration is \(P_d\); root translation removes precisely
the principal part \(S/z^m\) supported at infinity.

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMU12B6BE0C-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

For every \(R\)-algebra, two points \(p,p'\) have the same image under a
linear map \(M\) exactly when \(p-p'\in\ker M\).  These are precisely the
equations of the scheme-theoretic fiber product
\(\mathbf V(E)\times_{\mathbf V(E)}\mathbf V(E)\), where both arrows to the
middle copy are \(M\).  This proves the kernel-pair claim for \(M=Z^N\).

For the decomposition, consider the linear map
\[
\{\deg P_d<d\}\oplus\{\deg S<m\}
\longrightarrow \{\deg P<N\},
\qquad (P_d,S)\longmapsto z^mP_d+Q_dS.
\]
If its value is zero, reduction modulo \(Q_d\) gives
\(z^mP_d=0\).  Since \(Q_d(0)\ne0\), \(z\) is a unit modulo \(Q_d\), so
\(P_d=0\); then \(S=0\).  The source and target both have rank \(N=d+m\),
so the map is an isomorphism, proving existence and uniqueness over the
entire monic coefficient base.

[Machine-readable graph](../graph.json)
