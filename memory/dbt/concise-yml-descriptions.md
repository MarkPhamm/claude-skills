---
name: concise-yml-descriptions
description: "dbt yml model and column descriptions must be short and concise, a line or two, not paragraphs of counts and caveats"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5943c177-6ce4-48bc-9dc3-34abfc03c79b
  modified: 2026-10-16T09:04:52.142Z
---

Keep dbt yml descriptions short: a model description is one or two sentences (grain + what it
replaces or feeds), a column description is one line (what it is, source column, the one caveat
that matters). No long lists of row counts, value breakdowns, numbered caveats or history.

**Why:** the user said on 2026-10-16 that the yml descriptions on the offer list models (MR !149)
were "just too much"; detail like counts, review history and caveat lists belongs in the
Engineering Decision Log and the lineage sheet, not the yml.

**How to apply:** when writing or editing a model yml in a dbt project, write the minimum a reader needs
to use the column; put evidence and history in the eng log ([[engineering-log-and-lineage-sheet]]).
Related: [[no-header-comments-in-sql]], [[be-concise]].
