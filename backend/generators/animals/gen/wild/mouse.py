"""
Mouse image, drawn from scratch: full body from the side, with the long tail.
Output: mouse.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_head, paint_legs, paint_tail, paint_torso

COAT = (178, 180, 194)
COAT_FAR = (140, 142, 158)
BELLY = (234, 234, 242)
PINK = (248, 176, 190)

SPEC = QuadrupedSpec(
    coat=COAT,
    far_coat=COAT_FAR,
    foot=PINK,
    muzzle=BELLY,
    nose=PINK,
    body_center=(580, 660),
    body_rx=280,
    body_ry=180,
    leg_width=56,
    foot_rx=44,
    head_center=(300, 600),
    head_rx=130,
    head_ry=108,
    snout_rx=110,
    snout_ry=52,
    snout_drop=40,
)


def render_mouse_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail(painter=painter, points=[(830, 730), (960, 760), (990, 600), (900, 500)], widths=(30, 14), color=PINK)
    paint_torso(painter=painter, spec=SPEC)
    painter.blob(center=(520, 760), radius_x=190, radius_y=70, color=BELLY)
    paint_head(painter=painter, spec=SPEC)
    painter.blob(center=(360, 470), radius_x=95, radius_y=100, color=COAT_FAR)
    painter.spot(center=(360, 475), radius_x=60, radius_y=65, color=PINK)
    painter.save_image(name="mouse")


if __name__ == "__main__":
    render_mouse_image()
