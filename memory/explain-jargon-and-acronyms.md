---
name: explain-jargon-and-acronyms
description: "Always explain names/acronyms/jargon ELI5 by breaking them into pieces (schema parts, table code + field code), with explicit (guess) and ? labels; never invent acronym expansions"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fdf6ea55-8702-4d12-866e-0a28d3e09226
  modified: 2026-09-27T02:47:31.876Z
---

When an answer uses domain jargon or acronyms (e.g. source-system names, table codes, SCD2) or refers to one concept that appears under several names (e.g. a raw column, its renamed column and its business term), explain it in plain words the first time it appears.

The style the user explicitly approved (2026-09-27): "yep, from now i want you to explain like this".
- **Break every name into its pieces and explain each one.** For example `<DB>.<CONNECTOR>_<SRCDB>_<SRCSCHEMA>.<TABLE>` becomes database / Fivetran schema `<connector>_<source db>_<source schema>` / table, and a column like `ABCXYZ` becomes table code `ABC` + field code `XYZ`.
- **Keep a short "words used" glossary** (drop, turnover, theo, facility, epoch seconds, ...) in plain words.
- **Use three confidence levels:** no mark = the repo or data says so. "(guess)" = I inferred it. "?" = unknown. Say where each decoding came from.
- **Never invent what an acronym stands for.** Write "XYZ = the source system; what X-Y-Z stands for is ?".

**Why:** The user asked what several acronyms and column codes meant after the notes used those terms without explaining them. They have ADHD and need things short and ELI5.

**How to apply:** Do this in chat replies, notes, and docs. Keep it short: one gloss per term on first use, and bullets over paragraphs.
