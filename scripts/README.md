# scripts/

Local helper scripts for building the `needs/` Sphinx-needs traceability
project. Both scripts are standalone `bash`/POSIX scripts you can run from
a clone of this repo; neither depends on anything outside it.

## What's here

| Script | What it does |
|---|---|
| `fetch_external_needs.sh` | Exports the root project's own needs (`org_req`, `risk`, `problem`, `change`, `exception`, `tool`, `infra`) via `sphinx-build -b needs . _build/org_needs`, then copies the result to `needs/_external_needs/org_needs.json` — the exact path `needs/conf.py`'s `needs_external_needs` setting expects. This is the same export the "Export organisation/governance/ needs.json" step of `.github/workflows/ci-needs.yml` already runs inline; this script just makes it runnable locally too. |
| `build_needs.sh` | Builds `needs/`: creates/reuses a local venv, installs `needs/requirements.txt`, builds the HTML docs with `-W` (warnings as errors), then builds `needs/_build/needs/needs.json` and prints the resulting need count. Warns (doesn't fail) if `needs/_external_needs/org_needs.json` is missing, since without it any `:links:` field pointing at a root-project id will build as broken. |
| `build_safety_manual_pdf.sh` | Builds the Qorix-branded Safety User Manual PDF from `needs/communication/safety_user_manual.rst` via Sphinx's LaTeX builder + XeLaTeX. Wired into `.github/workflows/safety_user_manual_pdf.yml`, which calls it as `./scripts/build_safety_manual_pdf.sh`. See the known-gap note below — it currently can't succeed end to end. |

Run `fetch_external_needs.sh` before `build_needs.sh` if you've changed
anything under the root project (`organisation/governance/`, etc.) since the
last export — `needs/_external_needs/` is generated output, not something
committed to the repo.

```bash
scripts/fetch_external_needs.sh
scripts/build_needs.sh
```

## Known gap: `build_safety_manual_pdf.sh` can't complete yet

`needs/conf.py`'s `latex_documents` entry for this manual points at
`needs/communication/safety_user_manual.rst`, which doesn't exist in this
repo. The only real safety-manual content currently lives at
`doc/manuals/safety/safety_user_manual.rst`, in the root Sphinx project —
a different project entirely. Until one of those is reconciled (either
author `needs/communication/safety_user_manual.rst`, or repoint
`conf.py`/this pipeline at the root project's manual), running this script
— or the `safety_user_manual_pdf.yml` CI job that calls it — fails at the
`sphinx-build` step.
