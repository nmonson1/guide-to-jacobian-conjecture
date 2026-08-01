# Computation index

The supplement follows the mathematical decomposition of the paper.

| Mathematical role | Directory | Main checks |
| --- | --- | --- |
| Fixed 19D tensor and descendants | `computational-supplement/fixed-tensor/` | collision, nilpotence, rank-seven compression, Jordan chain, 38D Hessian construction, and 110D square-zero pairing |
| Waring and compression continuation | `computational-supplement/continuation/` | 52-cube lower bound, quartic functional, monomial shifts, target cleanup, and small Fraction-only certificates |
| Public 11D input to 19D | `computational-supplement/verify_19d_from_11d.py` | direct transfer from the credited public input |
| Regular \(5\times5\) collision line | `computational-supplement/n5-regular-jordan/` | geometric regularity over \(\mathbb F_{11}\) and Hensel lifting |
| Global extension obstruction | `computational-supplement/n5-regular-continuation/` | first-normal equations and the required rank drop away from the line |
| Smaller focused checks | `code/` | compression-slice and structural-extension verifiers |
| Monolith and prolongation | `code/monolith-prolongation/` | affine Lie/Hankel data, \(18+1\) layer structure, symplectic exclusion, and principal-\(\mathfrak{sl}_2\) obstruction |

Each subdirectory contains its own report, manifest, and replay script where
applicable. Start with:

```bash
cd computational-supplement/fixed-tensor
bash run_all.sh
cd ../continuation
bash run_all.sh
```

The key conceptual separation is deliberate: the collision-line equations
have smooth characteristic-zero solutions, but those solutions cannot extend
to a globally nilpotent Jacobian without additional degeneracy in the normal
directions.

The three new minimal replays are:

```bash
uv run --with sympy==1.14.0 python code/monolith-prolongation/verify_affine_lie_hankel.py
uv run --with sympy==1.14.0 python code/monolith-prolongation/verify_prolongation_structure.py
uv run --with sympy==1.14.0 python code/monolith-prolongation/verify_sl2_collision_obstruction.py
```

The full 64-character source hashes are recorded by the version-7 tree
manifest.
