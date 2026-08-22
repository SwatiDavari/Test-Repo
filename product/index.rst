Product / Program
=====================

Product- and program-level content for this repo: published docs,
project management records, architecture, product verification/testing,
per-language source scaffolding, and this repo's own traceability needs
(``org_req``/``risk``/``problem``/``change``/``exception``/``tool``/
``infra``/``decision`` — see ``needs_types_definition.rst``). Added
2026-08-21 to collapse what used to be separate top-level sidebar
entries (``management``, a broken ``integration test`` reference) into
one "Product / Program" entry with everything nested underneath as
collapsible sub-menus, the same pattern used for "Organization".

See :doc:`known_gaps` for divergences between this structure and the
request it was built from.

.. toctree::
   :caption: Docs
   :maxdepth: 1

   /doc/index

.. toctree::
   :caption: Project Management
   :maxdepth: 1

   /management/index

.. toctree::
   :caption: Architecture
   :maxdepth: 1

   architecture/index

.. toctree::
   :caption: Product Verification
   :maxdepth: 1

   /testing/index

.. toctree::
   :caption: Source
   :maxdepth: 1

   /source/index

.. toctree::
   :caption: Needs
   :maxdepth: 1

   /needs_types_definition
   Needs <needs_redirect>

.. toctree::
   :hidden:

   known_gaps
