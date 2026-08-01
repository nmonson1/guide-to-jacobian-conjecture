# Differential description

`RMU-441A6E6C` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-441A6E6C` · `theorem`

The invariant algebra is
\[
A^K=\ker\left(
A\xrightarrow{d_{X/R}}
A\otimes_R E^\vee
\longrightarrow
A\otimes_R\operatorname{coker}(M^\vee)
\right).
\]
Equivalently, in homogeneous degree \(r\), it is the kernel of one finite
syzygy map
\[
\operatorname{Sym}^r(E^\vee)\longrightarrow
\operatorname{Sym}^{r-1}(E^\vee)\otimes_R\operatorname{coker}(M^\vee).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

If \(f\) is translation-invariant, the linear term of
\(f(p+s)-f(p)\) vanishes modulo the equations \(Ms=0\); this is exactly the
displayed differential-kernel condition.  Conversely, if
\(df=M^\vee h\), work in the coordinate ring of \(X\times_RK\) and put
\(F(t)=f(p+ts)\).  Then
\[
F'(t)=\langle h(p+ts),Ms\rangle.
\]
This vanishes because \(Ms=0\) on \(K\).  Over a \(\mathbb Q\)-algebra a
polynomial with zero derivative is coefficientwise constant, so
\(F(1)=F(0)\) and \(f\) is invariant.  Restricting the differential map to
homogeneous degree \(r\) gives the stated finite syzygy map.

  - Does not establish: Presence in the manuscript is not an independent proof audit.
