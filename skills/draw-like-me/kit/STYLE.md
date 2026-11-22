# Drawing like Mark: style guide for this job

Mark Pham writes The Analytics Engineer's Handbook on Substack. His drawings look like notes on a
whiteboard: black ink, wobbly lines, handwritten words, and REAL data from the post in the picture.
The reference post is "Leetcode Series: Gaps and Islands Part 1" (cover + 9 inline drawings).
Never slideware, never icons/logos/mascots, never another writer's style.

Reference renders (open them with Read before you start):
- /home/claude/drawing/kit/examples/gi_cover.png  (+ .js)  - a cover
- /home/claude/drawing/kit/examples/gi_inline_rownumber.png (+ .js) - an inline drawing

## Rules (all of them, every drawing)

1. Ink on white. Background white, strokes #111 (`INK`), rough.js hand-drawn shapes only (helpers below).
   No straight vector boxes, gradients, shadows, emojis, logos.
2. Handwriting font for every word (automatic). Lowercase sentence case like a whiteboard
   (proper nouns/code identifiers keep their case: `dbt`, `Spark`, `fct_orders`, `SELECT`).
3. Real data, not icons. Draw the concept with actual values / names / numbers FROM THE POST:
   table rows, column names, model names, file paths, commands, row counts, timings, prices.
   5-10 values is plenty. Every value must be correct versus the post. Never invent numbers;
   if the post has no numbers for a concept, draw the real names/structure instead.
4. Violet highlighter (`highlight(x,y,w,h)`, theme colour #7c3aed at 0.28 opacity) for THE point:
   one swipe (two max) behind the thing the reader should notice first. Call highlight() BEFORE
   the ink that sits on top of it. Never yellow, never another purple.
5. One blue accent at most (`BLUE` #2f6fdb): a single arrow, circle, or one short annotation line
   marking the step that matters. Everything else black (grey `GREY` for small header labels).
6. Circles and arrows do the explaining: circle groups, curved arrows (never ruler-straight) with
   1-3 word labels (`gap`, `change`, `new version`, `runs first`).
7. Covers use a sandwich: doodle on top (the problem), the post title in the middle, doodle on
   the bottom (the trick / the answer). Plenty of white space.
8. `signature()` on every drawing (small grey "AE Handbook" bottom-right).

## Sizes

- Cover: `// size: 2000x1429`.
- Inline: `// size: 2000xH` with H between 760 and 1200. No title inside inline drawings.

## Text sizes and layout

- Cover title: the post title, 80-92px, max 2 lines (split long titles at a natural break,
  e.g. before "Part 3 -" or after the colon). A series/part line can sit under it at 64-76px.
  If the title is very long, shorten only by dropping the subtitle-ish tail after a dash/colon,
  never reword it. Keep the middle band roughly y=600-860.
- Inline labels 44-64px; values 52-70px; small grey header labels (`GREY`) 30-36px;
  nothing smaller than 30px (the image is shown ~730px wide on Substack).
- An inline drawing may end with ONE caption line (black, 38-44px, <= 70 characters,
  centered near the bottom) that states the takeaway, like the Gaps and Islands drawings
  ("lag(num) hands each row the num of the row before it").
- Center the composition on the canvas; keep >= 60px margins; don't leave half the canvas empty.
- Labels never sit on top of shapes or other text. Ellipses must fully surround what they group.
- No paragraphs: labels are 1-3 words; annotation/caption lines are one short sentence max.

## Helpers available in drawing code (render.py injects them)

```
W, H                          canvas size (from the "// size:" line)
INK, BLUE, VIOLET, GREY       colours
rect(x,y,w,h,opts)            hand-drawn rectangle      ell(cx,cy,w,h,opts)  ellipse (center x,y)
line(x1,y1,x2,y2,opts)        wobbly line               curve([[x,y],...],opts) smooth curve
poly([[x,y],...],opts)        polygon                   arrow([[x,y],...],opts) curved arrow, head at last point
highlight(x,y,w,h)            violet swipe (call before the ink)
cross(x,y,w,h,opts)           X scribble over something (removed/invalid)
text(s,x,y,size,anchor='middle',color=INK)   y is the baseline; anchor 'start'|'middle'|'end'
signature()
opts: {stroke:BLUE, strokeWidth:2.4, fill:..., fillStyle:'solid'|'hachure', roughness:..}
```
Default stroke width is 3.2 (use ~2-2.6 for arrows/ellipses/underlines). Don't redeclare helper
names or `W`/`H`. Use `const` names that don't clash (e.g. prefix with your own names).

## Picking what to draw (inline)

- One concept per drawing, the one a picture explains best: a before/after table, a row-level
  walk-through, a DAG/lineage of real model names, a pipeline with real tool names written as
  words in boxes (no logos), a timeline with real dates, a decision split with real criteria,
  a file tree with real paths, a command and what it produces, a comparison with real numbers.
- Write one sentence first: "the reader should get at a glance that ...". Put it as a comment
  at the top of the .js file.
- Spread drawings through the post (roughly one per main section); never two right after each
  other; place each one right AFTER the paragraph or heading that introduces the concept.
- Don't duplicate an existing screenshot unless the drawing adds the explanation it lacks.

## Checking (mandatory)

Render: `python3 /home/claude/drawing/render.py /home/claude/out/<slug>/*.js`
- Fix every `JS ERROR`, `CLIP`, `OVERLAP` line.
- Then open EVERY PNG with Read and look at it: no text cut at edges, ellipses surround what they
  group, arrows point at the right thing, no label sitting on a line or shape, violet behind the
  ink (not covering it opaquely), one blue accent max, values correct vs the post, composition
  centered and not crowded. Re-render until clean (usually 2-3 passes).

## Don'ts

- No logos, mascots, brand characters, product screenshots recreated, or other writers' drawings.
- No more than one violet swipe group (2 swipes max) and one blue accent per drawing.
- No numbers that aren't in the post.
- No paragraphs inside a drawing.
