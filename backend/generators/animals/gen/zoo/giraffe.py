"""
Giraffe image, drawn from scratch: full body from the side, with the long neck and spots.
Output: giraffe.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_blob_ear, paint_face, paint_head, paint_legs, paint_tail, paint_torso
from painting.flat_painter import build_width_profile, solid

COAT = (252, 208, 98)
COAT_FAR = (216, 168, 62)
SPOT = (186, 112, 54)
HOOF = (96, 66, 48)
HORN_TIP = (122, 76, 48)

SPEC = QuadrupedSpec(
    coat=COAT,
    far_coat=COAT_FAR,
    foot=HOOF,
    muzzle=(252, 228, 184),
    nose=HOOF,
    body_center=(650, 600),
    body_rx=240,
    body_ry=118,
    leg_width=44,
    foot_rx=32,
    foot_ry=20,
    head_center=(290, 220),
    head_rx=88,
    head_ry=64,
    snout_rx=76,
    snout_ry=42,
    snout_drop=28,
)
NECK_POINTS = [(520, 540), (410, 380), (310, 240)]
BODY_SPOTS = [(580, 560, 40), (680, 520, 46), (770, 590, 38), (610, 650, 34), (720, 650, 32)]
NECK_SPOTS = [(470, 470, 30), (415, 380, 28), (370, 300, 24), (445, 540, 26)]


def paint_neck_and_spots(painter):
    widths = build_width_profile(stops=[(0.0, 150), (1.0, 76)], point_count=3)
    neck_mask = painter.build_tapered_curve_mask(points=NECK_POINTS, widths=widths)
    painter.fill(mask=neck_mask, shade=solid(COAT))

    return neck_mask


def paint_spots(
    painter,
    torso_mask,
    neck_mask,
):
    for x, y, radius in BODY_SPOTS:
        painter.blob(center=(x, y), radius_x=radius, radius_y=radius * 0.85, color=SPOT, clip=torso_mask)

    for x, y, radius in NECK_SPOTS:
        painter.blob(center=(x, y), radius_x=radius, radius_y=radius * 0.85, color=SPOT, clip=neck_mask)


def paint_horns(painter):
    for base_x, tip_x in ((325, 340), (270, 262)):
        painter.line(points=[(base_x, 170), (tip_x, 100)], width=16, color=COAT_FAR)
        painter.blob(center=(tip_x, 92), radius_x=18, radius_y=18, color=HORN_TIP)


def render_giraffe_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail(painter=painter, points=[(880, 540), (920, 620), (925, 700), (910, 780)], widths=(24, 14), color=COAT_FAR)
    painter.blob(center=(908, 795), radius_x=22, radius_y=38, color=HORN_TIP)
    paint_horns(painter=painter)
    neck_mask = paint_neck_and_spots(painter=painter)
    torso_mask = paint_torso(painter=painter, spec=SPEC)
    paint_spots(painter=painter, torso_mask=torso_mask, neck_mask=neck_mask)
    paint_head(painter=painter, spec=SPEC, face=False)
    paint_face(painter=painter, spec=SPEC)
    paint_blob_ear(painter=painter, base=(345, 205), tip=(425, 185), width=44, color=COAT_FAR)
    painter.save_image(name="giraffe")


if __name__ == "__main__":
    render_giraffe_image()
