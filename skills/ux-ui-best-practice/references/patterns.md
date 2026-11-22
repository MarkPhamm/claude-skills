# Flat → Structured: transformation recipes

Each recipe: the flat symptom, the laws involved, and what to change. Adapt markup to the project's framework.

---

## 1. Hero with everything in it
**Symptom:** headline, three paragraphs, four buttons, a feature list and a form all above the fold.
**Laws:** Staging, Hick's, Fitts's.
**Fix:**
- Keep: one headline (≤ 10 words), one supporting line, one primary CTA, optional ghost secondary CTA, one visual.
- Move paragraphs to an "About/How it works" section; features to a card grid; form to its own section or a modal triggered by the CTA.
- Entrance (once, on load): headline → sub-line (+80ms) → CTA (+160ms) → visual (+240ms). Each fades + rises 12px, `--dur-reveal`, `--ease-out`.
```html
<section class="hero" data-reveal-group>
  <h1>Ship data products faster</h1>
  <p>One sentence that says who it's for and why.</p>
  <div><a class="btn btn-primary" href="#start">Get started</a> <a class="btn btn-ghost" href="#demo">Watch demo</a></div>
</section>
```

## 2. Long flat feature list
**Symptom:** 15 bullet points of equal weight.
**Laws:** Miller's, Hick's, Staging.
**Fix:** pick the top 3–6 and render as cards (icon, title, one line). Group the rest under tabs by category or a "See all features" disclosure. Cards reveal with a 50ms stagger; hover lifts 3px with `--shadow-3`.

## 3. Everything-expanded FAQ / specs / policies
**Symptom:** 20 Q&As fully open.
**Laws:** Progressive disclosure, Miller's.
**Fix:** native `<details><summary>` (accessible by default) or button + `.collapse`. Group into 3–5 categories. Animate open with `grid-template-rows` (220ms). Optionally keep the first item open. Add a search filter if > 15 items.

## 4. Mega navigation
**Symptom:** 12 top-level links.
**Laws:** Hick's, Jakob's, Fitts's.
**Fix:** ≤ 5–7 top-level items + one primary CTA at the right. Remaining links → dropdown menus or footer. Dropdowns open on click (and hover with ~100ms intent delay on desktop), animate opacity + 4px translateY in 150ms, close on Esc / outside click. Mobile: hamburger → full-height drawer sliding from the side (`--dur-slow`), body scroll locked, 44px rows. Nav links themselves get **no** entrance animation (Frequency of use).

## 5. Pricing table with no guidance
**Symptom:** 4 identical columns, 30 rows of checkmarks.
**Laws:** Hick's, Staging, Miller's.
**Fix:** 3 tiers; highlight the recommended one (badge, elevated `--shadow-3`, slight scale 1.02 on desktop). Show the 5 most important differences; collapse the full comparison table behind "Compare all features". Monthly/annual toggle animates the price with a quick crossfade (150ms), not a counting animation.

## 6. Unforgiving long form
**Symptom:** 14 fields on one page, errors only on submit.
**Laws:** Postel's, Miller's, Hick's, Doherty, Exaggerated feedback.
**Fix:**
- Split into 2–4 steps with a progress indicator; or group into fieldsets with headings.
- Remove optional fields or mark them "(optional)".
- `autocomplete`, `inputmode`, `type` on every field; normalize on blur (`normalize.*` in motion.js).
- Validate on blur; error text under the field with `aria-describedby`; invalid field shakes once.
- Submit: button shows spinner within 100ms, disables to prevent double submit, morphs to ✓ on success (`.pop`).
- Step change: slide 16px + fade, `--dur-base`; direction matches forward/back.

## 7. Dense data dashboard
**Symptom:** 10 charts and 4 tables on one screen.
**Laws:** Staging, Miller's, Frequency of use, Doherty.
**Fix:** top row of 3–5 KPI tiles; one primary chart; secondary charts in tabs or below the fold. Skeletons while loading. **Minimal motion**: no scroll reveals, no animated chart entrances on every refresh (maybe on first load only), instant filter changes or ≤ 150ms crossfades.

## 8. Static image gallery / testimonials wall
**Symptom:** 30 images or quotes in a grid.
**Laws:** Miller's, Staging.
**Fix:** show 6–9 with "Load more" (new items reveal with stagger). Lightbox via `<dialog>` with scale-from-thumbnail (View Transitions `view-transition-name` on the clicked image). No autoplay carousel; if a carousel is necessary, user-controlled with visible prev/next ≥ 44px and swipe.

## 9. Buttons with no feedback
**Symptom:** click does nothing visible until the network returns.
**Laws:** Doherty, Exaggerated feedback, Squash & stretch.
**Fix:** `.btn` utilities (hover lift, active press). Async actions: optimistic UI or loading state immediately; toast for confirmation sliding in from the corner (200ms in, 150ms out, auto-dismiss 4–6s, pausable on hover).

## 10. Flat single-plane design
**Symptom:** cards, header and modal all look the same depth.
**Laws:** Solid drawing in 3D, Staging.
**Fix:** elevation scale — page `none`, cards `--shadow-1`, hovered/raised `--shadow-3`, sticky header `--shadow-2` once scrolled, modal/drawer `--shadow-4` + scrim. Sticky header shadow fades in on scroll (CSS scroll-driven animation where supported, else a class toggled by an IntersectionObserver sentinel).
```css
@supports (animation-timeline: scroll()) {
  .site-header { animation: header-shadow linear both; animation-timeline: scroll(); animation-range: 0 80px; }
  @keyframes header-shadow { to { box-shadow: var(--shadow-2); } }
}
```

---

## Motion budget per page type

| Page type | Scroll reveals | Hero entrance | Hover/press | Page transitions |
|---|---|---|---|---|
| Marketing / landing | Yes, once | Yes | Yes | Yes |
| Docs / blog | Light (headings only) or none | No | Yes | Optional |
| App / dashboard / tool | No | No | Subtle | Fast crossfade only |
| Forms / checkout | No | No | Yes + strong feedback | Step slides |
