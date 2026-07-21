# Contributing

The repository is in a record-first baseline phase.

## Currently accepted

- corrections to contribution metadata;
- corrections to normalized claim statements or boundaries;
- primary-source improvements;
- corrections to attribution or source versions;
- improvements to record validation and site accessibility.

New third-party mathematical submissions will not be assigned a sequence
number until the project publishes its content license and editorial charter.

## Record discipline

A contribution, claim, assessment, and explanatory page are different objects:

- a **contribution** is an attributed work or historical import;
- a **claim** is a normalized mathematical assertion or question;
- an **assessment** says who checked what, by which method, against which
  version;
- **exposition** explains integrated claims to readers.

`listed` means that a contribution is in scope, attributable, intelligible, and
legally publishable. It does not mean that the project endorses its claims.
`integrated` is a separate editorial decision and requires a named assessment.

## Pull requests

1. Keep a pull request focused on one record or one infrastructure change.
2. Preserve source versions, dates, and attribution exactly.
3. State what the change does not establish.
4. Do not populate an `assessment_actions` field without naming the assessor,
   method, scope, and reviewed version.
5. Run:

   ```bash
   uv run --with-requirements requirements.txt python scripts/validate_records.py
   uv run python scripts/check_public_site.py
   uv run --with-requirements requirements.txt mkdocs build --strict
   ```

AI-assisted work must identify the tool and purpose. A human contributor
remains responsible for every submitted assertion.

