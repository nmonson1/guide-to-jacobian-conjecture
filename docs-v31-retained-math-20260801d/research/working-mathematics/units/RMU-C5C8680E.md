# Omitted values are singular

`RMU-C5C8680E` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-C5C8680E` · `theorem`

For every complex polynomial Keller map,
\[
O_F\subseteq\Sing(S_F).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Let
\[
\pi\colon\widetilde X\longrightarrow Y
\]
be the normalization of \(Y\) in \(\C(X)\).  The map factors as an open
immersion \(j\colon X\hookrightarrow\widetilde X\) followed by the finite
map \(\pi\).  Put \(D=\widetilde X\setminus X\).  The complement of the
affine open \(X\) is pure of codimension one, and
\[
S_F=\pi(D).
\]

First, \(O_F\) has codimension at least two.  Indeed, if an irreducible
divisor \(V(h)\subset Y\) were omitted, then \(h\circ F\) would be a
nowhere-zero polynomial on affine space and hence a nonzero constant.
Dominance makes \(F^*\) injective, forcing \(h\) itself to be constant.

Now take \(y\in S_F^{\mathrm{reg}}\).  After shrinking and making an
\'etale base change, the finite normalization has the standard tame local
form
\[
\Spec A[u_i]/(u_i^{e_i}-f)\longrightarrow\Spec A,
\]
where \(S_F=V(f)\).  The unique divisor over \(S_F\) in the \(i\)-th piece
is \(E_i=V(u_i)\).  Purity of \(D\) prevents deleting only an isolated
codimension-two subset of a retained sheet.

Every sheet with \(e_i>1\) must be deleted: retaining its divisor in \(X\)
would give ramification of the Keller map.  On the other hand, not all
divisors \(E_i\) can be deleted, since then a dense open part of \(S_F\)
would be omitted, contradicting
\(\operatorname{codim}O_F\ge2\).  Thus an unramified
sheet with \(e_i=1\) is retained, and its point over \(y\) belongs to
\(X\).  Hence \(y\in F(X)\), proving the claim.

  - Does not establish: Presence in the manuscript is not an independent proof audit.
