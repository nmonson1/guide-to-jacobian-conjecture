---
title: "What does infinity remember?"
description: "The boundary-and-globalization front: discriminants, valuations, Newton faces, dessins, and local-to-global reconstruction."
---

# What does infinity remember?

<p class="dek">A noninvertible Keller map cannot fail at a finite critical
point. Its failure must be encoded by the boundary through which sheets
escape.</p>

!!! info "Entry route"
    Read [discriminants](../ideas/discriminants.md), then
    [Newton--Puiseux expansions](../ideas/newton-puiseux.md) and
    [dessins d'enfants](../ideas/dessins.md).

## The running example

In the marked-cubic map, the finite cover ramifies along the discriminant.
The affine source deletes the repeated marked roots, so the same locus becomes
a nonproperness boundary rather than a critical-value locus. The
normalization of that discriminant and the way it meets other boundary
components retain geometric information that survives coordinate changes and
stabilization.

This suggests a general principle:

> The boundary is not bookkeeping added after the affine map is understood.
> It is where global noninvertibility is stored.

## Established landmarks

### Boundary geometry can carry stable moduli

In a concrete family of three-sheeted maps, a parameter can be recovered from
how a normalized singular discriminant component meets a distinguished plane
at infinity. That parameter survives arbitrary stabilization by unused
coordinates.

[Read the stable cubic-frame classification](../results/stable-cubic-frames.md)

### Newton data compress the plane problem

For a hypothetical plane counterexample, escaping branches determine
valuations and Newton--Puiseux expansions. Their leading faces severely
restrict the possible supports of the coordinate polynomials. The published
below-125 reduction ultimately leaves two explicit support configurations.

[Read the plane case](../background/plane-case.md)

### Some leading faces become finite Hurwitz problems

For the last supports below 125, the leading-face equation forces a degree-21
Belyi map. The associated passport has exactly five connected dessins. This
turns an infinite-looking coefficient problem into five exact boundary
models.

[Read the five boundary covers](../results/degree-21-dessins.md)

### Terminal exclusion and global reduction are separate obligations

An external announcement reports that an exact computation eliminates the
two full supports below 125. The published global reduction and the terminal
calculation play different roles; neither can silently substitute for the
other.

[Read the announced degree bound](../results/below-125.md)

## Open questions

1. **Completeness of boundary data.** Which finite collection of normalized
   branches, conductors, residues, and overlap maps determines an affine
   opening?
2. **Local-to-global attachment.** When compatible formal solutions on
   separate charts exist, what obstruction prevents them from gluing to one
   polynomial map?
3. **Coordinate independence.** Which Newton or Rees constructions compute an
   intrinsic invariant rather than an artifact of one compactification?
4. **The degree-125 frontier.** What are the actual components of the first
   surviving formal systems, and which of them are reachable from a global
   plane Keller map?

## Common logical traps

- A valid leading face need not extend to a complete Puiseux branch.
- A complete formal branch need not algebraize to a global polynomial map.
- A terminal certificate excludes only the branch rigorously routed to its
  input system.
- Equivalent valuations can look different in different boundary charts.

## A useful target

The ideal result would state a finite package of boundary data, prove a
reconstruction or obstruction theorem, and identify exactly where affineness
and polynomiality enter the argument.

**State reviewed through:** 7 August 2026.
