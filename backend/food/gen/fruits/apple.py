"""
Red apple image, drawn from scratch.
Output: apple.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

APPLE = ((244, 84, 70), (184, 32, 42))
SHINE = ((255, 150, 140), (255, 130, 120))
STEM = ((140, 84, 44), (100, 56, 28))
LEAF = ((130, 205, 84), (70, 150, 52))


def paint_apple(painter):
    left_half = painter.build_rotated_ellipse_mask(center=(420, 560), radius_x=250, radius_y=270)
    right_half = painter.build_rotated_ellipse_mask(center=(604, 560), radius_x=250, radius_y=270)
    bottom = painter.build_rotated_ellipse_mask(center=(512, 620), radius_x=280, radius_y=220)
    body_mask = painter.round_corners(mask=painter.union_all(masks=[left_half, right_half, bottom]), radius=30)
    painter.fill(mask=body_mask, shade=APPLE)
    painter.fill_ellipse(center=(340, 520), radius_x=36, radius_y=100, shade=SHINE, angle=15, clip=body_mask)


def paint_stem_and_leaf(painter):
    painter.fill_curve(points=[(512, 330), (520, 280), (545, 220)], width=36, shade=STEM)
    painter.fill_ellipse(center=(650, 250), radius_x=100, radius_y=44, shade=LEAF, angle=-28)


def render_apple_image():
    painter = FoodPainter()
    paint_apple(painter)
    paint_stem_and_leaf(painter)
    painter.save_image(name="apple")


if __name__ == "__main__":
    render_apple_image()
