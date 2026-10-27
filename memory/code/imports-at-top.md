---
name: imports-at-top
description: "Python imports always go at module top, never lazily inside functions"
metadata:
  node_type: memory
  type: feedback
  originSessionId: dfe8f483-4978-4d06-b922-432224c546ea
  modified: 2026-10-12T13:27:29.304Z
---

Put every Python import at the top of the module. No function-local / lazy imports, even for a code path only one branch uses.

**Why:** User corrected a lazy `import duckdb` inside `partitioned_folders()` in aivn_dbt/scripts/gen_bronze.py (2026-10-12): "import should always be at the top".

**How to apply:** Applies to all new Python code. Add imports to the module's top import block in the right group (stdlib / third-party / local).
