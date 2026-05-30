---
marp: true
theme: default
paginate: true
style: |
  :root {
    --rust:   #9E4100;
    --navy:   #2B3340;
    --gray:   #888888;
    --lgray:  #E0E0E0;
    --light:  #F7F8FA;
    --red:    #E85D50;
    --white:  #FFFFFF;
  }

  section {
    background: var(--white);
    font-family: Calibri, 'Trebuchet MS', sans-serif;
    color: var(--navy);
    padding: 0;
    display: flex;
    flex-direction: row;
  }

  /* page numbers */
  section[data-marpit-pagination]::after {
    color: var(--lgray);
    font-size: 0.6em;
    right: 16px;
    bottom: 10px;
  }

  /* ── LEFT SIDEBAR ── */
  .sidebar {
    width: 42px;
    min-width: 42px;
    background: var(--rust);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 16px 0;
    box-sizing: border-box;
  }

  .sidebar .seminar {
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    font-size: 0.52em;
    color: rgba(247,248,250,0.75);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    white-space: nowrap;
    font-family: Calibri, sans-serif;
  }

  .sidebar .assignment {
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    font-size: 0.52em;
    color: rgba(247,248,250,0.45);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    white-space: nowrap;
    font-family: Calibri, sans-serif;
  }

  /* ── INNER CONTENT WRAPPER ── */
  .inner {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 32px 48px 24px 32px;
    height: 100%;
    box-sizing: border-box;
    overflow: hidden;
  }

  /* ── SECTION LABEL ── */
  .section-num {
    font-family: Georgia, serif;
    font-size: 2.2em;
    font-weight: 700;
    color: var(--rust);
    line-height: 1;
    margin-bottom: 2px;
  }

  .section-sub {
    font-size: 0.62em;
    color: var(--gray);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 6px;
  }

  h1 {
    font-family: Georgia, serif;
    font-size: 1.3em;
    font-weight: 700;
    color: var(--navy);
    margin: 0 0 8px;
    letter-spacing: -0.01em;
  }

  hr {
    border: none;
    border-top: 1px solid var(--lgray);
    margin: 0 0 18px;
  }

  p {
    font-size: 0.8em;
    color: #555;
    line-height: 1.7;
    margin: 0 0 10px;
  }

  ul {
    font-size: 0.8em;
    color: #555;
    line-height: 1.7;
    padding-left: 1.2em;
    margin: 0;
  }

  li { margin-bottom: 3px; }
  strong { color: var(--navy); font-weight: 600; }
  code { font-size: 0.9em; background: #F0F0F0; padding: 1px 4px; border-radius: 3px; }


  /* ── TITLE SLIDE ── */
  section.title {
    background: linear-gradient(135deg, #2B3340 0%, #3B8EA5 50%, #9E4100 100%);
    flex-direction: column;
    padding: 0;
  }

  section.title::before { display: none; }

  section.title .title-inner {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 48px 60px;
  }

  section.title .course {
    font-size: 0.65em;
    color: rgba(247,248,250,0.6);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 60px;
  }

  section.title h1 {
    font-family: Georgia, serif;
    font-size: 2.6em;
    font-weight: 700;
    color: var(--light);
    letter-spacing: -0.02em;
    margin: 0 0 6px;
  }

  section.title .title-sub {
    font-size: 0.85em;
    color: rgba(247,248,250,0.7);
    margin-bottom: 32px;
  }

  section.title .title-rule {
    width: 100%;
    height: 1px;
    background: rgba(247,248,250,0.25);
    margin-bottom: 18px;
  }

  section.title .title-meta {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }

  section.title .title-meta .left {
    font-size: 0.68em;
    color: rgba(247,248,250,0.5);
  }

  section.title .title-meta .right {
    font-size: 0.68em;
    color: rgba(247,248,250,0.7);
    text-align: right;
    line-height: 1.6;
  }

  section.title .assignment {
    font-size: 0.72em;
    color: rgba(247,248,250,0.5);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
  }

  /* ── STATS ── */
  .stats {
    display: flex;
    gap: 1px;
    background: var(--lgray);
    border-radius: 4px;
    overflow: hidden;
    margin: 14px 0;
  }
  .stat {
    flex: 1;
    background: var(--white);
    padding: 14px 12px;
    text-align: center;
  }
  .stat .num { font-family: Georgia, serif; font-size: 1.7em; font-weight: 700; color: var(--rust); line-height: 1; }
  .stat .lbl { font-size: 0.62em; color: var(--gray); margin-top: 4px; letter-spacing: 0.03em; }

  /* ── COLS ── */
  .cols { display: flex; gap: 20px; }
  .col  { flex: 1; }

  /* ── CARD ── */
  .card {
    background: var(--light);
    border-radius: 4px;
    padding: 18px 20px;
    height: 100%;
    box-sizing: border-box;
  }
  .card .tag {
    font-size: 0.58em;
    color: var(--rust);
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 6px;
  }
  .card .ttl {
    font-family: Georgia, serif;
    font-size: 0.82em;
    font-weight: 700;
    color: var(--navy);
    line-height: 1.35;
    margin-bottom: 2px;
  }
  .card .src { font-size: 0.65em; color: var(--gray); margin-bottom: 10px; }
  .card ul   { font-size: 0.76em; color: #666; line-height: 1.6; }
  .card .note {
    margin-top: 10px;
    padding: 8px 12px;
    border-left: 2px solid var(--rust);
    background: white;
    border-radius: 0 3px 3px 0;
    font-size: 0.72em;
    color: #444;
    line-height: 1.5;
  }

  /* ── IMAGES ── */
  .img-wrap { display: flex; gap: 16px; }
  .img-col  { flex: 1; display: flex; flex-direction: column; gap: 5px; }
  .img-frame {
    background: var(--light);
    border-radius: 4px;
    overflow: hidden;
    flex: 1;
  }
  .img-frame img { width: 100%; height: 100%; object-fit: contain; display: block; }
  .img-cap { font-size: 0.6em; color: #AAAAAA; text-align: center; }

  /* ── ATTR BAR ── */
  .attr-bar {
    display: flex;
    margin-top: 12px;
    background: var(--lgray);
    border-radius: 4px;
    overflow: hidden;
    gap: 1px;
  }
  .attr { flex: 1; background: var(--white); padding: 10px 14px; }
  .attr .k { font-size: 0.56em; color: var(--gray); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 3px; }
  .attr .v { font-size: 0.76em; font-weight: 600; color: var(--navy); }
  .attr .v.rust { color: var(--rust); }
  .attr .v.red  { color: var(--red); }

  /* ── STEPS ── */
  .steps { display: flex; flex-direction: column; gap: 8px; }
  .step {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    padding: 12px 16px;
    background: var(--light);
    border-radius: 4px;
  }
  .step .n {
    font-family: Georgia, serif;
    font-size: 1em;
    font-weight: 700;
    color: var(--rust);
    min-width: 28px;
    padding-top: 1px;
  }
  .step .t { font-size: 0.8em; font-weight: 600; color: var(--navy); margin-bottom: 2px; }
  .step .d { font-size: 0.72em; color: #777; line-height: 1.5; }

  /* ── CONTENTS SLIDE ── */
  .contents-list { margin-top: 24px; }
  .contents-item {
    display: flex;
    align-items: baseline;
    gap: 24px;
    padding: 16px 0;
    border-bottom: 1px solid var(--lgray);
  }
  .contents-item:first-child { border-top: 1px solid var(--lgray); }
  .contents-num {
    font-family: Georgia, serif;
    font-size: 1.6em;
    font-weight: 700;
    color: var(--rust);
    min-width: 48px;
    line-height: 1;
  }
  .contents-title {
    font-size: 0.88em;
    color: var(--navy);
    font-weight: 600;
  }
  .contents-desc {
    font-size: 0.75em;
    color: var(--gray);
    margin-top: 2px;
  }
---

<!-- _class: title -->

<div class="title-inner">
  <div class="course">MaCAD 2025/26 · Digital Tools for Graph Machine Learning</div>
  <h1>GraphML_G02</h1>
  <div class="title-sub">Graph Learning Pipeline for Architectural Floor Plans</div>
  <div class="title-rule"></div>
  <div class="title-meta">
    <div class="left">
      <div class="assignment">Final Assignment</div>
      <div style="color:rgba(247,248,250,0.35); font-size:0.85em">IAAC &nbsp;·&nbsp; 1<sup>st</sup>aac</div>
    </div>
    <div class="right">
      Lakzhmy Zaro<br>
      María Sánchez<br>
      Charles Abi Chahine<br>
      Emilie El Chidiac
    </div>
  </div>
</div>

---

<div class="sidebar"><span class="seminar">Graph Machine Learning</span><span class="assignment">Final Assignment</span></div>
<div class="inner">
  <h1 style="color:var(--rust); font-size:1.6em; margin-bottom:4px">Contents</h1>
  <p style="font-size:0.72em; color:var(--gray); margin-bottom:0">This week we explored…</p>

  <div class="contents-list">
    <div class="contents-item">
      <div class="contents-num">01</div>
      <div>
        <div class="contents-title">Dataset</div>
        <div class="contents-desc">Modified Swiss Dwellings — 5,372 floor plans as NetworkX graphs</div>
      </div>
    </div>
    <div class="contents-item">
      <div class="contents-num">02</div>
      <div>
        <div class="contents-title">Research</div>
        <div class="contents-desc">MSD benchmark paper (ECCV 2024) · GNN node classification paper (eCAADe 2024)</div>
      </div>
    </div>
    <div class="contents-item">
      <div class="contents-num">03</div>
      <div>
        <div class="contents-title">Graph Structure</div>
        <div class="contents-desc">graph_in vs graph_out — zone labels, connectivity, and room type prediction</div>
      </div>
    </div>
    <div class="contents-item">
      <div class="contents-num">04</div>
      <div>
        <div class="contents-title">Next Steps</div>
        <div class="contents-desc">Floor plan recreation → graph construction → analysis → node classification</div>
      </div>
    </div>
  </div>
</div>

---

<div class="sidebar"><span class="seminar">Graph Machine Learning</span><span class="assignment">Final Assignment</span></div>
<div class="inner">
  <div class="section-num">01</div>
  <div class="section-sub">Dataset</div>
  <h1>Modified Swiss Dwellings</h1>
  <hr>

  <p>5,372 Swiss residential floor plans, each stored as a NetworkX graph in <code>.pickle</code> format. Three modalities exist — image, geometry, and graph — but we work exclusively with the <strong>graph modality</strong>. The pickle file has no visual on its own; the floor plans below were rendered by reading the polygon geometry stored on each graph node and drawing them with matplotlib.</p>

  <div class="img-frame" style="height:190px; margin: 12px 0 8px; border-radius:4px;">
    <img src="img/samples.png" style="object-fit:cover; object-position:center;">
  </div>
  <div class="img-cap" style="margin-bottom:10px">Plans 10000, 10009, 10014, 10019, 10029, 10031 — rendered from graph_out node geometry</div>

  <div class="stats">
    <div class="stat"><div class="num">5,372</div><div class="lbl">Floor Plans</div></div>
    <div class="stat"><div class="num">4</div><div class="lbl">Zone Types</div></div>
    <div class="stat"><div class="num">9</div><div class="lbl">Room Types</div></div>
    <div class="stat"><div class="num">.pickle</div><div class="lbl">Graph Format</div></div>
  </div>

</div>

---

<div class="sidebar"><span class="seminar">Graph Machine Learning</span><span class="assignment">Final Assignment</span></div>
<div class="inner">
  <div class="section-num">02</div>
  <div class="section-sub">Research</div>
  <h1>Literature</h1>
  <hr>

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

</div>

---

<div class="sidebar"><span class="seminar">Graph Machine Learning</span><span class="assignment">Final Assignment</span></div>
<div class="inner">
  <div class="section-num">03</div>
  <div class="section-sub">Graph Structure</div>
  <h1>From Plan to Graph — Plan 10000</h1>
  <hr>

  <p>Each plan is stored as two paired graphs. <strong>graph_out</strong> (left) holds the ground-truth room type per node plus polygon geometry — this is what we rendered to visualise the plan. <strong>graph_in</strong> (right) holds only zone labels and connectivity — this is what the model actually sees. No shapes, no areas, no coordinates.</p>

  <div class="img-wrap" style="height:270px; margin-top:12px">
    <div class="img-col">
      <div class="img-frame"><img src="img/plan_rooms.png"></div>
      <div class="img-cap"><strong>graph_out</strong> — room_type (0–8) + polygon geometry</div>
    </div>
    <div class="img-col">
      <div class="img-frame"><img src="img/plan_graph.png"></div>
      <div class="img-cap"><strong>graph_in</strong> — zoning_type (0–3) · door / entrance edges</div>
    </div>
  </div>

  <div class="attr-bar">
    <div class="attr"><div class="k">Model input</div><div class="v rust">zoning_type 0–3</div></div>
    <div class="attr"><div class="k">Edge type</div><div class="v">door · <span class="red">entrance</span></div></div>
    <div class="attr"><div class="k">Model target</div><div class="v">room_type 0–8</div></div>
    <div class="attr"><div class="k">Geometry used</div><div class="v" style="color:#AAAAAA">topology only</div></div>
  </div>

</div>

---

<div class="sidebar"><span class="seminar">Graph Machine Learning</span><span class="assignment">Final Assignment</span></div>
<div class="inner">
  <div class="section-num">04</div>
  <div class="section-sub">Next Steps</div>
  <h1>Pipeline</h1>
  <hr>

  <div class="steps">
    <div class="step">
      <div class="n">01</div>
      <div>
        <div class="t">Floor Plan Recreation</div>
        <div class="d">Recreate plan 10000 in Rhino. Room boundaries as closed polylines with shared edges between adjacent rooms — required for TopologicPy to detect adjacency.</div>
      </div>
    </div>
    <div class="step">
      <div class="n">02</div>
      <div>
        <div class="t">Graph Construction — TopologicPy</div>
        <div class="d">Convert the Rhino geometry into a graph. Assign zoning_type to nodes and door/entrance labels to edges to match the MSD input format.</div>
      </div>
    </div>
    <div class="step">
      <div class="n">03</div>
      <div>
        <div class="t">Graph Analysis — NetworkX</div>
        <div class="d">Compute degree, betweenness, and closeness centrality. Analyse spatial connectivity patterns across the floor plan.</div>
      </div>
    </div>
    <div class="step">
      <div class="n">04</div>
      <div>
        <div class="t">Node Classification — GraphSAGE-Pool</div>
        <div class="d">Run the pretrained model on our graph. Predict room_type from zone labels and connectivity. Compare against ground truth from MSD.</div>
      </div>
    </div>
  </div>

</div>
