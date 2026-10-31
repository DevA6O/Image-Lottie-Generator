"""
Owl image, drawn from scratch.
Output: owl.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, paint_pointed_ears
from painting.flat_painter import solid

FEATHER = (150, 104, 68)
WING = (116, 76, 50)
BELLY = (238, 212, 168)
FACE = (250, 234, 204)
IRIS = (252, 184, 48)
BEAK = (250, 150, 50)
FOOT = (250, 150, 50)
BELLY_MARK = (190, 140, 96)


def paint_feet(painter):
    for foot_x in (430, 594):
        painter.blob(center=(foot_x, 925), radius_x=64, radius_y=30, color=FOOT)


def paint_body(painter):
    paint_pointed_ears(painter=painter, center_x=512, base_y=380, spread=205, height=170, half_width=85, color=FEATHER, inner_color=WING, lean=-10)
    body_mask = painter.build_rotated_ellipse_mask(center=(512, 580), radius_x=300, radius_y=340)
    painter.fill(mask=body_mask, shade=solid(FEATHER))
    painter.fill_ellipse(center=(512, 740), radius_x=190, radius_y=190, shade=solid(BELLY), clip=body_mask)

    for mark_x, mark_y in ((440, 700), (584, 700), (512, 770), (440, 840), (584, 840)):
        painter.arc_line(center=(mark_x, mark_y), radius=34, start_angle=20, end_angle=160, width=11, color=BELLY_MARK)

    painter.blob(center=(235, 700), radius_x=70, radius_y=190, color=WING, angle=-14)
    painter.blob(center=(789, 700), radius_x=70, radius_y=190, color=WING, angle=14)


def paint_face(painter):
    painter.blob(center=(512, 480), radius_x=245, radius_y=170, color=FACE)

    for side in (-1, 1):
        eye_center = (512 + side * 115, 475)
        painter.spot(center=eye_center, radius_x=84, radius_y=84, color=(255, 255, 255))
        painter.spot(center=eye_center, radius_x=60, radius_y=60, color=IRIS)
        painter.spot(center=eye_center, radius_x=30, radius_y=30, color=EYE)
        painter.spot(center=(eye_center[0] - 12, eye_center[1] - 14), radius_x=9, radius_y=9, color=(255, 255, 255))

    painter.soft_polygon(points=[(482, 540), (542, 540), (512, 610)], color=BEAK, softness=24)


def render_owl_image():
    painter = AnimalPainter()
    paint_feet(painter)
    paint_body(painter)
    paint_face(painter)
    painter.save_image(name="owl")


if __name__ == "__main__":
    render_owl_image()
