Risks
=====

Organizational and project risks, tracked as ``risk`` needs — migrated
in-place from ``risk-register.yml`` (same id, same field values), so each
one is dead-link-checked and queryable via ``needtable`` instead of
living outside the build.

.. risk:: Toolchain migration to enterprise CI/CD platform unavailable
   :id: RISK_001
   :likelihood: medium
   :impact: low
   :mitigation: Track as a documented gap in README; revisit when enterprise/cicd-platform exists.

   Toolchain migration to the enterprise-wide CI/CD platform is not yet
   available; workflows are self-contained.

.. needtable::
   :types: risk
   :columns: id, title, likelihood, impact
   :style: table
