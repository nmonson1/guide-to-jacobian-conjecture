# One-sided high-weight noncommuting composition theorem

Let

```text
S=k[P,Q,R] subset B=k[x,y,z]
```

for the displayed Keller map, with source-torus weights

```text
wt(x)=-1,  wt(y)=1,  wt(z)=2.
```

Then `S` is graded, `P,Q,R` have weights `2,1,-1`, and `B_{<=6}` is supported
on `[-6,12]`.

## Abstract theorem

Let

```text
Phi = exp(c_m D_m) ... exp(c_1 D_1)
```

be an ordered composition of polynomial automorphisms, where every `c_i` is
nonzero and every `D_i` is a homogeneous locally nilpotent derivation of torus
weight `e_i`.

Assume either

```text
e_i >= 19 for every i
```

or

```text
e_i <= -19 for every i.
```

In the positive case let `e_0=min e_i`; in the negative case let
`e_0=max e_i`. Suppose the extremal weight occurs for exactly one derivation,
called `D_0`, and

```text
D_0(Q) notin S,       D_0(R) notin S.
```

Then

```text
Phi(S) intersect B_{<=6} = k.
```

The derivations need not commute and may change different coordinates.

## Proof

Take `g in Phi(S) intersect B_{<=6}` and write

```text
g=sum_{w=-6}^{12} g_w
```

in torus weights. Expanding `Phi^(-1)(g)` gives the zero-order terms `g_w`,
first-order terms `-c_i D_i(g_w)`, and finitely many higher words in the
`D_i`. The weight of a word is the input weight plus the sum of its derivation
weights.

If every shift is positive, every nonzero word has weight at least
`-6+19=13`; if every shift is negative, every nonzero word has weight at most
`12-19=-7`. Thus no derivative word can collide with a zero-order term.
Since `Phi^(-1)(g)` lies in the graded algebra `S`, every `g_w` lies in `S`.
The standard degree-six theorem gives

```text
g=a+bQ+dR.
```

Suppose the shifts are positive. If `d!=0`, the unique lowest derivative
weight is

```text
-1+e_0,
```

coming from `-d*c_0 D_0(R)`. Every other first-order term is higher and every
word of length at least two has shift at least `2e_0`. Hence `D_0(R)` would
belong to `S`, a contradiction. After `d=0`, a nonzero `b` similarly isolates
`D_0(Q)` at weight `1+e_0`.

For negative shifts, reverse highest and lowest. A nonzero `b` first isolates
`D_0(Q)` at the unique highest derivative weight `1+e_0`; after `b=0`, a
nonzero `d` isolates `D_0(R)` at `-1+e_0`. Again both are impossible.
Therefore `b=d=0` and `g` is constant.

## Elementary-monomial corollary

For an elementary derivation

```text
D=x_j^N partial_{x_i},
```

its weight is

```text
e=N*wt(x_j)-wt(x_i).
```

The exact common fiber

```text
(-12,1/11,-8/11),
(-10,1/11,-14/11),
(22,-1/22,65/484)
```

shows that `D(Q)` and `D(R)` are not in `S` for every coordinate direction
and every `N>=2`. Consequently the theorem applies to any finite ordered
composition of high-weight elementary monomial shears when:

1. all derivation weights have the same sign and absolute value at least 19;
2. the weight closest to zero occurs exactly once.

This includes many genuinely noncommuting compositions mixing different
coordinate directions. For example, positive-weight shears from the tails

```text
x -> x+f(y),    z -> z+g(y),
y -> y+h(z),    x -> x+k(z)
```

may be interleaved in any order, provided the smallest positive shift appears
once. The analogous statement holds for the two negative-weight `x`-based
directions.

## Repeated extremal weights

Uniqueness is only a convenient sufficient condition. If several derivations
have the extremal weight, put

```text
D_* = sum_{e_i=e_0} c_i D_i.
```

The same proof works whenever

```text
D_*(Q) notin S,       D_*(R) notin S.
```

This reduces repeated-weight compositions to a finite common-fiber linear
independence problem. It is the natural next extension.

## Boundary

The theorem does not cover compositions mixing positive and negative shifts,
low-weight derivations inside `[-18,18]`, or repeated extremal combinations
that become fiber-constant. These are now sharply isolated interaction cases.
