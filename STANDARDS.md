# Standards crosswalk

What each folder corresponds to in ISO/IEC/IEEE 29119 (software testing), ISO/IEC/IEEE 15288 (system/software life cycle processes), ISO 26262 (automotive functional safety), and Automotive SPICE (ASPICE, process assessment model). None of these standards define a folder layout — they define processes and work products. This maps this repo's folders to the *terminology* those standards use for the content that lives there, so a reviewer familiar with any one of them can find their way around.

## Needs/ — requirements, architecture, design, and safety traceability

| Folder / need type | ASPICE process | ISO 15288 process | ISO 26262 |
|---|---|---|---|
| `sys/` (`sys` needs) | SYS.2 System Requirements Analysis, SYS.3 System Architectural Design | 6.4.3 System/Software Requirements Definition | — |
| `mod_*/feat/` (`feat` needs) | SWE.1 Software Requirements Analysis | 6.4.3 System/Software Requirements Definition | — |
| `mod_*/comp/` (`comp` needs) | SWE.2 Software Architectural Design | 6.4.4 Architecture Definition | — |
| `mod_*/unit/` (`unit` needs) | SWE.3 Software Detailed Design and Unit Construction | 6.4.5 Design Definition | — |
| `safety/` (`sg` needs) | — | 6.3.4 Risk Management (technical management process) | Part 3 clause 6 — Hazard Analysis and Risk Assessment (HARA), Safety Goal |
| `safety/` (`fsr` needs) | — | — | Part 3 clause 8 — Functional Safety Concept |
| `safety/` (`tsr` needs) | — | — | Part 4 clause 6 — Technical Safety Concept; Part 6 — Software Safety Requirements |

Every need in `safety/` links either up to a `sys`/`feat` need or down into a `comp`/`unit` need (see `TSR_001` linking into `COMP_A_001`), because ISO 26262 doesn't replace the ASPICE requirements chain — it adds a safety-integrity layer on top of it. A safety case built from this graph is only as complete as ISO 26262 Part 2's confirmation measures require (confirmation review, functional safety audit, functional safety assessment) — those review artifacts aren't modeled here as needs; they'd be records under `doc/reference/` or a dedicated safety-case document, not traceability nodes.

## source/ — implementation

| Folder | ASPICE process | ISO 15288 process |
|---|---|---|
| `source/<lang>/` | SWE.3 Software Detailed Design and Unit Construction (the construction half) | 6.4.6 Implementation |
| `source/<lang>/tests/` (unit-level) | SWE.4 Software Unit Verification | 6.4.8 Verification |

## test/ — verification and validation

| Folder | ISO 29119-3 document type | ASPICE process |
|---|---|---|
| `plans/` | Level Test Plan | SWE.4/SWE.5/SWE.6, SYS.4/SYS.5 (planning) |
| `cases/<mod>/` | Level Test Case (Test Case Specification) | SWE.4/SWE.5/SWE.6 |
| `suites/<mod>/` | Test Procedure Specification | SWE.5/SWE.6, SYS.4/SYS.5 |
| `runs/<mod>/` | Level Test Log (Test Execution Log) | SWE.5/SWE.6 (execution records) |
| `reports/<mod>/` | Test Completion Report | SWE.6/SYS.5 (qualification reporting) |
| `incidents/` | Incident Report | SUP.9 Problem Resolution Management |

`test/` as a whole is what ISO 15288 calls out as the **Verification Process** (6.4.8, "did we build it right" — traces to `comp`/`unit`) and the **Validation Process** (6.4.11, "did we build the right thing" — traces to `sys`/`feat`); which folder content serves which depends on what level the test case covers, not on the folder itself.

## doc/ — published documentation

ISO 15288 doesn't name specific document types (that's 29119's and ASPICE's job); it calls this class of output the **Information Management Process** (6.3.6, at the technical management level) and, for released artifacts, output of the **Transition Process** (6.4.9).

| Folder | Closest standard term |
|---|---|
| `manuals/` | ASPICE SUP.7 Documentation (operator/user documentation) |
| `tutorials/` | ASPICE SUP.7 Documentation |
| `reference/` | ASPICE SUP.7 Documentation; also where ISO 26262 confirmation-measure records (review minutes, audit reports) belong if you don't want them as `Needs/safety` traceability nodes |
| `release_notes/` | ISO 15288 6.4.9 Transition Process (release output) |
| `errata/` | ASPICE SUP.9 Problem Resolution Management (published-doc corrections, not code defects — those go in `test/incidents/`) |

## Process-level folders (not artifact folders)

Some ASPICE/ISO 15288 processes don't produce a work product that lives in this tree at all — they govern *how* the tree is used, not what's in it: MAN.3 Project Management, MAN.5 Risk Management, SUP.1 Quality Assurance, SUP.8 Configuration Management (largely `git` itself plus branch/tag policy), SUP.10 Change Request Management. If your organization tracks these formally, they typically live in a project-management tool (Jira, Polarion) rather than as files here — nothing in this repo layout should be read as claiming to cover them.

## What's deliberately not modeled

ISO 26262's Part 5 (hardware) and Part 8 supporting processes (tool qualification, proven-in-use argument, dependent failure analysis) have no folder here — this sample is software-only, matching the slide it's built from. If `ara_score` has hardware-adjacent scope, that needs its own layer, not a forced fit into `source/`.
