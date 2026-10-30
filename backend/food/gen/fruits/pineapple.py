"""
Pineapple image, drawn from scratch.
Output: pineapple.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

FRUIT = ((255, 210, 70), (232, 150, 24))
DIAMOND_LINE = ((200, 120, 20), (200, 120, 20))
LEAF = ((110, 190, 80), (50, 130, 52))
DARK_LEAF = ((70, 150, 60), (40, 110, 46))

# (x offset from the center, half length, tilt in degrees)
LEAVES = [(-120, 190, -35), (120, 190, 35), (-60, 220, -15), (60, 220, 15), (0, 250, 0)]
LINE_SPACING = 90


def paint_crown(painter):
    for offset, half_length, tilt in LEAVES[:2]:
        painter.fill_ellipse(center=(512 + offset, 270), radius_x=42, radius_y=half_length * 0.62, shade=DARK_LEAF, angle=tilt)

    for offset, half_length, tilt in LEAVES[2:]:
        painter.fill_ellipse(center=(512 + offset, 250), radius_x=44, radius_y=half_length * 0.62, shade=LEAF, angle=tilt)


def paint_fruit(painter):
    fruit_mask = painter.build_rotated_ellipse_mask(center=(512, 650), radius_x=200, radius_y=270)
    painter.fill(mask=fruit_mask, shade=FRUIT)

    for top_y in range(0, 900, LINE_SPACING):
        painter.fill_stroke(start=(312, top_y), end=(712, top_y + 400), width=10, shade=DIAMOND_LINE, clip=fruit_mask)
        painter.fill_stroke(start=(712, top_y), end=(312, top_y + 400), width=10, shade=DIAMOND_LINE, clip=fruit_mask)


def render_pineapple_image():
    painter = FoodPainter()
    paint_crown(painter)
    paint_fruit(painter)
    painter.save_image(name="pineapple")


if __name__ == "__main__":
    render_pineapple_image()
