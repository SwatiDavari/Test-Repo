# test_repo

Sphinx-Needs based repository for ASPICE / ISO 26262 / ISO/SAE 21434 /
ISO 29119 aligned development. See `STANDARDS.md` for the folder-to-standard
crosswalk.

This repo has **two independent Sphinx projects**:

- **Root** (this `conf.py`) — organizational governance (`organisation/governance/`,
  `organisation/verification/`), strategy (`organisation/strategy/`), and project management
  (`management/`, `test/`). Renders `org_req` needs only.
- **`Needs/`** (its own `conf.py`) — the product traceability graph:
  system/feature/component/unit requirements and the safety chain
  (`sg`/`fsr`/`tsr`). Build it separately from inside `Needs/`.

## Build docs locally

```
pip install sphinx sphinx-needs
sphinx-build -b html . _build/html          # root project
cd Needs && sphinx-build -b html . _build/html   # Needs/ project
```

## Build & test code (per-language, under source/)

Each language under `source/<lang>/` has its own build tooling
(CMake for C/C++, Cargo for Rust, npm/tsc for TypeScript, pytest for
Python) — see `.github/workflows/` for the exact commands run in CI.

## Structure

- `Needs/` — product traceability: `Communication/`, `Diagnostics/`
  (feature/component/unit design per module), `safety/` (safety chain +
  `analyses/`), `cybersecurity/`, `quality/` — see `Needs/` for details.
- `organisation/governance/` — organization-level requirements per standard
  (ASPICE, ISO 26262, ISO/SAE 21434).
- `organisation/verification/` — ISO 29119 organization-level test-process
  requirements.
- `organisation/strategy/`, `organisation/common_framework/`, `organisation/tools/` — not yet
  reviewed as part of this documentation pass.
- `source/` — implementation, one folder per language.
- `test/` — test basis, conditions, design, procedures, cases, suites,
  reports, executions.
- `management/` — change, planning, problem, and risk registers.
- `doc/` — published documentation (manuals, tutorials, reference,
  release notes, errata).

## Known gaps (disclosed, not yet resolved)

- `Needs/conf.py` does not currently register `org_req`, `eng_need`, or
  `feat_req` types even though live content under `Needs/` uses `eng_need`
  (`business-needs.rst` etc.) and `Needs/Communication`'s orphaned
  `FEAT_DIAGNOSTICS_001` stub used `feat_req`. This file has reverted to
  its bare original twice during recent work with no identified cause —
  fixing it again is pending that investigation.
- `FEAT_A_001` and `FEAT_Z_001` both link to `SYS_001`, which doesn't exist
  anywhere in this repo (dead link).
- `organisation/common_framework/`, `organisation/tools/`, `organisation/strategy/` have not been
  reviewed for correctness as part of this documentation pass.
