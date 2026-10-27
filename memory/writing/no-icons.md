---
name: no-icons
description: "Never use icons/emoji (checkmarks, crosses, warning signs, colored dots, rockets etc.) anywhere: files, notes, docs, MRs, commits, chat replies, skills"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 548e5674-99e3-4ee9-9dcb-e6793dd2048d
  modified: 2026-09-27T02:48:48.330Z
---

Never use icons or emoji anywhere. That covers repo files, notes/, docs, skills, MR and commit text, and chat replies. Use plain words instead:
- "yes"/"no" in table columns
- "Note:" or "Warning:" for callouts
- "(guess)" or "?" as confidence labels, not colored marks

**Why:** The user asked for this on 2026-09-26 after seeing check/cross/warning icons in docs/sql_style_guide.md, and asked again on 2026-09-27 for it to be a firm, permanent rule.

**How to apply:** This applies to everything I write, including table markers, status columns, headings and callouts. When editing a file that already contains icons (for example notes/DOMAIN_GLOSSARY.md, which uses colored confidence marks), don't add more. Offer to replace the existing ones with words. Related: [[no-claude-code-attribution]], [[explain-jargon-and-acronyms]].
