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

### Step 1 — Floor Plan Design `01_dataset/floor_plan/`
Design our own residential floor plan in Rhino, from scratch.

- Rooms must be closed polylines, adjacent rooms must share the exact same edge (no gaps, no overlaps)
- The floor plan must be residential — confirmed by faculty

### Step 2 — Graph Construction & Analysis `02_graph_construction_analysis/`
Convert the Rhino floor plan into a graph, then analyse its structure — both with TopologicPy.
(The reference notebook covers construction and analysis together, so we're treating this as one combined step rather than splitting it across two folders.)

**Construction**
TopologicPy reads the geometry and automatically detects which rooms share walls.
Each shared wall with an opening becomes an edge. You then need to manually assign:
- `zoning_type` (0–3) to each node — based on the spatial role of each room (Living / Dynamic / Static / Functional)
- `connectivity` (door/entrance) to each edge — based on opening type

**Analysis**
Once the graph is built, analyse its structure using TopologicPy:
- **Degree centrality** — how many rooms each room connects to
- **Betweenness centrality** — which rooms act as bridges between parts of the plan
- **Closeness centrality** — how easily each room is reached from the rest

This step is about understanding the spatial logic of the floor plan as a network,
not about machine learning.

Reference notebook: `S03-07 Spatial Intelligence Part 1.ipynb`

### Step 3 — Node Classification `03_node_classification/`
Load the pretrained GraphSAGE-Pool model and run it on the graph from Step 2.

The model takes `zoning_type` and connectivity as input and outputs a predicted `room_type`
for each node. Compare the predictions to the room types we actually designed for our own
floor plan, to see how well a model trained on the MSD dataset generalises to a new plan.

Reference notebook: `S06-15 GML Node Classification.ipynb`

---

## What is Done

- [x] Repo structure set up, environment configured (`environment.yml`)
- [x] MSD dataset downloaded locally (gitignored, not committed)
- [x] Dataset exploration notebook (`explore_dataset.ipynb`) — browse any plan, view room types and graph overlay
- [x] DXF export notebook (`export_to_rhino.ipynb`) — exports any MSD plan to DXF for inspection in Rhino
- [x] Sample plan (10000) exported to DXF and opened in Rhino to study the dataset's structure
- [x] Presentation (`04_results/presentation/slides.md`)

## What is Still To Do

- [ ] Design our own residential floor plan in Rhino
- [ ] Build graph from Rhino geometry using TopologicPy
- [ ] Assign zone labels (zoning_type 0–3) and edge connectivity types (door/entrance)
- [ ] Graph analysis — degree, betweenness, closeness centrality using TopologicPy
- [ ] Run pretrained GraphSAGE-Pool model for node classification
- [ ] Document results in `04_results/`


