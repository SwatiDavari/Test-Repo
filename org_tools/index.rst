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

``org_tools/`` is where the organization states *which* tools count as
qualified for safety- or cybersecurity-relevant work, and *why* — per
ISO 26262 Part 8 Clause 11 and ASPICE SUP.8/SUP.1.

.. toctree::
   :maxdepth: 1

   policy
   tool_qualification_requirements
   tool_register
