# Marked Vandermonde factorization

`RMU-03794DFA` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-03794DFA` · `proposition`

If \(P(T)=(T-t)Q(T)\), then
\[
\Disc(P)=P'(t)^2\Disc(Q).
\]
For
\[
P(T)=A(c)T^3+B(c)T^2+bT-2a,\qquad r=P'(t),
\]
this becomes
\[
\Disc(P)
=r^2\bigl((3A(c)t+B(c))^2-4A(c)r\bigr).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Use the product formula
\[
\Disc((T-t)Q)=\Disc(T-t)\Disc(Q)\Res(T-t,Q)^2
\]
and \(\Res(T-t,Q)=Q(t)=P'(t)\).  Dividing the cubic by \(T-t\)
gives a quadratic whose discriminant is the displayed residual factor.

  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/root-slope-geometry.tex#prop:marked-vandermonde`](../../proof-sources/01-cubic-incidence/appendices/root-slope-geometry.md#label-prop-marked-vandermonde)
