# Lattice-gap reduction of terminal type-I.b boundary covers

**Working research note — 22 July 2026.** This note records an exact reduction obtained from the final-corner formulas for standard plane Keller pairs after replacing the fractional boundary parameter by the lattice quotient forced by the complete-chain gap. The result is a finite Hurwitz problem of substantially smaller degree than the ambient uniformizing cover. It does not prove that any listed boundary map extends to a Keller pair.

## 1. Final face equation on the fractional uniformizing line

Let a final regular corner of type I.b have

\[
A=\left(\frac a\ell,b\right),\qquad
\operatorname{st}(Q)=\left(\frac k\ell,0\right),\qquad
\operatorname{st}(P)=\left(1-\frac k\ell,1\right),
\]

with a standard coprime degree ratio \((m,n)\), in the orientation of equation (3.17) of Guccione--Guccione--Horruitiner--Valqui. Then

\[
\operatorname{en}(P)=mA,\qquad \operatorname{en}(Q)=nA,
\]

and

\[
\frac{\sigma}{\rho}=\frac{k-na}{n\ell b}.
\]

Put

\[
r=-\frac\sigma\rho=\frac{na-k}{n\ell b},\qquad z=x^r y.
\]

The terminal faces have the forms

\[
P_E=x^{1-k/\ell}y\,p(z),\qquad \deg p=mb-1,
\]

\[
Q_E=x^{k/\ell}q(z),\qquad \deg q=nb.
\]

For

\[
P=x^Ay^Bp(z),\qquad Q=x^Cy^Dq(z),\qquad z=x^ry,
\]

a direct differentiation gives

\[
[P,Q]=x^{A+C-1}y^{B+D-1}
\left((AD-BC)pq+(A-Br)zpq'+(rD-C)zp'q\right).
\]

The final-corner relation

\[
(m+n)bk-n(b\ell-a)=k
\]

reduces the three coefficients to a common scalar multiple of \((n,-m,n)\). After a nonzero target normalization,

\[
\boxed{npq-mzpq'+nzp'q=1.}
\tag{1.1}
\]

Therefore

\[
\tau(z)=z^n\frac{p(z)^n}{q(z)^m},
\qquad
\boxed{\tau'(z)=z^{n-1}\frac{p(z)^{n-1}}{q(z)^{m+1}}.}
\tag{1.2}
\]

If one forgets the lattice of the polynomial pair, this is a degree-\(mnb\) Belyi map with passport

\[
(n^{mb}),\qquad(m^{nb}),\qquad
\bigl((m+n)b-1,1^{mnb-(m+n)b+1}\bigr).
\tag{1.3}
\]

We call (1.3) the **ambient uniformizing passport**.

## 2. The lattice-gap quotient

Let

\[
g=\operatorname{gap}(\rho,\ell)=\frac{\rho}{\gcd(\rho,\ell)}.
\]

The complete-chain lattice theorem forces both face polynomials to use only powers of \(z^g\):

\[
p(z)=\bar p(u),\qquad q(z)=\bar q(u),\qquad u=z^g.
\tag{2.1}
\]

Consequently

\[
g\mid mb-1,\qquad g\mid nb.
\]

Since \(g\mid mb-1\), one has \(\gcd(g,b)=1\); hence \(g\mid n\). Set

\[
N=\frac ng,\qquad
A_0=\frac{mb-1}{g},\qquad
B_0=\frac{nb}{g}.
\]

Substitution into (1.1), followed by division by \(g\), gives the quotient equation

\[
\boxed{
N\bar p\bar q-mu\bar p\bar q'
+nu\bar p'\bar q=\frac1g.
}
\tag{2.2}
\]

Define

\[
\boxed{
\bar\tau(u)=u^N\frac{\bar p(u)^n}{\bar q(u)^m}.
}
\tag{2.3}
\]

Then

\[
\boxed{
\bar\tau'(u)=\frac1g\,
 u^{N-1}\frac{\bar p(u)^{n-1}}{\bar q(u)^{m+1}}.
}
\tag{2.4}
\]

Put

\[
D=\frac{mnb}{g},\qquad
H=\frac{(m+n)b-1}{g}.
\]

The actual lattice-compatible boundary cover has degree \(D\) and passport

\[
\boxed{
(n^{A_0},N),\qquad
(m^{B_0}),\qquad
(H,1^{D-H}).
}
\tag{2.5}
\]

Repeated parts are combined in the usual partition notation. The ambient map factors as

\[
\tau(z)=\bar\tau(z^g).
\]

Thus the degree-\(mnb\) cover is a cyclic \(g\)-pullback; the finite Hurwitz problem relevant to a polynomial complete-chain corner is the smaller degree-\(D\) problem (2.5).

### Connectedness

Every permutation triple with passport (2.5) is transitive. Indeed, an orbit not containing the unique \(H\)-cycle is fixed by the third permutation, so on that orbit the first two permutations are mutual inverses. Their cycle lengths would therefore have to agree. The ordinary cycles have lengths \(n\) and \(m\), which are coprime and greater than one. The only exceptional first-cycle length is \(N\mid n\); equality \(N=m\) would force \(m\mid n\), again impossible. Hence no second orbit exists.

## 3. The first five boundary problems

Exact Murnaghan--Nakayama character calculations give the following connected Hurwitz counts. In each listed quotient passport, the first partition has a unique fixed sheet. A deck transformation centralizing a transitive monodromy group is semiregular on the sheets, so that fixed sheet forces the deck group to be trivial. The weighted count is therefore the ordinary number of dessin classes.

| Case | \((m,n,b;k)\) | \(g\) | Ambient degree | Lattice quotient passport | Quotient degree | Classes |
|---|---:|---:|---:|---|---:|---:|
| \(F_2\), max degree 125 | \((3,5,2;1)\) | 5 | 30 | \((5,1),(3^2),(3,1^3)\) | 6 | 1 |
| one-step max 126 | \((2,3,5;2)\) | 3 | 30 | \((3^3,1),(2^5),(8,1^2)\) | 10 | 1 |
| two-step max 126 | \((3,2,3;1)\) | 2 | 18 | \((2^4,1),(3^3),(7,1^2)\) | 9 | 1 |
| \(F_{24}\), max 128 | \((3,4,3;1)\) | 4 | 36 | \((4^2,1),(3^3),(5,1^4)\) | 9 | 2 |
| one-step max 132 | \((2,3,8;1)\) | 3 | 48 | \((3^5,1),(2^8),(13,1^3)\) | 16 | 2 |

The first four rows have explicit quotient maps below.

## 4. The \(F_2\) correction: one relevant map, not eleven

For

\[
A=(7/5,2),\qquad k=1,\qquad(m,n)=(3,5),
\]

one has

\[
(\rho,\sigma)=(25,-17),\qquad g=5,
\]

and the ambient equation

\[
5pq-3zpq'+5zp'q=1,
\qquad \deg(p,q)=(5,10).
\]

The ambient degree-30 passport

\[
(5^6),(3^{10}),(15,1^{15})
\]

has eleven connected dessin classes: eight asymmetric, two with deck group \(C_3\), and one with deck group \(C_5\). This is an exact count, but it is **not** the polynomial complete-chain count.

The gap condition requires \(p,q\in K[z^5]\), so only the unique \(C_5\)-symmetric class survives. On \(u=z^5\),

\[
\bar p(u)=1-u,
\qquad
\bar q(u)=\frac15-\frac35u+\frac9{25}u^2,
\tag{4.1}
\]

and

\[
\bar p\bar q-3u\bar p\bar q'+5u\bar p'\bar q=\frac15.
\]

The unique quotient Belyi map is, up to target scaling,

\[
\boxed{
\phi_6(u)=
\frac{u(u-1)^5}{(u^2-\frac53u+\frac59)^3}.
}
\tag{4.2}
\]

The ambient terminal map is \(\phi_6(z^5)\). Therefore the reduced boundary datum for the first degree-125 complete-chain family is unique up to the standard source and target normalizations.

## 5. Explicit maps for the first post-125 rows

### 5.1 One-step maximum degree 126

Here

\[
A=(19/7,5),\quad k=2,\quad(m,n)=(2,3),
\quad(\rho,\sigma)=(21,-11),\quad g=3.
\]

The quotient passport is

\[
(3^3,1),(2^5),(8,1^2),
\]

and it has one class. Put

\[
P=u^3+u^2+\frac5{12}u+\frac1{18},
\]

\[
Q=u^5+\frac32u^4+u^3+\frac13u^2+\frac5{96}u+\frac1{576}.
\]

Then

\[
\boxed{uP^3-Q^2=-\frac{36u^2+28u+9}{2985984}.}
\tag{5.1}
\]

With \(\bar p=18P\) and \(\bar q=192Q\), equation (2.2) is

\[
\bar p\bar q-2u\bar p\bar q'+3u\bar p'\bar q=\frac13.
\]

The ambient face is obtained by \(u=z^3\).

### 5.2 Two-step maximum degree 126

Here

\[
A=(11/6,3),\quad k=1,\quad(m,n)=(3,2),
\quad(\rho,\sigma)=(12,-7),\quad g=2.
\]

The quotient passport

\[
(2^4,1),(3^3),(7,1^2)
\]

has one class. A normalized pair is

\[
\bar p=1+\frac{20}{3}u+24u^2+\frac{288}{7}u^3+\frac{288}{7}u^4,
\]

\[
\bar q=\frac12+5u+12u^2+18u^3,
\]

satisfying

\[
\bar p\bar q-3u\bar p\bar q'+2u\bar p'\bar q=\frac12.
\]

Equivalently, for

\[
P=u^4+u^3+\frac7{12}u^2+\frac{35}{216}u+\frac7{288},
\]

\[
Q=u^3+\frac23u^2+\frac5{18}u+\frac1{36},
\]

one has

\[
\boxed{uP^2-Q^3=-\frac{72u^2+39u+16}{746496}.}
\tag{5.2}
\]

The ambient face is obtained by \(u=z^2\).

### 5.3 Family \(F_{24}\), maximum degree 128

Here

\[
A=(19/8,3),\quad k=1,\quad(m,n)=(3,4),
\quad(\rho,\sigma)=(32,-25),\quad g=4.
\]

The quotient passport

\[
(4^2,1),(3^3),(5,1^4)
\]

has exactly two classes, conjugate over \(\mathbf Q(\sqrt6)\). With \(\varepsilon=\pm1\), set

\[
\bar p_\varepsilon
=1+u+\left(\frac13+\varepsilon\frac{\sqrt6}{18}\right)u^2,
\]

\[
\bar q_\varepsilon
=\frac14+\frac58u
+\left(\frac25+\varepsilon\frac{\sqrt6}{40}\right)u^2
+\left(\frac{17}{160}+\varepsilon\frac{11\sqrt6}{480}\right)u^3.
\]

They satisfy

\[
\bar p\bar q-3u\bar p\bar q'+4u\bar p'\bar q=\frac14.
\]

The ambient faces are obtained by \(u=z^4\).


## 6. Reduced-cover infinitesimal rigidity

Fix the constant terms of a quotient solution and write

\[
\bar p=p_0+\sum_{i=1}^{A}a_i u^i,
\qquad
\bar q=q_0+\sum_{j=1}^{B}b_j u^j.
\]

The differential of

\[
\mathcal F(\bar p,\bar q)
=N\bar p\bar q-mu\bar p\bar q'+nu\bar p'\bar q
\]

at a solution is

\[
\mathscr L(\alpha,\beta)
=N(\alpha\bar q+\bar p\beta)
-mu(\alpha\bar q'+\bar p\beta')
+nu(\alpha'\bar q+\bar p'\beta).
\tag{6.1}
\]

The infinitesimal source rescaling \(u\mapsto(1+\varepsilon)u\) gives

\[
(\alpha,\beta)=(u\bar p',u\bar q')\in\ker\mathscr L.
\tag{6.2}
\]

Exact coefficient matrices give:

| quotient map | \((A,B)\) | domain dimension | target dimension | rank | kernel |
|---|---:|---:|---:|---:|---|
| \(F_2\), max 125 | \((1,2)\) | 3 | 2 | 2 | source scaling |
| one-step max 126 | \((3,5)\) | 8 | 7 | 7 | source scaling |
| two-step max 126 | \((4,3)\) | 7 | 6 | 6 | source scaling |
| \(F_{24}\), minus | \((2,3)\) | 5 | 4 | 4 | source scaling |
| \(F_{24}\), plus | \((2,3)\) | 5 | 4 | 4 | source scaling |

The nonzero maximal minors produced by the verifier are respectively

\[
-\frac{36}{5},\qquad
2090188800,\qquad
\frac{37791360}{7},\qquad
\frac{99}{20}\mp\frac{153\sqrt6}{40}.
\]

Hence, after quotienting by source scaling, each explicit reduced terminal map is a reduced isolated point of its coefficient scheme.  The terminal-primary Hurwitz problem contributes no hidden infinitesimal modulus in these cases.  Any surviving flexibility must occur in the normal-neighborhood coefficients and their global residue gluing, not in a deformation of the reduced Belyi cover itself.

This is a coefficient-level statement.  It does not yet prove that the complete Newton-bounded boundary-gluing functor is an etale product of the reduced-cover point with the normal-jet Kuranishi problem; establishing that functorial splitting remains part of the global program.

## 7. Consequence for the gluing--descent program

The lattice correction changes the next computational problem materially:

- the degree-125 family \(F_2\) no longer requires eleven boundary Kuranishi calculations;
- it requires one calculation around the explicit degree-six quotient map (4.2), with the \(C_5\)-equivariant normal windows inherited from the polynomial lattice;
- the next two degree-126 chains likewise have unique quotient maps of degrees ten and nine;
- the first branching occurs at \(F_{24}\), with only two conjugate degree-nine maps.

The next exact geometric task is therefore finite and sharply specified:

1. propagate the complete-chain Newton polygons into the \(u=z^g\) quotient chart;
2. compute the two-point line-bundle windows for every normal layer;
3. construct the intrinsic operators \(\mathscr D_r\), their pole-filtered adjoints, and the Kuranishi forcing classes;
4. test whether the resulting gluing scheme is empty or whether vanishing high-pole residues produce a strict complete-chain descent.

The reduction in this note does not establish the gluing obstruction for these cases. It removes the unnecessary cyclic pullback and leaves a small, exact list of reduced boundary maps on which the universal residue machinery can be tested.

## Reproducibility

- `terminal_primary_belyi.py` verifies the final-corner equation, primitive direction, gap divisibility, quotient equation, derivative, passports, and the explicit \(F_2\) map.
- `count_F2_terminal_dessins.py` computes the eleven ambient classes and verifies that exactly one is the lattice-compatible \(C_5\) pullback.
- `verify_post125_terminal_examples.py` verifies all five quotient passports and Hurwitz counts, together with the explicit maps in Sections 4 and 5.
- `post125_terminal_passports.json` contains the exact machine-readable output.
- `terminal_face_rigidity.py` verifies the exact tangent ranks, scaling kernels, and nonzero maximal minors in Section 6.
