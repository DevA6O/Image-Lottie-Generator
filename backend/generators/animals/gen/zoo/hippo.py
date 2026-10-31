"""
Hippo image, drawn from scratch: full body from the side, with the huge mouth.
Output: hippo.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from animals.quadruped_shape import EYE_HIGHLIGHT, QuadrupedSpec, paint_head, paint_legs, paint_neck, paint_tail, paint_torso

SKIN = (160, 142, 182)
SKIN_FAR = (124, 108, 146)
MUZZLE = (206, 172, 202)
NOSTRIL = (120, 84, 120)
TUSK = (255, 250, 234)

SPEC = QuadrupedSpec(
    coat=SKIN,
    far_coat=SKIN_FAR,
    foot=SKIN_FAR,
    muzzle=MUZZLE,
    nose=NOSTRIL,
    body_center=(630, 640),
    body_rx=320,
    body_ry=205,
    leg_width=112,
    foot_rx=68,
    neck_base=(430, 600),
    neck_width=280,
    head_center=(310, 590),
    head_rx=160,
    head_ry=125,
    snout_rx=140,
    snout_ry=92,
    snout_drop=72,
)


def paint_eye_bump(painter):
    painter.blob(center=(350, 475), radius_x=42, radius_y=36, color=SKIN)
    painter.spot(center=(345, 475), radius_x=14, radius_y=14, color=EYE)
    painter.spot(center=(340, 470), radius_x=5, radius_y=5, color=EYE_HIGHLIGHT)


def paint_nostrils_and_tusk(painter):
    painter.spot(center=(165, 650), radius_x=14, radius_y=10, color=NOSTRIL)
    painter.spot(center=(215, 640), radius_x=14, radius_y=10, color=NOSTRIL)
    painter.spot(center=(220, 735), radius_x=14, radius_y=22, color=TUSK)


def render_hippo_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail(painter=painter, points=[(930, 600), (970, 640), (965, 700), (940, 740)], widths=(34, 20), color=SKIN_FAR)
    paint_torso(painter=painter, spec=SPEC)
    paint_neck(painter=painter, spec=SPEC)
    painter.blob(center=(415, 470), radius_x=38, radius_y=32, color=SKIN_FAR)
    paint_head(painter=painter, spec=SPEC, face=False)
    paint_eye_bump(painter=painter)
    paint_nostrils_and_tusk(painter=painter)
    painter.save_image(name="hippo")


if __name__ == "__main__":
    render_hippo_image()
