#!/usr/bin/env python3
"""One-day news poster: Sunday, 22 November 2026.

Original Pillow artwork. No external images, no network, no randomness.
Every run writes the same 1024x1024 PNG next to this file.
"""

from __future__ import annotations

import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(HERE, "entry.png")

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (7, 17, 33)
PANEL = (13, 29, 51)
BAND = (10, 24, 43)
LAND = (24, 61, 86)
LAND_EDGE = (48, 101, 130)
OUTLINE = (36, 70, 100)
CYAN = (73, 220, 238)
GOLD = (255, 199, 92)
CORAL = (255, 112, 104)
WHITE = (245, 250, 255)
MUTED = (163, 193, 216)

DATE_TEXT = "22 NOVEMBER 2026"
SUB_TEXT = "SUNDAY · ONE DAY · SIX STORIES"
SOURCE_TEXT = "SOURCES: REUTERS · AP · AFP · ARAB NEWS"
STAMP_TEXT = "EVENTS REPORTED ON 22 NOVEMBER 2026"

STORIES = [
    {
        "n": 1,
        "kicker": "EUROPE / CLIMATE",
        "lines": ("CLIMATE TALKS", "COLLAPSE"),
        "accent": GOLD,
        "pict": "globe",
    },
    {
        "n": 2,
        "kicker": "MIDDLE EAST / CONFLICT",
        "lines": ("IRAN STRIKES", "THE GULF"),
        "accent": CORAL,
        "pict": "missile",
    },
    {
        "n": 3,
        "kicker": "AFRICA / CONFLICT",
        "lines": ("DRONE HITS", "RUSSIAN SHIP"),
        "accent": CORAL,
        "pict": "drone",
    },
    {
        "n": 4,
        "kicker": "AMERICAS / POLITICS",
        "lines": ("HOUSE COUNT", "CONFIRMED"),
        "accent": CYAN,
        "pict": "capitol",
    },
    {
        "n": 5,
        "kicker": "ASIA / EDUCATION",
        "lines": ("AI EXAM CHIEF", "QUITS"),
        "accent": GOLD,
        "pict": "exam",
    },
    {
        "n": 6,
        "kicker": "ASIA-AFRICA / DISASTER",
        "lines": ("FIRE + BOAT", "DISASTERS"),
        "accent": CORAL,
        "pict": "fireboat",
    },
]

MAP_X, MAP_Y, MAP_W, MAP_H = 60, 214, 904, 190
PINS = [
    (1, 438, 46, "EUROPE", 372, 6, GOLD),
    (2, 512, 86, "MIDDLE EAST", 528, 62, CORAL),
    (3, 470, 122, "AFRICA", 366, 150, CORAL),
    (4, 148, 58, "AMERICAS", 68, 92, CYAN),
    (5, 688, 70, "ASIA", 644, 30, GOLD),
    (6, 766, 112, "ASIA / AFRICA", 724, 140, CORAL),
]

PANEL_X = (36, 522)
PANEL_Y = (440, 608, 776)
PANEL_W, PANEL_H = 466, 164
HEADLINE_MAX_W = PANEL_W - 40
KICKER_MAX_W = PANEL_W - 58 - 82


def font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def width(draw: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont) -> float:
    return draw.textlength(text, font=f)


def fitted(
    draw: ImageDraw.ImageDraw,
    text: str,
    high: int,
    low: int,
    max_w: int,
    bold: bool = True,
) -> tuple[ImageFont.FreeTypeFont, float]:
    for size in range(high, low - 1, -1):
        f = font(size, bold)
        w = width(draw, text, f)
        if w <= max_w:
            return f, w
    f = font(low, bold)
    raise ValueError(f"text does not fit at {low}px: {text!r} ({width(draw, text, f):.1f} > {max_w})")


def ruled(draw: ImageDraw.ImageDraw, y: int, color: tuple[int, int, int], h: int = 2) -> None:
    draw.rectangle((0, y, W - 1, y + h - 1), fill=color)


def draw_header(draw: ImageDraw.ImageDraw) -> None:
    ruled(draw, 0, CYAN, 5)
    date_font, _ = fitted(draw, DATE_TEXT, 92, 84, W - 32)
    draw.text((W // 2, 78), DATE_TEXT, font=date_font, fill=WHITE, anchor="mm")
    sub_font, _ = fitted(draw, SUB_TEXT, 28, 24, W - 120)
    draw.text((W // 2, 138), SUB_TEXT, font=sub_font, fill=GOLD, anchor="mm")
    draw.rounded_rectangle((400, 166, 624, 169), radius=1, fill=CYAN)


def poly(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]]) -> None:
    pts = [(MAP_X + x, MAP_Y + y) for x, y in points]
    draw.polygon(pts, fill=LAND, outline=LAND_EDGE)
    draw.line(pts + [pts[0]], fill=LAND_EDGE, width=2, joint="curve")


def ellipse(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    draw.ellipse((MAP_X + x0, MAP_Y + y0, MAP_X + x1, MAP_Y + y1), fill=LAND, outline=LAND_EDGE, width=2)


def draw_world(draw: ImageDraw.ImageDraw) -> None:
    draw.rectangle((0, 190, W - 1, 429), fill=BAND)
    ruled(draw, 190, CYAN, 2)
    ruled(draw, 428, CYAN, 2)

    # Original, deliberately simplified world silhouette.
    poly(draw, [(18, 28), (46, 18), (58, 28), (44, 40), (22, 40)])
    poly(draw, [(40, 40), (80, 24), (132, 20), (176, 28), (206, 40), (214, 58),
                (196, 70), (180, 64), (164, 78), (150, 96), (136, 92), (122, 72),
                (96, 66), (70, 72), (48, 60)])
    poly(draw, [(238, 10), (272, 4), (292, 18), (278, 38), (250, 34)])
    poly(draw, [(150, 96), (172, 100), (186, 112), (178, 120), (160, 110)])
    poly(draw, [(196, 112), (224, 104), (250, 112), (258, 132), (248, 154),
                (232, 178), (216, 184), (208, 160), (198, 140)])
    poly(draw, [(398, 36), (430, 28), (458, 34), (470, 46), (456, 58),
                (438, 54), (424, 64), (406, 56)])
    poly(draw, [(420, 76), (458, 70), (490, 76), (506, 96), (498, 124),
                (480, 154), (458, 168), (442, 150), (430, 124), (418, 100)])
    poly(draw, [(470, 30), (520, 20), (590, 18), (660, 24), (720, 22), (790, 32),
                (838, 48), (846, 68), (818, 82), (786, 78), (760, 92), (728, 86),
                (700, 104), (676, 96), (660, 76), (628, 70), (600, 58),
                (560, 60), (530, 50), (500, 54), (482, 44)])
    poly(draw, [(660, 76), (684, 80), (692, 104), (676, 116), (664, 98)])
    ellipse(draw, (724, 104, 750, 116))
    ellipse(draw, (758, 112, 784, 122))
    ellipse(draw, (792, 104, 812, 114))
    poly(draw, [(770, 138), (810, 130), (846, 138), (856, 156), (838, 172),
                (798, 170), (776, 158)])
    ellipse(draw, (826, 66, 840, 80))

    label_font = font(21)
    for n, px, py, label, lx, ly, accent in PINS:
        cx, cy = MAP_X + px, MAP_Y + py
        draw.ellipse((cx - 15, cy - 15, cx + 15, cy + 15), fill=accent, outline=WHITE, width=2)
        draw.text((cx, cy + 1), str(n), font=font(21), fill=NAVY, anchor="mm")
        tw = width(draw, label, label_font)
        bx = max(MAP_X + 4, min(MAP_X + MAP_W - tw - 20, MAP_X + lx))
        by = MAP_Y + ly
        draw.rounded_rectangle((bx, by, bx + tw + 20, by + 29), radius=7,
                               fill=NAVY, outline=accent, width=2)
        draw.text((bx + 10, by + 14), label, font=label_font, fill=WHITE, anchor="lm")


def star(draw: ImageDraw.ImageDraw, cx: int, cy: int, r: int, color: tuple[int, int, int]) -> None:
    import math

    pts = []
    for i in range(16):
        a = -math.pi / 2 + i * math.pi / 8
        rad = r if i % 2 == 0 else r / 2
        pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    draw.polygon(pts, fill=color)


def draw_pictogram(draw: ImageDraw.ImageDraw, kind: str, ox: int, oy: int,
                   accent: tuple[int, int, int]) -> None:
    """A 60x60 original pictogram drawn from primitives at (ox, oy)."""

    def ln(points, fill, w=3):
        draw.line([(ox + x, oy + y) for x, y in points], fill=fill, width=w, joint="curve")

    if kind == "globe":
        draw.ellipse((ox + 7, oy + 7, ox + 53, oy + 53), outline=CYAN, width=3)
        draw.ellipse((ox + 25, oy + 7, ox + 35, oy + 53), outline=CYAN, width=2)
        ln([(ox + 8, oy + 30), (ox + 52, oy + 30)], CYAN, 2)
        ln([(ox + 19, oy + 10), (ox + 30, oy + 25), (ox + 21, oy + 32), (ox + 39, oy + 51)], CORAL, 4)

    elif kind == "missile":
        ln([(ox + 8, oy + 47), (ox + 24, oy + 47)], CYAN, 3)
        ln([(ox + 32, oy + 53), (ox + 52, oy + 53)], CYAN, 3)
        ln([(ox + 13, oy + 44), (ox + 40, oy + 15)], CORAL, 5)
        draw.polygon([(ox + 45, oy + 10), (ox + 34, oy + 14), (ox + 41, oy + 22)], fill=GOLD)
        star(draw, ox + 44, oy + 27, 9, CORAL)

    elif kind == "drone":
        draw.ellipse((ox + 26, oy + 14, ox + 34, oy + 22), fill=GOLD)
        for rx, ry in ((14, 6), (46, 6), (14, 26), (46, 26)):
            ln([(ox + 30, oy + 18), (ox + rx, oy + ry)], WHITE, 2)
            draw.ellipse((ox + rx - 6, oy + ry - 3, ox + rx + 6, oy + ry + 3), outline=CYAN, width=2)
        draw.polygon([(ox + 8, oy + 42), (ox + 52, oy + 42), (ox + 46, oy + 53),
                      (ox + 14, oy + 53)], fill=WHITE)
        ln([(ox + 30, oy + 42), (ox + 30, oy + 30)], WHITE, 2)
        star(draw, ox + 42, oy + 36, 8, CORAL)

    elif kind == "capitol":
        draw.polygon([(ox + 6, oy + 38), (ox + 30, oy + 22), (ox + 54, oy + 38)], fill=CYAN)
        draw.rectangle((ox + 9, oy + 39, ox + 51, oy + 50), outline=WHITE, width=2)
        for x in (16, 27, 38, 47):
            ln([(ox + x, oy + 40), (ox + x, oy + 49)], WHITE, 2)
        ln([(ox + 18, oy + 16), (ox + 26, oy + 24), (ox + 43, oy + 6)], GOLD, 5)

    elif kind == "exam":
        draw.rounded_rectangle((ox + 7, oy + 8, ox + 38, oy + 52), radius=4,
                               outline=CYAN, width=3)
        ln([(ox + 26, oy + 8), (ox + 26, oy + 17), (ox + 38, oy + 17)], CYAN, 2)
        draw.text((ox + 22, oy + 28), "AI", font=font(17), fill=GOLD, anchor="mm")
        ln([(ox + 40, oy + 34), (ox + 55, oy + 34)], CORAL, 4)
        ln([(ox + 49, oy + 28), (ox + 55, oy + 34), (ox + 49, oy + 40)], CORAL, 4)

    elif kind == "fireboat":
        draw.polygon([(ox + 16, oy + 48), (ox + 8, oy + 34), (ox + 15, oy + 29),
                      (ox + 12, oy + 16), (ox + 25, oy + 31), (ox + 23, oy + 48)], fill=CORAL)
        draw.polygon([(ox + 29, oy + 42), (ox + 54, oy + 42), (ox + 49, oy + 52),
                      (ox + 34, oy + 52)], fill=WHITE)
        ln([(ox + 28, oy + 55), (ox + 56, oy + 55)], CYAN, 3)


def draw_panels(draw: ImageDraw.ImageDraw) -> None:
    for story in STORIES:
        col = (story["n"] - 1) % 2
        row = (story["n"] - 1) // 2
        x, y = PANEL_X[col], PANEL_Y[row]
        accent = story["accent"]

        draw.rounded_rectangle((x, y, x + PANEL_W - 1, y + PANEL_H - 1), radius=12,
                               fill=PANEL, outline=OUTLINE, width=2)
        draw.rectangle((x + 2, y + 14, x + 6, y + PANEL_H - 15), fill=accent)

        cx, cy = x + 34, y + 32
        draw.ellipse((cx - 17, cy - 17, cx + 17, cy + 17), fill=accent, outline=WHITE, width=2)
        draw.text((cx, cy + 1), str(story["n"]), font=font(21), fill=NAVY, anchor="mm")

        kick_font, _ = fitted(draw, story["kicker"], 24, 20, KICKER_MAX_W)
        draw.text((x + 58, y + 32), story["kicker"], font=kick_font, fill=accent, anchor="lm")

        draw_pictogram(draw, story["pict"], x + PANEL_W - 76, y + 6, accent)

        for i, line in enumerate(story["lines"]):
            head_font, _ = fitted(draw, line, 48, 46, HEADLINE_MAX_W)
            draw.text((x + 20, y + 66 + i * 46), line, font=head_font, fill=WHITE, anchor="lt")


def draw_footer(draw: ImageDraw.ImageDraw) -> None:
    ruled(draw, 952, CYAN, 2)
    draw.text((W // 2, 979), SOURCE_TEXT, font=font(21), fill=GOLD, anchor="mm")
    draw.text((W // 2, 1005), STAMP_TEXT, font=font(20), fill=MUTED, anchor="mm")
    ruled(draw, 1022, CYAN, 2)


def verify_layout() -> None:
    """Fail early if any string would overflow its allotted area."""
    probe = ImageDraw.Draw(Image.new("RGB", (W, H)))
    checks = [
        (DATE_TEXT, W - 32, 92, 84),
        (SUB_TEXT, W - 120, 28, 24),
        (SOURCE_TEXT, W - 80, 21, 21),
        (STAMP_TEXT, W - 80, 20, 20),
    ]
    for text, max_w, high, low in checks:
        _, w = fitted(probe, text, high, low, max_w)
        assert w <= max_w, f"overflow: {text!r} {w:.1f} > {max_w}"
    for story in STORIES:
        _, kw = fitted(probe, story["kicker"], 24, 20, KICKER_MAX_W)
        assert kw <= KICKER_MAX_W, story["kicker"]
        for line in story["lines"]:
            _, lw = fitted(probe, line, 48, 46, HEADLINE_MAX_W)
            assert lw <= HEADLINE_MAX_W, line
    for _, _, _, label, _, _, _ in PINS:
        assert width(probe, label, font(21)) <= 190, label
    print(f"LAYOUT OK: 6 panels, {len(PINS)} pins, all text within bounds")


def main() -> None:
    verify_layout()
    image = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(image)
    draw_header(draw)
    draw_world(draw)
    draw_panels(draw)
    draw_footer(draw)
    image.save(OUTPUT, format="PNG", optimize=False, compress_level=9)
    print(f"WROTE {OUTPUT} ({image.width}x{image.height})")


if __name__ == "__main__":
    main()
