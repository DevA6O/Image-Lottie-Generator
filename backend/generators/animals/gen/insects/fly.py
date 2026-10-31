"""
Fly image, drawn from scratch.
Output: fly.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from painting.flat_painter import solid

BODY = (74, 76, 92)
STRIPE = (108, 112, 132)
WING = (210, 226, 242)
EYE_RED = (226, 60, 66)
EYE_SHINE = (255, 200, 200)


def paint_wings_and_legs(painter):
    for side in (-1, 1):
        painter.blob(center=(512 + side * 215, 640), radius_x=90, radius_y=290, color=WING, angle=side * 28)

        for leg_y in (400, 480, 570):
            painter.line(points=[(512 + side * 80, leg_y), (512 + side * 200, leg_y - 30), (512 + side * 250, leg_y + 60)], width=14, color=BODY)


def paint_body(painter):
    abdomen_mask = painter.build_rotated_ellipse_mask(center=(512, 720), radius_x=135, radius_y=215)
    painter.fill(mask=abdomen_mask, shade=solid(BODY))

    for stripe_y in (680, 780):
        painter.fill_stroke(start=(380, stripe_y), end=(644, stripe_y), width=26, shade=solid(STRIPE), clip=abdomen_mask)

    painter.blob(center=(512, 470), radius_x=125, radius_y=115, color=BODY)


def paint_head(painter):
    painter.blob(center=(512, 290), radius_x=105, radius_y=90, color=BODY)

    for side in (-1, 1):
        painter.blob(center=(512 + side * 88, 280), radius_x=72, radius_y=88, color=EYE_RED, angle=side * 12)
        painter.spot(center=(512 + side * 70, 250), radius_x=16, radius_y=22, color=EYE_SHINE)


def render_fly_image():
    painter = AnimalPainter()
    paint_wings_and_legs(painter)
    paint_body(painter)
    paint_head(painter)
    painter.save_image(name="fly")


if __name__ == "__main__":
    render_fly_image()
