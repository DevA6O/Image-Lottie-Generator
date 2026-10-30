"""
Cheese wedge image with holes, drawn from scratch.
Output: cheese.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

FRONT = ((255, 196, 48), (234, 146, 20))
TOP = ((255, 230, 120), (255, 206, 72))
FRONT_HOLE = ((220, 130, 16), (240, 160, 30))
TOP_HOLE = ((240, 176, 50), (252, 196, 64))

CORNER_RADIUS = 34

FRONT_POINTS = [(110, 540), (914, 540), (914, 800), (110, 800)]
TOP_POINTS = [(110, 540), (340, 270), (914, 540)]

# (center_x, center_y, radius_x, radius_y)
FRONT_HOLES = [
    (300, 670, 62, 52),
    (560, 700, 40, 34),
    (740, 640, 70, 56),
]
TOP_HOLES = [
    (430, 470, 40, 22),
    (640, 500, 28, 16),
]


def paint_face(
    painter,
    face_mask,
    silhouette_mask,
    shade,
):
    visible_mask = painter.intersect_masks(first_mask=face_mask, second_mask=silhouette_mask)
    painter.fill_flat(mask=visible_mask, shade=shade)

    return visible_mask


def paint_holes(
    painter,
    holes,
    face_mask,
    shade,
):
    for center_x, center_y, radius_x, radius_y in holes:
        hole_mask = painter.build_ellipse_mask(center=(center_x, center_y), radius_x=radius_x, radius_y=radius_y)
        visible_mask = painter.intersect_masks(first_mask=hole_mask, second_mask=face_mask)
        painter.fill(mask=visible_mask, shade=shade)


def render_cheese_image():
    painter = FoodPainter()

    raw_top_mask = painter.build_polygon_mask(points=TOP_POINTS)
    raw_front_mask = painter.build_polygon_mask(points=FRONT_POINTS)

    # Round the outer silhouette only, so the two faces stay joined
    silhouette_mask = painter.round_corners(
        mask=painter.union_masks(first_mask=raw_top_mask, second_mask=raw_front_mask),
        radius=CORNER_RADIUS,
    )
    top_mask = paint_face(
        painter=painter,
        face_mask=raw_top_mask,
        silhouette_mask=silhouette_mask,
        shade=TOP,
    )
    front_mask = paint_face(
        painter=painter,
        face_mask=raw_front_mask,
        silhouette_mask=silhouette_mask,
        shade=FRONT,
    )
    paint_holes(painter=painter, holes=TOP_HOLES, face_mask=top_mask, shade=TOP_HOLE)
    paint_holes(painter=painter, holes=FRONT_HOLES, face_mask=front_mask, shade=FRONT_HOLE)

    painter.save_image(name="cheese")


if __name__ == "__main__":
    render_cheese_image()
