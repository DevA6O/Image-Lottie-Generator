"""
Grape bunch image, drawn from scratch.
Output: grapes.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter, build_width_profile, sample_curve

GRAPE = ((170, 100, 210), (96, 44, 140))
SHINE = ((214, 170, 236), (200, 150, 226))
STEM = ((140, 84, 44), (100, 56, 28))
LEAF = ((130, 205, 84), (70, 150, 52))
LEAF_VEIN = ((82, 150, 56), (82, 150, 56))

GRAPE_RADIUS = 82
GRAPE_SPACING = 148
ROW_COUNTS = [4, 3, 2, 1]
ROW_SPACING = 120
FIRST_ROW_Y = 430

STEM_WIDTH = 30
LEAF_WIDTH_STOPS = [(0.0, 12), (0.35, 120), (0.75, 96), (1.0, 8)]
VEIN_WIDTH = 8


def paint_stem(painter):
    painter.fill_curve(points=[(512, 400), (516, 320), (532, 250)], width=STEM_WIDTH, shade=STEM)


def paint_leaf(painter):
    center_line = sample_curve(start=(540, 250), first_control=(600, 150), second_control=(700, 120), end=(800, 190))
    widths = build_width_profile(stops=LEAF_WIDTH_STOPS)
    leaf_mask = painter.build_tapered_curve_mask(points=center_line, widths=widths, round_ends=False)
    painter.fill(mask=leaf_mask, shade=LEAF)

    # The vein follows the middle of the leaf and is cut off at the leaf edge
    painter.fill_curve(points=center_line[8:-12], width=VEIN_WIDTH, shade=LEAF_VEIN, clip=leaf_mask)


def paint_grapes(painter):
    # Bottom row first, so the upper grapes overlap the lower ones like in a real bunch
    for row in reversed(range(len(ROW_COUNTS))):
        count = ROW_COUNTS[row]
        y = FIRST_ROW_Y + row * ROW_SPACING

        for index in range(count):
            x = 512 + (index - (count - 1) / 2) * GRAPE_SPACING
            painter.fill_circle(center=(x, y), radius=GRAPE_RADIUS, shade=GRAPE)
            painter.fill_ellipse(center=(x - 28, y - 30), radius_x=18, radius_y=9, shade=SHINE, angle=-40)


def render_grapes_image():
    painter = FoodPainter()
    paint_stem(painter)
    paint_leaf(painter)
    paint_grapes(painter)
    painter.save_image(name="grapes")


if __name__ == "__main__":
    render_grapes_image()
