"""
Bee image, drawn from scratch.
Output: bee.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, paint_eye_pair
from painting.flat_painter import solid

YELLOW = (254, 206, 62)
BLACK = (58, 48, 56)
WING = (206, 236, 252)
CHEEK = (250, 150, 130)


def paint_wings(painter):
    painter.blob(center=(270, 520), radius_x=105, radius_y=190, color=WING, angle=28)
    painter.blob(center=(754, 520), radius_x=105, radius_y=190, color=WING, angle=-28)


def paint_body(painter):
    painter.soft_polygon(points=[(470, 870), (554, 870), (512, 960)], color=BLACK, softness=20)
    body_mask = painter.build_rotated_ellipse_mask(center=(512, 690), radius_x=225, radius_y=245)
    painter.fill(mask=body_mask, shade=solid(YELLOW))

    for stripe_y in (680, 790):
        painter.fill_stroke(start=(250, stripe_y), end=(774, stripe_y), width=60, shade=solid(BLACK), clip=body_mask)


def paint_head(painter):
    for side in (-1, 1):
        painter.line(points=[(512 + side * 70, 250), (512 + side * 130, 150), (512 + side * 190, 120)], width=14, color=BLACK)
        painter.blob(center=(512 + side * 195, 115), radius_x=24, radius_y=24, color=BLACK)

    painter.blob(center=(512, 400), radius_x=215, radius_y=180, color=YELLOW)
    paint_eye_pair(painter=painter, center_x=512, y=390, spread=105, radius=34)

    for side in (-1, 1):
        painter.spot(center=(512 + side * 150, 470), radius_x=34, radius_y=24, color=CHEEK)

    painter.arc_line(center=(512, 450), radius=60, start_angle=35, end_angle=145, width=13, color=EYE)


def render_bee_image():
    painter = AnimalPainter()
    paint_wings(painter)
    paint_body(painter)
    paint_head(painter)
    painter.save_image(name="bee")


if __name__ == "__main__":
    render_bee_image()
