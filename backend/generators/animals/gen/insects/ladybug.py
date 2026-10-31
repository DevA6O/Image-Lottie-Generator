"""
Ladybug image, drawn from scratch.
Output: ladybug.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from painting.flat_painter import solid

SHELL = (232, 54, 54)
BLACK = (50, 44, 52)
EYE_WHITE = (255, 255, 255)
SPOT_POSITIONS = ((350, 560, 52), (674, 560, 52), (330, 760, 46), (694, 760, 46), (512, 840, 38), (512, 650, 32))


def paint_legs_and_antennae(painter):
    for side in (-1, 1):
        for leg_y in (560, 680, 790):
            painter.line(points=[(512 + side * 280, leg_y), (512 + side * 380, leg_y + 30)], width=20, color=BLACK)

        painter.line(points=[(512 + side * 60, 250), (512 + side * 110, 150), (512 + side * 190, 110)], width=14, color=BLACK)


def paint_shell(painter):
    shell_mask = painter.build_rotated_ellipse_mask(center=(512, 640), radius_x=315, radius_y=335)
    painter.fill(mask=shell_mask, shade=solid(SHELL))
    painter.fill_stroke(start=(512, 330), end=(512, 960), width=14, shade=solid(BLACK), clip=shell_mask)

    for spot_x, spot_y, spot_radius in SPOT_POSITIONS:
        painter.fill_ellipse(center=(spot_x, spot_y), radius_x=spot_radius, radius_y=spot_radius, shade=solid(BLACK), clip=shell_mask)


def paint_head(painter):
    painter.blob(center=(512, 330), radius_x=170, radius_y=125, color=BLACK)

    for side in (-1, 1):
        painter.spot(center=(512 + side * 78, 300), radius_x=30, radius_y=36, color=EYE_WHITE, angle=side * 15)


def render_ladybug_image():
    painter = AnimalPainter()
    paint_legs_and_antennae(painter)
    paint_shell(painter)
    paint_head(painter)
    painter.save_image(name="ladybug")


if __name__ == "__main__":
    render_ladybug_image()
