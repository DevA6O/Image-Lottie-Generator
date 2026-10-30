"""
Purple onion image, drawn from scratch.
Output: onion.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter
from painting.flat_painter import sample_curve

ONION = ((214, 128, 176), (140, 60, 120))
LAYER_LINE = ((236, 176, 208), (236, 176, 208))
ROOT = ((226, 214, 196), (190, 176, 150))

LAYER_OFFSETS = [-150, -50, 50, 150]


def paint_roots(painter):
    for x in (480, 512, 544):
        painter.fill_stroke(start=(x, 840), end=(x + (x - 512) * 1.5, 920), width=12, shade=ROOT)


def paint_onion(painter):
    bulb = painter.build_rotated_ellipse_mask(center=(512, 620), radius_x=300, radius_y=250)
    tip = painter.build_polygon_mask(points=[(512, 200), (650, 480), (374, 480)])
    onion_mask = painter.round_corners(mask=painter.union_masks(first_mask=bulb, second_mask=tip), radius=50)
    painter.fill(mask=onion_mask, shade=ONION)

    for offset in LAYER_OFFSETS:
        layer_points = sample_curve(
            start=(512 + offset * 0.2, 260),
            first_control=(512 + offset * 1.6, 480),
            second_control=(512 + offset * 1.6, 720),
            end=(512 + offset * 0.4, 870),
        )
        painter.fill_curve(points=layer_points, width=12, shade=LAYER_LINE, clip=onion_mask)


def render_onion_image():
    painter = FoodPainter()
    paint_roots(painter)
    paint_onion(painter)
    painter.save_image(name="onion")


if __name__ == "__main__":
    render_onion_image()
