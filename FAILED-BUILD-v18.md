# Failed build v18

`docs-v18-20260730a/` was generated directly into an empty directory on
2026-07-30. The graph-native generator wrote its 494 deterministic pages, but
the public-site check then failed because the unchanged static site shell
(`index.md`, reader introductions, robots policy, and assets) had not first
been copied from the prior release.

The directory is retained as failed construction history and must not be
selected or deployed. Release v18a reconstructs the site in a new path by
copying only the prior release's non-generated static files before running
the write-once generator.
