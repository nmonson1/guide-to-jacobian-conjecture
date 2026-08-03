"""Fast exact Q[u]/(u^5-u^4+3u^3+3u^2+26) arithmetic.

Reconstructed from the public Lane 8 executable input.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import gcd
from typing import Iterable, Union

Scalar = Union[int, Fraction]
MOD_F = [Fraction(26), Fraction(0), Fraction(3), Fraction(3), Fraction(-1), Fraction(1)]


def _gcd_many(values):
    g = 0
    for v in values:
        g = gcd(g, abs(v))
        if g == 1:
            return 1
    return g


def _trim(p):
    while p and p[-1] == 0:
        p.pop()
    return p


def _padd(a, b):
    n = max(len(a), len(b))
    c = [Fraction(0)] * n
    for i in range(n):
        c[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return _trim(c)


def _psub(a, b):
    n = max(len(a), len(b))
    c = [Fraction(0)] * n
    for i in range(n):
        c[i] = (a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
    return _trim(c)


def _pmul(a, b):
    if not a or not b:
        return []
    c = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    c[i + j] += x * y
    return _trim(c)


def _pscale(s, a):
    return _trim([s * x for x in a]) if s else []


def _pdivmod(a, b):
    a = _trim(list(a))
    b = _trim(list(b))
    if not b:
        raise ZeroDivisionError
    if len(a) < len(b):
        return [], a
    q = [Fraction(0)] * (len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        d = len(a) - len(b)
        c = a[-1] / b[-1]
        q[d] += c
        for j, v in enumerate(b):
            a[d + j] -= c * v
        _trim(a)
    return _trim(q), a


def _xgcd(a, b):
    r0, r1 = _trim(list(a)), _trim(list(b))
    s0, s1 = [Fraction(1)], []
    t0, t1 = [], [Fraction(1)]
    while r1:
        q, r2 = _pdivmod(r0, r1)
        r0, r1 = r1, r2
        s0, s1 = s1, _psub(s0, _pmul(q, s1))
        t0, t1 = t1, _psub(t0, _pmul(q, t1))
    lead = r0[-1]
    return _pscale(1 / lead, r0), _pscale(1 / lead, s0), _pscale(1 / lead, t0)


def _as_frac(x: Scalar) -> Fraction:
    return x if isinstance(x, Fraction) else Fraction(x)


@dataclass(frozen=True, slots=True, init=False)
class K5:
    nums: tuple[int, int, int, int, int]
    den: int

    def __init__(self, coeffs: Iterable[Scalar] = (), den: int = 1):
        vals = list(coeffs)
        if den != 1:
            ns = [int(x) for x in vals]
            ns += [0] * (5 - len(ns))
            self._set(ns[:5], den)
            return
        fs = [_as_frac(x) for x in vals]
        fs += [Fraction(0)] * (5 - len(fs))
        if len(fs) > 5:
            raise ValueError
        d = 1
        for f in fs:
            d = d * f.denominator // gcd(d, f.denominator)
        ns = [f.numerator * (d // f.denominator) for f in fs]
        self._set(ns, d)

    def _set(self, ns, den):
        if den < 0:
            ns = [-x for x in ns]
            den = -den
        g = _gcd_many([den, *ns])
        if g:
            den //= g
            ns = [x // g for x in ns]
        object.__setattr__(self, "nums", tuple(ns))
        object.__setattr__(self, "den", den)

    @classmethod
    def raw(cls, ns, den=1):
        obj = object.__new__(cls)
        obj._set(list(ns), den)
        return obj

    @classmethod
    def coerce(cls, x):
        if isinstance(x, K5):
            return x
        f = _as_frac(x)
        return cls.raw([f.numerator, 0, 0, 0, 0], f.denominator)

    @property
    def coeffs(self):
        return tuple(Fraction(n, self.den) for n in self.nums)

    def __bool__(self):
        return any(self.nums)

    def __eq__(self, other):
        if isinstance(other, K5):
            return self.den == other.den and self.nums == other.nums
        if isinstance(other, (int, Fraction)):
            return self == K5.coerce(other)
        return False

    def __hash__(self):
        return hash((self.nums, self.den))

    def __neg__(self):
        return K5.raw([-x for x in self.nums], self.den)

    def __add__(self, other):
        other = K5.coerce(other)
        if not self:
            return other
        if not other:
            return self
        g = gcd(self.den, other.den)
        a = other.den // g
        b = self.den // g
        d = self.den * a
        return K5.raw([x * a + y * b for x, y in zip(self.nums, other.nums)], d)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-K5.coerce(other))

    def __rsub__(self, other):
        return K5.coerce(other) - self

    def __mul__(self, other):
        if isinstance(other, (int, Fraction)):
            f = _as_frac(other)
            if not f or not self:
                return K5()
            return K5.raw([x * f.numerator for x in self.nums], self.den * f.denominator)
        other = K5.coerce(other)
        if not self or not other:
            return K5()
        c = [0] * 9
        for i, a in enumerate(self.nums):
            if a:
                for j, b in enumerate(other.nums):
                    if b:
                        c[i + j] += a * b
        # u^5 = u^4 - 3u^3 - 3u^2 - 26.
        for d in range(8, 4, -1):
            v = c[d]
            if v:
                c[d - 1] += v
                c[d - 2] -= 3 * v
                c[d - 3] -= 3 * v
                c[d - 5] -= 26 * v
                c[d] = 0
        return K5.raw(c[:5], self.den * other.den)

    def __rmul__(self, other):
        return self * other

    @lru_cache(maxsize=None)
    def inverse(self):
        if not self:
            raise ZeroDivisionError
        a = [Fraction(n, self.den) for n in self.nums]
        a = _trim(a)
        g, s, _ = _xgcd(a, MOD_F)
        if g != [Fraction(1)]:
            raise ArithmeticError(g)
        _, rem = _pdivmod(s, MOD_F)
        rem += [Fraction(0)] * (5 - len(rem))
        return K5(rem[:5])

    def __truediv__(self, other):
        if isinstance(other, (int, Fraction)):
            f = _as_frac(other)
            if not f:
                raise ZeroDivisionError
            return K5.raw([x * f.denominator for x in self.nums], self.den * f.numerator)
        return self * K5.coerce(other).inverse()

    def __rtruediv__(self, other):
        return K5.coerce(other) * self.inverse()

    def __pow__(self, n):
        if n < 0:
            return self.inverse() ** (-n)
        out = K5([1])
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def __repr__(self):
        return f"K5(nums={self.nums},den={self.den})"


class KDomain:
    zero = K5()
    one = K5([1])
    unit = K5([0, 1])

    @staticmethod
    def convert(x):
        return K5.coerce(x)


K = KDomain()
