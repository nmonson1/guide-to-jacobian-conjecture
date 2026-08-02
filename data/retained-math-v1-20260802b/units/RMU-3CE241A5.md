# Stored terminal no-gluing theorem

`RMU-3CE241A5` · `theorem`

## Mathematical record

`RMU-3CE241A5` · `theorem`

After the canonical \(k=4\) rechart and the forced adjacent-chart
condition of \cref{prop:k4-chart-transition}, the complete
layer-five-through-seven support and chart-matching equations of the stored
degree-\(21\) terminal specialization have no common zero over the
algebraic closure of
\[
K_0=\mathbb Q[u]/(u^5-u^4+3u^3+3u^2+26).
\]

Dependencies:

- `uses` [`RMU-85A3EB1C`](../units/RMU-85A3EB1C.md): Formal statement references prop:k4-chart-transition.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

After the adjacent-chart linear equation is imposed, the layer-five
equation is affine-linear in one remaining coefficient \(d\):
\[
F_5=D(x)d+R(x,a,b).
\]
On \(D=0\), the specialized layer-five-through-seven equations have an
exact nineteen-term Nullstellensatz identity.

On \(D\ne0\), eliminating \(d\) reduces the problem to a five-generator
ideal \(J\subset K_0[x,a,b]\).  At the good prime
\((2053,u-216)\), integral points are excluded by a 201-term affine unit
certificate.  The common normal fan has \(93\) face patterns: \(61\) have a
monomial initial form, \(32\) require exact residue-torus tests, and the ten
surviving cones are covered by two explicit weighted charts.  Exact
identities in the \(x\)-dominant and \(a\)-dominant charts exclude those
cones.  Properness of the weighted compactification lifts emptiness from the
good fiber to characteristic zero.  An independent weighted-projective
implementation gives the same conclusion.

  - Full source and surrounding context: [`manuscripts/06-plane-boundary/appendices/degree-twenty-one-certificates.tex#thm:stored-terminal-layer-seven`](../../proof-sources/06-plane-boundary/appendices/degree-twenty-one-certificates.md#label-thm-stored-terminal-layer-seven)
