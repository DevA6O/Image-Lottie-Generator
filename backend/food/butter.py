"""
Butter block image with a cut slice, drawn from scratch.
Output: butter.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

FRONT = ((255, 226, 110), (245, 190, 60))
SIDE = ((240, 190, 70), (220, 154, 40))
TOP = ((255, 245, 190), (255, 230, 130))
HIGHLIGHT = ((255, 250, 214), (255, 238, 160))

BLOCK_TOP, BLOCK_BOTTOM = 330, 780
CORNER_RADIUS = 22

# Block as three faces: top, front and right side
TOP_POINTS = [(130, 480), (290, 330), (910, 330), (750, 480)]
FRONT_POINTS = [(130, 480), (750, 480), (750, 780), (130, 780)]
SIDE_POINTS = [(750, 480), (910, 330), (910, 630), (750, 780)]



def paint_block(painter):
    face_masks = {
        "side": painter.build_polygon_mask(points=SIDE_POINTS),
        "front": painter.build_polygon_mask(points=FRONT_POINTS),
        "top": painter.build_polygon_mask(points=TOP_POINTS),
    }
    block_mask = painter.union_masks(
        first_mask=painter.union_masks(first_mask=face_masks["side"], second_mask=face_masks["front"]),
        second_mask=face_masks["top"],
    )
    # Round the outer silhouette only, so the faces stay joined
    silhouette_mask = painter.round_corners(mask=block_mask, radius=CORNER_RADIUS)

    for face_name, shade in (("side", SIDE), ("front", FRONT), ("top", TOP)):
        visible_mask = painter.intersect_masks(first_mask=face_masks[face_name], second_mask=silhouette_mask)
        painter.fill_flat(mask=visible_mask, shade=shade)


def paint_cut_slice(painter):
    """Drawn over the block so a thin dark line shows where the knife cut."""
    cut_mask = painter.build_polygon_mask(points=[(272, 480), (432, 330), (450, 330), (290, 480)])
    painter.fill_flat(mask=cut_mask, shade=SIDE)
    cut_front_mask = painter.build_polygon_mask(points=[(272, 480), (290, 480), (290, 780), (272, 780)])
    painter.fill_flat(mask=cut_front_mask, shade=SIDE)


def paint_highlight(painter):
    highlight_mask = painter.build_stroke_mask(start=(400, 540), end=(660, 540), width=26)
    painter.fill_flat(mask=highlight_mask, shade=HIGHLIGHT)


def render_butter_image():
    painter = FoodPainter()
    paint_block(painter)
    paint_cut_slice(painter)
    paint_highlight(painter)
    painter.save_image(name="butter")


if __name__ == "__main__":
    render_butter_image()
