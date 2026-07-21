---
title: Status of claims
description: An evidence ledger separating formal proofs, exact certificates, public sources, review, and open problems.
---

# Status of claims

The public record is unusually fast-moving. This guide labels the kind of
support behind a statement rather than collapsing everything into “proved” or
“unproved.” Labels describe evidence, not historical priority.

## Evidence labels

<div class="label-list" markdown>

<div markdown><span class="status status-formalized">FORMALIZED</span> Checked by the Lean kernel in a cited public development.</div>
<div markdown><span class="status status-exact">EXACT CERTIFICATE</span> Reduced to finite exact arithmetic or polynomial identities with reproducible code.</div>
<div markdown><span class="status status-public">PUBLIC SOURCE</span> Stated and supported in a cited public mathematical source; not necessarily journal-reviewed.</div>
<div markdown><span class="status status-classical">CLASSICAL</span> A pre-2026 theorem or standard construction with a literature citation.</div>
<div markdown><span class="status status-review">UNDER REVIEW</span> Publicly proposed or submitted, but still awaiting mathematical or repository review.</div>
<div markdown><span class="status status-open">OPEN</span> No proof or counterexample is recorded here.</div>

</div>

## Core ledger

| Claim | Evidence | Boundary |
| --- | --- | --- |
| The displayed map has \\(\det JF=-2\\). | <span class="status status-formalized">FORMALIZED</span> <span class="status status-exact">EXACT</span> | A finite polynomial identity. |
| Three displayed rational points have image \\((-1/4,0,0)\\). | <span class="status status-formalized">FORMALIZED</span> <span class="status status-exact">EXACT</span> | This establishes noninjectivity. |
| The Jacobian conjecture is false in dimensions \\(n\ge3\\). | <span class="status status-public">PUBLIC SOURCE</span> | Dimension three plus stabilization; it says nothing downward about dimension two. |
| The plane Jacobian conjecture remains open. | <span class="status status-open">OPEN</span> | The three-variable construction does not descend automatically. |
| The explicit map has generic degree three and fiber sizes \\(3,1,0\\). | <span class="status status-public">PUBLIC SOURCE</span> <span class="status status-exact">EXACT</span> | Depends on the simple-projective-root description of the displayed binary cubic. |
| Its image is \\(\mathbb C^3\setminus\Gamma\\), while its nonproperness set is \\(V(\Delta)\\). | <span class="status status-public">PUBLIC SOURCE</span> <span class="status status-exact">EXACT</span> | Specific to this map; not a classification of all Keller maps. |
| Counterexamples of every generic degree at least three can be constructed in dimension three. | <span class="status status-public">PUBLIC SOURCE</span> | Public constructions exist; literature priority comparisons are still young. |
| Formal statements for Poisson and Dixmier consequences are being added to Formal Conjectures. | <span class="status status-review">UNDER REVIEW</span> | The relevant pull requests were open on 21 July 2026. |

## What a machine check does—and does not—supply

An exact symbolic script can prove the identity it encodes. It does not by
itself establish that every surrounding geometric interpretation is correct,
that a proposed generalization has complete hypotheses, or that an observation
is new. Lean can certify a formal statement and proof, but human review is still
needed to confirm that the statement faithfully expresses the intended
mathematics.

The [formalization page](formalization.md) links the current Lean artifacts. The
[contribution guide](contribute.md) explains how to propose corrections or add
claims without overstating their evidence.

