Tool Qualification Requirements
====================================

Two organizational requirements referenced by name in
:doc:`tool_register`'s prose (via the ``:need:`` inline role) since that
file was written, but never created — found while re-enabling
cross-project traceability end to end. Both decompose
:need:`ORG_TOOLREG_001` (the register's own existence) into policy this
repo doesn't yet fully satisfy; see each need's body for what's disclosed
as open versus actually done.

.. org_req:: Tool versions are pinned where correctness depends on them
   :id: ORG_TOOLCFG_001
   :version: 1.0.0
   :status: proposed
   :links: ORG_TOOLREG_001
   :standard: ASPICE SUP.8/SUP.9 tool qualification

   The organization shall pin an exact version in CI for any registered
   tool whose output correctness, safety relevance, or reproducibility
   depends on a specific version, and shall disclose which registered
   tools are not yet pinned as an open item in :doc:`tool_register`
   rather than an oversight.

   **Partial, disclosed rather than closed:** most tools in
   :doc:`tool_register` show ``:pinned: no`` today. That's the accurate
   current state, not a gap in this requirement's wording — closing it
   means pinning those tools, not rewriting this need.

.. org_req:: Tool Confidence Level is determined for qualification-relevant tools
   :id: ORG_TOOLQUAL_001
   :version: 1.0.0
   :status: proposed
   :links: ORG_TOOLREG_001
   :standard: ISO 26262-8 clause 11.4.5-11.4.7

   The organization shall determine a Tool Confidence Level (TCL) and a
   qualification status for each registered tool used in a
   safety-relevant workflow, and record both per tool in
   :doc:`tool_register`.

   **Not yet done, disclosed rather than closed:** every tool in
   :doc:`tool_register` shows ``tcl: TBD`` and
   ``qualification_status: not_yet_qualified`` (or
   ``not_applicable_in_repo_tool`` for the one in-repo script). No formal
   TCL determination has been performed for any tool yet.
