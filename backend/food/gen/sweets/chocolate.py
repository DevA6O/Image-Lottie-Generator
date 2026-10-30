"""
Chocolate bar image, drawn from scratch.
Output: chocolate.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

CHOCOLATE = ((120, 70, 44), (74, 40, 26))
SQUARE = ((150, 90, 56), (100, 56, 34))
WRAPPER = ((236, 70, 80), (180, 30, 52))
FOIL = ((236, 238, 244), (186, 192, 206))

BAR_LEFT, BAR_RIGHT = 250, 774
BAR_TOP, BAR_BOTTOM = 190, 850
COLUMNS, ROWS = 3, 5
SQUARE_GAP = 14
WRAPPER_TOP = 650


def paint_bar(painter):
    painter.fill_rounded_rect(box=(BAR_LEFT, BAR_TOP, BAR_RIGHT, BAR_BOTTOM), radius=40, shade=CHOCOLATE)
    square_width = (BAR_RIGHT - BAR_LEFT - SQUARE_GAP * (COLUMNS + 1)) / COLUMNS
    square_height = (WRAPPER_TOP - BAR_TOP - SQUARE_GAP * 2) / 3

    for row in range(3):
        for column in range(COLUMNS):
            left = BAR_LEFT + SQUARE_GAP + column * (square_width + SQUARE_GAP)
            top = BAR_TOP + SQUARE_GAP + row * (square_height + SQUARE_GAP * 0.4)
            painter.fill_rounded_rect(box=(left, top, left + square_width, top + square_height - 10), radius=14, shade=SQUARE)


def paint_wrapper(painter):
    wrapper_mask = painter.build_rounded_rect_mask(box=(BAR_LEFT - 6, WRAPPER_TOP, BAR_RIGHT + 6, BAR_BOTTOM + 6), radius=40)
    painter.fill(mask=wrapper_mask, shade=WRAPPER)
    painter.fill_polygon(points=[(BAR_LEFT - 6, WRAPPER_TOP), (BAR_RIGHT + 6, WRAPPER_TOP), (BAR_RIGHT + 6, WRAPPER_TOP + 40), (BAR_LEFT - 6, WRAPPER_TOP + 70)], shade=FOIL)


def render_chocolate_image():
    painter = FoodPainter()
    paint_bar(painter)
    paint_wrapper(painter)
    painter.save_image(name="chocolate")


if __name__ == "__main__":
    render_chocolate_image()
