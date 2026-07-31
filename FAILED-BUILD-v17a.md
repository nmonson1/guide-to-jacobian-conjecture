# Failed build: v17a

The additive `docs-v17a-20260729a/` candidate is not selected for
publication. Its source-local `release.json` link passed the Markdown-source
boundary check, but the link lived inside raw HTML. MkDocs therefore preserved
the literal `href` instead of rewriting it for the generated handoff
subdirectory, and the built-site checker rejected all seven routes.

The release-metadata link is now ordinary Markdown, allowing MkDocs to resolve
the source sibling into the correct built URL. The replacement candidate is
`docs-v17b-20260729a/`. The failed tree is retained because generated release
candidates are write-once.
