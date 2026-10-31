"""
Guinea pig image, drawn from scratch: full body from the side.
Output: guinea_pig.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_blob_ear, paint_head, paint_legs, paint_torso

COAT = (200, 140, 80)
COAT_FAR = (166, 112, 62)
PATCH = (255, 248, 238)
FOOT = (240, 188, 176)
EAR = (226, 160, 140)

SPEC = QuadrupedSpec(
    coat=COAT,
    far_coat=COAT_FAR,
    foot=FOOT,
    muzzle=PATCH,
    body_center=(590, 660),
    body_rx=330,
    body_ry=200,
    leg_width=70,
    foot_rx=48,
    foot_ry=26,
    head_center=(250, 600),
    head_rx=150,
    head_ry=130,
    snout_rx=80,
    snout_ry=62,
    snout_drop=38,
    eye_size=19,
)


def render_guinea_pig_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    torso_mask = paint_torso(painter=painter, spec=SPEC)
    painter.blob(center=(720, 600), radius_x=150, radius_y=140, color=PATCH, clip=torso_mask)
    paint_head(painter=painter, spec=SPEC)
    paint_blob_ear(painter=painter, base=(300, 500), tip=(380, 450), width=95, color=EAR)
    painter.save_image(name="guinea_pig")


if __name__ == "__main__":
    render_guinea_pig_image()
