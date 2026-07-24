# Guide to the Jacobian Conjecture

Source repository for a chronological, versioned record of events,
contributions, and claims concerning the Jacobian conjecture.

Published site: <https://nmonson1.github.io/guide-to-jacobian-conjecture/>

## Record-first guide

The site now contains:

1. 22 dated event records from 1884 through 21 July 2026;
2. 13 stable contribution records;
3. 28 source-linked public claim pages generated from validated JSON records;
4. 11 guided topic pages assembled only from those public claims.

A short overview and exact counterexample certificate are built on those
records. Longer methodology and mathematical storylines remain deferred.
Sequence numbers record entry into this repository; they do not by themselves
establish historical priority.

## Repository objects

- `events/`: dated developments, source-status observations, and corrections;
- `contributions/`: attributed works or historical imports;
- `claims/`: the original chronological claim-record baseline;
- `data/claims-v2/`: the preserved first promoted claim export;
- `data/claims-v3/`: the current scoped, dependency-linked public claim export;
- `data/packages-v1/`: the first reviewed mathematical-package export;
- `assessments/`: named, version-specific checks performed for this project;
- `docs/claim-v3/`: current generated page-per-claim views;
- `scripts/generate_claim_pages_v3.py`: the current deterministic claim renderer;
- `scripts/generate_chronology_v2.py`: the deterministic chronology renderer;
- `scripts/generate_overview_v2.py`: the overview and certificate renderer.
- `scripts/generate_topic_pages_v1.py`: the guided-topic renderer.

Event dates and contribution accessions are independent. The project records
external proof, computation, and formalization as evidence, but does not call
that material a project assessment until a named reviewer records exactly what
was checked against a pinned version.

## Build locally

With [`uv`](https://docs.astral.sh/uv/) installed:

```bash
uv run --with-requirements requirements.txt python scripts/validate_records.py
uv run --with-requirements requirements.txt python scripts/validate_public_claims_v2.py
uv run --with-requirements requirements.txt python scripts/generate_claim_pages.py
uv run --with-requirements requirements.txt python scripts/validate_public_claims_v3.py
uv run --with-requirements requirements.txt python scripts/generate_claim_pages_v3.py
uv run --with-requirements requirements.txt python scripts/generate_chronology_v2.py
uv run --with-requirements requirements.txt python scripts/generate_overview_v2.py
uv run --with-requirements requirements.txt python scripts/validate_public_packages_v1.py
uv run --with-requirements requirements.txt python scripts/generate_topic_pages_v1.py
uv run --with-requirements requirements.txt python scripts/check_public_site.py
uv run --with-requirements requirements.txt mkdocs build --strict
```

## Intake status

Corrections and source improvements are welcome. New third-party prose and
mathematical submissions will not be listed until a content license and
editorial charter have been selected.
