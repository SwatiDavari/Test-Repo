Qorix Engineering Processes
===========================

This is the root-level documentation project for Qorix Engineering Processes. It covers
organizational governance and project process; the product traceability
graph (system/feature/component/unit requirements, safety chain) lives in
``needs/`` as a **separate** Sphinx project — build it independently from
inside ``needs/`` (``sphinx-build -b html . _build``). See ``STANDARDS.md``
for how each folder maps onto ASPICE / ISO 15288 / ISO 26262 / ISO 29119
terminology. Published documentation lives under ``doc/`` (``release_notes/``,
``errata/`` — see ``doc/README.md``); as of 2026-08-21 this is real,
built Sphinx content (``myst_parser`` registered for the Markdown release
notes), not plain unbuilt Markdown as before. The product/safety user
manuals that used to live under ``doc/manuals/`` moved to
``needs/user_guide/`` — see that page for why.


See :doc:`changelog` for the dated history of structural and theme changes to this documentation site.

.. toctree::
   :maxdepth: 1

   getting_started
   organisation/index
   product/index
   decision records/decision_register
   changelog
