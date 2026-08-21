Cybersecurity (ISO/SAE 21434) — Product Level
=================================================

This folder is the product-level counterpart to
``organisation/governance/cybersecurity/org_cybsec_requirements.rst`` (organizational
CSMS-level clauses). Nothing at product level currently exists in this
repo — no threat, cyber goal, or cyber requirement has been captured
against ``Needs/Communication`` or ``Needs/Diagnostics``.

.. important::
   ``Needs/conf.py`` does not currently register a ``threat`` or
   ``cyber_req`` need type (only ``sys``/``feat``/``comp``/``unit`` and the
   safety ``sg``/``fsr``/``tsr`` chain are registered). This folder is
   structural scaffolding only — real TARA entries can't be authored as
   sphinx-needs directives until those types are added to conf.py. Rather
   than fabricate placeholder threat/requirement IDs that the build can't
   validate, this index states that gap explicitly.

.. toctree::
   :maxdepth: 1

   tara/index
