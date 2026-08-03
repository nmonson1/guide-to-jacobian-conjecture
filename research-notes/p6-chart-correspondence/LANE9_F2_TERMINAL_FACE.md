# Exact `F_2` terminal quotient face

**Status:** exact low-order reconstruction.  This is not the missing
order-`510/520/530` two-endpoint recurrence packet.

The first degree-`125` complete-chain family has lattice gap `5`.  Its
fractional terminal coordinate therefore descends through

```text
u=z^5.
```

Writing the quotient face as

```text
pbar=a+b*u,
qbar=c+d*u+e*u^2,
```

the terminal bracket equation is

```text
pbar*qbar-3*u*pbar*qbar'+5*u*pbar'*qbar=1/5.  (1)
```

Coefficient comparison in (1) gives

```text
a*c=1/5,
a*d=3*b*c,
5*a*e=3*b*d.                                  (2)
```

Up to the ordinary nonzero scaling of the face, take `a=1`, `b=-1`.
Then (2) gives the unique normalized quotient face

```text
pbar=1-u,
qbar=(9*u^2-15*u+5)/25.                       (3)
```

The associated normalized secondary map is

```text
tau(u)=729*u*(u-1)^5/(9*u^2-15*u+5)^3.       (4)
```

Direct differentiation gives

```text
tau'(u)=-3645*(u-1)^4/(9*u^2-15*u+5)^4.      (5)
```

The fibers are therefore:

- over `0`: a point of ramification index `5` and one unramified point;
- over infinity: two points of ramification index `3`;
- over `1`: the three roots of
  `135*u^3-405*u^2+396*u-125`, together with infinity of ramification
  index `3`.

Thus (4) has degree `6` and passport

```text
(5,1), (3,3), (3,1,1,1).                     (6)
```

The standard-library checker `lane9_f2_terminal_face.py` verifies (1)--(6)
exactly over `Q` and writes `lane9_f2_terminal_face.json` in CI.

## What this reconstructs

This supplies a real, exact `F_2` face object rather than a placeholder:

- the quotient coordinate and lattice gap;
- the normalized terminal face coefficients;
- the quotient ODE;
- the degree-six Belyi map, derivative, and passport.

## What it does not reconstruct

The public packet still needs separate ordered data for a high-order global
attachment replay:

- the two endpoint layer matrices and their bases;
- the endpoint support blocks through and beyond order `530`;
- every fresh parameter and its `C_5` character;
- the overlap and complete-chain normalization matrices.

No entry in (3)--(6) determines those higher normal-neighborhood objects.
They must be recovered from a source packet or rebuilt from the full
normalized Newton polygons; they are not inferred from the terminal Belyi
map alone.

## Reproduction

```bash
python research-notes/p6-chart-correspondence/lane9_f2_terminal_face.py \
  --output /tmp/lane9-f2-terminal-face.json

cd research-notes/p6-chart-correspondence
python -m unittest -v test_lane9_f2_terminal_face.py
```

GPT-5.6 Pro assisted with the reconstruction and exact-check implementation.
The note is unrefereed and should be checked before manuscript integration.
