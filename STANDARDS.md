# Standards crosswalk

What each folder corresponds to in ISO/IEC/IEEE 29119 (software testing), ISO/IEC/IEEE 15288 (system/software life cycle processes), ISO 26262 (automotive functional safety), and Automotive SPICE (ASPICE, process assessment model). None of these standards define a folder layout — they define processes and work products. This maps this repo's folders to the *terminology* those standards use for the content that lives there, so a reviewer familiar with any one of them can find their way around.

## Needs/ — requirements, architecture, design, and safety traceability

| Folder / need type | ASPICE process | ISO 15288 process | ISO 26262 |
|---|---|---|---|
| `systemslifecycle/` (`sys` needs, e.g. `sys_001.rst`) | SYS.2 System Requirements Analysis, SYS.3 System Architectural Design | 6.4.3 System/Software Requirements Definition | — |
| `<module>/feature/` (`feat` needs, e.g. `communication/feature/feat_a_001.rst`, `diagnostics/feature/feat_z_001.rst`) | SWE.1 Software Requirements Analysis | 6.4.3 System/Software Requirements Definition | — |
| `<module>/component/` (`comp` needs, e.g. `communication/component/comp_a_001.rst`, `diagnostics/component/comp_z_001.rst`) | SWE.2 Software Architectural Design | 6.4.4 Architecture Definition | — |
| `<module>/unit design/` (`unit` needs, e.g. `communication/unit design/unit_a_001.rst`, `diagnostics/unit design/unit_z_001.rst`) | SWE.3 Software Detailed Design and Unit Construction | 6.4.5 Design Definition | — |
| `functionalsafety/` (`sg` needs, e.g. `sg_001.rst`) | — | 6.3.4 Risk Management (technical management process) | Part 3 clause 6 — Hazard Analysis and Risk Assessment (HARA), Safety Goal |
| `functionalsafety/` (`fsr` needs, e.g. `fsr_001.rst`) | — | — | Part 3 clause 8 — Functional Safety Concept |
| `functionalsafety/` (`tsr` needs, e.g. `tsr_001.rst`) | — | — | Part 4 clause 6 — Technical Safety Concept; Part 6 — Software Safety Requirements |

`<module>/` today is `communication/` and `diagnostics/` — the two live modules under `Needs/`. Every need in `functionalsafety/` links either up to a `sys`/`feat` need or down into a `comp`/`unit` need (see `TSR_001` linking into `COMP_A_001`), because ISO 26262 doesn't replace the ASPICE requirements chain — it adds a safety-integrity layer on top of it. A safety case built from this graph is only as complete as ISO 26262 Part 2's confirmation measures require (confirmation review, functional safety audit, functional safety assessment) — those review artifacts aren't modeled here as needs; they'd be records under `doc/manuals/` (or a dedicated safety-case document), not traceability nodes.

## source/ — implementation

| Folder | ASPICE process | ISO 15288 process |
|---|---|---|
| `source/<lang>/` | SWE.3 Software Detailed Design and Unit Construction (the construction half) | 6.4.6 Implementation |
| `source/<lang>/tests/` (unit-level) | SWE.4 Software Unit Verification | 6.4.8 Verification |

## test/ — verification and validation

| Folder | ISO 29119-3 document type | ASPICE process |
|---|---|---|
| `testbasis/` | Test Basis (the source material a test is derived from, e.g. `basis.yml`) | SWE.4/SWE.5/SWE.6, SYS.4/SYS.5 (planning) |
| `teststrategy/` | Test Plan / Level Test Strategy (e.g. `product-verification-strategy.rst`) | SWE.4/SWE.5/SWE.6, SYS.4/SYS.5 (planning) |
| `testconditions/` | Test Condition (e.g. `TCOND_STARTUP_001.yml`) | SWE.4/SWE.5/SWE.6 |
| `testdesign/` | Test Design Specification (currently scaffolded, no content yet) | SWE.4/SWE.5/SWE.6 |
| `testcases/<module>/` | Level Test Case (Test Case Specification, e.g. `testcases/communication/case_a_001.md`) | SWE.4/SWE.5/SWE.6 |
| `testprocedures/` | Test Procedure Specification (e.g. `PROC_SYS_STARTUP_001.yml`) | SWE.5/SWE.6, SYS.4/SYS.5 |
| `testsuites/` | Test Suite grouping (e.g. `SUITE_RELEASE_SMOKE.yml`) | SWE.5/SWE.6, SYS.4/SYS.5 |
| `executions/` | Level Test Log (Test Execution Log, e.g. `EXEC_BUILD_2026_081.yml`) | SWE.5/SWE.6 (execution records) |
| `testreports/` | Test Completion Report (e.g. `product-verification-report.rst`) | SWE.6/SYS.5 (qualification reporting) |

There is currently no `incidents/`-equivalent folder under `test/` — published-doc corrections and defect tracking are not yet modeled here; see "Process-level folders" below for where that would live once it is. `test/` as a whole is what ISO 15288 calls out as the **Verification Process** (6.4.8, "did we build it right" — traces to `comp`/`unit`) and the **Validation Process** (6.4.11, "did we build the right thing" — traces to `sys`/`feat`); which folder content serves which depends on what level the test case covers, not on the folder itself.

## doc/ — published documentation

ISO 15288 doesn't name specific document types (that's 29119's and ASPICE's job); it calls this class of output the **Information Management Process** (6.3.6, at the technical management level) and, for released artifacts, output of the **Transition Process** (6.4.9).

| Folder | Closest standard term |
|---|---|
| `manuals/` | ASPICE SUP.7 Documentation (operator/user documentation; includes `manuals/safety/safety_user_manual.rst` and the `_pdf_template/` used to render it) |
| `release_notes/` | ISO 15288 6.4.9 Transition Process (release output, e.g. `v0.1.0.md`) |
| `errata/` | ASPICE SUP.9 Problem Resolution Management (published-doc corrections, not code defects — see the `test/` note above on where defect tracking would live) |

`tutorials/` and `reference/` do not exist under `doc/` yet — only `errata/`, `manuals/`, and `release_notes/` are present on disk today. If those two are still intended, add them when there's content to put in them rather than carrying empty placeholders.

## organisation/tools/ — tool qualification and usage governance

Organization-level policy and requirements about tools, not the tools themselves — actual scripts live in `tools/` (repo root), actual CI/CD in `.github/workflows/`, actual dev-environment config in `.vscode/`.

| Folder / file | ASPICE process | ISO 26262 |
|---|---|---|
| `organisation/tools/policy.rst` | SUP.1 Quality Assurance, SUP.8 Configuration Management (policy statement) | Part 8 clause 11 — Confidence in the Use of Software Tools (policy statement) |
| `organisation/tools/tool_qualification_requirements.rst` (`org_req` needs) | SUP.8 Configuration Management (tool register, version pinning); SUP.1 Quality Assurance (re-verification on change) | Part 8 clause 11.4.2 (Tool Identification), 11.4.5-11.4.7 (Tool Confidence Level determination) |

## Process-level folders (not artifact folders)

Some ASPICE/ISO 15288 processes don't produce a work product that lives in this tree at all — they govern *how* the tree is used, not what's in it: MAN.3 Project Management, MAN.5 Risk Management, SUP.8 Configuration Management beyond tool version pinning (branch/tag policy — largely `git` itself), SUP.9 Problem Resolution Management (formal incident tracking beyond `test/incidents/`), SUP.10 Change Request Management. If your organization tracks these formally, they typically live in a project-management tool (Jira, Polarion) rather than as files here — nothing in this repo layout should be read as claiming to cover them.

## What's deliberately not modeled

ISO 26262's Part 5 (hardware) and Part 8 supporting processes beyond tool qualification (proven-in-use argument, dependent failure analysis) have no folder here — this sample is software-only, matching the slide it's built from. If `Qorix Engineering Processes` has hardware-adjacent scope, that needs its own layer, not a forced fit into `source/`.
