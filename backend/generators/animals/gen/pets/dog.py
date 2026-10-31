"""
Dog image, drawn from scratch: full body from the side.
Output: dog.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_blob_ear, paint_head, paint_legs, paint_neck, paint_tail, paint_torso

COAT = (224, 170, 98)
COAT_FAR = (190, 136, 72)
EAR = (150, 98, 56)
PAW = (244, 218, 176)
TONGUE = (242, 130, 150)
COLLAR = (226, 64, 74)

SPEC = QuadrupedSpec(
    coat=COAT,
    far_coat=COAT_FAR,
    foot=PAW,
    muzzle=PAW,
    body_center=(600, 590),
    body_rx=265,
    body_ry=140,
    leg_width=64,
    head_center=(255, 430),
    head_rx=128,
    head_ry=110,
    snout_rx=92,
    snout_ry=52,
)


def paint_collar(painter):
    painter.line(points=[(355, 395), (385, 480), (380, 565)], width=30, color=COLLAR)


def render_dog_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_tail(painter=painter, points=[(820, 560), (930, 560), (950, 450), (900, 380)], widths=(60, 36), color=COAT)
    paint_torso(painter=painter, spec=SPEC)
    paint_neck(painter=painter, spec=SPEC)
    paint_collar(painter=painter)
    paint_head(painter=painter, spec=SPEC)
    painter.spot(center=(170, 520), radius_x=17, radius_y=30, color=TONGUE)
    paint_blob_ear(painter=painter, base=(300, 360), tip=(350, 570), width=110, color=EAR)
    painter.save_image(name="dog")


if __name__ == "__main__":
    render_dog_image()
