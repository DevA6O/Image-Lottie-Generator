"""
Zebra image, drawn from scratch: full body from the side, with stripes.
Output: zebra.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.horse_shape import HorseLook, draw_horse

LOOK = HorseLook(
    coat=(250, 248, 244),
    far_coat=(200, 198, 200),
    hoof=(52, 48, 56),
    muzzle=(86, 80, 90),
    mane=(44, 40, 50),
    ear_inner=(44, 40, 50),
    stocky=True,
)
STRIPE = (44, 40, 50)
STRIPE_WIDTH = 30


def paint_stripes(
    painter,
    body_mask,
):
    for stripe_x in range(360, 870, 70):
        painter.body_curve(points=[(stripe_x, 340), (stripe_x + 30, 540), (stripe_x, 720)], width=STRIPE_WIDTH, color=STRIPE, clip=body_mask)

    for stripe_y in range(330, 480, 60):
        painter.body_curve(points=[(230, stripe_y + 40), (330, stripe_y), (420, stripe_y + 30)], width=24, color=STRIPE, clip=body_mask)


def render_zebra_image():
    painter = AnimalPainter()
    body_mask = draw_horse(painter=painter, look=LOOK)
    paint_stripes(painter=painter, body_mask=body_mask)
    painter.save_image(name="zebra")


if __name__ == "__main__":
    render_zebra_image()
