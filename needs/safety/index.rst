Safety (ISO 26262)
====================

The functional safety chain — Safety Goal → Functional Safety Requirement →
Technical Safety Requirement — is not covered by ASPICE or ISO 15288 on
its own. It's kept in this same "all needs linked in one space" graph so a
technical safety requirement can link directly into the sys/feat/comp/unit
chain (see ``tsr_001`` in :doc:`technical_safety_requirements`, which links
into ``comp_a_001``).

Each stage of the chain is its own register — one file per artifact type,
not one file per need — so the count of safety goals, FSRs, and TSRs can
each grow independently.

.. toctree::
   :maxdepth: 1

   safety_goals
   functional_safety_requirements
   technical_safety_requirements
   analyses/index
