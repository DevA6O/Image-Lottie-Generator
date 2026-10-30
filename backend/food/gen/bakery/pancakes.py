"""
Pancake stack with butter and syrup, drawn from scratch.
Output: pancakes.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

PANCAKE = ((240, 190, 112), (206, 142, 66))
PANCAKE_EDGE = ((176, 112, 50), (176, 112, 50))
SYRUP = ((190, 100, 40), (130, 60, 22))
BUTTER = ((255, 240, 150), (248, 210, 90))

PANCAKE_TOPS = [420, 560, 700]
PANCAKE_HEIGHT = 130


def paint_pancakes(painter):
    for top in reversed(PANCAKE_TOPS):
        painter.fill_rounded_rect(box=(180, top, 844, top + PANCAKE_HEIGHT), radius=62, shade=PANCAKE_EDGE)
        painter.fill_rounded_rect(box=(180, top, 844, top + PANCAKE_HEIGHT - 14), radius=60, shade=PANCAKE)


def paint_syrup(painter):
    top_cap = painter.build_rotated_ellipse_mask(center=(512, 430), radius_x=300, radius_y=70)
    drips = [
        painter.build_rounded_rect_mask(box=(x - 34, 430, x + 34, y_end), radius=34)
        for x, y_end in [(290, 600), (470, 540), (650, 640), (760, 580)]
    ]
    syrup_mask = painter.round_corners(mask=painter.union_all(masks=[top_cap, *drips]), radius=20)
    painter.fill(mask=syrup_mask, shade=SYRUP)


def paint_butter(painter):
    painter.fill_rounded_rect(box=(430, 330, 594, 430), radius=16, shade=BUTTER)


def render_pancakes_image():
    painter = FoodPainter()
    paint_pancakes(painter)
    paint_syrup(painter)
    paint_butter(painter)
    painter.save_image(name="pancakes")


if __name__ == "__main__":
    render_pancakes_image()
