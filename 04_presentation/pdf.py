#!/usr/bin/env python3
"""
pdf.py  —  GraphML_G02 Presentation
Run:    python 04_presentation/pdf.py
Output: 04_presentation/slides.pdf
"""

import math
from pathlib import Path
from PIL import Image as _PILImage
_PILImage.MAX_IMAGE_PIXELS = None  # lift decompression bomb limit for large renders
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── PATHS ──────────────────────────────────────────────────────────────────────
HERE   = Path(__file__).parent
IMG    = HERE / 'img'
PNGS   = IMG / 'pngs'
OUTPUT = HERE / 'slides.pdf'

# ── PAGE ───────────────────────────────────────────────────────────────────────
W, H = 1920, 1080

# ── FONTS ──────────────────────────────────────────────────────────────────────
_CAL  = 'C:/Windows/Fonts/calibri.ttf'
_CALB = 'C:/Windows/Fonts/calibrib.ttf'
if Path(_CAL).exists():
    pdfmetrics.registerFont(TTFont('Body',      _CAL))
    pdfmetrics.registerFont(TTFont('Body-Bold', _CALB))
    FONT, FONT_B = 'Body', 'Body-Bold'
else:
    FONT, FONT_B = 'Helvetica', 'Helvetica-Bold'

# ── COLORS ─────────────────────────────────────────────────────────────────────
BG     = HexColor('#000000')
WHITE  = HexColor('#FFFFFF')
GREY   = HexColor('#AAAAAA')
LGREY  = HexColor('#CCCCCC')
DGREY  = HexColor('#444444')
XDGREY = HexColor('#141414')
FGREY  = HexColor('#888888')
RED    = HexColor('#FF3B30')
BLUE   = HexColor('#0A84FF')

ROOM_TYPES = [
    (HexColor('#440154'), 'bedroom'),
    (HexColor('#472d7b'), 'livingroom'),
    (HexColor('#3b528b'), 'kitchen'),
    (HexColor('#2c728e'), 'dining'),
    (HexColor('#21908c'), 'corridor'),
    (HexColor('#27ad81'), 'stairs'),
    (HexColor('#5ec962'), 'storeroom'),
    (HexColor('#addc30'), 'bathroom'),
    (HexColor('#fde725'), 'balcony'),
]

ACCENT_TEAL   = HexColor('#21908c')
ACCENT_PURPLE = HexColor('#472d7b')
ACCENT_YELLOW = HexColor('#fde725')
ACCENT_GREEN  = HexColor('#5ec962')

# ── LAYOUT ─────────────────────────────────────────────────────────────────────
PAD       = 80
GUTTER    = 48
CONTENT_W = W - 2 * PAD       # 1760
COL_W     = (CONTENT_W - GUTTER) // 2

Y_LABEL   = H - PAD           # 1000
Y_HEAD    = H - PAD - 92      # 908
HEAD_SIZE = 80
Y_LEGEND  = 110
Y_BAR     = 36

# ── SHARED 3D IMAGE FRAME (slides 07–10, same bounding box) ──────────────────
_3D_X = 0
_3D_Y = 50
_3D_W = W
_3D_H = 940


# ── ICON HELPERS ───────────────────────────────────────────────────────────────

def _icon_network(c, cx, cy, size=56, color=ACCENT_TEAL):
    r = size * 0.42
    nodes = [
        (cx - r * 1.1, cy - r * 0.5),
        (cx,           cy + r * 0.9),
        (cx + r * 1.1, cy - r * 0.5),
        (cx,           cy - r * 0.3),
    ]
    edges = [(0, 1), (0, 3), (1, 2), (1, 3), (2, 3)]
    c.setStrokeColor(color)
    c.setLineWidth(2.5)
    for i, j in edges:
        c.line(nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1])
    nr = size * 0.095
    c.setFillColor(color)
    for nx, ny in nodes:
        c.circle(nx, ny, nr, fill=1, stroke=0)


def _icon_grid(c, cx, cy, size=56, color=ACCENT_PURPLE):
    n, gap = 3, 4
    cell = (size - gap * (n - 1)) / n
    x0 = cx - size / 2
    y0 = cy - size / 2
    pattern = [1, 0, 1, 0, 1, 0, 1, 0, 1]
    for row in range(n):
        for col in range(n):
            idx = row * n + col
            c.setFillColor(color if pattern[idx] else HexColor('#2a2a2a'))
            c.rect(x0 + col * (cell + gap), y0 + row * (cell + gap),
                   cell, cell, fill=1, stroke=0)


def _icon_bed(c, cx, cy, size=52, color=ACCENT_PURPLE):
    w, h = size, size * 0.65
    x0, y0 = cx - w / 2, cy - h / 2
    c.setFillColor(color)
    c.rect(x0, y0, w, h * 0.35, fill=1, stroke=0)       # base
    c.setFillColor(HexColor('#2a2a2a'))
    c.rect(x0, y0 + h * 0.35, w, h * 0.65, fill=1, stroke=0)  # mattress
    c.setFillColor(color)
    c.circle(cx - w * 0.25, y0 + h * 0.75, w * 0.12, fill=1, stroke=0)
    c.circle(cx + w * 0.25, y0 + h * 0.75, w * 0.12, fill=1, stroke=0)


def _icon_corridor(c, cx, cy, size=56, color=ACCENT_TEAL):
    c.setFillColor(color)
    c.rect(cx - size / 2, cy - size * 0.15, size, size * 0.30, fill=1, stroke=0)
    for side in [-1, 1]:
        c.setFillColor(HexColor('#2a2a2a'))
        bx = cx - size / 2 + (0 if side == -1 else size * 0.75)
        c.rect(bx, cy - size * 0.35, size * 0.25, size * 0.70, fill=1, stroke=0)


def _icon_gear(c, cx, cy, size=56, color=ACCENT_GREEN):
    r_inner = size * 0.28
    r_outer = size * 0.45
    teeth   = 8
    pts = []
    for i in range(teeth * 2):
        angle = i * math.pi / teeth
        r = r_outer if i % 2 == 0 else r_inner
        pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    c.setFillColor(color)
    p = c.beginPath()
    p.moveTo(pts[0][0], pts[0][1])
    for px, py in pts[1:]:
        p.lineTo(px, py)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(BG)
    c.circle(cx, cy, size * 0.17, fill=1, stroke=0)


def _icon_balcony(c, cx, cy, size=56, color=ACCENT_YELLOW):
    r = size * 0.44
    p = c.beginPath()
    p.moveTo(cx - r, cy)
    p.arcTo(cx - r, cy, cx + r, cy + r * 2, 180, 180)
    p.close()
    c.setFillColor(color)
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(BG)
    c.rect(cx - r * 0.6, cy - size * 0.08, r * 1.2, size * 0.16, fill=1, stroke=0)


# ── CORE DRAWING HELPERS ───────────────────────────────────────────────────────

def fill_bg(c):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def draw_label(c, text, x=PAD, y=Y_LABEL):
    c.setFont(FONT, 22)
    c.setFillColor(GREY)
    for ch in text.upper():
        c.drawString(x, y, ch)
        x += c.stringWidth(ch, FONT, 22) + 8


def draw_headline(c, text, x=PAD, y=Y_HEAD, size=HEAD_SIZE):
    c.setFont(FONT_B, size)
    c.setFillColor(WHITE)
    for line in (text if isinstance(text, list) else [text]):
        c.drawString(x, y, line)
        y -= size * 1.18
    return y


def draw_accent_line(c, y_after, width=None, color=ACCENT_TEAL, thickness=3):
    if width is None:
        width = CONTENT_W
    y = y_after + HEAD_SIZE * 0.72 - 6
    c.setFillColor(color)
    c.rect(PAD, y, width, thickness, fill=1, stroke=0)
    return y - thickness - 18


def draw_bottom_bar(c, n, total):
    c.setFont(FONT, 19)
    c.setFillColor(FGREY)
    c.drawString(PAD, Y_BAR, 'GraphML_G02')
    c.drawRightString(W - PAD, Y_BAR, f'{n:02d} / {total:02d}')


def draw_sep_line(c, y, x_start=PAD):
    c.setStrokeColor(HexColor('#444444'))
    c.setLineWidth(1.5)
    c.line(x_start, y, W - PAD, y)


def wrap_and_draw(c, text, x, y, max_w, font, size, color=GREY, spacing=1.55, align='left'):
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    line  = ''
    def _draw_line(line, y):
        if align == 'center':
            c.drawCentredString(x + max_w / 2, y, line)
        else:
            c.drawString(x, y, line)
    for word in words:
        test = (line + ' ' + word).strip()
        if c.stringWidth(test, font, size) > max_w and line:
            _draw_line(line, y)
            y    -= size * spacing
            line  = word
        else:
            line = test
    if line:
        _draw_line(line, y)
        y -= size * spacing
    return y


def draw_bullets(c, items, x=PAD, y=None, size=28, max_w=None,
                 color=GREY, dot_color=ACCENT_TEAL):
    if y is None:
        y = Y_HEAD - 200
    if max_w is None:
        max_w = CONTENT_W - 40
    text_x = x + size * 1.1
    for item in items:
        c.setFont(FONT_B, size)
        c.setFillColor(dot_color)
        c.drawString(x, y, '·')
        y = wrap_and_draw(c, item, text_x, y, max_w - size * 1.1, FONT, size, color)
    return y


def draw_image(c, path, x, y, w, h, scale_mode='contain'):
    """scale_mode: 'contain' | 'fill_width' | 'boost'(1.5× contain, clipped)."""
    fpath = Path(path)
    if fpath.exists():
        try:
            img    = ImageReader(str(fpath))
            iw, ih = img.getSize()
            if scale_mode == 'fill_width':
                scale  = w / iw
                nw, nh = w, ih * scale
                ix     = x + (w - nw) / 2
                iy     = y + (h - nh) / 2
                c.saveState()
                clip = c.beginPath()
                clip.rect(x, y, w, h)
                c.clipPath(clip, stroke=0)
                c.drawImage(img, ix, iy, nw, nh, mask='auto')
                c.restoreState()
            elif scale_mode == 'boost':
                scale  = min(w / iw, h / ih) * 1.7
                nw, nh = iw * scale, ih * scale
                ix     = x + (w - nw) / 2
                iy     = y + (h - nh) / 2
                c.saveState()
                clip = c.beginPath()
                clip.rect(x, y, w, h)
                c.clipPath(clip, stroke=0)
                c.drawImage(img, ix, iy, nw, nh, mask='auto')
                c.restoreState()
            else:
                scale  = min(w / iw, h / ih)
                nw, nh = iw * scale, ih * scale
                c.drawImage(img, x + (w - nw) / 2, y + (h - nh) / 2, nw, nh, mask='auto')
            return
        except Exception:
            pass
    c.setFillColor(XDGREY)
    c.rect(x, y, w, h, fill=1, stroke=0)
    c.setFont(FONT, 22)
    c.setFillColor(DGREY)
    c.drawCentredString(x + w / 2, y + h / 2, f'[ {fpath.name} ]')


def draw_legend_strip(c, x=PAD, y=Y_LEGEND, width=None, caption='Node color encodes room type'):
    if width is None:
        width = CONTENT_W
    n  = len(ROOM_TYPES)
    sw = width / n
    # Caption title at the top
    if caption:
        c.setFont(FONT, 17)
        c.setFillColor(FGREY)
        c.drawCentredString(W / 2, y + 62, caption)
    for i, (color, name) in enumerate(ROOM_TYPES):
        sx = x + i * sw
        c.setFillColor(color)
        c.rect(sx, y + 22, sw - 2, 26, fill=1, stroke=0)
        c.setFont(FONT, 15)
        c.setFillColor(GREY)
        c.drawCentredString(sx + sw / 2, y, f'{i} – {name}')


def draw_thermal_strip(c, x=PAD, y=Y_LEGEND, width=None,
                       label_l='high', label_r='low'):
    if width is None:
        width = CONTENT_W
    steps = 60
    sw    = width / steps
    keys  = [
        (0.00, (210, 35,  20)),
        (0.30, (240, 150, 30)),
        (0.55, (250, 220, 50)),
        (0.75, (60,  180, 120)),
        (1.00, (20,  70,  200)),
    ]
    def lerp(t):
        for j in range(len(keys) - 1):
            t0, c0 = keys[j];  t1, c1 = keys[j + 1]
            if t0 <= t <= t1:
                f = (t - t0) / (t1 - t0)
                return Color(*[(c0[k] + f * (c1[k] - c0[k])) / 255 for k in range(3)])
        return Color(*[v / 255 for v in keys[-1][1]])
    for i in range(steps):
        c.setFillColor(lerp(i / (steps - 1)))
        c.rect(x + i * sw, y + 22, sw + 0.5, 26, fill=1, stroke=0)
    c.setFont(FONT, 17)
    c.setFillColor(GREY)
    c.drawString(x, y, label_l)
    c.drawRightString(x + width, y, label_r)


def draw_card(c, x, y, w, h, accent_color=ACCENT_TEAL, border=5):
    c.setFillColor(XDGREY)
    c.rect(x, y, w, h, fill=1, stroke=0)
    c.setFillColor(accent_color)
    c.rect(x, y, border, h, fill=1, stroke=0)


def draw_callout_tag(c, cx, cy, key, val, accent, w=260, h=90):
    """Small annotation tag: colored top border + key label + value.
    cy = top edge of the tag."""
    x = cx - w // 2
    y = cy - h
    c.setFillColor(Color(0.06, 0.06, 0.06, alpha=0.90))
    c.rect(x, y, w, h, fill=1, stroke=0)
    c.setFillColor(accent)
    c.rect(x, y + h - 4, w, 4, fill=1, stroke=0)
    c.setFont(FONT, 15)
    c.setFillColor(GREY)
    c.drawString(x + 14, y + h - 22, key.upper())
    c.setFont(FONT_B, 22)
    c.setFillColor(WHITE)
    c.drawString(x + 14, y + 14, val)


def draw_overlay_panel(c, x, y, w, h, title, items, accent,
                       title_size=26, item_size=21):
    c.setFillColor(Color(0.04, 0.04, 0.04, alpha=0.86))
    c.rect(x, y, w, h, fill=1, stroke=0)
    c.setFillColor(accent)
    c.rect(x, y, 4, h, fill=1, stroke=0)
    pad = 18
    ty  = y + h - pad - title_size
    c.setFont(FONT_B, title_size)
    c.setFillColor(accent)
    c.drawString(x + pad, ty, title)
    ty -= title_size * 0.5 + 10
    for item in items:
        c.setFont(FONT_B, item_size)
        c.setFillColor(accent)
        c.drawString(x + pad, ty, '·')
        ty = wrap_and_draw(c, item, x + pad + item_size * 1.1, ty,
                           w - pad - item_size * 1.1 - pad,
                           FONT, item_size, GREY, spacing=1.45)


def _3d_slide_base(c, n, total, img_name, label_text, headline_text):
    """Label + headline behind image; accent line drawn on top of image."""
    fill_bg(c)
    draw_label(c, label_text)
    y_after = draw_headline(c, headline_text, size=72)
    draw_accent_line(c, y_after)
    draw_image(c, PNGS / img_name, _3D_X, _3D_Y, _3D_W, _3D_H)


# ── SLIDES ─────────────────────────────────────────────────────────────────────

def slide_01(c, n, total):
    fill_bg(c)
    # Thin teal top bar
    c.setFillColor(ACCENT_TEAL)
    c.rect(0, H - 8, W, 8, fill=1, stroke=0)

    draw_label(c, 'G r a p h M L  ·  G r o u p  0 2')

    # Main title
    title_y = int(H * 0.56)
    c.setFont(FONT_B, 100)
    c.setFillColor(WHITE)
    c.drawString(PAD, title_y, 'Graph Learning Pipeline')
    c.drawString(PAD, title_y - 118, 'for Architectural Floor Plans')

    # Spacer line — more distance from title
    line_y = title_y - 150
    c.setFillColor(ACCENT_TEAL)
    c.rect(PAD, line_y, CONTENT_W, 3, fill=1, stroke=0)

    # Subtitle — below the line with breathing room
    c.setFont(FONT, 40)
    c.setFillColor(GREY)
    c.drawString(PAD, line_y - 56,
                 'Node classification on the Narkomfin Building using GraphSAGE')

    # Course + team — bigger
    c.setFont(FONT, 26)
    c.setFillColor(DGREY)
    c.drawString(PAD, 90, 'MaCAD 2025/26  ·  Digital Tools for Graph Machine Learning')
    c.setFont(FONT, 26)
    c.setFillColor(FGREY)
    c.drawRightString(W - PAD, 90,
        'Lakzhmy Zaro  ·  María Sánchez  ·  Charles Abi Chahine  ·  Emilie El Chidiac')

    draw_bottom_bar(c, n, total)


def slide_02(c, n, total):
    fill_bg(c)
    draw_label(c, 'C o n t e n t s')

    sections = [
        ('A', 'Modified Swiss Dwellings', ROOM_TYPES[0][0],
         'A benchmark of 5,372 residential floor plans encoded as spatial graphs'),
        ('B', 'Literature',               ROOM_TYPES[2][0],
         'Two papers and one pretrained GraphSAGE-Pool model'),
        ('C', 'Data Structure',           ROOM_TYPES[4][0],
         'Nodes, edges, features and ground-truth room-type labels'),
        ('D', 'The Narkomfin Building',   ROOM_TYPES[5][0],
         'Dom-kommuna, two unit types, one ideal graph ML subject'),
        ('E', 'Graph Analysis',           ROOM_TYPES[7][0],
         'Centrality measures, shortest paths and spatial logic'),
        ('F', 'Node Classification',      ROOM_TYPES[8][0],
         'Room type prediction from zoning features using GraphSAGE'),
    ]

    usable_h = Y_HEAD - (Y_BAR + 60)
    row_h    = usable_h / len(sections)
    y_top    = Y_HEAD + 10       # top of first row

    for i, (num, title, accent, desc) in enumerate(sections):
        y_row_top = y_top - i * row_h
        y_row_bot = y_row_top - row_h
        # colored left bar
        c.setFillColor(accent)
        c.rect(PAD, y_row_bot + 14, 4, row_h - 28, fill=1, stroke=0)
        # number
        c.setFont(FONT_B, 36)
        c.setFillColor(accent)
        c.drawString(PAD + 22, y_row_top - 40, num)
        # title
        c.setFont(FONT, 36)
        c.setFillColor(WHITE)
        c.drawString(PAD + 108, y_row_top - 40, title)
        # short description — below the title, with gap before separator
        c.setFont(FONT, 32)
        c.setFillColor(DGREY)
        c.drawString(PAD + 108, y_row_bot + 28, desc)
        # separator line
        draw_sep_line(c, y_row_bot + 14, x_start=PAD + 108)

    draw_bottom_bar(c, n, total)


def slide_03(c, n, total):
    fill_bg(c)
    draw_label(c, 'A  ·  D a t a s e t')
    y_after = draw_headline(c, 'Modified Swiss Dwellings')
    y_line  = draw_accent_line(c, y_after)

    stats = [
        ('5,372', 'Floor Plans',   ROOM_TYPES[0][0]),
        ('9',     'Room Types',    ROOM_TYPES[4][0]),
        ('4',     'Zone Types',    ROOM_TYPES[7][0]),
        ('.pickle', 'Graph Format', ROOM_TYPES[8][0]),
    ]
    box_w = (CONTENT_W - 3 * GUTTER) // 4
    box_h = 140
    box_y = y_line - 20 - box_h

    for i, (val, lbl, col) in enumerate(stats):
        bx = PAD + i * (box_w + GUTTER)
        draw_card(c, bx, box_y, box_w, box_h, accent_color=ACCENT_TEAL)
        c.setFont(FONT_B, 58)
        c.setFillColor(WHITE)
        c.drawString(bx + 24, box_y + 62, val)
        c.setFont(FONT, 22)
        c.setFillColor(GREY)
        c.drawString(bx + 24, box_y + 30, lbl)

    img_bot = Y_LEGEND + 60
    img_top = box_y - 8
    draw_image(c, IMG / 'samples3.png', PAD, img_bot, CONTENT_W, img_top - img_bot, scale_mode='fill_width')

    draw_legend_strip(c)
    draw_bottom_bar(c, n, total)


def slide_04(c, n, total):
    fill_bg(c)
    draw_label(c, 'B  ·  L i t e r a t u r e')
    y_after = draw_headline(c, 'Two papers, one pipeline.')
    y_line  = draw_accent_line(c, y_after)

    card_h   = 520                                          # fixed to content height
    avail_h  = (y_line - 12) - (Y_BAR + 60)
    card_bot = Y_BAR + 60 + (avail_h - card_h) // 2       # centered vertically
    card_top = card_bot + card_h
    pad_in   = 40

    for col_x, accent, tag, icon_fn, title_lines, src, items in [
        (PAD, ACCENT_TEAL, 'Paper 1',
         lambda cx, cy: _icon_grid(c, cx, cy, size=64, color=ACCENT_TEAL),
         ['MSD: A Benchmark Dataset for Floor Plan',
          'Generation of Building Complexes'],
         'ECCV 2024  ·  TU Delft',
         ['5,372 Swiss residential floor plans',
          '3 modalities: image, geometry, graph',
          'Graph encodes spatial zones, not room types',
          'Primary data source for this project']),
        (PAD + COL_W + GUTTER, ACCENT_TEAL, 'Paper 2',
         lambda cx, cy: _icon_network(c, cx, cy, size=64, color=ACCENT_TEAL),
         ['GNN for Node Classification and',
          'Attribute Allocation in Architectural BIM'],
         'eCAADe 2024  ·  Cardiff University',
         ['Uses the same MSD dataset',
          'Converts floor plans to graphs via TopologicPy',
          'Benchmarks GCN, GAT, GraphSAGE',
          'GraphSAGE-Pool, 4 layers, ~95% accuracy',
          'Pretrained model applied to our floor plan']),
    ]:
        draw_card(c, col_x, card_bot, COL_W, card_h, accent_color=accent)
        cy = card_top - pad_in

        # Icon top-right of card
        icon_fn(col_x + COL_W - 80, card_top - 70)

        # "Paper N" label — same visual weight as the title
        c.setFont(FONT_B, 36)
        c.setFillColor(accent)
        c.drawString(col_x + pad_in, cy, tag)
        cy -= 52

        # Paper title — slightly smaller so the tag doesn't compete
        c.setFont(FONT, 30)
        c.setFillColor(LGREY)
        for line in title_lines:
            c.drawString(col_x + pad_in, cy, line)
            cy -= 38
        cy -= 14

        # Source
        c.setFont(FONT, 22)
        c.setFillColor(GREY)
        c.drawString(col_x + pad_in, cy, src)
        cy -= 44

        # Divider
        c.setStrokeColor(accent)
        c.setLineWidth(0.5)
        c.line(col_x + pad_in, cy + 20, col_x + COL_W - pad_in, cy + 20)
        cy -= 20

        # Bullets
        draw_bullets(c, items, x=col_x + pad_in, y=cy,
                     size=28, max_w=COL_W - 2 * pad_in, dot_color=accent)

    draw_bottom_bar(c, n, total)


def slide_05(c, n, total):
    fill_bg(c)
    draw_label(c, 'C  ·  D a t a  S t r u c t u r e')
    y_after = draw_headline(c, 'What the graph encodes.')
    y_line  = draw_accent_line(c, y_after)

    # ── 2 × 2 equal cards ─────────────────────────────────────────────────────
    card_gap  = 20
    card_w    = (CONTENT_W - card_gap) // 2
    top_gap   = 80                                       # breathing room below accent line
    grid_bot  = Y_BAR + 60
    usable_h  = y_line - 20 - top_gap - grid_bot
    card_h    = (usable_h - card_gap) // 2

    # card origins (bottom-left corner of each card)
    cards_xy = [
        (PAD,                      grid_bot + card_h + card_gap),  # top-left
        (PAD,                      grid_bot),                       # bottom-left
        (PAD + card_w + card_gap,  grid_bot + card_h + card_gap),  # top-right
        (PAD + card_w + card_gap,  grid_bot),                      # bottom-right
    ]

    def _table_row(rx, ry, cols, widths, row_h, is_header=False, accent=WHITE):
        """Draw one table row starting at (rx, ry) as the bottom-left."""
        cx = rx
        for txt, w in zip(cols, widths):
            font = FONT_B if is_header or cols.index(txt) == 0 else FONT
            color = GREY if is_header else (WHITE if cols.index(txt) == 0 else LGREY)
            c.setFont(font, 17 if is_header else 19)
            c.setFillColor(color)
            c.drawString(cx + 10, ry + 9, str(txt))
            cx += w

    def _draw_data_card(bx, by, accent, icon_fn, card_title, headers, rows, col_ratios,
                        col_colors=None):
        """col_colors: optional dict {col_index: [color_per_row]} for custom cell colors."""
        c.setFillColor(XDGREY)
        c.rect(bx, by, card_w, card_h, fill=1, stroke=0)
        c.setFillColor(accent)
        c.rect(bx, by + card_h - 5, card_w, 5, fill=1, stroke=0)

        pad   = 22
        inner = card_w - 2 * pad
        widths = [int(r * inner) for r in col_ratios]

        icon_fn(bx + card_w - 54, by + card_h - 56)

        ty = by + card_h - pad - 28
        c.setFont(FONT_B, 28)
        c.setFillColor(WHITE)
        c.drawString(bx + pad, ty, card_title)
        ty -= 14

        ty -= 44

        c.setFillColor(accent)
        c.rect(bx + pad, ty, inner, 1.5, fill=1, stroke=0)
        ty -= 4

        row_h = 30
        c.setFillColor(HexColor('#242424'))
        c.rect(bx + pad, ty - row_h, inner, row_h, fill=1, stroke=0)
        _table_row(bx + pad, ty - row_h, headers, widths, row_h, is_header=True)
        ty -= row_h

        for ri, row in enumerate(rows):
            bg = HexColor('#181818') if ri % 2 == 0 else HexColor('#1e1e1e')
            c.setFillColor(bg)
            c.rect(bx + pad, ty - row_h, inner, row_h, fill=1, stroke=0)
            cx = bx + pad
            for ci, (cell, w) in enumerate(zip(row, widths)):
                # Determine color: custom override > accent for col0 > white/grey
                if col_colors and ci in col_colors:
                    clr = col_colors[ci][ri]
                    bold = True
                elif ci == 0:
                    clr = accent
                    bold = True
                else:
                    clr = WHITE if ri % 2 == 0 else GREY
                    bold = ri % 2 == 0
                c.setFont(FONT_B if bold else FONT, 19)
                c.setFillColor(clr)
                if str(cell):
                    c.drawString(cx + 10, ty - row_h + 9, str(cell))
                cx += w
            ty -= row_h

    # ── Card 0: graph_in — model input ────────────────────────────────────────
    _draw_data_card(
        *cards_xy[0], ACCENT_TEAL,
        lambda cx, cy: _icon_network(c, cx, cy, size=50, color=ACCENT_TEAL),
        'graph_in — model input',
        ['Attribute', 'Type', 'Values'],
        [('zoning_type',  'int', '0 · 1 · 2 · 3'),
         ('connectivity', 'str', "'door' · 'entrance'")],
        [0.35, 0.18, 0.47],
    )

    # ── Card 1: graph_out — ground truth ──────────────────────────────────────
    _draw_data_card(
        *cards_xy[1], ACCENT_TEAL,
        lambda cx, cy: _icon_grid(c, cx, cy, size=50, color=ACCENT_TEAL),
        'graph_out — ground truth',
        ['Attribute', 'Type', 'Description'],
        [('room_type', 'int',     '0 – 8'),
         ('geometry',  'Polygon', '2D room outline'),
         ('centroid',  'Point',   'centre of room')],
        [0.32, 0.22, 0.46],
    )

    # ── Card 2: Room types (0–8) ───────────────────────────────────────────────
    _rt_rows = [
        (str(i), ROOM_TYPES[i][1],
         str(i + 5) if i + 5 < len(ROOM_TYPES) else '',
         ROOM_TYPES[i + 5][1] if i + 5 < len(ROOM_TYPES) else '')
        for i in range(5)
    ]
    _draw_data_card(
        *cards_xy[2], ACCENT_TEAL,
        lambda cx, cy: _icon_bed(c, cx, cy, size=50, color=ACCENT_TEAL),
        'Room types (0 – 8)',
        ['ID', 'Room', 'ID', 'Room'],
        _rt_rows,
        [0.08, 0.35, 0.08, 0.49],
        col_colors={
            0: [ROOM_TYPES[i][0]     for i in range(5)],
            2: [ROOM_TYPES[i+5][0] if i+5 < len(ROOM_TYPES) else GREY for i in range(5)],
        },
    )

    # ── Card 3: Zone types (0–3) ───────────────────────────────────────────────
    _zone_colors = [HexColor('#E8DAEF'), HexColor('#D5F5E3'),
                    HexColor('#FDEBD0'), HexColor('#D6EAF8')]
    _draw_data_card(
        *cards_xy[3], ACCENT_TEAL,
        lambda cx, cy: _icon_gear(c, cx, cy, size=50, color=ACCENT_TEAL),
        'Zone types (0 – 3)',
        ['ID', 'Zone', 'Typical rooms'],
        [('0', 'Private',    'bedroom'),
         ('1', 'Dynamic',    'corridor, entrance'),
         ('2', 'Static',     'bedroom, bathroom'),
         ('3', 'Functional', 'kitchen, storeroom')],
        [0.08, 0.24, 0.68],
        col_colors={0: _zone_colors},
    )

    draw_bottom_bar(c, n, total)


def slide_06(c, n, total):
    fill_bg(c)
    draw_label(c, 'C  ·  D a t a  S t r u c t u r e')
    y_after = draw_headline(c, 'From floor plan to graph.')
    y_line  = draw_accent_line(c, y_after)

    # Flow boxes directly under the accent line
    n_boxes = 3
    box_h   = 82
    gap_box = 56
    box_w   = (CONTENT_W - (n_boxes - 1) * gap_box) // n_boxes
    fy_top  = y_line - 16          # flush under accent line
    fy_bot  = fy_top - box_h

    boxes = [
        ('Zone label per node',   'zoning_type input',     ACCENT_PURPLE),
        ('Graph topology',        'door / entrance edges', ACCENT_TEAL),
        ('Room type prediction',  'GraphSAGE-Pool output', ACCENT_YELLOW),
    ]
    for i, (title, sub, col) in enumerate(boxes):
        bx = PAD + i * (box_w + gap_box)
        draw_card(c, bx, fy_bot, box_w, box_h, accent_color=col)
        c.setFont(FONT_B, 26)
        c.setFillColor(WHITE)
        c.drawString(bx + 20, fy_bot + 46, title)
        c.setFont(FONT, 20)
        c.setFillColor(GREY)
        c.drawString(bx + 20, fy_bot + 18, sub)
        if i < n_boxes - 1:
            ax = bx + box_w + gap_box // 2 - 14
            c.setFont(FONT, 30)
            c.setFillColor(DGREY)
            c.drawString(ax, fy_bot + 30, '→')

    # Mini legends at the bottom
    leg_h     = 52
    leg_bot   = Y_BAR + 60
    leg_top   = leg_bot + leg_h
    half_w    = (CONTENT_W - GUTTER) // 2
    swatch    = 14
    leg_font  = 13

    # — Room types (left, 9 items) — show name, not number ——————
    rt_item_w = half_w / len(ROOM_TYPES)
    c.setFont(FONT_B, leg_font)
    c.setFillColor(FGREY)
    c.drawString(PAD, leg_top - leg_font - 2, 'Room types')
    for i, (color, name) in enumerate(ROOM_TYPES):
        sx = PAD + i * rt_item_w
        c.setFillColor(color)
        c.rect(sx, leg_bot + 18, rt_item_w - 3, swatch, fill=1, stroke=0)
        c.setFont(FONT, 11)
        c.setFillColor(GREY)
        c.drawCentredString(sx + rt_item_w / 2, leg_bot + 4, name)

    # — Right side: zone types + edge type legend ——————————————
    zone_colors = [HexColor('#E8DAEF'), HexColor('#D5F5E3'),
                   HexColor('#FDEBD0'), HexColor('#D6EAF8')]
    zone_names  = ['Private', 'Dynamic', 'Static', 'Functional']
    rx       = PAD + half_w + GUTTER
    # split right half: zones left portion, edge legend right portion
    zone_w   = int(half_w * 0.58)
    edge_w   = half_w - zone_w - GUTTER
    ex       = rx + zone_w + GUTTER

    zt_item_w = zone_w / len(zone_names)
    c.setFont(FONT_B, leg_font)
    c.setFillColor(FGREY)
    c.drawString(rx, leg_top - leg_font - 2, 'Zone types')
    for i, (color, name) in enumerate(zip(zone_colors, zone_names)):
        zx = rx + i * zt_item_w
        c.setFillColor(color)
        c.rect(zx, leg_bot + 18, zt_item_w - 3, swatch, fill=1, stroke=0)
        c.setFont(FONT, 11)
        c.setFillColor(GREY)
        c.drawCentredString(zx + zt_item_w / 2, leg_bot + 4, f'{i} – {name}')

    # Edge types
    c.setFont(FONT_B, leg_font)
    c.setFillColor(FGREY)
    c.drawString(ex, leg_top - leg_font - 2, 'Edge types')
    edge_types = [('door',     HexColor('#1A2744')),
                  ('entrance', HexColor('#C0392B'))]
    line_len = 28
    item_gap = 90
    ey = leg_bot + 22
    for j, (elabel, ecolor) in enumerate(edge_types):
        ox = ex + j * item_gap
        c.setStrokeColor(ecolor)
        c.setLineWidth(2.5)
        c.line(ox, ey, ox + line_len, ey)
        c.setFont(FONT, 12)
        c.setFillColor(GREY)
        c.drawString(ox + line_len + 6, ey - 4, elabel)

    # Image fills all remaining space between the boxes and the legends
    caption_h = 36
    img_top   = fy_bot - caption_h
    img_bot   = leg_top + 8
    draw_image(c, IMG / 'plan_graph-2.png', PAD, img_bot, CONTENT_W, img_top - img_bot,
               scale_mode='fill_width')

    # Caption between boxes and image
    c.setFont(FONT, 19)
    c.setFillColor(DGREY)
    c.drawCentredString(W // 2, img_top + 8,
        'Plan 10000  ·  zone types (left) and spatial connectivity graph (right)')

    draw_bottom_bar(c, n, total)


def slide_pipeline(c, n, total):
    fill_bg(c)
    draw_label(c, 'P r o c e s s')
    y_after = draw_headline(c, 'From floor plan to prediction.')
    y_line  = draw_accent_line(c, y_after)

    stages = [
        (ACCENT_PURPLE, '01', 'Geometry',
         'The Narkomfin, redrawn in Rhino, becomes analysable solids.',
         [('02.1  OBJ to BREP',
           'Convert the exported mesh into watertight face BREPs, one solid per room.')]),
        (ACCENT_TEAL, '02', 'Spatial Analysis',
         'Measure how each room sits within the circulation network.',
         [('02.2 – 02.4  Graph analysis',
           'Closeness, betweenness and shortest-path metrics across both unit types.')]),
        (ACCENT_GREEN, '03', 'Graph Preparation',
         'Encode the building as a labelled input graph.',
         [('03.0  Rhino to cell complex',
           'Build a Topologic cell complex from the BREPs.'),
          ('03.1  Prepare graph',
           'Label nodes with zoning_type, edges with door / entrance connectivity.')]),
        (ACCENT_YELLOW, '04', 'Prediction',
         'Infer room types from zoning and topology alone.',
         [('03.2  Predict',
           'Run the pretrained GraphSAGE-Pool model and flag misclassified nodes.')]),
    ]
    n_s     = len(stages)
    arrow_w = 46
    card_w  = (CONTENT_W - (n_s - 1) * arrow_w) // n_s
    card_h   = 400
    top_lim  = y_line - 16
    bot_lim  = Y_BAR + 60
    card_top = top_lim - max(0, (top_lim - bot_lim - card_h)) / 2
    card_bot = card_top - card_h

    for i, (accent, num, title, desc, books) in enumerate(stages):
        cx0 = PAD + i * (card_w + arrow_w)
        # Card + accent top bar
        c.setFillColor(XDGREY)
        c.rect(cx0, card_bot, card_w, card_h, fill=1, stroke=0)
        c.setFillColor(accent)
        c.rect(cx0, card_top - 6, card_w, 6, fill=1, stroke=0)

        # Big stage number
        c.setFont(FONT_B, 50)
        c.setFillColor(accent)
        c.drawString(cx0 + 30, card_top - 80, num)
        # Title
        c.setFont(FONT_B, 28)
        c.setFillColor(WHITE)
        c.drawString(cx0 + 30, card_top - 124, title)
        # Stage description
        wrap_and_draw(c, desc, cx0 + 30, card_top - 156, card_w - 60,
                      FONT, 18, GREY, spacing=1.35)

        # Thin divider before notebook entries
        ey = card_top - 206
        c.setFillColor(Color(1, 1, 1, alpha=0.10))
        c.rect(cx0 + 30, ey + 26, card_w - 60, 1, fill=1, stroke=0)

        # Notebook entries — id + what it does
        for bid, bdesc in books:
            c.setFillColor(accent)
            c.circle(cx0 + 36, ey + 6, 4, fill=1, stroke=0)
            c.setFont(FONT_B, 16)
            c.setFillColor(LGREY)
            c.drawString(cx0 + 50, ey, bid)
            yy = wrap_and_draw(c, bdesc, cx0 + 50, ey - 22, card_w - 80,
                               FONT, 14, GREY, spacing=1.3)
            ey = yy - 16

        # Arrow to next stage
        if i < n_s - 1:
            ax = cx0 + card_w + arrow_w / 2
            ay = card_bot + card_h / 2
            c.setFont(FONT_B, 42)
            c.setFillColor(DGREY)
            c.drawCentredString(ax, ay - 14, '→')

    draw_bottom_bar(c, n, total)


def slide_07(c, n, total):
    _3d_slide_base(c, n, total,
                   img_name      = 'actual-3d.png',
                   label_text    = 'D  ·  T h e  N a r k o m f i n  B u i l d i n g',
                   headline_text = 'A machine for collective living.')

    # Dark strip for callout tags
    c.setFillColor(Color(0, 0, 0, alpha=0.86))
    c.rect(0, 0, W, 172, fill=1, stroke=0)

    # Six tags — evenly spaced, aligned to footer edges
    tags = [
        ('Architects', 'Ginzburg & Milinis',  ROOM_TYPES[1][0]),
        ('Year',       '1930',                ROOM_TYPES[3][0]),
        ('Location',   'Moscow, Russia',      ROOM_TYPES[4][0]),
        ('Typology',   'Dom-kommuna',         ROOM_TYPES[5][0]),
        ('Scale',      '54 units, 6 floors',  ROOM_TYPES[6][0]),
        ('Unit types', 'F-type  ·  K-type',   ROOM_TYPES[8][0]),
    ]
    gap    = 12
    tag_w  = (CONTENT_W - (len(tags) - 1) * gap) // len(tags)
    tag_h  = 96
    tag_cy = 160     # top y of tags

    for i, (key, val, accent) in enumerate(tags):
        tx = PAD + i * (tag_w + gap)
        cx = tx + tag_w // 2
        draw_callout_tag(c, cx, tag_cy, key, val, accent, w=tag_w, h=tag_h)

    draw_bottom_bar(c, n, total)


def slide_08(c, n, total):
    _3d_slide_base(c, n, total,
                   img_name      = 'actual-3d.png',
                   label_text    = 'D  ·  T h e  N a r k o m f i n  B u i l d i n g',
                   headline_text = 'Why it maps to graph ML.')

    # Why we chose the Narkomfin — three reason columns (no strip over the image)
    reasons = [
        (ACCENT_PURPLE, '01', 'Clear spatial hierarchy',
         'Discrete living cells and corridors form a readable room-to-room structure.'),
        (ACCENT_TEAL, '02', 'Repetitive unit typologies',
         'Two unit types — F-type and K-type — repeat cleanly across every floor.'),
        (ACCENT_GREEN, '03', 'Explicit functional zoning',
         'A dom-kommuna where living, communal and circulation zones are clearly defined.'),
    ]
    col_gap = 40
    col_w   = (CONTENT_W - (len(reasons) - 1) * col_gap) // len(reasons)
    base_y  = 232   # top anchor for the reason block, clear of the footer

    for i, (accent, num, title, desc) in enumerate(reasons):
        cx0 = PAD + i * (col_w + col_gap)
        # Accent top bar
        c.setFillColor(accent)
        c.rect(cx0, base_y, 48, 4, fill=1, stroke=0)
        # Number
        c.setFont(FONT_B, 20)
        c.setFillColor(accent)
        c.drawString(cx0, base_y - 32, num)
        # Title
        c.setFont(FONT_B, 28)
        c.setFillColor(WHITE)
        c.drawString(cx0, base_y - 66, title)
        # Description
        wrap_and_draw(c, desc, cx0, base_y - 100, col_w,
                      FONT, 19, LGREY, spacing=1.4)

    draw_bottom_bar(c, n, total)


def slide_09(c, n, total):
    _3d_slide_base(c, n, total,
                   img_name      = 'simplified-3d.png',
                   label_text    = 'D  ·  T h e  N a r k o m f i n  B u i l d i n g',
                   headline_text = 'Simplified model, rooms as volumes.')

    c.setFillColor(Color(0, 0, 0, alpha=0.86))
    c.rect(0, 0, W, 185, fill=1, stroke=0)
    draw_legend_strip(c, y=Y_LEGEND + 6)
    draw_bottom_bar(c, n, total)


def slide_10(c, n, total):
    fill_bg(c)
    draw_label(c, 'D  ·  T h e  N a r k o m f i n  B u i l d i n g')
    y_after = draw_headline(c, 'Exploded axonometric by floor type.', size=72)
    draw_accent_line(c, y_after)
    draw_image(c, PNGS / 'simplified-3d-exploded.png',
               PAD // 2, _3D_Y + 80, W - PAD, _3D_H - 120)

    # Floating area labels
    def _area_label(cx, cy, text):
        tw = c.stringWidth(text, FONT_B, 34) + 32
        c.setFillColor(Color(0, 0, 0, alpha=0.60))
        c.rect(cx - tw / 2, cy - 8, tw, 46, fill=1, stroke=0)
        c.setFont(FONT_B, 34)
        c.setFillColor(WHITE)
        c.drawCentredString(cx, cy + 4, text)

    _area_label(320,  530, 'Amenities')
    _area_label(1590, 500, 'F - type')
    _area_label(1570, 240, 'K - type')

    c.setFillColor(Color(0, 0, 0, alpha=0.86))
    c.rect(0, 0, W, 185, fill=1, stroke=0)
    draw_legend_strip(c, y=Y_LEGEND + 6)
    draw_bottom_bar(c, n, total)


def slide_11(c, n, total):
    fill_bg(c)
    draw_label(c, 'D  ·  T h e  N a r k o m f i n  B u i l d i n g')
    y_after = draw_headline(c, 'K-type & F-type, five levels.')
    y_line  = draw_accent_line(c, y_after)

    img_bot = Y_LEGEND + 56
    draw_image(c, PNGS / 'exploded-levels.png', 0, img_bot, W, H - img_bot - 220)

    c.setFont(FONT_B, 26)
    c.setFillColor(WHITE)
    # Left column: L1 bottom, L2 top
    c.drawString(900, 310, 'L1')
    c.drawString(900, 490, 'L2')
    # Right column: L5 top, L4 middle, L3 bottom
    c.drawString(1800, 530, 'L5')
    c.drawString(1800, 400, 'L4')
    c.drawString(1800, 265, 'L3')

    draw_legend_strip(c)
    draw_bottom_bar(c, n, total)


def _analysis_slide(c, n, total, section_lbl, headline, img_path,
                    strip_fn, strip_kw, bullets):
    fill_bg(c)
    draw_label(c, section_lbl)
    y_after = draw_headline(c, headline)
    y_line  = draw_accent_line(c, y_after)

    # Layout geometry
    n_b   = len(bullets)
    b_gap = 12
    b_w   = (CONTENT_W - (n_b - 1) * b_gap) // n_b
    b_h   = 80
    b_top = y_line - 16
    b_bot = b_top - b_h
    img_top = b_bot - 10
    img_bot = Y_LEGEND + 56

    # Image drawn first (behind boxes) — fill_width to maximise size
    draw_image(c, img_path, 0, img_bot, W, img_top - img_bot, scale_mode='fill_width')

    # Bullet boxes on top of image
    for i, txt in enumerate(bullets):
        bx = PAD + i * (b_w + b_gap)
        c.setFillColor(XDGREY)
        c.rect(bx, b_bot, b_w, b_h, fill=1, stroke=0)
        wrap_and_draw(c, txt, bx + 16, b_bot + b_h - 20,
                      b_w - 32, FONT, 22, LGREY, spacing=1.35, align='center')

    strip_fn(c, **strip_kw)
    draw_bottom_bar(c, n, total)


def slide_12(c, n, total):
    _analysis_slide(c, n, total,
        section_lbl = 'E  ·  G r a p h  A n a l y s i s',
        headline    = 'Closeness centrality, Type K.',
        img_path    = IMG / 'plan1-closeness-centrality.png',
        strip_fn    = draw_thermal_strip,
        strip_kw    = dict(label_l='high integration', label_r='low integration'),
        bullets     = [
            'Corridor scores highest — fewest steps to every room',
            'Closeness drops steadily into private cells',
            'Staircase block scores lowest, dead-end terminal',
            'Corridor is the social and circulatory core',
        ],
    )


def slide_13(c, n, total):
    _analysis_slide(c, n, total,
        section_lbl = 'E  ·  G r a p h  A n a l y s i s',
        headline    = 'Betweenness centrality, Type K.',
        img_path    = IMG / 'plan1-betweenness-centrality.png',
        strip_fn    = draw_thermal_strip,
        strip_kw    = dict(label_l='high traffic', label_r='low traffic'),
        bullets     = [
            'Central corridor sections carry the most traffic',
            'Every cross-building journey passes through them',
            'End rooms have near-zero betweenness — destinations only',
            'Corridor is the most traversed and most accessible spine',
        ],
    )


def slide_14(c, n, total):
    fill_bg(c)
    draw_label(c, 'E  ·  G r a p h  A n a l y s i s')
    y_after = draw_headline(c, 'Shortest path, Type K.')
    y_line  = draw_accent_line(c, y_after)

    # Bullet boxes directly under accent line
    bullets = [
        'Grid and straightened paths are nearly identical',
        'Only 3.7% shorter when straightened',
        'Corridor is already the straightest possible route',
        'Optimal path and only social route are the same',
    ]
    n_b   = len(bullets)
    b_gap = 12
    b_w   = (CONTENT_W - (n_b - 1) * b_gap) // n_b
    b_h   = 80
    b_top = y_line - 16
    b_bot = b_top - b_h
    img_top = b_bot - 10
    img_bot = Y_LEGEND + 56

    # Image drawn first (behind boxes)
    draw_image(c, IMG / 'plan1-shortest-path.png', 0, img_bot, W, img_top - img_bot, scale_mode='fill_width')

    for i, txt in enumerate(bullets):
        bx = PAD + i * (b_w + b_gap)
        c.setFillColor(XDGREY)
        c.rect(bx, b_bot, b_w, b_h, fill=1, stroke=0)
        wrap_and_draw(c, txt, bx + 16, b_bot + b_h - 20,
                      b_w - 32, FONT, 22, LGREY, spacing=1.35, align='center')

    # Path legend — two items centered side by side
    leg_items  = [
        (RED,  'grid path (77.2 units)'),
        (BLUE, 'straightened path (74.4 units)'),
    ]
    swatch_w   = 26
    swatch_gap = 10
    item_gap   = 60
    leg_font   = 18
    item_widths = [swatch_w + swatch_gap + c.stringWidth(lbl, FONT, leg_font)
                   for _, lbl in leg_items]
    total_w    = sum(item_widths) + item_gap
    lx0        = W / 2 - total_w / 2
    sy         = Y_LEGEND + 24
    for k, (color, label) in enumerate(leg_items):
        lx = lx0 + k * (item_widths[0] + item_gap)
        c.setFillColor(color)
        c.rect(lx, sy, swatch_w, 16, fill=1, stroke=0)
        c.setFont(FONT, leg_font)
        c.setFillColor(GREY)
        c.drawString(lx + 34, sy, label)

    draw_bottom_bar(c, n, total)


def _prediction_slide(c, n, total, unit_type, img_name):
    fill_bg(c)
    draw_label(c, 'F  ·  N o d e  C l a s s i f i c a t i o n')
    y_after = draw_headline(c, f'Room type prediction, {unit_type}.')
    draw_accent_line(c, y_after)

    img_bot = Y_LEGEND + 100
    img_h   = Y_HEAD - 20 - img_bot
    draw_image(c, PNGS / img_name, PAD, img_bot, CONTENT_W, img_h)

    c.setFont(FONT, 19)
    c.setFillColor(DGREY)
    c.drawCentredString(W // 2, img_bot - 22,
        'Predicted room types  ·  red nodes = misclassified')

    draw_legend_strip(c)
    draw_bottom_bar(c, n, total)


def slide_15(c, n, total):
    _prediction_slide(c, n, total, 'K-type', 'plot-prediction-k.png')


def slide_16(c, n, total):
    _prediction_slide(c, n, total, 'F-type', 'plot-prediction-f.png')


def slide_17(c, n, total):
    fill_bg(c)
    draw_label(c, 'C o n c l u s i o n')
    y_after = draw_headline(c, 'What the graph knows.')
    y_line  = draw_accent_line(c, y_after)

    statements = [
        (ROOM_TYPES[0][0],
         "The Narkomfin's rigid spatial hierarchy makes it an ideal graph ML subject."),
        (ROOM_TYPES[2][0],
         "Clear zoning and repetitive unit types produce clean, classifiable node features."),
        (ROOM_TYPES[4][0],
         "The corridor's dominance in centrality analysis aligns with its Dynamic node label."),
        (ROOM_TYPES[6][0],
         "Two distinct unit types offer a direct, side-by-side comparison of spatial configurations."),
        (ROOM_TYPES[8][0],
         "Orthogonal geometry translates without ambiguity into a clean TopologicPy graph."),
    ]

    usable_h  = y_line - 20 - (Y_BAR + 60)
    row_h     = usable_h / len(statements)
    num_strs  = ['01', '02', '03', '04', '05']

    for i, (accent, text) in enumerate(statements):
        ry = y_line - 20 - (i + 1) * row_h
        card_h = row_h - 10

        # Dark card, full width
        c.setFillColor(XDGREY)
        c.rect(PAD, ry, CONTENT_W, card_h, fill=1, stroke=0)
        # Viridis left border
        c.setFillColor(accent)
        c.rect(PAD, ry, 6, card_h, fill=1, stroke=0)

        # Large colored number
        num_size = min(56, int(card_h * 0.65))
        c.setFont(FONT_B, num_size)
        c.setFillColor(accent)
        c.drawString(PAD + 28, ry + (card_h - num_size) / 2 + 4, num_strs[i])

        # Statement text
        txt_size = min(30, int(card_h * 0.35))
        c.setFont(FONT, txt_size)
        c.setFillColor(LGREY)
        c.drawString(PAD + 130, ry + (card_h - txt_size) / 2 + 4, text)

    draw_bottom_bar(c, n, total)


# ── MAIN ───────────────────────────────────────────────────────────────────────

def main():
    slides = [
        slide_01, slide_02, slide_03, slide_04,
        slide_05, slide_06, slide_pipeline,
        slide_07, slide_08,
        slide_09, slide_10, slide_11, slide_12,
        slide_13, slide_14, slide_15, slide_16,
        slide_17,
    ]
    total = len(slides)
    cv    = canvas.Canvas(str(OUTPUT), pagesize=(W, H))
    for i, fn in enumerate(slides, 1):
        fn(cv, i, total)
        cv.showPage()
    cv.save()
    print(f'Saved: {OUTPUT}  ({total} slides)')


if __name__ == '__main__':
    main()
