---
title: "Compact toric terminal certificate"
description: "Let\n\\[\n\\rho=F_4,\\qquad(g_1,g_2,g_3,g_4,g_5)\n=(F_6,F_8,F_9,F_{10},F_{11})\n\\]\nbe the six exact normalized obstruction polynomials in the supplement.\nThen\n\\[\nV(\\rho,g_1,g_2,g_3,g_4,g_5)(\\overline {K_0})=\\varnothing\n\\]\nover the quintic coefficient field \\(K_0\\)."
---

# Compact toric terminal certificate

`RMU-EFDE9AD3` · `theorem` · statement version `1`

## Exact statement

Let
\[
\rho=F_4,\qquad(g_1,g_2,g_3,g_4,g_5)
=(F_6,F_8,F_9,F_{10},F_{11})
\]
be the six exact normalized obstruction polynomials in the supplement.
Then
\[
V(\rho,g_1,g_2,g_3,g_4,g_5)(\overline {K_0})=\varnothing
\]
over the quintic coefficient field \(K_0\).

## Evidence and source access

### A proof body follows this labelled manuscript statement.

`SUP-RMUEFDE9AD3-01` · `proof`

A proof body follows this labelled manuscript statement.

**Establishes:** Supplies the manuscript proof attached to this statement.

**Source:** Inline evidence is reproduced below.

At \(p=2053\) and the split value \(u=216\), the five \(g_i\) have mixed
volume \(296\).  The Minkowski sum has \(344\) proper faces: \(270\) have a
monomial initial form, and exact saturated Laurent calculations show that
the other \(74\) initial ideals are unit ideals.  Hence the entire special
toric intersection is the reduced \(296\)-point scheme represented by the
archived multiplication matrices.  Multiplication by \(\rho\) has
determinant \(682\ne0\pmod{2053}\).

Let \(R\) be the unramified local DVR at \((2053,u-216)\), let
\(\mathcal T_R\) be the proper toric model, and put
\(Z=V(g_1,\ldots,g_5)\subseteq\mathcal T_R\).  The special fiber is finite
and has no toric-boundary points.  The non-quasi-finite locus of the proper
morphism \(Z\to\operatorname{Spec}R\) is closed, and its image is closed.  It
contains neither the closed point nor, by specialization in the spectrum of
a local DVR, the generic point.  Hence the morphism is quasi-finite and
proper, therefore finite.  Write \(A=\Gamma(Z,\mathcal O_Z)\).  Invertibility
of multiplication by \(\bar\rho\) on \(A/\mathfrak mA\) gives
\((A/\rho A)\otimes_R k=0\); Nakayama's lemma gives \(A/\rho A=0\).
Thus \(\rho\) is a unit on \(Z\), and the six polynomials have no common
zero over the algebraic closure of the characteristic-zero fraction field.
No finite-flat or finite-\'{e}tale lifting assertion is needed.  Repeating
the modular determinant calculation over the five split embeddings gives
determinant residues \(682,116,337,242,740\), whose product is
\(51\pmod{2053}\).

[Machine-readable graph](../graph.json)
