"""
Lemon image, drawn from scratch.
Output: lemon.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

LEMON = ((255, 244, 100), (236, 196, 36))
SHINE = ((255, 252, 190), (255, 250, 170))
LEAF = ((130, 205, 84), (70, 150, 52))

TILT_DEGREES = -22


def paint_lemon(painter):
    body_mask = painter.build_rotated_ellipse_mask(center=(512, 560), radius_x=330, radius_y=235, angle=TILT_DEGREES)
    left_tip = painter.build_rotated_ellipse_mask(center=(190, 700), radius_x=60, radius_y=42, angle=TILT_DEGREES)
    right_tip = painter.build_rotated_ellipse_mask(center=(834, 420), radius_x=60, radius_y=42, angle=TILT_DEGREES)
    outline = painter.union_all(masks=[body_mask, left_tip, right_tip])
    lemon_mask = painter.round_corners(mask=outline, radius=24)
    painter.fill(mask=lemon_mask, shade=LEMON)
    painter.fill_ellipse(center=(420, 480), radius_x=90, radius_y=30, shade=SHINE, angle=TILT_DEGREES, clip=lemon_mask)


def paint_leaf(painter):
    painter.fill_ellipse(center=(740, 290), radius_x=120, radius_y=44, shade=LEAF, angle=-30)


def render_lemon_image():
    painter = FoodPainter()
    paint_leaf(painter)
    paint_lemon(painter)
    painter.save_image(name="lemon")


if __name__ == "__main__":
    render_lemon_image()
