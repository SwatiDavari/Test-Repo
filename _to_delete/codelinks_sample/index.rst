Code Links Sample — source/c
===============================

.. note::
   This is a **sample**, scoped to ``source/c`` only, demonstrating what
   real (not free-text) traceability from implementation back to a design
   need looks like using `sphinx-codelinks
   <https://pypi.org/project/sphinx-codelinks/>`_. See ``README.md`` in
   this folder for what it does and doesn't cover, and why it's a
   separate Sphinx project rather than a change to the root project's own
   ``conf.py``.

What this replaces
---------------------

``source/c/include/communication/serializer.h`` has carried this comment
since it was written::

    /* Implements UNIT_A_001 (Proxy Serialization Unit) —
     * needs/communication/component/unit design/unit_a_001.rst:
     * "serialization and deserialization of messages within the proxy
     * layer." */

That's a real, correct claim — but it's prose. Nothing dead-link-checks
it, nothing notices if ``UNIT_A_001`` is renamed or retired, and there's
no queryable link from the need's own page back to *which lines*
implement it. ``source/c/src/communication/serializer.c`` now carries two
real markers instead, one per function:

.. code-block:: c

   // @Serialize a message into wire format, IMPL_C_SERIALIZER_ENCODE, impl, [UNIT_A_001]
   size_t serializer_encode(...) { ... }

   // @Deserialize a message from wire format, IMPL_C_SERIALIZER_DECODE, impl, [UNIT_A_001]
   int serializer_decode(...) { ... }

Each one becomes a real ``impl`` need at build time, below, with a real
``:links: UNIT_A_001`` — dead-link-checked exactly like every other link
in this repo's needs graphs.

The extracted needs
-----------------------

.. src-trace::
   :project: source_c
   :directory: .

Traceability views
----------------------

.. needtable::
   :types: impl
   :columns: id, title, links

.. needflow::
   :types: impl, unit
   :link_types: links
