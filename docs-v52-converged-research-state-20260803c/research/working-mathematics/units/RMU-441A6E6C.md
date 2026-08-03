---
title: "Differential description"
description: "The invariant algebra is\n\\[\nA^K=\\ker\\left(\nA\\xrightarrow{d_{X/R}}\nA\\otimes_R E^\\vee\n\\longrightarrow\nA\\otimes_R\\operatorname{coker}(M^\\vee)\n\\right).\n\\]\nEquivalently, in homogeneous degree \\(r\\), it is the kernel of one finite\nsyzygy map\n\\[\n\\operatorname{Sym}^r(E^\\vee)\\longrightarrow\n\\operatorname{Sym}^{r-1}(E^\\vee)\\otimes_R\\operatorname{coker}(M^\\vee).\n\\]"
---

# Differential description

`RMU-441A6E6C` · `theorem` · statement version `1`

## Exact statement

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

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMU441A6E6C-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

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

[Machine-readable graph](../graph.json)
