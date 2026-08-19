#!/usr/bin/env python3
"""Traceability gate: report sphinx-needs needs with no incoming or outgoing
link (orphans).

Usage:
    python tools/check_orphan_needs.py <path to needs.json>
    python tools/check_orphan_needs.py <path to needs.json> --baseline <path to baseline.json>

needs.json is produced by `sphinx-build -b needs . <outdir>` (see
.github/workflows/docs.yml). This mirrors the same orphan filter already
used interactively in needs_overview.rst's needtable:

    :filter: len(links) == 0 and len(links_back) == 0

Without --baseline: exit 0 if no orphans are found, 1 if any are found.

With --baseline: the baseline file is a JSON list of need ids that are
known, accepted orphans as of a point in time (e.g. top-of-hierarchy
organizational requirements with nothing decomposed under them yet — not
every orphan is a mistake). Exit 0 if every current orphan is already in
the baseline; exit 1 only if a NEW orphan appears that isn't. This is
what makes the check safe to run as a hard, unconditional CI gate on a
repo that already has disclosed orphan debt: it blocks regressions
(something *new* silently losing its links) without also blocking every
future PR on debt nobody asked this PR to pay down.

docs.yml runs this without `|| echo "::warning::..."` — a nonzero exit
here now fails the CI job.

NOTE on named link types: conf.py / needs/conf.py define `needs_links`
entries (derived_from/satisfies/fulfils/implements/verifies/belongs_to/
consists_of), additive alongside the built-in `links` field, added to
align with qorix-ik-main's qik-axon link vocabulary. sphinx-needs stores
each one under its own key in needs.json (e.g. a `:satisfies:` target
lands in `satisfies`/`satisfies_back`, not `links`/`links_back` —
verified directly against a real needs.json before writing this) so a
need connected ONLY via a named field has empty `links`/`links_back` and
would misreport as an orphan under the original links-only check below.
LINK_FIELDS covers every field a connection can be recorded under, so
that misreport doesn't happen. Keep it in sync with both conf.py files'
`needs_links` dict if either changes.
"""
import argparse
import json
import sys

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
    parser.add_argument(
        "--baseline",
        help="path to a JSON list of already-accepted orphan need ids; "
        "if given, only NEW orphans not in this list cause a failure",
    )
    args = parser.parse_args()

    with open(args.needs_json, encoding="utf-8") as f:
        data = json.load(f)

    versions = data.get("versions", {})
    current = data.get("current_version", "")
    version_data = versions.get(current) or next(iter(versions.values()), {})
    needs = version_data.get("needs", {})

    orphans = {
        need_id
        for need_id, need in needs.items()
        if not any(need.get(field) for field in LINK_FIELDS)
        and not any(need.get(f"{field}_back") for field in LINK_FIELDS)
    }

    total = len(needs)
    print(f"Checked {total} need(s) in {args.needs_json}")

    if not orphans:
        print(
            "No orphan needs found (every need has at least one incoming "
            "or outgoing link)."
        )
        return 0

    baseline = set()
    if args.baseline:
        with open(args.baseline, encoding="utf-8") as f:
            baseline = set(json.load(f))

    new_orphans = orphans - baseline
    resolved = baseline - orphans

    print(f"Found {len(orphans)} orphan need(s) — no incoming or outgoing link:")
    for need_id in sorted(orphans):
        need = needs[need_id]
        docname = need.get("docname", "?")
        title = need.get("title", "")
        flag = "" if need_id in baseline else "  <-- NEW, not in baseline"
        print(f"  - {need_id} ({title!r}) in {docname}{flag}")

    if resolved:
        print(
            f"\n{len(resolved)} previously-baselined id(s) are no longer "
            f"orphans — safe to remove from the baseline file: "
            f"{', '.join(sorted(resolved))}"
        )

    if args.baseline:
        if new_orphans:
            print(f"\n{len(new_orphans)} NEW orphan(s) not covered by the baseline.")
            return 1
        print("\nAll current orphans are already in the accepted baseline.")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
