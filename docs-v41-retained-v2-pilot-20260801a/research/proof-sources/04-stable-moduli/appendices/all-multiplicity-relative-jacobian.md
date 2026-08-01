---
title: "Text proof source — 04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex"
description: "Sanitized current source with exact TeX-label anchors."
---

# Text proof source

`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex`

This is the current sanitized source text used by the retained working graph. Comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `d4e5cd4c56ce4c119081878211471af72dca352b0cc0da4648bf6903b856d342` · 12,266 bytes

## Exact label anchors

<a id="label-app-all-multiplicity-relative-jacobian"></a>
- `app:all-multiplicity-relative-jacobian` — source line 2
<a id="label-eq-projective-source-identification"></a>
- `eq:projective-source-identification` — source line 31
<a id="label-prop-primitive-discriminant-content"></a>
- `prop:primitive-discriminant-content` — source line 55
<a id="label-prop-intrinsic-common-planes"></a>
- `prop:intrinsic-common-planes` — source line 86
<a id="label-prop-relative-jacobian-chart"></a>
- `prop:relative-jacobian-chart` — source line 130
<a id="label-lem-common-factor-multiplicity"></a>
- `lem:common-factor-multiplicity` — source line 187
<a id="label-thm-all-multiplicity-torelli"></a>
- `thm:all-multiplicity-torelli` — source line 206
<a id="label-prop-q-minus-two-weighted-stratum"></a>
- `prop:q-minus-two-weighted-stratum` — source line 304
<a id="label-prop-one-root-transition"></a>
- `prop:one-root-transition` — source line 342
<a id="label-q-all-multiplicity-infinity-gluing"></a>
- `q:all-multiplicity-infinity-gluing` — source line 396

## Complete source

~~~tex
\section{All multiplicities via the relative Jacobian blowup}
\label{app:all-multiplicity-relative-jacobian}

The squarefree boundary-residue argument extends to arbitrary common roots
once the absolute singular locus is replaced by the relative Jacobian over
the intrinsic affine \(c\)-line.  Let \((A,B)\) be an admissible cubic frame,
put \(Q=A/c\), and write
\[
P_{a,b,c}(T)=A(c)T^3+B(c)T^2+bT-2a.
\]
All discriminant surfaces and blowups in this appendix are schemes over
\(\C\).  The nonproperness divisor is reduced, but the intersections,
relative differentials, Fitting ideals, Rees algebras, and exceptional
divisors retain their scheme structures and multiplicities.

\subsection{Projective incidence and the primitive discriminant}

Consider
\[
\overline X_{A,B}
=V\!\left(AU^3+BU^2V+bUV^2-2aV^3\right)
\subset\A^3_{a,b,c}\times\PP^1_{[U:V]}.
\]
The marked-root map extends regularly by
\[
(x,y,z)\longmapsto
\left(G_{A,B}(x,y,z),[1+xy:x]\right).
\]
If \(\overline X^{\mathrm{simp}}\) is the simple-projective-root locus, then
\begin{equation}
\label{eq:projective-source-identification}
\A^3
\simeq
\overline X^{\mathrm{simp}}\setminus V(V,Q(c)).
\end{equation}
On the finite-root chart the inverse is the usual reconstruction formula.
At \(x=0\), the retained infinity root lies over \(c=0\); writing
\[
A=c+a_2c^2+a_3c^3+\cdots,\qquad
B=-2-4a_2c+b_2c^2+\cdots,
\]
its restriction is the triangular map
\[
b=y+4a_2,\qquad
a=z+4y^2+2a_2y-2b_2-8a_3.
\]
Thus the retained infinity section belongs to the affine source.

The cubic discriminant is
\[
\Delta=B^2b^2-4Ab^3+8B^3a-108A^2a^2-36ABab.
\]

\begin{proposition}[Primitive discriminant]
\label{prop:primitive-discriminant-content}
Its coefficient content in \(a,b\) is
\[
\chi(c)=\gcd(A(c),B(c)^2),
\]
normalized by \(\chi(0)=1\).  The polynomial
\(\delta=\Delta/\chi\) is irreducible, and
\[
S_{G_{A,B}}
=V(\delta)\cup
\bigcup_{s\in V(Q)_{\mathrm{red}}}V(c-s).
\]
\end{proposition}

\begin{proof}
At \(s\), the minimum coefficient valuation of \(\Delta\) is
\[
\min\{\ord_sA,\,2\ord_sB\},
\]
which gives the content formula.  Over \(\C(c)\),
\[
\Disc_a(\Delta)=64(B^2-3Ab)^3,
\]
which is not a square in \(\C(c,b)\); Gauss's lemma gives irreducibility
after removing content.  Finally,
\cref{eq:projective-source-identification} identifies the boundary of a
proper incidence morphism: its two kinds of images are nonsimple roots and
the deleted simple infinity roots.
\end{proof}

\begin{proposition}[Intrinsic common planes]
\label{prop:intrinsic-common-planes}
For a deleted root \(s\) of \(A\),
\[
B(s)=0
\quad\Longleftrightarrow\quad
V(\delta)\cap V(c-s)
\text{ is scheme-theoretically nonreduced}.
\]
\end{proposition}

\begin{proof}
Put \(u=c-s\), \(A=u^r\alpha\), and \(B=u^k\beta\), with the displayed
units at \(u=0\).  If \(k=0\), the restriction is the reduced smooth conic
\[
B(s)^2\bigl(b^2+8B(s)a\bigr).
\]
If \(k>0\), its primitive restriction is, according as
\(r<2k\), \(r=2k\), or \(r>2k\),
\[
-4\alpha(0)b^3,\qquad
b^2(\beta(0)^2-4\alpha(0)b),\qquad
\beta(0)^2b^2.
\]
\end{proof}

\subsection{The relative Gauss chart}

The pencil of deleted planes recovers \(c\) up to affine change.  On
\(D=V(\delta)\), define
\[
\mathfrak J_{D/\A^1}
=\operatorname{Fitt}_1\Omega_{D/\A^1}
=(\delta_a,\delta_b).
\]
Let \(\mathfrak B_D=\operatorname{Bl}_{\mathfrak J}D\).  Write
\[
g=\gcd(A,B),\qquad A=gA_0,\qquad B=gB_0,
\]
and put
\[
H_0=3A_0t+B_0,\qquad \rho=g^3/\chi.
\]

\begin{proposition}[Finite-root chart and weighted divisor]
\label{prop:relative-jacobian-chart}
The \(\delta_a\)-chart of \(\mathfrak B_D\) is canonically
\(\A^2_{c,t}\).  On it,
\[
\mathfrak J\mathcal O_{\A^2}
=\bigl(\rho(c)H_0(c,t)^3\bigr).
\]
\end{proposition}

\begin{proof}
Let \(R=\C[a,b,c]/(\delta)\).  It is a domain by
\cref{prop:primitive-discriminant-content}.  The \(\delta_a\)-chart has
coordinate ring
\[
R\left[\frac{\delta_b}{\delta_a}\right].
\]
Under the repeated-root parametrization
\[
b=-3At^2-2Bt,\qquad
a=-At^3-\tfrac12Bt^2,
\]
one obtains
\[
\delta_a=8\rho H_0^3,\qquad
\delta_b=-4t\rho H_0^3.
\]
Hence \(t=-2\delta_b/\delta_a\), so this ring is \(R[t]\).  The displayed
formulas make \(a,b\) polynomials in \(c,t\), while \(R[t]\) already
contains \(c,t\); consequently it is exactly \(\C[c,t]\).  Extending the
Rees ideal to this chart gives the asserted principal divisor.
\end{proof}

This chart is intrinsic.  Indeed, on the other chart put
\(q=\delta_a/\delta_b=-2/t\).  Then
\[
B(c)=qb+\frac32q^2a,\qquad
A(c)=\frac14q^2b+\frac12q^3a.
\]
The divisorial components of the complement \(q=0\) therefore lie precisely
over the scheme-theoretically nonreduced intersections with the common
deleted planes characterized by \cref{prop:intrinsic-common-planes}.
Removing those intrinsically characterized prime divisors leaves the chart
of \cref{prop:relative-jacobian-chart}.

\subsection{Multiplicity recovery and stable Torelli}

At a deleted root \(s\), let
\[
r=\ord_sA,\qquad k=\ord_sB,\qquad m=\min(r,k).
\]
The intrinsic chart records
\[
p=\ord_sA_0=r-m,\qquad
d=\ord_s\rho=3m-\min(r,2k).
\]

\begin{lemma}[Multiplicity recovery]
\label{lem:common-factor-multiplicity}
The common-factor multiplicity is
\[
m=
\begin{cases}
d,&p\ge d,\\[1mm]
(p+d)/2,&p<d.
\end{cases}
\]
\end{lemma}

\begin{proof}
If \(r\le k\), then \((p,d)=(0,2r)\), so \((p+d)/2=r=m\).  If
\(k<r<2k\), then \(p=r-k<3k-r=d\) and \((p+d)/2=k=m\).  Finally, if
\(r\ge2k\), then \(d=k=m\) and \(p=r-k\ge d\).  These cases exhaust the
possibilities.
\end{proof}

\begin{theorem}[All-multiplicity fixed-frame Torelli]
\label{thm:all-multiplicity-torelli}
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
\end{theorem}

\begin{proof}
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
\end{proof}

Equivalently, scaling identifies the decorated Artin schemes
\[
\left(\Spec\C[c]/(A/c),\,B\bmod(A/c)\right).
\]
\begin{proposition}[The exceptional weighted stratum]
\label{prop:q-minus-two-weighted-stratum}
For the exceptional quadratic member
\(A=c(c+1)\), \(B=-2(c+1)^2\), one has
\[
\rho=(c+1)^2,\qquad H_0=3ct-2(c+1).
\]
Thus its special behavior is the intrinsic vertical multiplicity two, not
an ad hoc extra orbit invariant.
\end{proposition}

\begin{proof}
Here \(g=c+1\), \(A_0=c\), \(B_0=-2(c+1)\), and
\(\chi=c+1\).  Substitution in
\cref{prop:relative-jacobian-chart} gives
\[
\mathfrak J\mathcal O_{\A^2}
=\bigl((c+1)^2(3ct-2(c+1))^3\bigr),
\]
so the vertical multiplicity is exactly two.
\end{proof}

\subsection{The elementary cross-length boundary chart}

The preceding theorem works at fixed degree.  There is nevertheless a
simple codimension-one transition between successive fixed-degree normal
forms.  Write the length-\(N\) coefficient chart as
\[
 Q=1+q_1c+\cdots+q_Nc^N,\qquad
 R=r_0+r_1c+\cdots+r_{N-1}c^{N-1},
\]
with
\[
 A=cQ,\qquad B=-2-4q_1c+c^2R.
\]
The divisor \(q_N=0\) in its coefficient closure is the locus where one
root of \(Q\) has escaped to infinity.

\begin{proposition}[One-root transition]
\label{prop:one-root-transition}
On the open part
\[
 q_N=0,\qquad q_{N-1}\operatorname{Res}(Q,B)\ne0,
\]
put
\[
 \kappa=\frac{r_{N-1}}{q_{N-1}},\qquad
 r'_j=r_j-\kappa q_j\quad(0\le j\le N-2),
 \qquad q_0=1.
\]
Then the coefficient change is invertible and equivariant, with \(\kappa\)
of weight two.  The boundary chart is the length-\((N-1)\) chart times
\(\A^1_\kappa\), and the map to polynomial left--right orbit data contracts
the second factor.
\end{proposition}

\begin{proof}
Set \(R'=R-\kappa Q\).  Its top coefficient vanishes, so
\(\deg R'\le N-2\), while
\[
 B-B'=\kappa c^2Q=\kappa cA
       =3A\left(\frac{\kappa c}{3}\right).
\]
The last expression is exactly the allowed polynomial root-translation
gauge.  Conversely,
\[
 r_j=r'_j+\kappa q_j\quad(0\le j\le N-2),\qquad
 r_{N-1}=\kappa q_{N-1},
\]
so this is an invertible coordinate change on \(q_{N-1}\ne0\).  Under the
weighted scaling, \(q_j\) has weight \(j\), \(r_j\) has weight \(j+2\),
and hence \(\kappa\) has weight two and \(r'_j\) has weight \(j+2\).
Finally, with the displayed degrees in the Sylvester determinant,
\[
 \operatorname{Res}(Q,B)
 =(-1)^{N-1}q_{N-1}\operatorname{Res}(Q,B').
\]
The multiplier is a unit on this chart, so the resultant-open condition is
unchanged.
\end{proof}

The first two instances are
\[
\begin{array}{c|c|c}
\text{transition}&\kappa&R'\\ \hline
2\longrightarrow1&r_1/q_1&r_0-r_1/q_1\\[1mm]
3\longrightarrow2&r_2/q_2&(r_0-r_2/q_2)+(r_1-q_1r_2/q_2)c.
\end{array}
\]
Thus the first boundary phenomenon is not an additional modulus: it is a
gauge line over the lower-length chart.

\begin{question}[Gluing at infinity]
\label{q:all-multiplicity-infinity-gluing}
Can \cref{prop:one-root-transition} be extended across simultaneous root
escapes, the nonunit resultant boundary, and the weighted
relative-Jacobian marking to give a full compactification?  This also
includes comparison with the \(\alpha=0\) stratum and remains separate from
the finite-root theorem above.
\end{question}
~~~

[Back to the text-source index](../../index.md)
