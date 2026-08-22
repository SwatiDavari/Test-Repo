System Requirements
=======================

Register of system-level (``sys``) requirements tying the product's
modules together — one file for every system requirement, not one file
per requirement. Add new system requirements here as additional
``.. sys::`` directives.

.. sys:: Inter-application communication and service discovery
   :id: sys_msgdisc_001
   :version: 1.0.0
   :status: proposed
   :standard: ASPICE SYS.2 / ISO 15288 6.4.3 System Requirements Definition

   The system shall provide adaptive application instances with both a
   publish-subscribe messaging capability and a runtime service-discovery
   capability, so instances can exchange messages and locate one another
   without a fixed, build-time wiring of endpoints.

.. note::
   Both ``feat_a_001`` (Communication — Publish-Subscribe Messaging) and
   ``feat_z_001`` (Diagnostics — Service Discovery) declare
   ``:links: sys_msgdisc_001`` — this is their shared system-level parent:
   adaptive application instances need both capabilities to find and
   message each other.
