"""
Whole egg image, drawn from scratch.
Output: egg.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

SHELL = ((255, 244, 224), (232, 200, 156))
SHINE = ((255, 255, 250), (255, 252, 240))
SPECKLE = ((206, 168, 124), (206, 168, 124))

SPECKLES = [(470, 600), (590, 700), (420, 740), (620, 560), (520, 790), (680, 660)]


def paint_shell(painter):
    shell_mask = painter.build_pear_mask(
        center_x=512,
        top_center_y=420,
        top_radius=170,
        bottom_center_y=600,
        bottom_radius=248,
    )
    painter.fill(mask=shell_mask, shade=SHELL)

    return shell_mask


def paint_details(
    painter,
    shell_mask,
):
    painter.fill_ellipse(center=(400, 470), radius_x=40, radius_y=100, shade=SHINE, angle=25, clip=shell_mask)

    for center in SPECKLES:
        painter.fill_circle(center=center, radius=9, shade=SPECKLE, clip=shell_mask)


def render_egg_image():
    painter = FoodPainter()
    shell_mask = paint_shell(painter)
    paint_details(painter=painter, shell_mask=shell_mask)
    painter.save_image(name="egg")


if __name__ == "__main__":
    render_egg_image()
