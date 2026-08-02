# All-multiplicity fixed-frame Torelli

`RMU-F7236EAC` · `theorem`

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

A stable target automorphism identifies the reduced nonproperness divisors.
Their primitive discriminant components are singular along the generic cusp
curve, whereas the plane components are smooth, so the primitive components
are preserved and the deleted planes are permuted.  Since at least one
deleted plane is present, a matched pair gives an equality of principal
prime ideals
\[
C-\widetilde s=\lambda(c-s),
\]
where \(C\) is the pullback of the target base coordinate.  Hence
\(C=uc+v\), with \(u\ne0\), and the two relative \(\A^1\)-structures are
identified up to this affine change.

After adjoining \(\ell\) stabilization coordinates one has
\[
\Omega_{(D\times\A^\ell)/\A^1}
\simeq
\Omega_{D/\A^1}\oplus\mathcal O^{\,\ell},
\]
and therefore
\[
\operatorname{Fitt}_{\ell+1}
\Omega_{(D\times\A^\ell)/\A^1}
=
\operatorname{Fitt}_1(\Omega_{D/\A^1})
\mathcal O_{D\times\A^\ell}.
\]
Thus the relative-Jacobian blowup, the intrinsic finite-root chart obtained
by deleting the exceptional primes over common-root planes, and the divisor
\(\operatorname{div}(\rho H_0^3)\) are all preserved after stabilization.

On that chart the factor \(H_0=3A_0t+B_0\) is primitive, irreducible, and
the unique nonvertical component.  Consequently
\[
3\widetilde A_0(C)T+\widetilde B_0(C)
=\kappa(3A_0(c)t+B_0(c))
\]
for some \(\kappa\in\C^*\).  Solving the equality shows that \(T\) has no
stabilization-variable dependence and has the form
\(T=\mu(c)t+h(c)\).  The full cylinder Jacobian makes
\(\mu\in\C^*\).

At every deleted root, the order of the horizontal coefficient \(A_0\)
recovers \(p_s\), while the vertical multiplicity of \(\rho\) recovers
\(d_s\).  By \cref{lem:common-factor-multiplicity}, the common-factor
multiplicity and hence \(\ord_sA\) are recovered.  The deleted planes account
for every root except the retained simple root zero, so \(v=0\).  The full
root divisors, with multiplicity, now agree; admissibility at zero fixes the
scalar and gives
\[
\widetilde A(uc)=uA(c).
\]

Comparing \(t\)-coefficients in the \(H_0\)-identity and differentiating at
zero gives \(u\mu=\kappa\).  With \(g=\gcd(A,B)\) and
\(\widetilde g=\gcd(\widetilde A,\widetilde B)\), both normalized to have
value one at zero, it follows that
\[
\widetilde g(uc)=g(c).
\]
Multiplying the constant coefficient identity by \(g\) yields
\[
\widetilde B(uc)=\kappa B(c)-3uA(c)h(c).
\]
Evaluation at zero gives \(\kappa=1\).  Differentiating there, and using the
admissibility jets together with \(\widetilde A(uc)=uA(c)\), gives
\(h(0)=0\).  This is condition (iii).

Conversely, after the diagonal scaling, condition (iii) writes the
difference of the two \(B\)'s as \(3A\phi\) with
\(\phi\in c\C[c]\).  The polynomial root translation from
\cref{thm:general-boundary-torelli} constructs an ordinary left--right
equivalence and uses neither squarefreeness nor coprimality.

  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#thm:all-multiplicity-torelli`](../../proof-sources/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.md#label-thm-all-multiplicity-torelli)
