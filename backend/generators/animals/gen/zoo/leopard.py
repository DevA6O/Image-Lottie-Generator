"""
Leopard image, drawn from scratch: full body from the side, with rosette spots.
Output: leopard.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.big_cat_shape import BigCatLook, build_big_cat_spec, paint_big_cat_body, paint_big_cat_face

LOOK = BigCatLook(
    coat=(244, 200, 100),
    far_coat=(204, 160, 66),
    belly=(255, 240, 208),
    tail_tip=(110, 74, 44),
    ear_inner=(110, 74, 44),
)
SPOT = (110, 74, 44)
ROSETTE_CENTERS = [(450, 500), (540, 480), (630, 500), (720, 480), (490, 580), (580, 570), (670, 590), (760, 570), (400, 560)]
HEAD_SPOT_CENTERS = [(300, 400), (250, 380), (340, 440), (210, 410)]


def paint_rosettes(
    painter,
    torso_mask,
):
    """Rings made of two clipped ellipses, so no spot can leave the body."""
    for rosette_center in ROSETTE_CENTERS:
        painter.blob(center=rosette_center, radius_x=28, radius_y=28, color=SPOT, clip=torso_mask)
        painter.blob(center=rosette_center, radius_x=15, radius_y=15, color=LOOK.coat, clip=torso_mask)


def paint_head_spots(painter):
    for spot_center in HEAD_SPOT_CENTERS:
        painter.spot(center=spot_center, radius_x=9, radius_y=9, color=SPOT)


def render_leopard_image():
    painter = AnimalPainter()
    spec = build_big_cat_spec(look=LOOK)
    torso_mask, _ = paint_big_cat_body(painter=painter, spec=spec, look=LOOK)
    paint_rosettes(painter=painter, torso_mask=torso_mask)
    paint_head_spots(painter=painter)
    paint_big_cat_face(painter=painter, spec=spec)
    painter.save_image(name="leopard")


if __name__ == "__main__":
    render_leopard_image()
