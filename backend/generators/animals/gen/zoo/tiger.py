"""
Tiger image, drawn from scratch: full body from the side, with stripes.
Output: tiger.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.big_cat_shape import BigCatLook, build_big_cat_spec, paint_big_cat_body, paint_big_cat_face

LOOK = BigCatLook(
    coat=(248, 150, 52),
    far_coat=(206, 112, 30),
    belly=(255, 244, 226),
    tail_tip=(52, 44, 48),
    ear_inner=(52, 44, 48),
)
STRIPE = (52, 44, 48)


def paint_body_stripes(
    painter,
    torso_mask,
):
    for stripe_x in range(400, 880, 60):
        painter.body_curve(points=[(stripe_x, 400), (stripe_x - 25, 500), (stripe_x + 5, 600)], width=24, color=STRIPE, clip=torso_mask)


def paint_head_stripes(
    painter,
    head_mask,
):
    for stripe_x in (235, 275, 315):
        painter.body_curve(points=[(stripe_x, 350), (stripe_x + 4, 380), (stripe_x, 405)], width=13, color=STRIPE, clip=head_mask)


def render_tiger_image():
    painter = AnimalPainter()
    spec = build_big_cat_spec(look=LOOK)
    torso_mask, head_mask = paint_big_cat_body(painter=painter, spec=spec, look=LOOK)
    paint_body_stripes(painter=painter, torso_mask=torso_mask)
    paint_head_stripes(painter=painter, head_mask=head_mask)
    paint_big_cat_face(painter=painter, spec=spec)
    painter.save_image(name="tiger")


if __name__ == "__main__":
    render_tiger_image()
