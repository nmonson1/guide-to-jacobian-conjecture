---
title: The geometry
description: How simple roots of a binary cubic encode the fibers and the escape of sheets at infinity.
---

# A cubic controls every fiber

Write ((p,q,r)) for target coordinates and form the binary cubic

\[
\Phi_{p,q,r}(S,T)=2pS^3-qS^2T+2ST^2-rT^3.
\]

The key geometric fact is that a source point over ((p,q,r)) corresponds to a
**simple projective root** ([S:T]\in\mathbb P^1) of this cubic. For the
explicit map, the root attached to ((x,y,z)) is

\[
[S:T]=[x:1+xy].
\]

Conversely, every simple root reconstructs one affine source point by explicit
rational formulas whose denominators are nonzero precisely at simple roots.

## The fiber count

<div class="fiber-grid" markdown>

<div class="fiber-card" markdown>
<span class="fiber-count">3</span>
### Distinct roots
Off the discriminant, the cubic has three simple roots and the map has three preimages.
</div>

<div class="fiber-card" markdown>
<span class="fiber-count">1</span>
### One double root
On the discriminant away from the triple-root curve, only the simple root remains affine.
</div>

<div class="fiber-card" markdown>
<span class="fiber-count">0</span>
### One triple root
On the special curve, there is no simple root and therefore no affine preimage.
</div>

</div>

The discriminant used in the public verification note is

\[
\Delta(p,q,r)=q^2-16p-q^3r+18pqr-27p^2r^2.
\]

Thus the generic degree is three. The map is a finite étale three-sheeted cover
away from (V(\Delta)), but it is not globally finite or proper.

## Escape, not collision at a critical point

On a generic point of (V(\Delta)), two roots merge in the projective cubic.
Those two affine inverse branches escape to infinity; the third branch remains
finite and nonsingular. On the triple-root curve

\[
\Gamma=V(12p-q^2,\,3qr-4),
\]

the last finite branch also disappears. Consequently,

\[
F(\mathbb C^3)=\mathbb C^3\setminus\Gamma.
\]

The nonproperness set is the hypersurface (V(\Delta)), while the set actually
omitted from the image is only the codimension-two curve (\Gamma).

## Four notions worth keeping separate

| Notion | In this example |
| --- | --- |
| Affine critical locus | Empty, because \\(\det JF=-2\\). |
| Branching of the finite completion | Supported on the cubic discriminant. |
| Nonproperness set | The hypersurface \\(V(\Delta)\\). |
| Omitted locus | The triple-root curve \\(\Gamma\\). |

Confusing these notions makes the example seem paradoxical. Once the finite
projective-root cover is separated from its affine simple-root open, the
mechanism is concrete: local inverses do not fail; inverse sheets leave the
affine chart.

!!! info "Primary source"
    The full incidence isomorphism, inverse formulas, fiber classification,
    image, and nonproperness calculation appear in [*A Counterexample to the
    Jacobian Conjecture*](https://www.ulam.ai/research/jacobian.pdf), Sections
    3–4. Independent computational accounts are listed under
    [sources](resources.md).

