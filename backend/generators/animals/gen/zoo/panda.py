"""
Panda image, drawn from scratch: full body from the side, with black legs, shoulder band and eye patch.
Output: panda.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bear_shape import BearLook, build_bear_spec, paint_bear_body
from animals.face_parts import EYE
from animals.quadruped_shape import EYE_HIGHLIGHT, paint_face

BLACK = (46, 42, 50)
LOOK = BearLook(
    coat=(252, 252, 250),
    far_coat=(30, 28, 34),
    foot=BLACK,
    muzzle=(238, 236, 236),
    ear=BLACK,
    ear_inner=BLACK,
    nose=BLACK,
    leg_coat=BLACK,
)


def paint_shoulder_band(
    painter,
    torso_mask,
):
    painter.body_curve(points=[(440, 380), (450, 560), (440, 720)], width=120, color=BLACK, clip=torso_mask)


def paint_eye_patch(
    painter,
    spec,
):
    eye_x = spec.head_center[0] - spec.head_rx * 0.3
    eye_y = spec.head_center[1] - spec.head_ry * 0.2
    painter.spot(center=(eye_x + 8, eye_y + 4), radius_x=34, radius_y=46, color=BLACK, angle=25)
    painter.spot(center=(eye_x, eye_y), radius_x=15, radius_y=15, color=EYE_HIGHLIGHT)
    painter.spot(center=(eye_x, eye_y), radius_x=8, radius_y=8, color=EYE)


def render_panda_image():
    painter = AnimalPainter()
    spec = build_bear_spec(look=LOOK)
    torso_mask, _ = paint_bear_body(painter=painter, spec=spec, look=LOOK)
    paint_shoulder_band(painter=painter, torso_mask=torso_mask)
    paint_face(painter=painter, spec=spec)
    paint_eye_patch(painter=painter, spec=spec)
    painter.save_image(name="panda")


if __name__ == "__main__":
    render_panda_image()
