---
title: "The last low-degree plane supports force exactly five boundary covers"
description: "The exact degree-21 Belyi-map classification forced by the two surviving Newton supports below 125."
---

# The last low-degree plane supports force exactly five boundary covers

<p class="dek">A leading-face differential equation reduces an infinite
coefficient problem to five explicit dessins of degree 21.</p>

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
boundary models. The result is also a clean example of the explanatory chain

\[
\text{Newton face}
\longrightarrow
\text{differential equation}
\longrightarrow
\text{Belyi map}
\longrightarrow
\text{finite permutation census}.
\]

Those five models are candidate inputs for later globalization calculations;
this classification does not supply the still-unpublished terminal proof
announced by ratto3423.

## What it does not prove

A face solution need not extend to a global polynomial Keller pair. The
theorem classifies the forced lower face; later layer equations are required
to exclude the two full supports.

## Public proof route

- [Certificate manuscript, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/06-plane-boundary/appendices/degree-twenty-one-certificates.tex) — statement, enumeration, and reconstructed coefficients.
- [Plane-boundary working manuscript PDF, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/06-plane-boundary-obstructions-2026-07-29-v13.pdf) — reader-facing snapshot dated 29 July 2026.
- [Exact computational supplement, pinned ZIP](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/docs-v56-converged-research-20260804j/assets/technical-materials/06-plane-boundary-computational-supplement.zip) — begin with `COMPUTATION.md`, then `computational-supplement/degree-twenty-one/README.md`.

This is an exact computer-assisted theorem claimed in the linked project
source, authored by Nathaniel Monson. Its appearance in the guide is not a
separate independent verification of the certificates or proof.
