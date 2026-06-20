"""
name_objects_by_layer.py
Run inside Rhino: Tools > PythonScript > Run

For each floor type (k, f):
  - Names every visible room volume   as  bedroom_1, corridor_2, ...
  - Names every visible aperture face as  door_1, passage_2, ...
  - Exports type_{ft}_rooms.obj and type_{ft}_apertures.obj
    to the same folder as the .3dm file (assets folder).

Layer structure expected:
  room_type_k :: 0-bedroom, 1-livingroom, ... (sublayers)
  room_type_f :: 0-bedroom, 1-livingroom, ...
  door_type_k :: door, passage, entrance_door
  door_type_f :: door, passage, entrance_door
"""

import rhinoscriptsyntax as rs
import os
import re


def visible_objects_on_layer(layer):
    """Return all visible objects on a single layer."""
    if not rs.LayerVisible(layer):
        return []
    objs = rs.ObjectsByLayer(layer) or []
    return [o for o in objs if not rs.IsObjectHidden(o)]


def name_and_collect(parent_layer):
    """
    Walk sublayers of parent_layer, name each visible object
    as  <room_type>_<counter>  and return the full list.
    """
    all_objects = []
    counters    = {}

    for layer in (rs.LayerNames() or []):
        if not layer.startswith(parent_layer + '::'):
            continue

        sublayer  = layer.split('::')[-1]
        type_name = re.sub(r'^\d+-', '', sublayer)   # "0-bedroom" -> "bedroom"

        for obj in visible_objects_on_layer(layer):
            counters[type_name] = counters.get(type_name, 0) + 1
            rs.ObjectName(obj, f'{type_name}_{counters[type_name]}')
            all_objects.append(obj)

    return all_objects


def export_selection(objects, filepath):
    """Select objects and export to OBJ."""
    rs.UnselectAllObjects()
    rs.SelectObjects(objects)
    rs.Command(f'-_Export "{filepath}" _Enter _Enter', False)
    rs.UnselectAllObjects()


def run():
    doc_path = rs.DocumentPath()
    if not doc_path:
        print('ERROR: Save the .3dm file first.')
        return

    export_dir = os.path.dirname(doc_path)

    for ft in ['k', 'f']:
        print(f'\n=== Floor type: {ft.upper()} ===')

        # --- Rooms ---
        room_parent = f'room_type_{ft}'
        rooms = name_and_collect(room_parent)
        if rooms:
            path = os.path.join(export_dir, f'type_{ft}_rooms.obj')
            export_selection(rooms, path)
            print(f'  Rooms:     {len(rooms)} objects -> {path}')
        else:
            print(f'  Rooms:     no visible objects on {room_parent}::*  — skipped')

        # --- Apertures ---
        door_parent = f'door_type_{ft}'
        doors = name_and_collect(door_parent)
        if doors:
            path = os.path.join(export_dir, f'type_{ft}_apertures.obj')
            export_selection(doors, path)
            print(f'  Apertures: {len(doors)} objects -> {path}')
        else:
            print(f'  Apertures: no visible objects on {door_parent}::*  — skipped')

    print('\nDone.')


run()
