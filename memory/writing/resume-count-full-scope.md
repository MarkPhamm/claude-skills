---
name: resume-count-full-scope
description: "For resume bullets, count the whole project scope (all models incl. teammates' and pending/unmerged MRs), not just merged or own work"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4631df65-bbea-4614-b8e4-f52507820c6c
  modified: 2026-10-03T13:53:03.723Z
---

When writing resume bullets from project work (resume repo: ~/projects/Minh_Pham_Resume), count everything in scope: all facts, dims, bronze models, semantic views across every branch, including teammates' work and pending/unmerged MRs. Use the biggest honest number, not just what's merged into qa or what the user built alone.

**Why:** User said "resume is the place where you make yourself impressive, count everything, vs pending models also". A first draft that said "1 fact, 4 dims" (only their reservation star schema) was rejected as too small.

**How to apply:** Count model files across all remote branches (git ls-tree on each origin/* branch, dedupe names, drop superseded or deleted ones). Still keep claims traceable to the repo or to what the user tells you. Resume rules (1 page, 2-line bullets) are in that repo's CLAUDE.md. Related: [[be-concise]]
