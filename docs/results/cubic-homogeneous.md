---
title: "William Thompson (21 July 2026): a cubic-homogeneous counterexample in 24 variables"
description: "An explicit counterexample in the classical cubic-homogeneous normal form, with exact certificates."
---

# William Thompson (21 July 2026): a cubic-homogeneous counterexample in 24 variables

<p class="byline">Construction, certificate package, and verifier programs by
William Thompson</p>

## What is true and why

Classical reduction theorems made maps of the form \(X+H(X)\), with \(H\)
homogeneous cubic, central to the Jacobian conjecture. Thompson converted the
new counterexample into this strict normal form while keeping the result
explicit enough to check term by term.

## Precise result

There is an explicit polynomial map

\[
G(U)=U+H(U)\colon\mathbf Q^{24}\longrightarrow\mathbf Q^{24}
\]

such that every nonzero component of \(H\) is homogeneous of degree three,

\[
\det DG=1,
\]

and two displayed distinct rational points have the same image. The map has
54 nonzero cubic monomials.

## Discussion

The importance of the result is structural rather than dimensional. It
places a concrete counterexample inside the normal form used by the
Bass–Connell–Wright and Yagzhev reductions, so questions about nilpotent
Jacobian matrices, cubic-linear forms, and the neighboring Hessian
conjecture can be tested on an exact example.

Twenty-four is an upper bound supplied by this construction, not a proof of
minimality. Smaller cubic-homogeneous presentations are a separate problem.

## Sources and verification

- [Thompson's repository, pinned revision](https://github.com/wtho704/explicit-cubic-homogeneous-jacobian-counterexample/tree/45a7616fdf5a20c065564f2676190093722696b9)
- [Archived release on Zenodo](https://doi.org/10.5281/zenodo.21466221)
- [Bass–Connell–Wright, “The Jacobian conjecture: reduction of degree and formal expansion of the inverse”](https://doi.org/10.1090/S0273-0979-1982-15032-7)
