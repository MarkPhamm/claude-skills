---
name: no-header-comments-in-sql
description: Never put a comment block at the top of a dbt .sql model; only short inline comments where the logic needs one
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5943c177-6ce4-48bc-9dc3-34abfc03c79b
  modified: 2026-10-16T09:04:47.846Z
---

Never write a header comment block at the top of a SQL model (no "-- Grain: ..." / design notes
before the first CTE). Keep comments inline, short, and only where a line of logic is not obvious.

**Why:** the user asked for this on 2026-10-16 after the offer list models (MR !149) opened with
long header blocks; grain, joins and caveats belong in the yml and the eng log, not the SQL.

**How to apply:** when writing or editing any model in a dbt project, start the file with `with ...`;
move design notes to the yml description (kept short, see [[concise-yml-descriptions]]) or the
Engineering Decision Log ([[engineering-log-and-lineage-sheet]]).
