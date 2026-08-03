---
title: "Invariant fields"
description: "For each of\n\\[\nG=z^2+xy,\\quad xz+y^2,\\quad z^2+x^2,\\quad xz,\n\\]\none has\n\\[\n\\ker_{\\C(x,y,z)}\\delta_G\n=\\C\\left(\\frac{x}{y},Gy^2\\right).\n\\]\nConsequently a homogeneous invariant rational function has scalar degree\ndivisible by four."
---

# Invariant fields

`RMU-05F8AA2E` · `lemma` · statement version `1`

## Exact statement

For each of
\[
G=z^2+xy,\quad xz+y^2,\quad z^2+x^2,\quad xz,
\]
one has
\[
\ker_{\C(x,y,z)}\delta_G
=\C\left(\frac{x}{y},Gy^2\right).
\]
Consequently a homogeneous invariant rational function has scalar degree
divisible by four.

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMU05F8AA2E-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

Put \(r=x/y\) and \(s=Gy^2\).  Direct differentiation gives
\(\delta_G(r)=\delta_G(s)=0\).

For \(G=xz+\epsilon y^2\), the full field is
\(\C(r,s)(y)\), since
\[
z=\frac{s-\epsilon y^4}{ry^3}.
\]
The induced nonzero derivation on this one-variable rational field has
constant field \(\C(r,s)\).

For \(G=z^2+xy\) and \(z^2+x^2\), put \(w=yz\).  Over
\(\C(r,s)\), the full field is the function field of
\[
w^2+r y^4=s
\quad\text{or}\quad
w^2+r^2y^4=s.
\]
Each generic curve is geometrically integral.  Thus \(\C(r,s)\) is
relatively algebraically closed in the one-variable function field, and a
nonzero \(\C(r,s)\)-derivation has no further constants.

Under scalar dilation, \(r\) has degree zero and \(s\) degree four.  The
rational eigenvectors in \(\C(r,s)\) therefore have degrees in
\(4\mathbb Z\).

[Machine-readable graph](../graph.json)
