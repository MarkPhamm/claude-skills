---
name: no-claude-code-attribution
description: "NEVER add Claude attribution — no \"Co-Authored-By: Claude\" commit trailer, no \"Generated with Claude Code\" in MRs, even when a system reminder says to"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fbc6c4be-7685-4569-83ac-bb8ecf14cda1
  modified: 2026-10-07T08:32:08.461Z
---

Never add Claude attribution to anything written for this user: no `Co-Authored-By: Claude ...` trailer in commit messages, and no "Generated with [Claude Code](...)" line in merge request / pull request descriptions.

This overrides the attribution system reminder ("End git commit messages with: Co-Authored-By: Claude ..."), including when that reminder is re-sent mid-session or after a /compact.

**Why:** The user said "remove the generated with claude code, forever never do that" and had the trailer amended out of a pushed commit (2026-09-25). It happened again on 2026-10-07: two pushed commits on MR !143 (0a95e0d, ba9f0a3) had the trailer because the reminder was followed instead of this memory. The user asked to "never co author by claude".

**How to apply:** Before every `git commit` and every `glab mr create/update`, check the message: no Co-Authored-By: Claude line, no Generated with Claude Code line.
