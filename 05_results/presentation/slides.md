---
marp: true
theme: default
paginate: true
style: |
  :root {
    --black: #111111;
    --teal:  #00A896;
    --gray:  #888888;
    --light: #F5F5F5;
    --red:   #E05555;
  }

  section {
    background: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif;
    color: var(--black);
    padding: 56px 72px;
  }

  section::after {
    color: #CCCCCC;
    font-size: 0.65em;
  }

  h1 {
    font-size: 1.5em;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: var(--black);
    margin: 0 0 6px;
  }

  h2 {
    font-size: 0.7em;
    font-weight: 400;
    color: var(--teal);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin: 0 0 20px;
  }

  p {
    font-size: 0.82em;
    color: #555555;
    line-height: 1.75;
    margin: 0;
  }

  ul {
    font-size: 0.82em;
    color: #555555;
    line-height: 1.75;
    padding-left: 1.2em;
    margin: 0;
  }

  li { margin-bottom: 2px; }

  strong { color: var(--black); font-weight: 600; }

  /* ── TITLE ── */
  section.title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 80px 80px;
  }

  section.title .eyebrow {
    font-size: 0.65em;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--teal);
    margin-bottom: 24px;
  }

  section.title h1 {
    font-size: 3.2em;
    font-weight: 700;
    letter-spacing: -0.03em;
    line-height: 1.05;
    margin: 0 0 16px;
  }

  section.title .sub {
    font-size: 0.88em;
    color: var(--gray);
    margin-bottom: 40px;
  }

  section.title hr {
    border: none;
    border-top: 1px solid #E0E0E0;
    margin: 0 0 28px;
    width: 100%;
  }

  section.title .nav {
    font-size: 0.72em;
    color: #BBBBBB;
    letter-spacing: 0.04em;
  }

  section.title .nav b {
    color: var(--teal);
    font-weight: 600;
  }

  section.title .team {
    position: absolute;
    bottom: 48px;
    left: 80px;
    font-size: 0.65em;
    color: #CCCCCC;
  }

  /* ── CONTENT ── */
  section.content {
    padding-top: 56px;
  }

  /* ── STATS ── */
  .stats {
    display: flex;
    gap: 1px;
    background: #E8E8E8;
    border-radius: 6px;
    overflow: hidden;
    margin: 24px 0;
  }

  .stat {
    flex: 1;
    background: white;
    padding: 20px 16px;
    text-align: center;
  }

  .stat .num {
    font-size: 1.8em;
    font-weight: 700;
    color: var(--teal);
    line-height: 1;
  }

  .stat .lbl {
    font-size: 0.65em;
    color: var(--gray);
    margin-top: 5px;
    letter-spacing: 0.04em;
  }

  /* ── COLS ── */
  .cols { display: flex; gap: 28px; margin-top: 20px; }
  .col  { flex: 1; }

  /* ── CARD ── */
  .card {
    background: var(--light);
    border-radius: 6px;
    padding: 22px 24px;
    height: 100%;
    box-sizing: border-box;
  }

  .card .tag {
    font-size: 0.6em;
    color: var(--teal);
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 8px;
  }

  .card .ttl {
    font-size: 0.85em;
    font-weight: 600;
    color: var(--black);
    line-height: 1.4;
    margin-bottom: 3px;
  }

  .card .src {
    font-size: 0.68em;
    color: var(--gray);
    margin-bottom: 12px;
  }

  .card ul {
    font-size: 0.78em;
    color: #666;
    line-height: 1.65;
  }

  .card .note {
    margin-top: 12px;
    padding: 9px 12px;
    border-left: 2px solid var(--teal);
    background: white;
    border-radius: 0 4px 4px 0;
    font-size: 0.75em;
    color: #444;
    line-height: 1.5;
  }

  /* ── IMAGE FRAME ── */
  .img-wrap { display: flex; gap: 20px; margin-top: 20px; }
  .img-col  { flex: 1; display: flex; flex-direction: column; gap: 6px; }

  .img-frame {
    background: var(--light);
    border-radius: 6px;
    overflow: hidden;
    flex: 1;
  }

  .img-frame img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
  }

  .img-cap {
    font-size: 0.65em;
    color: #AAAAAA;
    text-align: center;
  }

  /* ── ATTR BAR ── */
  .attr-bar {
    display: flex;
    margin-top: 16px;
    background: #E8E8E8;
    border-radius: 6px;
    overflow: hidden;
    gap: 1px;
  }

  .attr {
    flex: 1;
    background: white;
    padding: 12px 16px;
  }

  .attr .k {
    font-size: 0.58em;
    color: var(--gray);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 3px;
  }

  .attr .v {
    font-size: 0.8em;
    font-weight: 600;
    color: var(--black);
  }

  .attr .v.teal { color: var(--teal); }
  .attr .v.red  { color: var(--red); }

  /* ── STEPS ── */
  .steps { display: flex; flex-direction: column; gap: 10px; margin-top: 20px; }

  .step {
    display: flex;
    align-items: flex-start;
    gap: 18px;
    padding: 14px 18px;
    background: var(--light);
    border-radius: 6px;
  }

  .step .n {
    font-size: 0.6em;
    font-weight: 700;
    color: var(--teal);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    min-width: 44px;
    padding-top: 2px;
  }

  .step .t {
    font-size: 0.82em;
    font-weight: 600;
    color: var(--black);
    margin-bottom: 2px;
  }

  .step .d {
    font-size: 0.74em;
    color: #777;
    line-height: 1.5;
  }
---

<!-- _class: title -->

<div class="eyebrow">IAAC MaCad · AIA26 S.3 Graph ML · 2025–26</div>

# GraphML_G02

<div class="sub">Graph Learning Pipeline for Architectural Floor Plans</div>

<hr>

<div class="nav">
  <b>01</b> Dataset &ensp; <b>02</b> Research &ensp; <b>03</b> Graph Structure &ensp; <b>04</b> Next Steps
</div>

<div class="team">Charles Abi Chahine · Emilie El Chidiac · Lakzhmy Zaro · Maria Sánchez i Domínguez</div>

---

<!-- _class: content -->

## 01 — Dataset
# Modified Swiss Dwellings

<p>5,372 Swiss residential floor plans, each stored as a NetworkX graph in <code>.pickle</code> format. Three modalities exist — image, geometry, and graph — but we work exclusively with the <strong>graph modality</strong>. The pickle file has no visual on its own; the floor plans below were rendered by reading the polygon geometry stored on each graph node and drawing them with matplotlib.</p>

<div class="img-frame" style="height:200px; margin: 14px 0 10px;">
  <img src="img/samples.png" style="object-fit:cover; object-position:center;">
</div>
<div class="img-cap" style="margin-bottom:10px">Plans 10000, 10009, 10014, 10019 — rendered from graph_out node geometry</div>

<div class="stats">
  <div class="stat"><div class="num">5,372</div><div class="lbl">Floor Plans</div></div>
  <div class="stat"><div class="num">4</div><div class="lbl">Zone Types</div></div>
  <div class="stat"><div class="num">9</div><div class="lbl">Room Types</div></div>
  <div class="stat"><div class="num">.pickle</div><div class="lbl">Graph Format</div></div>
</div>

---

<!-- _class: content -->

## 02 — Research
# Literature

<div class="cols">
  <div class="col">
    <div class="card">
      <div class="tag">Paper 1</div>
      <div class="ttl">MSD: A Benchmark Dataset for Floor Plan Generation of Building Complexes</div>
      <div class="src">ECCV 2024 · TU Delft</div>
      <ul>
        <li>5,372 Swiss residential floor plans</li>
        <li>3 modalities: image, geometry, graph</li>
        <li>Richer than RPLAN & LIFULL — multi-apartment, compass orientation, inter-unit links</li>
        <li>Graph encodes spatial zones, not room types</li>
      </ul>
      <div class="note">This dataset is our primary data source.</div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <div class="tag">Paper 2</div>
      <div class="ttl">GNN for Node Classification and Attribute Allocation in Architectural BIM</div>
      <div class="src">eCAADe 2024 · Cardiff University</div>
      <ul>
        <li>Uses the same MSD dataset</li>
        <li>Converts floor plans to graphs via TopologicPy</li>
        <li>Benchmarks GCN, GAT, GraphSAGE architectures</li>
        <li>GraphSAGE-Pool, 4 layers — ~95% accuracy</li>
      </ul>
      <div class="note">The pretrained model from this paper is what we will run on our floor plan.</div>
    </div>
  </div>
</div>

---

<!-- _class: content -->

## 03 — Graph Structure
# From Plan to Graph — Plan 10000

<p>Each plan is stored as two paired graphs. <strong>graph_out</strong> (left) holds the ground-truth room type per node, plus polygon geometry — this is what we rendered to visualise the plan. <strong>graph_in</strong> (right) holds only zone labels and connectivity — this is what the model actually sees. No shapes, no areas, no coordinates. Room function must be inferred from topology alone.</p>

<div class="img-wrap" style="height:290px; margin-top:14px">
  <div class="img-col">
    <div class="img-frame">
      <img src="img/plan_rooms.png">
    </div>
    <div class="img-cap"><strong>graph_out</strong> — room_type (0–8) + polygon geometry per node</div>
  </div>
  <div class="img-col">
    <div class="img-frame">
      <img src="img/plan_graph.png">
    </div>
    <div class="img-cap"><strong>graph_in</strong> — zoning_type (0–3) per node · door / entrance edges</div>
  </div>
</div>

<div class="attr-bar">
  <div class="attr"><div class="k">Model input</div><div class="v teal">zoning_type 0–3</div></div>
  <div class="attr"><div class="k">Edge type</div><div class="v">door · <span class="red">entrance</span></div></div>
  <div class="attr"><div class="k">Model target</div><div class="v">room_type 0–8</div></div>
  <div class="attr"><div class="k">Geometry used</div><div class="v" style="color:#AAAAAA">topology only</div></div>
</div>

---

<!-- _class: content -->

## 04 — Next Steps
# Pipeline

<div class="steps">
  <div class="step">
    <div class="n">Step 1</div>
    <div>
      <div class="t">Floor Plan Recreation</div>
      <div class="d">Recreate plan 10000 in Rhino. Clean room boundaries as closed polylines with shared edges between adjacent rooms.</div>
    </div>
  </div>
  <div class="step">
    <div class="n">Step 2</div>
    <div>
      <div class="t">Graph Construction — TopologicPy</div>
      <div class="d">Convert the Rhino geometry into a graph. Assign zoning_type to nodes and door/entrance labels to edges to match the MSD input format.</div>
    </div>
  </div>
  <div class="step">
    <div class="n">Step 3</div>
    <div>
      <div class="t">Graph Analysis — NetworkX</div>
      <div class="d">Compute degree, betweenness, and closeness centrality. Analyse spatial connectivity patterns across the floor plan.</div>
    </div>
  </div>
  <div class="step">
    <div class="n">Step 4</div>
    <div>
      <div class="t">Node Classification — GraphSAGE-Pool</div>
      <div class="d">Run the pretrained model on our graph. Predict room_type from zone labels and connectivity. Compare against ground truth from MSD.</div>
    </div>
  </div>
</div>
