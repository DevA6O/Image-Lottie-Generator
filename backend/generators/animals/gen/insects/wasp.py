"""
Wasp image, drawn from scratch.
Output: wasp.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from painting.flat_painter import solid

YELLOW = (252, 214, 40)
BLACK = (50, 44, 52)
WING = (214, 234, 248)
EYE_WHITE = (255, 255, 255)


def paint_wings_and_legs(painter):
    for side in (-1, 1):
        painter.blob(center=(512 + side * 150, 420), radius_x=70, radius_y=210, color=WING, angle=side * 38)
        painter.blob(center=(512 + side * 120, 500), radius_x=50, radius_y=140, color=WING, angle=side * 62)

        for leg_y in (370, 430, 490):
            painter.line(points=[(512 + side * 70, leg_y), (512 + side * 190, leg_y - 20), (512 + side * 230, leg_y + 60)], width=14, color=BLACK)


def paint_abdomen(painter):
    abdomen_mask = painter.build_rotated_ellipse_mask(center=(512, 740), radius_x=125, radius_y=215)
    painter.soft_polygon(points=[(490, 940), (534, 940), (512, 1000)], color=BLACK, softness=14)
    painter.fill(mask=abdomen_mask, shade=solid(YELLOW))

    for band_y in (680, 770, 860):
        painter.fill_stroke(start=(380, band_y), end=(644, band_y), width=40, shade=solid(BLACK), clip=abdomen_mask)

    painter.blob(center=(512, 540), radius_x=44, radius_y=34, color=BLACK)


def paint_front(painter):
    painter.blob(center=(512, 430), radius_x=110, radius_y=100, color=BLACK)
    painter.fill_stroke(start=(440, 400), end=(584, 400), width=24, shade=solid(YELLOW))
    painter.blob(center=(512, 270), radius_x=105, radius_y=95, color=YELLOW)

    for side in (-1, 1):
        painter.line(points=[(512 + side * 40, 200), (512 + side * 110, 110), (512 + side * 100, 40)], width=12, color=BLACK)
        painter.blob(center=(512 + side * 75, 270), radius_x=40, radius_y=52, color=BLACK)
        painter.spot(center=(512 + side * 68, 252), radius_x=11, radius_y=11, color=EYE_WHITE)


def render_wasp_image():
    painter = AnimalPainter()
    paint_wings_and_legs(painter)
    paint_abdomen(painter)
    paint_front(painter)
    painter.save_image(name="wasp")


if __name__ == "__main__":
    render_wasp_image()
