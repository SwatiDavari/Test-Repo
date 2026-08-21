# doc - Output / deliverable

Published documentation, as distinct from `Needs/` (traceable
requirements) and `source/markdown/` (working drafts):

- `release_notes/` — one file per release.
- `errata/` — known issues and corrections against published docs.

**2026-08-21: `manuals/` moved to `needs/user_guide/`.** Both the general
product user manual and the Safety User Manual used to live here as
`manuals/user_manual.rst` and `manuals/safety/safety_user_manual.rst`.
They're now `needs/user_guide/user_manual.rst` and
`needs/user_guide/safety/safety_user_manual.rst` — the Safety User
Manual's traceable content (`safefeat`/`rec`/`res` directives) only
parses correctly under the `needs/` project's schema, and living outside
it meant the *root* project's Sphinx build picked these files up by
accident (nothing excluded `doc/` from its source scan) and threw
"Unknown directive type" errors on every build. See
`needs/user_guide/index.rst` for the full rationale. `manuals/` is left
empty (just `.gitkeep`) here as a result — nothing currently uses it.

## Building user_manual.rst to PDF

`needs/user_guide/user_manual.rst` is converted to PDF via Pandoc (not
part of the `needs/`/root Sphinx builds — this is a standalone
conversion so no binary template is required, per the yml/rst/md-only
source policy).

Locally:

```
cd needs/user_guide
pandoc user_manual.rst -o user_manual.pdf --pdf-engine=pdflatex
```

In CI: `.github/workflows/user_manual_pdf.yml` runs the same command on
every push/PR that touches this file and uploads `user_manual.pdf` as a
build artifact.
