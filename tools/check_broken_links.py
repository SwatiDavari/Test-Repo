#!/usr/bin/env python3
"""Traceability gate: fail if any sphinx-needs link-type field (`:links:`
or a named type like `:satisfies:`/`:verifies:`) points at a need id that
does not exist anywhere in the graph (a dead link).

This is a hard, zero-tolerance gate — unlike check_orphan_needs.py, no
baseline/allowlist is supported here, because as of this writing there is
no pre-existing broken-link debt in this repo to grandfather in. If a
future change reintroduces broken-link debt on purpose (rare — usually
it's a mistake), that's a signal to fix the link, not to add an exception
mechanism to this script.

Background: this is exactly the class of defect SYS_001 was — a need
declared `:links: SYS_001` before SYS_001 existed, so the link was dead
and nothing caught it. sphinx-needs' own `needs_report_dead_links` config
plus `-W` already catches this *within* a single Sphinx project (see
needs/conf.py + .github/workflows/ci-needs.yml). This script gives the
same protection to the root project (org_req/risk/problem/change/
exception/tool/infra), whose CI build (.github/workflows/docs.yml) does
not run with `-W` — turning that on wholesale currently fails on the
disclosed content gaps in README.md's "Known gaps" section (five
`process_description.rst` template stubs not in any toctree, and one
missing `needs_overview` page), which are content gaps, not a
link-correctness problem. This script targets link correctness only.

Usage: python tools/check_broken_links.py <path to needs.json>

needs.json is produced by `sphinx-build -b needs . <outdir>`.
"""
import argparse
import json
import sys

# Every link-type field this repo's needs can use: the sphinx-needs
# built-in `links` field, plus every key of `needs_links` in conf.py /
# needs/conf.py (added to align with qorix-ik-main's qik-axon link
# vocabulary). Each is dead-link-checked independently by sphinx-needs
# itself (verified with a real build: `:satisfies: BAD_ID` fails a -W
# build with `needs.link_outgoing`, exactly like a bad `:links:` target
# does) — but this script predates that addition and originally only
# looked at `links`, which would have silently stopped checking any need
# connected solely via a named field. Keep this list in sync with both
# conf.py files' `needs_links` dict if either changes.
LINK_FIELDS = [
    "links",
    "derived_from",
    "satisfies",
    "fulfils",
    "implements",
    "verifies",
    "belongs_to",
    "consists_of",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("needs_json", help="path to needs.json")
    args = parser.parse_args()

    with open(args.needs_json, encoding="utf-8") as f:
        data = json.load(f)

    versions = data.get("versions", {})
    current = data.get("current_version", "")
    version_data = versions.get(current) or next(iter(versions.values()), {})
    needs = version_data.get("needs", {})

    total = len(needs)
    print(f"Checked {total} need(s) in {args.needs_json}")

    broken = []
    for need_id, need in needs.items():
        for field in LINK_FIELDS:
            for target_id in need.get(field) or []:
                if target_id not in needs:
                    broken.append((need_id, field, target_id))

    if not broken:
        print(
            "No broken links found (every link-type field target exists: "
            f"{', '.join(LINK_FIELDS)})."
        )
        return 0

    print(f"Found {len(broken)} broken link(s) — target id does not exist:")
    for source_id, field, target_id in sorted(broken):
        docname = needs[source_id].get("docname", "?")
        print(f"  - {source_id} :{field}: -> {target_id!r}  (in {docname})")

    return 1


if __name__ == "__main__":
    sys.exit(main())
