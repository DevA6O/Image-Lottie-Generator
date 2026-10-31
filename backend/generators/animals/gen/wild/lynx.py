"""
Lynx image, drawn from scratch: full body from the side, with ear tufts and a cheek ruff.
Output: lynx.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_head, paint_legs, paint_neck, paint_pointed_ear, paint_tail, paint_torso

COAT = (208, 164, 102)
COAT_FAR = (172, 128, 78)
CREAM = (248, 232, 200)
SPOT = (140, 98, 58)
TUFT = (50, 42, 44)
EAR_INNER = (236, 160, 160)

SPEC = QuadrupedSpec(
    coat=COAT,
    far_coat=COAT_FAR,
    foot=CREAM,
    muzzle=CREAM,
    body_center=(600, 590),
    body_rx=255,
    body_ry=125,
    leg_width=60,
    foot_rx=46,
    neck_base=(400, 540),
    neck_width=150,
    head_center=(265, 450),
    head_rx=115,
    head_ry=100,
    snout_rx=60,
    snout_ry=42,
    snout_drop=34,
    eye_size=17,
)
SPOT_CENTERS = [(480, 520), (560, 590), (640, 520), (720, 600), (780, 520), (850, 590), (520, 650)]


def paint_ear_with_tuft(
    painter,
    base,
    tip,
    color,
):
    paint_pointed_ear(painter=painter, base=base, tip=tip, width=115, color=color, inner_color=EAR_INNER)
    painter.line(points=[tip, (tip[0] + 2, tip[1] - 65)], width=14, color=TUFT)


def render_lynx_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail(painter=painter, points=[(830, 580), (880, 590), (900, 620), (905, 660)], widths=(60, 50), color=COAT_FAR)
    painter.blob(center=(902, 670), radius_x=30, radius_y=36, color=TUFT)
    paint_ear_with_tuft(painter=painter, base=(330, 390), tip=(375, 225), color=COAT_FAR)
    torso_mask = paint_torso(painter=painter, spec=SPEC)

    for spot_center in SPOT_CENTERS:
        painter.spot(center=spot_center, radius_x=18, radius_y=18, color=SPOT)

    paint_neck(painter=painter, spec=SPEC)
    paint_ear_with_tuft(painter=painter, base=(255, 385), tip=(245, 215), color=COAT)
    paint_head(painter=painter, spec=SPEC)
    painter.spot(center=(290, 560), radius_x=80, radius_y=46, color=CREAM, angle=25)
    painter.save_image(name="lynx")


if __name__ == "__main__":
    render_lynx_image()
