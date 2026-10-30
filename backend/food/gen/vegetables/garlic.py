"""
Garlic bulb image, drawn from scratch.
Output: garlic.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter
from painting.flat_painter import sample_curve

GARLIC = ((255, 252, 244), (214, 204, 186))
CLOVE_LINE = ((196, 184, 164), (196, 184, 164))
ROOT = ((206, 190, 160), (170, 152, 124))

LINE_OFFSETS = [-190, -95, 0, 95, 190]


def paint_roots(painter):
    for x in (460, 512, 564):
        painter.fill_stroke(start=(x, 830), end=(x + (x - 512), 900), width=14, shade=ROOT)


def paint_bulb(painter):
    bulb = painter.build_rotated_ellipse_mask(center=(512, 610), radius_x=300, radius_y=240)
    tip = painter.build_polygon_mask(points=[(512, 170), (610, 440), (414, 440)])
    garlic_mask = painter.round_corners(mask=painter.union_masks(first_mask=bulb, second_mask=tip), radius=50)
    painter.fill(mask=garlic_mask, shade=GARLIC)

    for offset in LINE_OFFSETS:
        line_points = sample_curve(
            start=(512 + offset * 0.1, 260),
            first_control=(512 + offset * 1.7, 440),
            second_control=(512 + offset * 1.5, 700),
            end=(512 + offset * 0.3, 850),
        )
        painter.fill_curve(points=line_points, width=10, shade=CLOVE_LINE, clip=garlic_mask)


def render_garlic_image():
    painter = FoodPainter()
    paint_roots(painter)
    paint_bulb(painter)
    painter.save_image(name="garlic")


if __name__ == "__main__":
    render_garlic_image()
