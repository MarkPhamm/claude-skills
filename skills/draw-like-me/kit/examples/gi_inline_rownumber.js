// size: 2000x1000
// Point: id minus row_number stays constant inside a streak, so it becomes the island key.
const rows=[['id','1','2','3','4','5','6','7'],['num','1','1','1','2','1','2','2'],['rn_num','1','2','3','1','4','2','3']];
const x0=700, cw=165, lx=150;
const ys=[150,300,450], yd=650;
// violet swipe first, so it sits under the ink: the "1" that breaks the streak
highlight(x0+4*cw-45, ys[2]-75, 90, yd-ys[2]+110);
rows.forEach((r,ri)=>{ text(r[0],lx,ys[ri],56,'start'); r.slice(1).forEach((v,i)=>text(v,x0+i*cw,ys[ri],56)); });
line(x0-80,ys[2]+45,x0+6*cw+80,ys[2]+42,{strokeWidth:2});
text('id - rn_num',lx,yd,56,'start');
['0','0','0','3','1','4','4'].forEach((v,i)=>text(v,x0+i*cw,yd,56));
ell(x0+cw,yd-18,3*cw+70,95,{strokeWidth:2.4});           // the first island shares key 0
arrow([[x0+4*cw+5,yd+150],[x0+4*cw-12,yd+105],[x0+4*cw,yd+55]],{stroke:BLUE,strokeWidth:2.4});
text('the 4th "1" is at id 5: it fell behind by 1, new island',x0+4*cw+20,yd+200,42,'middle',BLUE);
signature();
