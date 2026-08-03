---
title: "Model research brief — Where bounded-degree source triviality first fails"
description: "A self-contained mathematical handoff for a research model."
---

# Where bounded-degree source triviality first fails

<p class="claim-tag">Lane 3 · Updated 3 August 2026</p>

## Why this lane matters

Finite-order deformation calculations can make two maps look equivalent even
when no polynomial equivalence exists over the complete base. This lane asks
which intrinsic datum detects that failure, and how the required complexity
grows with the Artin order.

## Setup and notation

This lane contains two related threads. The ready task belongs to the formal
effectivity thread. The finite Kuranishi reconstruction is retained as exact
input for a later chain comparison, but no theorem currently identifies the
two deformation complexes.

### Thread A — finite Kuranishi reconstruction

Work over a characteristic-zero field. The fixed degree-seven affine slice
has ten tangent parameters \(u_1,\ldots,u_{10}\), maximal ideal

\[
\mathfrak m=(u_1,\ldots,u_{10}),
\]

and a filtered transverse Kuranishi ideal
\(I\subset k[[u_1,\ldots,u_{10}]]\). A new minimal generator of initial
degree \(r\) is a nonzero degree-\(r\) initial class in \(I/\mathfrak m I\).
This is the convention used by the order-five and order-six certificates.

### Thread B — formal effectivity of the cubic frame

For a commutative \(\mathbf Q\)-algebra \(R\), put

\[
c=2x-3x^2y-x^3z,\qquad t=y+\frac1x,\qquad r=\frac2x.
\]

Here **admissible** means
\(A(0)=0\), \(A'(0)=1\), \(B(0)=-2\), and
\(B'(0)=-2A''(0)\). For an admissible pair \(A,B\in R[c]\), the cubic-frame map
\(G_{A,B}=(a,b,c)\) is defined by

\[
b=r-3A(c)t^2-2B(c)t,\qquad
2a=A(c)t^3+B(c)t^2+tb.
\]

The admissibility conditions make these expressions polynomial. Define

\[
A_\alpha(c)=c(1+\alpha c),\qquad
B_{\alpha,q}(c)=-2-4\alpha c+q\alpha^2c^2,
\]

and let \(F_{\alpha,q}=G_{A_\alpha,B_{\alpha,q}}\) be the associated
cubic-frame Keller map. For \(\phi(c)\in cR[c]\), the source root translation

\[
\Theta_\phi(x,y,z)=
\left(x,\,y+\phi(c),\,z-3\frac{\phi(c)}x\right)
\]

is polynomial because \(c/x=2-3xy-x^2z\). The explicit triangular target
map \(\Xi_\phi\) in the linked theorem satisfies

\[
G_{A,B+3A\phi}=\Xi_\phi\circ G_{A,B}\circ\Theta_\phi.
\]

A **framed degree-\(D\) equivalence** here means one of these \(c\)-fixed
root translations with \(\deg_c\phi\le D\), together with its displayed
target correction. This is narrower than arbitrary stable polynomial
left-right equivalence.

For \(q\ne q'\) and \(R_M=\mathbf C[s]/(s^M)\), let
\(\kappa_M(q,q')\) be the minimum, over all ordinary or stabilized polynomial
left-right equivalences between \(F_{s,q}\) and \(F_{s,q'}\) over \(R_M\), of

\[
\max\{m,\deg\Phi,\deg\Phi^{-1},\deg\Psi,\deg\Psi^{-1}\},
\]

where \(m\) is the number of stabilization variables.

For \(\alpha=s\), the normalized conductor chart has an escaping divisor
\(c=-1/s\). Its boundary value
\(B_{s,q}(-1/s)=q+2\) is the **escaping conductor decoration** that the
stable classification recovers on the generic fibre.

## Reusable mathematics

### Thread B: exact framed law

Put \(\delta=q'-q\). A framed translation of \(c\)-degree at most \(D\)
exists exactly when \(\delta\alpha^{D+2}=0\). It is unique, with residual
\((-1)^D\delta\alpha^{D+2}c^{D+2}\). Thus for
\(\alpha=s\bmod s^M\) its exact degree is \(M-2\).

### Thread B: formal non-effectivity

The maps \(F_{s,q}\) and \(F_{s,q'}\) are compatibly polynomially
left-right equivalent over every \(R_M\), but are not stably polynomially
left-right equivalent over \(\mathbf C[[s]]\). The nonexistence uses the
proved stable \(q\)-classification after passage to the generic fibre.

### Thread B: unrestricted lower bound

The exact theorem proves

\[
\liminf_{M\to\infty}
\frac{\kappa_M(q,q')}{\log\log M}\ge \frac1{\log4}.
\]

It does not prove a linear unrestricted degree law.

### Thread A: finite reconstruction

The exact direct-coordinate replay gives

| degree | initial rank | Hilbert value | new minimal generators |
| ---: | ---: | ---: | ---: |
| 2 | 11 | 44 | 11 |
| 3 | 112 | 108 | 13 |
| 4 | 558 | 157 | 11 |
| 5 | 1857 | 145 | 0 |

At degree five, \(\operatorname{rank}(\mathfrak m I)=2503\) and
\(\operatorname{rank}(I)=2538\). This is an exact replay of recovered
equations, not an independent derivation from the displayed base map.

### Thread A: the primitive sextic

The order-six computation gives one new weight-three class, represented by

\[
642816u_1u_6u_7^4-60u_4u_7u_8^4+5u_4u_8^5
-75u_5u_6u_8^4.
\]

Here \(\operatorname{rank}(\mathfrak m I)=542\),
\(\operatorname{rank}(I)=545\), and the corresponding pure-sextic initial
ranks are \(341\) and \(342\). This is a finite weighted calculation, not an
orbit classification.

## Live problem

Find an invariant of the unframed stable left-right groupoid that recovers
the escaping conductor decoration in the family \(F_{s,q}\). Quantify how a
complexity-\(D\) equivalence can transport that invariant through the Artin
tower, and improve the proved double-logarithmic lower bound if possible.

## Ready task L3-T1 — intrinsic recovery from the Artin tower

**Inputs.** The complete
[formal-effectivity theorem](lane-3-source-packet.md#source-c413ecb87f258d26),
the [recovery integration and evidence boundaries](lane-3-source-packet.md#source-2210ec80b02f0f23),
and the stable-\(q\) classification in
[Paper 4](../proof-sources/04-stable-moduli/main.md).

**Deliverable.** Give an invariant defined without choosing the conductor
frame whose comparison with the normalized generic fibre recovers the value
\(B_{s,q}(-1/s)=q+2\), so equality of the invariant for two members forces
\(q=q'\). Prove how every complexity-\(D\) equivalence transports it through
each \(R_M\); and obtain either a stronger lower bound for \(\kappa_M\) or a
precise mechanism showing why the present effective-Nullstellensatz bound is
the natural limit of this method.

**Dependencies.** The stable inequivalence of distinct \(q\), compatibility
of the explicit Artin equivalences, and the exact definition of
\(\kappa_M\) above.

**Limits.** The sharp \(M-2\) law is framed. It may not be promoted to an
unframed lower bound without a new invariant argument.

## Non-ready follow-up — compare direct and marked-root complexes

A chain-level comparison through order six would be useful, but the native
marked-root contracting homotopy and basis data beyond order four are not in
the supplied packet. The known ranks and primitive sextic should not be
recomputed and renamed as that comparison. This follow-up becomes actionable
only when those data are exposed.

Connections to realization complexity in Lane 6 are welcome if they retain
the framed/unrestricted distinction.

## Exact sources

- [Order-five replay and scope](lane-3-source-packet.md#source-cd92beb1f9f8cbbe)
- [Order-five verifier](lane-3-source-packet.md#source-68c9400aba7a75f5)
- [Order-six reconstruction statement and primitive sextic](../proof-sources/03-local-rigidity/appendices/source-flow-reconstruction-progress.md)
- [Formal family and theorem](lane-3-source-packet.md#source-c413ecb87f258d26)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
