# Thirty-six minimal equations

`RMU-400F1EBA` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-400F1EBA` · `theorem`

The conormal space of the Kuranishi ideal has dimension
\[
\mu(I_\kappa)
=\dim_\mathbb Q I_\kappa/\mathfrak mI_\kappa=36.
\]
Its initial-order distribution is
\[
11,\ 13,\ 11,\ 0,\ 1
\]
in orders \(2,3,4,5,6\), respectively.  The corresponding torus characters
are
\begin{align*}
E_2(z)={}&z^{-6}+z^{-5}+z^{-2}+z+z^2+z^3+2z^4+2z^5+z^6,\\
E_3(z)={}&z^{-3}+2z^{-2}+2z^{-1}+1+2z+z^2+z^3+z^5+2z^6,\\
E_4(z)={}&z^{-8}+z^{-7}+2z^{-6}+2z^{-5}+z^{-4}+z^{-3}+z^{-2}+2z^5,\\
E_6(z)={}&z^3.
\end{align*}
No new minimal generator first appears in orders seven, eight, or nine.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Exact filtered Kuranishi elimination produces 36 independent classes with the
displayed orders and weights.  Independently within the computational
pipeline, the Koszul complex of the modular algebra gives
\[
\dim_{\mathbb F_p}H_1(u_1,\ldots,u_{10};R_{\mathbb F_p})=36
\]
with the same weight character.  Since
\[
H_1(u;R)\cong
\operatorname{Tor}_1^{S_0}(R,\mathbb Q)
\cong I_\kappa/\mathfrak mI_\kappa,
\]
specialization gives the matching characteristic-zero upper bound.  The 36
exact classes give the lower bound.

  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#thm:equations`](../../proof-sources/03-local-rigidity/main.md#label-thm-equations)
