# doc - Output / deliverable

Published documentation, as distinct from `Needs/` (traceable
requirements) and `source/markdown/` (working drafts):

- `manuals/` — end-user or operator manuals.
- `release_notes/` — one file per release.
- `errata/` — known issues and corrections against published docs.

**2026-08-21: `manuals/` briefly moved to `needs/user_guide/` and back.**
The Safety User Manual (`manuals/safety/safety_user_manual.rst`) uses
three sphinx-needs directives (`safefeat`/`rec`/`res`) that were only
registered in `needs/conf.py`'s schema, not the root project's — building
it here threw "Unknown directive type" errors. Moved it (and
`manuals/user_manual.rst`, for a single "User Guide" location) into
`needs/user_guide/` to use that schema, then moved both back here the
same day at the request to keep them under Product/Program → Docs as
originally structured. The real fix that let them come back: `safefeat`/
`rec`/`res` are now also registered as real need types in the *root*
project's own `conf.py`, so they parse correctly here.

Known trade-off, disclosed rather than hidden: `safety_user_manual.rst`
links (`:links:`, `:need:`) to `TSR_001`/`SG_001`/`FSR_001`/`COMP_A_001`,
which are real needs — but they're defined in the *separate* `needs/`
Sphinx project, not here, so this project's build can't validate or
resolve them and shows "linked need not found" warnings for each. This
matches the file's original, pre-existing state (these warnings aren't
new); making them resolve for real would need a two-way needs-import
pipeline between this project and `needs/` (mirroring the existing
one-way org_req import `needs/` already does from this project) —
flagged as a possible follow-up rather than building it now.

## Building manuals/user_manual.rst to PDF

`manuals/user_manual.rst` is converted to PDF via Pandoc (not part of the
`needs/`/root Sphinx builds — this is a standalone conversion so no binary
template is required, per the yml/rst/md-only source policy).

Locally:

```
cd doc/manuals
pandoc user_manual.rst -o user_manual.pdf --pdf-engine=pdflatex
```

In CI: `.github/workflows/user_manual_pdf.yml` runs the same command on
every push/PR that touches this file and uploads `user_manual.pdf` as a
build artifact.
