"""
Baguette image, drawn from scratch.
Output: baguette.png (1024x1024, transparent background) in frontend/results/food
"""
import math

from food_painter import FoodPainter

CRUST = ((232, 170, 80), (196, 124, 46))
UNDERSIDE = ((150, 88, 34), (150, 88, 34))
SLASH = ((255, 232, 176), (248, 204, 126))

START = (230, 770)
END = (800, 260)
WIDTH = 160
UNDERSIDE_OFFSET = 18
SLASH_POSITIONS = [0.2, 0.4, 0.6, 0.8]
SLASH_HALF_LENGTH = 38
SLASH_SLANT = 22


def paint_loaf(painter):
    underside_start = (START[0], START[1] + UNDERSIDE_OFFSET)
    underside_end = (END[0], END[1] + UNDERSIDE_OFFSET)
    painter.fill_stroke(start=underside_start, end=underside_end, width=WIDTH, shade=UNDERSIDE)
    painter.fill_stroke(start=START, end=END, width=WIDTH, shade=CRUST)


def paint_slashes(painter):
    axis_length = math.dist(START, END)
    axis = ((END[0] - START[0]) / axis_length, (END[1] - START[1]) / axis_length)
    across = (-axis[1], axis[0])

    for position in SLASH_POSITIONS:
        center = (START[0] + (END[0] - START[0]) * position, START[1] + (END[1] - START[1]) * position)
        slash_start = (
            center[0] - across[0] * SLASH_HALF_LENGTH - axis[0] * SLASH_SLANT,
            center[1] - across[1] * SLASH_HALF_LENGTH - axis[1] * SLASH_SLANT,
        )
        slash_end = (
            center[0] + across[0] * SLASH_HALF_LENGTH + axis[0] * SLASH_SLANT,
            center[1] + across[1] * SLASH_HALF_LENGTH + axis[1] * SLASH_SLANT,
        )
        painter.fill_stroke(start=slash_start, end=slash_end, width=30, shade=SLASH)


def render_baguette_image():
    painter = FoodPainter()
    paint_loaf(painter)
    paint_slashes(painter)
    painter.save_image(name="baguette")


if __name__ == "__main__":
    render_baguette_image()
