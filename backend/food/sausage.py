"""
Grilled sausage image, drawn from scratch.
Output: sausage.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter, sample_curve

MEAT = ((214, 104, 66), (150, 56, 36))
GRILL_MARK = ((110, 36, 24), (110, 36, 24))
SHINE = ((248, 170, 140), (240, 150, 120))

SAUSAGE_WIDTH = 200
GRILL_MARK_POSITIONS = [0.25, 0.4, 0.55, 0.7, 0.85]


def build_sausage_points():
    return sample_curve(start=(210, 360), first_control=(250, 820), second_control=(760, 860), end=(820, 520))


def paint_sausage(painter):
    points = build_sausage_points()
    sausage_mask = painter.build_curve_mask(points=points, width=SAUSAGE_WIDTH)
    painter.fill(mask=sausage_mask, shade=MEAT)

    for position in GRILL_MARK_POSITIONS:
        x, y = points[int(position * (len(points) - 1))]
        painter.fill_stroke(start=(x - 60, y - 60), end=(x + 60, y + 60), width=26, shade=GRILL_MARK, clip=sausage_mask)

    painter.fill_curve(
        points=sample_curve(start=(280, 380), first_control=(310, 700), second_control=(560, 740), end=(700, 600)),
        width=22,
        shade=SHINE,
        clip=sausage_mask,
    )


def render_sausage_image():
    painter = FoodPainter()
    paint_sausage(painter)
    painter.save_image(name="sausage")


if __name__ == "__main__":
    render_sausage_image()
