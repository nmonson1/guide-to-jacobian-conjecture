---
title: "Torus nullcone"
description: "Let \\(X\\) be an affine finite-type \\(\\Gm\\)-scheme with a fixed point \\(0\\),\nequivariantly embedded in\n\\[\nV=V_-\\oplus V_0\\oplus V_+.\n\\]\nIf the reduced germs at zero of\n\\[\nX\\cap V_-,\\qquad X\\cap V_0,\\qquad X\\cap V_+\n\\]\nare all zero-dimensional, then the reduced germ\n\\((X_{\\mathrm{red}},0)\\) is zero-dimensional."
---

# Torus nullcone

`RMU-08E3EA3C` · `lemma` · statement version `1`

## Exact statement

Let \(X\) be an affine finite-type \(\Gm\)-scheme with a fixed point \(0\),
equivariantly embedded in
\[
V=V_-\oplus V_0\oplus V_+.
\]
If the reduced germs at zero of
\[
X\cap V_-,\qquad X\cap V_0,\qquad X\cap V_+
\]
are all zero-dimensional, then the reduced germ
\((X_{\mathrm{red}},0)\) is zero-dimensional.

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMU08E3EA3C-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

Suppose a positive-dimensional irreducible component
\(Y\subset X_{\mathrm{red}}\) passes through zero.  The connected group
\(\Gm\) preserves \(Y\).  If its action on \(Y\) is trivial, then
\(Y\subset V_0\), a contradiction.

Otherwise the generic orbit has dimension one, and
\[
\dim(Y/\!/\Gm)\le\dim Y-1.
\]
The fiber of \(Y\to Y/\!/\Gm\) over the image of zero therefore has positive
local dimension at zero.  Let \(Z\) be a positive-dimensional irreducible
component of that fiber through zero.

Every invariant regular function has on \(Z\) its value at zero.  Thus all
weight-zero coordinate functions vanish on \(Z\).  If a positive-weight
coordinate \(x_i\) and a negative-weight coordinate \(y_j\) were both
nonzero at a point of \(Z\), the balanced monomial
\[
x_i^{|\operatorname{wt}(y_j)|}
y_j^{\operatorname{wt}(x_i)}
\]
would be a nonzero invariant there, a contradiction.  Hence
\(Z\subset V_+\cup V_-\).  Irreducibility puts \(Z\) in one of these two
subspaces, contradicting the hypotheses.

[Machine-readable graph](../graph.json)
