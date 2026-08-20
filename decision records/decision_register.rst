Decision Records
=====================

Architecture/engineering decision records for this organization, satisfied
as ``decision`` needs (see ``conf.py``'s ``needs_types``) so each one is
dead-link-checked and queryable via ``needtable``, the same treatment
already given to the tool, risk, problem, and change registers.

Migrated in-place from ``0001-static-analysis-tool-selection.md`` (same
content, same status) — same rationale as ``tool_register.rst``'s own
migration from ``tool_register.yml``: a real need built into this Sphinx
project, instead of a Markdown file this build has no parser for (no
``myst_parser``/``recommonmark`` is registered here) and never reads.

.. decision:: Static analysis tool for C/C++ (MISRA C:2017 / ISO 26262)
   :id: DEC_STATIC_ANALYSIS_TOOL_001
   :version: 1.0.0
   :status: proposed
   :links: ORG_CYBERSEC_TOOL_001, ORG_TOOLCFG_001, ORG_TOOLQUAL_001

   **Status:** proposed — under evaluation. No tool has been selected
   yet; this record exists to track the decision, not to announce one.

   **Context**

   ``organisation/governance/coding guidelines/c/c_MISRA2017.md``
   documents MISRA C:2017 as this organization's C coding standard
   (plain Markdown, not part of this Sphinx build — same as ``doc/``
   per this project's own index page, so no ``:doc:`` cross-reference
   is possible to it). Nothing in CI currently enforces it, though:
   :doc:`../organisation/tools/tool_register`'s ``source/c``/``source/cpp``
   entries are CMake (build) and CTest (test execution) only — no static
   analyzer is registered for either language, and
   ``.github/workflows/ci-source-c.yml`` / ``ci-source-cpp.yml`` don't
   run one.

   This is a real, disclosed gap against this organization's own policy:

   - :need:`ORG_CYBERSEC_TOOL_001` requires "a process for qualifying and
     managing the tools used to support cybersecurity activities (e.g.,
     static analysis, fuzzing, vulnerability scanning)."
   - :need:`ORG_TOOLCFG_001` and :need:`ORG_TOOLQUAL_001` require version
     pinning and a determined Tool Confidence Level for any tool used in
     a safety-relevant workflow — neither can be satisfied for a static
     analyzer that isn't registered yet.
   - :doc:`../organisation/tools/policy` treats tool qualification
     (ISO 26262-8 clause 11) as a prerequisite for trusting any tool's
     output on safety-relevant work — relevant here since ``source/c``
     is where the MISRA C:2017 guideline, and any eventual
     ASIL-classified component, would live.

   Two commercial options are on the table: Parasoft (C/C++test) and
   Coverity (now Black Duck Coverity, formerly a Synopsys product).

   **Decision drivers**

   - MISRA C:2017 rule coverage for C, ideally also MISRA C++ for
     ``source/cpp``.
   - A formal ISO 26262 tool-qualification kit or pre-existing
     certification, since :need:`ORG_TOOLQUAL_001` will eventually
     require a TCL determination for whichever tool is registered.
   - Fit with the existing CI shape (``ci-source-c.yml``,
     ``ci-source-cpp.yml``, currently CMake/CTest-only, GitHub
     Actions-based).
   - License/cost model — both are commercial, seat- or CI-node-licensed
     tools; neither has a meaningful free tier for this use case (unlike
     ruff, clippy, eslint already in :doc:`../organisation/tools/tool_register`).

   **Options considered**

   *Option A — Parasoft C/C++test*

   - Parasoft states "100% coverage of MISRA, AUTOSAR C++ 14, CERT, and
     other coding standards" in its static analysis capability.
   - States its "C/C++ solutions for static analysis, unit testing, and
     code coverage have been TÜV SÜD certified for ISO 26262 at all ASIL
     levels," and offers a tool qualification kit that "automates the
     process of assessing and validating" the tool for that use.
   - Also covers unit testing and code coverage (C/C++test CT), which
     could eventually replace or sit alongside the plain CTest entry
     already registered, not just add a new static-analysis line.

   *Option B — Coverity (Black Duck Coverity)*

   - Lists MISRA C (2004, 2012, 2023, 2025) and MISRA C++ (2008, 2023)
     support explicitly — broader MISRA-version coverage than confirmed
     for Option A.
   - TÜV SÜD-certified under IEC 61508-3, qualified up to ASIL D under
     ISO 26262 and DO-178C Level A, with a "Qualification Kit (Q-Kit)"
     for safety-critical configuration.
   - Broader multi-language reach (22 languages per its own claims) —
     relevant only if static analysis coverage were ever extended beyond
     ``source/c``/``source/cpp`` to ``source/python``, ``source/rust``,
     or ``source/typescript``, none of which currently lack a linter
     already (ruff, clippy, eslint are all registered and free).
   - Note the ownership change: Coverity was a Synopsys product; as of
     this evaluation it is sold and supported as **Black Duck Coverity**,
     not Synopsys — relevant for whoever runs procurement, since old
     Synopsys pricing/support pages are stale.

   **Decision outcome**

   Not yet decided. Both options carry a real TÜV SÜD / IEC 61508-3 /
   ISO 26262 certification claim and MISRA C coverage claim per their own
   vendor material — a side-by-side technical evaluation (actual
   MISRA C:2017 rule-set coverage against this repo's ``source/c``,
   license cost at this org's likely seat/node count, and CI integration
   effort for ``ci-source-c.yml``/``ci-source-cpp.yml``) has not been
   done and is the next step before either is registered in
   :doc:`../organisation/tools/tool_register`.

   **Consequences if left undecided**

   :need:`ORG_CYBERSEC_TOOL_001`, :need:`ORG_TOOLCFG_001`, and
   :need:`ORG_TOOLQUAL_001` remain unsatisfied for C/C++ static analysis
   specifically — this mirrors the already-disclosed gap in
   :doc:`../organisation/tools/tool_register` (no static analyzer
   registered for ``source/c``/``source/cpp`` today) rather than
   creating a new one.

   **Sources:** `ISO 26262 Compliance & Tools — Parasoft
   <https://www.parasoft.com/solutions/iso-26262/>`_,
   `C/C++test — Parasoft
   <https://www.parasoft.com/products/parasoft-c-ctest/>`_,
   `Coverity Static Analysis — Black Duck
   <https://www.blackduck.com/static-analysis-tools-sast/coverity.html>`_

.. needtable::
   :types: decision
   :columns: id, title, status
   :style: table
