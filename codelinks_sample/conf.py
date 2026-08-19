# Configuration file for Sphinx + Sphinx-Needs + sphinx-codelinks
#
# THIS IS A SAMPLE, NOT A PRODUCTION PROJECT — see README.md in this folder
# for exactly what it demonstrates and, more importantly, what it doesn't
# (only source/c; the other four languages under source/ are untouched;
# not wired into CI; not merged into the root project's own conf.py).
#
# Why a third, separate Sphinx project instead of adding sphinx_codelinks
# directly to the root conf.py: sphinx-codelinks 1.4.0 (the only version on
# PyPI — every release requires Python >=3.12) cannot be installed under
# Python 3.11, and .github/workflows/docs.yml pins the root project's build
# to Python 3.11 (see ORG_TOOLCFG_001 / TOOL_SPHINX_ROOT in
# organisation/tools/tool_register.rst — that pin is deliberate, documented
# tool-qualification state, not an oversight). Adding `sphinx_codelinks` to
# the root project's `extensions` list would make the real CI's Sphinx
# import fail outright on every build. Keeping this as an isolated project
# with its own conf.py — the same pattern this repo already uses to keep
# `needs/` separate from the root project — means this sample can be built
# and verified for real (it is: see README.md) without touching, or being
# able to break, anything that already runs in CI.

project = "Qorix Engineering Processes — Code Links Sample (source/c)"
master_doc = "index"
extensions = ["sphinx_needs", "sphinx_codelinks"]

# needs_external_needs (below) requires a non-empty Sphinx `version`, same
# reason as root conf.py's own copy of this comment.
version = "1.0"
release = "1.0"

# --- Cross-project traceability to needs/ ----------------------------------
# The whole point of this sample is that `IMPL_C_SERIALIZER_ENCODE`
# (extracted from a comment marker in source/c/src/communication/
# serializer.c) can carry a real, dead-link-checked `:links: UNIT_A_001`
# instead of the free-text "Implements UNIT_A_001" comment that was already
# sitting in serializer.h. That requires importing needs/'s own needs.json
# as external needs here — exactly the same needs_external_needs mechanism
# needs/conf.py already uses to import the root project's org_req needs,
# pointed the other direction.
#
# json_path is a build artifact: generate it first with
#   cd needs && python3 -m sphinx -b needs . _build/needsjson
# (needs/'s needs.json is not committed to the repo, matching the existing
# convention for organisation/'s own export — see needs/conf.py's comment).
# base_url is a placeholder pointing at a local build of needs/'s HTML;
# point it at the deployed needs/ site's real URL once one exists, same
# caveat as needs/conf.py's own base_url placeholder.
needs_external_needs = [
    {
        "base_url": "../needs/_build/html/",
        "json_path": "../needs/_build/needsjson/needs.json",
        "id_prefix": "",
    }
]

needs_types = [
    # Native to this sample: what sphinx-codelinks extracts from a source
    # comment marker (`// @<title>, <id>, <type>, [<links>]`) and turns into
    # a real need via add_need() at build time — see README.md for the
    # exact marker syntax used in source/c/src/communication/serializer.c.
    dict(directive="impl", prefix="IMPL_", color="#546E7A", style="node",
         title="Implementation Artifact — extracted from a source-code "
                "comment marker by sphinx-codelinks"),

    # --- External types, imported only ----------------------------------
    # Nothing in this sample ever writes `.. unit::` etc. directly — these
    # entries exist purely so needs_external_needs (above) can load
    # needs/'s own native needs.json as real, dead-link-checked citations.
    # Registering only `unit` (the one type an `impl` need actually links
    # to in this sample) is not enough in practice: needs_external_needs
    # validates every entry in the imported needs.json against a known
    # type, not just the ones actually referenced — so every native type
    # needs/'s own build produces has to be listed here too, or the import
    # fails with "Unknown need type" the same way root conf.py's own
    # comment on this describes. Copied from needs/conf.py's needs_types.
    dict(directive="sys", prefix="SYS_", color="#BFD8D2", style="node",
         title="External: System Requirement (needs/)"),
    dict(directive="feat", prefix="FEAT_", color="#FEDCD2", style="node",
         title="External: Feature / Software Requirement (needs/)"),
    dict(directive="comp", prefix="COMP_", color="#DF744A", style="node",
         title="External: Component / Software Architecture (needs/)"),
    dict(directive="unit", prefix="UNIT_", color="#DCB239", style="node",
         title="External: Unit / Detailed Design (needs/)"),
    dict(directive="sg", prefix="SG_", color="#B71C1C", style="node",
         title="External: Safety Goal (needs/)"),
    dict(directive="fsr", prefix="FSR_", color="#D32F2F", style="node",
         title="External: Functional Safety Requirement (needs/)"),
    dict(directive="tsr", prefix="TSR_", color="#E57373", style="node",
         title="External: Technical Safety Requirement (needs/)"),
    dict(directive="eng_need", prefix="NEED_", color="#8E9AAF", style="node",
         title="External: Stakeholder / Business / Operational Need (needs/)"),
    dict(directive="tc", prefix="TC_", color="#43A047", style="node",
         title="External: Unit Test Case (needs/)"),
    dict(directive="itc", prefix="ITC_", color="#00897B", style="node",
         title="External: Component Integration Test Case (needs/)"),
]

# Every field needs/'s native needs actually use, registered here too —
# needs_external_needs rejects any field it doesn't recognize with
# "Unknown keys in external need source" (confirmed by a real build; first
# attempt without this list warned on 40+ field names, including `asil`/
# `cal` and every named-link `_back` variant). Values/descriptions don't
# matter for this sample — nothing here queries them — only that they
# exist so the import doesn't warn. Copied from needs/conf.py's own
# needs_fields (minus `pinned`/`toolchain_step`/etc., which belong only to
# the external `tool` type needs/ itself imports from root — irrelevant
# here since this sample doesn't register `tool`).
needs_fields = {
    name: {"schema": {"type": "string"}, "nullable": True}
    for name in [
        "standard", "derives_from", "kind", "domain", "lifecycle_stage",
        "rationale", "use_case", "dependency", "input_reference",
        "req_type", "impact", "actions", "asil", "cal", "version",
        "pinned", "toolchain_step", "used_in", "ci_workflow", "tcl",
        "qualification_status", "provider", "acquisition",
        "availability_note", "likelihood", "mitigation", "affected_needs",
    ]
}

# Named link types, needed so the `_back` variants (satisfies_back,
# verifies_back, etc.) that show up on needs/'s exported needs are
# recognized too — copied verbatim from needs/conf.py's own needs_links.
needs_links = {
    "derived_from": {"incoming": "gives rise to",     "outgoing": "derived_from"},
    "satisfies":    {"incoming": "is satisfied by",   "outgoing": "satisfies"},
    "fulfils":      {"incoming": "is fulfilled by",   "outgoing": "fulfils"},
    "implements":   {"incoming": "is implemented by", "outgoing": "implements"},
    "verifies":     {"incoming": "is verified by",    "outgoing": "verifies"},
    "belongs_to":   {"incoming": "consists of",       "outgoing": "belongs_to"},
    "consists_of":  {"incoming": "belongs to",        "outgoing": "consists_of"},
}

needs_id_required = True
needs_id_regex = r"^[A-Z]+_[A-Za-z0-9_]+"
needs_report_dead_links = True

# needs/'s own SG_001 need carries `:links: ORG_SMS_001` — a real link, but
# to an org_req need that lives in the ROOT project, which THIS sample
# doesn't import (only needs/'s own needs.json, not root's too — importing
# root's as well just to resolve one transitively-external link is more
# than a source/c sample needs). Without root's needs.json also loaded,
# sphinx-needs can't tell ORG_SMS_001 apart from a genuinely broken link on
# an external need, and warns `needs.external_link_outgoing`. Suppressed
# deliberately, not because the link is actually broken — verified by
# checking needs/'s own `-W` build (see needs/ itself) has 0 warnings, so
# the break only appears here, an artifact of a two-hop external import
# this sample doesn't chase.
suppress_warnings = ["needs.external_link_outgoing"]

# --- sphinx-codelinks: scan source/c for `// @title, id, type, [links]` ---
# markers and turn each one into a real `impl` need at build time.
#
# Configured via a TOML file (codelinks.toml), not a `src_trace_projects =
# {...}` dict assigned directly here. Tried the direct-dict form first: it
# builds without error but the `.. src-trace::` directive then crashes with
# `KeyError: 'source_discover_config'` — sphinx_codelinks only calls the
# internal `generate_project_configs()` step (which populates that key)
# from the TOML-loading code path (`load_config_from_toml` in
# sphinx_extension/source_tracing.py), not from a conf.py-assigned dict.
# Confirmed by reading that module's source, not guessed after the
# traceback. The TOML path is also what the standalone `codelinks` CLI
# itself expects, so it's the better-supported shape to standardize on
# regardless.
src_trace_config_from_toml = "codelinks.toml"
