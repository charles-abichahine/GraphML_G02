**Comparative Graph Analysis of Narkomfin Building — Type K vs Type F Apartments**

GraphML — Assignment 02 by Group 02

TopologicPy + Python (Jupyter Notebook)

**Building Overview**

The Narkomfin Building (1930, Moscow) by Moisei Ginzburg and Ignaty Milinis contains several apartment typologies arranged along a shared corridor spine. This report compares two of the primary unit types — the Type K and Type F — using identical graph-based spatial analysis methods.

* **Type K** is a two-storey duplex. L1 is a single continuous corridor floor; L2 comprises eleven disconnected rooms above it. The corridor is at the base, rooms above. Two floors, twelve stair connections.
* **Type F** is a three-storey unit. L2 (middle floor) is a single continuous living/corridor floor; L1 (below) and L3 (above) are both fragmented into multiple disconnected rooms. The corridor is in the middle, rooms above and below. Three floors, nineteen stair connections at two junction levels.

Both units were analysed with the same pipeline: 0.5-unit grid sampling, ray-casting point-in-polygon filtering, 4-neighbour adjacency, and stair-edge stitching. Seven metrics were computed for each.

---

## Building Graphs

| Type K (2 floors) | Type F (3 floors) |
| :---- | :---- |
| ![K Graph](exports/K%20Type/building%20graph_.5.png) | ![F Graph](exports/F%20Type/Ftype_building%20graph_.5.png) |

**Type K:** L1 is a dense continuous mesh; L2 is fragmented into room islands above it. Stair edges cluster in the centre. The graph is asymmetric — one dense floor, one sparse.

**Type F:** L2 (middle) is the dense continuous mesh; L1 and L3 are fragmented room floors above and below. Stair edges connect all three levels. The graph is vertically symmetric — sparse, dense, sparse.

**Comparison:** Both types organise around a single continuous corridor floor, but the Type F sandwiches it between two room layers instead of placing it at the base. The Type F has roughly 50% more nodes and edges due to the third floor, and its stair count is higher (19 stairs × 2 junctions = up to 38 stair edges vs 12 for the Type K).

---

## Closeness Centrality

| Type K | Type F |
| :---- | :---- |
| ![K Closeness](exports/K%20Type/closeness%20centrality_.5.png) | ![F Closeness](exports/F%20Type/Ftype_closeness%20centrality_.5.png) |

**Type K:** The hottest zone is a linear band along the L1 corridor, peaking at the centre. L2 rooms are uniformly cold. The gradient is one-directional — accessibility decreases upward from the corridor to the rooms above.

**Type F:** The hottest zone is on L2 (middle floor), again peaking at the centre of the corridor. L1 and L3 rooms are uniformly cold. The gradient is bidirectional — accessibility decreases both downward to L1 and upward to L3.

**Comparison:** The closeness profiles are structurally identical — a hot corridor spine with cold room extremities — but the Type F distributes the cold zones symmetrically above and below instead of stacking them only above. This means:
* The Type F corridor is more central in the building's topology (equidistant from rooms in both directions) than the Type K corridor (which is at the bottom, maximally distant from the highest rooms).
* The most remote rooms in the Type F are at the ends of L1 and L3; in the Type K they are at the far ends of L2. The Type F may have a slightly higher maximum topological depth due to the extra floor.

---

## Betweenness Centrality

| Type K | Type F |
| :---- | :---- |
| ![K Betweenness](exports/K%20Type/betweeness%20centrality_.5.png) | ![F Betweenness](exports/F%20Type/Ftype_betweeness%20centrality_.5.png) |

**Type K:** A sharp hot line runs along the L1 corridor centreline. Stair landings show localised spikes. L2 rooms are entirely dark.

**Type F:** An equally sharp hot line on L2, with stair landing spikes at both the L1-facing and L3-facing connections. L1 and L3 rooms are entirely dark.

**Comparison:** Both types concentrate virtually all betweenness into the corridor — the same single-spine routing pattern. However:
* The Type F corridor carries a double load: it serves rooms on two floors instead of one, and any L1↔L3 path must traverse L2 as a mandatory intermediary.
* The Type F stair landings absorb traffic from two directions (up and down), making them more critical chokepoints.
* Both buildings are structurally fragile in the same way — blocking the corridor severs access to all rooms — but the Type F is more fragile because a corridor obstruction disconnects two floors of rooms instead of one.

---

## Shortest Path

| Type K | Type F |
| :---- | :---- |
| ![K Path](exports/K%20Type/shortest%20path_.5.png) | ![F Path](exports/F%20Type/Ftype_shortest%20path.png) |

**Type K:** The path runs the length of the L1 corridor, then ascends one stair to L2. One horizontal traverse, one vertical jump.

**Type F:** The path ascends from L1 to L2, traverses the L2 corridor, then ascends again to L3. One vertical jump, one horizontal traverse, one vertical jump.

**Comparison:**
* The Type K path is a simple L-shape: horizontal then vertical.
* The Type F path is a Z-shape: vertical, horizontal, vertical. The L2 corridor segment is the longest portion — the horizontal transit layer dominates.
* In both types, the straightened (blue) path closely tracks the topological (red) path, confirming that the narrow corridor geometry leaves little room for geometric optimisation.
* The Type F path necessarily crosses two floor boundaries, adding stair traversal overhead. The vertical distance is doubled, but the critical bottleneck remains horizontal — the corridor length controls total path distance.

---

## Degree Centrality

| Type K | Type F |
| :---- | :---- |
| ![K Degree](exports/K%20Type/degree%20centrality_.5.png) | ![F Degree](exports/F%20Type/Ftype_degree%20centrality_.5.png) |

**Comparison:** Both types show nearly uniform degree across all cells. The only bright spots are stair landing cells (yellow dots), where vertical edges add extra connections. The Type F stair landings may show slightly higher degree than the Type K's because each L2 stair cell can connect to both L1 and L3 (potential degree 6 vs 5). Otherwise, the local connectivity signature is identical — the spatial hierarchy only emerges at global scales.

---

## Clustering Coefficient

| Type K | Type F |
| :---- | :---- |
| ![K Clustering](exports/K%20Type/clustering%20coefficient_.5.png) | ![F Clustering](exports/F%20Type/Ftype_clustering%20coefficient_.5.png) |

**Comparison:** Both are uniformly zero — identical results. The 4-neighbour rectilinear grid cannot form triangles. Neither apartment has ring corridors, courtyards, or loop connections. Both enforce strictly sequential spatial logic.

---

## Community Detection

| Type K | Type F |
| :---- | :---- |
| ![K Communities](exports/K%20Type/community%20detection_.5.png) | ![F Communities](exports/F%20Type/Ftype_community%20detection_.5.png) |

**Type K:** Communities slice the building into longitudinal bands — each containing a segment of the L1 corridor plus the L2 rooms directly above. Two-floor vertical slices.

**Type F:** The same longitudinal-band pattern, but extended into three floors — each community contains a segment of the L2 corridor plus L1 rooms below and L3 rooms above. Three-floor vertical slices.

**Comparison:**
* Both types self-organise into vertical slices, not horizontal layers. The stair connections are strong enough to bind rooms to their nearest corridor segment across floor boundaries.
* The Type F communities are thicker — they span three floors instead of two — confirming that the middle-floor corridor serves as a more powerful integrating element when it has rooms on both sides.
* In both cases, the community boundaries run perpendicular to the corridor, dividing the apartment into longitudinal zones. This means the building's true spatial units are not rooms or floors but vertical bands — exactly what Ginzburg's "living cell" concept intended.

---

## Comparative Summary

| Metric | Type K (2 floors) | Type F (3 floors) |
| :---- | :---- | :---- |
| **Floors** | 2 (corridor + rooms above) | 3 (rooms below + corridor + rooms above) |
| **Corridor position** | Bottom (L1) | Middle (L2) |
| **Stair connections** | 12 (one junction) | 19 × 2 junctions (up to 38 edges) |
| **Closeness gradient** | One-directional (up from corridor) | Bidirectional (up and down from corridor) |
| **Betweenness load** | Corridor serves 1 floor of rooms | Corridor serves 2 floors of rooms |
| **Structural fragility** | Corridor failure disconnects L2 | Corridor failure disconnects L1 and L3 |
| **Community pattern** | 2-floor vertical slices | 3-floor vertical slices |
| **Clustering** | Zero (no loops) | Zero (no loops) |
| **Degree variation** | Minimal (stair spots only) | Minimal (stair spots only) |

---

## Conclusion

**Same spine, different symmetry.** The Type K and Type F share the same fundamental spatial logic — a single continuous corridor that absorbs all circulation, with private rooms accessed only via stairs. The difference is symmetry: the Type K is asymmetric (corridor at the bottom, rooms above), while the Type F is symmetric (corridor in the middle, rooms above and below).

**The middle position is stronger.** Placing the corridor in the middle (Type F) rather than at the base (Type K) makes it a more effective spatial integrator. The L2 corridor in the Type F is equidistant from both room floors, producing a balanced accessibility profile. The L1 corridor in the Type K is maximally distant from the far end of L2, creating a steeper accessibility gradient.

**But more fragile.** The Type F corridor carries a double structural load. It is the only horizontal routing layer for two floors of rooms instead of one. The betweenness analysis shows it as an even sharper bottleneck than the Type K corridor. Any obstruction on L2 disconnects twice the number of rooms.

**Vertical slicing is universal.** Community detection in both types produces the same pattern: longitudinal vertical bands, not horizontal floor separations. The stairs bind rooms to their nearest corridor segment strongly enough to override the floor boundary. This is the graph's confirmation of Ginzburg's design intent — the Narkomfin apartments are not stacked flats but integrated three-dimensional living cells, organised vertically around a shared circulation spine.

**Graph analysis reveals what plans cannot.** Viewed in plan, the Type K and Type F look like variations on the same narrow corridor scheme. The graph analysis exposes the structural difference: the Type F's middle-floor corridor is topologically more central but also more critical. It quantifies the trade-off between integration (the middle position connects equally in both directions) and resilience (the middle position concentrates all risk into a single layer). These are invisible in a floor plan but legible in the graph.
