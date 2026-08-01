# The easy transverse branches

`RMU-F0578ED7` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-F0578ED7` · `proposition`

In \eqref{eq:homogeneous}, suppose
\[
H_4=(0,0,h),\qquad H_3=(P,Q,R).
\]
If \(P,Q\) are linearly dependent, or if their pencil contains the cube of a
linear form, then \(F\) is an automorphism.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

A row of \(JF\) cannot vanish, so every target combination of the
coordinates of \(F\) has no critical point.  In the dependent case a target
combination of the first two components has degree at most two, and
\cref{lem:quadratic-coordinate} applies.  In the cube-containing case a
combination has degree at most three with cubic part a cube, and
\cref{lem:cubic-coordinate} applies.

After straightening this component to a variable \(t\), choose the other
target combination among the first two original components.  Over
\(\overline{k(t)}\), the remaining two coordinates form a plane Keller map.
In the quadratic case one component has degree at most six.  In the cubic
case it has degree in
\[
\set{1,2,3,4,5,6,7,9}.
\]
Indeed, substituting \(w_2=c^{-1}(t-\psi)\) into a cubic gives degree at most
seven unless the \(w_2^3\) term and the cubic part of \(\psi\) are both
nonzero, in which case the unique top term has degree nine.  Every displayed
integer is a product of at most two primes, counted with multiplicity.
The corrected Appelgate--Onishi plane theorem, in the form completed by
Nagata, therefore makes the plane map an automorphism
\cite{appelgateOnishi1985,nagata1988two}.  Its inverse over
\(\overline{k(t)}\) is unique, hence fixed by every automorphism over
\(k(t)\), and therefore descends to \(k(t)\).  It follows that \(F\) is
birational over \(k\).  A birational Keller self-map is injective by
Zariski's Main Theorem and hence an automorphism by Ax--Grothendieck.

  - Full source and surrounding context: [`manuscripts/02-low-degree/main.tex#prop:easy-branches`](../../proof-sources/02-low-degree/main.md#label-prop-easy-branches)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
