---
title: "Five degree-21 dessins on the last supports below 125"
description: "The exact Belyi-map classification forced by the two surviving Newton supports."
---

# Five degree-21 dessins on the last supports below 125

!!! info "Reading level"
    This is a specialist, computer-assisted boundary classification. Read
    [dessins d'enfants](../ideas/dessins.md) for the permutation picture and
    [Newton--Puiseux expansions](../ideas/newton-puiseux.md) for why a plane
    polynomial map produces boundary data.

## What is true and why

The two Newton supports left by the published below-125 reduction force the
same leading-face differential equation. Rewriting it as the derivative of
a rational function produces a Belyi map. Its ramification passport is so
restrictive that the corresponding permutation triples can be completely
enumerated.

## Precise result

For either support, the leading face has the form

\[
P_{\mathrm{face}}=Xp(z),
\qquad
Q_{\mathrm{face}}=X^2Yq(z),
\qquad z=XY^2,
\]

with \(\deg p=7\), \(\deg q=10\), and

\[
pq+2zpq'-3zp'q=1.
\]

Consequently

\[
\tau(z)=z\frac{q(z)^2}{p(z)^3}
\]

is a degree-21 Belyi map with passport

\[
(2^{10}1),\qquad(3^7),\qquad(17\,1^4).
\]

There are exactly five connected dessins with this passport. They form one
arithmetic orbit over an irreducible quintic field, have trivial deck group,
and have monodromy group \(A_{21}\).

## Why it matters

An apparently infinite coefficient problem has become a list of five exact
boundary models. Those five are candidate inputs for terminal globalization
calculations; this classification does not supply the still-unpublished
terminal proof announced by ratto3423. The residue degree also distinguishes
this boundary from a previously proposed degree-16 “Three-dessin” model.

## What it does not prove

A face solution need not extend to a global polynomial Keller pair. The
theorem classifies the forced lower face; later layer equations are required
to exclude the two full supports.

## Proof source and status

- [Certificate manuscript, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/06-plane-boundary/appendices/degree-twenty-one-certificates.tex)
- [Plane-boundary working manuscript PDF, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/06-plane-boundary-obstructions-2026-07-29-v13.pdf)
- [Exact computational supplement, pinned ZIP](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/docs-v56-converged-research-20260804j/assets/technical-materials/06-plane-boundary-computational-supplement.zip)

This is an exact computer-assisted theorem of the project, authored by
Nathaniel Monson. Its enumeration, coefficient reconstruction, and replay
certificates are part of the linked public source snapshot. In the ZIP,
begin with `COMPUTATION.md`; the degree-21 replay is documented in
`computational-supplement/degree-twenty-one/README.md`.
