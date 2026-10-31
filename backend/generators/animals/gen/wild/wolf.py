"""
Wolf image, drawn from scratch: full body from the side.
Output: wolf.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_head, paint_legs, paint_neck, paint_pointed_ear, paint_tail, paint_torso

COAT = (136, 142, 156)
COAT_FAR = (104, 108, 122)
BACK = (98, 102, 116)
LIGHT = (214, 218, 228)
DARK = (62, 64, 76)

SPEC = QuadrupedSpec(
    coat=COAT,
    far_coat=COAT_FAR,
    foot=DARK,
    muzzle=LIGHT,
    nose=(40, 38, 46),
    body_center=(590, 560),
    body_rx=270,
    body_ry=135,
    leg_width=54,
    neck_base=(400, 510),
    neck_width=150,
    head_center=(250, 420),
    head_rx=115,
    head_ry=95,
    snout_rx=105,
    snout_ry=46,
)


def render_wolf_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail(painter=painter, points=[(830, 560), (940, 620), (965, 730), (925, 830)], widths=(60, 120), color=BACK)
    paint_pointed_ear(painter=painter, base=(325, 380), tip=(375, 225), width=130, color=COAT_FAR, inner_color=DARK)
    torso_mask = paint_torso(painter=painter, spec=SPEC)
    painter.blob(center=(590, 470), radius_x=270, radius_y=80, color=BACK, clip=torso_mask)
    painter.blob(center=(480, 680), radius_x=190, radius_y=60, color=LIGHT, clip=torso_mask)
    paint_neck(painter=painter, spec=SPEC)
    paint_pointed_ear(painter=painter, base=(255, 375), tip=(260, 210), width=135, color=COAT, inner_color=DARK)
    paint_head(painter=painter, spec=SPEC)
    painter.save_image(name="wolf")


if __name__ == "__main__":
    render_wolf_image()
