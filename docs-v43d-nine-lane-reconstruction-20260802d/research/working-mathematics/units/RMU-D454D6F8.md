# Branchwise exact Nullstellensatz certificates

`RMU-D454D6F8` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-D454D6F8` · `theorem`

For each sign, the stored nine-generator ideal is the unit ideal:
\[
I_+=K_\eta[I,H,G,A],\qquad I_-=K_\eta[I,H,G,A].
\]
More precisely, the supplement gives cofactors \(C_{\epsilon,j}\) such that
\[
\sum_{j=0}^{8}C_{\epsilon,j}F_{\epsilon,j}=1,
\qquad \epsilon\in\{+,-\},
\]
and every product \(C_{\epsilon,j}F_{\epsilon,j}\) has total degree at most
five.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

The monomials of total degree at most five in four variables span a
\(126\)-dimensional space.  Modular row reduction at \(p=31\), using a root
of the quintic field polynomial, selects \(111\) rows.  The two selected
\(111\times111\) minors have determinants \(1\) and \(17\) modulo \(31\).
Exact rational elimination then produces 80 nonzero cofactor monomials for
each sign.  A separate GMP program and an independently written
rational-arithmetic Python implementation multiply the cofactors by the
original generators, reduce in the quintic field, and recover exactly the
constant polynomial \(1\).

  - Full source and surrounding context: [`manuscripts/06-plane-boundary/appendices/degree-twenty-one-certificates.tex#thm:branchwise-terminal-unit`](../../proof-sources/06-plane-boundary/appendices/degree-twenty-one-certificates.md#label-thm-branchwise-terminal-unit)
