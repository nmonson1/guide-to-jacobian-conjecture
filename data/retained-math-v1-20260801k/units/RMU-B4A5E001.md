# Invariant ring at a transverse simple conic basepoint

`RMU-B4A5E001` · `lemma`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-B4A5E001` · `lemma`

Let k be a field of characteristic zero. Suppose p is a common zero of A and B such that dG(p), dA(p), and dB(p) are linearly independent. In etale local coordinates (g,a,b)=(G,A,B), let delta=-2g partial_g+a partial_a+b partial_b. Then k[g,a,b]^delta=k[ga^2,gab,gb^2], which is isomorphic to k[U,V,W]/(V^2-UW). In particular, a transverse simple basepoint contributes no additional local polynomial invariants beyond the three conic target coordinates.

Hypotheses:

- The ground field has characteristic zero.
- The point p is a common zero of A and B.
- The differentials dG(p), dA(p), and dB(p) are linearly independent, so (G,A,B) are etale local coordinates.

Support:

- **proof:** The source supplies a complete monomial-weight proof of the local invariant-ring identity. — Inline support is reproduced on the unit record.

A monomial g^k a^i b^j has delta-weight -2k+i+j, so it is invariant exactly when i+j=2k. Then i and j have the same parity. Let s in {0,1} be their common parity and put r=(i-s)/2 and t=(j-s)/2. Since k=r+s+t, one has g^k a^i b^j=(ga^2)^r(gab)^s(gb^2)^t. Hence ga^2, gab, and gb^2 generate the invariant ring. Their exponent vectors have the single primitive relation 2(1,1,1)=(1,2,0)+(1,0,2), so the corresponding semigroup algebra is k[U,V,W]/(V^2-UW).

  - Does not establish: A global degree-five fixed-factor exclusion.
  - Does not establish: Any statement about nontransverse or higher-length basepoints.

Limitations:

- This is a local invariant-ring calculation, not a global Keller exclusion.
- It does not cover nontransverse basepoints, higher scheme-theoretic intersection length, or global gluing into the determinant arc.

## Connections

- `related_to` `JCG-F299193A`: This local calculation narrows the retained open basepoint-boundary problem to nontransverse, higher-length, and global-gluing cases.

## Attribution

- Credit: ChatGPT research dialogue
