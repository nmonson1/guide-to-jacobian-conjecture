# Guide to the Jacobian Conjecture

Source repository for a chronological, versioned record of events,
contributions, and claims concerning the Jacobian conjecture.

Published site: <https://nmonson1.github.io/guide-to-jacobian-conjecture/>

## Record-first rebuild

The first public exposition has been unpublished from the current build. It
remains recoverable from Git history at commit `a96286c`. The replacement now
contains:

1. 22 dated event records from 1884 through 21 July 2026;
2. 13 stable contribution accessions;
3. 21 normalized mathematical and historical claims.

Exposition will be added only after the relevant contribution, claim, and
assessment records exist. Sequence numbers record entry into this repository;
they do not by themselves establish historical priority.

## Repository objects

- `events/`: dated developments, source-status observations, and corrections;
- `contributions/`: attributed works or historical imports;
- `claims/`: normalized mathematical assertions and questions;
- `assessments/`: named, version-specific checks performed for this project;
- `docs/`: the sparse public index of those records.

Event dates and contribution accessions are independent. The project records
external proof, computation, and formalization as evidence, but does not call
that material a project assessment until a named reviewer records exactly what
was checked against a pinned version.

## Build locally

With [`uv`](https://docs.astral.sh/uv/) installed:

```bash
uv run --with-requirements requirements.txt python scripts/validate_records.py
uv run --with-requirements requirements.txt mkdocs build --strict
```

## Intake status

Corrections and source improvements are welcome. New third-party prose and
mathematical submissions will not be listed until a content license and
editorial charter have been selected.
