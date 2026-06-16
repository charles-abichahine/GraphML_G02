import rhinoscriptsyntax as rs
import os
from collections import defaultdict

ROOM_LAYERS = [
    "bedroom", "livingroom", "kitchen", "dining",
    "corridor", "stairs", "storeroom", "bathroom", "balcony"
]

DOOR_LAYERS = ["door", "passage", "entrance_door"]

# Export folder — same directory as this Rhino file
EXPORT_FOLDER = rs.DocumentPath()
ROOMS_OBJ     = os.path.join(EXPORT_FOLDER, "type_k_rooms.obj")
APERTURES_OBJ = os.path.join(EXPORT_FOLDER, "type_k_apertures.obj")

# ── Step 1: Name all objects by layer with a counter ──────────────────────
counters  = defaultdict(int)
room_ids  = []
door_ids  = []
renamed   = 0
skipped   = 0

for obj_id in rs.AllObjects():
    layer = rs.ObjectLayer(obj_id)
    layer_name = layer.split("::")[-1]

    if layer_name in ROOM_LAYERS:
        counters[layer_name] += 1
        name = "{}_{}".format(layer_name, counters[layer_name])
        rs.ObjectName(obj_id, name)
        room_ids.append(obj_id)
        renamed += 1

    elif layer_name in DOOR_LAYERS:
        counters[layer_name] += 1
        name = "{}_{}".format(layer_name, counters[layer_name])
        rs.ObjectName(obj_id, name)
        door_ids.append(obj_id)
        renamed += 1

    else:
        skipped += 1

print("Naming done. Renamed: {}  |  Skipped: {}".format(renamed, skipped))
print("Counts per type:")
for layer_name, count in sorted(counters.items()):
    print("  {}: {}".format(layer_name, count))

# ── Step 2: Export rooms.obj ───────────────────────────────────────────────
rs.UnselectAllObjects()
rs.SelectObjects(room_ids)
rs.Command('-_Export "{}" _Enter _Enter'.format(ROOMS_OBJ), False)
rs.UnselectAllObjects()
print("Exported rooms.obj  →  {}".format(ROOMS_OBJ))

# ── Step 3: Export apertures.obj ───────────────────────────────────────────
rs.SelectObjects(door_ids)
rs.Command('-_Export "{}" _Enter _Enter'.format(APERTURES_OBJ), False)
rs.UnselectAllObjects()
print("Exported apertures.obj  →  {}".format(APERTURES_OBJ))
