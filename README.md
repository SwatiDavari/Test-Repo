# Qorix Engineering Processes

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

## One organization, one repo, one workspace

Everything — docs, product traceability, governance, and source for five
languages — lives in this single repository, opened in VS Code as a single
workspace root via `qorix-engg.code-workspace` (no multi-root, no separate
repos to juggle).

```
test_repo/
├── .github/
│   └── workflows/
│       ├── ci-needs.yml
│       ├── ci-source-c.yml
│       ├── ci-source-cpp.yml
│       ├── ci-source-python.yml
│       ├── ci-source-rust.yml
│       ├── ci-source-typescript.yml
│       ├── ci.yml
│       └── docs.yml
├── .vscode/
│   ├── extensions.json
│   ├── settings.json
│   └── tasks.json
├── doc/
│   ├── errata/
│   │   └── .gitkeep
│   ├── manuals/
│   │   └── .gitkeep
│   ├── reference/
│   │   └── .gitkeep
│   ├── release_notes/
│   │   └── v0.1.0.md
│   ├── tutorials/
│   │   └── .gitkeep
│   └── README.md
├── management/
│   ├── change/
│   │   ├── change-register.yml
│   │   └── changes.rst
│   ├── exceptions/   (empty)
│   ├── planning/
│   │   ├── milestones.yml
│   │   └── project-plan.rst
│   ├── problem/
│   │   ├── problem-register.yml
│   │   └── problems.rst
│   └── risk/
│       ├── risk-register.yml
│       └── risks.rst
├── Needs/
│   ├── Communication/
│   │   ├── component/
│   │   │   ├── requirements/
│   │   │   │   └── index.rst
│   │   │   ├── comp_a_001.rst
│   │   │   └── index.rst
│   │   ├── feature/
│   │   │   ├── requirements/
│   │   │   │   └── index.rst
│   │   │   ├── feat_a_001.rst
│   │   │   └── index.rst
│   │   ├── unit design/
│   │   │   └── unit_a_001.rst
│   │   └── index.rst
│   ├── cybersecurity/
│   │   ├── tara/
│   │   │   └── index.rst
│   │   └── index.rst
│   ├── Diagnostics/
│   │   ├── component/
│   │   │   └── comp_z_001.rst
│   │   ├── feature/
│   │   │   └── feat_z_001.rst
│   │   ├── unit design/
│   │   │   └── unit_z_001.rst
│   │   └── index.rst
│   ├── quality/
│   │   ├── metrics/
│   │   │   └── index.rst
│   │   ├── reviews/
│   │   │   └── index.rst
│   │   └── index.rst
│   ├── safety/
│   │   ├── analyses/
│   │   │   ├── dependent-failure-analysis.rst
│   │   │   ├── fmea.rst
│   │   │   └── index.rst
│   │   ├── fsr_001.rst
│   │   ├── index.rst
│   │   ├── sg_001.rst
│   │   └── tsr_001.rst
│   ├── sys/
│   │   ├── index.rst
│   │   └── sys_001.rst
│   ├── business-needs.rst
│   ├── conf.py
│   ├── index.rst
│   ├── operational-needs.rst
│   ├── requirements.txt
│   └── stakeholder-needs.rst
├── organisation/common_framework/
│   ├── core lib/   (empty)
│   └── HAL/   (empty)
├── organisation/governance/
│   ├── aspice/
│   │   ├── index.rst
│   │   └── org_aspice_requirements.rst
│   ├── coding guidelines/
│   │   ├── c/
│   │   │   ├── c_MISRA2017.md
│   │   │   └── README.md
│   │   ├── cpp/
│   │   │   └── README.md
│   │   ├── markdown/
│   │   │   └── README.md
│   │   ├── python/
│   │   │   └── README.md
│   │   └── rust/
│   │       ├── crates/
│   │       │   └── example_crate/
│   │       │       ├── src/
│   │       │       │   └── lib.rs
│   │       │       └── Cargo.toml
│   │       ├── Cargo.toml
│   │       ├── README.md
│   │       └── rustfmt.toml
│   ├── cybersecurity/
│   │   ├── index.rst
│   │   └── org_cybsec_requirements.rst
│   ├── functionalsafety/
│   │   ├── index.rst
│   │   └── org_fusa_requirements.rst
│   ├── policies/
│   │   ├── cybersecurity.rst
│   │   ├── quality.rst
│   │   └── safety.rst
│   └── index.rst
├── organisation/strategy/
│   ├── roadmap.rst
│   └── strategy.rst
├── organisation/tools/
│   ├── index.rst
│   ├── policy.rst
│   └── tool_qualification_requirements.rst
├── organisation/verification/
│   └── iso29119/
│       ├── policy/   (empty)
│       ├── strategy/
│       │   └── product-verification-strategy.rst
│       ├── index.rst
│       └── organizational_requirements.rst
├── source/
│   ├── c/
│   │   ├── include/
│   │   │   ├── communication/
│   │   │   │   └── router.h.c
│   │   │   └── example.h
│   │   ├── src/
│   │   │   ├── communication/
│   │   │   │   └── router.c
│   │   │   └── example.c
│   │   ├── tests/
│   │   │   ├── communication/
│   │   │   │   └── test_router.c
│   │   │   └── CMakeLists.txt
│   │   ├── .clang-format
│   │   ├── CMakeLists.txt
│   │   └── README.md
│   ├── cpp/
│   │   ├── include/
│   │   │   └── example.hpp
│   │   ├── src/
│   │   │   └── example.cpp
│   │   ├── tests/
│   │   │   └── CMakeLists.txt
│   │   ├── .clang-format
│   │   ├── CMakeLists.txt
│   │   └── README.md
│   ├── markdown/
│   │   └── README.md
│   ├── python/
│   │   ├── src/
│   │   │   └── example_package/
│   │   │       └── __init__.py
│   │   ├── tests/
│   │   │   └── test_example.py
│   │   ├── .ruff.toml
│   │   ├── pyproject.toml
│   │   └── README.md
│   ├── rust/
│   │   ├── crates/
│   │   │   └── example_crate/
│   │   │       ├── src/
│   │   │       │   └── lib.rs
│   │   │       └── Cargo.toml
│   │   ├── Cargo.toml
│   │   ├── README.md
│   │   └── rustfmt.toml
│   └── typescript/
│       ├── src/
│       │   └── index.ts
│       ├── test/
│       │   └── index.test.ts
│       ├── eslint.config.js
│       ├── package.json
│       ├── README.md
│       └── tsconfig.json
├── test/
│   ├── executions/
│   │   ├── .gitkeep
│   │   └── EXEC_BUILD_2026_081.yml
│   ├── test-basis/
│   │   ├── .gitkeep
│   │   └── basis.yml
│   ├── test-cases/
│   │   ├── communication/
│   │   │   └── case_a_001.md
│   │   ├── .gitkeep
│   │   └── index.rst
│   ├── test-conditions/
│   │   ├── .gitkeep
│   │   └── TCOND_STARTUP_001.yml
│   ├── test-design/
│   │   └── .gitkeep
│   ├── test-procedures/
│   │   ├── .gitkeep
│   │   └── PROC_SYS_STARTUP_001.yml
│   ├── test-reports/
│   │   ├── .gitkeep
│   │   └── product-verification-report.rst
│   ├── test-strategy/
│   │   └── product-verification-strategy.rst
│   ├── test-suites/
│   │   ├── .gitkeep
│   │   └── SUITE_RELEASE_SMOKE.yml
│   ├── index.rst
│   └── README.md
├── tools/
│   └── check_orphan_needs.py
├── .gitignore
├── .pre-commit-config.yaml
├── conf.py
├── getting_started.rst
├── index.rst
├── needs_overview.rst
├── qorix-engg.code-workspace
├── README.md
└── STANDARDS.md
```

`(empty)` marks directories that exist but currently hold no tracked
content — `management/exceptions/`, `organisation/common_framework/core lib/`,
`organisation/common_framework/HAL/`, and `organisation/verification/iso29119/policy/`.
They're scaffolded, not yet filled in.

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
- `organisation/tools/` — tool qualification & usage governance (ISO 26262-8
  clause 11, ASPICE SUP.8/SUP.1) — see `organisation/tools/index.rst`.
- `organisation/strategy/`, `organisation/common_framework/` — not yet reviewed as part of
  this documentation pass.
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
- `organisation/common_framework/` and `organisation/strategy/` have not been reviewed for
  correctness as part of this documentation pass.
