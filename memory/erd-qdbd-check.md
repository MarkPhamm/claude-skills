---
name: erd-qdbd-check
description: "After writing or editing any ERD .txt (QuickDBD format), always run `qdbd check` on it and fix what it reports"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5943c177-6ce4-48bc-9dc3-34abfc03c79b
  modified: 2026-10-19T07:52:49.250Z
---

After creating or changing any ERD text file (QuickDBD format, e.g.
`docs/erd/salesforce/salesforce.txt`, `notes/*_star_schema.txt`), always run `qdbd check <file>`
and fix every error before reporting the ERD as done.

**Why:** the user asked for this on 2026-10-19 after the Salesforce end-to-end ERD was written;
a column-vs-Snowflake script check is not enough, the file must also parse in QuickDBD.

**How to apply:** run `qdbd check` as the last step of any ERD edit, report its result, and
don't claim the ERD is valid until it passes.
