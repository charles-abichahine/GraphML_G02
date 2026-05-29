# Team Notes — GraphML_G02

A living document to keep the team oriented. Update it as decisions are made.

---

## What are we doing?

We are building a graph-based machine learning pipeline for architectural floor plans.
The goal is to take a floor plan, represent it as a graph, and use a pretrained neural network
to predict what each room is — bedroom, kitchen, bathroom, etc. — based only on its position
in the spatial zone structure and how it connects to other rooms.

No image processing. No geometry fed into the model. Just graph topology.

---

## The Dataset — Modified Swiss Dwellings (MSD)

5,372 Swiss residential floor plans, each stored as two paired NetworkX graphs in `.pickle` format.
Download from Kaggle (see README) and place in `01_dataset/data/`. These files are large and gitignored.

### graph_in — the input
This is what the model receives. Each node represents a room and carries one attribute:

| Attribute | Type | Values |
|---|---|---|
| `zoning_type` | int | 0 = Living, 1 = Dynamic, 2 = Static, 3 = Functional |

Each edge represents a connection between two adjacent rooms and carries:

| Attribute | Type | Values |
|---|---|---|
| `connectivity` | str | `'door'` or `'entrance'` |

### graph_out — the target
This is what we want to predict. Same graph structure, but nodes now carry the ground-truth room label plus geometry:

| Attribute | Type | Description |
|---|---|---|
| `room_type` | int | 0–8 (see table below) |
| `geometry` | shapely Polygon | 2D room outline |
| `centroid` | shapely Point | centre of the room |

### Room types
| ID | Name | ID | Name |
|---|---|---|---|
| 0 | Balcony | 5 | Kitchen |
| 1 | Bathroom | 6 | Living Room |
| 2 | Bedroom | 7 | Storeroom |
| 3 | Corridor | 8 | Other |
| 4 | Dining | | |

`Other` (8) typically refers to shared circulation spaces — stairwells, lift shafts, landings.

### What the pickle file actually is
It is a serialized Python object. There is no image or visual attached to it.
When you load it you get a NetworkX graph with attributes on nodes and edges.
The floor plan visualizations in `explore_dataset.ipynb` are drawn by reading the
`geometry` polygons from each node and rendering them with matplotlib. We built that from scratch.

---

## The Task

Given `graph_in` (zone labels + connectivity), predict `room_type` on every node.

The model never sees coordinates, areas, or shapes — only the graph structure.
It must infer that a node with zone=2 (static) connected by doors to a corridor and a bedroom
is probably a bathroom, based on patterns learned from 5,000+ floor plans.

---

## The Model — GraphSAGE-Pool

From Paper 2 (eCAADe 2024, Cardiff University). Trained on the full MSD dataset.
Architecture: GraphSAGE with pooling aggregation, 4 layers, ~95% node classification accuracy.

We are not training a model. We are running this pretrained model on our own reconstructed floor plan
and comparing its predictions against the original MSD labels.

The pretrained weights are in the faculty notebook `S06-15 GML Node Classification.ipynb`.

---

## Pipeline — What Each Step Does

### Step 1 — Floor Plan Recreation `01_dataset/floor_plan/`
Pick one floor plan from the MSD dataset and recreate it in Rhino.
We chose **plan 10000**.

- Use `export_to_rhino.ipynb` to export the DXF — this gives you the room outlines directly from the pickle file, already scaled and labelled by room type
- In Rhino, clean up the geometry: rooms must be closed polylines, adjacent rooms must share the exact same edge (no gaps, no overlaps)
- The DXF has separate layers per room type and a graph overlay layer you can toggle off

Why recreate it instead of using the data directly? Because the next step (TopologicPy) needs clean Rhino geometry as input — it can't read pickle files.

### Step 2 — Graph Construction `02_graph_construction/`
Convert the Rhino floor plan into a graph using TopologicPy.

TopologicPy reads the geometry and automatically detects which rooms share walls.
Each shared wall with an opening becomes an edge. You then need to manually assign:
- `zoning_type` (0–3) to each node — based on the original MSD labels from plan 10000
- `connectivity` (door/entrance) to each edge — based on opening type

Reference notebook: `S03-07 Spatial Intelligence Part 1.ipynb`

### Step 3 — Graph Analysis `03_graph_analysis/`
Once the graph is built, analyse its structure using NetworkX:

- **Degree centrality** — how many rooms each room connects to
- **Betweenness centrality** — which rooms act as bridges between parts of the plan
- **Closeness centrality** — how easily each room is reached from the rest

This step is about understanding the spatial logic of the floor plan as a network,
not about machine learning.

### Step 4 — Node Classification `04_node_classification/`
Load the pretrained GraphSAGE-Pool model and run it on the graph from Step 2.

The model takes `zoning_type` and connectivity as input and outputs a predicted `room_type`
for each node. Compare the predictions to the original MSD ground truth for plan 10000.

Reference notebook: `S06-15 GML Node Classification.ipynb`

---

## What is Done

- [x] Repo structure set up, environment configured (`environment.yml`)
- [x] MSD dataset downloaded locally (gitignored, not committed)
- [x] Dataset exploration notebook (`explore_dataset.ipynb`) — browse any plan, view room types and graph overlay
- [x] DXF export notebook (`export_to_rhino.ipynb`) — exports plan 10000 to Rhino with layers
- [x] Plan 10000 DXF exported and opened in Rhino
- [x] Presentation (`05_results/presentation/index.html`)

## What is Still To Do

- [ ] Clean up plan 10000 geometry in Rhino (shared edges, closed polylines)
- [ ] Build graph from Rhino geometry using TopologicPy
- [ ] Assign zone labels and edge connectivity types
- [ ] Graph analysis (centrality metrics)
- [ ] Run pretrained model and compare predictions to ground truth
- [ ] Document results in `05_results/`


