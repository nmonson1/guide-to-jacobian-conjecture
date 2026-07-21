---
title: Contribute
description: Submit English mathematical exposition, corrections, certificates, sources, and optional Lean formalizations.
---

# Contribute to the guide

This project is intended to supply the layer currently missing from the public
record: a reviewable English-language mathematical artifact. You do not need to
know Lean to contribute.

<div class="contribution-grid" markdown>

<div markdown>
### English mathematics
Clarify a proof, correct hypotheses, improve an explanation, or add a carefully scoped consequence.
</div>

<div markdown>
### Sources and review
Add a primary reference, report a conflict, check attribution, or audit historical priority.
</div>

<div markdown>
### Exact certificates
Contribute reproducible symbolic computation, independent implementations, hashes, and expected output.
</div>

<div markdown>
### Formalization
Link a Lean development, align an English claim with its formal statement, or add machine-checked geometry.
</div>

</div>

## The unit of review is a claim

A mathematical pull request should make it possible for a reviewer to answer:

1. **What exactly is asserted?** Include all hypotheses and conventions.
2. **Why should we believe it?** Link a proof, primary source, exact
   certificate, or formalization.
3. **What is the evidence status?** Use the labels from the
   [status page](status.md).
4. **Where does it stop?** State the boundary of the conclusion.
5. **Who did what?** Credit the idea, proof, implementation, checking, and
   review separately where appropriate.

## Ways in

- [Propose a mathematical claim or open question](https://github.com/nmonson1/guide-to-jacobian-conjecture/issues/new?template=claim.yml)
- [Report a correction](https://github.com/nmonson1/guide-to-jacobian-conjecture/issues/new?template=correction.yml)
- [Improve a source](https://github.com/nmonson1/guide-to-jacobian-conjecture/issues/new?template=source.yml)
- [Open the repository](https://github.com/nmonson1/guide-to-jacobian-conjecture)

Every page also has an edit button. Substantial changes should begin with an
issue so parallel work can be coordinated.

## Editorial rules

- Do not turn a successful exact computation into a broader theorem without a
  proof of the implication.
- Do not call an observation new without an appropriate literature and
  priority search.
- Preserve corrections and failed approaches when they materially constrain
  future work.
- Prefer primary sources to news coverage or secondhand summaries.
- Identify AI assistance and the independent checks applied to its output.
- Keep the two-dimensional problem distinct from results obtained by
  stabilization in dimensions three and higher.

The repository’s [full contribution instructions](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/main/CONTRIBUTING.md)
describe the pull-request checklist and local build commands.

