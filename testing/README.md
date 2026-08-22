# test

Test automation artifacts, cross-referenced to ISO/IEC/IEEE 29119-3 document types and ASPICE test processes (SYS.4/SYS.5, SWE.4/SWE.5/SWE.6). Full crosswalk in `../STANDARDS.md`.

> **2026-08-22:** the folder names below previously didn't match what's on disk (`plans/`, `cases/<mod>/`, `suites/<mod>/`, `runs/<mod>/`, `reports/<mod>/`, `incidents/` were never actually created under `testing/` — the real folders use `test <noun>/` naming). Corrected below to the folders that actually exist. Four empty, untracked `architecture/`, `component/`, `feature/`, `unit/` folders that had been scaffolded directly under `testing/` (duplicating the `needs/software/<module>/` hierarchy with nothing in them, and never referenced from any index or doc) were moved to `_to_delete/` at the repo root pending manual delete — see that folder's own README. Separately, `test basis/basis.yml` had stale placeholder IDs and `test conditions/`/`test procedures/` (referenced by `test cases/index.rst` but never created) are new — both fixed/added in the same pass; see `test cases/index.rst`'s own note for the detail.

- `test basis/` — **Test Basis** (29119-3). `basis.yml` lists the upstream requirement/need IDs this verification effort is checked against.
- `test strategy/` — **Test Plan** (29119-3 Level Test Plan). States scope, entry/exit criteria, and which `Needs` ids product verification covers — see `product-verification-strategy.rst`.
- `test cases/<mod>/` — **Test Case Specification** (29119-3 Level Test Case). Individual test case definitions, linked back to a `Needs` id via a `Covers:` reference in each case file. One subfolder per module (`communication/`, `diagnostics/`).
- `test conditions/` — **Test Condition** (29119-3). Entry condition(s) that must hold before a system-level test case can run.
- `test procedures/` — **Test Procedure Specification** (29119-3). Steps to execute each system-level test case.
- `test design/` — **Test Design Specification** (29119-3). Currently scaffolded, no content yet.
- `test suites/` — **Test Procedure Specification** (29119-3). Groupings/ordering of cases into runnable procedures.
- `test executions/` — **Test Execution Log** (29119-3 Level Test Log). Records of executed runs (timestamped, environment info).
- `test reports/` — **Test Completion Report** (29119-3). Generated pass/fail summary per run.

There is no `incidents/` folder yet — defects aren't currently filed at this level. (Unit-level test artifacts, colocated with each unit's design, live separately under `needs/software/<module>/component/unit test/` and are documented in that folder's own README.)

`test strategy/` and `test cases/`/`test conditions/`/`test procedures/`/`test suites/` are authored by hand; `test executions/`, `test reports/`, and any future incident register are meant to be generated/filed by CI or the tester and should be gitignored except for retained history if you want it in-repo.
