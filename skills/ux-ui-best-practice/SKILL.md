---
name: ux-ui-best-practice
description: Turn a flat "everything visible at once" website into one that follows UX/UI best practice (laws of UX, progressive disclosure, accessibility) and adds purposeful transitions and animation. Use when asked to improve, restructure, polish, modernize or animate a page, landing page, dashboard or HTML/React/Vue/Svelte site, or when the user says the UI feels flat, cluttered, overwhelming or static.
---

# UX/UI Best Practice + Motion

Goal: take a page where every piece of content is dumped on screen at once and turn it into one that **guides attention, reduces cognitive load, feels responsive, and moves with purpose** — without breaking content, SEO or accessibility.

Two halves, applied in this order:

1. **Structure first (UX laws)** — fix hierarchy, chunking, choices and targets. Animation cannot rescue a bad layout.
2. **Motion second (animation principles)** — add transitions that explain change, confirm actions and direct focus.

Full definitions + implementation rules for all 20 principles: `references/principles.md`.
Copy-paste tokens and utilities: `assets/motion.css`, `assets/motion.js`.
Before/after transformation recipes: `references/patterns.md`.

---

## Workflow

### 1. Audit the flat page (don't edit yet)

Read the whole page and write a short audit table with: section, what's wrong, which law it breaks, the fix. Check for:

- **No single focal point** above the fold (Staging) — more than one primary CTA, competing headlines.
- **Walls of options** — nav with >7 items, 5+ equal-weight buttons, long flat feature lists (Hick's, Miller's).
- **Everything expanded** — FAQs, specs, long bios, pricing details shown in full (progressive disclosure).
- **Tiny or cramped targets** — icon buttons < 24×24px, links packed together (Fitts's, WCAG 2.5.8).
- **Unfamiliar patterns** — logo not linking home, nav not at top/left, custom scrollbars, hamburger on desktop (Jakob's).
- **Strict inputs** — forms that reject spaces in phone numbers, case-sensitive emails, no paste (Postel's).
- **No feedback** — buttons with no hover/active/loading state, actions with no confirmation (Doherty, Exaggerated feedback).
- **Flat depth** — no elevation system; cards, modals and page all on one plane (Solid drawing).

Identify the stack (plain HTML/CSS, Tailwind, React, Vue, Svelte, Next, Astro) and use its idioms. Prefer CSS; reach for JS only when CSS can't do it. Use an existing animation lib if the project already has one (Motion/Framer Motion, GSAP); don't add one for things CSS handles.

### 2. Restructure (UX laws)

Apply in this order — each item maps to a law in `references/principles.md`:

1. **One job per viewport (Staging).** Hero = one headline, one sub-line, one primary CTA, optionally one secondary (ghost) CTA. Everything else moves below.
2. **Chunk content (Miller's).** Group into sections of 3–5 items. Long lists → cards in a grid, tabs, or "Show more". Add clear section headings so the page is skimmable.
3. **Cut choices (Hick's).** Primary nav ≤ 5–7 items; move the rest to a footer or "More" menu. One primary button style per view; demote the rest to secondary/tertiary.
4. **Progressive disclosure.** Hide secondary detail behind `<details>`/accordions, tabs, modals/drawers, or "Read more". Keep it in the DOM (SEO, Ctrl+F) — hide visually, not by deleting.
5. **Targets (Fitts's + Bigger hit areas).** Interactive elements ≥ 44×44px on touch (24×24 absolute min, WCAG 2.2). Expand hit areas with padding or a `::before` overlay rather than making the visual bigger. Put primary actions where the thumb/cursor already is (end of a form, bottom on mobile).
6. **Familiar patterns (Jakob's).** Logo top-left → home. Nav top. Search with a magnifier. Cart top-right. Underlined/colored links. Standard form controls.
7. **Forgiving input (Postel's).** Trim whitespace, accept many phone/date formats, `type="email"`/`inputmode`/`autocomplete` attributes, inline validation on blur not on every keystroke, clear error text next to the field.
8. **Visual hierarchy.** Type scale (e.g. 1.25 ratio), max line length ~65ch, consistent 4/8px spacing scale, more whitespace between sections than within them, contrast ≥ 4.5:1 for body text.

### 3. Add motion (animation principles)

Install the tokens from `assets/motion.css` first so every animation shares the same durations and easings. Then add motion in this priority order — stop when the page feels alive, not when every element moves:

| Priority | Where | Principle(s) | Typical recipe |
|---|---|---|---|
| 1 | Button / link / input states | Snappy timing, Exaggerated feedback, Squash & stretch | hover lift 1–2px, `:active` scale(0.97), 120–160ms |
| 2 | Disclosure (accordion, tabs, menus, modals, drawers) | Slow in & out, Pose to pose, Follow through | animate `grid-template-rows` 0fr→1fr / transform+opacity, 200–300ms |
| 3 | Section reveal on scroll | Staging, Secondary action | fade + 12–24px translateY, stagger children 40–60ms, **once only** |
| 4 | Hero entrance | Anticipation, Staging, Follow through | headline → sub → CTA sequence, total ≤ 800ms |
| 5 | Page / view changes | Pose to pose | View Transitions API with fallback |
| 6 | Depth & delight | Solid drawing, Arcs, Overall appeal | elevation on hover, subtle tilt, curved path for "add to cart" fly |

Hard rules:

- **Animate only `transform` and `opacity`** (and `filter`/`clip-path` sparingly). Never animate `width`, `height`, `top`, `left`, `margin` — use transforms or the `grid-template-rows` trick.
- **Durations:** micro-interactions 100–200ms, UI transitions 200–300ms, large/entrance up to 400–500ms. Nothing the user waits on > 300ms. Exit faster than enter (~75%).
- **Easing:** never `linear` for UI movement. Entering = ease-out, leaving = ease-in, moving on screen = ease-in-out. Springs for draggable/physical things.
- **Frequency of use:** things used constantly (nav links, table rows, keyboard shortcuts, command palette) get little or no animation. Rare moments (onboarding, success, first visit) can be richer.
- **Respond within 400ms (Doherty).** Show optimistic UI, skeletons or a spinner immediately; never block feedback on the network.
- **Interruptible.** Use CSS transitions (not keyframes) for state changes so reversing mid-way works. Don't lock UI during an animation.
- **Reveal animations run once** and must not hide content from no-JS users, crawlers or print. Content is visible by default; JS adds the "pre-reveal" class.
- **`prefers-reduced-motion: reduce`** → remove movement (translate/scale/parallax), keep short opacity fades. Already handled in `assets/motion.css`; keep it when you customize.
- **No scroll-jacking, no autoplaying carousels, no parallax on body text, nothing flashing > 3×/sec.**

### 4. Verify

- Keyboard-only pass: every interactive element reachable, visible `:focus-visible` ring, Esc closes overlays, focus returns to trigger.
- Toggle OS reduced-motion (or DevTools → Rendering → Emulate `prefers-reduced-motion`) — page must still be fully usable.
- Disable JS — all content still visible.
- Check DevTools Performance: no layout thrash, animations on compositor, no long tasks > 50ms from animation code.
- Mobile width (375px): targets ≥ 44px, no horizontal scroll, hero CTA visible without scrolling.
- Re-read the audit table and confirm each row is fixed.

### 5. Report back

Summarize briefly: the audit table (before → after), which principles were applied where, and anything intentionally left alone (and why).

---

## Quick decision guide

- "Should this animate?" → Does it explain a change, confirm an action, or direct attention? If none, don't animate it.
- "How long?" → Small + frequent = shorter. Big + rare = longer. When unsure, 200ms ease-out.
- "Show or hide this content?" → Needed by most visitors to decide/act → show. Needed by some → disclose on demand.
- "How many items here?" → More than ~7 → group, paginate, or prioritize.
