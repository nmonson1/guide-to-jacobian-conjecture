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
- six version-13 reader PDFs and one companion Results and Research Register;
- six self-contained, searchable program handoffs plus one cross-program
  state page under `/research/handoffs/`;
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

`site-state.json` is the single sanitized release pointer. It pins the
publication, unified claim graph, manuscript and technical-material
manifests, generated docs tree, expected counts, and Pacific-time release
date. Generators and checks resolve their paths and counts from it.

The selected inputs currently include the sanitized canonical/publication
export, hashes and metadata for six reader manuscripts and their companion
register, and the versioned MkDocs source tree. The stable implementation
surfaces are:

- `site-state.json`: active release selection and counts;
- `scripts/generate_living_guide_v2.py`: deterministic renderer for stable
  claim pages, result/open-problem collections, programs, evidence, and
  catalogue pages;
- `scripts/check_public_site_v2.py`: source-data, content, leak, proof-access,
  search, and route validation;
- `data/model-briefs-v5-20260729a/`: hash-pinned sanitized source for
  model-ready HTML handoffs;
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
