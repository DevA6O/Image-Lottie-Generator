"""
Cow image, drawn from scratch: full body from the side.
Output: cow.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_blob_ear, paint_head, paint_legs, paint_neck, paint_tail, paint_torso

COAT = (252, 250, 246)
COAT_FAR = (214, 210, 208)
PATCH = (62, 56, 62)
HOOF = (74, 62, 60)
PINK = (246, 168, 182)
HORN = (246, 228, 176)

SPEC = QuadrupedSpec(
    coat=COAT,
    far_coat=COAT_FAR,
    foot=HOOF,
    muzzle=PINK,
    nose=(206, 110, 130),
    body_center=(600, 530),
    body_rx=300,
    body_ry=170,
    leg_width=68,
    neck_base=(380, 500),
    neck_width=150,
    head_center=(225, 510),
    head_rx=125,
    head_ry=118,
    snout_rx=84,
    snout_ry=68,
    snout_drop=52,
)


def paint_tail_and_udder(painter):
    paint_tail(painter=painter, points=[(870, 480), (930, 560), (935, 680), (910, 780)], widths=(26, 16), color=COAT_FAR)
    painter.blob(center=(905, 800), radius_x=34, radius_y=56, color=PATCH, angle=10)
    painter.blob(center=(720, 705), radius_x=70, radius_y=48, color=PINK)


def paint_patches(
    painter,
    torso_mask,
):
    painter.blob(center=(500, 440), radius_x=105, radius_y=85, color=PATCH, angle=-15, clip=torso_mask)
    painter.blob(center=(760, 590), radius_x=110, radius_y=95, color=PATCH, angle=20, clip=torso_mask)


def paint_horns_and_ear(painter):
    painter.body_curve(points=[(285, 410), (295, 345), (335, 320)], width=34, color=HORN)
    paint_blob_ear(painter=painter, base=(330, 470), tip=(440, 450), width=62, color=COAT_FAR, inner_color=PINK)


def render_cow_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail_and_udder(painter=painter)
    torso_mask = paint_torso(painter=painter, spec=SPEC)
    paint_patches(painter=painter, torso_mask=torso_mask)
    paint_horns_and_ear(painter=painter)
    paint_neck(painter=painter, spec=SPEC)
    paint_head(painter=painter, spec=SPEC)
    painter.save_image(name="cow")


if __name__ == "__main__":
    render_cow_image()
