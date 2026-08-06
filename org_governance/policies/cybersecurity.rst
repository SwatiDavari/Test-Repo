Cybersecurity Policy
=======================

Statement
---------

This organization maintains a Cybersecurity Management System (CSMS) per
ISO/SAE 21434 Clause 5, and treats cybersecurity as a continuous
organizational responsibility rather than a one-time product gate —
covering governance, culture, information sharing, tool management,
information security management, audit, and continuous monitoring.

The detailed, individually-tracked requirements that implement this policy
live in :doc:`../iso21434/org_cybsec_requirements`.

Scope
-----

Applies to every project developing or maintaining a road vehicle
system, component, or software with cybersecurity relevance.

Relationship to product-level TARA
--------------------------------------

This policy governs the organization's CSMS. Product-level threat
analysis and risk assessment for test_repo's own features lives in
``Needs/cybersecurity/tara/`` — currently scaffolding only, since
``Needs/conf.py`` does not yet register the ``threat``/``cyber_req``
need types required to author it as real sphinx-needs content.
