# Parameter-complete `F_2` attachment recurrence

**Status:** exact finite-dimensional criterion and executable contract.  The
actual order-`510/520/530` endpoint matrices remain absent from the public
packet, so this note does not report a numerical global-attachment verdict.

## 1. The intrinsic finite-order system

Fix all lower orders.  At normal order `r`, collect the unknown left endpoint
correction, right endpoint correction, overlap correction, and every fresh
order-`r` parameter into

```text
X_r=(x_r^L,x_r^R,o_r,p_r).
```

Concatenate:

1. the two endpoint determinant equations;
2. the overlap/normalization equations;
3. the coefficients outside both finite Newton windows;
4. any presentation and cyclic-descent equations.

The complete order-`r` problem is one exact affine system

```text
M_r X_r=b_r.                                  (1.1)
```

All nonlinear dependence on lower orders is already evaluated in `b_r` and
in any known coefficients of `M_r`.  Thus, once the real blocks are supplied,
finite-order attachment is an exact rational linear-algebra problem.

## 2. Fresh parameters change the obstruction space

Write the full matrix as

```text
M_r=[C_r | P_r],                              (2.1)
```

where `C_r` contains endpoint and overlap correction columns and `P_r`
contains every fresh-parameter column.  The parameter-zero slice tests only

```text
C_r x_r=b_r.                                  (2.2)
```

The two obstruction spaces are

```text
O_full = ker(M_r^T),
O_slice= ker(C_r^T).                           (2.3)
```

They satisfy the exact identity

```text
O_full=ker(C_r^T) intersect ker(P_r^T).        (2.4)
```

Consequently a left-null vector of `C_r` is an intrinsic obstruction
functional only when it also annihilates every fresh-parameter column.
Equivalently,

```text
b_r in im(C_r)+im(P_r)                        (2.5)
```

is the full compatibility criterion, whereas `b_r in im(C_r)` is merely the
chosen zero-parameter slice.

### Proposition 2.1 — slice-dependent apparent obstruction

Suppose `ell^T C_r=0` and `ell^T b_r` is nonzero.  This proves inconsistency of
(2.2).  It proves inconsistency of (1.1) only if `ell^T P_r=0` as well.
If `ell^T P_r` is nonzero, the condition can be cancelled by a fresh
parameter and is not gauge- or chart-independent.

This is the exact linear-algebra reason that a nonzero order-`530` value
computed after setting new parameters to zero cannot be promoted to a global
obstruction.

## 3. `C_5` descent

After equivariant decomposition,

```text
M_r = direct-sum_(chi in Z/5) M_(r,chi),
b_r = direct-sum_(chi in Z/5) b_(r,chi).      (3.1)
```

The full system is feasible exactly when each character block is feasible.
Every variable in a preassembled block must have the block character; known
products of lower-order variables and wall parameters must be moved into the
correct character component before export.

For the `k=4` wall parameter, the parameter character is `4 mod 5`, and a
`q`-th wall term shifts coefficient character by `-4q`.  A scalar invariant
wall effect first returns at wall order five.  This bookkeeping applies to
all correction and support equations, not only to invariant face
coefficients.

## 4. Finite polynomial support

Polynomiality adds rows to (1.1): every coefficient outside the allowed left
or right Newton window is set to zero.  There is no separate infinite
argument at a fixed truncation.  Once the ordered support blocks are supplied,
the exact feasibility calculation is finite.

The support rows must be formed after transporting the entire overlap datum:
coefficient vector, equation density, fixed-presentation operation columns,
rechart columns, fresh parameters, and residue-dual functionals.  Truncating a
transported Laurent vector by itself does not define a chart overlap.

## 5. Executable contract

`lane9_f2_attachment_recurrence.py` reads a rational JSON contract with:

- a cyclic modulus;
- normal orders;
- character blocks;
- named variables and their kinds;
- named equations;
- the exact matrix and right-hand side.

For every block it reports:

```text
rank(M), rank([M|b]), consistency,
solution dimension, left nullity,
nonzero left-null obstruction certificates,
```

and repeats the calculation after deleting all fresh-parameter columns.  A
block is marked `slice_dependent_apparent_obstruction` precisely when the
full system is consistent but the zero-parameter slice is not.

The included contract

```text
synthetic_f2_parameter_retention_contract.json
```

is explicitly synthetic.  It is a regression fixture demonstrating at orders
`510`, `520`, and `530` how fresh columns remove conditions visible on the
zero-parameter slice.  It is not evidence about the numerical `F_2`
recurrence.

## 6. Data required for the real replay

A real contract must publish, for both endpoints and every relevant order:

1. ordered correction bases and determinant matrices;
2. ordered finite support windows and outside-window rows;
3. overlap and complete-chain normalization matrices;
4. all fresh parameters, first occurrence orders, and `C_5` characters;
5. the lower-order forcing vector in the same equation basis;
6. an archive manifest and hashes sufficient to reproduce the export.

The hash-pinned public Program 6 ZIP contains the terminal face, the degree-30
coefficient recurrence, and related Hurwitz data.  The deterministic Lane 9
scan found no small UTF-8 member matching an order-`510/520/530`,
fresh-parameter, or `F_2` matrix/support-block endpoint packet.  The checker
therefore refuses to synthesize a numerical order-`530` verdict.

## 7. Reproduction

```bash
cd research-notes/p6-chart-correspondence

python -m unittest -v test_lane9_f2_attachment_recurrence.py

python lane9_f2_attachment_recurrence.py \
  synthetic_f2_parameter_retention_contract.json \
  --output /tmp/synthetic-f2-parameter-retention-report.json
```

GPT-5.6 Pro assisted with the theorem formulation, exact implementation, and
regression design.  This note is unrefereed; the actual endpoint export must
be reviewed independently before any global claim is made.
