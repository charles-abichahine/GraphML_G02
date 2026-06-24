**Graph Analysis of Narkomfin Building — Type F Apartment (Three Floors)**

GraphML — Assignment 02 by Group 02

TopologicPy + Python (Jupyter Notebook)

**Building Overview**

The Narkomfin Building was designed by Moisei Ginzburg and Ignaty Milinis and completed in 1930 in Moscow. The Type F apartment is one of the building's key duplex typologies — a three-storey unit that inverts the relationship between corridor and dwelling found in the Type K. Where the Type K places its continuous corridor on L1 with rooms above, the Type F organises itself around a continuous middle floor (L2) that functions as the primary living and circulation level, with fragmented room floors both above (L3) and below (L1).

The unit was loaded from a single OBJ file containing all three floor plans and nineteen stair surfaces. The stairs span the full height of the building (Z=0 to Z=6), and the code automatically creates stair connections at both the L1→L2 and L2→L3 junctions. L1 comprises multiple disconnected room surfaces, L2 is a single continuous plan, and L3 is similarly fragmented into multiple separate rooms.

The floor plans were converted into a spatial graph using the same grid-sampling pipeline as the Type K analysis: a regular 0.5-unit grid, ray-casting point-in-polygon filtering, 4-neighbour adjacency per floor, and stair-edge stitching between adjacent floor pairs. Seven metrics were computed and visualised.

**Building graph**

![Building Graph](exports/F%20Type/Ftype_building%20graph_.5.png)

The combined three-floor building graph at GRID_SIZE=0.5. Red dots are graph nodes (cell centroids), grey lines are adjacency edges, and vertical lines are stair connections. The three floors are separated vertically for visual clarity.

Key findings:

* L2 (middle floor) reads as the densest, most continuous mesh of the three floors. It runs the full length of the unit as a single unbroken surface, producing a wide band of well-connected cells. This is the spatial backbone of the Type F apartment.
* L1 (bottom) and L3 (top) are both visibly fragmented — each comprises multiple disconnected room islands that rely entirely on stairs for access to L2 and to each other.
* The stair edges (vertical lines) connect all three floors. Each stair location produces two vertical connections — one from L1 to L2 and one from L2 to L3 — creating a ladder-like vertical structure through the building.
* The fragmentation is symmetric: rooms exist both above and below the circulation floor. This is the defining characteristic of the Type F — the corridor floor is sandwiched between two layers of private rooms, unlike the Type K where rooms sit only above.

**Closeness centrality — heatmap**

![Closeness Centrality](exports/F%20Type/Ftype_closeness%20centrality_.5.png)

Colour shows how globally accessible each cell is. Yellow and orange mark the most integrated cells; blue and purple mark cells that take the longest to reach from everywhere else.

Key findings:

* The brightest region — highest closeness — sits squarely on L2, concentrated in the centre of the plan. This confirms L2 as the topological heart of the apartment: the cells with the shortest average path distance to every other cell across all three floors.
* The closeness gradient on L2 is linear along the corridor, peaking at the centre and falling toward both ends. This is the same pattern seen in the Type K corridor, but here it operates on the middle floor rather than the bottom.
* L1 and L3 rooms are uniformly blue-purple — topologically deep. Reaching any room on L1 or L3 from the corridor requires descending or ascending via a stair, then navigating within the isolated room. The rooms at the far ends of both upper and lower floors are the darkest — the most remote spaces in the entire apartment.
* The gradient is notably more symmetric than the Type K. Because rooms exist on both sides of the corridor floor (above and below), the closeness drop-off is distributed vertically in both directions. The corridor is equidistant from L1 and L3, producing a balanced accessibility profile.
* Architecturally, this reveals the Constructivist design logic of the Type F: the living floor is the spatial integrator, with privacy increasing in both vertical directions — downward to L1 rooms and upward to L3 rooms.

**Betweenness centrality — heatmap**

![Betweenness Centrality](exports/F%20Type/Ftype_betweeness%20centrality_.5.png)

Colour shows how often each cell lies on shortest paths between all other pairs of cells. Yellow marks critical bottlenecks; dark blue marks cells that carry no through-traffic.

Key findings:

* The highest betweenness forms a bright hot line running along the L2 corridor centreline — an even more concentrated spine than in the Type K. Virtually all movement between any two spaces in the building must pass through this single linear band on the middle floor.
* The stair landing zones on L2 show localised betweenness spikes at both the L1-facing and L3-facing stair connections. These cells absorb all vertical traffic in both directions, making them doubly loaded compared to the Type K's stairs (which only connect two floors).
* L1 and L3 rooms are almost entirely dark — near-zero betweenness. They are pure destination spaces. No shortest path between any two other cells routes through them. This is the topological signature of dead-end rooms accessed from a central spine.
* The betweenness concentration is more extreme than in the Type K because the corridor must serve rooms on two floors instead of one. Every cross-floor path (L1→L3) must traverse L2 twice — once ascending, once on the corridor, once ascending again — making the corridor the mandatory intermediary for all vertical movement.
* This makes the Type F corridor the most structurally critical space in the building. Any obstruction on L2 would sever access not just to one floor of rooms but to two.

**Shortest path**

![Shortest Path](exports/F%20Type/Ftype_shortest%20path.png)

The red line is the topological shortest path from L1 to L3 — a full cross-building traversal spanning all three floors. The blue line is the geometrically straightened version within each floor's boundary. The vertical red segments are the stair connections between floors.

Key findings:

* The path ascends from L1 via a stair to L2, traverses the full length of the L2 corridor, then ascends again via a second stair to reach L3. The corridor is the mandatory horizontal transit layer — there is no direct L1-to-L3 shortcut.
* The L2 segment is by far the longest portion of the path, confirming the corridor's role as the primary horizontal routing channel. The L1 and L3 segments are short — just enough to reach the stair from the origin room and the destination room from the stair.
* The straightened (blue) path closely follows the topological (red) path on L2, indicating the corridor is narrow enough that the grid graph already produces a geometrically efficient route.
* The two vertical transitions (L1→L2 and L2→L3) are clearly visible as vertical jumps. The path selects the stairs closest to its origin and destination, confirming that stair placement directly controls cross-floor routing efficiency.
* This three-floor traversal reveals the fundamental movement logic of the Type F: horizontal movement is handled exclusively by L2; vertical movement is constrained to stair locations; and any L1↔L3 journey necessarily passes through the middle floor.

**Degree centrality — heatmap**

![Degree Centrality](exports/F%20Type/Ftype_degree%20centrality_.5.png)

Colour shows how many direct neighbours each cell has. Yellow marks cells with the most immediate connections; purple marks cells that touch few others.

Key findings:

* The floor plan is almost uniformly salmon-orange across all three floors, indicating consistent local connectivity. Interior cells have 4 neighbours; edge cells have 2-3. The Type F shows the same degree uniformity as the Type K — the plan is topologically flat at the local scale.
* The few brighter yellow spots correspond to stair landing cells on L2, where the stair edges add fifth and sixth connections (links to both L1 and L3). These are the only cells in the building with above-average local degree.
* L1 and L3 room interiors have the same orange tone as L2 — locally, a room cell has the same connectivity as a corridor cell. The hierarchy between corridor and rooms only manifests at the global scale (closeness, betweenness), not the local scale.
* The edges and corners of the disconnected L1 and L3 rooms show slightly cooler tones where cells lose neighbours at room boundaries.

**Clustering coefficient**

![Clustering Coefficient](exports/F%20Type/Ftype_clustering%20coefficient_.5.png)

The clustering coefficient measures how interconnected a node's immediate neighbours are.

Key findings:

* The entire heatmap is uniformly dark — all clustering coefficients are zero. This is the expected result for a 4-neighbour rectilinear grid: no two neighbours of a cell are themselves neighbours, so triangles cannot form.
* This confirms that the Type F, like the Type K, has no locally clustered spatial zones. The plan is strictly sequential at every scale — no ring corridors, no courtyards, no loop connections. You can only go forward or back.

**Community detection**

![Community Detection](exports/F%20Type/Ftype_community%20detection_.5.png)

Each colour marks a distinct cluster of cells that are more densely connected internally than to the rest of the network. The Louvain algorithm groups the plan into zones based purely on graph topology.

Key findings:

* The communities slice the building into longitudinal bands — vertical sections that each contain a segment of the L2 corridor plus the L1 and L3 rooms directly above and below it. This is the same pattern found in the Type K, but extended symmetrically into three floors.
* **Purple/blue (west portion)** — the western end of L2 and the L1 rooms below it form a community. These cells share the nearest western stairs and are topologically remote from the east end.
* **Teal/blue-green (centre-west)** — the centre-west corridor segment and its overhead L3 rooms and underlying L1 rooms group together. This zone contains several stair connections.
* **Yellow-green (centre-east to east)** — the eastern portion of the apartment, including L2 corridor, L3 rooms above, and L1 rooms below, forms another band.
* **Green (far east L3 and ends)** — the extremities cluster as isolated endpoint communities.
* The community boundaries run perpendicular to the corridor, not between floors. The stair connections are strong enough to bind L1, L2, and L3 cells at each longitudinal position into a single community rather than letting the floors separate. This confirms the building's vertical integration — each community is a three-floor vertical slice of the apartment.
* The three-floor version of this pattern is more complex than the Type K's two-floor version, but the underlying logic is identical: the building self-organises into vertical slices, not horizontal layers.

**Conclusion**

**Circulation Patterns** The Type F apartment channels all horizontal movement through the L2 corridor — a single continuous floor that sits between two layers of fragmented rooms. Unlike the Type K, where the corridor is at the base with rooms above, the Type F places its circulation spine in the middle, making it the mandatory intermediary for all cross-floor movement. Any journey between L1 and L3 must pass through L2 twice.

**Hierarchy of Spaces** There is a clear three-tier spatial hierarchy. The L2 corridor is maximally accessible and carries all through-traffic (highest closeness and betweenness). The L1 and L3 rooms are topological dead ends — private destination spaces with near-zero betweenness. The privacy gradient runs symmetrically outward from the corridor: down to L1 and up to L3.

**Accessibility and Connectivity** Accessibility follows a linear gradient along L2, peaking in the centre and falling toward both ends. Cross-floor accessibility is entirely dependent on stair placement. The rooms at the far ends of L1 and L3 are the most remote spaces in the building. The vertical symmetry means that L1 rooms and L3 rooms at the same longitudinal position have roughly equal accessibility — neither floor is privileged over the other.

**Functional Zoning** The community detection reveals the same longitudinal-band pattern as the Type K: vertical slices that each contain a corridor segment and its associated rooms above and below. The Type F extends this pattern into three floors, creating thicker vertical slices that span the full height of the building. This is the spatial signature of the Constructivist duplex — the corridor binds each vertical slice into a coherent unit, with privacy increasing in both vertical directions away from the circulation spine.

**Why graph analysis is useful for this building** The Type F is compact but vertically complex — three floors, one continuous corridor, and dozens of disconnected rooms above and below. The graph analysis reveals that the middle floor is not just a corridor but the structural spine that holds the entire apartment together. The betweenness heatmap shows it carries a double load compared to the Type K corridor (serving rooms on two floors instead of one). The community detection confirms that the building's true spatial units are three-floor vertical slices — a finding that quantifies Ginzburg's concept of integrated living cells stacked around a shared circulation layer.
