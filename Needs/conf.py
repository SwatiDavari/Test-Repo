extensions = ["sphinx_needs"]

project = "ara_score Needs"
master_doc = "index"

# --- Need types = the pptx "Cluster" (glob/Feat/Comp/Unit -> int/req/arc/des),
# each cross-referenced to the standard process/work-product it corresponds
# to. See ../STANDARDS.md for the full crosswalk and rationale. ---
needs_types = [
    dict(directive="sys", prefix="SYS_", color="#BFD8D2", style="node",
         title="System Requirement — ASPICE SYS.2 / ISO 15288 System Requirements Definition"),
    dict(directive="feat", prefix="FEAT_", color="#FEDCD2", style="node",
         title="Feature / Software Requirement — ASPICE SWE.1 / ISO 15288 Requirements Definition"),
    dict(directive="comp", prefix="COMP_", color="#DF744A", style="node",
         title="Component / Software Architecture — ASPICE SWE.2 / ISO 15288 Architecture Definition"),
    dict(directive="unit", prefix="UNIT_", color="#DCB239", style="node",
         title="Unit / Detailed Design — ASPICE SWE.3 / ISO 15288 Design Definition"),

    # ISO 26262 functional safety chain — not covered by ASPICE or ISO 15288
    # on its own; layered onto the same needs graph so a safety requirement
    # can link straight into the sys/feat/comp/unit chain above.
    dict(directive="sg", prefix="SG_", color="#B71C1C", style="node",
         title="Safety Goal — ISO 26262-3 clause 6 (HARA)"),
    dict(directive="fsr", prefix="FSR_", color="#D32F2F", style="node",
         title="Functional Safety Requirement — ISO 26262-3 clause 8"),
    dict(directive="tsr", prefix="TSR_", color="#E57373", style="node",
         title="Technical Safety Requirement — ISO 26262-4 clause 6 / ISO 26262-6"),

    # Upstream-of-sys needs: raw stakeholder/business/operational needs
    # (Needs/*-needs.rst) that sys requirements are elicited from. Not
    # part of the ASPICE/ISO 15288 requirements-definition chain itself —
    # this is the pre-requirements input layer feeding it. Added because
    # business-needs.rst / operational-needs.rst / stakeholder-needs.rst
    # already use this directive live in this repo; previously
    # unregistered, which made any build touching them fail outright with
    # "Unknown directive type eng_need".
    dict(directive="eng_need", prefix="NEED_", color="#8E9AAF", style="node",
         title="Stakeholder / Business / Operational Need"),
]

# Free-text fields on needs.
# `standard` and `derives_from` are intentionally NOT registered as
# needs_extra_links: elsewhere in this repo (org_governance/, governed by
# the root conf.py) derives_from mixes real need ids with external
# standard-clause citations that have no matching need — as a real link
# that would fail needs_report_dead_links. Kept as free text here too, for
# the same reason and for consistency between the two conf.py files, even
# though every derives_from usage actually inside Needs/ today happens to
# cite a real eng_need id.
needs_fields = {
    "standard": {
        "description": "Standard/clause this need satisfies",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "derives_from": {
        "description": "Upstream need id or external standard clause this "
                        "requirement derives from (free text — not "
                        "dead-link-checked)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "kind": {
        "description": "Need classification used by eng_need, e.g. 'need'",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "domain": {
        "description": "Requirement/need domain, e.g. functional, "
                        "operational, business",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "lifecycle_stage": {
        "description": "Lifecycle stage this need belongs to, e.g. "
                        "stakeholder_needs",
        "schema": {"type": "string"},
        "nullable": True,
    },
}

# Every need must declare at least one upstream link via the built-in
# `links` option (sys <- feat <- comp <- unit, sg <- fsr <- tsr). A broken
# or missing link, or a duplicate id, fails the build below with -W.
needs_id_required = True
needs_id_regex = r"^[A-Z]+_[A-Za-z0-9_]+"

# Fail the build (not just warn) on unresolvable need links, e.g. a
# `:links:` field pointing at an id that doesn't exist.
needs_report_dead_links = True
