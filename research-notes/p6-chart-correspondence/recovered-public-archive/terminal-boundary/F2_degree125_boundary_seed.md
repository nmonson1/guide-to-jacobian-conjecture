# Boundary seed for the first post-125 complete-chain case

## Source data

The first family at maximum degree 125 in the complete-chain table is

\[
F_2:\qquad A_0=(5,20),\quad A_0'=(1,0),\quad A_1=(7/5,2),
\qquad (m,n)=(3,5).
\]

This note extracts the exact terminal-edge information that is available before a full Newton-support normalization.

## 1. Starting direction and fractional coordinate

The edge difference is

\[
A_0-A_0'=(4,20),
\]

so its primitive normal direction is

\[
(\rho,\sigma)=(5,-1).
\]

The standard fractional edge coordinate is therefore

\[
z=x^{-\sigma/\rho}y=x^{1/5}y.
\]

For the \(P\)-coordinate, the edge runs from

\[
mA_0'=(3,0)
\quad\text{to}\quad
mA_0=(15,60),
\]

so

\[
\ell_{5,-1}(P)=x^3p(z),\qquad \deg p=60,\qquad p(0)\ne0.
\]

For \(Q\), the corresponding edge runs from \((5,0)\) to \((25,100)\), hence

\[
\ell_{5,-1}(Q)=x^5q(z),\qquad \deg q=100.
\]

Because the original pair is polynomial in \(x,y\), only powers \(z^{5j}\) occur. Equivalently, with

\[
w=z^5=xy^5,
\]

one may write

\[
\ell_{5,-1}(P)=x^3\widetilde p(w),\quad \deg\widetilde p=12,
\]

\[
\ell_{5,-1}(Q)=x^5\widetilde q(w),\quad \deg\widetilde q=20.
\]

## 2. Common-power and double-root constraint

The standard leading-form theorem for an \((m,n)=(3,5)\) pair gives, up to nonzero scalars,

\[
p(z)=R(z)^3,\qquad q(z)=R(z)^5,
\qquad \deg R=20.
\]

In the integral coordinate \(w=z^5\), this becomes

\[
\widetilde p(w)=S(w)^3,\qquad
\widetilde q(w)=S(w)^5,
\qquad \deg S=4.
\]

The child-corner formula is

\[
A_1=A_0'+\frac{m_\lambda}{m}
\left(-\frac\sigma\rho,1\right).
\]

Substituting the table data gives

\[
(7/5,2)=(1,0)+\frac{m_\lambda}{3}(1/5,1),
\]

and therefore

\[
\boxed{m_\lambda=6.}
\]

Thus the chosen root has multiplicity six in \(p=R^3\), hence multiplicity two in \(R\). Since \(p(0)\ne0\), the root is nonzero. After the fractional shear

\[
y\longmapsto y+\lambda x^{-1/5},
\qquad z\longmapsto z+\lambda,
\]

we have

\[
R(z+\lambda)=z^2T(z),\qquad T(0)\ne0,
\]

and the new leading monomial of \(P\) is

\[
x^3z^6=x^{21/5}y^6.
\]

Dividing its exponent pair by \(m=3\) gives

\[
(7/5,2)=A_1,
\]

which independently verifies the chain transition.

## 3. What this fixes, and what it does not

The complete-chain data already force:

- the fractional scale \(l_1=5\);
- a quartic integral common-root polynomial \(S(w)\);
- a distinguished nonzero double root of \(S\);
- the first approximate-root shear;
- the child corner \((7/5,2)\).

They do **not** yet determine:

- the complete normalized Newton polygons after the shear;
- the monomial bracket exponent \(\kappa\) in the final toric chart;
- the adjacent-component pole scale \(a\);
- the higher normal-neighborhood line-bundle windows (the reduced primary Hurwitz problem is determined in Section 5);
- the secondary contact degree \(e\).

Once \((a,\kappa)\) are obtained, with common powers \((3,5)\), the universal contact formula gives

\[
\boxed{e=8a-\kappa-1.}
\]

If \(e>a^2\), the secondary cover is then forced by the universal transport theorem and has passport

\[
(a^a\,(e-a^2)),\qquad(e),\qquad(a+1\,1^{e-a-1}).
\]

## 4. Remaining support-normalization task

The reduced primary face can be determined without the entire support (Section 5). Full support propagation is still needed for the gluing problem:

1. propagate the fractional shear through the full standard rectangle;
2. use the terminal-corner inequalities and the gap-five congruence to discard forbidden lattice points;
3. choose the adjacent toric ray and return to the quotient coordinate \(u=z^5\);
4. enumerate the finite normal-layer windows;
5. compute \(a\), \(\kappa\), the secondary contact data, and the two-point line-bundle spaces.

This is the first meaningful test of whether the degree-21 gluing mechanism is a terminal-chain mechanism rather than a special feature of the \((8,28)\) support.

## 5. Subsequent terminal-face determination and lattice quotient

The type-I.b final-corner formulas give

\[
A_1=(7/5,2),\quad k=1,\quad(m,n)=(3,5),
\]

\[
(\rho,\sigma)=(25,-17),\qquad z=x^{17/25}y,
\]

\[
P_E=x^{4/5}y\,p(z),\quad\deg p=5,
\qquad
Q_E=x^{1/5}q(z),\quad\deg q=10,
\]

and

\[
5pq-3zpq'+5zp'q=1.
\tag{5.1}
\]

The fractional uniformizing cover has degree 30 and passport

\[
(5^6),(3^{10}),(15,1^{15}).
\]

That ambient passport has eleven connected dessin classes.  However, the complete-chain lattice gap is

\[
g=\operatorname{gap}(25,5)=5.
\]

Polynomial support therefore forces

\[
p(z)=\bar p(z^5),\qquad q(z)=\bar q(z^5).
\]

With \(u=z^5\), equation (5.1) becomes

\[
\bar p\bar q-3u\bar p\bar q'+5u\bar p'\bar q=\frac15,
\]

with

\[
\deg\bar p=1,\qquad\deg\bar q=2.
\]

The lattice-compatible quotient passport is

\[
\boxed{(5,1),(3^2),(3,1^3),}
\]

of degree six.  Its connected Hurwitz count is one, and its deck group is trivial.  A normalized representative is

\[
\bar p=1-u,
\qquad
\bar q=\frac15-\frac35u+\frac9{25}u^2,
\]

so, up to target scaling,

\[
\boxed{
\phi_6(u)=\frac{u(u-1)^5}{(u^2-\frac53u+\frac59)^3}.
}
\]

The degree-30 ambient face is the cyclic pullback \(\phi_6(z^5)\).  Thus only the unique \(C_5\)-symmetric one among the eleven ambient dessins is compatible with the polynomial lattice.

## 6. Revised next exact computation

The reduced terminal map is now completely fixed.  The next calculation is not an eleven-case degree-30 search.  It is one \(C_5\)-equivariant normal-neighborhood computation around the explicit degree-six map above:

1. propagate the full Newton support through the complete chain into the quotient coordinate \(u=z^5\);
2. determine the allowed two-point line-bundle windows for the normal coefficients;
3. form the intrinsic determinant layer operators and their pole-filtered residue adjoints;
4. compute the boundary Kuranishi section;
5. prove either no gluing or a strict complete-chain descent.

See `terminal_primary_belyi_reduction.md` and `verify_post125_terminal_examples.py`.
