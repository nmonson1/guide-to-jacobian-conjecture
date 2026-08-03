# Public active-tree compaction

This branch prepares a storage cleanup; it does not change the deployed site,
`site-state.json`, `mkdocs.yml`, or any generated release tree.

Run:

```bash
uv run --with-requirements requirements.txt python -B \
  scripts/inventory_active_tree.py
```

The inventory derives the allowlist from `site-state.json`. It treats the
selected `docs_dir` and every selected component `data_dir` as active, lists
all other tracked generated roots as archival candidates, and separately
lists untracked generated candidates. It never chooses a release from a
version suffix and never deletes anything. `--output` writes a new file and
refuses to overwrite an existing one.

At baseline tag `pre-compaction-public-v49-20260803`, release v49 selects one
documentation root and eight data roots. Those roots contain 2,312 tracked
files and 20,273,597 apparent bytes. Another 156 tracked generated roots
contain 53,370 files and 836,874,946 apparent bytes. The main checkout also
has 35 untracked generated candidate roots; those require an ownership check
after Lane 3 and Lane 8 finish.

After the next coherent release is deployed and verified:

1. rerun the inventory against the new `site-state.json`;
2. retain the new selected roots and ordinary maintained source;
3. remove inactive tracked generated roots from `main`, relying on the named
   baseline tag and Git history for recovery;
4. remove untracked candidates only after confirming that no active agent or
   lane owns them;
5. run the complete generation, publication-boundary, strict MkDocs,
   built-site, browser, link, and deployed-site checks.

Removing old trees from the active branch does not rewrite Git history and
therefore does not immediately shrink `.git`. It does reduce checkout size,
status and traversal work, release diffs, and the chance that an obsolete
tree is mistaken for current source. History rewriting is not part of this
plan.
