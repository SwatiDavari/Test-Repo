Enterprise Architecture Framework
==================================

This page renders the repo/workspace skeleton diagram as a committed, versioned
source file rather than an external screenshot — every change to the
architecture is a reviewable git diff from here on, not a redrawn image.
It depicts this repo's actual current structure: the workspace root, the
``Needs/`` traceability space, the enterprise governance folders, and the
source/test/doc/management clusters. See ``STANDARDS.md`` for how each piece
maps onto ASPICE / ISO 15288 / ISO 26262 / ISO 29119 terminology, and
:doc:`../../org_tools/index` for the tool that qualifies the tools referenced
inside this structure.

.. uml:: enterprise_architecture.puml

This diagram is scoped to *this* repo, not to Eclipse S-CORE's
``process_description`` or any other external consortium process — those are
external standards this repo's projects may additionally tailor against
(see ``STANDARDS.md``), not the source this framework derives from.
