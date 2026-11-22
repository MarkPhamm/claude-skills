# The 20 Principles — what they mean and how to implement them on the web

Sources: Disney's *The Illusion of Life* (Thomas & Johnston), Raphael Salaja's userinterface.wiki, Jon Yablonski's *Laws of UX*, Emil Kowalski (frequency of use), WCAG 2.2.

Token names (`--dur-*`, `--ease-*`) refer to `assets/motion.css`.

---

## Part A — Animation principles (1–12)

### 1. Squash & stretch
**Means:** things squish on impact and stretch in motion, giving them weight.
**On the web:** keep it subtle — 2–6% max. Pressed buttons compress (`scale(0.97)`), a toggle knob stretches horizontally while sliding, a notification badge pops (`scale 0 → 1.15 → 1`).
```css
.btn:active { transform: scale(0.97); transition-duration: var(--dur-instant); }
.badge-pop { animation: pop var(--dur-base) var(--ease-spring); }
@keyframes pop { 0%{transform:scale(0)} 60%{transform:scale(1.15)} 100%{transform:scale(1)} }
```
**Avoid:** squashing text or anything the user is reading.

### 2. Anticipation wind-up
**Means:** a small pull-back before the big move, so people see it coming.
**On the web:** a drawer handle nudges before opening; a "send" icon dips back before flying off; hover state hints at what click will do (arrow shifts 2px right on a "Next" link).
```css
.link-arrow svg { transition: transform var(--dur-fast) var(--ease-out); }
.link-arrow:hover svg { transform: translateX(3px); }
```
**Avoid:** anticipation that delays the actual response past 100ms.

### 3. Staging the focus
**Means:** direct the eye to one thing at a time.
**On the web:** one primary CTA per view; sequence the hero (headline → sub → CTA); dim the background behind modals; reveal sections as they enter the viewport; only one element animating "loudly" at a time.

### 4. Pose to pose
**Means:** set the key poses and let the browser fill in the frames.
**On the web:** define start/end states as classes or `data-state` and let CSS transitions interpolate. Use the View Transitions API between page/view states. Use `@starting-style` for elements entering from `display:none`.
```css
.panel { opacity: 1; transform: none; transition: opacity var(--dur-base) var(--ease-out), transform var(--dur-base) var(--ease-out); }
.panel[data-state="closed"] { opacity: 0; transform: translateY(8px); }
```

### 5. Follow through (& overlapping action)
**Means:** parts keep moving after the main body stops, then settle.
**On the web:** stagger children after the container lands (card arrives, then title, then meta 40ms apart); a spring with slight overshoot on a modal (`--ease-spring`); an icon inside a button rotates slightly after the button press.

### 6. Slow in & slow out
**Means:** accelerate and decelerate; never constant speed.
**On the web:** entering = `--ease-out` (fast start, gentle stop), exiting = `--ease-in`, moving across screen = `--ease-in-out`. `linear` only for spinners, progress bars and opacity loops.

### 7. Moving in arcs
**Means:** natural motion follows curves.
**On the web:** "add to cart" flying item, FAB morphing into a sheet, dragged item snapping back. Use separate easing on X and Y (nested elements or `offset-path`).
```css
.fly-x { animation: flyX 500ms var(--ease-in-out) forwards; }
.fly-y { animation: flyY 500ms var(--ease-in) forwards; } /* different curve on Y = arc */
```
**Avoid:** arcs for ordinary UI transitions (dropdowns, modals) — those should move straight and fast.

### 8. Secondary action
**Means:** a small flourish that backs up the main action.
**On the web:** a checkmark draws after "Saved" toast appears; a heart emits a tiny burst when liked; a card's shadow deepens as it lifts. Must be quieter and shorter than the primary action.

### 9. Snappy timing
**Means:** duration sets the feel; keep UI animation under 300ms.
| Kind | Duration |
|---|---|
| Hover, press, toggle, tooltip | 100–160ms (`--dur-fast`) |
| Dropdown, accordion, tab, toast | 200–250ms (`--dur-base`) |
| Modal, drawer, page transition | 250–350ms (`--dur-slow`) |
| One-off hero / onboarding sequence | ≤ 800ms total |
Exits ≈ 75% of entrance duration. Bigger distance → slightly longer, but never sluggish.

### 10. Exaggerated feedback
**Means:** push it past real so the moment lands.
**On the web:** invalid form field shakes (3 quick 4–6px oscillations); success button morphs to a green check with a small scale bump; copy button flashes "Copied!". Reserve for meaningful moments, not every click.
```css
@keyframes shake { 0%,100%{transform:none} 20%,60%{transform:translateX(-5px)} 40%,80%{transform:translateX(5px)} }
.field[aria-invalid="true"] { animation: shake 300ms var(--ease-out); }
```

### 11. Solid drawing in 3D
**Means:** give flat things depth and volume.
**On the web:** a consistent elevation scale (`--shadow-1..4`); higher layers = bigger, softer shadows; hover lifts cards 2–4px and increases shadow; modals sit above a dimmed scrim; optional subtle `perspective` tilt (≤ 6°) on hero cards. Layered shadows look more real than one large blur.

### 12. Overall appeal
**Means:** the sum of every detail done with care.
**On the web:** one motion language (shared tokens), consistent radii/spacing/type scale, crisp focus rings, no jank (60fps), no layout shift (CLS < 0.1), and restraint — the best interfaces feel calm.

---

## Part B — UX laws (13–20)

### 13. Fitts's law
**Means:** bigger, closer targets are faster to hit.
**On the web:** primary CTA large and near the content it acts on; submit button directly below the last field; sticky bottom action bar on mobile; screen edges/corners are "infinite" targets on desktop; keep destructive actions away from frequent ones.

### 14. Bigger hit areas
**Means:** the clickable area can be bigger than it looks.
**On the web:** ≥ 44×44px touch targets (Apple HIG / WCAG 2.5.5 AAA), 24×24px absolute minimum (WCAG 2.2 SC 2.5.8 AA), ≥ 8px between adjacent targets. Make whole cards clickable via a stretched link.
```css
.icon-btn { position: relative; }
.icon-btn::before { content:""; position:absolute; inset:-10px; } /* invisible larger hit area */
.card { position: relative; }
.card a.stretched::after { content:""; position:absolute; inset:0; }
```

### 15. Hick's law
**Means:** more choices → slower decisions.
**On the web:** ≤ 7 top-level nav items; one primary action per view; highlight a recommended pricing tier; break long forms into steps; use smart defaults; search/filter for long lists.

### 16. Miller's law
**Means:** we hold ~7 (±2) things in mind; chunk information.
**On the web:** group features into 3–5 cards per row; split phone/card numbers into groups; break content into sections with headings; use tabs for parallel content; summarize first, details on demand.

### 17. Doherty threshold
**Means:** respond within 400ms or it feels slow.
**On the web:** visual feedback on press within ~100ms; optimistic updates; skeleton screens for loads > 300ms; spinners/progress for > 1s; prefetch on hover; keep INP (Interaction to Next Paint) < 200ms. Animation must never be the reason something feels slow.

### 18. Postel's law
**Means:** accept messy input, give back clean output.
**On the web:** trim and normalize input; accept "+84 90 123 4567", "0901234567", "090-123-4567"; case-insensitive emails; allow paste; `autocomplete`, `inputmode`, `type` attributes; format the value back cleanly on blur; helpful error messages that say how to fix it.

### 19. Jakob's law
**Means:** people expect your site to work like the sites they already use.
**On the web:** logo top-left links home; nav across the top (desktop) / hamburger or tab bar (mobile); links look like links; search icon = magnifier; cart top-right; Esc closes modals; clicking the scrim closes it; back button works (don't break history with SPA routing).

### 20. Frequency of use
**Means:** the more often something is used, the less it should animate.
**On the web:** no entrance animation on nav, sidebar, table rows, list filters, keyboard-triggered actions, command palettes; instant tab switches in tools people use all day; save the richer motion for first-run, empty states, success moments and marketing pages. If a user will see it 100× a day, it should take ≤ 150ms or 0ms.

---

## Accessibility guardrails (always on)

- `@media (prefers-reduced-motion: reduce)`: remove translate/scale/parallax/autoplay; keep opacity fades ≤ 150ms.
- Never flash more than 3 times per second (WCAG 2.3.1).
- Anything that auto-moves > 5s needs pause/stop (WCAG 2.2.2).
- Content hidden by reveal animations must be visible without JS and to screen readers.
- Disclosure widgets: correct `aria-expanded`, `aria-controls`; modals trap focus and restore it on close (or use native `<dialog>`).
- Visible `:focus-visible` outline, 3:1 contrast against its background.
