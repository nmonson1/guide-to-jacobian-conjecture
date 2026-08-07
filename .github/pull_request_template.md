## Reader need

What page would someone want to visit, and what does this change help them
understand or do?

## Mathematical scope

State the exact result or exposition change. What does it not prove?

## Sources and credit

List primary sources, stable versions or retrieval dates, and each person's
role. Call out any precedence or attribution change explicitly.

## Editorial state

- [ ] Every substantive page is hand-authored.
- [ ] New pages begin as `unread` in `editorial/reviews.json`.
- [ ] I did not approve a page on the owner's behalf.
- [ ] External developments known to be relevant are credited and sourced.

## Checks

- [ ] `python -m unittest discover -s tests`
- [ ] `python scripts/check_site.py`
- [ ] `mkdocs build --strict`
- [ ] `python scripts/check_built_site.py site`
