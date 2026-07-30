---
title: "Program 6 v13 corrections and proof repairs"
description: "Corrections to Proposition 3.3, the contact-degree argument, the A21 monodromy proof, and the terminal certificate semantics."
---

<p class="claim-tag">Program 6 · v13 audit repair note</p>
# Program 6 v13 corrections and proof repairs

<p class="dek">A source-level correction note for <em>Boundary Belyi Covers and Normal Jets</em>, v13.</p>

[LaTeX correction source](../assets/audit-repairs/program6-v13-corrigendum.tex){ .md-button .md-button--primary }
[Independent small-check scripts](program6-v13-audit-checks.md){ .md-button }
[Checksums and scope](../assets/audit-repairs/program6-v13-audit-manifest.json){ .md-button }

!!! warning "Scope"
    This note repairs hand arguments and clarifies what the stored finite certificates would need to prove. It does **not** independently replay the large terminal archive, certify the upstream Newton queue as exhaustive, or prove the degree-below-125 theorem.

The v13 PDF title page is dated **22 July 2026**. The filename and public manuscript manifest record the **29 July 2026 public release**. These dates should be displayed separately.

## 1. Proposition 3.3: corrected codomain

Let \(A=\deg p\) and \(B=\deg q\), and write the reduced face equation as

\[
F(p,q)=Npq-m u\,p q'+n u\,p'q=\text{constant}.
\]

Variations fixing the constant coefficients lie in

\[
U=u k[u]_{\le A}\oplus u k[u]_{\le B}.
\]

The differential is

\[
L(\alpha,\beta)=N(\alpha q+p\beta)
-m u(\alpha q'+p\beta')+n u(\alpha' q+p'\beta).
\]

The constant coefficient vanishes. The coefficient of \(u^{A+B}\) is

\[
(N-mB+nA)(\alpha_Aq_B+p_A\beta_B),
\]

and the endpoint relation is \(N-mB+nA=0\). Thus the intended map is

\[
\boxed{
L:u k[u]_{\le A}\oplus u k[u]_{\le B}
\longrightarrow u k[u]_{\le A+B-1}.
}
\]

**Corrected Proposition 3.3.** For each explicit reduced cover in Section 3, this map is surjective and its kernel is the source-scaling line spanned by \((up',uq')\). Consequently the normalized quotient solution is a reduced isolated point after quotienting by source scaling.

The existing rank table proves this corrected formulation: the domain has dimension \(A+B\), the displayed rank is \(A+B-1\), and the nonzero source-scaling vector lies in the kernel.

## 2. Proposition 5.2: repaired contact-degree argument

Let \(D=(t=0)\), with coordinate \(s\) along \(D\), and suppose

\[
\pi=t^a c(s)+O(t^{a+1}),\qquad
\tau=\tau_0(s)+\sum_{j\ge1}t^j h_j(s).
\]

The coefficient of \(t^{a-1}dt\wedge ds\) in \(d\pi\wedge d\tau\) is

\[
a c(s)\tau_0'(s).
\]

Therefore

\[
\operatorname{ord}_D(d\pi\wedge d\tau)>a-1
\quad\Longrightarrow\quad d(\tau|_D)=0.
\]

In the normalized Section 5 chart, \(c(s)=s/(s-1)\). At a lower order \(j\), the wedge-invisible homogeneous equation is

\[
a c h_j'-j c'h_j=0,
\]

whose solutions are \(h_j=Cc^{j/a}\). Since \(\operatorname{div}(c)=(0)-(1)\), such a solution is rational exactly when \(a\mid j\). Writing \(j=ar\), it is precisely the leading contribution of the target shear

\[
\tau\longmapsto\tau-C\pi^r.
\]

After all lower resonant shears are removed, if \(e\) is the first remaining normal order, then

\[
\operatorname{ord}_D(d\pi\wedge d\tau)=a+e-1.
\]

Now assume

\[
v_E(P)=-m,\quad v_E(Q)=-n,\quad
v_D(P)=-ma,\quad v_D(Q)=-na,
\]

choose \(c,d\in\mathbf Z\) with \(dn-cm=1\), and set

\[
\pi=P^c/Q^d,\qquad \tau=Q^m/P^n.
\]

If \(x=t^{-1}\) up to a unit and

\[
dP\wedge dQ=x^\kappa\,dx\wedge dy
\]

up to a unit, put \(K_D=\operatorname{ord}_D(dx\wedge dy)\). Direct differentiation gives

\[
d\pi\wedge d\tau
=-P^{c-n-1}Q^{m-d-1}\,dP\wedge dQ,
\]

hence

\[
N:=\operatorname{ord}_D(d\pi\wedge d\tau)
=a(m+n+1)-\kappa+K_D.
\]

Define

\[
e_*=a(m+n)-\kappa+K_D+1.
\]

If \(e_*>0\), then \(N>a-1\), so the wedge order itself forces \(\tau|_D\) to be constant. The normalized resonance argument then gives

\[
\boxed{e=e_*.}
\]

For the regular toric chart in v13, \(K_D=-2\), so

\[
\boxed{e=a(m+n)-\kappa-1.}
\]

### Stored \((4,17)\) contact

For \((m,n,a,\kappa,K_D)=(2,3,4,2,-2)\),

\[
e=4(2+3)-2-1=17>0.
\]

Thus the missing constant-residue step follows from the computed wedge order, and the degree-17 secondary Belyi map survives. Its passport remains

\[
(4^4,1),\qquad (17),\qquad (5,1^{12}).
\]

## 3. Proposition C.1: a hand proof of \(A_{21}\)

Let \(G\) be the monodromy group of a connected degree-21 cover with passport

\[
(2^{10},1),\qquad (3^7),\qquad (17,1^4).
\]

All three branch permutations are even, so \(G\subseteq A_{21}\). Connectedness gives transitivity. A nontrivial block has size \(3\) or \(7\), hence there are \(7\) or \(3\) blocks. The induced permutation of the blocks by the 17-cycle must be trivial, since neither \(S_7\) nor \(S_3\) has an element of order 17. Every block is therefore invariant under that 17-cycle, but the block containing a moved point would have to contain its full 17-element orbit, impossible for a block of size 3 or 7. Thus \(G\) is primitive.

Jordan's theorem now implies that a primitive subgroup of \(S_{21}\) containing a prime 17-cycle, with \(17\le21-3\), contains \(A_{21}\). Therefore

\[
\boxed{G=A_{21}.}
\]

This removes the permutation-certificate dependency for the monodromy identification. The exact count of five maps and their arithmetic orbit remain computational claims.

## 4. Theorem C.6: what the Macaulay minor must certify

Let the selected polynomials be \(F_1,\ldots,F_6\). The certificate must specify finite multiplier spaces \(V_i\), a complete target monomial space \(W\), and

\[
\mu:\bigoplus_{i=1}^6V_i\longrightarrow W,
\qquad (H_i)_i\longmapsto\sum_iH_iF_i.
\]

A nonzero \(7121\times7121\) minor proves the unit-ideal conclusion only if the replay verifies all of the following:

1. the 7,121 rows form the **entire ordered basis** of \(W\);
2. that basis contains the constant monomial \(1\);
3. the reported minor uses every row of \(W\);
4. its reduction has determinant \(859\pmod{2053}\).

Under these conditions \(\mu\) is surjective, so \(1\in\operatorname{im}\mu\subseteq(F_1,\ldots,F_6)\). If the rows are only a subset of a larger target basis, the minor proves only a rank statement; an explicit solution of \(\mu(H_i)=1\) or a Nullstellensatz cofactor identity is then required.

The explicit cofactor identities in Theorem C.7 already provide a complete final proof interface for the two stored branch ideals, subject to the separate correctness of the reduction to those branches.

## 5. Theorem C.8: finite plus Nakayama

Let \(R\) be the unramified local DVR at \((2053,u-216)\), let \(\mathcal T_R\) be the proper toric model, and put

\[
Z=V(g_1,\ldots,g_5)\subseteq\mathcal T_R.
\]

Assume the initial-ideal replay proves that the special fiber \(Z_k\) has no toric-boundary points and is the reduced finite scheme of length 296 represented by the archived multiplication matrices. Properness and finiteness of the closed fiber imply that \(Z\to\operatorname{Spec}R\) is proper and quasi-finite, hence finite.

Write \(A=\Gamma(Z,\mathcal O_Z)\). If multiplication by \(\bar\rho\) on \(A/\mathfrak mA\) is invertible, then

\[
(A/\rho A)\otimes_R k=0.
\]

Nakayama's lemma gives \(A/\rho A=0\), so \(\rho\) is a unit in \(A\). Consequently

\[
\boxed{
V_{\overline{K_0}}(\rho,g_1,g_2,g_3,g_4,g_5)=\varnothing.
}
\]

For the stored specialization, the multiplication determinant is

\[
682\not\equiv0\pmod{2053},
\]

so the conclusion follows. A finite-flat or finite-étale lifting statement is unnecessary for this no-common-zero result.

## 6. Degree-below-125 scope

The Program 6 conclusion should be stated as follows:

> For each displayed terminal system, the exact certificates establish the claimed emptiness. A global conclusion that every plane Keller map of maximum coordinate degree below 125 is an automorphism additionally requires an independently replayed and audited proof that the upstream Newton reduction, saturations, normalizations, branch eliminations, and chart attachments exhaust every candidate.

The degree-below-125 statement may be reported only as an external, source-attributed announcement or literature claim, with its independent review status shown separately. It is not proved by the v13 Program 6 manuscript.

## Disposition

| # | Item | Repair status |
|---:|---|---|
| 1 | Proposition 3.3 | Repaired by specifying the codomain \(u k[u]_{\le A+B-1}\). |
| 2 | Proposition 5.2 | Repaired; the positive wedge order forces constant residue, and the \((4,17)\) application survives. |
| 3 | Proposition C.1 | \(A_{21}\) follows from parity, primitivity, and Jordan's theorem. |
| 4 | Theorem C.6 | Exact logical requirements are specified; the large archive still needs replay against them. |
| 5 | Theorem C.8 | Repaired by properness, finiteness, and Nakayama. |
| 6 | Degree below 125 | Remains conditional inside Program 6 on the upstream exhaustiveness and attachment audit. |

## Evidence boundary

The accompanying small-check archive independently verifies the low-dimensional Hurwitz counts, explicit face identities, tangent ranks and minors, scaling kernels, and basic arithmetic of the quintic coefficient field. It does not replay the 7,121-row Macaulay computation, the full toric initial-ideal calculation, or the branch-reduction pipeline.

[Back to Program 6](programs/plane-boundary-obstructions.md)
