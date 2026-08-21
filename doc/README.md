# doc - Output / deliverable

Published documentation, as distinct from `Needs/` (traceable requirements) and `source/markdown/` (working drafts):

- `manuals/` — end-user or operator manuals.
- `release_notes/` — one file per release.
- `errata/` — known issues and corrections against published docs.

## Building manuals/user_manual.rst to PDF

`manuals/user_manual.rst` is converted to PDF via Pandoc (not part of the
`Needs/`/root Sphinx builds — this is a standalone conversion so no binary
template is required, per the yml/rst/md-only source policy).

Locally:

```
cd doc/manuals
pandoc user_manual.rst -o user_manual.pdf --pdf-engine=pdflatex
```

In CI: `.github/workflows/user_manual_pdf.yml` runs the same command on
every push/PR that touches this file and uploads `user_manual.pdf` as a
build artifact.
