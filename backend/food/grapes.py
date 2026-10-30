"""
Grape bunch image, drawn from scratch.
Output: grapes.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

GRAPE = ((170, 100, 210), (96, 44, 140))
SHINE = ((214, 170, 236), (200, 150, 226))
STEM = ((130, 90, 50), (96, 62, 34))
LEAF = ((130, 205, 84), (70, 150, 52))

GRAPE_RADIUS = 78
ROW_COUNTS = [4, 3, 2, 1]
ROW_SPACING = 135
FIRST_ROW_Y = 400


def paint_stem_and_leaf(painter):
    painter.fill_curve(points=[(512, 300), (520, 250), (560, 190)], width=30, shade=STEM)
    painter.fill_ellipse(center=(690, 250), radius_x=130, radius_y=56, shade=LEAF, angle=-22)


def paint_grapes(painter):
    for row, count in enumerate(ROW_COUNTS):
        y = FIRST_ROW_Y + row * ROW_SPACING

        for index in range(count):
            x = 512 + (index - (count - 1) / 2) * GRAPE_RADIUS * 2
            painter.fill_circle(center=(x, y), radius=GRAPE_RADIUS, shade=GRAPE)
            painter.fill_ellipse(center=(x - 28, y - 28), radius_x=18, radius_y=9, shade=SHINE, angle=-40)


def render_grapes_image():
    painter = FoodPainter()
    paint_stem_and_leaf(painter)
    paint_grapes(painter)
    painter.save_image(name="grapes")


if __name__ == "__main__":
    render_grapes_image()
