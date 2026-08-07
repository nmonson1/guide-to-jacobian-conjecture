# Contributing

The most useful contributions improve something a reader deliberately visits:
a clearer explanation, a corrected theorem statement, a missing diagram, a
better primary source, a credit correction, or a stronger route into the
mathematics.

## Write for the mathematical reader

- Begin with a question, phenomenon, example, or object whose behavior needs
  explanation.
- Introduce an abstraction after the reader has seen why it is useful.
- State the causal chain behind a memorable slogan; do not rely on compressed
  pronouncements alone.
- Name the surprising or difficult step. Mathematical judgment is part of
  exposition.
- Prefer a specific heading such as `How the boundary recovers q` to a generic
  heading such as `Discussion` or `What is true and why`.
- Use diagrams when they reveal a map, a fiber, a boundary, a loop, or a
  degeneration more efficiently than prose.
- Keep the best central contrasts and remove habitual `not A, but B`
  constructions. Positive causal statements usually read more smoothly.
- End by resolving the opening question or exposing the next obstruction.

The full working conventions are in `editorial/expository-style.md`.

## Keep the reading and audit layers distinct

The reading page explains the mathematics. The [proof and evidence
ledger](docs/results/evidence-ledger.md) records proof links, formal checks,
publication status, role-specific attribution, chronology, and scope. Logical
hypotheses and limitations that change the theorem remain in the reading page.
Archival bookkeeping normally moves to the ledger.

Do not treat AI output as a source. Historical claims need a citable public
record, and mathematical claims need a proof route.

## Credit

Credit people for their actual roles: question, construction, proof,
computation, exposition, formalization, correction, announcement, or another
documented contribution. Prefer primary sources and stable versions. Do not
infer priority from close public timestamps or private chronology absent from
the public record.

Our aim is to record every relevant external contribution known to us.
Omissions are mistakes to be corrected, not editorial judgments that the work
was unimportant.

## Editorial workflow

New public pages must be entered in both `editorial/navigation.json` and
`editorial/reviews.json`, initially as `unread`. Do not approve a page on the
owner's behalf. Approval pins the exact Markdown hash; later edits remove the
page from ordinary navigation, search, and the sitemap until it is reviewed
again.

Before opening a pull request, run:

```bash
uv run --with-requirements requirements.txt python -m unittest discover -s tests
uv run --with-requirements requirements.txt python scripts/check_site.py
uv run --with-requirements requirements.txt mkdocs build --strict
uv run --with-requirements requirements.txt python scripts/check_built_site.py site
python scripts/audit_prose.py
```

The prose audit is advisory. A pull request should explain the reader need,
the mathematical scope, the sources and credit, the editorial state, and the
checks performed.
