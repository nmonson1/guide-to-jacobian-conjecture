# Independent checks for Program 6, paper v13

These scripts reproduce only the small, hand-auditable computations used in the audit:

- exact Frobenius/Murnaghan--Nakayama Hurwitz counts for the five table rows, the degree-21 passport, and the ambient degree-30 weighted count;
- exact substitution checks for the five explicit quotient face equations and identities (3.2), (3.3);
- exact tangent ranks and the source-scaling kernels in Proposition 3.3, using the natural zero-constant target space;
- basic arithmetic of the displayed quintic coefficient field.

They do **not** replay the paper's large terminal certificate archive, reconstruct the degree-21 Belyi maps, verify the 7,121-by-7,121 Macaulay minor, or check the toric/weighted-projective certificates in Appendix C.

Run with:

```bash
python -m pip install -r requirements.txt
python hurwitz_counts.py
python explicit_symbolic_checks.py
python quintic_arithmetic.py
```
