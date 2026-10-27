---
name: recommendation-sql-and-caveats
description: Whenever recommending one approach over another, give a 1-line TL;DR, then the SQL of each option and 1-2 short caveats each
metadata:
  type: feedback
---

Whenever I make a recommendation, show the SQL for each option (recommended and alternative)
with 1-2 short caveats each.

**Why:** on 2026-10-20 the user had to ask for the SQL of both host_hist_sk options, then
complained the answer was too wordy.

**How to apply:** start with a one-line TL;DR saying what the code literally does in plain words
([[be-concise]]). Then one small SQL block per option (only the lines that differ), then at most
1-2 short caveat bullets per option. No preamble, no "both options" section.
