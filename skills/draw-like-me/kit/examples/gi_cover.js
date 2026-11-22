// size: 2000x1429
const vals=['1','1','1','2','1','2','2']; const x0=380,cw=180,y=200;
highlight(x0-20,y-10,3*cw-10,150);
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
