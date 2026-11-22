"""Render Mark-style hand-drawn PNGs.

Usage:
    python3 /home/claude/drawing/render.py a.js [b.js ...]

Each .js file holds ONLY the drawing code (the part between the "---- drawing ----"
markers in the draw-like-me skill). Its first line must declare the canvas size:

    // size: 2000x1429        (cover)
    // size: 2000x1000        (inline, 900-1200 tall, no title)

The PNG is written next to the .js file with the same basename (a.js -> a.png).
After rendering, the script prints automatic checks:
  - CLIP   text that runs past the canvas edge (40px margin)
  - OVERLAP two text labels whose boxes overlap
Fix every warning, then still open the PNG with Read and look at it.
"""
import base64, os, re, sys
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
rough = open(os.path.join(HERE, 'node_modules/roughjs/bundled/rough.js')).read()
font = base64.b64encode(open(os.path.join(
    HERE, 'node_modules/@fontsource/architects-daughter/files/architects-daughter-latin-400-normal.woff2'), 'rb').read()).decode()

helpers = """
const svg=document.getElementById('s'); const rc=rough.svg(svg); let seed=7;
const INK='#111', BLUE='#2f6fdb', VIOLET='#7c3aed', GREY='#888';   // VIOLET = Substack theme colour
const O=(o={})=>Object.assign({stroke:INK,strokeWidth:3.2,roughness:1.6,bowing:1.2,seed:seed++},o);
const add=n=>{svg.appendChild(n);return n;};
const rect=(x,y,w,h,o)=>add(rc.rectangle(x,y,w,h,O(o)));
const ell=(cx,cy,w,h,o)=>add(rc.ellipse(cx,cy,w,h,O(o)));
const line=(x1,y1,x2,y2,o)=>add(rc.line(x1,y1,x2,y2,O(o)));
const curve=(pts,o)=>add(rc.curve(pts,O(o)));
const poly=(pts,o)=>add(rc.polygon(pts,O(o)));
const arrow=(pts,o={})=>{curve(pts,o);const c=o.stroke||INK;const [x2,y2]=pts[pts.length-1],[x1,y1]=pts[pts.length-2];const a=Math.atan2(y2-y1,x2-x1),L=26;
  add(rc.polygon([[x2,y2],[x2-L*Math.cos(a-0.45),y2-L*Math.sin(a-0.45)],[x2-L*Math.cos(a+0.45),y2-L*Math.sin(a+0.45)]],O({stroke:c,fill:c,fillStyle:'solid'})));};
// violet highlighter swipe behind something: call BEFORE drawing the ink on top
const highlight=(x,y,w,h)=>{const g=add(rc.rectangle(x,y,w,h,O({stroke:'none',fill:VIOLET,fillStyle:'solid',roughness:2.2})));g.setAttribute('opacity','0.28');return g;};
const text=(s,x,y,size,anchor='middle',color=INK)=>{const t=document.createElementNS('http://www.w3.org/2000/svg','text');
  t.setAttribute('x',x);t.setAttribute('y',y);t.setAttribute('font-size',size);t.setAttribute('text-anchor',anchor);t.setAttribute('fill',color);t.textContent=s;svg.appendChild(t);return t;};
// strike-through scribble over something (e.g. a removed row)
const cross=(x,y,w,h,o={})=>{line(x,y,x+w,y+h,o);line(x+w,y,x,y+h,o);};
const signature=()=>text('AE Handbook',W-60,H-50,34,'end','#666');
"""

check_js = """
(() => {
  const ts=[...document.querySelectorAll('text')].map(t=>{const b=t.getBBox();return {s:t.textContent,x:b.x,y:b.y,w:b.width,h:b.height};});
  const out=[]; const M=40;
  for(const t of ts){ if(t.s==='AE Handbook') continue;
    if(t.x<M||t.y<M*0.5||t.x+t.w>W-M||t.y+t.h>H-M*0.5) out.push('CLIP    "'+t.s+'" box=('+Math.round(t.x)+','+Math.round(t.y)+','+Math.round(t.x+t.w)+','+Math.round(t.y+t.h)+')'); }
  for(let i=0;i<ts.length;i++)for(let j=i+1;j<ts.length;j++){const a=ts[i],b=ts[j];
    const ox=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x), oy=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y);
    if(ox>4&&oy>6) out.push('OVERLAP "'+a.s+'" x "'+b.s+'"'); }
  return out;
})()
"""


def render(page, js_path):
    src = open(js_path).read()
    m = re.search(r'size:\s*(\d+)\s*x\s*(\d+)', src.split('\n')[0])
    if not m:
        print(f'{js_path}: first line must be "// size: WxH"')
        return
    W, H = int(m.group(1)), int(m.group(2))
    out = os.path.splitext(js_path)[0] + '.png'
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.set_viewport_size({'width': W, 'height': H})
    html = f"""<style>@font-face{{font-family:hand;src:url(data:font/woff2;base64,{font})}}
body{{margin:0}} svg{{display:block;background:#fff}} text{{font-family:hand}}</style>
<svg id=s width={W} height={H} viewBox="0 0 {W} {H}"></svg>
<script>{rough}</script><script>const W={W},H={H};{helpers}
{src}
</script>"""
    page.set_content(html)
    page.wait_for_timeout(350)
    page.screenshot(path=out)
    warns = page.evaluate(check_js) if not errors else []
    status = 'OK' if not errors and not warns else 'CHECK'
    print(f'[{status}] {out} ({W}x{H})')
    for e in errors:
        print('   JS ERROR:', e)
    for w in warns:
        print('   ', w)


if __name__ == '__main__':
    files = sys.argv[1:]
    if not files:
        print(__doc__)
        sys.exit(1)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for f in files:
            pg = b.new_page()          # fresh page per image
            render(pg, f)
            pg.close()
        b.close()
