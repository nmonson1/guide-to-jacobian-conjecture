#!/usr/bin/env python3
"""Independent Fraction-based verifier for the small certificates.

This file does not import SymPy and does not reconstruct the maps.  It
independently checks the serialized sparse rational matrices, determinants,
ranks, isotropic-block zeros, q_* membership, and quartic obstruction circuit.
"""
from __future__ import annotations
from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
D = json.loads((ROOT / "small_certificates.json").read_text())

def Q(s):
    return Fraction(s)

def dense(obj):
    M = [[Fraction(0) for _ in range(obj["cols"])] for _ in range(obj["rows"])]
    for i, j, c in obj["entries"]:
        M[i][j] = Q(c)
    return M

def rank(A):
    M = [row[:] for row in A]
    if not M:
        return 0
    m, n = len(M), len(M[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if M[i][c]), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        u = M[r][c]
        M[r] = [x/u for x in M[r]]
        for i in range(m):
            if i != r and M[i][c]:
                a = M[i][c]
                M[i] = [x-a*y for x, y in zip(M[i], M[r])]
        r += 1
        if r == m:
            break
    return r

def det(A):
    M = [row[:] for row in A]
    n = len(M)
    assert all(len(row) == n for row in M)
    ans = Fraction(1)
    for c in range(n):
        p = next((i for i in range(c, n) if M[i][c]), None)
        if p is None:
            return Fraction(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            ans = -ans
        u = M[c][c]
        ans *= u
        for i in range(c+1, n):
            if M[i][c]:
                a = M[i][c]/u
                for j in range(c, n):
                    M[i][j] -= a*M[c][j]
    return ans

def hstack(A, b):
    return [row + [b[i][0]] for i, row in enumerate(A)]

W = dense(D["derivative_W"])
assert rank(W) == D["W_rank"] == 39
assert det(dense(D["W_minor"])) == Q(D["W_minor_det"]) == 648

# Pair order is (i,j), 0<=i<=j<19.
pairs = [(i, j) for i in range(19) for j in range(i, 19)]
AA = {tuple(p) for p in D["W_AA_column_pairs"]}
for j, pair in enumerate(pairs):
    if pair in AA:
        assert all(row[j] == 0 for row in W)

K = dense(D["constant_kernel_matrix"])
assert rank(K) == 19
assert det(dense(D["constant_kernel_minor"])) == Q(D["constant_kernel_minor_det"]) == 18

# Reconstruct q_* as a linear combination of derivative rows.
qvec = [Fraction(0) for _ in range(190)]
for i, c in D["qstar_coeffs_in_W"]:
    cc = Q(c)
    for j in range(190):
        qvec[j] += cc*W[i][j]

S = [[Fraction(0) for _ in range(19)] for _ in range(19)]
for coeff, (i, j) in zip(qvec, pairs):
    if i == j:
        S[i][i] = coeff
    else:
        S[i][j] = S[j][i] = coeff/2
assert rank(S) == 13
I = D["qstar_symmetric_minor_indices"]
Sm = [[S[i][j] for j in I] for i in I]
assert Sm == dense(D["qstar_symmetric_minor"])
assert det(Sm) == Q(D["qstar_symmetric_minor_det"]) == Fraction(-1, 256)

R = dense(D["quartic_restricted_operator"])
dv = dense(D["quartic_D4_vector"])
assert rank(R) == 12
assert rank(hstack(R, dv)) == 13
lam = [Q(x) for x in D["quartic_lambda"]]
for j in range(len(R[0])):
    assert sum(lam[i]*R[i][j] for i in range(13)) == 0
assert sum(lam[i]*dv[i][0] for i in range(13)) == 1
for omitted in range(13):
    assert rank([row for i, row in enumerate(R) if i != omitted]) == 12


AT = dense(D["stabilizer_system"])
EB = dense(D["stabilizer_basis"])
assert rank(AT) == D["stabilizer_rank"] == 82
assert rank(EB) == D["stabilizer_dimension"] == 62
# AT*EB=0.
for i in range(len(AT)):
    for j in range(len(EB[0])):
        assert sum(AT[i][k]*EB[k][j] for k in range(144)) == 0

N = dense(D["commuting_nilpotent_N"])
assert any(any(row) for row in N)
def mmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
assert mmul(N, N) == [[Fraction(0) for _ in range(12)] for _ in range(12)]
for j in range(62):
    flat = [EB[i][j] for i in range(144)]
    T = [flat[12*i:12*(i+1)] for i in range(12)]
    assert mmul(T, N) == mmul(N, T)

print("[ok] custom Fraction verifier: W rank/minor and 12D zero block")
print("[ok] custom Fraction verifier: no constant JH kernel and q_* rank 13")
print("[ok] custom Fraction verifier: 13-row quartic circuit and Lambda(D4)=1")
print("[ok] custom Fraction verifier: 62D stabilizer and commuting square-zero element")
