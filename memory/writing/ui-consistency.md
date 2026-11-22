---
name: ui-consistency
description: "Any UI the user sees (docs cards, buttons, tables, screenshots, viewer) must be visually consistent: same shape, one-line labels, aligned"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f6913f71-5671-4694-8b7f-9efe5664ced6
  modified: 2026-11-20T10:11:17.030Z
---

Every set of sibling UI elements (doc cards, buttons, table rows, screenshots, toolbar items) must look like one system: same shape and height, titles and labels on one line, matching text length, links/actions aligned at the same spot. No wrapping titles, no ragged cards.

**Why:** the user called a set of four "start here" cards "so bad" (2026-11-20) because titles wrapped to two lines, descriptions had different lengths and the links sat at different heights.

**How to apply:** before shipping any UI or docs layout change, screenshot it at desktop and mobile widths and measure, not just eyeball: every label one line, siblings same height, actions aligned. Shorten copy to fit rather than letting it wrap. Fix every instance of the same pattern, not only the one reported. Related: [[no-icons]].
