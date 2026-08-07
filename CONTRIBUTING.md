# Contributing

The most useful contributions improve a page a reader might genuinely want
to use: clearer exposition, a corrected theorem statement, a missing external
development, better credit, or a stronger primary source.

## Content rules

- Substantive pages are hand-authored. Do not generate a page for every
  internal claim, record, lane, or computation.
- The guide is selective about our work and inclusive about external work.
- Credit people for distinct roles: question, construction, proof,
  computation, exposition, formalization, correction, or other actual role.
- Prefer primary sources and describe their form accurately. An announcement
  is not a refereed paper; a computation has only the scope its inputs and
  certificates support.
- Keep the guide nontechnical in proof length, not imprecise in statement.
  Link full proofs and computations rather than reproducing every step.
- Do not add raw conversations, private paths, internal research identifiers,
  or unsanitized working artifacts.
- Do not treat AI output as a source. Historical claims need a citable public
  record, and mathematical claims need a proof route.

Our aim is to record every relevant external contribution known to us.
Omissions are mistakes to be corrected, not editorial judgments that the work
was unimportant.

Authorship and AI assistance are disclosed once, project-wide, in
`docs/about/ai-assistance.md`. Do not add generic AI boilerplate to every
mathematics page; add a page-specific note only when the computational or
formal method matters to the result itself.

## Result-page shape

A major result page normally contains:

1. a headline, including name and date for external work;
2. “What is true and why,” one compressed paragraph that makes a nearby
   expert unsurprised by the proof;
3. the precise definitions, hypotheses, and conclusion;
4. discussion or a longer proof sketch, including importance and limits;
5. links to primary sources and relevant computations.

A computation page may be a navigational cul-de-sac: enough detail to replay
the proof or calculation, but no conceptual dependency that a reader needed
to understand the result page.

## Editorial workflow

New pages must be entered in both `editorial/navigation.json` and
`editorial/reviews.json`, initially as `unread`. Do not mark a page approved on
someone else's behalf. Approval pins the exact Markdown hash; subsequent edits
automatically remove the page from ordinary navigation, search, and the
sitemap until it is reviewed again.

Before opening a pull request, run:

```bash
uv run --with-requirements requirements.txt python -m unittest discover -s tests
uv run --with-requirements requirements.txt python scripts/check_site.py
uv run --with-requirements requirements.txt mkdocs build --strict --site-dir /tmp/jacobian-guide-preview
uv run --with-requirements requirements.txt python scripts/check_built_site.py /tmp/jacobian-guide-preview
```

In the pull request, identify the reader need, mathematical scope, sources,
credit changes, and what the change does not establish.
