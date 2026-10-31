"""
Penguin image, drawn from scratch.
Output: penguin.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import solid

BLACK = (52, 56, 72)
WHITE = (250, 250, 252)
BEAK = (252, 156, 48)
FOOT = (252, 156, 48)
CHEEK = (252, 204, 90)


def paint_feet(painter):
    for foot_x in (390, 634):
        painter.blob(center=(foot_x, 905), radius_x=95, radius_y=38, color=FOOT)


def paint_body(painter):
    body_mask = painter.build_rotated_ellipse_mask(center=(512, 520), radius_x=285, radius_y=375)
    painter.blob(center=(215, 600), radius_x=62, radius_y=175, color=BLACK, angle=22)
    painter.blob(center=(809, 600), radius_x=62, radius_y=175, color=BLACK, angle=-22)
    painter.fill(mask=body_mask, shade=solid(BLACK))
    painter.fill_ellipse(center=(512, 640), radius_x=200, radius_y=290, shade=solid(WHITE), clip=body_mask)


def paint_face(painter):
    painter.spot(center=(512, 395), radius_x=165, radius_y=105, color=WHITE)

    for side in (-1, 1):
        painter.spot(center=(512 + side * 130, 400), radius_x=44, radius_y=34, color=CHEEK)
        painter.spot(center=(512 + side * 90, 360), radius_x=22, radius_y=22, color=EYE)
        painter.spot(center=(512 + side * 83, 352), radius_x=7, radius_y=7, color=(255, 255, 255))

    painter.soft_polygon(points=[(470, 400), (554, 400), (512, 480)], color=BEAK, softness=26)


def render_penguin_image():
    painter = AnimalPainter()
    paint_feet(painter)
    paint_body(painter)
    paint_face(painter)
    painter.save_image(name="penguin")


if __name__ == "__main__":
    render_penguin_image()
