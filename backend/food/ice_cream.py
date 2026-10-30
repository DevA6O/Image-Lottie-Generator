"""
Ice cream cone with two scoops, drawn from scratch.
Output: ice_cream.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

CONE = ((240, 190, 110), (206, 140, 62))
WAFFLE_LINE = ((180, 116, 44), (180, 116, 44))
STRAWBERRY = ((255, 170, 200), (240, 110, 160))
MINT = ((170, 236, 214), (100, 200, 170))
CHERRY = ((238, 60, 70), (170, 28, 46))

LINE_SPACING = 70


def paint_cone(painter):
    outline = painter.build_polygon_mask(points=[(320, 540), (704, 540), (512, 930)])
    cone_mask = painter.round_corners(mask=outline, radius=14)
    painter.fill(mask=cone_mask, shade=CONE)

    for offset in range(0, 800, LINE_SPACING):
        painter.fill_stroke(start=(200 + offset * 0.5, 500 + offset * 0.5), end=(850, 1150 - offset * 0.7), width=12, shade=WAFFLE_LINE, clip=cone_mask)
        painter.fill_stroke(start=(850 - offset * 0.5, 500 + offset * 0.5), end=(200, 1150 - offset * 0.7), width=12, shade=WAFFLE_LINE, clip=cone_mask)


def paint_scoops(painter):
    painter.fill_ellipse(center=(512, 560), radius_x=220, radius_y=80, shade=MINT)
    painter.fill_circle(center=(512, 400), radius=190, shade=STRAWBERRY)
    painter.fill_circle(center=(512, 195), radius=48, shade=CHERRY)


def render_ice_cream_image():
    painter = FoodPainter()
    paint_cone(painter)
    paint_scoops(painter)
    painter.save_image(name="ice_cream")


if __name__ == "__main__":
    render_ice_cream_image()
