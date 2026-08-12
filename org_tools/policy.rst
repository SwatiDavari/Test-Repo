Tool Usage Policy
====================

Statement
---------

This organization treats tool confidence as a prerequisite for trusting
any output produced by a software tool in the development or verification
chain — a compiler, a static analyzer, Sphinx-Needs' traceability build,
or a CI job's pass/fail verdict. No safety- or cybersecurity-relevant work
product is considered valid on the strength of a tool's output alone
unless that tool's qualification status has been determined first, per
ISO 26262 Part 8 Clause 11 (Confidence in the Use of Software Tools).

The detailed, individually-tracked requirements that implement this
policy live in :doc:`tool_qualification_requirements` (tool
identification/registration, tool confidence level determination, version
pinning, and re-verification on tool change).

Scope
-----

Applies to every tool used in this organization's development,
verification, or traceability chain — build tools (CMake, Cargo,
pytest, npm/tsc), the Sphinx-Needs toolchain that produces this
traceability graph, and the CI runners that execute both.

Ownership
---------

Tool governance is owned at the organization level, not the project
level — a project selects *which* qualified tools it uses and at what
version (see ``ORG_TOOLCFG_001``), but may not introduce an
unregistered or unqualified tool into a safety- or cybersecurity-relevant
chain without first satisfying ``ORG_TOOLREG_001`` and
``ORG_TOOLQUAL_001``.
