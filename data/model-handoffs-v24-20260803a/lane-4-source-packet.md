# Lane 4 exact research source packet

This page exposes the proof notes, computation contracts, programs,
and finite inputs used by the focused lane brief. Each section names
its canonical repository path and source hash. No private checkout or
download is required.

## Included files

- `manuscripts/02-low-degree/code/program-2-2026-07-29-v3/f4-marked-chart/quartic_F4_endgame_complete.md` — `51373ef59b0d8ca705048e4c88f615f8f23aba34918de4f16e01cb564669999a`
- `manuscripts/02-low-degree/code/program-2-2026-07-29-v3/f4-marked-chart/verify_quartic_F4_endgame.replay_fixed.py` — `c36723303aadbd669d130e988de76419b4ce0ea739a5ebf99b984b4fc754d94f`
- `research-notes/lane4-f4-contract-20260803-v1/F4_INPUT_CONTRACT.md` — `d8bf85998e9377cba79e551b381ee0ba7dd12f990b78ce39854b551a3bddf61a`
- `research-notes/lane4-f4-contract-20260803-v1/LOCAL_CHART_RECOVERY.md` — `59ce235b71eaa9fa22c437c6aef1b448ee5e342da9554808420c5cadd38efb79`
- `research-notes/lane4-f4-contract-20260803-v1/f4-contract.schema.json` — `65291074944b53aa1581ab4e93694c384987a0115fb59e1802ba63a9bcb82340`
- `research-notes/lane4-f4-contract-20260803-v1/q4-f4-local-chart-v1.json` — `1a139d0a832c48a07b73d6acbe51efc82c11ff40afb6b55a709aeb867659ebe2`
- `research-notes/lane4-f4-contract-20260803-v1/verify_contract_and_routing.py` — `6a64525606f8e21897befcb5a8cf71f2715eb116a8cd8218bebaecd2d11f9bc6`
- `research-notes/lane4-quartic-endgame-20260802-v1/case-tree/lane4-case-tree.csv` — `63962c80bd4a6d61aa3e948109071b9b0393f40c3357bc5c5b0b90aa509ba5c3`
- `research-notes/lane4-quartic-endgame-20260802-v1/case-tree/lane4-global-case-tree.md` — `82393d020cad9346365fe2c388baa7cdd5abb2a2e789eaf3b5e2590998c386d9`

## `manuscripts/02-low-degree/code/program-2-2026-07-29-v3/f4-marked-chart/quartic_F4_endgame_complete.md`

<pre><code class="language-markdown">
# The exceptional triple-ramification F4 endgame in a regular Hilbert--Burch chart

## Status

This note gives a candidate closure of the weighted-inflection `F4` endgame in the primitive binary triple-ramification branch.  It is conditional on the upstream leading-curve and Hilbert--Burch reductions placing the map in the `(3,4)` chart described below.  The calculation is exact, but it has not received independent specialist review.

The public handoff formulates the remaining calculation using a chart-dependent algebraic extension

\&#91;
\mathbf Q(\tau)&#91;d&#93;/(q_4(d,\tau))
\&#93;

and asks for the solution of `D_6=0` followed by a uniform `D_5` obstruction.  The polynomial `q_4(d,\tau)` and the full displayed `D_6,D_5` formulas are not present in the reviewed public artifacts.  The argument below avoids reconstructing that eliminant: it marks the double ramification root and works in regular Hilbert--Burch coordinates.  In those coordinates the highest-\(z\) part of `D_6` is a two-variable divisibility problem, while the coefficient of \(z^2\) in `D_5` is rigid under all lower binary corrections.

The calculation reproduces the recorded anchor

\&#91;
&#91;y^3z^2&#93;D_5=-\frac13
\&#93;

after interchanging \(x\) and \(y\).  It does not yet reproduce the two recorded `D_6` coefficients \(104/3\), because those belong to the unrecovered rational chart rather than the regular marked-root chart used here.

---

## 1. Determinant arc and the rigid coefficient

After rescaling the third target coordinate, write the quartic determinant arc as

\&#91;
\widetilde K_\epsilon
 =\Phi+\epsilon\Psi+\epsilon^2\Xi+\epsilon^3\Lambda,
\&#93;

where

\&#91;
\Phi=(P,Q,R),
\&#93;

with \(P,Q\in k&#91;x,y&#93;_4\) and \(R\in k&#91;x,y&#93;_3\).  Write the normal parts of \(\Psi\) as

\&#91;
A=z\alpha+A_0(x,y),\qquad
B=z\beta+B_0(x,y),\qquad
E=z\eta+E_0(x,y).
\&#93;

The first determinant equation is

\&#91;
J(Q,R)\alpha-J(P,R)\beta+J(P,Q)\eta=0. \tag{1.1}
\&#93;

At the next layer, write

\&#91;
C=\frac{c_0}{2}z^2+zC_1+C_0,
\qquad
D=\frac{d_0}{2}z^2+zD_1+D_0.
\&#93;

Only \(c_0,d_0\) enter the coefficient of \(z\) in `D_6`.  More importantly, the coefficient of \(z^2\) in `D_5` is independent of

* all binary integration constants \(A_0,B_0,E_0,C_0,D_0\);
* the linear forms \(C_1,D_1\);
* the third component of \(\Xi\);
* all linear terms \(\Lambda\).

Indeed, a \(z^2\) term in a three-row Jacobian determinant must use the two \(x,y\)-derivatives of the normal terms and one \(z\)-derivative.  Binary integration constants lower the \(z\)-degree, and the third component of \(\Xi\) is only linear.

For later use, the rigid coefficient is

\&#91;
\begin{aligned}
\Omega_5={}&amp;
 \eta J(\alpha,\beta)
 -\beta J(\alpha,\eta)
 +\alpha J(\beta,\eta)\\
&amp;+c_0\bigl(J(\beta,R)+J(Q,\eta)\bigr)
-d_0\bigl(J(\alpha,R)+J(P,\eta)\bigr).
\end{aligned} \tag{1.2}
\&#93;

Consequently, if \(\Omega_5\ne0\), no choice of lower binary terms can complete the determinant arc.

---

## 2. A regular `(3,4)` Hilbert--Burch chart

Choose the marked one-form

\&#91;
\omega=x\,dy.
\&#93;

Let

\&#91;
R=ax^3+bx^2y+cxy^2+\rho y^3, \tag{2.1}
\&#93;

and define

\&#91;
u=ax^2+bxy+cy^2,\tag{2.2}
\&#93;

\&#91;
v=-\frac b3x^2-cxy-3\rho y^2,\tag{2.3}
\&#93;

\&#91;
P=\frac{3a}{4}x^4+\frac{2b}{3}x^3y+\frac c2x^2y^2,\tag{2.4}
\&#93;

\&#91;
Q_0=ax^3y+bx^2y^2+cxy^3+\frac{3\rho}{4}y^4.\tag{2.5}
\&#93;

Then

\&#91;
dP=x\,dR+v\omega,
\qquad
dQ_0=y\,dR+u\omega. \tag{2.6}
\&#93;

Set

\&#91;
H=-xR_x,
\qquad
w=vy-xu.
\&#93;

Taking exterior products in (2.6) gives the exact factorization

\&#91;
J(Q_0,R)=Hu,
\qquad
J(P,R)=Hv,
\qquad
J(P,Q_0)=Hw. \tag{2.7}
\&#93;

The residual Hilbert--Burch syzygies are

\&#91;
s_3=(x,y,1),
\qquad
s_4=(v,u,0). \tag{2.8}
\&#93;

Hence every normal of degree pattern \((2,2,1)\) satisfying (1.1) is

\&#91;
(\alpha,\beta,\eta)
 =\ell(x,y,1)+\kappa(v,u,0), \tag{2.9}
\&#93;

where

\&#91;
\ell=px+qy
\&#93;

is linear and \(\kappa\in k\).

Define the quadratic form

\&#91;
\begin{aligned}
M={}&amp;\left(\frac{b^2}{3}-ac\right)x^2
 +\left(\frac{2bc}{3}-6a\rho\right)xy
 +(c^2-3b\rho)y^2.
\end{aligned} \tag{2.10}
\&#93;

A direct calculation gives

\&#91;
v\,du-u\,dv=M(y\,dx-x\,dy). \tag{2.11}
\&#93;

Substituting (2.9) into the pure-normal part of `D_6` reduces its coefficient of \(z\) to

\&#91;
S_6=xu\ell^2-2\kappa xyM\ell+3\kappa^2MR. \tag{2.12}
\&#93;

The complete coefficient of \(z\) in `D_6` is therefore

\&#91;
S_6+H(c_0u-d_0v)=0. \tag{2.13}
\&#93;

This is the regular-chart replacement for the rational `q_4,D_6` compatibility calculation.

---

## 3. Weighted inflection

The weighted-inflection condition is that the quadratic \(R_x\) be a square:

\&#91;
R_x=3ax^2+2bxy+cy^2=L^2. \tag{3.1}
\&#93;

Equivalently,

\&#91;
b^2=3ac. \tag{3.2}
\&#93;

There are three geometric cases.

1. The double root of \(R_x\) is distinct from the marked root and from the projective endpoint.  This is the generic chart.
2. The double root collides with one endpoint.  This is the reduced chart.
3. The square is supported on the transverse endpoint.  Then \(a=b=0\), and both leading quartics have the fixed quadratic factor \(y^2\).  This is the already-separated quadratic fixed-factor branch.

If \(R_x=0\), the leading data degenerate to a lower-span or fixed-component leaf.

Thus only the first two cases are intrinsic to the primitive `F4` endgame.

---

## 4. Generic marked weighted-inflection chart

Normalize

\&#91;
a=\frac13,
\qquad b=c=1,
\qquad \rho=\tau.
\&#93;

Then

\&#91;
R=\frac13x^3+x^2y+xy^2+\tau y^3, \tag{4.1}
\&#93;

\&#91;
L=x+y,
\qquad R_x=L^2, \tag{4.2}
\&#93;

\&#91;
u=\frac13x^2+xy+y^2, \tag{4.3}
\&#93;

\&#91;
v=-\frac13x^2-xy-3\tau y^2, \tag{4.4}
\&#93;

\&#91;
H=-xL^2, \tag{4.5}
\&#93;

and

\&#91;
M=\frac{1-3\tau}{3}\,y(2x+3y). \tag{4.6}
\&#93;

The constant target shear

\&#91;
Q=Q_0-\frac12P
\&#93;

gives

\&#91;
Q=-\frac18x^4+\frac34x^2y^2+xy^3+\frac{3\tau}{4}y^4. \tag{4.7}
\&#93;

This is exactly the displayed weighted-quartic shape

\&#91;
q_0x^4+q_2x^2y^2+q_3xy^3+q_4y^4
\&#93;

with \(q_3\ne0\).

### 4.1 Classification of the `D_6` highest-normal part

The coefficient of \(y^5\) in (2.12) is

\&#91;
&#91;y^5&#93;S_6=3\kappa^2\tau(1-3\tau). \tag{4.8}
\&#93;

On the primitive generic open set

\&#91;
\tau\ne0,
\qquad
\tau\ne\frac13,
\&#93;

we must have

\&#91;
\kappa=0. \tag{4.9}
\&#93;

Equation (2.13) becomes

\&#91;
u(\ell^2-c_0L^2)+d_0L^2v=0. \tag{4.10}
\&#93;

Now

\&#91;
u+v=(1-3\tau)y^2,
\&#93;

so \(\gcd(u,v)=1\) for \(\tau\ne1/3\), and

\&#91;
u(-y,y)=\frac13y^2,
\&#93;

so \(L\nmid u\).  Hence

\&#91;
\gcd(u,L^2v)=1. \tag{4.11}
\&#93;

Reducing (4.10) modulo \(u\) forces

\&#91;
d_0=0. \tag{4.12}
\&#93;

It follows that

\&#91;
\ell^2=c_0L^2. \tag{4.13}
\&#93;

Every nonzero normal is therefore, for some \(\lambda\ne0\),

\&#91;
\ell=\lambda L,
\qquad
c_0=\lambda^2,
\qquad
d_0=0. \tag{4.14}
\&#93;

This classifies the highest-\(z\) part of every possible full `D_6` solution.  The remaining, lower-\(z\) equations may or may not be solvable; that distinction is irrelevant because the next rigid coefficient never vanishes.

### 4.2 The `D_5` obstruction

For \(\kappa=0\),

\&#91;
\alpha=\lambda xL,
\qquad
\beta=\lambda yL,
\qquad
\eta=\lambda L.
\&#93;

Substitution into (1.2) gives

\&#91;
\boxed{
\Omega_5=-\lambda^3xu
=-\frac{\lambda^3}{3}x(x^2+3xy+3y^2).
} \tag{4.15}
\&#93;

This is nonzero for every \(\lambda\ne0\).  Since it is the coefficient of \(z^2\), no lower binary term can cancel it.

With \(\lambda=1\), the coefficient of \(x^3z^2\) is

\&#91;
-\frac13.
\&#93;

After interchanging \(x\) and \(y\), this reproduces the recorded consistency anchor

\&#91;
&#91;y^3z^2&#93;D_5=-\frac13. \tag{4.16}
\&#93;

### 4.3 Boundary values of \(\tau\)

If \(\tau=0\), then

\&#91;
R=xu,
\qquad Q_0=yR,
\&#93;

and \(P,Q_0\) have a common linear factor \(x\).  This is the fixed-linear-factor branch.

If \(\tau=1/3\), then

\&#91;
R=\frac13(x+y)^3,
\qquad v=-u.
\&#93;

The residual pair is dependent and all three planar minors acquire the extra factor \(u\); this routes to the high-ramification/aligned-fourth-power branch rather than the primitive triple-ramification chart.

Thus no exceptional value of \(\tau\) remains inside the primitive generic `F4` branch.

---

## 5. Reduced weighted-inflection chart

When the double root reaches the marked endpoint, normalize

\&#91;
a=\frac13,
\qquad b=c=0,
\qquad \rho=\tau\ne0.
\&#93;

Then

\&#91;
R=\frac13x^3+\tau y^3, \tag{5.1}
\&#93;

\&#91;
P=\frac14x^4, \tag{5.2}
\&#93;

\&#91;
Q_0=\frac13x^3y+\frac{3\tau}{4}y^4, \tag{5.3}
\&#93;

\&#91;
u=\frac13x^2,
\qquad v=-3\tau y^2,
\qquad H=-x^3,
\qquad M=-2\tau xy. \tag{5.4}
\&#93;

The coefficient of \(xy^4\) in (2.12) is

\&#91;
&#91;xy^4&#93;S_6=-6\kappa^2\tau^2. \tag{5.5}
\&#93;

Thus

\&#91;
\kappa=0. \tag{5.6}
\&#93;

Equation (2.13), after division by \(x^3\), reads

\&#91;
\frac13\ell^2-
rac{c_0}{3}x^2-3\tau d_0y^2=0. \tag{5.7}
\&#93;

The mixed coefficient forces \(pq=0\).  Projectively there are exactly two nonzero branches.

### 5.1 Branch \(\ell=x\)

Here

\&#91;
c_0=1,
\qquad d_0=0.
\&#93;

Formula (1.2) gives

\&#91;
\boxed{\Omega_5=-\frac13x^3.} \tag{5.8}
\&#93;

### 5.2 Branch \(\ell=y\)

Here

\&#91;
c_0=0,
\qquad d_0=\frac{1}{9\tau}.
\&#93;

Formula (1.2) gives

\&#91;
\boxed{\Omega_5=\frac23y^3.} \tag{5.9}
\&#93;

Both branches are obstructed.

At \(\tau=0\), the leading pair has the common cubic factor \(x^3\), so this endpoint belongs to the fixed-component boundary.

---

## 6. Conclusion

Within the regular marked `(3,4)` Hilbert--Burch chart, every primitive weighted-inflection normal satisfying the highest-\(z\) part of `D_6` has a nonzero, rigid coefficient of \(z^2\) in `D_5`.

More precisely:

\&#91;
\boxed{
\begin{array}{ll}
\text{generic chart:}&amp;
\Omega_5=-\lambda^3xu\ne0,\\&#91;1mm&#93;
\text{reduced }\ell=x\text{ chart:}&amp;
\Omega_5=-\frac13x^3\ne0,\\&#91;1mm&#93;
\text{reduced }\ell=y\text{ chart:}&amp;
\Omega_5=\frac23y^3\ne0.
\end{array}}
\&#93;

All parameter values at which the `D_6` classification changes route to an already separated fixed-component or high-ramification branch.

Therefore the regular-chart calculation gives a candidate closure of the exceptional `F4` endgame:

&gt; **Candidate F4 exclusion.**  Subject to the upstream triple-ramification Hilbert--Burch classification and the stated boundary routing, no primitive quartic Keller map exists on the weighted-inflection `F4` locus.

The chart-dependent quartic extension \(q_4(d,\tau)\) is not needed for the exclusion: marking the double ramification root replaces it by the linear syzygy coordinate \(\ell\), and `D_6` forces \(\ell\) to be the square root \(L\) itself.  The surviving `D_5` coefficient is then visibly nonzero.

---

## 7. Remaining audit items

Before this should be promoted from a candidate result to a theorem in the guide, four checks remain.

1. Verify line by line that the continuation appendix's exceptional `F4` divisor is birationally identical to the marked chart (2.1)--(2.9), including the reduced endpoint.
2. Translate between the unrecovered \((d,\tau)\) coordinates and the marked double-root coordinate.  This is expected to explain the eliminant \(q_4(d,\tau)\) as a chart artifact.
3. Reproduce the recorded `D_6` coefficients \(104/3\) after translating normalizations.  The `D_5` anchor \(-1/3\) is already reproduced exactly.
4. Replay the calculation independently in a second computer-algebra system and audit the upstream case tree.

None of these items changes the internal algebra of the regular-chart obstruction; they concern identification and exhaustiveness relative to the public continuation chart.
</code></pre>

## `manuscripts/02-low-degree/code/program-2-2026-07-29-v3/f4-marked-chart/verify_quartic_F4_endgame.replay_fixed.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact verifier for the weighted-inflection F4 endgame.

The calculation is performed in a regular Hilbert--Burch chart.  It proves
that the z^2 coefficient of D5 is nonzero after all D6-compatible normals,
for both the generic q3 != 0 chart and the reduced q3 = 0 chart.
"""
from __future__ import annotations
import sympy as sp
x,y,z,t,p,q,k,c0,d0=sp.symbols('x y z t p q k c0 d0')

def J(f,g): return sp.expand(sp.diff(f,x)*sp.diff(g,y)-sp.diff(f,y)*sp.diff(g,x))
def detJ(f1,f2,f3):
    return sp.expand(sp.Matrix(&#91;&#91;sp.diff(f1,v) for v in (x,y,z)&#93;,
                                &#91;sp.diff(f2,v) for v in (x,y,z)&#93;,
                                &#91;sp.diff(f3,v) for v in (x,y,z)&#93;&#93;).det())
def hpart(f,n):
    P=sp.Poly(sp.expand(f),x,y,z); out=0
    for mon,coef in P.terms():
        if sum(mon)==n: out += coef*x**mon&#91;0&#93;*y**mon&#91;1&#93;*z**mon&#91;2&#93;
    return sp.expand(out)
def zcoef(f,j): return sp.Poly(sp.expand(f),z).coeff_monomial(z**j)

# --------------------------------------------------------------------------
# 1. Canonical (3,4) Hilbert--Burch gradient factorization.
# --------------------------------------------------------------------------
a,b,c,rho=sp.symbols('a b c rho')
u=a*x**2+b*x*y+c*y**2
v=-sp.Rational(1,3)*b*x**2-c*x*y-3*rho*y**2
R=a*x**3+b*x**2*y+c*x*y**2+rho*y**3
P=sp.Rational(3,4)*a*x**4+sp.Rational(2,3)*b*x**3*y+sp.Rational(1,2)*c*x**2*y**2
Q0=a*x**3*y+b*x**2*y**2+c*x*y**3+sp.Rational(3,4)*rho*y**4
w=sp.expand(v*y-u*x)
H=sp.expand(-x*sp.diff(R,x))
assert sp.expand(J(Q0,R)-H*u)==0
assert sp.expand(J(P,R)-H*v)==0
assert sp.expand(J(P,Q0)-H*w)==0
# Gradient factorization with omega=x dy.
assert sp.expand(sp.diff(P,x)-x*sp.diff(R,x))==0
assert sp.expand(sp.diff(P,y)-x*sp.diff(R,y)-x*v)==0
assert sp.expand(sp.diff(Q0,x)-y*sp.diff(R,x))==0
assert sp.expand(sp.diff(Q0,y)-y*sp.diff(R,y)-x*u)==0

# Hessian-like quadratic M from v du-u dv.
M=(sp.Rational(1,3)*b**2-a*c)*x**2+(sp.Rational(2,3)*b*c-6*a*rho)*x*y+(c**2-3*b*rho)*y**2
eta_x=sp.expand(v*sp.diff(u,x)-u*sp.diff(v,x))
eta_y=sp.expand(v*sp.diff(u,y)-u*sp.diff(v,y))
assert sp.expand(eta_x-y*M)==0
assert sp.expand(eta_y+x*M)==0

# General binary D7 normal ell*s3+k*s4.
ell=p*x+q*y
Az=sp.expand(x*ell+k*v)
Bz=sp.expand(y*ell+k*u)
Ez=ell
assert sp.expand(u*Az-v*Bz+w*Ez)==0
A3=z*Az; B3=z*Bz; E2=z*Ez
D6self=zcoef(detJ(A3,B3,R)+detJ(P,B3,E2)+detJ(A3,Q0,E2),1)
D6compact=sp.expand(x*u*ell**2-2*k*x*y*M*ell+3*k**2*M*R)
assert sp.expand(D6self-D6compact)==0

# General z^2 coefficient of D5 after Czz=c0 and Dzz=d0.
C2=sp.Rational(1,2)*c0*z**2
D2=sp.Rational(1,2)*d0*z**2
D5=hpart(detJ(A3,B3,E2)+detJ(A3,D2,R)+detJ(C2,B3,R)
         +detJ(P,D2,E2)+detJ(C2,Q0,E2),5)
O5=zcoef(D5,2)
O5formula=(Ez*J(Az,Bz)-Bz*J(Az,Ez)+Az*J(Bz,Ez)
           +c0*(J(Bz,R)+J(Q0,Ez))-d0*(J(Az,R)+J(P,Ez)))
assert sp.expand(O5-O5formula)==0

# --------------------------------------------------------------------------
# 2. Generic weighted-inflection chart q3 != 0.
# Normalize b=c=1, a=1/3; then R_x=(x+y)^2.
# --------------------------------------------------------------------------
subs_generic={a:sp.Rational(1,3),b:1,c:1,rho:t}
ug=sp.expand(u.subs(subs_generic)); vg=sp.expand(v.subs(subs_generic))
Rg=sp.expand(R.subs(subs_generic)); Pg=sp.expand(P.subs(subs_generic)); Qg0=sp.expand(Q0.subs(subs_generic))
Hg=sp.expand(H.subs(subs_generic)); Mg=sp.factor(M.subs(subs_generic))
L=x+y
assert sp.expand(sp.diff(Rg,x)-L**2)==0
assert sp.expand(Hg+x*L**2)==0
assert sp.expand(Mg-(1-3*t)*y*(2*x+3*y)/3)==0
# Target shear gives exactly the displayed weighted quartic shape.
Qg=sp.expand(Qg0-sp.Rational(1,2)*Pg)
assert sp.expand(Qg-(-sp.Rational(1,8)*x**4+sp.Rational(3,4)*x**2*y**2+x*y**3+sp.Rational(3,4)*t*y**4))==0

# The generic D6-compatible normal is ell=L,k=0, with Czz=1,Dzz=0.
normal_generic={p:1,q:1,k:0,c0:1,d0:0,**subs_generic}
Sg=sp.expand(D6self.subs(normal_generic))
assert sp.expand(Sg+Hg*ug)==0
Og=sp.factor(O5.subs(normal_generic))
expected_generic=-sp.Rational(1,3)*x*(x**2+3*x*y+3*y**2)
assert sp.expand(Og-expected_generic)==0

# Check the decisive extreme coefficient forcing k=0 away from t=0,1/3.
Sg_general=sp.Poly(sp.expand(D6self.subs(subs_generic)),x,y)
assert sp.expand(Sg_general.coeff_monomial(y**5)-3*k**2*t*(1-3*t))==0

# --------------------------------------------------------------------------
# 3. Reduced weighted-inflection chart q3=0.
# Normalize a=1/3,b=c=0,rho=t, so R_x=x^2 and H=-x^3.
# --------------------------------------------------------------------------
subs_red={a:sp.Rational(1,3),b:0,c:0,rho:t}
ur=sp.expand(u.subs(subs_red)); vr=sp.expand(v.subs(subs_red))
Rr=sp.expand(R.subs(subs_red)); Pr=sp.expand(P.subs(subs_red)); Qr=sp.expand(Q0.subs(subs_red))
Hr=sp.expand(H.subs(subs_red)); Mr=sp.expand(M.subs(subs_red))
assert sp.expand(sp.diff(Rr,x)-x**2)==0
assert sp.expand(Hr+x**3)==0
assert sp.expand(Mr+2*t*x*y)==0
# The xy^4 coefficient forces k=0 for t != 0.
Sr_general=sp.Poly(sp.expand(D6self.subs(subs_red)),x,y)
assert sp.factor(Sr_general.coeff_monomial(x*y**4))==-6*k**2*t**2

# Two projective normals remain: ell=x and ell=y.
red_x={p:1,q:0,k:0,c0:1,d0:0,**subs_red}
assert sp.expand(D6self.subs(red_x)+Hr*ur)==0
Oredx=sp.factor(O5.subs(red_x))
assert sp.expand(Oredx+sp.Rational(1,3)*x**3)==0
red_y={p:0,q:1,k:0,c0:0,d0:1/(9*t),**subs_red}
assert sp.expand(D6self.subs(red_y)+Hr*(-sp.Rational(1,1)/(9*t))*0)==sp.expand(D6self.subs(red_y))  # no-op sanity
# Direct D6 cancellation: S+H*(c0*u-d0*v)=0.
assert sp.expand(D6self.subs(red_y)+Hr*(0*ur-(1/(9*t))*vr))==0
Oredy=sp.factor(O5.subs(red_y))
assert sp.expand(Oredy-sp.Rational(2,3)*y**3)==0

# --------------------------------------------------------------------------
# 4. Direct determinant replay for the generic and reduced x branches.
# --------------------------------------------------------------------------
def replay(Pv,Qv,Rv,az,bz,ez,cv,dv):
    F1=Pv+z*az+sp.Rational(1,2)*cv*z**2
    F2=Qv+z*bz+sp.Rational(1,2)*dv*z**2
    F3=Rv+z*ez
    Det=detJ(F1,F2,F3)
    return hpart(Det,7),hpart(Det,6),hpart(Det,5)
D7g,D6g,D5g=replay(Pg,Qg0,Rg,x*L,y*L,L,1,0)
assert D7g==0 and D6g==0
assert sp.expand(zcoef(D5g,2)-expected_generic)==0
D7r,D6r,D5r=replay(Pr,Qr,Rr,x**2,x*y,x,1,0)
assert D7r==0 and D6r==0
assert sp.expand(zcoef(D5r,2)+sp.Rational(1,3)*x**3)==0

print('PASS: canonical (3,4) Hilbert--Burch gradient factorization')
print('PASS: compact D6 self-obstruction formula')
print('PASS: general rigid z^2 coefficient formula for D5')
print('PASS: generic weighted-inflection chart; D5 obstruction =', expected_generic)
print('PASS: reduced x-normal chart; D5 obstruction = -x^3/3')
print('PASS: reduced y-normal chart; D5 obstruction = 2*y^3/3')
print('PASS: direct determinant replay through D5')
</code></pre>

## `research-notes/lane4-f4-contract-20260803-v1/F4_INPUT_CONTRACT.md`

<pre><code class="language-markdown">
# Exact input contract for the Q4-F4 compatibility problem

## Status

This document specifies the minimum data needed for an auditable elimination
of the surviving Lane 4 terminal system. It is deliberately fail-closed.

The current sources identify an exceptional branch with ramification degree
3 and Hilbert--Burch type (3,4), and report that the remaining
weighted-inflection family is defined over a finite extension of
Q(tau). They do not publish, in one reconstructible artifact, the defining
polynomial q4(d,tau), the normalized forms P,Q,R, the complete gauge choices,
every allowed coefficient of H3,H2,L, or every factor inverted on the F4
chart.

Consequently this packet does not manufacture an F4 checker from descriptive
prose. An elimination result is admissible only after a complete instance of
f4-contract.schema.json has been supplied and independently reconstructed
from the geometric normal form.

## Required payload

A complete instance must contain all of the following:

1. Exact source commit, source paths, SHA-256 digests, and derivation
   locators for every formula.
2. The explicit polynomial q4(d,tau), immutable variable order, and exact
   open set on which its field statement is used.
3. Exact P,Q,R, with direct checks of their degrees, gcd(P,Q)=1,
   Hilbert--Burch type (3,4), and ramification degree 3.
4. The most general H3,H2,L allowed after normalization. Every removed
   coefficient must be paired with the invertible action that removes it.
5. One product S containing every pivot, denominator, discriminant,
   resultant, and rank minor inverted in reaching F4.
6. A separate route or saturated system for every irreducible factor of S
   and for intersections where the rank profile changes.
7. A canonical determinant-layer convention and the exact list of layers
   already solved.
8. At least two exact sample reconstructions, including a previously
   reported obstruction, with expected coefficient vectors and hashes.

The linear part may be normalized to the identity only if the supplied
source and target actions prove that this preserves the F4 chart and all
lower-layer freedom. Otherwise L remains a general invertible matrix and the
ideal includes an auxiliary equation u det(L)-1.

## Canonical ring and symbol order

The intended generic coordinate ring is

    Q&#91;tau,d,a,b,l,u&#93; / (q4(d,tau), u*S*det(L)-1),

where a, b, and l are precisely the coefficients left in H3, H2, and L.
The instance must prescribe an immutable symbol order. Hashes are computed
from canonical polynomial serialization, not pretty-printed CAS output.

## Elimination protocol

### Stage A: solve D6 as a module

Separate the coefficients occurring linearly in D6 and write M6*u=b6.
Compute its generic rank and rank-drop Fitting ideals, an exact affine
solution u=u0+N*lambda on the declared open set, and a substitution check of
every D6 coefficient. Every pivot division must be recorded in S.

### Stage B: test all D5 cancellations in the cokernel

After substituting the full D6 solution, write D5=omega+T*v, where v includes
every still-free coefficient able to cancel the reported obstruction.
Cancellation is possible exactly when omega vanishes in coker(T). A useful
certificate is either a symbolic left-kernel vector ell*T=0 with ell*omega
invertible on the chart, or augmented maximal minors proving a rank jump.

A coefficient obstruction obtained after setting any allowed component of v
to zero is not a certificate for the unrestricted branch.

### Stage C: saturation certificate

Let I contain q4, all D6 and D5 coefficients, the normal-form relations, and
u*S*det(L)-1. The generic chart is empty exactly when 1 lies in I. The final
artifact must include a compact exact certificate and an independent
characteristic-zero verifier.

Finite-field computations may discover ranks, monomial orders, and
certificate support. They are not the final characteristic-zero proof.

### Stage D: exceptional factors

Every factor of S=0 is recomputed from its own polynomial system. It cannot
be obtained by substituting zero into a formula derived after division by
that factor. Intersections are separate whenever rank or stabilizer dimension
changes.

### Stage E: a surviving component

If the saturated D6/D5 ideal is not the unit ideal, compute a primary
component or rational univariate representation and continue through every
remaining determinant layer. Solving D6 and D5 alone produces only a
candidate jet.

## Acceptance checklist

- q4(d,tau) is explicit and hash-pinned.
- P,Q,R are explicit and independently reconstructed.
- All unrestricted coefficients of H3,H2,L are present.
- Every gauge removal has an explicit invertible action.
- The complete open-factor product S is explicit.
- Every factor of S=0 has a separate owner or saturation.
- D6 is solved without a hidden pivot division.
- D5 is tested modulo all cancellation variables.
- The characteristic-zero certificate is independently verified.
- Sample values are reconstruction tests, not a generic proof.

Until these items are supplied, Q4-F4 is an exact research target but not a
publicly reconstructible finite system.
</code></pre>

## `research-notes/lane4-f4-contract-20260803-v1/LOCAL_CHART_RECOVERY.md`

<pre><code class="language-markdown">
# Recovered Q4-F4 local-chart certificate

The public degree-three v5 archive contains more exact F4 data than the
earlier intake summary preserved here: it reconstructs explicit `q4`,
`P,Q,R`, one normal solution `(u,v,C,D=d)`, six encoded `D6` coefficients,
and four pure-`z^2` `D5` coefficients.  All twelve surviving archive programs
replay deterministically with SymPy 1.14.0, and every fresh output is
byte-identical to its stored replay target.

`q4-f4-local-chart-v1.json` preserves that result without weakening the
complete `f4-contract.schema.json` gate.  Its local schema requires the
following negative facts:

- the archived solution is not a general `D6` module solution;
- the four `D5` coefficients do not include every possible lower-layer
  cancellation variable;
- the reported denominator list is not certified as the complete chart-open
  product;
- complement routes, gauges, and unrestricted `H3,H2,L` are absent; and
- there is no characteristic-zero saturation or unit-ideal certificate for
  the full system.

Within the encoded chart, the exact calculation proves that all six displayed
`D6` coefficients vanish modulo `q4`.  For the four displayed `D5`
coefficients, their resultants with `q4` have only the reported common
boundary factor, and the residual primitive gcd is one.  The two roots over
`tau=3` give nonzero values `Xi(1,1)=-5/54` and `5/54` as reconstruction
samples.

This is a local algebra certificate, not a global chart theorem.  In
particular it does not show that every allowed `D5` cancellation has been
tested, that all F4 complements are owned, that the degree-three chart family
is exhaustive, or that the rooted quartic case tree covers every normalized
quartic Keller map.

Replay from the repository root with:

```bash
uv run --with sympy==1.14.0 python \
  research-notes/lane4-f4-contract-20260803-v1/verify_q4_f4_local_chart.py

uv run --with sympy==1.14.0 python \
  research-notes/lane4-f4-contract-20260803-v1/verify_degree3_archive_replay.py
```
</code></pre>

## `research-notes/lane4-f4-contract-20260803-v1/f4-contract.schema.json`

<pre><code class="language-json">
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://nmonson1.github.io/guide-to-jacobian-conjecture/schemas/lane4-f4-contract-v1.json",
  "title": "Lane 4 Q4-F4 exact input contract",
  "type": "object",
  "additionalProperties": false,
  "required": &#91;
    "schema_version",
    "branch_id",
    "status",
    "provenance",
    "coefficient_field",
    "symbols",
    "leading_data",
    "lower_layers",
    "chart",
    "determinant_contract",
    "sample_reconstructions"
  &#93;,
  "properties": {
    "schema_version": {"const": 1},
    "branch_id": {"const": "Q4-F4"},
    "status": {"const": "complete"},
    "provenance": {
      "type": "object",
      "additionalProperties": false,
      "required": &#91;"source_commit", "sources"&#93;,
      "properties": {
        "source_commit": {"type": "string", "pattern": "^&#91;0-9a-f&#93;{40}$"},
        "sources": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": &#91;"path", "sha256", "role"&#93;,
            "properties": {
              "path": {"type": "string", "minLength": 1},
              "sha256": {"type": "string", "pattern": "^&#91;0-9a-f&#93;{64}$"},
              "role": {"type": "string", "minLength": 1}
            }
          }
        }
      }
    },
    "coefficient_field": {
      "type": "object",
      "additionalProperties": false,
      "required": &#91;
        "base_field",
        "parameters",
        "algebraic_symbol",
        "minimal_polynomial",
        "localization_factors"
      &#93;,
      "properties": {
        "base_field": {"const": "Q"},
        "parameters": {
          "type": "array",
          "minItems": 1,
          "items": {"type": "string", "minLength": 1}
        },
        "algebraic_symbol": {"type": "string", "minLength": 1},
        "minimal_polynomial": {
          "type": "object",
          "additionalProperties": false,
          "required": &#91;"expression", "variable_order", "sha256"&#93;,
          "properties": {
            "expression": {"type": "string", "minLength": 1},
            "variable_order": {
              "type": "array",
              "minItems": 2,
              "items": {"type": "string", "minLength": 1}
            },
            "sha256": {"type": "string", "pattern": "^&#91;0-9a-f&#93;{64}$"}
          }
        },
        "localization_factors": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": &#91;"id", "expression", "zero_owner"&#93;,
            "properties": {
              "id": {"type": "string", "minLength": 1},
              "expression": {"type": "string", "minLength": 1},
              "zero_owner": {"type": "string", "minLength": 1}
            }
          }
        }
      }
    },
    "symbols": {
      "type": "object",
      "additionalProperties": false,
      "required": &#91;
        "source_variables",
        "parameter_order",
        "h3_coefficients",
        "h2_coefficients",
        "linear_coefficients"
      &#93;,
      "properties": {
        "source_variables": {
          "type": "array",
          "minItems": 3,
          "maxItems": 3,
          "items": {"type": "string", "minLength": 1}
        },
        "parameter_order": {
          "type": "array",
          "minItems": 2,
          "items": {"type": "string", "minLength": 1}
        },
        "h3_coefficients": {
          "type": "array",
          "items": {"type": "string", "minLength": 1}
        },
        "h2_coefficients": {
          "type": "array",
          "items": {"type": "string", "minLength": 1}
        },
        "linear_coefficients": {
          "type": "array",
          "items": {"type": "string", "minLength": 1}
        }
      }
    },
    "leading_data": {
      "type": "object",
      "additionalProperties": false,
      "required": &#91;"P", "Q", "R", "checks"&#93;,
      "properties": {
        "P": {"type": "string", "minLength": 1},
        "Q": {"type": "string", "minLength": 1},
        "R": {"type": "string", "minLength": 1},
        "checks": {
          "type": "object",
          "additionalProperties": false,
          "required": &#91;
            "degrees",
            "coprime_PQ",
            "hilbert_burch_type",
            "ramification_degree"
          &#93;,
          "properties": {
            "degrees": {"type": "array", "const": &#91;4, 4, 3&#93;},
            "coprime_PQ": {"const": true},
            "hilbert_burch_type": {"const": &#91;3, 4&#93;},
            "ramification_degree": {"const": 3}
          }
        }
      }
    },
    "lower_layers": {
      "type": "object",
      "additionalProperties": false,
      "required": &#91;"H3", "H2", "L", "gauges"&#93;,
      "properties": {
        "H3": {
          "type": "array",
          "minItems": 3,
          "maxItems": 3,
          "items": {"type": "string", "minLength": 1}
        },
        "H2": {
          "type": "array",
          "minItems": 3,
          "maxItems": 3,
          "items": {"type": "string", "minLength": 1}
        },
        "L": {
          "type": "array",
          "minItems": 3,
          "maxItems": 3,
          "items": {
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items": {"type": "string", "minLength": 1}
          }
        },
        "gauges": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": &#91;"coefficient", "action", "invertibility_condition"&#93;,
            "properties": {
              "coefficient": {"type": "string", "minLength": 1},
              "action": {"type": "string", "minLength": 1},
              "invertibility_condition": {"type": "string", "minLength": 1}
            }
          }
        }
      }
    },
    "chart": {
      "type": "object",
      "additionalProperties": false,
      "required": &#91;"inherited_hypotheses", "open_product", "complement_routes"&#93;,
      "properties": {
        "inherited_hypotheses": {
          "type": "array",
          "minItems": 1,
          "items": {"type": "string", "minLength": 1}
        },
        "open_product": {"type": "string", "minLength": 1},
        "complement_routes": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": &#91;"factor_id", "owner"&#93;,
            "properties": {
              "factor_id": {"type": "string", "minLength": 1},
              "owner": {"type": "string", "minLength": 1}
            }
          }
        }
      }
    },
    "determinant_contract": {
      "type": "object",
      "additionalProperties": false,
      "required": &#91;
        "map_expression",
        "layer_convention",
        "already_solved_layers",
        "required_layers",
        "linear_invertibility_equation"
      &#93;,
      "properties": {
        "map_expression": {"type": "string", "minLength": 1},
        "layer_convention": {"type": "string", "minLength": 1},
        "already_solved_layers": {
          "type": "array",
          "items": {"type": "integer"}
        },
        "required_layers": {
          "type": "array",
          "minItems": 2,
          "items": {"type": "integer"},
          "contains": {"const": 6}
        },
        "linear_invertibility_equation": {"type": "string", "minLength": 1}
      }
    },
    "sample_reconstructions": {
      "type": "array",
      "minItems": 2,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": &#91;"parameters", "expected_sha256", "expected_obstructions"&#93;,
        "properties": {
          "parameters": {"type": "object"},
          "expected_sha256": {"type": "string", "pattern": "^&#91;0-9a-f&#93;{64}$"},
          "expected_obstructions": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "string", "minLength": 1}
          }
        }
      }
    }
  }
}
</code></pre>

## `research-notes/lane4-f4-contract-20260803-v1/q4-f4-local-chart-v1.json`

<pre><code class="language-json">
{
  "schema_version": 1,
  "branch_id": "Q4-F4",
  "status": "partial_local_chart_certificate",
  "provenance": {
    "repository_commit": "25fd4547397cca49fbff3293e381359930cbdbf0",
    "sources": &#91;
      {
        "path": "manuscripts/02-low-degree/code/program-2-2026-07-30-v5/quartic_binary_endgame/degree3/src/check_F4_weighted.py",
        "sha256": "73e7b0dcb95a0a0922fe09c6b08e358477311525780b692a52d5c287e127130c",
        "role": "recovered principal F4 checker"
      },
      {
        "path": "manuscripts/02-low-degree/code/program-2-2026-07-30-v5/quartic_binary_endgame/degree3/src/common.py",
        "sha256": "87abdeefe37721ded218c989816ab68da00cecfbbff6f6d7c877c34d402cd052",
        "role": "reconstructed exact binary-form helper"
      },
      {
        "path": "manuscripts/02-low-degree/code/program-2-2026-07-30-v5/quartic_binary_endgame/degree3/src/weighted_common.py",
        "sha256": "2e617da21345cc4a2c79ff120c41e93944da7564ed05cb8730e9044d0cf4560e",
        "role": "reconstructed weighted-chart helper"
      },
      {
        "path": "manuscripts/02-low-degree/code/program-2-2026-07-30-v5/quartic_binary_endgame/degree3/stored_outputs/F4_weighted.json",
        "sha256": "4d3985ac48628882e2385e402dc8642452914582ce072e1d9f2b09ae7878d041",
        "role": "byte-replay target and full encoded coefficient artifact"
      }
    &#93;
  },
  "coefficient_field": {
    "description": "Q(tau)&#91;d&#93;/(q4) on the encoded chart",
    "variable_order": &#91;"d", "tau"&#93;,
    "q4": "4*d**2*tau**8 + 48*d**2*tau**7 + 232*d**2*tau**6 + 576*d**2*tau**5 + 772*d**2*tau**4 + 528*d**2*tau**3 + 144*d**2*tau**2 + 24*d*tau**7 + 108*d*tau**6 + 60*d*tau**5 - 180*d*tau**4 - 84*d*tau**3 + 72*d*tau**2 - 288*tau**5 + 153*tau**4 + 306*tau**3 + 45*tau**2 - 180*tau - 36"
  },
  "leading_forms": {
    "coefficient_convention": "&#91;c0,...,cn&#93; means sum c_i*x^(n-i)*y^i",
    "P": &#91;
      "3/4",
      "(-39*tau**2 - 45*tau - 24)/(tau**3 + 8*tau**2 + 21*tau + 18)",
      "(144*tau**4 + 390*tau**3 + 483*tau**2 + 240*tau + 39)/(2*tau**5 + 22*tau**4 + 94*tau**3 + 194*tau**2 + 192*tau + 72)",
      "(-36*tau**3 - 48*tau**2 - 21*tau - 3)/(tau**4 + 10*tau**3 + 37*tau**2 + 60*tau + 36)",
      "0"
    &#93;,
    "Q": &#91;
      "0",
      "3/(tau + 3)",
      "(-39*tau**2 - 45*tau - 24)/(2*tau**3 + 12*tau**2 + 22*tau + 12)",
      "(48*tau**3 + 114*tau**2 + 123*tau + 39)/(tau**4 + 10*tau**3 + 37*tau**2 + 60*tau + 36)",
      "(-108*tau**4 - 180*tau**3 - 111*tau**2 - 30*tau - 3)/(4*tau**5 + 40*tau**4 + 148*tau**3 + 240*tau**2 + 144*tau)"
    &#93;,
    "R": &#91;
      "1",
      "(-39*tau**2 - 45*tau - 24)/(tau**3 + 7*tau**2 + 16*tau + 12)",
      "(72*tau**3 + 159*tau**2 + 162*tau + 39)/(tau**4 + 10*tau**3 + 37*tau**2 + 60*tau + 36)",
      "(-36*tau**4 - 60*tau**3 - 37*tau**2 - 10*tau - 1)/(tau**5 + 10*tau**4 + 37*tau**3 + 60*tau**2 + 36*tau)"
    &#93;
  },
  "encoded_lower_data": {
    "A": &#91;
      "(39*tau**2 + 45*tau + 24)/(tau**4 + 10*tau**3 + 37*tau**2 + 60*tau + 36)",
      "(-72*tau**3 - 159*tau**2 - 162*tau - 39)/(tau**5 + 11*tau**4 + 47*tau**3 + 97*tau**2 + 96*tau + 36)",
      "(36*tau**3 + 48*tau**2 + 21*tau + 3)/(tau**5 + 10*tau**4 + 37*tau**3 + 60*tau**2 + 36*tau)"
    &#93;,
    "B": &#91;
      "3/(tau + 3)",
      "(-39*tau**2 - 45*tau - 24)/(tau**4 + 8*tau**3 + 23*tau**2 + 28*tau + 12)",
      "(24*tau**2 + 45*tau + 39)/(tau**4 + 10*tau**3 + 37*tau**2 + 60*tau + 36)"
    &#93;,
    "normal_solution": {
      "u": "(2*d*tau**5 + 16*d*tau**4 + 46*d*tau**3 + 56*d*tau**2 + 24*d*tau - 36*tau**4 - 27*tau**3 + 15*tau**2 + 36*tau + 12)/(2*tau**5 + 16*tau**4 + 46*tau**3 + 56*tau**2 + 24*tau)",
      "v": "(-12*d*tau**6 - 82*d*tau**5 - 194*d*tau**4 - 194*d*tau**3 - 82*d*tau**2 - 12*d*tau + 126*tau**4 + 141*tau**3 - 66*tau**2 - 159*tau - 42)/(2*tau**6 + 22*tau**5 + 94*tau**4 + 194*tau**3 + 192*tau**2 + 72*tau)",
      "C": "(6*d*tau**5 + 35*d*tau**4 + 62*d*tau**3 + 35*d*tau**2 + 6*d*tau + 18*tau**4 - 21*tau**3 - 9*tau**2 + 9*tau + 3)/(tau**6 + 10*tau**5 + 37*tau**4 + 60*tau**3 + 36*tau**2)",
      "D": "d"
    }
  },
  "chart": {
    "historical_label": "F4",
    "encoded_ansatz": "Recovered common-root weighted-inflection formulas with one displayed normal solution (u,v,C,D=d); the archive does not encode the unrestricted H3,H2,L coefficient space.",
    "declared_nonzero_factors": &#91;
      "tau",
      "tau+1",
      "tau+2",
      "tau+3",
      "tau-1",
      "2*tau+1",
      "3*tau+1"
    &#93;,
    "complete_open_product": false,
    "all_complement_routes_supplied": false
  },
  "determinant_layers": {
    "D6": {
      "encoded_coefficients": 6,
      "remainders_mod_q4": &#91;"0", "0", "0", "0", "0", "0"&#93;,
      "general_module_solution": false
    },
    "D5": {
      "encoded_pure_z2_coefficients": 4,
      "resultant_raw_gcd": "tau**3*(tau - 1)**6*(tau + 1)**4*(tau + 2)**2*(tau + 3)**2",
      "resultant_primitive_gcd": "1",
      "all_cancellation_variables_included": false
    }
  },
  "samples": &#91;
    {"tau": "3", "d": "5/24", "Xi_1_1": "-5/54"},
    {"tau": "3", "d": "-11/24", "Xi_1_1": "5/54"}
  &#93;,
  "full_contract_gate": {
    "accepted_by_complete_f4_schema": false,
    "unrestricted_H3_H2_L_supplied": false,
    "gauge_table_supplied": false,
    "complete_open_product_supplied": false,
    "characteristic_zero_unit_certificate_supplied": false
  },
  "does_not_establish": &#91;
    "a complete instance of f4-contract.schema.json",
    "a general D6 module solution with every allowed lower-layer coefficient",
    "a D5 cokernel obstruction after every allowed cancellation variable",
    "a saturation or unit-ideal certificate for the unrestricted characteristic-zero system",
    "ownership of every vanishing denominator, discriminant, pivot, or rank-drop complement",
    "global chart coverage or exhaustiveness of the quartic case tree",
    "invertibility of every degree-four Keller map"
  &#93;
}
</code></pre>

## `research-notes/lane4-f4-contract-20260803-v1/verify_contract_and_routing.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Check the finite skeleton of the Lane 4 repairs and F4 contract.

This is a regression checker, not a proof of the geometric inputs and not an
elimination of Q4-F4.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
REPOSITORY = ROOT.parents&#91;1&#93;
MANUSCRIPT = REPOSITORY / "manuscripts" / "02-low-degree" / "main.tex"
CONTRACT = ROOT / "F4_INPUT_CONTRACT.md"
SCHEMA = ROOT / "f4-contract.schema.json"


def leading_image_leaves() -&gt; tuple&#91;tuple&#91;int, int, int&#93;, ...&#93;:
    leaves = tuple(
        sorted(
            (e, k, g)
            for e in range(2, 5)
            for k in range(1, 5)
            for g in range(5)
            if g + e * k == 4
        )
    )
    expected = ((2, 1, 2), (2, 2, 0), (3, 1, 1), (4, 1, 0))
    assert leaves == expected
    return leaves


def relative_closure_regression() -&gt; None:
    x, t = sp.symbols("x t")
    polynomial = sp.Poly(x**2 - t, x, domain=sp.QQ.frac_field(t))
    assert polynomial.is_irreducible

    text = MANUSCRIPT.read_text(encoding="utf-8")
    for marker in (
        "Singular homogeneous Jacobian forces a curve image",
        "The span-three entry to the curve tree",
        "does not by itself prove that a chosen parametrization",
        "&#91;x^2:y^2:0&#93;",
        "proof above avoids this shortcut",
    ):
        assert marker in text, marker


def composite_table() -&gt; tuple&#91;tuple&#91;int, int, int, int&#93;, ...&#93;:
    rows = tuple(
        sorted(
            (g, n, e, n // e)
            for g in range(4)
            for n in (4 - g,)
            for e in range(2, n + 1)
            if n % e == 0
        )
    )
    expected = (
        (0, 4, 2, 2),
        (0, 4, 4, 1),
        (1, 3, 3, 1),
        (2, 2, 2, 1),
    )
    assert rows == expected
    return rows


def valuation_skeleton() -&gt; None:
    for length in range(1, 6):
        for values in itertools.product(range(4), repeat=length):
            if sum(values) == 3:
                assert any(value % 2 for value in values)

    for c in (1, 3):
        for multiplicity in range(1, 17):
            if (c * multiplicity) % 4 == 0:
                assert multiplicity % 4 == 0

    assert all((3 * multiplicity) % 4 for multiplicity in (1, 2, 3))

    text = MANUSCRIPT.read_text(encoding="utf-8")
    for marker in (
        "4\\nu_\\Gamma(R)=3\\mu",
        "fixed components can cancel poles",
        "nonnegativity of \\(c_\\xi\\) was used only",
    ):
        assert marker in text, marker


def contract_shape() -&gt; int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = set(schema&#91;"required"&#93;)
    expected = {
        "schema_version",
        "branch_id",
        "status",
        "provenance",
        "coefficient_field",
        "symbols",
        "leading_data",
        "lower_layers",
        "chart",
        "determinant_contract",
        "sample_reconstructions",
    }
    assert required == expected
    assert schema&#91;"properties"&#93;&#91;"status"&#93;&#91;"const"&#93; == "complete"
    assert schema&#91;"properties"&#93;&#91;"branch_id"&#93;&#91;"const"&#93; == "Q4-F4"

    text = CONTRACT.read_text(encoding="utf-8")
    for marker in (
        "deliberately fail-closed",
        "does not manufacture an F4 checker",
        "solve D6 as a module",
        "test all D5 cancellations in the cokernel",
        "saturation certificate",
        "Finite-field computations",
    ):
        assert marker in text, marker
    return len(required)


def main() -&gt; int:
    leaves = leading_image_leaves()
    relative_closure_regression()
    rows = composite_table()
    valuation_skeleton()
    keys = contract_shape()
    print("lane4 structural repair validation: PASS")
    print("leading_image_leaves=" + ";".join(map(str, leaves)))
    print("relative_closure_regression=PASS")
    print(f"composite_rows={len(rows)}")
    print("valuation_skeleton=PASS")
    print(f"f4_required_blocks={keys}")
    print("f4_status=awaiting exact complete instance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

## `research-notes/lane4-quartic-endgame-20260802-v1/case-tree/lane4-case-tree.csv`

<pre><code class="language-csv">
node,parent,hypotheses,owner,packet_status,remaining_boundary
rho1,root,rho4=1,public rank-one theorem,public input,hypotheses of public theorem
span3-conic,root,rho4=3 and image degree 2,seven conic orbit arguments,candidate proofs plus exact checks,specialist review and second CAS
span3-cubic,root,rho4=3 and image degree 3,packet rational-cubic argument,candidate proof plus exact checks,specialist review and plane theorem
span3-quartic,root,rho4=3 and image degree 4,public quartic-frontier theorem,public input,frontier preclassification
R0,rho2,R=0,packet quadratic-coordinate argument,candidate proof,plane theorem citation
binary-fixed,rho2,P Q R binary and gcd(P Q)&gt;1,public fixed-factor packets,public exact packets,proof-to-code crosswalk and second lineage
binary-zero-minor,rho2,P Q R binary gcd=1 and one minor zero,public edge theorem plus packet R=0 argument,public input plus candidate proof,plane theorem citation
binary-fourth-power,rho2,P Q R binary gcd=1 and pencil has fourth power,public fourth-power proposition,public routing input,overlap ownership
r0-2,rho2,binary coprime nonzero minors r&lt;=2,public ramification theorems,public input,source hypotheses as stated
r3-tau-minus-one,r3,independent (3 4) chart and tau=-1,packet tau=-1 theorem,candidate proof plus exact replay,upstream chart placement and specialist review
r3-other,r3,remaining dependent generic resonant and degenerate charts,public v5 chart family,not independently reproduced here,proof-code crosswalk and independent lineage
r4,rho2,binary coprime nonzero minors r=4,packet high-ramification theorem,candidate proof plus exact replay,upstream Hilbert-Burch placement specialist review second CAS
r5,rho2,binary coprime nonzero minors r=5,packet high-ramification theorem,candidate algebraic proof,plane theorem and specialist review
quadratic-source,rho2,nonbinary composite e=2 d=2,public nine-chart theorem,public exact packet,proof-to-code crosswalk
primitive-fourth-power,rho2,nonbinary primitive gcd=1,packet repaired valuation plus public fourth-power proposition,candidate routing repair,overlap ownership
nonbinary-fixed,rho2,nonbinary primitive gcd&gt;1,public valuation plus packet centralizer lemma,candidate proof repair,preceding coefficient derivation and specialist review
</code></pre>

## `research-notes/lane4-quartic-endgame-20260802-v1/case-tree/lane4-global-case-tree.md`

<pre><code class="language-markdown">
# Lane 4 quartic case tree — candidate repaired routing

## Status and scope

This document is an ownership map for the ordinary-degree-four branch in
three variables.  It combines public Program 2 inputs with the candidate
proof repairs and exact calculations in this packet.  It is intended for
specialist review; it is not a generated claim-graph update and does not
promote the global conclusion

\&#91;
D_{\min}\ge 5.
\&#93;

The unconditional public interval remains

\&#91;
4\le D_{\min}\le 7.
\&#93;

Status terms used below have the following meanings.

| Status | Meaning |
| --- | --- |
| public input | A theorem or certificate already present in the public Program 2 source; this packet does not re-prove it. |
| candidate proof | A complete prose argument supplied here, but not yet independently refereed. |
| exact replay | A finite symbolic calculation rerun over exact characteristic-zero arithmetic. |
| conditional | The implication uses an upstream chart-placement, classification, or plane theorem stated separately. |
| not independently reproduced here | The public v5 packet reports a successful replay, but this packet does not supply a new derivation of that chart. |

## Ownership convention

The structural loci overlap.  To turn the cover into a case tree, assign a
map to the first applicable branch in the following order:

1. the zero cubic normal layer `R=0`;
2. the binary branch `P,Q,R in k&#91;x,y&#93;`;
3. the genuinely nonbinary quadratic-source branch;
4. the primitive coprime fourth-power branch;
5. the genuinely nonbinary fixed-component branch.

Inside the binary branch, assign a nonconstant fixed factor before the
fourth-power and ramification branches.  In the coprime branch, remove zero
minors before defining the common ramification degree.  This is an ownership
rule only; it does not claim that the underlying geometric loci are disjoint.

## Structural tree

```text
quartic Keller map F = LX + H2 + H3 + H4
|
+-- rho4 = 1
|   `-- rank-one theorem -&gt; automorphism                         &#91;public input&#93;
|
+-- rho4 = 3
|   |
|   +-- leading image a conic
|   |   +-- four historical invariant-field orbits              &#91;public input&#93;
|   |   `-- G = x^2, xy, z^2                                   &#91;candidate proofs + exact checks&#93;
|   |
|   +-- leading image a proper rational cubic
|   |   `-- cusp/node; transverse and all marked factors        &#91;candidate proof + exact checks&#93;
|   |
|   `-- leading image a proper rational quartic
|       `-- balanced and tricuspidal/frontier types              &#91;public input; preclassification required&#93;
|
`-- rho4 = 2
    |
    +-- normalize H4=(P,Q,0), P,Q independent quartics;
    |   put R=(H3)_3
    |
    +-- R=0
    |   `-- quadratic coordinate + plane reduction              &#91;candidate proof; plane theorem&#93;
    |
    `-- R != 0 and Jac(P,Q,R)=0
        |
        +-- P,Q,R binary in two source forms
        |   |
        |   +-- G=gcd(P,Q) nonconstant
        |   |   +-- deg G=3: squarefree / 2+1 / triple line      &#91;public exact packet&#93;
        |   |   +-- deg G=2: divisor and endpoint tree           &#91;public 38-group packet&#93;
        |   |   `-- deg G=1: residual-cubic orbit tree           &#91;public exact packet&#93;
        |   |
        |   `-- gcd(P,Q)=1
        |       |
        |       +-- U,V,or W zero                                &#91;public edge theorem; R=0 repaired here&#93;
        |       |
        |       +-- pencil contains a fourth power               &#91;public routing proposition&#93;
        |       |
        |       `-- U,V,W nonzero; r=deg gcd(U,V,W)
        |           +-- r=0                                     &#91;public regular theorem&#93;
        |           +-- r=1                                     &#91;public simple-ramification theorem&#93;
        |           +-- r=2                                     &#91;public double-ramification theorem&#93;
        |           +-- r=3
        |           |   +-- dependent (2,5) syzygy               &#91;public v5; not independently reproduced here&#93;
        |           |   `-- independent (3,4) syzygy
        |           |       +-- primitive tau=-1 divisor         &#91;candidate proof + exact replay here&#93;
        |           |       `-- all other generic/exceptional
        |           |           v5 charts                         &#91;public v5; not independently reproduced here&#93;
        |           +-- r=4
        |           |   +-- dependent residual syzygies          &#91;candidate algebraic proof&#93;
        |           |   +-- independent, residual square         &#91;candidate gcd contradiction&#93;
        |           |   `-- independent, reduced residual
        |           |       +-- squarefree Gamma                  &#91;candidate kernel argument&#93;
        |           |       +-- repeated root away from endpoints
        |           |       |   +-- nonprimitive component       &#91;gcd exit&#93;
        |           |       |   +-- generic / 3+1                &#91;candidate proof + exact replay&#93;
        |           |       |   `-- internal 2+2                 &#91;candidate proof + exact replay&#93;
        |           |       `-- repeated endpoint                &#91;candidate proof + exact replay&#93;
        |           `-- r=5                                     &#91;candidate aligned cube/fourth-power proof&#93;
        |
        +-- genuinely nonbinary composite intermediate field
        |   `-- only n=4=(e,d)=(2,2)
        |       +-- binary degeneration                          &#91;binary owner&#93;
        |       +-- fixed-component degeneration                 &#91;fixed owner&#93;
        |       `-- no-fixed genuinely nonbinary locus           &#91;public nine-chart packet&#93;
        |
        +-- composition-primitive, gcd(P,Q)=1, nonbinary
        |   `-- valuation forces a fourth-power member           &#91;candidate repaired routing&#93;
        |       `-- binary / quadratic-source / aligned exit
        |
        `-- composition-primitive, gcd(P,Q)=G nonconstant, nonbinary
            +-- deg G=2                                         &#91;public corrected valuation&#93;
            `-- deg G=1
                `-- aligned / binary / residual-pole branch
                    `-- homogeneous cubic centralizer endpoint   &#91;candidate repair&#93;
```

## Why the span-two structural cover has four owners

Write

\&#91;
P=GA,\qquad Q=GB,\qquad \gcd(A,B)=1,
\&#93;

and put `n=deg A=deg B`.  The weighted one-variable field input gives an
intermediate rational parameter with

\&#91;
n=ed.
\&#93;

After the binary branch is removed, the composite possibilities are

\&#91;
\begin{array}{c|c|c}
\deg G&amp;n&amp;(e,d)\\ \hline
0&amp;4&amp;(4,1),(2,2)\\
1&amp;3&amp;(3,1)\\
2&amp;2&amp;(2,1).
\end{array}
\&#93;

The repaired valuation argument sends every `d=1` case to the binary owner;
the only genuinely nonbinary composite case is `(e,d)=(2,2)`.  For a
primitive coprime reduced pencil, the valuation sum produces a fourth-power
fiber.  For a primitive pencil with `G != 1`, the generic-divisor valuation
puts every component of `G` on a special fiber.  These are exactly the four
structural owners listed above.

## Leaf-to-evidence table

| ID | Leaf | Mathematical owner | Packet evidence | Remaining boundary |
| --- | --- | --- | --- | --- |
| S1 | `rho4=1` | public rank-one theorem | locator only | hypotheses of public theorem |
| S2 | seven conic orbits | four public orbits plus three packet propositions | exact `z^2` checker; exact branch scripts and terminal identities for `x^2,xy` | specialist review; second CAS desirable |
| S3 | proper rational cubic | packet cusp/node argument | exact transverse, marked-node, marked-cusp and pivot-minor scripts | specialist review; plane theorem |
| S4 | proper rational quartic | public frontier theorems | locator only | upstream quartic-image preclassification |
| B0 | `R=0` | packet quadratic-coordinate argument | prose proof | exact per-coordinate plane-theorem citation |
| B1 | nonbinary `(2,2)` | public nine-chart theorem | locator only | proof-to-code crosswalk |
| B2 | binary fixed factors | public fixed-factor packets | locator only | proof-to-code crosswalk; second lineage |
| B3 | coprime binary `r&lt;=2` | public ramification filtration | locator only | source hypotheses as stated |
| B4a | primitive `r=3`, `tau=-1` | packet theorem | exact standalone checker and stored output | upstream chart placement; specialist review |
| B4b | remaining `r=3` charts | public v5 family | no new independent packet here | generic and exceptional proof-code crosswalk; independent reproduction |
| B5 | primitive binary `r=4` | packet projective theorem | exact repeated-root, `3+1`, `2+2`, endpoint and second-normal checker | upstream Hilbert--Burch placement; specialist review; second CAS |
| B6 | primitive binary `r=5` | packet algebraic argument | exact supporting identities in the high-ramification checker | plane theorem; specialist review |
| B7 | fourth-power member | public edge proposition | locator only | overlap ownership |
| B8 | nonbinary fixed components | public valuation plus packet centralizer repair | prose lemma | verify preceding coefficient derivation; specialist review |
| B9 | zero minor | public edge proposition plus packet `R=0` proof | prose proof | plane theorem citation |

## Material not promoted by this packet

Earlier exploratory session notes reported additional work on a generic
`r=3` kernel-plane calculation and on a `tau=0` specialization.  No complete,
self-contained source-and-output artifact for those reports was retained in
the present packet.  They are therefore **not evidence in this submission**
and do not change row B4b.

## Remaining publication gates

Even if every candidate argument in this packet survives review, a public
global theorem still requires:

1. a line-by-line audit that every edge in this ownership tree matches the
   hypotheses of its cited source statement;
2. a proof-to-code crosswalk for the public quadratic-source, fixed-factor,
   and remaining degree-three charts;
3. independent reproduction of the remaining `r=3` generic and exceptional
   systems, preferably in a second computer-algebra system;
4. verification and exact citation of the Appelgate--Onishi/Nowicki--Nakai
   plane theorem in every function-field use; and
5. specialist review of the new structural, conic, rational-cubic,
   high-ramification, and `tau=-1` arguments.

Until those gates close, this is a candidate repaired synthesis rather than
an unconditional proof of `D_min &gt;= 5`.
</code></pre>

[Back to Lane 4](quartic-endgame.md)
