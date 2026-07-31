# Failed build: v17

The additive `docs-v17-20260729a/` candidate is not selected for publication.
Its generated handoff snapshot linked to `../release.json` in Markdown source,
which points outside the handoff source directory and was rejected by the
publication-boundary link checker.

The generator was corrected to use the source-local sibling
`release.json`; MkDocs converts that source link to the appropriate built
route. The replacement candidate is `docs-v17a-20260729a/`. The failed tree is
retained because generated release candidates are write-once.
