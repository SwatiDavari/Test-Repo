Tool Governance
=================

Organization-level policy and requirements for the tools used to develop
and verify products under this organization — tool qualification status,
version control, and re-verification triggers.

This is **governance about tools**, not the tools themselves:

- Actual CI scripts live in ``tools/`` (repo root, e.g.
  ``check_orphan_needs.py``).
- Actual CI/CD execution lives in ``.github/workflows/``.
- Actual dev-environment configuration lives in ``.vscode/``.

``organisation/tools/`` is where the organization states *which* tools count as
qualified for safety- or cybersecurity-relevant work, and *why* — per
ISO 26262 Part 8 Clause 11 and ASPICE SUP.8/SUP.1.

See :doc:`policy`, :doc:`tool_qualification_requirements`, and
:doc:`tool_register` (all listed directly in the root sidebar, not
nested under this page — see organisation/governance/index.rst's note
on sidebar flattening).
