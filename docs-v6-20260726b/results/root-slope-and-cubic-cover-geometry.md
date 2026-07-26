---
title: "The Root-Slope Mechanism and Cubic Cover Geometry"
description: "For any polynomial potential H(T,c), the marked-root and slope equations b=r-H_T(t,c), 2a=H(t,c)+tb have Jacobian r/2; composing with t=y+1/x, r=2/x, c=w(x,y)-x^3z has Jacobian -2 whenever the formulas extend polynomially, and generic degree deg_T H."
---

# The Root-Slope Mechanism and Cubic Cover Geometry

<p class="dek">For any polynomial potential H(T,c), the marked-root and slope equations b=r-H_T(t,c), 2a=H(t,c)+tb have Jacobian r/2; composing with t=y+1/x, r=2/x, c=w(x,y)-x^3z has Jacobian -2 whenever the formulas extend polynomially, and generic degree deg_T H.</p>

<span class="status status-kind">Result</span> <span class="status status-draft">Working draft</span>

**Credited to dorky (derivation); Nathaniel Monson (research direction and mathematical responsibility).**

**Source coverage:** Public sources are linked below. The linked working manuscript has exact locations for every program-relevant defining claim on this page. This says where the claims are recorded, not that they have been independently verified.

## The central idea

The theorem-level package is centered on the following mechanism: For any polynomial potential H(T,c), the marked-root and slope equations b=r-H_T(t,c), 2a=H(t,c)+tb have Jacobian r/2; composing with t=y+1/x, r=2/x, c=w(x,y)-x^3z has Jacobian -2 whenever the formulas extend polynomially, and generic degree deg_T H.  Its supporting records isolate the ingredients that establish the statement and the qualifications that control its scope.

## For a first reading

Begin with the precise statement, then use the component statements as a map of the argument.  They separate the main assertion from proof ingredients, examples, qualifications, and corrections without requiring the reader to reconstruct the development from a claim ledger.

## Precise statement

For any polynomial potential H(T,c), the marked-root and slope equations b=r-H_T(t,c), 2a=H(t,c)+tb have Jacobian r/2; composing with t=y+1/x, r=2/x, c=w(x,y)-x^3z has Jacobian -2 whenever the formulas extend polynomially, and generic degree deg_T H.

## Proof idea and technical structure

### Universal Root Slope Identity: For any polynomial potential H(T,c), the marked-root and slope equations b=r-H_T(t,c), 2a=H(t…

For any polynomial potential H(T,c), the marked-root and slope equations b=r-H_T(t,c), 2a=H(t,c)+tb have Jacobian r/2; composing with t=y+1/x, r=2/x, c=w(x,y)-x^3z has Jacobian -2 whenever the formulas extend polynomially, and generic degree deg_T H.

*Defining · Primary Statement · recorded*

[Open the deeper technical record](../technical/universal-root-slope-identity-for-any-polynomial-potential-h-t-c-the-0106262f.md)

### Root Collision Escape Formula: On a sheet marked by a simple root t_i of a cubic, x_i=2/P'(t_i)=2/[A(c)(t_i-t_j)(t_i-t_k)];…

On a sheet marked by a simple root t_i of a cubic, x_i=2/P'(t_i)=2/[A(c)(t_i-t_j)(t_i-t_k)]; collision of the marked root therefore sends that affine source branch to infinity while the finite completion retains the ramification.

*Defining · Supporting Result · recorded*

[Open the deeper technical record](../technical/root-collision-escape-formula-on-a-sheet-marked-by-a-simple-root-ada71038.md)

### Normalized Family Monodromy: For every coprime normalized cubic-frame pair in the stated family, the inverse cubic is irre…

For every coprime normalized cubic-frame pair in the stated family, the inverse cubic is irreducible with nonsquare discriminant over C(a,b,c), so its generic Galois closure and geometric monodromy are S3.

*Defining · Supporting Result · proof offered*

[Open the deeper technical record](../technical/normalized-family-monodromy-for-every-coprime-normalized-cubic-frame-pair-in-the-504733cf.md)

### Discriminant Complement Topology: Over A(c) nonzero, the normalized cubic discriminant complement is the product of the punctur…

Over A(c) nonzero, the normalized cubic discriminant complement is the product of the punctured c-line and the centered three-point configuration space; if A has s distinct roots, its fundamental group is F_s times B_3 and the permutation monodromy is the standard B_3-to-S3 quotient.

*Defining · Supporting Result · recorded*

[Open the deeper technical record](../technical/discriminant-complement-topology-over-a-c-nonzero-the-normalized-cubic-discriminant-complement-8ef344e1.md)

### Family Deck Group Triviality: For every coprime admissible cubic-frame pair, the generic function-field extension has no no…

For every coprime admissible cubic-frame pair, the generic function-field extension has no nontrivial deck transformation; ordinary source automorphisms over the identity target are therefore trivial.

*Defining · Supporting Result · proof offered*

[Open the deeper technical record](../technical/family-deck-group-triviality-for-every-coprime-admissible-cubic-frame-pair-the-5b09e55b.md)

### Degree-three function-field extension with S3 Galois closure

The function-field extension induced by the Alpöge map has degree 3 and an S3 Galois closure, as described by the cited explicit cubic model.

*Shared · Supporting Result · proof offered*

[Open the deeper technical record](../technical/degree-three-function-field-extension-with-s3-galois-closure-1b137277.md)

## Manuscripts and external links

- [Cubic Marked-Root Covers](../assets/manuscripts/01-cubic-marked-root-covers-2026-07-22-v9.pdf) — Nathaniel Monson, 2026-07-22; working manuscript; the version-9 reader-and-register release records the current statement and evidence boundary for the claims placed here; SHA-256 `6f10fbcf7b3fb9c5e76624994c018b3f19eba6ffbdfaaf280dc872aa9dc49d06`
- [Results and Research Register for Six Jacobian-Conjecture Programs](../assets/manuscripts/07-results-and-research-register-2026-07-22-v9.pdf) — companion statement and evidence-boundary catalogue; SHA-256 `f905805fd5b27f1eaa1c0ac03449da0d0f6d90607250988be85e54e4621acda3`
- [Galois structure of the new counterexample to the Jacobian conjecture: an explicit cubic model with S3 monodromy — is this known? — dorky](https://mathoverflow.net/questions/513387/)

## Connects to

- [Base Cover Monodromy And Deck Group](base-cover-monodromy-and-deck-group.md)
- [Base Map Fibers Image And Nonproperness](base-map-fibers-image-and-nonproperness.md)
- [The Common Cover of the Descendant Ladder](common-cover-of-the-descendant-ladder.md)
- [Why the Double-Root Slice Is Affine Three-Space](double-root-affine-source.md)
- [Finite Triple Covers, Conductors, and Automorphisms](finite-triple-covers-conductors-and-automorphisms.md)
- [Uniqueness in the Multiplication-Incidence Construction](multiplication-incidence-uniqueness.md)

## Evidence, review, and detailed credit

**Evidence present:** computation, proof.

**Independent review:**

- None Recorded: No independent review is represented in this public record.

**Detailed credit:**

- dorky: derivation; documented authorship — Contribution recorded in Galois structure of the new counterexample.
- Nathaniel Monson: research direction and mathematical responsibility; attributed by source

**AI assistance:**

- ChatGPT: derivation and drafting; research assistance
- Responsible human(s): Nathaniel Monson

??? info "Registry details"
    Release state: `draft_public`

    Visibility: `catalogued`

    Source form: announcement, working manuscript

    Manuscript coverage: `complete`

    `complete` means that every program-relevant defining claim has an exact manuscript location. It does not mean independent proof review or machine verification.

    Grouped members: 6

    Canonical registry: v9

[Back to all results and open problems](../research.md)
