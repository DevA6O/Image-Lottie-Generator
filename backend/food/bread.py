"""
Bread loaf image, drawn from scratch.
Output: bread.png (1024x1024, transparent background) in frontend/results/food
"""
from layer_painter import OUT_DIR, LayerPainter

CRUST_COLORS = [(0.0, (150, 80, 30)), (1.0, (196, 112, 44))]
SHADOW_COLORS = [(0.0, (120, 60, 24)), (1.0, (150, 80, 30))]
TOP_COLORS = [(0.0, (240, 176, 84)), (1.0, (214, 136, 56))]
SLASH_COLORS = [(0.0, (255, 232, 176)), (1.0, (250, 206, 128))]

LOAF_TOP, LOAF_BOTTOM = 270, 790
UNDERSIDE_TOP = 715
DOME_BASE_Y = 540
BASE_CORNER_RADIUS = 70

SLASH_WIDTH = 44
SLASH_LINES = [
    ((330, 420), (395, 560)),
    ((470, 385), (535, 525)),
    ((610, 420), (675, 560)),
]


def build_loaf_mask(
    painter,
    inset,
):
    """A dome on top of a flat base. inset shrinks the shape evenly on all sides."""
    full_ellipse_mask = painter.build_ellipse_mask(
        center=(512, DOME_BASE_Y),
        radius_x=402 - inset,
        radius_y=270 - inset,
    )
    upper_half_mask = painter.build_polygon_mask(points=[(0, 0), (1024, 0), (1024, DOME_BASE_Y), (0, DOME_BASE_Y)])
    dome_mask = painter.intersect_masks(first_mask=full_ellipse_mask, second_mask=upper_half_mask)
    base_mask = painter.build_polygon_mask(
        points=[
            (110 + inset, DOME_BASE_Y),
            (914 - inset, DOME_BASE_Y),
            (914 - inset, LOAF_BOTTOM - inset),
            (110 + inset, LOAF_BOTTOM - inset),
        ],
    )
    loaf_mask = painter.union_masks(first_mask=dome_mask, second_mask=base_mask)

    return painter.round_corners(mask=loaf_mask, radius=BASE_CORNER_RADIUS - inset)


def paint_loaf_body(painter):
    loaf_mask = build_loaf_mask(painter=painter, inset=0)
    painter.paint(mask=loaf_mask, color_stops=CRUST_COLORS, top=LOAF_TOP, bottom=LOAF_BOTTOM)

    # Darker rim at the bottom, like the baked underside
    underside_mask = painter.intersect_masks(
        first_mask=loaf_mask,
        second_mask=painter.build_polygon_mask(points=[(0, UNDERSIDE_TOP), (1024, UNDERSIDE_TOP), (1024, 1024), (0, 1024)]),
    )
    painter.paint(mask=underside_mask, color_stops=SHADOW_COLORS, top=UNDERSIDE_TOP, bottom=LOAF_BOTTOM)


def paint_loaf_top(painter):
    top_mask = build_loaf_mask(painter=painter, inset=38)
    top_mask = painter.intersect_masks(
        first_mask=top_mask,
        second_mask=painter.build_polygon_mask(points=[(0, 0), (1024, 0), (1024, UNDERSIDE_TOP - 10), (0, UNDERSIDE_TOP - 10)]),
    )
    painter.paint(mask=top_mask, color_stops=TOP_COLORS, top=LOAF_TOP, bottom=UNDERSIDE_TOP)


def paint_slashes(painter):
    for start, end in SLASH_LINES:
        slash_mask = painter.build_stroke_mask(start=start, end=end, width=SLASH_WIDTH)
        painter.paint(mask=slash_mask, color_stops=SLASH_COLORS, top=385, bottom=560)


def render_bread_image():
    painter = LayerPainter()
    paint_loaf_body(painter)
    paint_loaf_top(painter)
    paint_slashes(painter)
    painter.save(out_file=OUT_DIR / "bread.png")


if __name__ == "__main__":
    render_bread_image()
