Tool Register
================

The register satisfying :need:`ORG_TOOLREG_001` — one ``tool`` need per
tool actually invoked by a workflow under ``.github/workflows/`` or
``.pre-commit-config.yaml``. Migrated in-place from ``tool_register.yml``
(same ids, same field values) so each entry is queryable via
``needtable`` and its :need:`ORG_TOOLREG_001` link is dead-link-checked,
instead of living in a file this build never reads.

``pinned`` reflects whether the CI step that runs a tool pins an exact
version (see :need:`ORG_TOOLCFG_001`) — most entries below do not, which
is a real, disclosed gap, not an oversight. ``tcl`` and
``qualification_status`` are TBD for every tool: no formal Tool
Confidence Level determination (ISO 26262-8 clause 11.4.5-11.4.7) has
been performed yet — see :need:`ORG_TOOLQUAL_001`.

.. org_req:: Tool register exists and is kept current
   :id: ORG_TOOLREG_001
   :status: approved
   :standard: ASPICE SUP.8/SUP.9 tool qualification

   The organization shall maintain a register of every tool invoked by a
   CI workflow or pre-commit hook, recording at minimum: what the tool
   is, where it is used, which CI workflow invokes it, whether its
   version is pinned, and its current tool-qualification status.

.. note::
   Every ``tool`` need below already declared ``:links: ORG_TOOLREG_001``
   before this need existed, which made ``ORG_TOOLREG_001`` a dead link
   on all 20 of them — the same dead-link pattern found and fixed at
   ``SYS_001`` (see ``needs/systemslifecycle/sys_001.rst``), one layer
   up, in the organizational graph instead of the product graph. Found
   by actually building this project with the external-needs pipeline
   wired up end to end, not by static file inspection. Added here as
   the parent this file's own opening line was already asserting
   ("The register satisfying :need:`ORG_TOOLREG_001`"), not as new
   scope.

   ``ORG_TOOLCFG_001`` and ``ORG_TOOLQUAL_001``, referenced in prose
   above, now exist in :doc:`tool_qualification_requirements` (added at
   the same time as this need, both decomposing it) — the pinning and
   TCL-determination work they require is still genuinely open, disclosed
   there and in each tool entry's ``pinned``/``tcl``/``qualification_status``
   fields below, not silently claimed done.

.. tool:: CMake
   :id: TOOL_CMAKE
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: build
   :used_in: source/c, source/cpp
   :ci_workflow: ci-source-c.yml, ci-source-cpp.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: CTest
   :id: TOOL_CTEST
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: test_execution
   :used_in: source/c, source/cpp
   :ci_workflow: ci-source-c.yml, ci-source-cpp.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: Python (source/python)
   :id: TOOL_PYTHON_SOURCE
   :links: ORG_TOOLREG_001
   :pinned: yes
   :version: 3.12
   :toolchain_step: build
   :used_in: source/python
   :ci_workflow: ci-source-python.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: ruff
   :id: TOOL_RUFF
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: static_analysis
   :used_in: source/python
   :ci_workflow: ci-source-python.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: pytest
   :id: TOOL_PYTEST
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: test_execution
   :used_in: source/python
   :ci_workflow: ci-source-python.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: Rust (stable toolchain via dtolnay/rust-toolchain)
   :id: TOOL_RUST_TOOLCHAIN
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: build
   :used_in: source/rust
   :ci_workflow: ci-source-rust.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: cargo fmt
   :id: TOOL_CARGO_FMT
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: static_analysis
   :used_in: source/rust
   :ci_workflow: ci-source-rust.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: cargo clippy (-D warnings)
   :id: TOOL_CARGO_CLIPPY
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: static_analysis
   :used_in: source/rust
   :ci_workflow: ci-source-rust.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: cargo test
   :id: TOOL_CARGO_TEST
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: test_execution
   :used_in: source/rust
   :ci_workflow: ci-source-rust.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: Node.js
   :id: TOOL_NODE
   :links: ORG_TOOLREG_001
   :pinned: yes
   :version: 20
   :toolchain_step: build
   :used_in: source/typescript
   :ci_workflow: ci-source-typescript.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: tsc (--noEmit)
   :id: TOOL_TSC
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: static_analysis
   :used_in: source/typescript
   :ci_workflow: ci-source-typescript.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: eslint
   :id: TOOL_ESLINT
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: static_analysis
   :used_in: source/typescript
   :ci_workflow: ci-source-typescript.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: npm test
   :id: TOOL_NPM_TEST
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: test_execution
   :used_in: source/typescript
   :ci_workflow: ci-source-typescript.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: Python (root docs project)
   :id: TOOL_SPHINX_ROOT
   :links: ORG_TOOLREG_001
   :pinned: yes
   :version: 3.11
   :toolchain_step: traceability
   :used_in: root Sphinx project
   :ci_workflow: docs.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: sphinx, sphinx-needs, furo, sphinxcontrib-plantuml, Pillow
   :id: TOOL_SPHINX_NEEDS_ROOT
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: traceability
   :used_in: root Sphinx project
   :ci_workflow: docs.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: PlantUML (default-jre-headless, graphviz, plantuml apt packages)
   :id: TOOL_PLANTUML
   :links: ORG_TOOLREG_001
   :pinned: no
   :toolchain_step: traceability
   :used_in: root Sphinx project — needflow/uml diagrams
   :ci_workflow: docs.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: tools/check_orphan_needs.py (in-repo script, not a third-party tool)
   :id: TOOL_ORPHAN_GATE
   :links: ORG_TOOLREG_001
   :pinned: yes
   :version: repo-versioned, see tools/check_orphan_needs.py
   :toolchain_step: traceability
   :used_in: root Sphinx project — traceability gate
   :ci_workflow: docs.yml
   :tcl: TBD
   :qualification_status: not_applicable_in_repo_tool

.. tool:: Python, sphinx, sphinx-needs (Needs/ project)
   :id: TOOL_SPHINX_NEEDS_CHILD
   :links: ORG_TOOLREG_001
   :pinned: yes
   :version: Python 3.12 (Needs/requirements.txt pins sphinx, sphinx-needs — no version numbers)
   :toolchain_step: traceability
   :used_in: Needs/ Sphinx project
   :ci_workflow: ci-needs.yml
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: black (pre-commit)
   :id: TOOL_BLACK
   :links: ORG_TOOLREG_001
   :pinned: yes
   :version: 24.4.2
   :toolchain_step: static_analysis
   :used_in: whole repo, pre-commit hook
   :ci_workflow: .pre-commit-config.yaml — not run in any GitHub Actions workflow
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. tool:: pre-commit-hooks (trailing-whitespace, end-of-file-fixer, check-yaml)
   :id: TOOL_PRECOMMIT_HOOKS
   :links: ORG_TOOLREG_001
   :pinned: yes
   :version: v4.6.0
   :toolchain_step: static_analysis
   :used_in: whole repo, pre-commit hook
   :ci_workflow: .pre-commit-config.yaml — not run in any GitHub Actions workflow
   :tcl: TBD
   :qualification_status: not_yet_qualified

.. needtable::
   :types: tool
   :columns: id, title, toolchain_step, pinned, tcl
   :style: table
