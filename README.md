# The Jacobian Conjecture: A Living Guide

Source repository for the public working draft at
<https://nmonson1.github.io/guide-to-jacobian-conjecture/>.

The site is accessible but deliberately unannounced. Every rendered page
currently carries `noindex, nofollow`, and `robots.txt` asks crawlers not to
index the site. Those measures reduce discoverability; they do not provide
privacy.

## Public structure

The candidate guide has five top-level reader paths:

1. Start;
2. Understand — the counterexample, its geometry, and the plane case;
3. Results — highlights, the complete collection index, open problems, and
   corrections;
4. Research — current state, six programs, and seven papers; and
5. Evidence — claim-level proof access and technical materials.

The active local release candidate contains:

- 85 result collections and 19 open-problem collections;
- 368 stable-tagged atomic claim pages, all included in site search but kept
  out of the main navigation;
- 534 many-to-many claim memberships across six research programs;
- 564 retained working-mathematics units, 544 supplied support objects, and
  48 typed relations across six overlapping program views;
- six version-13 reader PDFs and one companion Results and Research Register;
- ten primary model entrypoints under `/research/handoffs/`: one portfolio
  hub plus nine first-class research lanes. Six longer program dossiers remain
  as deeper overlapping subject views. The second 30 July checkpoint adds
  the corrected Program 1 `U0/U1/U2/B` boundary taxonomy and C.4 proof
  boundary, the scoped degree-five/six exclusions, the Program 3 and 4 proof
  audits, complete Program 5 source coupling together with the moving-target
  and secondary-class frontier, and the Program 6 filtered-action formalism.
  It records missing companion inputs for the stronger Program 5 packet.
  A subsequent GitHub recovery pass pins the Program 9 package and larger
  Program 6 chart packet at draft PR 1, the Program 4 six-obligation packet
  at PR 2, the Program 3 corrigendum at PR 3, and the Program 6 corrigendum
  at PR 4. All remain unmerged and keep their mathematical boundaries; the
  newest PR 1 head classifies the selected finite rank-six plane through its
  first intrinsic obstruction: generic slopes and `r=4` fail cubically,
  while the two conjugate exceptional slopes have 17-dimensional cubic-lift
  fibres but fail quartically, with exact certificate pairing `-1152`. The
  result does not classify the full row-base fibre or stable quotient. The
  same checkpoint adds ordered-composition PRS charts, a five-variable
  universal order-six reduction, and the five-dimensional Program 5
  polynomial-gauge core with its three residual surfaces. Its
  twelve package tests and thirty Program 6 tests pass. PR 4's
  source repairs are integrated with the old Macaulay implication explicitly
  conditional. Complete-chain admissibility and global attachment remain
  open. Conditional global syntheses remain conditional, and the
  public interval stays
  \(4\leq D_{\min}\leq 7\), and the state page names exhaustive
  message-to-claim reconciliation as the next post-import audit;
- a 2 August manual reconstruction of all nine first-class lanes from their
  source conversations, durable proof bodies, retained mathematics, and exact
  computation boundaries. The pages now expose the strongest reusable
  results, precise hypotheses, actual remaining gates, scoped task sequences,
  and explicit warnings against promoting slices or terminal certificates to
  global theorems. Lane 1 retains its complete defect/resolvent proof access,
  while Lane 6 preserves the compiler-owned first-class selected-plane
  argument;
- 76 collections with complete manuscript coverage, nine with partial
  coverage, and 19 for which manuscript coverage is not applicable;
- 21 context-only private records, not exported.

Seventeen collections are stable external public records. The other 85 are
explicitly labeled working drafts. Release state does not encode proof
strength, review, machine checking, attribution, or source form.

## Publication boundary

The private Jacobian research repository is authoritative. This repository
contains only its deterministic sanitized publication export, reader-facing
prose, versioned PDFs, selected immutable technical materials, and build
machinery.

`site-state.json` is the single sanitized site-release pointer. It pins the
legacy publication and stable-tag claim graph, the retained
working-mathematics graph,
manuscript and technical-material manifests, generated docs tree, expected
counts, and Pacific-time release date. Generators and checks resolve their
paths and counts from it. Every
model handoff also exposes the selected release as
`/research/handoffs/release.json`; its visible snapshot, counts, and
manuscript links are rendered from that same pointer.

The two mathematical components have different jobs. The 368 stable-tag
claim pages preserve the legacy publication pipeline and durable public URLs;
the 564-unit retained graph is the current progress-facing corpus for research
models. A retained `corrects` relation is rendered programmatically on the
affected legacy claim and collection pages, so historical wording cannot
silently outrank its current working replacement. Advancing either component
does not implicitly advance the other.

The selected inputs currently include the sanitized canonical/publication
export, hashes and metadata for six reader manuscripts and their companion
register, and the versioned MkDocs source tree. The stable implementation
surfaces are:

- `site-state.json`: active release selection and counts;
- `scripts/generate_living_guide_v2.py`: deterministic renderer for stable
  claim pages, result/open-problem collections, programs, retained
  working-mathematics units, evidence and catalogue pages, model handoffs,
  and the machine-readable handoff release;
- `scripts/check_public_site_v2.py`: source-data, content, leak, proof-access,
  search, release-coherence, and route validation;
- `data/model-handoffs-v16-20260802d/`: hash-pinned sanitized source for
  the hub, nine lane entrypoints, and six program dossiers; logical manuscript
  slots resolve against the selected manuscript manifest, so a stale PDF
  version fails the build;
- `scripts/check_deployed_site.py`: production verification that GitHub Pages
  serves the exact selected handoff release after deployment;
- `scripts/generate_compatibility_stubs_v1.py`: historical noindex
  compatibility pages for earlier public routes (not part of the active
  renderer).

The technical-material release contains sanitized computational supplements
for all six programs, two standalone Program 4 notes, their exact-check source
bundle, and one focused Program 2 boundary calculation.  The Program 4
supplement includes the elementary one-root transition, and the Program 5
supplement includes the global chart quintics and all seventeen sampled
first-normal rank profiles. It does not contain
raw conversations, internal evidence ledgers, private locators, or uncurated
working trees. Every artifact is hash-pinned, and archive contents plus PDF
text and metadata are inspected by the release and site checks.

The exporter and site checks reject private filesystem paths, ChatGPT share
links, conversation/message locators, internal record IDs, and UUIDs. PDF
text and metadata are scanned through the same boundary.

Earlier repository layers remain as historical public construction records;
they are not part of the active MkDocs source tree.

## Build and validate

With [`uv`](https://docs.astral.sh/uv/) installed:

```bash
uv run --with-requirements requirements.txt python scripts/generate_living_guide_v2.py
uv run --with-requirements requirements.txt python scripts/check_public_site_v2.py
uv run --with-requirements requirements.txt mkdocs build --strict --site-dir /tmp/jacobian-guide-preview
uv run --with-requirements requirements.txt python scripts/check_built_site.py /tmp/jacobian-guide-preview
```

For browser coverage:

```bash
uv run --with-requirements requirements.txt python -m playwright install chromium
uv run --with-requirements requirements.txt python scripts/browser_smoke_v1.py \
  --site-dir /tmp/jacobian-guide-preview
```

The browser suite covers desktop and mobile navigation (including every
handoff), both color schemes, MathJax, PDF proof links, noindex, heading
structure, landmarks, link labels, contrast, keyboard focus, reduced motion,
and horizontal overflow.

## Current publication policy

Source and attribution improvements are welcome. The guide can be corrected
directly while it remains unannounced. A durable public corrections ledger
will begin only when readers are deliberately invited to use the site.

No announcement, release tag, DOI, or manuscript submission is part of this
working-draft deployment.
