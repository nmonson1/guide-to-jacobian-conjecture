# Cubic pencils

`RMU-FE8A1810` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-FE8A1810` · `proposition`

Let \(P,Q\) be independent homogeneous cubics satisfying
\eqref{eq:highest}.  Then their pencil either contains the cube of a linear
form, or \(P,Q,h\) are polynomials in two independent linear forms.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

First suppose \(\gcd(P,Q)=1\).  Apply
\cref{lem:weighted-field} directly to \(P,Q,h\).
If \(e>1\), then \(3=ed\) gives \(e=3,d=1\), so \(P,Q\) are binary in two
linear forms.

If \(e=1\), write \(w=R(t)\).  For
\(F_\xi=P-\xi Q\), let \(r_\xi=\ord_\xi R\), and set
\[
c_\xi=r_\xi+4\mathbf1_{\xi=\infty}.
\]
If an irreducible component of \(F_\xi\) has multiplicity \(m\), valuation
gives
\[
3\nu(h)=c_\xi m.
\]
Every \(c_\xi\) is nonnegative and
\[
\sum_{\xi\in\PP^1}c_\xi=4.
\]
If no fiber is a cube, every cubic fiber has a component whose multiplicity
is prime to three.  The displayed valuation then makes every \(c_\xi\) a
multiple of three, contradicting their sum.

Now write \(P=GA,Q=GB\) with \(G\ne1\) and \(\gcd(A,B)=1\).
If \(\deg G=2\), then \(A,B\) are independent linear forms.  An irreducible
factor of \(G\), of multiplicity \(m=1\) or \(2\), cannot carry a
nonconstant \(A/B\), since its valuation would give
\[
3\nu(h)=4m.
\]
Every component of \(G\) is therefore a fiber line of the pencil
\(\angles{A,B}\); hence \(G,P,Q\) are binary.

If \(G=\ell\), the reduced pencil \(A/B\) has degree two.  In the composite
case \cref{lem:weighted-field} gives \(e=2,d=1\).  The valuation along
\(\ell\) forces \(\ell\) into the same binary pencil.  In the primitive
case, the same valuation first makes \(A/B\) constant on \(\ell=0\).
After changing the pencil basis, write \(A=\ell m\).  If
\(m\) is proportional to \(\ell\), then \(P=\ell^3\).  Otherwise, with
\(r=\ord_0R\), valuations along \(m=0\) and \(\ell=0\) give
\[
3\nu_m(h)=r,\qquad 3\nu_\ell(h)=r+4,
\]
which is impossible modulo three.

Finally, if \(P,Q\) are binary in linear forms \(a,b\), then
\[
dP\wedge dQ=J_{a,b}(P,Q)\,da\wedge db
\]
with nonzero planar Jacobian.  Equation \eqref{eq:highest} forces the
derivative of \(h\) transverse to \(a,b\) to vanish, so \(h\) is binary in
the same forms.

  - Full source and surrounding context: [`manuscripts/02-low-degree/main.tex#prop:cubic-pencils`](../../proof-sources/02-low-degree/main.md#label-prop-cubic-pencils)
