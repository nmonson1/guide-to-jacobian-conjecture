# Jacobian continuation bundle

This bundle continues the exact attacks on the 19-dimensional
cubic-homogeneous representative and the rank-five square-zero search.

Main results:

* ordinary vector-Waring lower bound for the fixed tensor: **52**;
* fixed full-rank square-zero pairing interval: **52 <= N <= 110**;
* a 13-term exact quartic obstruction functional;
* uniqueness of `P2=-d^2 e_a` among 605 scalar monomial triangular shifts;
* exact exclusion of the first three-row, one-edge-per-row, coordinate-collision class;
* corrected exhaustive F5 search over all nonzero edge coefficients.

Start with `CONTINUATION_REPORT.md`.

Verification:

```bash
./run_all.sh
```

The scripts use exact rational arithmetic.  `verify_small_certificates.py`
uses only Python's `fractions.Fraction` and JSON; it does not import SymPy.
The finite-field exhaustive stage requires a C++17 compiler.
