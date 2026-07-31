# Failed build: docs v23a

The `docs-v23a-20260730a` tree contains a complete static scaffold and 494
generated pages, but its Program 2 model brief was derived from the compact
private lab brief rather than the validated full public handoff. Public-site
validation correctly rejected the missing coverage rule, glossary,
dependency map, proof-signature index, and full seven-orbit conic claim
package.

The tree is retained as a construction record and is not selected by
`site-state.json`. The corrected build uses `docs-v23b-20260730a` and the
hash-pinned `model-briefs-v12b-20260730a` source release.
