# Finite-jet realization

`RMU-36E4F40C` · `proposition`

## Mathematical record

`RMU-36E4F40C` · `proposition`

Let \(k\) be an infinite field of characteristic zero, and let
\(\widehat\phi\in\operatorname{Aut}k[[x,y]]\) fix the origin and satisfy
\(\det J\widehat\phi=1\).  For every \(N\), there is a polynomial
automorphism \(\phi_N\in\operatorname{Aut}k[x,y]\), with
\(\det J\phi_N=1\), whose \(N\)-jet agrees with that of
\(\widehat\phi\).  It may be chosen as a finite composition of linear
\(\mathrm{SL}_2(k)\) maps and polynomial shears.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Match the linear part first.  Inductively, suppose the first unmatched
homogeneous term has degree \(n\):
\[
(x,y)+(f_n,g_n)+O(\mathfrak m^{n+1}).
\]
The Jacobian-one condition gives
\(\partial_xf_n+\partial_yg_n=0\), so for a homogeneous binary form
\(K_{n+1}\),
\[
(f_n,g_n)=(\partial_yK_{n+1},-\partial_xK_{n+1}).
\]
Over an infinite field, powers of linear forms span the binary forms of
each degree.  Write
\[
K_{n+1}=\sum_i c_i\ell_i^{\,n+1},
\qquad \ell_i=a_ix+b_iy.
\]
The Hamiltonian flow of each summand is the exact polynomial shear
\[
(x,y)\longmapsto
(x,y)+c_i(n+1)\ell_i^n(b_i,-a_i),
\]
because \(\ell_i\) is constant in the direction \((b_i,-a_i)\).  Composing
these shears matches the degree-\(n\) discrepancy and changes only higher
degrees.  Induction through degree \(N\) proves the claim.

  - Full source and surrounding context: [`manuscripts/06-plane-boundary/appendices/exact-normal-linearization.tex#prop:finite-jet-realization`](../../proof-sources/06-plane-boundary/appendices/exact-normal-linearization.md#label-prop-finite-jet-realization)
