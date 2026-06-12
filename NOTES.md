# Team Notes — GraphML_G02

A living document to keep the team oriented. Update it as decisions are made.

---

## What are we doing?

Graph-based ML pipeline for architectural floor plans. We take a floor plan, represent it as a graph, and use a pretrained neural network to predict room types from spatial zone labels and connectivity — no image processing, no geometry fed into the model.

---

## The Dataset — Modified Swiss Dwellings (MSD)

5,372 Swiss residential floor plans as paired NetworkX graphs in `.pickle` format.
Download from Kaggle (see README) and place in `01_dataset/data/`. Gitignored.

Each plan has two graphs:
- **`graph_in`** — input: nodes carry `zoning_type` (0 Living · 1 Dynamic · 2 Static · 3 Functional), edges carry `connectivity` (door/entrance)
- **`graph_out`** — target: nodes carry `room_type` (0–8) and shapely geometry

Room types: 0 Balcony · 1 Bathroom · 2 Bedroom · 3 Corridor · 4 Dining · 5 Kitchen · 6 Living Room · 7 Storeroom · 8 Other

---

## The Model — GraphSAGE-Pool

Pretrained on the full MSD dataset (eCAADe 2024, Cardiff University). ~95% node classification accuracy.
We are not training — we run it on our Narkomfin graphs and interpret the predictions.
Weights in `03_node_classification/assets/msd_node_classifier.pt`.

---

## Pipeline

### Step 1 — Floor Plan Input `01_dataset/floor_plan/`
Two Narkomfin Building floor plans (Ginzburg & Milinis, Moscow 1930) — F-type duplex and K-type communal block — redrawn in Rhino as closed polylines with shared edges.

### Step 2 — Graph Analysis `02_graph_analysis/`
OBJ → face BREP (`notebooks/02.1`), then spatial analysis across three notebooks (`notebooks/02.2–02.4`): closeness centrality, betweenness centrality, shortest path. Results saved to `02_graph_analysis/results/`.

### Step 3 — Node Classification `03_node_classification/`
Label nodes with `zoning_type` and edges with connectivity, export graph CSVs (`notebooks/03.1`), then run the pretrained model (`notebooks/03.2`). Output in `03_node_classification/results/`.

---

## What is Done

- [x] Repo structure set up, environment configured (`environment.yml`)
- [x] MSD dataset downloaded locally (gitignored)
- [x] Dataset exploration (`notebooks/01.1`) and DXF export (`notebooks/01.2`) notebooks
- [x] Narkomfin floor plans modelled in Rhino, exported as OBJ, converted to face BREP
- [x] Presentation (`04_presentation/slides.md`)

## What is Still To Do

- [ ] Graph analysis — closeness centrality, betweenness centrality, shortest path for both plans
- [ ] Assign zone labels (`zoning_type` 0–3) and connectivity types to Narkomfin graphs
- [ ] Run pretrained GraphSAGE-Pool model for node classification
- [ ] Document and interpret results
- [ ] Finalise presentation
