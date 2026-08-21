Threat Analysis and Risk Assessment (TARA)
==============================================

Scope
-----

A product-level TARA against ``Needs/Communication`` (message delivery,
subscriber authorization) and ``Needs/Diagnostics`` (service discovery)
would sit here, following ISO/SAE 21434 clause 15.

Nothing is captured yet. In particular, ``TSR_001``'s authorization check
is a safety requirement, not a cybersecurity one — whether an unauthorized
subscriber gaining access is also a security-relevant threat (as opposed to
only a safety hazard) has not been evaluated, and that evaluation is the
natural first entry for this file once it exists.

Pending
-------

- Add a ``threat`` and ``cyber_req`` need type to ``Needs/conf.py``
  (tracked separately — see the open conf.py investigation).
- Identify assets, threat scenarios, and attack paths for the Communication
  and Diagnostics modules.
- Decide whether the authorization-bypass failure mode already flagged in
  this repo's FMEA (``../../safety/analyses/fmea``) is also a security
  threat, and if so, link the two.
