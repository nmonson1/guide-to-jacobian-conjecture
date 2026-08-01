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

The map \(F\) is étale and hence open, so \(O_F\) is closed.  It has
codimension at least two.  Indeed, if an irreducible divisor
\(V(h)\subset Y\) were contained in \(O_F\), then \(h\circ F\) would be a
nowhere-zero polynomial on affine space and hence a nonzero constant.
Dominance makes \(F^*\) injective, forcing \(h\) itself to be constant.

Let
\[
\pi\colon\widetilde X\longrightarrow Y
\]
be the normalization of \(Y\) in \(\C(X)\).  Zariski's Main Theorem factors
\(F\) as an open immersion \(j\colon X\hookrightarrow\widetilde X\) followed
by the finite map \(\pi\).  Put \(D=\widetilde X\setminus X\).  Every
irreducible component of \(D\) has codimension one: this is the purity of the
complement of a dense affine open in a separated locally Noetherian scheme
(Stacks Project, Lemma 31.17.5, Tag
\href{https://stacks.math.columbia.edu/tag/0BCQ}{0BCQ}).  Moreover
\[
S_F=\pi(D).
\]

Take \(y\in S_F^{\mathrm{reg}}\).  After shrinking around \(y\), the reduced
nonproperness set is a regular effective Cartier divisor \(V(f)\).  Over its
complement the finite normalization equals \(X\), so it is a finite
étale cover.  Characteristic zero makes every codimension-one
ramification index tame.  Abhyankar's lemma for a regular divisor (Stacks
Project, Lemma 58.31.5, Tag
\href{https://stacks.math.columbia.edu/tag/0EYG}{0EYG}) therefore gives, after
an étale base change \(\Spec A\to Y\), a disjoint union of standard
normalizations
\[
\Spec A[u_i]/(u_i^{e_i}-f)\longrightarrow\Spec A,
\]
The unique prime divisor over \(V(f)\) in the \(i\)-th piece is
\(E_i=V(u_i)\).

If \(e_i>1\), then \(E_i\) is ramified for \(\pi\), so its generic point
cannot lie in \(X\): otherwise the restriction \(F=\pi|_X\) would ramify.
Thus every ramified \(E_i\) is a boundary component.  Conversely, after
shrinking once more, purity of \(D\) implies that the boundary in each
standard piece is either all of \(E_i\) or none of it.  There is no additional
codimension-two deletion on a retained \(E_i\), because every boundary
divisor in this neighborhood maps into \(V(f)\), and \(E_i\) is the unique
prime over \(f\) in its piece.

Not all \(E_i\) can be deleted.  If they were, an étale-open dense
subset of the divisor \(V(f)\) would be omitted, contradicting
\(\operatorname{codim}O_F\ge2\).  Hence some \(E_i\) is retained.  It must
have \(e_i=1\), and then its point over the chosen lift of \(y\) lies in the
base change of \(X\).  Existence of that point descends through the
surjective étale neighborhood, so \(y\in F(X)\).

Thus every smooth point of \(S_F\) belongs to the image, which is equivalent
to \(O_F\subseteq\Sing(S_F)\).

  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/omitted-values.tex#thm:omitted-singular`](../../proof-sources/01-cubic-incidence/appendices/omitted-values.md#label-thm-omitted-singular)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
