"""
Fox image, drawn from scratch: full body from the side.
Output: fox.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_head, paint_legs, paint_neck, paint_pointed_ear, paint_tail, paint_torso

FUR = (238, 124, 48)
FUR_FAR = (196, 98, 36)
SOCK = (70, 52, 52)
WHITE = (255, 248, 238)

SPEC = QuadrupedSpec(
    coat=FUR,
    far_coat=FUR_FAR,
    foot=SOCK,
    muzzle=FUR,
    body_center=(570, 570),
    body_rx=250,
    body_ry=125,
    leg_width=58,
    foot_rx=40,
    foot_ry=22,
    neck_base=(380, 540),
    neck_width=130,
    head_center=(265, 440),
    head_rx=122,
    head_ry=100,
    snout_rx=115,
    snout_ry=46,
    snout_drop=30,
)


def paint_tail_and_ears(painter):
    paint_tail(painter=painter, points=[(790, 570), (930, 650), (965, 480), (905, 330)], widths=(60, 190), color=FUR)
    painter.blob(center=(915, 345), radius_x=58, radius_y=72, color=WHITE, angle=-20)
    paint_pointed_ear(painter=painter, base=(310, 380), tip=(355, 200), width=150, color=FUR_FAR, inner_color=SOCK)
    paint_pointed_ear(painter=painter, base=(250, 370), tip=(250, 185), width=160, color=FUR, inner_color=SOCK)


def render_fox_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail_and_ears(painter=painter)
    paint_torso(painter=painter, spec=SPEC)
    paint_neck(painter=painter, spec=SPEC)
    paint_head(painter=painter, spec=SPEC)
    painter.spot(center=(200, 490), radius_x=100, radius_y=26, color=WHITE, angle=8)
    painter.save_image(name="fox")


if __name__ == "__main__":
    render_fox_image()
