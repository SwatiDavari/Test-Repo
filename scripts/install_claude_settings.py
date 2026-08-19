#!/usr/bin/env python3
"""Scaffold or verify this product's Claude Code / MCP wiring.

Idempotent: safe to run on a fresh product repo (writes the files) or an
existing one (reports drift without overwriting anything you've customized,
unless --force is given). This is the product-repo-side counterpart to
qorix-ik-main's own scaffold step (`qik init` embeds the equivalent files
via rust/qik-main/src/scaffold.rs) — written here as a small, readable
Python script rather than requiring the qik binary to be installed just to
stand up a new product repo's AI-agent wiring.

Ensures:
  .mcp.json              registers the qik MCP server
  .claude/settings.json   wires qik_first_guard.py (PreToolUse) and
                          qik_nexus_lifecycle.py (StopHook)

It does NOT write the hook scripts themselves or the agent persona files
(.claude/agents/*.md) — those come from qorix-ik-main as-is and should be
pulled in via `qik upgrade`, not hand-copied here, so this product repo
keeps receiving fixes to them centrally.

Usage:
  python tools/install_claude_settings.py            # scaffold/check
  python tools/install_claude_settings.py --force     # overwrite drifted files
  python tools/install_claude_settings.py --check     # exit 1 if anything is missing/drifted, write nothing
"""
import argparse
import json
import sys
from pathlib import Path

MCP_JSON = {
    "mcpServers": {
        "qik": {
            "command": "qik-mcp",
            "args": [],
        }
    }
}

CLAUDE_SETTINGS = {
    "hooks": {
        "PreToolUse": [
            {
                "hooks": [
                    {
                        "command": 'python3 "${CLAUDE_PROJECT_DIR}/.claude/hooks/qik_first_guard.py"',
                        "statusMessage": "qik-first guard: checking for a manual needs/.qik sweep...",
                        "type": "command",
                    }
                ],
                "matcher": "Grep|Glob|Bash",
            }
        ],
        "StopHook": [
            {
                "hooks": [
                    {
                        "command": 'python3 "${CLAUDE_PROJECT_DIR}/.claude/hooks/qik_nexus_lifecycle.py"',
                        "statusMessage": "qik-nexus-lifecycle: checking PI item completion state...",
                        "type": "command",
                    }
                ]
            }
        ],
    }
}


def check_or_write(path: Path, wanted: dict, force: bool, check_only: bool) -> bool:
    """Return True if `path` already matches `wanted` or was brought in line."""
    if path.exists():
        try:
            current = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            current = None
        if current == wanted:
            print(f"ok      {path}")
            return True
        if check_only:
            print(f"drift   {path}  (does not match expected content)")
            return False
        if not force:
            print(f"skip    {path}  (exists and differs — rerun with --force to overwrite)")
            return False
        path.write_text(json.dumps(wanted, indent=2) + "\n")
        print(f"updated {path}")
        return True

    if check_only:
        print(f"missing {path}")
        return False

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(wanted, indent=2) + "\n")
    print(f"created {path}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--force", action="store_true", help="overwrite files that exist but differ")
    parser.add_argument("--check", action="store_true", help="report only, write nothing, exit 1 on any drift")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    ok = True
    ok &= check_or_write(repo_root / ".mcp.json", MCP_JSON, args.force, args.check)
    ok &= check_or_write(repo_root / ".claude" / "settings.json", CLAUDE_SETTINGS, args.force, args.check)

    for hook in ("qik_first_guard.py", "qik_nexus_lifecycle.py"):
        hook_path = repo_root / ".claude" / "hooks" / hook
        if not hook_path.exists():
            print(f"missing {hook_path}  (pull this from qorix-ik-main / `qik upgrade` — not scaffolded here)")
            ok = False

    if args.check and not ok:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
