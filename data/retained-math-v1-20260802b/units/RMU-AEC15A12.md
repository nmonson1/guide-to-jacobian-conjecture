# Universal root--slope transform

`RMU-AEC15A12` · `proposition`

## Mathematical record

`RMU-AEC15A12` · `proposition`

Let \(H(T,c)\in k[T,c]\), where \(2\in k^*\), and define
\[
b=r-H_T(t,c),\qquad
2a=H(t,c)+tb.
\]
Then, for
\[
P_{a,b,c}(T)=H(T,c)+bT-2a,
\]
one has
\[
P_{a,b,c}(t)=0,\qquad P'_{a,b,c}(t)=r,
\]
and
\[
2\,da-t\,db-H_c(t,c)\,dc=r\,dt.
\]
Consequently
\[
\det\frac{\partial(a,b,c)}{\partial(t,r,c)}=\frac r2.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

The root and derivative identities are immediate from the definitions.
Differentiating \(2a=H(t,c)+tb\) and substituting
\(H_T(t,c)+b=r\) gives the one-form identity.  Wedge it with
\(db\wedge dc\); since
\[
db=dr-H_{TT}\,dt-H_{Tc}\,dc,
\]
the stated determinant follows.

  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/root-slope-geometry.tex#prop:root-slope-transform`](../../proof-sources/01-cubic-incidence/appendices/root-slope-geometry.md#label-prop-root-slope-transform)
