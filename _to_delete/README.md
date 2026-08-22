# _to_delete/

Staging area for files/folders confirmed unneeded, kept here (not deleted
outright) so a reviewer can check before they're purged for good. This
repo periodically wipes this folder clean in its own commit (see git log:
"Delete _to_delete directory") and starts it fresh for the next round —
this is that fresh round.

## 2026-08-22 — staleness audit

- `_claude_add_test.txt` — debug leftover from testing `git add` during
  the `.git/index.lock` troubleshooting earlier in this session. Content
  was just "hello test"; served no purpose in the repo.
- `needs_software_diagnostics_requirements_emptydir/` — the empty shell of
  `needs/software/diagnostics/requirements/`, left behind after its
  `index.rst` (a byte-identical duplicate of the Communication
  requirements page) was quarantined and removed. Nothing was left inside
  once that file was gone.

Both are dead-weight cleanup, not content changes — safe to
`git add -A && git commit` along with the rest of this session's changes,
then wipe this folder in its own commit per the usual convention.
