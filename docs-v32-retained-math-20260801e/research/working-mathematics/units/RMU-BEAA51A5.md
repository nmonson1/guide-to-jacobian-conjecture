# Classifying map and Cartesian pullback

`RMU-BEAA51A5` · `proposition`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-BEAA51A5` · `proposition`

Let \(F\colon\A^3\to\A^3\) be a generic-degree-three Keller map, and let
\(\pi\colon\overline X\to Y=\A^3\) be the normalization of the target in its
function field.  Assume that \(\pi\) is finite flat of degree three.  Then,
after choosing a frame of the trace-zero bundle, there is a morphism
\[
\gamma\colon Y\longrightarrow V
\]
such that, for \(Y^\circ=\gamma^{-1}(V^{\mathrm{sm}})\), the square
\[
\begin{array}{ccc}
\overline X^\circ&\longrightarrow&\mathcal M^{\mathrm{sm}}\\
\big\downarrow&&\big\downarrow m\\
Y^\circ&\xrightarrow{\ \gamma\ }&V^{\mathrm{sm}}
\end{array}
\]
is Cartesian.  In particular, \(\overline X^\circ\to Y^\circ\) is the
pullback of the universal resultant-one marked-root cover over the full
simple-root locus.  This proves the finite-cover assertion of
\cref{prop:conditional-master}; identifying the original affine source still
requires separate boundary data.

Dependencies:

- `uses` `RMU-DD6B3EDC`: Formal statement references prop:conditional-master.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Put \(\mathcal B=\pi_*\mathcal O_{\overline X}\).  Since \(3\) is invertible,
the trace map splits the unit inclusion and gives
\[
\mathcal B\simeq\mathcal O_Y\oplus\mathcal E,
\qquad
\mathcal E=\ker(\operatorname{tr}_{\mathcal B/\mathcal O_Y}),
\]
where \(\mathcal E\) is locally free of rank two.  Every algebraic vector
bundle on affine space is trivial by the Quillen--Suslin theorem, so choose a
global frame of \(\mathcal E\).

The functorial cubic-algebra/binary-cubic correspondence over an arbitrary
base \cite{miranda1985,wood2011} associates to \(\mathcal B\), with this
frame, a binary cubic and hence the morphism \(\gamma\colon Y\to V\).  On the
nonzero-discriminant locus it identifies \(\Spec_Y\mathcal B\) with the
finite étale scheme of roots of that cubic.

It remains to identify that root scheme with \(\mathcal M^{\mathrm{sm}}\).
Let \(f\in V^{\mathrm{sm}}\), and choose one of its three projective linear
factors \([L]\).  Writing \(f=LQ\), the residual quadratic \(Q\) has two
distinct roots and is coprime to \(L\).  Replacing \((L,Q)\) by
\((sL,s^{-1}Q)\) preserves the product and changes the resultant by
\[
\Res(sL,s^{-1}Q)=s\Res(L,Q).
\]
There is therefore a unique \(s\in\C^*\) for which the resultant is one.
This construction is algebraic in families and is inverse to forgetting the
normalized factorization.  Hence
\(m\colon\mathcal M^{\mathrm{sm}}\to V^{\mathrm{sm}}\) is the universal
three-sheeted root-incidence cover, and the displayed square is Cartesian.

  - Does not establish: Presence in the manuscript is not an independent proof audit.
