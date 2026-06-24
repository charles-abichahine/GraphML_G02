const pptxgen = require("pptxgenjs");
const path = require("path");

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "Group 02";
pres.title = "Graph Analysis — Narkomfin Building";

const BG = "0D0D0D";
const WHITE = "FFFFFF";
const GREY = "AAAAAA";
const ACCENT = "E8A838";

const K_DIR = path.join(__dirname, "exports", "K Type");
const F_DIR = path.join(__dirname, "exports", "F Type");

function addSlideHeader(slide, section, title) {
  slide.background = { color: BG };
  slide.addText(section, {
    x: 0.5, y: 0.3, w: 9, h: 0.35,
    fontSize: 11, fontFace: "Arial", color: ACCENT, bold: true, margin: 0
  });
  slide.addText(title, {
    x: 0.5, y: 0.6, w: 9, h: 0.6,
    fontSize: 32, fontFace: "Arial", color: WHITE, bold: true, margin: 0
  });
}

function addFooter(slide, num, total) {
  slide.addText("GraphML_G02", {
    x: 0.5, y: 5.15, w: 3, h: 0.35,
    fontSize: 9, fontFace: "Arial", color: GREY, margin: 0
  });
  slide.addText(`${num} / ${total}`, {
    x: 7.5, y: 5.15, w: 2, h: 0.35,
    fontSize: 9, fontFace: "Arial", color: GREY, align: "right", margin: 0
  });
}

function makeBullets(items, opts = {}) {
  return items.map((text, i) => ({
    text,
    options: {
      bullet: true,
      breakLine: i < items.length - 1,
      fontSize: opts.fontSize || 12,
      color: opts.color || WHITE,
      fontFace: "Arial"
    }
  }));
}

// Layout: image left, bullets right
function imageLeftBulletsRight(slide, imgPath, bullets, imgW, imgH) {
  const imgX = 0.5;
  const imgY = 1.4;
  imgW = imgW || 5.0;
  imgH = imgH || 3.2;
  slide.addImage({
    path: imgPath,
    x: imgX, y: imgY, w: imgW, h: imgH,
    sizing: { type: "contain", w: imgW, h: imgH }
  });
  slide.addText(makeBullets(bullets), {
    x: imgW + 0.8, y: 1.4, w: 10 - imgW - 1.3, h: 3.6,
    valign: "top", paraSpaceAfter: 6, margin: 0
  });
}

// Layout: two images side by side with labels
function twoImages(slide, imgPathL, labelL, imgPathR, labelR, imgW, imgH) {
  imgW = imgW || 4.2;
  imgH = imgH || 2.8;
  const y = 1.6;
  slide.addText(labelL, {
    x: 0.5, y: 1.25, w: imgW, h: 0.3,
    fontSize: 11, fontFace: "Arial", color: ACCENT, bold: true, margin: 0
  });
  slide.addImage({
    path: imgPathL, x: 0.5, y: y, w: imgW, h: imgH,
    sizing: { type: "contain", w: imgW, h: imgH }
  });
  slide.addText(labelR, {
    x: 5.3, y: 1.25, w: imgW, h: 0.3,
    fontSize: 11, fontFace: "Arial", color: ACCENT, bold: true, margin: 0
  });
  slide.addImage({
    path: imgPathR, x: 5.3, y: y, w: imgW, h: imgH,
    sizing: { type: "contain", w: imgW, h: imgH }
  });
}

const TOTAL = 16;
let sn = 0;

// --- SLIDE 1: Title ---
sn++;
let s = pres.addSlide();
s.background = { color: BG };
s.addText("GRAPH ANALYSIS", {
  x: 0.5, y: 1.2, w: 9, h: 0.5,
  fontSize: 14, fontFace: "Arial", color: ACCENT, bold: true, charSpacing: 4, margin: 0
});
s.addText("Narkomfin Building\nType K & Type F Apartments", {
  x: 0.5, y: 1.8, w: 9, h: 1.6,
  fontSize: 36, fontFace: "Arial", color: WHITE, bold: true, margin: 0
});
s.addText("GraphML — Assignment 02 by Group 02\nTopologicPy + Python (Jupyter Notebook)", {
  x: 0.5, y: 3.6, w: 9, h: 0.8,
  fontSize: 13, fontFace: "Arial", color: GREY, margin: 0
});
addFooter(s, sn, TOTAL);

// --- SLIDE 2: Building Overview ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "01 — OVERVIEW", "Building Overview");
s.addText(makeBullets([
  "The Narkomfin Building (1930, Moscow) by Ginzburg & Milinis — Soviet Constructivist housing organised around collective living principles.",
  "Type K: two-storey duplex. L1 = continuous corridor floor. L2 = 11 disconnected rooms above. Corridor at the base, rooms above. 12 stair connections.",
  "Type F: three-storey unit. L2 (middle) = continuous living/corridor floor. L1 (below) and L3 (above) = fragmented rooms. Corridor in the middle. 19 stairs spanning all 3 floors.",
  "Both types share the same linear corridor spine logic but differ in vertical organisation — K is asymmetric (base corridor), F is symmetric (middle corridor).",
  "Method: 0.5-unit grid sampling, ray-casting PIP filtering, 4-neighbour adjacency, stair-edge stitching between floor pairs."
]), {
  x: 0.5, y: 1.4, w: 9, h: 3.6, valign: "top", paraSpaceAfter: 8, margin: 0
});
addFooter(s, sn, TOTAL);

// --- SLIDE 3: Building Graph — Type K ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "02 — BUILDING GRAPH", "Building graph, Type K");
imageLeftBulletsRight(s, path.join(K_DIR, "building graph_.5.png"), [
  "L1 is a dense, continuous mesh — the corridor spine runs the full length of the unit.",
  "L2 is visibly fragmented into room islands, linked to L1 only through vertical stair edges.",
  "Stair edges cluster in the centre, creating a narrow band of cross-floor connectivity.",
  "Graph density is very low — reflecting the linear, corridor-dominated topology."
]);
addFooter(s, sn, TOTAL);

// --- SLIDE 4: Building Graph — Type F ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "02 — BUILDING GRAPH", "Building graph, Type F");
imageLeftBulletsRight(s, path.join(F_DIR, "Ftype_building graph_.5.png"), [
  "L2 (middle) is the densest, most continuous mesh — the spatial backbone of the Type F.",
  "L1 (bottom) and L3 (top) are both fragmented into room islands, symmetric about the corridor.",
  "Each stair produces two vertical connections (L1→L2 and L2→L3), creating a ladder-like structure.",
  "The fragmentation is symmetric: rooms exist both above and below the corridor floor."
]);
addFooter(s, sn, TOTAL);

// --- SLIDE 5: Closeness — Type K ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "03 — CLOSENESS CENTRALITY", "Closeness centrality, Type K");
imageLeftBulletsRight(s, path.join(K_DIR, "closeness centrality_.5.png"), [
  "Highest closeness forms a hot band along the L1 main corridor, centre-to-east — the topological heart of the apartment.",
  "The gradient is strikingly linear, falling toward both ends of the corridor.",
  "L2 rooms are uniformly blue-purple — topologically deep, confirming they are destination spaces.",
  "The corridor is the primary spatial integrator. Privacy gradient runs upward from L1 to L2."
]);
addFooter(s, sn, TOTAL);

// --- SLIDE 6: Closeness — Type F ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "03 — CLOSENESS CENTRALITY", "Closeness centrality, Type F");
imageLeftBulletsRight(s, path.join(F_DIR, "Ftype_closeness centrality_.5.png"), [
  "Highest closeness sits on L2 (middle floor), concentrated at the centre of the plan.",
  "The gradient is bidirectional — accessibility decreases both downward to L1 and upward to L3.",
  "L1 and L3 rooms are uniformly blue-purple — topologically deep in both directions.",
  "The middle-floor corridor is equidistant from rooms on both sides, producing a balanced accessibility profile."
]);
addFooter(s, sn, TOTAL);

// --- SLIDE 7: Betweenness — Type K ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "04 — BETWEENNESS CENTRALITY", "Betweenness centrality, Type K");
imageLeftBulletsRight(s, path.join(K_DIR, "betweeness centrality_.5.png"), [
  "A sharp hot line runs along the L1 corridor centreline — virtually all movement passes through this single narrow band.",
  "Stair landing zones show localised betweenness spikes — critical chokepoints for vertical traffic.",
  "L2 rooms are entirely dark (near-zero betweenness) — they are topological dead ends.",
  "The corridor is not just accessible but the sole routing channel. Obstruction would sever the entire apartment."
]);
addFooter(s, sn, TOTAL);

// --- SLIDE 8: Betweenness — Type F ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "04 — BETWEENNESS CENTRALITY", "Betweenness centrality, Type F");
imageLeftBulletsRight(s, path.join(F_DIR, "Ftype_betweeness centrality_.5.png"), [
  "An equally sharp hot line on L2 — the corridor carries a double load, serving rooms on two floors.",
  "Stair landings absorb traffic from both directions (up and down), making them doubly loaded chokepoints.",
  "L1 and L3 rooms are entirely dark — pure destination spaces with no through-traffic.",
  "Any L1↔L3 path must traverse L2 as a mandatory intermediary. The corridor is more critical than in Type K."
]);
addFooter(s, sn, TOTAL);

// --- SLIDE 9: Shortest Path — side by side ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "05 — SHORTEST PATH", "Shortest path, Type K vs Type F");
twoImages(s,
  path.join(K_DIR, "shortest path_.5.png"), "TYPE K — L1 → L2",
  path.join(F_DIR, "Ftype_shortest path.png"), "TYPE F — L1 → L2 → L3"
);
s.addText(makeBullets([
  "Type K: L-shaped path — horizontal along L1 corridor, then one vertical jump to L2.",
  "Type F: Z-shaped path — vertical up to L2, horizontal along corridor, vertical up to L3.",
  "Both: straightened (blue) path closely tracks topological (red) — the narrow corridor leaves little room for geometric optimisation.",
  "The L2 corridor segment dominates the Type F path. Stair placement controls cross-floor routing efficiency in both types."
], { fontSize: 11 }), {
  x: 0.5, y: 4.55, w: 9, h: 0.9, valign: "top", paraSpaceAfter: 2, margin: 0
});
addFooter(s, sn, TOTAL);

// --- SLIDE 10: Degree Centrality — side by side ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "06 — DEGREE CENTRALITY", "Degree centrality, Type K vs Type F");
twoImages(s,
  path.join(K_DIR, "degree centrality_.5.png"), "TYPE K",
  path.join(F_DIR, "Ftype_degree centrality_.5.png"), "TYPE F"
);
s.addText(makeBullets([
  "Both types show nearly uniform degree — the plan is topologically flat at the local scale.",
  "Yellow spots at stair landings where vertical edges add connections (degree 5 in K, up to 6 in F).",
  "Room interiors have the same local connectivity as corridor interiors. The hierarchy only emerges at the global scale.",
], { fontSize: 11 }), {
  x: 0.5, y: 4.55, w: 9, h: 0.75, valign: "top", paraSpaceAfter: 2, margin: 0
});
addFooter(s, sn, TOTAL);

// --- SLIDE 11: Clustering — side by side ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "07 — CLUSTERING COEFFICIENT", "Clustering coefficient, Type K vs Type F");
twoImages(s,
  path.join(K_DIR, "clustering coefficient_.5.png"), "TYPE K",
  path.join(F_DIR, "Ftype_clustering coefficient_.5.png"), "TYPE F"
);
s.addText(makeBullets([
  "Both: uniformly zero. In a 4-neighbour rectilinear grid, no two neighbours of a cell are themselves neighbours — triangles cannot form.",
  "Neither apartment has ring corridors, courtyards, or loop connections. Both enforce strictly sequential spatial logic — you can only go forward or back."
], { fontSize: 11 }), {
  x: 0.5, y: 4.55, w: 9, h: 0.75, valign: "top", paraSpaceAfter: 2, margin: 0
});
addFooter(s, sn, TOTAL);

// --- SLIDE 12: Community Detection — Type K ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "08 — COMMUNITY DETECTION", "Community detection, Type K");
imageLeftBulletsRight(s, path.join(K_DIR, "community detection_.5.png"), [
  "Communities slice the building into longitudinal bands — each containing a corridor segment and its L2 rooms above.",
  "Western zone (purple/blue): kitchen block + west L2 rooms. Central zone (blue/teal): corridor core + stair-connected rooms.",
  "Community boundaries run perpendicular to the corridor — the building self-organises into vertical slices, not floor layers.",
  "Stairs bind each L2 room to its nearest L1 corridor segment more strongly than to other L2 rooms."
]);
addFooter(s, sn, TOTAL);

// --- SLIDE 13: Community Detection — Type F ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "08 — COMMUNITY DETECTION", "Community detection, Type F");
imageLeftBulletsRight(s, path.join(F_DIR, "Ftype_community detection_.5.png"), [
  "Same longitudinal-band pattern, extended to three floors — each community spans a corridor segment plus L1 rooms below and L3 rooms above.",
  "Communities are thicker vertical slices than Type K — the middle corridor binds rooms on both sides.",
  "Community boundaries still run perpendicular to the corridor. Floors do not separate into their own communities.",
  "The building's true spatial units are three-floor vertical slices — consistent with Ginzburg's integrated living cells."
]);
addFooter(s, sn, TOTAL);

// --- SLIDE 14: Comparative Summary ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "09 — COMPARISON", "Comparative summary");
const tableRows = [
  [
    { text: "Metric", options: { bold: true, color: ACCENT, fill: { color: "1A1A2E" }, fontSize: 11, fontFace: "Arial" } },
    { text: "Type K (2 floors)", options: { bold: true, color: ACCENT, fill: { color: "1A1A2E" }, fontSize: 11, fontFace: "Arial" } },
    { text: "Type F (3 floors)", options: { bold: true, color: ACCENT, fill: { color: "1A1A2E" }, fontSize: 11, fontFace: "Arial" } }
  ],
  [
    { text: "Corridor position", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "Bottom (L1)", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "Middle (L2)", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } }
  ],
  [
    { text: "Stair connections", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "12 (one junction)", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "19 x 2 junctions", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } }
  ],
  [
    { text: "Closeness gradient", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "One-directional (up)", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "Bidirectional (up + down)", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } }
  ],
  [
    { text: "Betweenness load", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "Serves 1 floor of rooms", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "Serves 2 floors of rooms", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } }
  ],
  [
    { text: "Structural fragility", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "Corridor failure disconnects L2", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "Corridor failure disconnects L1 + L3", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } }
  ],
  [
    { text: "Community pattern", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "2-floor vertical slices", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "3-floor vertical slices", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } }
  ],
  [
    { text: "Clustering", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "Zero (no loops)", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } },
    { text: "Zero (no loops)", options: { fontSize: 10, color: WHITE, fontFace: "Arial" } }
  ]
];
s.addTable(tableRows, {
  x: 0.5, y: 1.4, w: 9, colW: [2.2, 3.4, 3.4],
  border: { pt: 0.5, color: "333333" },
  fill: { color: "111111" },
  rowH: [0.4, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35]
});
addFooter(s, sn, TOTAL);

// --- SLIDE 15: Conclusion ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "10 — CONCLUSION", "Key findings");
s.addText(makeBullets([
  "Same spine, different symmetry: both types use a single continuous corridor absorbing all circulation. Type K places it at the base (asymmetric), Type F in the middle (symmetric).",
  "The middle position is stronger: Type F's L2 corridor is equidistant from rooms in both directions, producing a more balanced accessibility profile.",
  "But more fragile: Type F's corridor carries a double structural load — the only horizontal route for two floors of rooms. Obstruction disconnects twice the spaces.",
  "Vertical slicing is universal: community detection in both types produces longitudinal bands, not floor separations. Stairs bind rooms to their nearest corridor segment across floor boundaries.",
  "The Narkomfin apartments are not stacked flats but integrated three-dimensional living cells, organised vertically around a shared circulation spine."
]), {
  x: 0.5, y: 1.4, w: 9, h: 3.6, valign: "top", paraSpaceAfter: 10, margin: 0
});
addFooter(s, sn, TOTAL);

// --- SLIDE 16: Why Graph Analysis ---
sn++;
s = pres.addSlide();
addSlideHeader(s, "10 — CONCLUSION", "Why graph analysis");
s.addText(makeBullets([
  "Graph analysis turns qualitative spatial intuition into measurable, comparable values across both apartment types.",
  "Betweenness exposes the corridor as a single-point-of-failure routing spine — invisible in a standard floor plan reading.",
  "Closeness quantifies the privacy gradient between floors and reveals that the Type F's middle-floor corridor is more topologically central.",
  "Community detection shows the building's true spatial units are vertical slices — confirming Ginzburg's design intent of integrated living cells.",
  "The comparative analysis reveals a structural trade-off: the Type F is better integrated but more fragile — a finding that only the graph makes legible."
]), {
  x: 0.5, y: 1.4, w: 9, h: 3.6, valign: "top", paraSpaceAfter: 10, margin: 0
});
addFooter(s, sn, TOTAL);

// --- Write ---
const outPath = path.join(__dirname, "GraphML_G02_GraphAnalysis_Slides.pptx");
pres.writeFile({ fileName: outPath }).then(() => {
  console.log("Saved: " + outPath);
}).catch(err => {
  console.error("Error:", err);
});
