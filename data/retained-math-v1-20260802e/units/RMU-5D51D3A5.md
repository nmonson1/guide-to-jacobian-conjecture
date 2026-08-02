# Leading-image factorization

`RMU-5D51D3A5` · `lemma`

## Mathematical record

`RMU-5D51D3A5` · `lemma`

Suppose \(H_4\ne0\) and the image closure \(C_4(F)\) is a curve of
degree \(e\ge1\).  Then there are coprime forms \(A,B\) of a common
degree \(k\ge1\), binary forms \(h=(h_0,h_1,h_2)\) of degree \(e\)
with no common root giving a proper parametrization of \(C_4(F)\), and a
form \(G\), such that
\[
H_4=G\cdot h(A,B),\qquad \deg G+ek=4.
\]
The possible leaves with a nondegenerate image are
\[
(e,k,\deg G)\in\{(2,1,2),\ (2,2,0),\ (3,1,1),\ (4,1,0)\},
\]
and \(e=1\) is the leading-target-span-two locus.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

Let \(K\) be the relative algebraic closure of
\(\phi_4^*k(C_4(F))\) in \(k(\PP^2)\).  It has transcendence degree
one and is unirational, hence rational by L\"uroth: \(K=k(A/B)\) with
\(A,B\) coprime forms of a common degree \(k\).  The ratios
\(H_{4,i}/H_{4,j}\) lie in \(K\), so
\([H_{4,1}:H_{4,2}:H_{4,3}]=[h_0(A,B):h_1(A,B):h_2(A,B)]\) for binary
forms \(h_i\) without common root, and the induced map
\(\PP^1\to C_4(F)\) is birational because \(K\) is relatively
algebraically closed; hence the parametrization is proper and
\(e=\deg C_4(F)\).  The substituted forms \(h_i(A,B)\) have no common
factor: a common root of the \(h_i\) does not exist, so a common factor
would force the coprime pencil \((A,B)\) to have a base divisor.  Hence
\(G=\gcd(H_{4,1},H_{4,2},H_{4,3})\) satisfies
\(H_{4,i}=G\,h_i(A,B)\) up to one common scalar, and the degree
relation follows.

  - Full source and surrounding context: [`manuscripts/02-low-degree/main.tex#lem:leading-image`](../../proof-sources/02-low-degree/main.md#label-lem-leading-image)
