# Exact elimination of the two exceptional `(8,28)` branches

## Result

Let

\[
\begin{aligned}
T(Y)={}&43215205018107904Y^5-15455317150390026240Y^4\\
&+3097871869703740194816Y^3-340770032682537179234304Y^2\\
&+23295891481369636508226432Y-513198182072654549018449551
\end{aligned}
\]

and put \(K=\mathbf Q[\eta]/(T(\eta))\). The exact systems called `b1_dcrit` and `b-1_dcrit` in `certificate_systems.json` consist of nine polynomials

\[
F_{\epsilon,0},\ldots,F_{\epsilon,8}\in K[I,H,G,A],\qquad \epsilon\in\{+1,-1\}.
\]

These are the two exceptional full-polygon branches left after the preceding layer-by-layer reduction.

> **Exact certificate theorem.** For each \(\epsilon=\pm1\), there are polynomials
> \(C_{\epsilon,j}\in K[I,H,G,A]\) such that
> \[
> \sum_{j=0}^{8}C_{\epsilon,j}F_{\epsilon,j}=1.
> \]
> Moreover every product \(C_{\epsilon,j}F_{\epsilon,j}\) has total degree at most \(5\).

Consequently

\[
(F_{\epsilon,0},\ldots,F_{\epsilon,8})=K[I,H,G,A]
\]

for both signs. Neither exceptional branch has a solution over \(\overline K\).

Each certificate has exactly 80 nonzero cofactor monomials. Generator 8 is not needed. The largest displayed numerator or denominator has about 26,600 decimal digits.

## Exact Macaulay proof

Let \(R=K[I,H,G,A]\), and let \(R_{\le5}\) be the vector space of polynomials of total degree at most five. It has

\[
\dim_K R_{\le5}=\binom{5+4}{4}=126.
\]

For each system, form all permitted multiples

\[
mF_{\epsilon,j},\qquad \deg(mF_{\epsilon,j})\le5.
\]

A modular row-echelon calculation at

\[
p=31,\qquad \eta\mapsto-1
\]

selected 111 rows. The corresponding \(111\times111\) pivot minors have determinants

\[
1\pmod{31}\quad(\epsilon=+1),
\qquad
17\pmod{31}\quad(\epsilon=-1).
\]

All coefficient denominators and the field relation are regular under this specialization. Hence these pivot minors are nonzero over \(K\).

Exact GMP rational elimination in the basis

\[
1,\eta,\eta^2,\eta^3,\eta^4
\]

then solved for a row combination equal to the constant monomial vector. The result was checked against **all 126 columns**, not only against the 111 pivot columns. Grouping rows with the same generator gives the displayed Nullstellensatz identities.

The derivation program reported:

```text
b1_dcrit CERTIFIED terms=80 seconds=625.653
b-1_dcrit CERTIFIED terms=80 seconds=742.692
```

A separate GMP program, which performs no elimination and merely rereads the output certificates and multiplies them by the original rows, reported:

```text
b1_dcrit VERIFIED exact over Q[y]/T; terms=80 columns=126
b-1_dcrit VERIFIED exact over Q[y]/T; terms=80 columns=126
```

A separately written Python `Fraction` implementation also reconstructed the cofactors, multiplied them by the nine original generators, reduced modulo \(T\), and obtained exactly the constant polynomial \(1\) for both signs.

## Cleared form

Let \(D_H\) clear all cofactor denominators and \(D_F\) clear all generator denominators. The files `*_cleared_certificate.json` record integer-coefficient representatives

\[
H^{\mathrm{int}}_j=D_HC_j,
\qquad
F^{\mathrm{int}}_j=D_FF_j,
\]

satisfying

\[
D_HD_F=\sum_jH^{\mathrm{int}}_jF^{\mathrm{int}}_j
\]

in \(\mathbf Q[\eta,I,H,G,A]/(T(\eta))\). The decimal lengths are:

| Branch | digits of \(D_H\) | digits of \(D_F\) |
|---|---:|---:|
| \(b=1\) | 26,616 | 898 |
| \(b=-1\) | 26,617 | 898 |

## Mathematical implication

The 2022 reduction of Guccione–Guccione–Horruitiner–Valqui proves that a plane Keller counterexample with maximum coordinate degree below 125 must have degree pair \((72,108)\) or \((108,72)\), and identifies the normalized \((8,28)\) case as the remaining unsolved coefficient system. The authors explicitly state that eliminating it would raise the bound from 108 to 125.

The work preceding this certificate calculation reduced the normalized \((8,28)\) case to:

1. a truncated polygon, eliminated exactly;
2. the full polygon with all ordinary branches eliminated exactly;
3. the two exceptional systems certified here.

Thus, **within that reduction**, this certificate computation closes the last two branches and yields

\[
\boxed{\max\{\deg P,\deg Q\}\ge125}
\]

for a hypothetical plane Keller counterexample.

## Proof audit

The certificate theorem for the two stored ideals is unconditional and independently replayed. It uses only exact integer/rational arithmetic.

The global degree-125 consequence additionally depends on the correctness and exhaustiveness of the earlier symbolic reductions from the two raw Newton-polygon coefficient ideals to the branch systems. The current bundle contains the resulting systems and several intermediate artifacts, but one upstream utility file used by the recursive derivation, `lower_face_layers.py`, is absent. Before treating the degree-125 statement as publication-ready, the full reduction should be rebuilt in one clean script directly from the raw supports and checked by a second implementation.

No conclusion about the full two-dimensional Jacobian conjecture follows from the degree-125 bound alone.

## Primary literature context

J. A. Guccione, J. J. Guccione, R. Horruitiner, and C. Valqui, *Increasing the degree of a possible counterexample to the Jacobian Conjecture from 100 to 108*, arXiv:2204.14178 (2022).

## Minimal replay

From the extracted minimal bundle:

```bash
g++ -O3 -std=c++17 gmp_verify_certificate.cpp -lgmpxx -lgmp \
  -o gmp_verify_certificate

./gmp_verify_certificate \
  b1_dcrit_selected_matrix.txt b1_dcrit_gmp_certificate.txt

./gmp_verify_certificate \
  b-1_dcrit_selected_matrix.txt b-1_dcrit_gmp_certificate.txt
```

The expected output is the two `VERIFIED exact` lines displayed above. The checker recomputes every coefficient of the resulting polynomial in the 126-dimensional degree-five monomial basis.
