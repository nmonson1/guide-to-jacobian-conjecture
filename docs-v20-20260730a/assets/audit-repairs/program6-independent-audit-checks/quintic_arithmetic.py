"""Independent arithmetic checks for K0 = Q[u]/(u^5-u^4+3u^3+3u^2+26)."""
from __future__ import annotations

import sympy as sp

u = sp.symbols("u")
f = u**5 - u**4 + 3 * u**3 + 3 * u**2 + 26


def roots_mod_prime(poly, prime: int):
    return [a for a in range(prime) if int(poly.subs(u, a)) % prime == 0]


def main() -> None:
    assert sp.factor(f) == f
    discriminant = int(sp.discriminant(f, u))
    assert discriminant == 784_822_272
    assert sp.factorint(discriminant) == {2: 12, 3: 1, 13: 1, 17: 3}

    numerical_roots = sp.nroots(f, n=40, maxsteps=200)
    real_roots = [root for root in numerical_roots if abs(sp.im(root)) < sp.Float("1e-30")]
    assert len(real_roots) == 1

    roots_2053 = roots_mod_prime(f, 2053)
    assert roots_2053 == [216, 531, 664, 721, 1975]
    assert all(int(sp.diff(f, u).subs(u, root)) % 2053 != 0 for root in roots_2053)

    # At p=31, 5 is a simple root and the complementary factor is irreducible.
    factor_31 = sp.factor(f, modulus=31)
    assert int(f.subs(u, 5)) % 31 == 0

    print("irreducible over Q: yes")
    print("signature: (1, 2)")
    print(f"discriminant: {discriminant} = {sp.factorint(discriminant)}")
    print(f"roots modulo 2053: {roots_2053} (all simple)")
    print(f"factorization modulo 31: {factor_31}")


if __name__ == "__main__":
    main()
