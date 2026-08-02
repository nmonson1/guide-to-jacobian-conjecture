# Conditional five-variable terminal unit-ideal certificate

`RMU-ED13585F` · `theorem`

## Mathematical record

`RMU-ED13585F` · `theorem`

Suppose replay of the archived Macaulay data confirms that its \(7{,}121\)
rows are the complete ordered target monomial basis, that this basis contains
\(1\), and that the certified \(7{,}121\)-by-\(7{,}121\) minor uses every
target row.  Then, for the stored normalized full-support system, the six
selected obstruction equations generate the unit ideal over \(K_0\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

For the six selected polynomials \(F_i\), let \(V_i\) be the recorded
multiplier spaces and let \(W\) be the recorded target monomial space.  The
Macaulay map
\[
\mu:\bigoplus_{i=1}^6V_i\longrightarrow W,
\qquad (H_i)_i\longmapsto\sum_i H_iF_i
\]
has \(10{,}824\) columns.  The certificate must verify that its
\(7{,}121\) rows are the complete ordered basis of \(W\), that this basis
contains the constant monomial \(1\), and that the selected
\(7{,}121\)-by-\(7{,}121\) minor uses every target row.  Subject to those
three replay conditions, reduction at a good prime and at the selected
quintic embedding gives
\[
\det=859\pmod{2053}.
\]
The determinant is therefore nonzero in characteristic zero and \(\mu\) is
surjective, so \(1\in(F_1,\ldots,F_6)\).  If the recorded rows are only a
subset of a larger target basis, the minor proves only a rank statement and
does not prove the conclusion.  The certificate package regenerates all
fifteen exact equations, rebuilds the matrix, and replays the fixed pivot
minor; confirming the three target-basis conditions is an explicit audit
obligation.

  - Full source and surrounding context: [`manuscripts/06-plane-boundary/appendices/degree-twenty-one-certificates.tex#thm:terminal-unit`](../../proof-sources/06-plane-boundary/appendices/degree-twenty-one-certificates.md#label-thm-terminal-unit)
