# Guide to the Jacobian Conjecture

Source repository for an English-language, evidence-labeled guide to the 2026
Jacobian-conjecture counterexample, its geometry, formal verification, and the
surviving two-dimensional problem.

The published site will be:

<https://nmonson1.github.io/guide-to-jacobian-conjecture/>

## Editorial boundary

This is a curated public guide, not a mirror of private research conversations
or recovered working archives. Every mathematical assertion published here
should carry a source and an evidence status. Lean is welcome but optional.

## Build locally

With [`uv`](https://docs.astral.sh/uv/) installed:

```bash
uv run --with-requirements requirements.txt mkdocs serve
```

Run the same checks used by continuous integration:

```bash
uv run python scripts/check_public_site.py
uv run --with-requirements requirements.txt mkdocs build --strict
```

## Contributing

English exposition, corrections, source improvements, exact computations, and
formalizations are all in scope. See [CONTRIBUTING.md](CONTRIBUTING.md).

No content license has been selected yet. A license must be chosen before
accepting third-party prose contributions.

