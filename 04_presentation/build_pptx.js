/* Build an editable PowerPoint from the GraphML_G02 HTML deck.
   Run:  NODE_PATH=$(npm root -g) node build_pptx.js   (from 04_presentation/) */
const pptxgen = require("pptxgenjs");
const P = new pptxgen();
P.defineLayout({ name: "S", width: 13.333, height: 7.5 });
P.layout = "S";
P.author = "GraphML_G02";
P.title = "Graph Learning Pipeline for Architectural Floor Plans";

// ── helpers ──────────────────────────────────────────────────────────────────
const i  = px => +(px / 144).toFixed(3);     // px(1920-wide) -> inches
const pt = px => +(px * 0.5).toFixed(1);     // px -> points
const SERIF = "Georgia", SANS = "Calibri", MONO = "Consolas";

// colours
const C = {
  c0:"440154", c1:"472d7b", c2:"3b528b", c3:"2c728e", c4:"21908c",
  c5:"27ad81", c6:"5ec962", c7:"addc30", c8:"fde725",
  teal:"21908c", green:"5ec962", yellow:"fde725", amber:"e8b84b", red:"ff5e54", blue:"4a6f9c",
  white:"f3f5f8", grey:"9aa1ac", dgrey:"5b626d", line:"262a32",
  panel:"14161b", panel2:"1c1f26", bg:"000000",
};
const ROOMS = [["440154","bedroom"],["472d7b","living"],["3b528b","kitchen"],["2c728e","dining"],
  ["21908c","corridor"],["27ad81","stairs"],["5ec962","storeroom"],["addc30","bathroom"],["fde725","balcony"]];

const PADX = 80;            // left/right content padding (px)
const CW = 1920 - 2*PADX;   // content width px

function newSlide() { const s = P.addSlide(); s.background = { color: C.bg }; return s; }

function rect(s, xpx, ypx, wpx, hpx, fill, opt={}) {
  s.addShape(P.shapes.RECTANGLE, { x:i(xpx), y:i(ypx), w:i(wpx), h:i(hpx),
    fill:{ color:fill, ...(opt.transparency!=null?{transparency:opt.transparency}:{}) },
    line:{ type:"none" }, ...(opt.radius?{}: {}) });
}
function rrect(s, xpx, ypx, wpx, hpx, fill, rad=0.08) {
  s.addShape(P.shapes.ROUNDED_RECTANGLE, { x:i(xpx), y:i(ypx), w:i(wpx), h:i(hpx),
    fill:{ color:fill }, line:{ type:"none" }, rectRadius:rad });
}
function T(s, runs, xpx, ypx, wpx, hpx, o={}) {
  const arr = Array.isArray(runs) ? runs : [{ text:runs }];
  s.addText(arr, { x:i(xpx), y:i(ypx), w:i(wpx), h:i(hpx),
    align:o.align||"left", valign:o.valign||"top", margin:o.margin!=null?o.margin:0,
    fontFace:o.font||SANS, fontSize:o.size||pt(36), color:o.color||C.white,
    bold:o.bold||false, italic:o.italic||false, charSpacing:o.cs||0,
    lineSpacingMultiple:o.lsm||undefined, paraSpaceAfter:o.psa||undefined, wrap:true });
}
// spaced uppercase eyebrow + serif title (NO accent line per request kept subtle)
function header(s, eyebrow, title, titleRuns) {
  T(s, [{text:"● ", options:{color:C.teal}}, {text:eyebrow.toUpperCase(), options:{color:C.grey}}],
    PADX, 60, CW, 40, { font:SANS, size:pt(21), cs:3, bold:false });
  if (titleRuns) T(s, titleRuns, PADX, 96, CW, 130, { font:SERIF, size:pt(74), bold:true });
  else T(s, title, PADX, 96, CW, 130, { font:SERIF, size:pt(74), bold:true });
  rect(s, PADX, 214, 920, 3, C.teal);          // thin teal rule (deck identity)
}
function footer(s, n) {
  T(s, "GraphML_G02", PADX, 990, 400, 40, { font:MONO, size:pt(19), color:C.dgrey });
  T(s, `${String(n).padStart(2,"0")} / 18`, 1920-PADX-400, 990, 400, 40,
    { font:MONO, size:pt(19), color:C.dgrey, align:"right" });
}
// room-type legend strip across [x,x+w]
function legend(s, xpx, ypx, wpx, opt={}) {
  const n = ROOMS.length, sw = wpx / n;
  ROOMS.forEach(([col,name], k) => {
    const sx = xpx + k*sw;
    rect(s, sx+2, ypx, sw-6, 16, col);
    T(s, opt.nonum ? name : `${k} – ${name}`, sx, ypx+22, sw, 26,
      { size:pt(15), color:C.grey, align:"center" });
  });
}
function thermal(s, xpx, ypx, wpx, ll, lr) {
  const stops=[[210,35,20],[240,150,30],[250,220,50],[60,180,120],[20,70,200]];
  const segs=24, sw=wpx/segs;
  const lerp=(a,b,t)=>Math.round(a+(b-a)*t);
  for (let k=0;k<segs;k++){
    const t=k/(segs-1), f=t*(stops.length-1), j=Math.min(stops.length-2,Math.floor(f)), r=f-j;
    const col=stops[j].map((v,m)=>lerp(v,stops[j+1][m],r));
    const hex=col.map(v=>v.toString(16).padStart(2,"0")).join("");
    rect(s, xpx+k*sw, ypx, sw+0.5, 14, hex);
  }
  T(s, ll, xpx, ypx+20, wpx/2, 24, { size:pt(17), color:C.grey });
  T(s, lr, xpx+wpx/2, ypx+20, wpx/2, 24, { size:pt(17), color:C.grey, align:"right" });
}
const dot = (col) => ({ text:"■ ", options:{ color:col } });
const imgContain = (s, path, xpx, ypx, wpx, hpx) =>
  s.addImage({ path, sizing:{ type:"contain", w:i(wpx), h:i(hpx) }, x:i(xpx), y:i(ypx), w:i(wpx), h:i(hpx) });

// ════════════════ 01 · TITLE ════════════════
(() => {
  const s = newSlide();
  s.addShape(P.shapes.OVAL, { x:i(900), y:i(-200), w:i(1400), h:i(1100), fill:{color:C.c1,transparency:78}, line:{type:"none"} });
  s.addShape(P.shapes.OVAL, { x:i(-300), y:i(500), w:i(1200), h:i(1000), fill:{color:C.teal,transparency:82}, line:{type:"none"} });
  // network motif
  const nodes=[[300,240,C.green,7],[760,300,C.green,6],[1320,320,C.green,6],[520,380,C.red,17],
    [900,500,C.red,15],[1680,360,C.red,14],[430,600,C.teal,7],[640,720,C.teal,8],[1520,540,C.teal,7]];
  [[0,3],[3,1],[1,4],[3,6],[6,7],[4,7],[2,5],[5,8]].forEach(([a,b])=>{
    s.addShape(P.shapes.LINE,{ x:i(nodes[a][0]),y:i(nodes[a][1]),w:i(nodes[b][0]-nodes[a][0]),h:i(nodes[b][1]-nodes[a][1]),line:{color:C.teal,width:1,transparency:55} });
  });
  nodes.forEach(([x,y,col,r])=> s.addShape(P.shapes.OVAL,{ x:i(x-r),y:i(y-r),w:i(2*r),h:i(2*r),fill:{color:col},line:{type:"none"} }));
  T(s, [{text:"● ",options:{color:C.teal}},{text:"GRAPHML · GROUP 02",options:{color:C.grey}}], 96, 80, 1000, 40, { size:pt(22), cs:3 });
  T(s, [{text:"Graph Learning Pipeline\n",options:{}},{text:"for Architectural ",options:{}},{text:"Floor Plans",options:{color:C.green}}],
    96, 470, 1500, 250, { font:SERIF, size:pt(96), bold:true, lsm:1.0 });
  T(s, "Node classification on the Narkomfin Building using GraphSAGE — from redrawn geometry to a labelled spatial graph and predicted room types.",
    96, 740, 1300, 120, { size:pt(32), color:C.grey });
  rect(s, 96, 884, 1728, 1, C.line);
  T(s, [{text:"FINAL ASSIGNMENT\n",options:{color:C.teal,bold:true,cs:2}},{text:"MaCAD 2025/26 · IAAC\nDigital Tools for Graph Machine Learning",options:{color:C.dgrey}}],
    96, 910, 900, 120, { size:pt(20) });
  T(s, "Lakzhmy Zaro · María Sánchez\nCharles Abi Chahine · Emilie El Chidiac",
    1920-96-900, 916, 900, 120, { size:pt(22), color:C.grey, align:"right" });
})();

// ════════════════ 02 · CONTENTS ════════════════
(() => {
  const s = newSlide();
  header(s, "Contents", "What we cover.");
  const rows = [
    ["01","Modified Swiss Dwellings","A benchmark of 5,372 residential floor plans encoded as spatial graphs",C.c0],
    ["02","Literature","Two papers and one pretrained GraphSAGE-Pool model",C.c2],
    ["03","Data Structure","Nodes, edges, features and ground-truth room-type labels",C.c4],
    ["04","The Narkomfin Building","Dom-kommuna, two unit types, one ideal graph-ML subject",C.c5],
    ["05","Graph Analysis","Centrality measures, shortest paths and spatial logic",C.c7],
    ["06","Node Classification","Room-type prediction from zoning features using GraphSAGE",C.c8],
  ];
  let y = 300; const rh = 108;
  rows.forEach(([num,title,desc,col])=>{
    rect(s, PADX, y, CW, 1, C.line);
    T(s, num, PADX, y+24, 110, 60, { font:SERIF, size:pt(40), bold:true, color:col });
    T(s, title, PADX+150, y+22, 1200, 50, { size:pt(30), bold:true });
    T(s, desc, PADX+150, y+64, 1400, 40, { size:pt(21), color:C.dgrey });
    y += rh;
  });
  rect(s, PADX, y, CW, 1, C.line);
  footer(s, 1);
})();

// ════════════════ 03 · DATASET ════════════════
(() => {
  const s = newSlide();
  header(s, "01 — Dataset", "Modified Swiss Dwellings.");
  // chips
  const chips=["5,372 floor plans","Multi-apartment clusters","Corridor buildings","Single units","Graph modality"];
  let cx=PADX;
  chips.forEach((c,k)=>{ const w=c.length*11+44; rrect(s,cx,250,w,46,k===0?"143a39":C.panel,0.12);
    T(s,c,cx,250,w,46,{size:pt(20),color:k===0?"7fe3dd":C.grey,align:"center",valign:"middle"}); cx+=w+14; });
  imgContain(s, "img/samples3_tight.png", PADX, 330, CW, 360);
  T(s, "Three sample plans — a wide variety of residential typologies, scales and orientations · node colour encodes room type",
    PADX, 706, CW, 30, { size:pt(18), color:C.dgrey, align:"center" });
  // stats
  const stats=[["5,372","Floor Plans"],["9","Room Types"],["4","Zone Types"],[".pickle","Graph Format"]];
  const sw=(CW-3*16)/4;
  stats.forEach(([v,l],k)=>{ const x=PADX+k*(sw+16); rrect(s,x,760,sw,150,C.panel,0.06);
    T(s,v,x+26,786,sw-40,70,{font:SERIF,size:pt(v.length>4?40:58),bold:true});
    T(s,l,x+26,860,sw-40,40,{size:pt(22),color:C.grey}); });
  footer(s, 2);
})();

// ════════════════ 04 · LITERATURE ════════════════
(() => {
  const s = newSlide();
  header(s, "02 — Literature", "Two papers, one pipeline.");
  const colW=(CW-48)/2, top=300, ch=560;
  const cards=[
    [PADX,C.teal,"PAPER 01","MSD: A Benchmark Dataset for Floor Plan Generation of Building Complexes","ECCV 2024 · TU Delft",
      ["5,372 Swiss residential floor plans","3 modalities: image, geometry, graph","Graph encodes spatial zones, not room types"],"Primary data source for this project."],
    [PADX+colW+48,C.green,"PAPER 02","GNN for Node Classification & Attribute Allocation in Architectural BIM","eCAADe 2024 · Cardiff University",
      ["Same MSD dataset, graphs via TopologicPy","Benchmarks GCN, GAT, GraphSAGE","GraphSAGE-Pool, 4 layers, ~95% accuracy"],"Pretrained model applied to our floor plan."],
  ];
  cards.forEach(([x,acc,tag,title,src,bullets,note])=>{
    rrect(s,x,top,colW,ch,C.panel,0.05);
    T(s,tag,x+40,top+34,colW-80,40,{size:pt(18),bold:true,color:acc,cs:2});
    T(s,title,x+40,top+78,colW-80,110,{font:SERIF,size:pt(30),bold:true,lsm:1.05});
    T(s,src,x+40,top+205,colW-80,30,{font:MONO,size:pt(18),color:C.grey});
    T(s,bullets.map((b,k)=>({text:b,options:{bullet:{indent:18},color:C.grey,breakLine:true,paraSpaceAfter:10}})),
      x+40,top+260,colW-80,180,{size:pt(23)});
    rrect(s,x+40,top+ch-100,colW-80,64,"0d0f13",0.08);
    T(s,note,x+58,top+ch-100,colW-116,64,{size:pt(19),color:C.grey,valign:"middle"});
  });
  footer(s, 3);
})();

// ════════════════ 05 · DATA STRUCTURE ════════════════
(() => {
  const s = newSlide();
  header(s, "03 — Data Structure", "What the graph encodes.");
  const gw=(CW-20)/2, gh=290, top=300;
  const pos=[[PADX,top],[PADX+gw+20,top],[PADX,top+gh+20],[PADX+gw+20,top+gh+20]];
  const tbl=(x,y,title,head,rows,colW)=>{
    rrect(s,x,y,gw,gh,C.panel,0.05);
    T(s,title,x+26,y+20,gw-52,40,{size:pt(26),bold:true});
    s.addTable([head.map(h=>({text:h,options:{color:C.grey,bold:true,fontSize:pt(15),fill:{color:C.panel}}}))].concat(
      rows.map(r=>r.map((c,ci)=>({text:String(c.t!=null?c.t:c),options:{color:c.col||(ci===0?C.white:C.grey),bold:ci===0,fontSize:pt(17),fill:{color:C.panel}}})))),
      { x:i(x+22), y:i(y+72), w:i(gw-44), colW:colW.map(w=>i((gw-44)*w)), border:{type:"none"}, fontFace:MONO,
        rowH:i(34), valign:"middle" });
  };
  tbl(pos[0][0],pos[0][1],"graph_in — model input",["Attribute","Type","Values"],
    [[{t:"zoning_type",col:"7fe3dd"},"int","0 · 1 · 2 · 3"],[{t:"connectivity",col:"7fe3dd"},"str","'door' · 'entrance'"]],[.35,.18,.47]);
  tbl(pos[1][0],pos[1][1],"graph_out — ground truth",["Attribute","Type","Description"],
    [[{t:"room_type",col:"9be7b6"},"int","0 – 8"],[{t:"geometry",col:"9be7b6"},"Polygon","2D room outline"],[{t:"centroid",col:"9be7b6"},"Point","centre of room"]],[.32,.22,.46]);
  tbl(pos[2][0],pos[2][1],"Room types (0 – 8)",["ID","Room","ID","Room"],
    [["0","Bedroom","5","Stairs"],["1","Living room","6","Storeroom"],["2","Kitchen","7","Bathroom"],["3","Dining","8","Balcony"],["4","Corridor","",""]],[.1,.4,.1,.4]);
  tbl(pos[3][0],pos[3][1],"Zone types (0 – 3)",["ID","Zone","Typical rooms"],
    [["0","Private","bedroom"],["1","Dynamic","corridor, entrance"],["2","Static","bedroom, bathroom"],["3","Functional","kitchen, storeroom"]],[.1,.26,.64]);
  footer(s, 4);
})();

// ════════════════ 06 · PLAN → GRAPH ════════════════
(() => {
  const s = newSlide();
  header(s, "03 — Data Structure", "From floor plan to graph.");
  const fb=[["Zone label per node","zoning_type input",C.c1],["Graph topology","door / entrance edges",C.c4],["Room type prediction","GraphSAGE-Pool output",C.c8]];
  const fw=(CW-2*70)/3;
  fb.forEach(([t,sub,col],k)=>{ const x=PADX+k*(fw+70); rrect(s,x,250,fw,82,C.panel,0.08);
    rect(s,x,250,fw,4,col);
    T(s,t,x+20,262,fw-40,34,{size:pt(24),bold:true}); T(s,sub,x+20,298,fw-40,28,{font:MONO,size:pt(17),color:C.grey});
    if(k<2) T(s,"→",x+fw+18,268,34,40,{size:pt(28),color:C.dgrey}); });
  imgContain(s, "img/plan_graph-2_tight.png", PADX, 360, CW, 470);
  // two legends
  T(s,"ROOM TYPES — LEFT PLAN",PADX,850,CW/2,24,{font:MONO,size:pt(15),color:C.dgrey,cs:1});
  legend(s, PADX, 884, CW/2-40, {nonum:true});
  T(s,"ZONE TYPES — RIGHT PLAN",PADX+CW/2,850,420,24,{font:MONO,size:pt(15),color:C.dgrey,cs:1});
  const zones=[["E8DAEF","0 – Private"],["D5F5E3","1 – Dynamic"],["FDEBD0","2 – Static"],["D6EAF8","3 – Functional"]];
  const zw=460/4;
  zones.forEach(([col,nm],k)=>{ const x=PADX+CW/2+k*zw; rect(s,x,884,zw-6,16,col); T(s,nm,x,906,zw,24,{size:pt(14),color:C.grey,align:"center"}); });
  T(s,"EDGE TYPES",PADX+CW/2+520,850,300,24,{font:MONO,size:pt(15),color:C.dgrey,cs:1});
  rect(s,PADX+CW/2+520,890,40,5,C.blue); T(s,"door",PADX+CW/2+570,884,120,24,{size:pt(16),color:C.grey});
  rect(s,PADX+CW/2+520,924,40,5,"c0392b"); T(s,"entrance",PADX+CW/2+570,918,140,24,{size:pt(16),color:C.grey});
  footer(s, 5);
})();

// ════════════════ 07 · PIPELINE ════════════════
(() => {
  const s = newSlide();
  header(s, "Process", "One building, two paths, one read.");
  // bookends
  const bw=210, fullTop=380, fullBot=900, fh=fullBot-fullTop;
  rrect(s,PADX,fullTop,bw,fh,C.panel,0.05);
  T(s,"DECISION",PADX,fullTop+34,bw,30,{size:pt(13),bold:true,cs:2,align:"center"});
  T(s,"The\nNarkomfin",PADX,fullTop+fh/2-50,bw,80,{font:SERIF,size:pt(30),bold:true,align:"center",lsm:1.05});
  T(s,"our case study",PADX,fullTop+fh/2+40,bw,30,{size:pt(16),color:C.grey,align:"center"});
  const ex=1920-PADX-bw;
  rrect(s,ex,fullTop,bw,fh,C.panel,0.05);
  T(s,"OUTCOME",ex,fullTop+34,bw,30,{size:pt(13),bold:true,cs:2,align:"center",color:C.green});
  T(s,"Conclusion",ex,fullTop+fh/2-30,bw,60,{font:SERIF,size:pt(30),bold:true,align:"center"});
  T(s,"what the graph knows",ex,fullTop+fh/2+40,bw,30,{size:pt(16),color:C.grey,align:"center"});
  // lanes
  const laneX=PADX+bw+70, geomW=300, stageX=laneX+geomW+70, stageW=600, predX=stageX+stageW+44, predW=290;
  const r1=410, r2=660, nodeH=200, subY1=560, subY2=810;
  const geom=(x,y,nm,sub,acc)=>{ rrect(s,x,y,geomW,nodeH,C.panel,0.06); rect(s,x,y,4,nodeH,acc);
    T(s,"GEOMETRY",x+24,y+22,geomW-40,24,{size:pt(13),bold:true,color:acc,cs:1});
    T(s,nm,x+24,y+70,geomW-40,40,{size:pt(32),bold:true}); T(s,sub,x+24,y+128,geomW-40,30,{size:pt(18),color:C.grey}); };
  const stage=(x,y,w,title,desc,step,acc)=>{ rrect(s,x,y,w,nodeH,C.panel,0.06); rect(s,x,y,4,nodeH,acc);
    T(s,title,x+26,y+22,w-50,40,{size:pt(30),bold:true});
    T(s,desc,x+26,y+76,w-50,40,{size:pt(18),color:C.grey});
    T(s,step,x+26,y+128,w-50,50,{font:MONO,size:pt(15),color:C.teal}); };
  const sub=(x,y,w,txt,acc)=>{ rrect(s,x,y,w,150,"101319",0.06);
    T(s,"HOW IT WORKS",x+18,y+14,w-36,24,{font:MONO,size:pt(13),bold:true,color:acc,cs:1});
    T(s,txt,x+18,y+44,w-36,100,{size:pt(15),color:C.grey,lsm:1.05}); };
  const arrow=(x,y)=>T(s,"→",x,y,50,40,{size:pt(28),color:C.dgrey});
  geom(laneX,r1,"Floor Plan","2D plan, redrawn",C.c1); arrow(laneX-58,r1+80);
  stage(stageX,r1,stageW,"Spatial Analysis","How each room sits within the circulation network.","02.1 OBJ→BREP · 02.2–02.4 centrality & shortest path",C.c4);
  arrow(stageX-58,r1+80);
  sub(stageX,subY1,stageW,"The plan is grid-sliced into a Topologic shell, then navigation & analysis graphs are derived. Metrics: closeness = integration, betweenness = choice, plus degree, community detection and isovist visibility.",C.c4);
  geom(laneX,r2,"Simplified 3D","rooms as volumes",C.c1); arrow(laneX-58,r2+80);
  stage(stageX,r2,stageW,"Graph Preparation","Encode the 3D model as a labelled input graph.","03.0 Rhino→cell complex · 03.1 label nodes & edges",C.c5);
  arrow(stageX-58,r2+80); arrow(stageX+stageW+4,r2+80);
  stage(predX,r2,predW,"Prediction","Infer room types from zoning.","03.2 GraphSAGE-Pool",C.c8);
  sub(stageX,subY2,stageW,"Named Rhino room volumes + aperture surfaces build a TopologicPy CellComplex & room graph. MSD features encoded: 4-class zoning_type, door / passage / entrance connectivity, exported to CSV for GraphSAGE.",C.c5);
  arrow(PADX+bw+8,fullTop+fh/2-20); arrow(ex-58,fullTop+fh/2-20);
  footer(s, 6);
})();

// ── shared hero-image slides (08,09,10) ──
function heroImage(s, path, topPx=180) { imgContain(s, path, PADX, topPx, CW, 640); }

// ════════════════ 08 · NARKOMFIN INTRO ════════════════
(() => {
  const s = newSlide();
  header(s, "04 — The Narkomfin Building", "A machine for collective living.");
  imgContain(s, "img/pngs/actual-3d_tight.png", PADX, 250, CW, 560);
  const meta=[["Architects","Ginzburg & Milinis",C.c1],["Year","1930",C.c3],["Location","Moscow, Russia",C.c4],
    ["Typology","Dom-kommuna",C.c5],["Scale","54 units · 6 floors",C.c6],["Unit types","F · K",C.c8]];
  const mw=(CW-5*12)/6;
  meta.forEach(([k,v,acc],idx)=>{ const x=PADX+idx*(mw+12); rrect(s,x,840,mw,96,"1a1d24",0.06); rect(s,x,840,mw,4,acc);
    T(s,k.toUpperCase(),x+16,856,mw-28,22,{size:pt(14),color:C.dgrey,cs:1}); T(s,v,x+16,884,mw-28,40,{size:pt(20),bold:true}); });
  footer(s, 7);
})();

// ════════════════ 09 · WHY GRAPH ML ════════════════
(() => {
  const s = newSlide();
  header(s, "04 — The Narkomfin Building", "Why it maps to graph ML.");
  imgContain(s, "img/pngs/actual-3d_tight.png", PADX, 230, CW, 470);
  const reasons=[["01","Clear spatial hierarchy","Discrete living cells and corridors form a readable room-to-room structure.",C.c1],
    ["02","Repetitive unit typologies","Two unit types — F-type and K-type — repeat cleanly across every floor.",C.c4],
    ["03","Explicit functional zoning","A dom-kommuna where living, communal and circulation zones are clearly defined.",C.c5]];
  const rw=(CW-2*26)/3;
  reasons.forEach(([n,t,d,acc],idx)=>{ const x=PADX+idx*(rw+26); rrect(s,x,760,rw,170,C.panel,0.06);
    T(s,n,x+26,778,rw-40,30,{font:MONO,size:pt(20),bold:true,color:acc});
    T(s,t,x+26,816,rw-40,40,{font:SERIF,size:pt(27),bold:true});
    T(s,d,x+26,866,rw-40,60,{size:pt(20),color:C.grey,lsm:1.05}); });
  footer(s, 8);
})();

// ════════════════ 10 · SIMPLIFIED MODEL ════════════════
(() => {
  const s = newSlide();
  header(s, "04 — The Narkomfin Building", "Simplified model, rooms as volumes.");
  imgContain(s, "img/pngs/simplified-3d_tight.png", PADX, 250, CW, 580);
  T(s,"NODE COLOUR ENCODES ROOM TYPE",PADX,856,CW,24,{font:MONO,size:pt(15),color:C.dgrey,cs:1});
  legend(s, PADX, 892, CW);
  footer(s, 9);
})();

// ════════════════ 11 · EXPLODED AXON ════════════════
(() => {
  const s = newSlide();
  header(s, "04 — The Narkomfin Building", "Exploded axonometric by floor type.");
  imgContain(s, "img/pngs/simplified-3d-exploded_tight.png", PADX, 250, CW, 580);
  const fl=(t,xpx,ypx)=>{ const w=t.length*15+36; rrect(s,xpx,ypx,w,46,"000000cc"?"0a0c10":"0a0c10",0.1);
    T(s,t,xpx,ypx,w,46,{size:pt(24),bold:true,align:"center",valign:"middle"}); };
  fl("F-type", PADX+CW*0.62, 320);
  fl("Amenities", PADX+CW*0.02, 600);
  fl("K-type", PADX+CW*0.30, 760);
  T(s,"NODE COLOUR ENCODES ROOM TYPE",PADX,856,CW,24,{font:MONO,size:pt(15),color:C.dgrey,cs:1});
  legend(s, PADX, 892, CW);
  footer(s, 10);
})();

// ════════════════ 12 · FIVE LEVELS ════════════════
(() => {
  const s = newSlide();
  header(s, "04 — The Narkomfin Building", "K-type & F-type, five levels.");
  imgContain(s, "img/pngs/exploded-levels.png", PADX, 260, CW, 540);
  const lab=(t,xpx,ypx,acc)=>{ const w=t.length*16+34; rrect(s,xpx,ypx,w,44,"0a0c10",0.1);
    T(s,t,xpx,ypx,w,44,{size:pt(23),bold:true,align:"center",valign:"middle",color:acc||C.white}); };
  lab("K-type",PADX+CW*0.42,440,C.teal); lab("L2",PADX+CW*0.44,500); lab("L1",PADX+CW*0.44,690);
  lab("F-type",PADX+CW*0.92,300,C.teal); lab("L5",PADX+CW*0.93,360); lab("L4",PADX+CW*0.93,560); lab("L3",PADX+CW*0.93,740);
  T(s,"NODE COLOUR ENCODES ROOM TYPE",PADX,856,CW,24,{font:MONO,size:pt(15),color:C.dgrey,cs:1});
  legend(s, PADX, 892, CW);
  footer(s, 11);
})();

// ── analysis slides 13,14,15 ──
function analysis(s, n, sub, title, img, bullets, acc, strip) {
  header(s, "05 — Graph Analysis", title);
  imgContain(s, img, PADX, 260, CW*0.56, 560);
  const bx=PADX+CW*0.6, bw=CW*0.4;
  T(s, bullets.map(b=>({text:b.t!=null?b.t:b,options:{bullet:{indent:18},color:C.grey,bold:b.b||false,breakLine:true,paraSpaceAfter:18}})),
    bx, 360, bw, 360, { size:pt(25) });
  strip(s, bx, 720, bw);
  footer(s, n);
}
(() => { const s=newSlide(); analysis(s,12,"05 — Graph Analysis","Closeness centrality, Type K.","img/plan1-closeness-centrality.png",
  [{t:"Corridor scores highest — fewest steps to every room",b:true},"Closeness drops steadily into private cells","Staircase block scores lowest — dead-end terminal","Corridor is the social and circulatory core"],
  C.c4,(s,x,y,w)=>thermal(s,x,y,w,"high integration","low integration")); })();
(() => { const s=newSlide(); analysis(s,13,"05 — Graph Analysis","Betweenness centrality, Type K.","img/plan1-betweenness-centrality.png",
  [{t:"Central corridor sections carry the most traffic",b:true},"Every cross-building journey passes through them","End rooms have near-zero betweenness — destinations only","Corridor is the most traversed and most accessible spine"],
  C.c8,(s,x,y,w)=>thermal(s,x,y,w,"high traffic","low traffic")); })();
(() => { const s=newSlide(); header(s,"05 — Graph Analysis","Shortest path, Type K.");
  imgContain(s,"img/plan1-shortest-path.png",PADX,260,CW*0.56,560);
  const bx=PADX+CW*0.6, bw=CW*0.4;
  T(s,[{text:"Grid and straightened paths are nearly identical",options:{bullet:{indent:18},color:C.grey,breakLine:true,paraSpaceAfter:18}},
    {text:"Only 3.7% shorter when straightened",options:{bullet:{indent:18},color:C.grey,bold:true,breakLine:true,paraSpaceAfter:18}},
    {text:"Corridor is already the straightest possible route",options:{bullet:{indent:18},color:C.grey,breakLine:true,paraSpaceAfter:18}},
    {text:"Optimal path and only social route are the same",options:{bullet:{indent:18},color:C.grey}}],bx,360,bw,300,{size:pt(25)});
  rect(s,bx,700,26,6,"ff453a"); T(s,"grid path · 77.2 u",bx+40,692,300,24,{size:pt(18),color:C.grey,font:MONO});
  rect(s,bx,740,26,6,"0a84ff"); T(s,"straightened · 74.4 u",bx+40,732,320,24,{size:pt(18),color:C.grey,font:MONO});
  footer(s,14); })();

// ── prediction slides 16,17 (results top, images mid, legend bottom) ──
function prediction(s, n, type, accc, acc, lbl, stats, conf, insight, gtImg, prImg) {
  header(s, "06 — Node Classification", `Room type prediction, ${type}.`);
  // results band
  const ry=250, rleftW=CW*0.30;
  T(s,[{text:acc,options:{}},{text:"%",options:{fontSize:pt(40)}}],PADX,ry,rleftW,90,{font:SERIF,size:pt(80),bold:true,color:accc});
  T(s,lbl,PADX,ry+110,rleftW,30,{size:pt(18),color:C.grey});
  stats.forEach(([v,l,col],k)=>{ const x=PADX+k*(rleftW/3); T(s,v,x,ry+150,rleftW/3,50,{font:SERIF,size:pt(36),bold:true,color:col});
    T(s,l.toUpperCase(),x,ry+210,rleftW/3,24,{size:pt(14),color:C.grey,cs:1}); });
  const cx=PADX+rleftW+44, cw=CW-rleftW-44;
  T(s,"WHERE IT WENT WRONG · TRUE → PREDICTED",cx,ry,cw,24,{font:MONO,size:pt(15),color:C.grey,cs:1});
  conf.forEach(([cnt,a,ac,b,bc,frac],k)=>{ const y=ry+40+k*46;
    T(s,String(cnt),cx,y,46,40,{font:SERIF,size:pt(28),bold:true,color:"ff6a5e",align:"right"});
    T(s,[dot(ac),{text:a+"  ",options:{color:C.white}},{text:"→  ",options:{color:C.dgrey}},dot(bc),{text:b,options:{color:C.grey}}],
      cx+62,y+4,cw-360,36,{size:pt(21)});
    rect(s,cx+cw-150,y+14,150,8,"24262c"); rect(s,cx+cw-150,y+14,Math.max(6,150*frac),8,"ff6a5e"); });
  T(s,insight,cx,ry+40+conf.length*46+14,cw,40,{size:pt(18),color:C.grey});
  // images
  const iy=540, half=(CW-30)/2;
  T(s,"Ground truth",PADX,iy,half,30,{size:pt(22),bold:true,align:"center"});
  T(s,"Prediction",PADX+half+30,iy,half,30,{size:pt(22),bold:true,align:"center",color:C.teal});
  imgContain(s,gtImg,PADX,iy+40,half,300); imgContain(s,prImg,PADX+half+30,iy+40,half,300);
  legend(s, PADX, 900, CW);
  footer(s, n);
}
(() => { const s=newSlide(); prediction(s,15,"K-type",C.amber,"67.9","rooms correctly classified · 55 / 81",
  [["55","Correct",C.green],["26","Errors",C.red],["81","Rooms",C.white]],
  [[10,"Living room","472d7b","Kitchen","3b528b",1.0],[9,"Stairs","27ad81","Storeroom","5ec962",0.9],[6,"Living room","472d7b","Corridor","21908c",0.6],[1,"Stairs","27ad81","Bathroom","addc30",0.1]],
  "Errors cluster on rooms with near-identical connectivity — living rooms read as kitchens and stairs as storerooms.",
  "img/prediction/type-k-ground-truth.png","img/prediction/type-k-prediction.png"); })();
(() => { const s=newSlide(); prediction(s,16,"F-type",C.green,"91.3","rooms correctly classified · 210 / 230",
  [["210","Correct",C.green],["20","Errors",C.red],["230","Rooms",C.white]],
  [[16,"Kitchen","3b528b","Corridor","21908c",1.0],[2,"Living room","472d7b","Corridor","21908c",0.13],[1,"Storeroom","5ec962","Bathroom","addc30",0.06],[1,"Bathroom","addc30","Stairs","27ad81",0.06]],
  "16 of 20 errors are kitchens predicted as corridor — the single dominant blind spot; everything else is near-perfect.",
  "img/prediction/type-f-ground-truth.png","img/prediction/type-f-prediction.png"); })();

// ════════════════ 18 · CONCLUSION ════════════════
(() => {
  const s = newSlide();
  header(s, "Conclusion", "What the prediction tells us.");
  // hero compare
  T(s,[{text:"91.3",options:{}},{text:"%",options:{fontSize:pt(44)}}],560,320,360,100,{font:SERIF,size:pt(90),bold:true,color:C.green,align:"center"});
  T(s,"F-type · 210 / 230 rooms",520,430,440,30,{size:pt(19),color:C.grey,align:"center"});
  rrect(s,640,470,200,40,"000000"); s.addShape(P.shapes.ROUNDED_RECTANGLE,{x:i(648),y:i(472),w:i(184),h:i(36),fill:{type:"none"},line:{color:C.green,width:1},rectRadius:0.18});
  T(s,"IN-DISTRIBUTION",640,472,200,36,{size:pt(13),color:C.green,align:"center",valign:"middle",cs:1});
  T(s,"vs",930,360,60,40,{font:SERIF,size:pt(28),italic:true,color:C.dgrey,align:"center"});
  T(s,[{text:"67.9",options:{}},{text:"%",options:{fontSize:pt(44)}}],1000,320,360,100,{font:SERIF,size:pt(90),bold:true,color:C.amber,align:"center"});
  T(s,"K-type · 55 / 81 rooms",980,430,400,30,{size:pt(19),color:C.grey,align:"center"});
  s.addShape(P.shapes.ROUNDED_RECTANGLE,{x:i(1058),y:i(472),w:i(244),h:i(36),fill:{type:"none"},line:{color:C.amber,width:1},rectRadius:0.18});
  T(s,"OUT-OF-DISTRIBUTION",1050,472,260,36,{size:pt(13),color:C.amber,align:"center",valign:"middle",cs:1});
  T(s,[{text:"Same pretrained model, same building — ",options:{color:C.grey}},{text:"two very different results.",options:{color:C.white,bold:true}}],
    PADX,540,CW,34,{size:pt(20),align:"center"});
  const tk=[["01","It generalizes — unevenly","F-type's duplex apartments resemble the Swiss Dwellings the model trained on, so it scores 91%. K-type's communal dom-kommuna layout is unlike anything in training — accuracy falls to 68%.",C.c4],
    ["02","Errors are systematic","Mistakes aren't random — rooms sharing a connectivity signature get swapped: living rooms ↔ kitchens, stairs ↔ storerooms, open kitchens read as corridor.",C.amber],
    ["03","Topology captures convention","Connectivity alone reads conventional plans well. The Narkomfin's social-condenser program — its whole point — is exactly what challenges the model.",C.c1]];
  const tw=(CW-2*24)/3;
  tk.forEach(([n,t,d,acc],idx)=>{ const x=PADX+idx*(tw+24); rrect(s,x,620,tw,300,C.panel,0.05);
    T(s,n,x+30,640,tw-60,30,{font:MONO,size:pt(17),bold:true,color:acc});
    T(s,t,x+30,678,tw-60,70,{font:SERIF,size:pt(25),bold:true,lsm:1.05});
    T(s,d,x+30,770,tw-60,140,{size:pt(18),color:C.grey,lsm:1.1}); });
  footer(s, 17);
})();

P.writeFile({ fileName: "GraphML_G02.pptx" }).then(f => console.log("Saved", f));
