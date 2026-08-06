Safety (ISO 26262)
====================

The functional safety chain — Safety Goal → Functional Safety Requirement →
Technical Safety Requirement — is not covered by ASPICE or ISO 15288 on
its own. It's kept in this same "all needs linked in one space" graph so a
technical safety requirement can link directly into the sys/feat/comp/unit
chain (see ``TSR_001`` below, which links into ``COMP_A_001``).

.. toctree::
   :maxdepth: 1

   sg_001
   fsr_001
   tsr_001
   analyses/index
