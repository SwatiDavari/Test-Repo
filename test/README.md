# test

Test automation artifacts, cross-referenced to ISO/IEC/IEEE 29119-3 document types and ASPICE test processes (SYS.4/SYS.5, SWE.4/SWE.5/SWE.6). Full crosswalk in `../STANDARDS.md`.

- `plans/` — **Test Plan** (29119-3 Level Test Plan). One file per module, states scope, entry/exit criteria, and which `Needs` ids it covers.
- `cases/<mod>/` — **Test Case Specification** (29119-3 Level Test Case). Individual test case definitions, linked back to a `Needs` id via a `Covers:` reference in each case file.
- `suites/<mod>/` — **Test Procedure Specification** (29119-3). Groupings/ordering of cases into runnable procedures.
- `runs/<mod>/` — **Test Execution Log** (29119-3 Level Test Log). Records of executed runs (timestamped, environment info).
- `reports/<mod>/` — **Test Completion Report** (29119-3). Generated pass/fail summary per run.
- `incidents/` — **Incident Report** (29119-3). One file per defect found during test execution, not per module — an incident can span modules.

`plans/` and `cases/`/`suites/` are authored by hand; `runs/`, `reports/`, and new `incidents/` entries are meant to be generated/filed by CI or the tester and should be gitignored except for retained history if you want it in-repo.
