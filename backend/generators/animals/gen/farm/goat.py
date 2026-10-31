"""
Goat image, drawn from scratch: full body from the side, with horns and a beard.
Output: goat.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_blob_ear, paint_head, paint_legs, paint_neck, paint_tail, paint_torso
from painting.flat_painter import build_width_profile, sample_curve, solid

COAT = (240, 228, 208)
COAT_FAR = (204, 190, 168)
HOOF = (70, 60, 60)
HORN = (150, 124, 96)

SPEC = QuadrupedSpec(
    coat=COAT,
    far_coat=COAT_FAR,
    foot=HOOF,
    muzzle=(252, 246, 236),
    body_center=(600, 560),
    body_rx=265,
    body_ry=140,
    leg_width=48,
    neck_base=(400, 500),
    neck_width=125,
    head_center=(255, 420),
    head_rx=92,
    head_ry=82,
    snout_rx=74,
    snout_ry=44,
    snout_drop=36,
)


def paint_horns(painter):
    points = sample_curve(start=(295, 360), first_control=(330, 270), second_control=(400, 240), end=(470, 270))
    widths = build_width_profile(stops=[(0.0, 40), (1.0, 12)], point_count=len(points))
    painter.fill_tapered_curve(points=points, widths=widths, shade=solid(HORN))


def paint_beard(painter):
    painter.soft_polygon(points=[(190, 490), (235, 490), (205, 585)], color=COAT_FAR, softness=24)


def render_goat_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail(painter=painter, points=[(850, 500), (890, 480), (905, 450), (895, 410)], widths=(44, 22), color=COAT)
    paint_torso(painter=painter, spec=SPEC)
    paint_neck(painter=painter, spec=SPEC)
    paint_horns(painter=painter)
    paint_head(painter=painter, spec=SPEC)
    paint_beard(painter=painter)
    paint_blob_ear(painter=painter, base=(320, 400), tip=(430, 430), width=52, color=COAT_FAR)
    painter.save_image(name="goat")


if __name__ == "__main__":
    render_goat_image()
