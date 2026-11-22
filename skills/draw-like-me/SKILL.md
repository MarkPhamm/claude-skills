---
name: "draw-like-me"
description: "Draw a hand-sketched illustration in Mark's style (ink sketch, violet highlighter matching his Substack theme, one blue accent) for Substack covers or inline diagrams of data and SQL concepts."
---

# Draw like Mark

Mark writes The Analytics Engineer's Handbook on Substack. His drawings look like notes on a whiteboard: black ink, wobbly lines, handwritten words, and real data in the picture (rows, values, flags, tables). They should never look like slideware or a copy of another writer's style.

## The style

These are the rules that make a drawing look like Mark's. Follow all of them unless he asks otherwise.

1. **Ink on white.** Background `#ffffff`, strokes `#111`, stroke width about 3 on a 2000px canvas. Draw with rough.js: roughness 1.6, bowing 1.2. Every shape is hand-drawn. No straight vector boxes, no gradients, no shadows.
2. **Handwriting.** Architects Daughter for every word. The title is about 90px, labels 46 to 64px. Write in lowercase sentence case, the way he writes on a whiteboard.
3. **Real data, not icons.** Draw the concept with the actual values: cells holding `1 1 1 2`, rows of snapshots like `free free pro`, a `change flag` row over a `running sum` row, `valid_from` to `9999-12-31` on a line. The data must be correct.
4. **Violet highlighter for the point.** The highlighter is Mark's Substack theme colour, `#7c3aed` (the violet on his Subscribe button), drawn at opacity about 0.28 so it reads as a light tint behind the ink. One or two rough swipes go behind the thing the reader should notice first: the island, the changed row, the new version. Draw the swipe before the ink so it sits underneath. Never yellow, and never a guessed purple: use the theme hex so the drawings match the publication.
5. **One blue accent, at most.** `#2f6fdb` for a single arrow or circle that shows the step that matters. Everything else stays black.
6. **Circles and arrows do the explaining.** Circle groups (islands, versions), point at boundaries with a short curved arrow and a one-word label (`gap`, `change`, `new version`). Arrows are curves, never ruler-straight.
7. **A sandwich layout for covers.** Doodle on top, title in the middle, doodle on the bottom, with plenty of white space. The top doodle shows the problem and the bottom one shows the trick.
8. **Signature.** A small handwritten `AE Handbook` in the bottom-right corner, 34px, grey `#666`.

## Sizes

| Use | Canvas |
| --- | --- |
| Substack cover and social preview | 2000 x 1429 |
| Inline diagram in a post | 2000 x 900 to 1200, no title in the picture |
| Square, for LinkedIn or Notes | 1600 x 1600 |

## How to make one

1. Before drawing, write one sentence: what should the reader understand at a glance? Pick the data that shows it (5 to 10 values is plenty) and decide which element gets the violet swipe.
2. Install the tools once per session:

```bash
mkdir -p drawing && cd drawing && npm init -y >/dev/null
npm i roughjs@4.6.6 @fontsource/architects-daughter@5.0.13
```

3. Copy the script below into `drawing/make.py`, then write the drawing between the `# ---- drawing ----` markers using the helpers.
4. Render with `python3 make.py`, then open the PNG with the Read tool and look at it. Check that no text is cut off at the edges, that circles actually surround the cells they group, that boxes do not overlap, that the violet sits behind the ink, and that the values are correct. Fix and re-render until it is clean, usually two or three passes.
5. Show Mark the PNG before it goes anywhere public.

```python
import base64, sys
from playwright.sync_api import sync_playwright

W, H = 2000, 1429          # cover size; change for other uses
OUT = sys.argv[1] if len(sys.argv) > 1 else 'drawing.png'

rough = open('node_modules/roughjs/bundled/rough.js').read()
font = base64.b64encode(open('node_modules/@fontsource/architects-daughter/files/architects-daughter-latin-400-normal.woff2', 'rb').read()).decode()

helpers = """
const svg=document.getElementById('s'); const rc=rough.svg(svg); let seed=7;
const INK='#111', BLUE='#2f6fdb', VIOLET='#7c3aed';   // VIOLET = Substack theme colour
const O=(o={})=>Object.assign({stroke:INK,strokeWidth:3.2,roughness:1.6,bowing:1.2,seed:seed++},o);
const add=n=>{svg.appendChild(n);return n;};
const rect=(x,y,w,h,o)=>add(rc.rectangle(x,y,w,h,O(o)));
const ell=(cx,cy,w,h,o)=>add(rc.ellipse(cx,cy,w,h,O(o)));
const line=(x1,y1,x2,y2,o)=>add(rc.line(x1,y1,x2,y2,O(o)));
const curve=(pts,o)=>add(rc.curve(pts,O(o)));
const arrow=(pts,o={})=>{curve(pts,o);const c=o.stroke||INK;const [x2,y2]=pts[pts.length-1],[x1,y1]=pts[pts.length-2];const a=Math.atan2(y2-y1,x2-x1),L=26;
  add(rc.polygon([[x2,y2],[x2-L*Math.cos(a-0.45),y2-L*Math.sin(a-0.45)],[x2-L*Math.cos(a+0.45),y2-L*Math.sin(a+0.45)]],O({stroke:c,fill:c,fillStyle:'solid'})));};
// violet highlighter swipe behind something: call BEFORE drawing the ink on top
const highlight=(x,y,w,h)=>{const g=add(rc.rectangle(x,y,w,h,O({stroke:'none',fill:VIOLET,fillStyle:'solid',roughness:2.2})));g.setAttribute('opacity','0.28');return g;};
const text=(s,x,y,size,anchor='middle',color=INK)=>{const t=document.createElementNS('http://www.w3.org/2000/svg','text');
  t.setAttribute('x',x);t.setAttribute('y',y);t.setAttribute('font-size',size);t.setAttribute('text-anchor',anchor);t.setAttribute('fill',color);t.textContent=s;svg.appendChild(t);};
const signature=()=>text('AE Handbook',W-60,H-50,34,'end','#666');
"""

# ---- drawing ----
# Example: the Gaps and Islands Part 1 cover. Replace with the new drawing.
drawing = """
const vals=['1','1','1','2','1','2','2']; const x0=380,cw=180,y=200;
highlight(x0-20,y-10,3*cw-10,150);                 // the island the reader should see first
vals.forEach((v,i)=>{rect(x0+i*cw,y,130,130);text(v,x0+i*cw+65,y+88,70);});
ell(x0+cw+65,y+65,3*cw+30,230,{strokeWidth:2.6});
ell(x0+3*cw+65,y+65,cw+5,215,{strokeWidth:2.6});
ell(x0+4*cw+65,y+65,cw+5,215,{strokeWidth:2.6});
ell(x0+5.5*cw+65,y+65,2*cw+30,225,{strokeWidth:2.6});
text('island',x0+cw+65,y-45,54); text('island',x0+5.5*cw+65,y-45,54);
text('gap',x0+3.5*cw+65,y+250,46);
arrow([[x0+3.5*cw+65,y+210],[x0+3.5*cw+60,y+175],[x0+3.5*cw+65,y+150]],{strokeWidth:2,stroke:BLUE});
text('Leetcode Series: Gaps and Islands',1000,690,92); text('Part 1',1000,800,80);
const yb=1010, flags=['1','0','0','1','1','1','0'], sums=['1','1','1','2','3','4','4'];
flags.forEach((f,i)=>{text(f,x0+i*cw+65,yb+60,64);text(sums[i],x0+i*cw+65,yb+250,64);});
text('change flag',x0-70,yb+60,46,'end'); text('running sum',x0-70,yb+250,46,'end');
arrow([[x0-200,yb+85],[x0-160,yb+150],[x0-200,yb+200]],{strokeWidth:2.4});
line(x0-20,yb+130,x0+7*cw,yb+128,{strokeWidth:2});
signature();
"""
# ---- drawing ----

html = f"""<style>@font-face{{font-family:hand;src:url(data:font/woff2;base64,{font})}}
body{{margin:0}} svg{{display:block;background:#fff}} text{{font-family:hand}}</style>
<svg id=s width={W} height={H} viewBox="0 0 {W} {H}"></svg>
<script>{rough}</script><script>const W={W},H={H};{helpers}{drawing}</script>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': W, 'height': H})
    pg.on('pageerror', lambda e: print('JS ERROR:', e))
    pg.set_content(html)
    pg.wait_for_timeout(500)
    pg.screenshot(path=OUT)
    b.close()
print('saved', OUT)
```

If the PNG comes out blank, read the `JS ERROR` line: usually a typo in the drawing code or a variable declared twice. Use a fresh page for each image, as the script does.

## Putting it on Substack

For a cover, the drawing goes in as the first image of the post body (an image node with `topImage: false`) and as the post's `cover_image`, so the social preview and the archive thumbnail show the drawing instead of whatever image comes first. A post that is already live only changes after pressing Update in the editor. Changing a live post never needs to send another email.

## Don'ts

- No logos, mascots or brand characters, and no copying another writer's drawings.
- No more than one violet swipe and one blue accent. If everything is highlighted, nothing is.
- No numbers that are not true. If the post's example data is available, use it.
- No paragraphs inside the drawing. Labels are one to three words, and the title is the post title.