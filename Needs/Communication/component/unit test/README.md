# unit test

Unit-level test artifacts for the `communication` module, cross-referenced to ISO/IEC/IEEE 29119-3 document types and ASPICE SWE.4 (Software Unit Verification). Full crosswalk in `../../../STANDARDS.md`.

This is a **unit-level** folder — scoped to verifying individual units under `Needs/communication/unit design/` (e.g. `UNIT_A_001`) in isolation. It intentionally does not repeat artifact types that already exist once, at the appropriate broader scope, under the root `integration test/` folder:

- **not duplicated here**: `testbasis/` (source material is project-wide, not per unit), `teststrategy/` (one product-verification strategy already covers all levels — see `integration test/teststrategy/`), `testsuites/` (groupings span multiple test levels, not a single unit), `executions/` (execution logs are tied to system-level build/suite runs, not individual units).
- **kept here, scoped to this unit**:
  - `test cases/` — **Test Case Specification** (29119-3 Level Test Case). Individual unit test case definitions, linked back to the unit via a `Covers:` reference.
  - `test design/` — **Test Design Specification** (29119-3). Currently scaffolded — how `test cases/` would be derived from `UNIT_A_001`'s design.
  - `test reports/` — **Test Completion Report** (29119-3). Pass/fail summary for this unit's test cases.
  - `test summary/` — Rollup summary of unit-test results across `test cases/`. Currently scaffolded (`metrics/` has no content yet).

This module has no `test conditions/` or `test procedures/` subfolder — unlike `diagnostics/unit test/` below, `UNIT_A_001`'s test case has no entry-condition or multi-step-procedure content defined yet, so those folders were not created here.

Defects found during unit test execution are filed at the project level (see `STANDARDS.md`'s note on incident tracking), not duplicated per unit.
