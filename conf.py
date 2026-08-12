# Configuration file for Sphinx + Sphinx-Needs
# Repo: Qorix Engineering Processes — root-level project docs.
#
# This is a SEPARATE Sphinx project from Needs/conf.py. Needs/ has its own
# conf.py and builds independently (sys/feat/comp/unit + sg/fsr/tsr — the
# product traceability graph). This root project covers everything that
# sits outside Needs/: organization-level requirements (org_req, used under
# org_governance/), plus plain narrative docs (doc/, management/, test/,
# org_verification/, org_strategy/).
#
# NOTE: this file previously contained Test_Dashboard's full conf.py
# (project = "product-x", a needs_types list with sys_req/hazard/threat/
# ssr/cyber_goal/etc., and source_repository pointing at Test_Dashboard's
# GitHub URL). None of that reflected this repo — it's been replaced with
# only what Qorix Engineering Processes root-level content actually uses.

project = "Qorix Engineering Processes"
master_doc = "index"
extensions = ["sphinx_needs", "sphinxcontrib.plantuml"]
html_theme = "furo"

# CRITICAL: without this, `sphinx-build -b html . _build/html` run from the
# repo root (exactly what .github/workflows/docs.yml does) walks into
# Needs/ and tries to parse its sg/fsr/tsr/comp/feat/unit directives using
# THIS conf.py's schema (which only knows org_req) — 9 "Unknown directive
# type" errors, confirmed by testing the exact CI invocation locally.
# Needs/ is a separate Sphinx project with its own conf.py and its own CI
# job (ci-needs.yml, working-directory: Needs) — it must stay excluded here.
exclude_patterns = ["Needs", "_build", "Thumbs.db", ".DS_Store"]

needs_types = [
    dict(directive="org_req", prefix="ORG_", color="#B8003D", style="node",
         title="Organizational Requirement — ISO 26262 Part 2 / "
                "ISO/SAE 21434 Clause 5 / ASPICE org-level / ISO 29119 "
                "org-level / ISO/IEC/IEEE 15288 clause 6.2"),

    # Management registers (management/) and the tool register (org_tools/).
    # Previously each entry lived only in a .yml file this Sphinx build
    # never read (risk-register.yml, problem-register.yml,
    # change-register.yml, tool_register.yml) with an .rst stub pointing at
    # it. Migrated in-place to real needs, one per existing YAML record —
    # same ids, same field values — so each gets dead-link checking and is
    # queryable via needtable instead of living outside the build.
    dict(directive="risk", prefix="RISK_", color="#B71C1C", style="node",
         title="Organizational or Project Risk"),
    dict(directive="problem", prefix="PRB_", color="#D32F2F", style="node",
         title="Problem Report"),
    dict(directive="change", prefix="CR_", color="#5C6BC0", style="node",
         title="Change Request"),
    dict(directive="exception", prefix="EXC_", color="#8E24AA", style="node",
         title="Tailoring Exception — deviation from the org-level process "
                "described in org_governance/framework/process_metamodel"),
    dict(directive="tool", prefix="TOOL_", color="#00838F", style="node",
         title="Qualified Tool — invoked by a CI workflow or pre-commit hook, "
                "per ASPICE SUP.8/SUP.9 tool qualification"),
    dict(directive="infra", prefix="INFRA_", color="#455A64", style="node",
         title="Infrastructure Element — ISO/IEC/IEEE 15288 clause 6.2.2, "
                "outcome (b): infrastructure identified and specified"),
]

# Same treatment as Needs/conf.py: `derives_from` is used inconsistently in
# the org_req content as both a real need ID (e.g. ORG_SMS_001) and a
# free-text external standard-clause citation (e.g. ISO26262_2_5_4_2_1)
# with no matching need. Registering it as a needs_extra_links option would
# fail the dead-link gate on every clause citation. Kept as a free-text
# field instead — same rationale as Needs/conf.py.
needs_fields = {
    "standard": {
        "description": "Standard/clause this need satisfies",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "derives_from": {
        "description": "Upstream ID or external standard clause this "
                        "requirement derives from (free text — not "
                        "dead-link-checked)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "likelihood": {
        "description": "Risk likelihood (from risk-register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "impact": {
        "description": "Risk impact (from risk-register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "mitigation": {
        "description": "Risk mitigation plan (from risk-register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "affected_needs": {
        "description": "Need IDs a problem/change affects, as recorded in "
                        "problem-register.yml / change-register.yml. Kept "
                        "as free text, not a real link — these ids "
                        "(SWR_*, SYSR_*) are illustrative placeholders used "
                        "elsewhere in the repo (see test/test-strategy/) "
                        "and don't resolve to any actual need, so "
                        "registering this as a needs_extra_links option "
                        "would fail the dead-link gate.",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "pinned": {
        "description": "Whether the tool's version is pinned in CI "
                        "(from tool_register.yml: version_pinned)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "version": {
        "description": "Pinned version string, when known "
                        "(from tool_register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "toolchain_step": {
        "description": "build / static_analysis / test_execution / "
                        "traceability (from tool_register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "used_in": {
        "description": "Module(s) or project(s) this tool is used in "
                        "(from tool_register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "ci_workflow": {
        "description": "Workflow file(s) that invoke this tool "
                        "(from tool_register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "tcl": {
        "description": "Tool Confidence Level, ISO 26262-8 clause "
                        "11.4.5-11.4.7 (from tool_register.yml — TBD for "
                        "every tool, no determination made yet)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "qualification_status": {
        "description": "Tool qualification status (from tool_register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "provider": {
        "description": "Who provides/hosts this infrastructure element "
                        "(e.g. GitHub Actions, GitHub Pages, local machine)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "acquisition": {
        "description": "How this infrastructure element was acquired "
                        "(SaaS subscription, self-hosted, checked-in config "
                        "file, etc.) — ISO/IEC/IEEE 15288 clause 6.2.2 "
                        "outcome (c)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "availability_note": {
        "description": "What guarantees availability today, and what "
                        "monitors it — ISO/IEC/IEEE 15288 clause 6.2.2 "
                        "outcome (d). Free text; disclose 'none' rather "
                        "than implying monitoring that doesn't exist.",
        "schema": {"type": "string"},
        "nullable": True,
    },
}

needs_id_required = True
needs_id_regex = r"^[A-Z]+_[A-Za-z0-9_]+"
needs_report_dead_links = True
