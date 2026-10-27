---
name: ask-base-branch
description: Always ask which branch to check out / branch from before creating a new branch; never assume qa or main
metadata:
  node_type: memory
  type: feedback
  originSessionId: 548e5674-99e3-4ee9-9dcb-e6793dd2048d
  modified: 2026-09-26T05:39:31.007Z
---

Before creating a new branch, always ask the user which base branch to check out from. Don't assume (even though feature MRs usually land in `qa`).

**Why:** The user asked for this explicitly (2026-09-26). The branching flow (feature → qa → main) has exceptions, and they want to choose the base themselves.

**How to apply:** When a task needs a new branch, ask "branch from which base?" first. Also don't commit or push until the user says so. They like to review and ask questions first; see [[no-claude-code-attribution]] for commit/MR rules.
