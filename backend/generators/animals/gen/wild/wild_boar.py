"""
Wild boar image, drawn from scratch: full body from the side, with bristles and a tusk.
Output: wild_boar.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from animals.quadruped_shape import EYE_HIGHLIGHT, QuadrupedSpec, paint_legs, paint_pointed_ear, paint_tail, paint_torso

COAT = (116, 92, 82)
COAT_FAR = (84, 64, 58)
BRISTLE = (58, 46, 46)
SNOUT = (160, 126, 112)
TUSK = (250, 238, 206)
HOOF = (50, 40, 40)

SPEC = QuadrupedSpec(
    coat=COAT,
    far_coat=COAT_FAR,
    foot=HOOF,
    muzzle=SNOUT,
    body_center=(620, 590),
    body_rx=310,
    body_ry=175,
    leg_width=48,
    foot_rx=34,
)


def paint_bristles(painter):
    for spike_x in range(400, 900, 55):
        relative_x = (spike_x - SPEC.body_center[0]) / SPEC.body_rx
        back_y = SPEC.body_center[1] - SPEC.body_ry * (1 - relative_x**2) ** 0.5
        spike = [(spike_x - 32, back_y + 25), (spike_x + 8, back_y - 62), (spike_x + 36, back_y + 25)]
        painter.soft_polygon(points=spike, color=BRISTLE, softness=18)


def paint_head(painter):
    painter.blob(center=(310, 600), radius_x=150, radius_y=125, color=COAT)
    painter.blob(center=(185, 650), radius_x=118, radius_y=62, color=SNOUT, angle=-12)
    painter.blob(center=(105, 640), radius_x=22, radius_y=32, color=BRISTLE)
    painter.body_curve(points=[(215, 690), (175, 660), (170, 620)], width=22, color=TUSK)
    painter.spot(center=(290, 560), radius_x=15, radius_y=15, color=EYE)
    painter.spot(center=(285, 554), radius_x=5, radius_y=5, color=EYE_HIGHLIGHT)


def render_wild_boar_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail(painter=painter, points=[(920, 560), (960, 580), (965, 640), (940, 690)], widths=(30, 14), color=COAT_FAR)
    paint_torso(painter=painter, spec=SPEC)
    painter.blob(center=(470, 520), radius_x=170, radius_y=140, color=COAT)
    paint_bristles(painter=painter)
    paint_pointed_ear(painter=painter, base=(340, 500), tip=(400, 390), width=95, color=COAT_FAR)
    paint_head(painter=painter)
    painter.save_image(name="wild_boar")


if __name__ == "__main__":
    render_wild_boar_image()
