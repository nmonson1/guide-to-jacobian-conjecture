# Failed build v18a

`docs-v18a-20260730a/` correctly combined the unchanged static shell with 494
fresh graph-native pages, but the public-site validator rejected its source
briefs before release:

- the Program 2 handoff had accidentally removed the required `Coverage
  rule` and `Compact glossary` semantic markers while being condensed below
  4,000 words;
- the cross-program handoff used the status-like phrase “independent
  specialist review”; and
- `mkdocs.yml` did not carry the date expected from the release pointer.

The directory is retained as failed construction history and must not be
selected or deployed. The corrected, still-3,989-word Program 2 source is
regenerated in v18b.
