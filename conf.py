# Configuration file for Sphinx + Sphinx-Needs
# Repo: test_repo (ara_score) — root-level project docs.
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
# only what test_repo's own root-level content actually uses.

project = "test_repo (ara_score)"
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
                "ISO/SAE 21434 Clause 5 / ASPICE org-level / ISO 29119 org-level"),
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
}

needs_id_required = True
needs_id_regex = r"^[A-Z]+_[A-Za-z0-9_]+"
needs_report_dead_links = True
