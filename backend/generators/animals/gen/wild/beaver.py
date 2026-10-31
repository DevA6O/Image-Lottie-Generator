"""
Beaver image, drawn from scratch: full body from the side, with the flat tail.
Output: beaver.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_head, paint_legs, paint_torso
from painting.flat_painter import solid

COAT = (146, 96, 58)
COAT_FAR = (112, 72, 44)
BELLY = (206, 156, 106)
TAIL = (84, 62, 56)
TAIL_LINE = (60, 44, 42)
TOOTH = (255, 250, 232)

SPEC = QuadrupedSpec(
    coat=COAT,
    far_coat=COAT_FAR,
    foot=COAT_FAR,
    muzzle=BELLY,
    body_center=(590, 630),
    body_rx=290,
    body_ry=190,
    leg_width=64,
    foot_rx=50,
    head_center=(260, 590),
    head_rx=130,
    head_ry=112,
    snout_rx=75,
    snout_ry=58,
    snout_drop=40,
)


def paint_flat_tail(painter):
    tail_mask = painter.build_rotated_ellipse_mask(center=(880, 780), radius_x=140, radius_y=70, angle=-25)
    painter.fill(mask=tail_mask, shade=solid(TAIL))

    for shift in (-60, 0, 60):
        painter.body_curve(points=[(800 + shift, 700), (840 + shift, 780), (800 + shift, 860)], width=10, color=TAIL_LINE, clip=tail_mask)


def render_beaver_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_flat_tail(painter=painter)
    paint_torso(painter=painter, spec=SPEC)
    painter.blob(center=(470, 730), radius_x=170, radius_y=80, color=BELLY)
    paint_head(painter=painter, spec=SPEC)
    painter.spot(center=(195, 665), radius_x=26, radius_y=34, color=TOOTH)
    painter.blob(center=(335, 495), radius_x=42, radius_y=42, color=COAT_FAR)
    painter.save_image(name="beaver")


if __name__ == "__main__":
    render_beaver_image()
