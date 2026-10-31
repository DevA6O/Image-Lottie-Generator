"""
Cheetah image, drawn from scratch: slim full body from the side, with spots and tear lines.
Output: cheetah.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.big_cat_shape import BigCatLook, build_big_cat_spec, paint_big_cat_body, paint_big_cat_face

LOOK = BigCatLook(
    coat=(236, 190, 106),
    far_coat=(196, 150, 72),
    belly=(252, 236, 204),
    tail_tip=(60, 48, 46),
    ear_inner=(60, 48, 46),
    slim=True,
)
SPOT = (60, 48, 46)
SPOT_CENTERS = [(440, 490), (520, 460), (600, 500), (680, 460), (760, 500), (480, 560), (560, 580), (640, 560), (720, 590), (800, 560), (400, 540)]


def paint_spots(
    painter,
    torso_mask,
):
    for spot_center in SPOT_CENTERS:
        painter.blob(center=spot_center, radius_x=14, radius_y=14, color=SPOT, clip=torso_mask)


def paint_tear_line(painter):
    painter.body_curve(points=[(231, 440), (228, 485), (200, 505)], width=12, color=SPOT)


def render_cheetah_image():
    painter = AnimalPainter()
    spec = build_big_cat_spec(look=LOOK)
    torso_mask, _ = paint_big_cat_body(painter=painter, spec=spec, look=LOOK)
    paint_spots(painter=painter, torso_mask=torso_mask)
    paint_big_cat_face(painter=painter, spec=spec)
    paint_tear_line(painter=painter)
    painter.save_image(name="cheetah")


if __name__ == "__main__":
    render_cheetah_image()
