---
title: "About"
description: "Scope, methodology, attribution, AI assistance, review language, sources, and ways to improve the guide."
---

# About This Guide

<p class="dek">A living, source-linked reading guide—not a journal, a proof
assistant, or a claim that the fast-moving post-counterexample literature has
already settled.</p>

## Scope

The guide covers mathematical results and open problems made newly relevant
by the Jacobian-conjecture counterexample. It is not an encyclopedia of the
entire subject. The reader-facing layer consists of six overview sections,
six working research programs, 74 theorem-level result pages, and 20
open-problem pages.

Deeper technical records preserve the smaller statements from which those
pages are assembled. They are intentionally absent from navigation and search.
Raw conversations, private research ledgers, unsanitized code, and working
source trees are not published here.

## How a page is assembled

Each ordinary result page keeps distinct questions distinct:

<div class="method-grid">
  <div>
    <h3>What is claimed?</h3>
    <p>A self-contained description, precise statement, proof idea, and supporting components.</p>
  </div>
  <div>
    <h3>Where did it come from?</h3>
    <p>Public sources are recorded separately as announcements, manuscripts, preprints, repositories, or refereed publications.</p>
  </div>
  <div>
    <h3>Who receives credit?</h3>
    <p>Credit is role-specific: problem suggestion, discovery, proof, exposition, computation, formalization, or another documented contribution.</p>
  </div>
  <div>
    <h3>What evidence exists?</h3>
    <p>Proofs, computations, formalizations, direct checks, and citations are listed without collapsing them into one confidence score.</p>
  </div>
</div>

The public pages are generated deterministically from a sanitized publication
layer pinned to canonical registry version 9. Human-written exposition may
override any generated section. The exporter refuses to overwrite an earlier
run, records file hashes, and rejects private filesystem paths, private
conversation locators, share links, and internal record identifiers.

## What the labels mean

`Established public record` means the result was already present in an
external public source selected for the guide. It does not mean the guide has
independently reproved the result.

`Working draft` means the page may be read publicly but belongs to current,
unrefereed research. Release state is separate from mathematical evidence,
source form, and independent review.

`Machine check` always has a stated scope. A Lean proof of the displayed
determinant and collision does not machine-check every geometric consequence
or every claim in a linked manuscript.

## Review and uncertainty

The baseline for this working draft is AI-assisted mathematical development
with human mathematical review at varying depth. That is weaker than peer
review, independent reproduction, or formal verification. Some exact
calculations have stronger evidence, and the page says so; many research
claims do not.

The practical expectation should be that the site contains mistakes. A strong
model may regard a statement as very likely and a human mathematician may have
read it without either fact turning the statement into an independently
verified theorem. Readers should use the source, evidence, and review fields
rather than infer reliability from polish.

## Attribution and AI assistance

`Source` answers where the guide encountered a statement, proof, exposition,
formalization, or check. `Credited to` answers who is assigned a mathematical
or documentary role and why. The two may differ.

For the counterexample, the guide gives the source-reported chain prominently:
Akhil Mathew suggested the problem to Levent Alpöge; Alpöge put it to Fable;
Fable produced the work leading to the example; Alpöge announced the resulting
map. Later proof, exposition, and formalization receive their own credits.

AI assistance is structured rather than stored as a vague note. The guide
records the system, role, purpose, and responsible human when that information
is available. AI systems are not silently folded into human credit and are not
treated as responsible authors.

## Sources

The fastest starting points are:

- [The announced map and technical note](https://www.ulam.ai/research/jacobian.pdf)
- [Terence Tao's geometric digestion](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
- [David Speyer's Secret Blogging Seminar discussion](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)
- [Formal Conjectures PR 4474](https://github.com/google-deepmind/formal-conjectures/pull/4474)
- [The complete Research catalogue](research.md)

The result pages link more narrowly to MathOverflow discussions, code,
formalizations, manuscripts, and earlier literature.

## Improve a source or attribution

Before the guide is announced, errors can be corrected directly. A durable
public corrections ledger will begin only when readers are deliberately
invited to use the site.

- [Suggest a source or attribution improvement](https://github.com/nmonson1/guide-to-jacobian-conjecture/issues/new?template=source.yml)
- [Open a general contribution issue](https://github.com/nmonson1/guide-to-jacobian-conjecture/issues/new)
- [Read the contribution guide](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/main/CONTRIBUTING.md)

## Discoverability

This is an accessible public working draft, not a private preview. Every
rendered page currently carries `noindex, nofollow`, and `robots.txt` asks
crawlers not to index the site. Those measures reduce accidental discovery;
they are not access control.
