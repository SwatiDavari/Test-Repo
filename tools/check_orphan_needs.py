#!/usr/bin/env python3
"""Traceability gate: report sphinx-needs needs with no incoming or outgoing
link (orphans).

Usage: python tools/check_orphan_needs.py <path to needs.json>

needs.json is produced by `sphinx-build -b needs . <outdir>` (see
.github/workflows/docs.yml). This mirrors the same orphan filter already
used interactively in needs_overview.rst's needtable:

    :filter: len(links) == 0 and len(links_back) == 0

Exit code 0 if no orphans are found, 1 if any are found (docs.yml wraps
this call in `|| echo "::warning::..."`, so a nonzero exit here does not
fail the CI job — it only makes that warning annotation actually fire when
there's something real to report, instead of firing on every run
regardless of content, or never firing because the script didn't exist).
"""
import json
import sys


def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <path to needs.json>", file=sys.stderr)
        return 2

    needs_json_path = sys.argv[1]
    with open(needs_json_path, encoding="utf-8") as f:
        data = json.load(f)

    versions = data.get("versions", {})
    current = data.get("current_version", "")
    version_data = versions.get(current) or next(iter(versions.values()), {})
    needs = version_data.get("needs", {})

    orphans = [
        need_id
        for need_id, need in needs.items()
        if not need.get("links") and not need.get("links_back")
    ]

    total = len(needs)
    print(f"Checked {total} need(s) in {needs_json_path}")

    if not orphans:
        print("No orphan needs found (every need has at least one incoming "
              "or outgoing link).")
        return 0

    print(f"Found {len(orphans)} orphan need(s) — no incoming or outgoing "
          f"link:")
    for need_id in sorted(orphans):
        need = needs[need_id]
        docname = need.get("docname", "?")
        title = need.get("title", "")
        print(f"  - {need_id} ({title!r}) in {docname}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
