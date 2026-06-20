import rhinoscriptsyntax as rs

# Colors from Color.ByValueInRange(label, minValue=0, maxValue=8)
ROOM_COLORS = {
    'bedroom':    (68,  1,   84),
    'livingroom': (70,  44,  122),
    'kitchen':    (58,  80,  138),
    'dining':     (44,  113, 142),
    'corridor':   (34,  144, 139),
    'stairs':     (44,  173, 127),
    'storeroom':  (95,  200, 96),
    'bathroom':   (172, 220, 48),
    'balcony':    (253, 231, 37),
}

def set_layer_colors():
    layers = rs.LayerNames()
    if not layers:
        print('No layers found.')
        return

    changed = []
    for layer in layers:
        # Get just the last part of the layer name (e.g. "room_type_k::0-bedroom" -> "0-bedroom")
        short = layer.split('::')[-1].strip()

        for room_type, rgb in ROOM_COLORS.items():
            # Match "bedroom", "0-bedroom", "bedroom_1" etc.
            if room_type in short:
                rs.LayerColor(layer, rgb)
                changed.append(f'  {layer}  ->  RGB{rgb}')
                break

    if changed:
        print('Layer colors updated:')
        for c in changed:
            print(c)
    else:
        print('No matching layers found. Check that your layer names contain the room type (bedroom, livingroom, etc.)')

set_layer_colors()
