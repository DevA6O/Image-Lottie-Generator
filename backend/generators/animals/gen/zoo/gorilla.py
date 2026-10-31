"""
Gorilla image, drawn from scratch: full body from the side, walking on its knuckles.
Output: gorilla.png (1024x1024, transparent background) in frontend/results/animals
"""
from dataclasses import replace

from animals.animal_painter import AnimalPainter
from animals.bear_shape import BearLook, build_bear_spec, paint_bear_body
from animals.face_parts import EYE
from animals.quadruped_shape import EYE_HIGHLIGHT

FUR = (88, 88, 108)
FACE = (50, 48, 60)
MUZZLE = (126, 112, 118)
LOOK = BearLook(
    coat=FUR,
    far_coat=(62, 62, 80),
    foot=(54, 54, 68),
    muzzle=MUZZLE,
    ear=FUR,
    ear_inner=FACE,
    nose=FACE,
)


def build_gorilla_spec():
    return replace(
        build_bear_spec(look=LOOK),
        body_center=(630, 520),
        body_rx=290,
        body_ry=215,
        leg_width=128,
        foot_rx=74,
        neck_base=(420, 450),
        head_center=(280, 410),
        head_rx=125,
        head_ry=110,
        snout_rx=64,
        snout_ry=44,
        snout_drop=42,
    )


def paint_face(
    painter,
    spec,
):
    head_x, head_y = spec.head_center
    painter.blob(center=(head_x - 40, head_y + 20), radius_x=88, radius_y=76, color=FACE)
    painter.blob(center=(head_x - 62, head_y + 52), radius_x=62, radius_y=42, color=MUZZLE)
    painter.blob(center=(head_x + 10, head_y - 90), radius_x=88, radius_y=50, color=(66, 66, 84))
    painter.spot(center=(head_x - 44, head_y - 4), radius_x=14, radius_y=14, color=EYE_HIGHLIGHT)
    painter.spot(center=(head_x - 44, head_y - 4), radius_x=8, radius_y=8, color=EYE)
    painter.spot(center=(head_x - 82, head_y + 40), radius_x=7, radius_y=10, color=FACE)
    painter.spot(center=(head_x - 52, head_y + 40), radius_x=7, radius_y=10, color=FACE)


def render_gorilla_image():
    painter = AnimalPainter()
    spec = build_gorilla_spec()
    paint_bear_body(painter=painter, spec=spec, look=LOOK)
    paint_face(painter=painter, spec=spec)
    painter.save_image(name="gorilla")


if __name__ == "__main__":
    render_gorilla_image()
