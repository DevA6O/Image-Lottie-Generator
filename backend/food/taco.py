"""
Taco image, drawn from scratch.
Output: taco.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

SHELL_BACK = ((226, 166, 62), (196, 124, 36))
SHELL_FRONT = ((255, 212, 98), (236, 164, 48))
LETTUCE = ((150, 214, 84), (92, 168, 56))
TOMATO = ((238, 70, 56), (190, 40, 40))
CHEESE = ((255, 222, 80), (246, 178, 36))

SHELL_BASE_Y = 760


def build_half_disc_mask(
    painter,
    radius_x,
    radius_y,
):
    disc_mask = painter.build_rotated_ellipse_mask(center=(512, SHELL_BASE_Y), radius_x=radius_x, radius_y=radius_y)
    upper_half = painter.build_box_mask(left=0, top=0, right=1024, bottom=SHELL_BASE_Y)

    return painter.intersect_masks(first_mask=disc_mask, second_mask=upper_half)


def paint_back_shell(painter):
    painter.fill(mask=build_half_disc_mask(painter=painter, radius_x=350, radius_y=400), shade=SHELL_BACK)


def paint_filling(painter):
    for x in range(230, 800, 62):
        painter.fill_circle(center=(x, 420 + abs(x - 512) * 0.25), radius=48, shade=LETTUCE)

    for x, y in [(330, 400), (470, 360), (610, 360), (730, 410)]:
        painter.fill_circle(center=(x, y + 20), radius=34, shade=TOMATO)

    for x, y in [(400, 400), (550, 380), (680, 390)]:
        painter.fill_rounded_rect(box=(x - 30, y - 18, x + 30, y + 18), radius=8, shade=CHEESE)


def paint_front_shell(painter):
    painter.fill(mask=build_half_disc_mask(painter=painter, radius_x=350, radius_y=300), shade=SHELL_FRONT)


def render_taco_image():
    painter = FoodPainter()
    paint_back_shell(painter)
    paint_filling(painter)
    paint_front_shell(painter)
    painter.save_image(name="taco")


if __name__ == "__main__":
    render_taco_image()
