Safety Goals
===============

Register of Safety Goal (``sg``) needs, one HARA-derived goal per
directive — new safety goals are added here, not as new files.

.. sg:: Prevent unauthorized message delivery
   :id: sg_001
   :version: 1.0.0
   :status: proposed
   :asil: ASIL B
   :links: ORG_SMS_001
   :standard: ISO 26262-3 clause 6 (HARA)

   The vehicle function shall not act on messages delivered to an
   application instance that was not an authorized subscriber, as this
   could trigger an unintended actuation.

.. note::
   ``:links: ORG_SMS_001`` — organisation/governance/functionalsafety/
   org_fusa_requirements.rst states that its organizational safety
   management system requirements are prerequisites for any
   product-level safety work (HARA, safety goals, FSR/TSR/SSR); this
   need cites that prerequisite as a real, dead-link-checked link (via
   ``needs_external_needs``, see ``conf.py``), not free-text prose.
