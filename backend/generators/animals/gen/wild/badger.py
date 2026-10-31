"""
Badger image, drawn from scratch: full body from the side, with the striped head.
Output: badger.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from animals.quadruped_shape import QuadrupedSpec, build_head_mask, paint_legs, paint_tail
from painting.flat_painter import solid

COAT = (136, 136, 148)
BACK = (170, 170, 182)
DARK = (46, 44, 52)
LEG = (84, 84, 100)
LEG_FAR = (62, 60, 74)
WHITE = (248, 246, 244)

SPEC = QuadrupedSpec(
    coat=WHITE,
    far_coat=LEG_FAR,
    foot=DARK,
    muzzle=WHITE,
    nose=DARK,
    leg_coat=LEG,
    body_center=(610, 640),
    body_rx=300,
    body_ry=170,
    leg_width=62,
    foot_rx=48,
    head_center=(270, 600),
    head_rx=130,
    head_ry=105,
    snout_rx=105,
    snout_ry=50,
    snout_drop=38,
)


def paint_head(painter):
    painter.blob(center=SPEC.head_center, radius_x=SPEC.head_rx, radius_y=SPEC.head_ry, color=WHITE)
    painter.blob(center=SPEC.snout_center, radius_x=SPEC.snout_rx, radius_y=SPEC.snout_ry, color=WHITE)
    head_mask = build_head_mask(painter=painter, spec=SPEC)
    painter.body_curve(points=[(400, 520), (240, 585), (110, 650)], width=62, color=DARK, clip=head_mask)
    painter.spot(center=SPEC.nose_center, radius_x=24, radius_y=20, color=DARK)
    painter.spot(center=(240, 585), radius_x=17, radius_y=17, color=WHITE)
    painter.spot(center=(240, 585), radius_x=9, radius_y=9, color=EYE)


def render_badger_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail(painter=painter, points=[(890, 600), (940, 620), (960, 660), (950, 710)], widths=(60, 40), color=LEG_FAR)
    torso_mask = painter.build_rotated_ellipse_mask(center=SPEC.body_center, radius_x=SPEC.body_rx, radius_y=SPEC.body_ry)
    painter.fill(mask=torso_mask, shade=solid(COAT))
    painter.blob(center=(540, 560), radius_x=220, radius_y=70, color=BACK, clip=torso_mask)
    painter.blob(center=(385, 495), radius_x=44, radius_y=44, color=DARK)
    paint_head(painter=painter)
    painter.save_image(name="badger")


if __name__ == "__main__":
    render_badger_image()
