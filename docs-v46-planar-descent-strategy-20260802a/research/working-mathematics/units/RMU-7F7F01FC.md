# Exact pure-weight certificates

`RMU-7F7F01FC` · `proposition`

## Mathematical record

`RMU-7F7F01FC` · `proposition`

For the Kuranishi germ of \eqref{eq:kuranishi-ring}, the following hold.
\begin{enumerate}[label=(\roman*)]
\item On the positive locus, with parameters
\[
(p_1,p_2,p_3,p_4,p_5)=(u_7,u_8,u_2,u_9,u_{10}),
\]
the eliminated ideal contains
\[
p_1^6,\quad p_2^6,\quad p_3^3,\quad p_4^3,\quad p_5^2.
\]
\item On the negative locus, with parameters
\[
(n_1,n_2,n_3,n_4)=(u_1,u_5,u_4,u_3),
\]
the eliminated ideal contains
\[
n_1^4,\quad n_2^4,\quad n_3^4,\quad n_4^3.
\]
\item The weight-zero locus has one tangent parameter \(q=u_6\).  Its first
nonzero compatibility equation occurs in order three and has coefficient
\[
\frac{212135552}{304438725}q^3.
\]
\end{enumerate}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

The determinant equations are triangular by torus weight.  On the positive
locus, variables in the current weight block enter through \(D\Phi_G\),
while nonlinear terms use lower positive weights.  Exact recursive
elimination through weight six leaves five free tangent parameters; a
rational Gr\"obner basis has 24 elements and contains the five displayed
powers.  The negative calculation reverses the weights.  Elimination through
absolute weight eight produces a 16-element rational Gr\"obner basis
containing the four displayed powers.

In weight zero there are 21 coefficient variables and the linearized
determinant map has rank 20.  Solving the pivot variables formally in \(q\)
produces no order-two compatibility condition.  At order three, the
coefficient of \(x^8y^4z^2\) is the displayed nonzero multiple of \(q^3\).
The scripts, exact outputs, and hash-pinned reproduction record are described
in \cref{sec:computation}.

  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#prop:pure-weight`](../../proof-sources/03-local-rigidity/main.md#label-prop-pure-weight)
