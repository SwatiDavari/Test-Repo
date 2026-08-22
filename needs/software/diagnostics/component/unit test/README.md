# unit test

Unit-level test artifacts for the `diagnostics` module, cross-referenced to ISO/IEC/IEEE 29119-3 document types and ASPICE SWE.4 (Software Unit Verification). Full crosswalk in `../../../../../STANDARDS.md`.

This is a **unit-level** folder — scoped to verifying individual units under `needs/software/diagnostics/component/unit design/` (e.g. `unit_z_001`) in isolation. It intentionally does not repeat artifact types that already exist once, at the appropriate broader scope, under the root `testing/` folder:

- **not duplicated here**: `testbasis/` (source material is project-wide, not per unit), `teststrategy/` (one product-verification strategy already covers all levels — see `testing/test strategy/`), `testsuites/` (groupings span multiple test levels, not a single unit), `executions/` (execution logs are tied to system-level build/suite runs, not individual units).
- **kept here, scoped to this unit**:
  - `test conditions/` — **Test Condition** (29119-3). Entry condition(s) that must hold before a unit test case can run.
  - `test design/` — **Test Design Specification** (29119-3). Currently scaffolded — how `test cases/` would be derived from `unit_z_001`'s design.
  - `test cases/` — **Test Case Specification** (29119-3 Level Test Case). Individual unit test case definitions, linked back to the unit via a `Covers:` reference.
  - `test procedures/` — **Test Procedure Specification** (29119-3). Steps to execute each unit test case.
  - `test reports/` — **Test Completion Report** (29119-3). Pass/fail summary for this unit's test cases.

This module has no `test summary/` subfolder — unlike `communication/component/unit test/` above, no rollup-summary content has been started here yet.

Defects found during unit test execution are filed at the project level (see `STANDARDS.md`'s note on incident tracking), not duplicated per unit.
