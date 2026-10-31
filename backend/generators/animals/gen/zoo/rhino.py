"""
Rhino image, drawn from scratch: full body from the side, with two horns.
Output: rhino.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_head, paint_legs, paint_neck, paint_pointed_ear, paint_tail, paint_torso

SKIN = (162, 166, 180)
SKIN_FAR = (124, 128, 144)
FOLD = (128, 132, 148)
HORN = (242, 228, 192)

SPEC = QuadrupedSpec(
    coat=SKIN,
    far_coat=SKIN_FAR,
    foot=SKIN_FAR,
    muzzle=(176, 180, 194),
    nose=(70, 70, 84),
    body_center=(620, 580),
    body_rx=320,
    body_ry=185,
    leg_width=104,
    foot_rx=64,
    neck_base=(420, 520),
    neck_width=230,
    head_center=(255, 540),
    head_rx=140,
    head_ry=105,
    snout_rx=120,
    snout_ry=66,
    snout_drop=55,
)


def paint_horns(painter):
    painter.soft_polygon(points=[(120, 600), (225, 590), (150, 450)], color=HORN, softness=26)
    painter.soft_polygon(points=[(225, 520), (285, 515), (260, 440)], color=HORN, softness=22)


def paint_skin_folds(painter):
    painter.arc_line(center=(520, 560), radius=110, start_angle=-60, end_angle=60, width=10, color=FOLD)
    painter.arc_line(center=(790, 580), radius=100, start_angle=-110, end_angle=-30, width=10, color=FOLD)


def render_rhino_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail(painter=painter, points=[(920, 540), (960, 600), (960, 680), (940, 740)], widths=(30, 16), color=SKIN_FAR)
    paint_torso(painter=painter, spec=SPEC)
    paint_skin_folds(painter=painter)
    paint_neck(painter=painter, spec=SPEC)
    paint_pointed_ear(painter=painter, base=(345, 460), tip=(395, 360), width=70, color=SKIN_FAR)
    paint_head(painter=painter, spec=SPEC)
    paint_horns(painter=painter)
    painter.save_image(name="rhino")


if __name__ == "__main__":
    render_rhino_image()
