# Lane 2 PRS boundary research packet

> **Status:** unrefereed, AI-assisted research packet; exact symbolic replay
> supplied; no independent specialist review recorded. Nathaniel Monson
> remains responsible for every submitted assertion.

This directory contains the complete Lane 2 progress packet produced on
1–2 August 2026. The source bundle contains:

- 15 proof and corrective notes;
- 12 exact SymPy replay programs;
- 12 captured outputs, checked against fresh replay;
- an audit of public wording and scope boundaries;
- a machine-readable manifest and SHA-256 inventory; and
- a top-level runner that executes every replay and compares output
  byte-for-byte.

The archive is split into text parts because the repository connector used for
this draft cannot upload one binary blob. Reconstruct it with:

```bash
python assemble.py --extract
```

The reconstructed file must have SHA-256

```text
c77588de647cb2bfff5b9a080252144ea99e934c70b1eea9faafad5a91c424bf
```

and is named `lane2-prs-boundary-2026-08-02-v1.zip`.

## Mathematical contents

The packet includes self-contained proof drafts for the
principal-subresultant/Hankel/rectangular-Schur identity, the arbitrary-rank
block-reversal rank profile, and the resulting filtered Smith exponents. It
then develops the complete-PRS boundary in ranks three and four and the actual
`(m,nu)=(5,5)` quintic model, including ordered resolutions, saturated
multi-Rees equations, cubic-scroll normalization, finite normalization across
`T=0`, and the ordered/symmetric flop comparison.

## Scope fences

The packet does not claim a global arbitrary-rank log-smooth PRS atlas,
extension of the relative-Jacobian marking across every merge, equality with
an unrigidified orbit quotient, or intrinsic reconstruction of the affine
opening. The active generated-site release is deliberately unchanged by this
pull request; assimilation should follow mathematical review.
