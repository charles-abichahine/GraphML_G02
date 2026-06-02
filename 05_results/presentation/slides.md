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
    width: 54px;
    min-width: 54px;
    background: var(--rust);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 18px 0;
    box-sizing: border-box;
  }

  .sidebar .seminar {
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    font-size: 0.56em;
    color: rgba(247,248,250,0.85);
    letter-spacing: 0.06em;
    font-style: italic;
    font-family: Calibri, sans-serif;
    text-align: end;
  }

  .sidebar .assignment {
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    font-size: 0.56em;
    font-weight: 700;
    font-style: italic;
    color: rgba(247,248,250,0.9);
    letter-spacing: 0.06em;
    font-family: Calibri, sans-serif;
    align-self: flex-end;
    padding-right: 6px;
  }

  /* ── INNER CONTENT WRAPPER ── */
  .inner {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 28px 44px 20px 28px;
    height: 100%;
    box-sizing: border-box;
    overflow: hidden;
  }

  /* ── SECTION LABEL ── */
  .sec-hdr {
    display: flex;
    align-items: baseline;
    gap: 14px;
    margin-bottom: 6px;
  }
  .section-num {
    font-family: Georgia, serif;
    font-size: 2.2em;
    font-weight: 700;
    color: var(--rust);
    line-height: 1;
  }
  .section-sub {
    font-size: 0.62em;
    color: var(--gray);
    letter-spacing: 0.08em;
    text-transform: uppercase;
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
    margin: 0 0 14px;
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
    margin: 10px 0;
  }
  .stat {
    flex: 1;
    background: var(--white);
    padding: 10px 8px;
    text-align: center;
  }
  .stat .num { font-family: Georgia, serif; font-size: 1.5em; font-weight: 700; color: var(--rust); line-height: 1; }
  .stat .lbl { font-size: 0.58em; color: var(--gray); margin-top: 4px; letter-spacing: 0.03em; }

  /* ── COLS ── */
  .cols { display: flex; gap: 20px; }
  .col  { flex: 1; }

  /* ── CARD ── */
  .card {
    background: var(--light);
    border-radius: 4px;
    padding: 14px 16px;
    height: 100%;
    box-sizing: border-box;
  }
  .card .tag {
    font-size: 0.58em;
    color: var(--rust);
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 5px;
  }
  .card .ttl {
    font-family: Georgia, serif;
    font-size: 0.78em;
    font-weight: 700;
    color: var(--navy);
    line-height: 1.3;
    margin-bottom: 2px;
  }
  .card .src { font-size: 0.62em; color: var(--gray); margin-bottom: 8px; }
  .card ul   { font-size: 0.72em; color: #666; line-height: 1.55; }
  .card .note {
    margin-top: 8px;
    padding: 6px 10px;
    border-left: 2px solid var(--rust);
    background: white;
    border-radius: 0 3px 3px 0;
    font-size: 0.68em;
    color: #444;
    line-height: 1.45;
  }

  /* ── IMAGES ── */
  .img-wrap { display: flex; gap: 14px; }
  .img-col  { flex: 1; display: flex; flex-direction: column; gap: 4px; }
  .img-frame {
    background: white;
    border-radius: 4px;
    overflow: hidden;
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  /* contain so images are never stretched */
  .img-frame img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    display: block;
  }
  .img-cap { font-size: 0.58em; color: #AAAAAA; text-align: center; }

  /* ── ATTR BAR ── */
  .attr-bar {
    display: flex;
    margin-top: 10px;
    background: var(--lgray);
    border-radius: 4px;
    overflow: hidden;
    gap: 1px;
  }
  .attr { flex: 1; background: var(--white); padding: 8px 12px; }
  .attr .k { font-size: 0.56em; color: var(--gray); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px; }
  .attr .v { font-size: 0.72em; font-weight: 600; color: var(--navy); }
  .attr .v.rust { color: var(--rust); }
  .attr .v.red  { color: var(--red); }

  /* ── STEPS ── */
  .steps { display: flex; flex-direction: column; gap: 7px; }
  .step {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 10px 14px;
    background: var(--light);
    border-radius: 4px;
  }
  .step .n {
    font-family: Georgia, serif;
    font-size: 1em;
    font-weight: 700;
    color: var(--rust);
    width: 36px;
    min-width: 36px;
    max-width: 36px;
    white-space: nowrap;
    flex-shrink: 0;
    line-height: 1;
    text-align: left;
  }
  .step .t { font-size: 0.76em; font-weight: 600; color: var(--navy); margin-bottom: 2px; }
  .step .d { font-size: 0.68em; color: #777; line-height: 1.45; }

  /* ── CHIPS ── */
  .chips { display: flex; gap: 6px; flex-wrap: wrap; margin: 8px 0; }
  .chip {
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.65em;
    font-weight: 600;
    letter-spacing: 0.03em;
    background: var(--light);
    color: var(--navy);
    border: 1px solid var(--lgray);
  }
  .chip.rust { background: var(--rust); color: white; border-color: var(--rust); }

  /* ── ZONE SWATCHES ── */
  .zones { display: flex; gap: 6px; margin: 8px 0; }
  .zone {
    flex: 1;
    padding: 6px 8px;
    border-radius: 4px;
    display: flex;
    flex-direction: column;
    gap: 2px;
  }
  .zone .z-num  { font-family: Georgia, serif; font-size: 1em; font-weight: 700; color: white; }
  .zone .z-name { font-size: 0.58em; font-weight: 700; color: rgba(255,255,255,0.85); text-transform: uppercase; letter-spacing: 0.06em; }
  .zone .z-desc { font-size: 0.56em; color: rgba(255,255,255,0.65); margin-top: 1px; }

  /* ── FACT CALLOUTS ── */
  .facts { display: flex; flex-direction: column; gap: 7px; }
  .fact {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 9px 12px;
    background: var(--light);
    border-radius: 4px;
  }
  .fact .f-num   { font-family: Georgia, serif; font-size: 1.4em; font-weight: 700; color: var(--rust); min-width: 44px; line-height: 1; }
  .fact .f-label { font-size: 0.76em; font-weight: 600; color: var(--navy); }
  .fact .f-desc  { font-size: 0.65em; color: var(--gray); }

  /* ── TABLES ── */
  .tbl { width: 100%; border-collapse: collapse; font-size: 0.6em; margin-bottom: 6px; }
  .tbl th { background: var(--navy); color: white; padding: 4px 8px; text-align: left; font-weight: 600; font-size: 0.9em; }
  .tbl td { padding: 3px 8px; border-bottom: 1px solid var(--lgray); color: #444; }
  .tbl tr:last-child td { border-bottom: 1px solid var(--lgray); }
  .tbl tr:nth-child(even) td { background: var(--light); }
  .tbl code { background: #EDEDED; padding: 1px 3px; border-radius: 3px; font-size: 0.9em; color: var(--rust); }
  .tbl .val { color: var(--navy); font-weight: 600; }

  /* ── FLOW ── */
  .flow { display: flex; align-items: center; gap: 6px; margin: 8px 0; }
  .flow-box {
    flex: 1;
    padding: 6px 10px;
    background: var(--light);
    border-radius: 4px;
    text-align: center;
  }
  .flow-box .f-label { font-size: 0.66em; font-weight: 600; color: var(--navy); }
  .flow-box .f-sub   { font-size: 0.58em; color: var(--gray); margin-top: 1px; }
  .flow-arrow { font-size: 1.1em; color: var(--rust); }

  /* ── CONTENTS SLIDE ── */
  .contents-list { margin-top: 18px; }
  .contents-item {
    display: flex;
    align-items: baseline;
    gap: 20px;
    padding: 12px 0;
    border-bottom: 1px solid var(--lgray);
  }
  .contents-item:first-child { border-top: 1px solid var(--lgray); }
  .contents-num {
    font-family: Georgia, serif;
    font-size: 1.5em;
    font-weight: 700;
    color: var(--rust);
    min-width: 44px;
    line-height: 1;
  }
  .contents-title {
    font-size: 0.84em;
    color: var(--navy);
    font-weight: 600;
  }
  .contents-desc {
    font-size: 0.7em;
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
      <div style="color:rgba(247,248,250,0.35); font-size:0.85em">IAAC &nbsp;·&nbsp; MaCAD 2025/26</div>
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

<div class="sidebar"><span class="seminar">Digital tools for<br>Graph Machine Learning</span><span class="assignment">Final Assignment - G02</span></div>
<div class="inner">
  <h1 style="color:var(--rust); font-size:1.6em; margin-bottom:4px">Contents</h1>
  <p style="font-size:0.72em; color:var(--gray); margin-bottom:0">This week we explored the Swiss Dwellings dataset and the research papers behind it, and defined the next steps for our graph ML pipeline.</p>

  <div class="contents-list">
    <div class="contents-item">
      <div class="contents-num">01</div>
      <div>
        <div class="contents-title">Dataset</div>
        <div class="contents-desc">Modified Swiss Dwellings — 5,372 residential floor plans as NetworkX graphs · Plan 10000 selected</div>
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

<div class="sidebar"><span class="seminar">Digital tools for<br>Graph Machine Learning</span><span class="assignment">Final Assignment - G02</span></div>
<div class="inner">
  <div class="sec-hdr"><div class="section-num">01</div><div class="section-sub">Dataset</div></div>
  <h1>Modified Swiss Dwellings</h1>
  <hr>

  <div class="chips">
    <span class="chip rust">5,372 floor plans</span>
    <span class="chip">Multi-apartment clusters</span>
    <span class="chip">Corridor buildings</span>
    <span class="chip">Single units</span>
    <span class="chip">Graph modality only</span>
  </div>

  <div class="img-frame" style="height:200px; margin:6px 0; border-radius:4px; background:white;">
    <img src="img/samples2.png" style="width:100%; height:100%; object-fit:contain; object-position:center;">
  </div>
  <div class="img-cap" style="margin-bottom:6px">3 sample plans — wide variety of residential typologies, scales and orientations</div>

  <div class="stats">
    <div class="stat"><div class="num">5,372</div><div class="lbl">Floor Plans</div></div>
    <div class="stat"><div class="num">4</div><div class="lbl">Zone Types</div></div>
    <div class="stat"><div class="num">9</div><div class="lbl">Room Types</div></div>
    <div class="stat"><div class="num">.pickle</div><div class="lbl">Graph Format</div></div>
  </div>
</div>

---

<div class="sidebar"><span class="seminar">Digital tools for<br>Graph Machine Learning</span><span class="assignment">Final Assignment - G02</span></div>
<div class="inner">
  <div class="sec-hdr"><div class="section-num">01</div><div class="section-sub">Dataset — Selected Plan</div></div>
  <h1>Plan 10000 — Multi-Apartment Cluster</h1>
  <hr>

  <div class="cols" style="flex:1; min-height:0; margin-top:4px; gap:10px; align-items:stretch;">
    <div class="col" style="flex:3; display:flex; flex-direction:column; gap:6px; min-height:0;">
      <div style="flex:1; min-height:0; display:flex; align-items:center; justify-content:center;">
        <img src="img/plan_rooms.png" style="width:100%; height:100%; object-fit:contain; display:block;">
      </div>
      <div class="img-cap">Room types — rendered from graph_out geometry</div>
    </div>
    <div class="col" style="flex:1; display:flex; flex-direction:column; gap:8px; justify-content:center; padding-left:16px;">
      <div class="facts">
        <div class="fact">
          <div class="f-num">41</div>
          <div><div class="f-label">Rooms</div><div class="f-desc">across 2 apartments</div></div>
        </div>
        <div class="fact">
          <div class="f-num">2</div>
          <div><div class="f-label">Apartments</div><div class="f-desc">sharing a common entrance</div></div>
        </div>
        <div class="fact">
          <div class="f-num">✓</div>
          <div><div class="f-label">Ground Truth</div><div class="f-desc">validate predictions against MSD labels</div></div>
        </div>
      </div>
      <div class="chips" style="margin-top:4px">
        <span class="chip">Cluster typology</span>
        <span class="chip">Diagonal layout</span>
      </div>
    </div>
  </div>
</div>

---

<div class="sidebar"><span class="seminar">Digital tools for<br>Graph Machine Learning</span><span class="assignment">Final Assignment - G02</span></div>
<div class="inner">
  <div class="sec-hdr"><div class="section-num">02</div><div class="section-sub">Research</div></div>
  <h1>Literature</h1>
  <hr>

  <div class="cols" style="flex:1; min-height:0;">
    <div class="col">
      <div class="card">
        <div class="tag">Paper 1</div>
        <div class="ttl">MSD: A Benchmark Dataset for Floor Plan Generation of Building Complexes</div>
        <div class="src">ECCV 2024 · TU Delft</div>
        <ul>
          <li>5,372 Swiss residential floor plans</li>
          <li>3 modalities: image, geometry, graph</li>
          <li>Richer than RPLAN &amp; LIFULL — multi-apartment, compass orientation, inter-unit links</li>
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

<div class="sidebar"><span class="seminar">Digital tools for<br>Graph Machine Learning</span><span class="assignment">Final Assignment - G02</span></div>
<div class="inner">
  <div class="sec-hdr"><div class="section-num">03</div><div class="section-sub">Graph Structure</div></div>
  <h1>Data Structure</h1>
  <hr>

  <div class="cols" style="gap:24px; margin-top:2px;">
    <div class="col">
      <div style="font-size:0.58em; font-weight:700; color:var(--rust); text-transform:uppercase; letter-spacing:0.1em; margin-bottom:4px">graph_in — model input</div>
      <table class="tbl">
        <tr><th>Attribute</th><th>Type</th><th>Values</th></tr>
        <tr><td><code>zoning_type</code></td><td>int</td><td class="val">0 · 1 · 2 · 3</td></tr>
        <tr><td><code>connectivity</code></td><td>str</td><td class="val">'door' · 'entrance'</td></tr>
      </table>
      <div style="font-size:0.58em; font-weight:700; color:var(--navy); text-transform:uppercase; letter-spacing:0.1em; margin:8px 0 4px">graph_out — ground truth</div>
      <table class="tbl">
        <tr><th>Attribute</th><th>Type</th><th>Description</th></tr>
        <tr><td><code>room_type</code></td><td>int</td><td class="val">0 – 8</td></tr>
        <tr><td><code>geometry</code></td><td>Polygon</td><td>2D room outline</td></tr>
        <tr><td><code>centroid</code></td><td>Point</td><td>centre of room</td></tr>
      </table>
    </div>
    <div class="col">
      <div style="font-size:0.58em; font-weight:700; color:var(--navy); text-transform:uppercase; letter-spacing:0.1em; margin-bottom:4px">Room types (0 – 8)</div>
      <table class="tbl">
        <tr><th>ID</th><th>Room</th><th>ID</th><th>Room</th></tr>
        <tr><td class="val">0</td><td>Balcony</td><td class="val">5</td><td>Kitchen</td></tr>
        <tr><td class="val">1</td><td>Bathroom</td><td class="val">6</td><td>Living Room</td></tr>
        <tr><td class="val">2</td><td>Bedroom</td><td class="val">7</td><td>Storeroom</td></tr>
        <tr><td class="val">3</td><td>Corridor</td><td class="val">8</td><td>Other</td></tr>
        <tr><td class="val">4</td><td>Dining</td><td></td><td></td></tr>
      </table>
      <div style="font-size:0.58em; font-weight:700; color:var(--navy); text-transform:uppercase; letter-spacing:0.1em; margin:8px 0 4px">Zone types (0 – 3)</div>
      <table class="tbl">
        <tr><th>ID</th><th>Zone</th><th>Typical rooms</th></tr>
        <tr><td class="val">0</td><td>Living</td><td>Living room, dining</td></tr>
        <tr><td class="val">1</td><td>Dynamic</td><td>Corridor, entrance</td></tr>
        <tr><td class="val">2</td><td>Static</td><td>Bedroom, bathroom</td></tr>
        <tr><td class="val">3</td><td>Functional</td><td>Kitchen, storeroom</td></tr>
      </table>
    </div>
  </div>
</div>

---

<div class="sidebar"><span class="seminar">Digital tools for<br>Graph Machine Learning</span><span class="assignment">Final Assignment - G02</span></div>
<div class="inner">
  <div class="sec-hdr"><div class="section-num">03</div><div class="section-sub">Graph Structure</div></div>
  <h1>From Plan to Graph — Plan 10000</h1>
  <hr>

  <img src="img/plan_graph.png" style="width:100%; height:300px; object-fit:contain; object-position:center; display:block; margin-top:2px;">
  <div class="img-cap" style="margin:4px 0 10px;">Plan 10000 — room types (left) and spatial connectivity graph (right)</div>

  <div class="flow" style="margin-top:4px;">
    <div class="flow-box" style="border-left:3px solid #7B61FF">
      <div class="f-label">Zone label per node</div>
      <div class="f-sub">graph_in input</div>
    </div>
    <div class="flow-arrow">→</div>
    <div class="flow-box" style="border-left:3px solid var(--rust)">
      <div class="f-label">Graph topology</div>
      <div class="f-sub">door / entrance edges</div>
    </div>
    <div class="flow-arrow">→</div>
    <div class="flow-box" style="border-left:3px solid var(--navy)">
      <div class="f-label">Room type prediction</div>
      <div class="f-sub">GraphSAGE-Pool output</div>
    </div>
  </div>
</div>

---

<div class="sidebar"><span class="seminar">Digital tools for<br>Graph Machine Learning</span><span class="assignment">Final Assignment - G02</span></div>
<div class="inner">
  <div class="sec-hdr"><div class="section-num">04</div><div class="section-sub">Next Steps</div></div>
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
