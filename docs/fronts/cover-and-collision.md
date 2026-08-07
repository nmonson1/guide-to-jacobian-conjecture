---
title: "Front I: intrinsic cover and collision geometry"
description: "From the affine formula to the finite cover, monodromy, and collision algebra."
---

# Front I: intrinsic cover and collision geometry

!!! info "For researchers"
    Start with [covers and monodromy](../ideas/monodromy.md) and
    [normalization](../ideas/normalization.md) if the terminology is new.

The displayed counterexample is a polynomial map, but its central mechanism
is a finite three-sheeted cover with part of its ramification boundary
removed. This front asks which features of that picture are intrinsic.

## The story so far

The function-field extension determines a finite normalization of the
target. Over a regular value, its points are the sheets of the map;
monodromy records how those sheets permute. Fiber products record collisions:
the off-diagonal part of \(X\times_YX\) parametrizes pairs of distinct source
points with the same image.

For the fixed cubic opening, these objects can be calculated explicitly. The
generic monodromy is \(S_3\), and the diagonal can be split from the
collision algebra by a canonical idempotent. Near a triple-root point, the
three boundary functions generate the square of the maximal ideal. That
small local model is the source of several flatness and defect calculations.

## The main open question

Can one recognize an affine Keller opening from intrinsic finite-cover data?
Knowing the abstract cover is not enough: one must also recover which
boundary was deleted and why the remaining open is affine space. A useful
answer should work without choosing the binary-cubic coordinates that made
the first example visible.

## Places to enter

- [Covers and monodromy](../ideas/monodromy.md)
- [Normalization](../ideas/normalization.md)
- [The marked-root construction](../background/marked-root-geometry.md)
- [Keller maps of every generic degree](../results/every-generic-degree.md)

The concrete target is an intrinsic recognition theorem: finite-cover and
boundary data that are both necessary and sufficient for an affine Keller
opening, tested on at least one family beyond the original coordinates.
