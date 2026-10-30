"""
Corn cob with husk, drawn from scratch.
Output: corn.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

COB = ((255, 224, 80), (240, 170, 24))
KERNEL_LINE = ((214, 148, 20), (214, 148, 20))
HUSK = ((140, 205, 90), (80, 150, 56))
HUSK_DARK = ((100, 176, 70), (60, 128, 48))

TILT_DEGREES = -45
LINE_SPACING = 56


def paint_husk(painter):
    painter.fill_ellipse(center=(340, 720), radius_x=300, radius_y=84, shade=HUSK_DARK, angle=TILT_DEGREES - 18)
    painter.fill_ellipse(center=(320, 720), radius_x=300, radius_y=84, shade=HUSK, angle=TILT_DEGREES + 20)


def paint_cob(painter):
    cob_mask = painter.build_rotated_ellipse_mask(center=(580, 450), radius_x=350, radius_y=160, angle=TILT_DEGREES)
    painter.fill(mask=cob_mask, shade=COB)

    for offset in range(-600, 600, LINE_SPACING):
        painter.fill_stroke(start=(100, 700 + offset), end=(900, offset - 100), width=9, shade=KERNEL_LINE, clip=cob_mask)
        painter.fill_stroke(start=(100, 100 - offset), end=(900, 900 - offset), width=9, shade=KERNEL_LINE, clip=cob_mask)


def render_corn_image():
    painter = FoodPainter()
    paint_cob(painter)
    paint_husk(painter)
    painter.save_image(name="corn")


if __name__ == "__main__":
    render_corn_image()
