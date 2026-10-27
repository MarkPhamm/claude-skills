---
name: review-checkout-and-run
description: "When reviewing an MR/branch, always check out the branch locally, run dbt (build/compile/show) and query the built models, not just read the diff"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f7c07bb8-5251-4ad6-b8b8-7592437fc205
  modified: 2026-10-16T08:23:13.370Z
---

When reviewing an MR or branch, check out the branch locally (stash local edits first), then run dbt on the changed models and their parents (compile, build into the dev schema, run tests) and query the built relations to confirm each finding. Do not review from `glab mr diff` / `git show` alone.

**Why:** the user rejected a review done only from the diff plus raw-source queries; they want findings backed by the real compiled/built models.

**How to apply:** stash, `git checkout <branch>`, `dbt deps`, `dbt build --select +<changed models>` (dev target), query the built tables, then report what ran, what failed, and what was not run.
