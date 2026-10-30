"""
Strawberry cake slice image, drawn from scratch.
Output: cake_slice.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

SPONGE = ((250, 214, 150), (232, 176, 98))
CREAM = ((255, 255, 255), (246, 238, 238))
ICING = ((255, 150, 176), (236, 98, 136))
PLATE_BASE = ((120, 70, 50), (92, 52, 38))
CHERRY = ((238, 60, 70), (170, 28, 46))

CAKE_LEFT, CAKE_RIGHT = 190, 834
ICING_DRIP_CENTERS = [(260, 470), (400, 490), (560, 470), (700, 490), (790, 450)]


def paint_sponge(painter):
    painter.fill_rounded_rect(box=(CAKE_LEFT, 420, CAKE_RIGHT, 830), radius=40, shade=SPONGE)
    painter.fill_rounded_rect(box=(CAKE_LEFT, 560, CAKE_RIGHT, 610), radius=0, shade=CREAM)
    painter.fill_rounded_rect(box=(CAKE_LEFT, 750, CAKE_RIGHT, 830), radius=40, shade=PLATE_BASE)


def paint_icing(painter):
    painter.fill_rounded_rect(box=(CAKE_LEFT - 20, 330, CAKE_RIGHT + 20, 450), radius=50, shade=ICING)

    for center in ICING_DRIP_CENTERS:
        painter.fill_ellipse(center=center, radius_x=44, radius_y=62, shade=ICING)


def paint_cherry(painter):
    painter.fill_stroke(start=(512, 260), end=(570, 180), width=14, shade=PLATE_BASE)
    painter.fill_circle(center=(512, 290), radius=62, shade=CHERRY)


def render_cake_slice_image():
    painter = FoodPainter()
    paint_sponge(painter)
    paint_icing(painter)
    paint_cherry(painter)
    painter.save_image(name="cake_slice")


if __name__ == "__main__":
    render_cake_slice_image()
