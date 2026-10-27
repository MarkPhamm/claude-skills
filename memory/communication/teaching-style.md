---
name: teaching-style
description: "How to pace explanations when teaching this user Terraform (or similar) — no trailing questions, prioritize conceptual understanding over running commands"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4fd810ad-23b5-420b-a924-598842454f63
  modified: 2026-09-15T03:05:08.441Z
---

Don't end responses with a question asking whether to proceed to the next step (e.g. "want me to run apply now?" or "should we move on?"). Just explain; let the user drive when they're ready to move.

**Why:** User said explicitly: "chill, just don't ask question at the end, applying is easy, understand the code is not." Running commands (`terraform apply`, etc.) is trivial to them — the bottleneck is understanding the code/concepts, not execution.

**How to apply:** When teaching, stop after explaining a concept instead of prompting "want me to continue?". Only ask a real question when genuinely blocked on a decision only the user can make — not as a pacing device. Bias toward deeper, more fundamental explanation (assume very little prior knowledge) over offering to take the next action.
