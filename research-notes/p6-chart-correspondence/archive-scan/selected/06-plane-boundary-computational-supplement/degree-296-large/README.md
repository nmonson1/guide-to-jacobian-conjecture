# Boundary Belyi / filtered-residue / degree-296 certificate package

This archive contains the revised manuscript and exact replay for the local
terminal no-gluing theorem.

## Decisive results

- filtered principal-part reconstruction through normal order 8;
- mixed volume `MV(A,B,C,C,C)=296`;
- all 344 proper toric faces exhausted;
- 270 faces rejected by a monomial initial form;
- the remaining 74 saturated Laurent initial ideals verified to be unit ideals;
- complete 296-dimensional reduced finite algebra over `F_2053`;
- coordinate multiplication matrices invertible;
- `det(m_rho)=682 mod 2053`;
- five split determinant residues `682,116,337,242,740` with product `51 mod 2053`;
- characteristic-zero finite-etale lifting and no common zero of the six exact polynomials.

The mathematical scope and imported dependencies are stated in
`THEOREM_AND_DEPENDENCIES.md`.

## Requirements

- Python 3.11 or later
- `sympy`, `numpy`, `scipy`
- a C++17 compiler
- optional: `latexmk`, `pdflatex`, and `bibtex` to rebuild the manuscript

## Replay

From the archive root:

```bash
./run_all.sh
```

The script writes fresh outputs below `generated/` and checks them against the
archived exact summaries where a byte-for-byte reference is available.

Expected decisive lines include:

```text
base_mixed_volume=296
certificate_passed=1
quotient_dimension=296
f4_rank=296 f4_determinant=682
characteristic_polynomial_degree=296 squarefree_gcd_degree=0
rational_field_norm_residue=51
proper_face_count=344
nontrivial_face_tests=74
face_tests=74 all_unit=1
```

## Manuscript

- Source: `manuscript/06-plane-boundary/main.tex`
- Built PDF: `manuscript/06-plane-boundary/main.pdf`
- New residue section: `manuscript/06-plane-boundary/sections/filtered-principal-parts.tex`
- New toric norm section: `manuscript/06-plane-boundary/sections/toric-norm.tex`
