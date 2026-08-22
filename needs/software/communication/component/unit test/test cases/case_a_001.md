# Case tc_unit_a_001: Publish/Subscribe dispatch (unit)

Covers: UNIT_A_001

Verifies, at the unit level and in isolation (no process boundary, no
network, no timeout), that the message-dispatch routine delivers a
published payload to exactly the subscriber callback(s) registered on
the matching topic, and does not invoke callbacks registered on other
topics.

This replaces the previous copy of `test/test-cases/communication/case_a_001.md`,
which duplicated the feature-level case (`Covers: feat_a_001`, a real
timeout window across a process boundary) under this unit-test folder.
The feature-level case still lives at the root `test/` — this one is
scoped to the unit alone.
