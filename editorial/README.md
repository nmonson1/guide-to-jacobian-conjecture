# Editorial state

Every Markdown page in `docs/` is hand-authored and publicly buildable. The
files in this directory control only whether an exact page version is listed
in ordinary navigation, indexed by the site search, and included in the
sitemap.

The states are `unread`, `needs_revision`, and `approved`. Approval records a
SHA-256 hash of the exact Markdown file. Changing an approved file makes its
effective state `changed_since_review` until the new version is reviewed.

This is an internal editorial workflow. It is not a statement about whether a
mathematical result has been independently reviewed.
