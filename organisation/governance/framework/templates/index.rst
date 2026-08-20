Deliverable Templates
=========================

The "Template" element of each side's Guidance Set in :doc:`../process_metamodel`
is a category label on the diagram, not a file. These three are the actual
templates it refers to — the canonical, copyable form of the ``feat`` /
``comp`` / ``unit`` directives registered in ``Needs/conf.py`` (a separate
Sphinx project — see the root :doc:`../../../../index`). Directive names, id
prefixes, and required fields below match that registration exactly; they
are shown as literal text, not live directives, since this build's own
``conf.py`` does not know those directive types.

Feature template
-----------------

.. code-block:: rst

   .. feat:: <Feature Name>
      :id: FEAT_<MODULE>_<NNN>
      :status: draft
      :links: SYS_<NNN>
      :standard: ASPICE SWE.1 / ISO 15288 6.4.3

      <Non-empty description of the feature-level requirement.>

Component template
--------------------

.. code-block:: rst

   .. comp:: <Component Name>
      :id: COMP_<MODULE>_<NNN>
      :status: draft
      :links: FEAT_<MODULE>_<NNN>
      :standard: ASPICE SWE.2 / ISO 15288 6.4.4

      <Non-empty description of the architectural design element.>

Unit template
--------------

.. code-block:: rst

   .. unit:: <Unit Name>
      :id: UNIT_<MODULE>_<NNN>
      :status: draft
      :links: COMP_<MODULE>_<NNN>
      :standard: ASPICE SWE.3 / ISO 15288 6.4.5

      <Non-empty description of the detailed-design element — a
      function, class, or module.>

Populated examples
--------------------

For each template applied to a real module, see ``needs/systemslifecycle/index.rst``,
``needs/communication/feature/index.rst``,
``needs/communication/component/index.rst``, and
``needs/communication/component/unit design/units.rst``.
