# Contributing

This is an unannounced public working draft. The most useful contributions
right now are:

- a better primary source;
- a correction to a statement or its scope;
- a correction to role-specific credit;
- a more precise description of what a proof, computation, or formalization
  checks;
- an accessibility or presentation fix.

Use the
[source-improvement form](https://github.com/nmonson1/guide-to-jacobian-conjecture/issues/new?template=source.yml)
or open a focused issue.

## Keep the publication concepts separate

- `source` records where a statement, proof, exposition, formalization, or
  check was encountered;
- `credited_to` records a person and role, together with the basis for that
  attribution;
- `ai_assistance` records the system, purpose, role, and responsible human;
- `evidence_present` records the kind and scope of available evidence;
- `source_form` distinguishes announcements, working manuscripts, preprints,
  repositories, and refereed publications;
- `independent_review` records exactly what, if anything, was independently
  checked.

Please do not compress these fields into one confidence or publication-status
label.

## Public-boundary rules

Do not add raw conversations, ChatGPT share links, private filesystem paths,
internal archive locators, private record identifiers, working TeX trees, or
unsanitized computational artifacts. Public code and formalizations should be
linked at stable public revisions.

AI-assisted work must identify the system and purpose. A human contributor
remains responsible for every submitted assertion.

## Before opening a pull request

Run:

```bash
uv run --with-requirements requirements.txt python scripts/generate_living_guide_v1.py
uv run --with-requirements requirements.txt python scripts/generate_compatibility_stubs_v1.py
uv run --with-requirements requirements.txt python scripts/check_public_site.py
uv run --with-requirements requirements.txt mkdocs build --strict --site-dir /tmp/jacobian-guide-preview
uv run --with-requirements requirements.txt python scripts/check_built_site.py /tmp/jacobian-guide-preview
```

Keep a pull request focused, preserve exact source versions and dates, and say
what the proposed change does not establish.
