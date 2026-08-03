#!/usr/bin/env python3
"""Exact arithmetic checks for the F2, maximum-degree-125 complete-chain seed."""
from fractions import Fraction
from math import gcd

A0 = (Fraction(5), Fraction(20))
A0p = (Fraction(1), Fraction(0))
A1 = (Fraction(7, 5), Fraction(2))
m, n = 3, 5

# Primitive normal to the edge A0-A0'.
dx = A0[0] - A0p[0]
dy = A0[1] - A0p[1]
g = gcd(dx.numerator, dy.numerator)
rho = dy / g
sigma = -dx / g
assert (rho, sigma) == (5, -1)

# Degrees in z=x^(1/5)y.
p_degree = m * (A0[1] - A0p[1])
q_degree = n * (A0[1] - A0p[1])
assert p_degree == 60 and q_degree == 100
assert p_degree % m == 0 and q_degree % n == 0
R_degree = p_degree / m
assert R_degree == 20
assert R_degree % 5 == 0
S_degree = R_degree / 5
assert S_degree == 4

# Child formula A1=A0' + (m_lambda/m)(-sigma/rho,1).
mult_ratio = A1[1] - A0p[1]
m_lambda = m * mult_ratio
assert m_lambda == 6
computed_A1 = (
    A0p[0] + mult_ratio * Fraction(-sigma, rho),
    A0p[1] + mult_ratio,
)
assert computed_A1 == A1

# After shifting a double root of R to zero, P has x^3 z^6.
new_x_exp = Fraction(3) + Fraction(6, 5)
new_y_exp = Fraction(6)
assert (new_x_exp / m, new_y_exp / m) == A1

print("F2 edge direction:", (rho, sigma))
print("degrees in z:", p_degree, q_degree, "common R degree:", R_degree)
print("integral common-root polynomial S(x y^5) degree:", S_degree)
print("chosen p-root multiplicity:", m_lambda, "=> double root of R/S")
print("child corner verified:", computed_A1)
print("all exact F2 seed checks passed")
