"""Independent exact symbolic checks for the explicit quotient covers.

Checks:
* the five displayed quotient face equations;
* identities (3.2) and (3.3);
* tangent-matrix ranks and one-dimensional source-scaling kernels.
"""
from __future__ import annotations

import sympy as sp

u = sp.symbols("u")


def face_expression(p, q, N: int, m: int, n: int):
    return sp.expand(N * p * q - m * u * p * sp.diff(q, u) + n * u * sp.diff(p, u) * q)


def tangent_matrix(p, q, N: int, m: int, n: int):
    degree_p = sp.degree(p, u)
    degree_q = sp.degree(q, u)
    a_coeffs = sp.symbols(f"a1:{degree_p + 1}")
    b_coeffs = sp.symbols(f"b1:{degree_q + 1}")
    alpha = sum(a_coeffs[i - 1] * u**i for i in range(1, degree_p + 1))
    beta = sum(b_coeffs[i - 1] * u**i for i in range(1, degree_q + 1))

    linearization = sp.Poly(
        sp.expand(
            N * (alpha * q + p * beta)
            - m * u * (alpha * sp.diff(q, u) + p * sp.diff(beta, u))
            + n * u * (sp.diff(alpha, u) * q + sp.diff(p, u) * beta)
        ),
        u,
    )
    variables = list(a_coeffs) + list(b_coeffs)
    # The natural target is the zero-constant polynomial space. Its basis is
    # u, ..., u^(deg p + deg q - 1).
    target_degree = degree_p + degree_q - 1
    matrix = sp.Matrix(
        [
            [sp.expand(linearization.coeff_monomial(u**power)).coeff(var) for var in variables]
            for power in range(1, target_degree + 1)
        ]
    )
    scaling_vector = sp.Matrix(
        [sp.expand(u * sp.diff(p, u)).coeff(u, i) for i in range(1, degree_p + 1)]
        + [sp.expand(u * sp.diff(q, u)).coeff(u, i) for i in range(1, degree_q + 1)]
    )
    return matrix, scaling_vector


def proportional(v, w) -> bool:
    return all(
        sp.simplify(v[i] * w[j] - v[j] * w[i]) == 0
        for i in range(len(v))
        for j in range(len(v))
    )


def main() -> None:
    sqrt6 = sp.sqrt(6)
    cases = []

    p = 1 - u
    q = sp.Rational(1, 5) - sp.Rational(3, 5) * u + sp.Rational(9, 25) * u**2
    cases.append(("F2", p, q, 1, 3, 5, sp.Rational(1, 5), 2, -sp.Rational(36, 5)))

    P = u**3 + u**2 + sp.Rational(5, 12) * u + sp.Rational(1, 18)
    Q = (
        u**5
        + sp.Rational(3, 2) * u**4
        + u**3
        + sp.Rational(1, 3) * u**2
        + sp.Rational(5, 96) * u
        + sp.Rational(1, 576)
    )
    cases.append(("one-step", 18 * P, 192 * Q, 1, 2, 3, sp.Rational(1, 3), 7, sp.Integer(2090188800)))

    p = 1 + sp.Rational(20, 3) * u + 24 * u**2 + sp.Rational(288, 7) * u**3 + sp.Rational(288, 7) * u**4
    q = sp.Rational(1, 2) + 5 * u + 12 * u**2 + 18 * u**3
    cases.append(("two-step", p, q, 1, 3, 2, sp.Rational(1, 2), 6, sp.Rational(37791360, 7)))

    for epsilon in (-1, 1):
        p = 1 + u + (sp.Rational(1, 3) + epsilon * sqrt6 / 18) * u**2
        q = (
            sp.Rational(1, 4)
            + sp.Rational(5, 8) * u
            + (sp.Rational(2, 5) + epsilon * sqrt6 / 40) * u**2
            + (sp.Rational(17, 160) + epsilon * 11 * sqrt6 / 480) * u**3
        )
        cases.append((f"F24 epsilon={epsilon}", p, q, 1, 3, 4, sp.Rational(1, 4), 4, sp.Rational(99, 20) + epsilon * sp.Rational(153, 40) * sqrt6))

    for name, p, q, N, m, n, rhs, expected_rank, expected_minor in cases:
        assert sp.simplify(face_expression(p, q, N, m, n) - rhs) == 0
        matrix, scaling = tangent_matrix(p, q, N, m, n)
        assert matrix.rank() == expected_rank
        assert sp.simplify(matrix[:, :matrix.rows].det() - expected_minor) == 0
        residual = (matrix * scaling).applyfunc(sp.simplify)
        assert all(entry == 0 for entry in residual)
        kernel = matrix.nullspace()
        assert len(kernel) == 1
        assert proportional(kernel[0], scaling)
        print(
            f"{name}: face identity OK; tangent matrix {matrix.rows}x{matrix.cols}, "
            f"rank {matrix.rank()}, listed maximal minor OK, kernel = source scaling"
        )

    P = u**3 + u**2 + sp.Rational(5, 12) * u + sp.Rational(1, 18)
    Q = (
        u**5
        + sp.Rational(3, 2) * u**4
        + u**3
        + sp.Rational(1, 3) * u**2
        + sp.Rational(5, 96) * u
        + sp.Rational(1, 576)
    )
    assert sp.expand(u * P**3 - Q**2 + (36 * u**2 + 28 * u + 9) / sp.Integer(2985984)) == 0

    P = u**4 + u**3 + sp.Rational(7, 12) * u**2 + sp.Rational(35, 216) * u + sp.Rational(7, 288)
    Q = u**3 + sp.Rational(2, 3) * u**2 + sp.Rational(5, 18) * u + sp.Rational(1, 36)
    assert sp.expand(u * P**2 - Q**3 + (72 * u**2 + 39 * u + 16) / sp.Integer(746496)) == 0
    print("Identities (3.2) and (3.3): OK")


if __name__ == "__main__":
    main()
