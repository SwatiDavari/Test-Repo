#!/usr/bin/env python3
"""Traceability gate: report sphinx-needs links that point at a need id
which does not exist anywhere in the graph.

This is the general form of the exact defect test_repo's own README
disclosed: FEAT_A_001 and FEAT_Z_001 both link to SYS_001, which is never
written — the apex of the V is a dead reference, and every feature under it
is structurally floating. tools/check_orphan_needs.py (kept from test_repo,
unchanged) catches needs with NO links at all; this script catches the
opposite and arguably more dangerous failure — a link that looks fine at a
glance but resolves to nothing.

Usage: python tools/check_broken_links.py <path to needs.json> [--require ID [ID ...]]

needs.json is produced by `sphinx-build -b needs . <outdir>` (see
tools/build_needs.sh). sphinx-needs aggregates every outgoing link — no
matter which custom link type (links / derived_from / fulfils / implements
/ ...) — into each need's "links" field, so scanning that one field is
enough to catch a broken reference regardless of link type.

--require lets CI additionally assert that specific ids exist at all (not
just that nothing links to a missing one) — use it to pin the product's own
HEAD-of-the-V system anchor, e.g.:

    python tools/check_broken_links.py needs/_build/needs/needs.json \\
        --require SYS_001

Exit code 0 if no broken links and all --require ids exist, 1 otherwise.
Intended to run as a hard gate (see .github/workflows/needs-gate.yml) — no
"::warning"-and-continue here; a broken link at the apex of the V is exactly
the class of defect this repo shape must never merge silently.
"""
import argparse
import json
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("needs_json", help="path to needs.json")
    parser.add_argument(
        "--require",
        nargs="*",
        default=[],
        metavar="ID",
        help="need id(s) that must exist in the graph (e.g. the product's "
             "own system-level anchor)",
    )
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
        for target_id in need.get("links") or []:
            if target_id not in needs:
                broken.append((need_id, target_id))

    missing_required = [rid for rid in args.require if rid not in needs]

    if not broken and not missing_required:
        print("No broken links found (every link target exists).")
        if args.require:
            print(f"Required anchor id(s) present: {', '.join(args.require)}")
        return 0

    if broken:
        print(f"Found {len(broken)} broken link(s) — target id does not exist:")
        for source_id, target_id in sorted(broken):
            docname = needs[source_id].get("docname", "?")
            print(f"  - {source_id} -> {target_id!r}  (in {docname})")

    if missing_required:
        print(f"Found {len(missing_required)} required id(s) missing entirely:")
        for rid in missing_required:
            print(f"  - {rid}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
