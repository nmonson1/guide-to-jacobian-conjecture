# All-multiplicity fixed-frame Torelli

`RMU-F7236EAC` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-F7236EAC` · `theorem`

Let \((A,B)\) and \((\widetilde A,\widetilde B)\) be admissible cubic
frames, with \(A/c\) and \(\widetilde A/c\) nonconstant.  The following are
equivalent:
\begin{enumerate}[label=(\roman*)]
\item \(G_{A,B}\) and \(G_{\widetilde A,\widetilde B}\) are stably
left--right equivalent;
\item they are ordinarily polynomially left--right equivalent;
\item there is \(u\in\C^\times\) such that
\[
\widetilde A(uc)=uA(c),\qquad
\widetilde B(uc)-B(c)\in cA(c)\C[c].
\]
\end{enumerate}
No squarefreeness or coprimality hypothesis is required.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

The intrinsic finite-root chart, its marked vertical lines, and the divisor
\(\operatorname{div}(\rho H_0^3)\) all survive a product with affine space.
A stable equivalence preserves this data.  More explicitly, after adjoining
\(m\) stabilization coordinates one has
\[
\Omega_{(D\times\A^m)/\A^1}
\simeq \Omega_{D/\A^1}\oplus\mathcal O^{\,m},
\qquad
\operatorname{Fitt}_{m+1}
\Omega_{(D\times\A^m)/\A^1}
=\operatorname{Fitt}_1\Omega_{D/\A^1};
\]
thus the relative-Jacobian center and its weighted divisor are recovered
intrinsically after stabilization.  A marked vertical line forces the
pulled-back base coordinate to have the form \(C=uc+v\).  The unique
nonvertical divisor forces
\[
3\widetilde A_0(C)T+\widetilde B_0(C)
=\kappa(3A_0(c)t+B_0(c)).
\]
Thus \(T=\mu(c)t+h(c)\).  The cylinder Jacobian makes \(\mu\) a nonzero
constant and excludes dependence on stabilization variables.

The horizontal divisor gives every \(p_s\), while the vertical multiplicity
gives every \(d_s\).  By
\cref{lem:common-factor-multiplicity}, all multiplicities of \(A\) are
therefore preserved.  The deleted planes account for every root except the
retained root zero, so \(v=0\).  Comparing the \(t\)-coefficient and using
the admissible first jets gives
\[
\widetilde A(uc)=uA(c).
\]
The constant coefficient then gives
\[
\widetilde B(uc)-B(c)=-3uA(c)h(c).
\]
Differentiating at zero shows \(h(0)=0\), which is condition (iii).
Conversely, the explicit root translation used in the ordinary
classification constructs a polynomial left--right equivalence and does
not use squarefreeness or coprimality.

  - Does not establish: Presence in the manuscript is not an independent proof audit.
