"""
Cat image, drawn from scratch: full body from the side.
Output: cat.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_head, paint_legs, paint_neck, paint_pointed_ear, paint_tail, paint_torso

COAT = (238, 160, 82)
COAT_FAR = (200, 124, 56)
STRIPE = (190, 108, 44)
CREAM = (255, 238, 212)
EAR_INNER = (246, 150, 166)
WHISKER = (255, 244, 230)

SPEC = QuadrupedSpec(
    coat=COAT,
    far_coat=COAT_FAR,
    foot=CREAM,
    muzzle=CREAM,
    body_center=(590, 600),
    body_rx=250,
    body_ry=118,
    leg_width=50,
    foot_rx=38,
    neck_base=(390, 540),
    neck_width=140,
    head_center=(265, 450),
    head_rx=112,
    head_ry=98,
    snout_rx=58,
    snout_ry=40,
    snout_drop=32,
    eye_size=17,
)


def paint_stripes(painter, torso_mask):
    for stripe_x in (500, 590, 680, 770):
        painter.body_curve(points=[(stripe_x, 470), (stripe_x - 20, 540), (stripe_x, 610)], width=20, color=STRIPE, clip=torso_mask)


def paint_whiskers(painter):
    for tilt in (-22, 0, 22):
        painter.line(points=[(215, 505 + tilt * 0.4), (140, 505 + tilt)], width=6, color=WHISKER)


def render_cat_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail(painter=painter, points=[(810, 600), (950, 620), (990, 440), (900, 330)], widths=(52, 38), color=COAT)
    paint_pointed_ear(painter=painter, base=(320, 390), tip=(350, 240), width=115, color=COAT_FAR, inner_color=EAR_INNER)
    torso_mask = paint_torso(painter=painter, spec=SPEC)
    paint_stripes(painter=painter, torso_mask=torso_mask)
    paint_neck(painter=painter, spec=SPEC)
    paint_pointed_ear(painter=painter, base=(250, 385), tip=(240, 225), width=125, color=COAT, inner_color=EAR_INNER)
    paint_head(painter=painter, spec=SPEC)
    paint_whiskers(painter=painter)
    painter.save_image(name="cat")


if __name__ == "__main__":
    render_cat_image()
