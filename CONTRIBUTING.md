# Contributing

This project accepts English-language mathematical contributions through
GitHub pull requests. Lean is useful but not required.

## Good contributions

- correct or clarify an existing claim;
- add a primary source and explain precisely what it supports;
- improve an exposition without strengthening its mathematical conclusion;
- add an exact, reproducible computational certificate;
- link or contribute a Lean formalization;
- turn an unresolved assertion into a clearly scoped open question.

## Claim discipline

Every substantive new claim should state:

1. the exact assertion and hypotheses;
2. its evidence status;
3. the source or certificate supporting it;
4. its boundary—what it does **not** establish;
5. whether novelty or priority has actually been checked.

Use one of the site's evidence labels: `FORMALIZED`, `EXACT-CERTIFICATE`,
`PUBLIC-SOURCE`, `CLASSICAL`, `UNDER-REVIEW`, or `OPEN`.

Do not present numerical evidence as an exact proof, a successful script as a
proof of surrounding prose, or a same-day calculation as historically new.

## Pull-request process

1. Open or claim an issue for a substantial contribution.
2. Keep each pull request focused on one mathematical change.
3. Include links to primary sources and reproducible commands where relevant.
4. Ensure `scripts/check_public_site.py` and `mkdocs build --strict` pass.
5. Respond to mathematical and editorial review.

Authorship and intellectual credit should be described in the pull request,
not inferred from line counts. AI-assisted work must identify what was checked
independently and by whom.

