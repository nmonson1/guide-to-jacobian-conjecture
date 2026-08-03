# Public generated-tree compaction preflight

The current inventory is `public-baseline-f6a353f-20260803-v2b.json`. It was
measured at commit `f6a353f` while `site-state.json` still selected public v51,
so it is a baseline and recoverability audit, not the deletion list for v52.
The earlier `v2` inventory omitted 45 symlink entries and is superseded.

At this baseline, `site-state.json` selects one docs tree and eight data roots:
2,323 tracked files and 122,225,422 apparent bytes. Another 160 tracked roots
contain 55,742 files and 958,861,384 apparent bytes. The main checkout has 35
untracked generated roots with 20,961 regular files, 45 symlinks, and
151,253,577 apparent bytes.

All 35 untracked roots have distinct normalized content from every tracked
generated root. They are preserved in the write-once archive identified by
`archive-locator-20260803-v2.json`; the archive copied symlinks as symlinks and
then compared every regular-file hash and link target with the source. Two
earlier output directories are incomplete and contain no manifest. They are
safe to remove after the valid `v2c` manifest is independently checked, but
must never be cited as recovery artifacts.

## Safe post-v52 deletion rule

Do not reuse the 160-root baseline list blindly. After v52 is generated and
selected, rerun `inventory_active_tree.py` and
`inventory_generated_recoverability.py` against the v52 commit. The exact
tracked deletion pathspec is the fresh inventory's `inactive_roots`; the exact
allowlist is its selected docs root plus selected data roots. Remove nothing
outside those generated-root classes.

Before applying that pathspec:

1. verify `pre-compaction-public-v49-20260803` still resolves to `3911f19`;
2. archive any newly appearing untracked root whose digest has no tracked
   duplicate;
3. hash the v52 retained-math exports, handoffs, proof sources, compatibility
   map, and stable-route set;
4. perform the removal in a scoped commit and regenerate to a new docs suffix;
5. require those mathematical exports and routes to be byte-identical;
6. run generation, publication-boundary, strict MkDocs, built-site, link,
   browser, and live-release checks.

The inventory also records branch ancestry and missing/prunable worktree
metadata. Only branches whose tips are ancestors of the final integration
commit are automatic branch-deletion candidates. A missing worktree does not
make a branch with branch-only commits disposable.

## First v52 candidate measurement

`public-candidate-5773af3-20260803-v2.json` is a second write-once inventory
made after the first coherent v52 candidate was committed. It selects
`docs-v52-converged-research-state-20260803c` and eight data roots, totalling
2,330 files and 126,698,076 bytes. The exact inactive pathspec has 165 roots,
57,005 files, and 1,075,984,995 bytes. Its SHA-256 is
`d9fd7e22b676e0fb317ff02f9f48391691e720d8ecaffe3bafb3338d06b69c9b`.

That exact 165-root list is safe to apply only if `5773af3` is the release
freeze. If review produces another release commit or suffix, rerun the tool
and use the successor inventory instead.
