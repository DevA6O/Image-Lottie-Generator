"""
Coffee cup with steam, drawn from scratch.
Output: coffee.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter
from painting.flat_painter import sample_curve

CUP = ((255, 255, 255), (216, 222, 234))
SAUCER = ((236, 240, 248), (190, 198, 214))
COFFEE = ((130, 76, 44), (84, 44, 26))
STEAM = ((220, 224, 234), (196, 202, 216))

STEAM_X_POSITIONS = [410, 512, 614]


def paint_saucer(painter):
    painter.fill_ellipse(center=(512, 810), radius_x=360, radius_y=70, shade=SAUCER)


def paint_handle(painter):
    handle_points = sample_curve(start=(720, 540), first_control=(900, 520), second_control=(900, 760), end=(700, 740))
    painter.fill_curve(points=handle_points, width=50, shade=CUP)


def paint_cup(painter):
    cup_mask = painter.round_corners(
        mask=painter.build_polygon_mask(points=[(290, 480), (734, 480), (680, 800), (344, 800)]),
        radius=60,
    )
    painter.fill(mask=cup_mask, shade=CUP)
    painter.fill_ellipse(center=(512, 480), radius_x=222, radius_y=44, shade=CUP)
    painter.fill_ellipse(center=(512, 484), radius_x=190, radius_y=30, shade=COFFEE)


def paint_steam(painter):
    for x in STEAM_X_POSITIONS:
        wave = sample_curve(start=(x, 410), first_control=(x - 70, 340), second_control=(x + 70, 260), end=(x, 180))
        painter.fill_curve(points=wave, width=28, shade=STEAM)


def render_coffee_image():
    painter = FoodPainter()
    paint_saucer(painter)
    paint_handle(painter)
    paint_cup(painter)
    paint_steam(painter)
    painter.save_image(name="coffee")


if __name__ == "__main__":
    render_coffee_image()
