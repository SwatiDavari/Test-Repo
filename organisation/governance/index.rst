Organizational Governance
=============================

Organization-level requirements and policies — prerequisites that must
exist before any product-level work (safety, cybersecurity, quality) can
be considered valid under the corresponding standard. Per-standard detail
requirements live one folder down; policy statements (the "why", not the
detailed "shall" requirements) live under ``policies/``.

Per-standard organizational requirements: :doc:`aspice/index`,
:doc:`cybersecurity/index`, :doc:`functionalsafety/index`,
:doc:`quality/index`, :doc:`systemslifecycle/index`.

Policies: :doc:`policies/safety`, :doc:`policies/cybersecurity`,
:doc:`policies/quality`.

.. note::
   All of the pages above are listed directly, flat, in the root
   sidebar's "Organizational Governance" section rather than nested under
   this page. Furo (this project's theme) always renders its sidebar at
   full depth regardless of any toctree's ``:maxdepth:`` — the only way
   to avoid multi-level expandable nesting in the sidebar is to not
   declare that nesting in a toctree at all, so each page here links to
   its children in prose instead.
