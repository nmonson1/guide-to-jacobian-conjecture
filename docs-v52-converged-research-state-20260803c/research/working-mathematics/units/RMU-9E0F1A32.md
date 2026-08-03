---
title: "Weighted one-variable field"
description: "Let \\(P,Q\\) be homogeneous forms of the same degree \\(a>0\\).  Write\n\\[\nP=GA,\\qquad Q=GB,\\qquad \\gcd(A,B)=1,\n\\qquad n=\\deg A=\\deg B,\n\\]\nand let \\(h\\) be homogeneous of degree \\(b>0\\).  Put\n\\[\n  \\begin{aligned}\n  t&=P/Q=A/B, & g&=\\gcd(a,b),\\\\\n  p&=a/g, & q&=b/g, & w&=h^p/Q^q,\n  \\end{aligned}\n\\]\nand suppose that \\(h\\) is algebraic over \\(k(P,Q)\\).  Then \\(w\\) is\nalgebraic over \\(k(t)\\).\n\nIf \\(K_1=k(t,w)\\), there are coprime homogeneous forms \\(A_0,B_0\\) of a\ncommon degree \\(d\\) and a rational function \\(\\mathcal R\\) of degree \\(e\\)\nsuch that\n\\[\nK_1=k(A_0/B_0),\\qquad t=\\mathcal R(A_0/B_0),\n\\qquad n=ed.\n\\]"
---

# Weighted one-variable field

`RMU-9E0F1A32` · `lemma` · statement version `1`

## Exact statement

Let \(P,Q\) be homogeneous forms of the same degree \(a>0\).  Write
\[
P=GA,\qquad Q=GB,\qquad \gcd(A,B)=1,
\qquad n=\deg A=\deg B,
\]
and let \(h\) be homogeneous of degree \(b>0\).  Put
\[
  \begin{aligned}
  t&=P/Q=A/B, & g&=\gcd(a,b),\\
  p&=a/g, & q&=b/g, & w&=h^p/Q^q,
  \end{aligned}
\]
and suppose that \(h\) is algebraic over \(k(P,Q)\).  Then \(w\) is
algebraic over \(k(t)\).

If \(K_1=k(t,w)\), there are coprime homogeneous forms \(A_0,B_0\) of a
common degree \(d\) and a rational function \(\mathcal R\) of degree \(e\)
such that
\[
K_1=k(A_0/B_0),\qquad t=\mathcal R(A_0/B_0),
\qquad n=ed.
\]

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMU9E0F1A32-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

Choose a polynomial relation among \(P,Q,h\) and retain a nonzero
source-homogeneous part.  Every monomial \(P^iQ^jh^k\) in that part
satisfies
\[
a(i+j)+bk=M.
\]
It follows that all exponents \(k\) are congruent modulo \(p=a/g\).
After removing their common residual power of \(h\), the relation has the
form
\[
\sum_i C_i(P,Q)h^{pi}=0,
\qquad \deg C_i=N-qi
\]
for a suitable integer \(N\).  Division by \(Q^N\) gives a polynomial
relation for \(w\) over \(k(t)\).

The one-variable field \(K_1\subset k(\PP^2)\) is the function field of a
curve dominated by \(\PP^2\).  Restriction to a suitable line makes that
curve unirational, hence rational in characteristic zero.  Thus
\(K_1=k(s)\), and \(s\) can be written \(A_0/B_0\) with \(A_0,B_0\)
coprime homogeneous forms of the same degree \(d\).

Write \(\mathcal R=U/V\), where \(U,V\) are coprime binary forms of degree
\(e\).  The substituted forms \(U(A_0,B_0)\) and \(V(A_0,B_0)\) remain
coprime: their common divisor would, by the binary resultant identities,
divide powers of both \(A_0\) and \(B_0\).  Comparing degrees in the reduced
ratio \(A/B=\mathcal R(A_0/B_0)\) yields \(n=ed\).

[Machine-readable graph](../graph.json)
