"""
Carrot image, drawn from scratch.
Output: carrot.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter
from painting.flat_painter import build_normal, build_width_profile, sample_curve

CARROT = ((255, 164, 56), (222, 92, 18))
GROOVE = ((200, 82, 16), (200, 82, 16))
LEAF = ((140, 212, 92), (70, 150, 52))
LEAF_BACK = ((100, 180, 76), (52, 124, 46))

CARROT_WIDTHS = [(0.0, 190), (0.1, 200), (0.5, 115), (1.0, 16)]
LEAF_WIDTHS = [(0.0, 36), (0.45, 86), (1.0, 6)]
GROOVE_POSITIONS = [0.22, 0.38, 0.52, 0.66, 0.78]
GROOVE_LENGTH = 62
GROOVE_WIDTH = 12

# Each leaf: start, first control, second control, end
LEAVES = [
    ((310, 270), (280, 190), (240, 130), (190, 70)),
    ((300, 270), (290, 190), (300, 120), (330, 50)),
    ((300, 280), (230, 260), (170, 240), (100, 230)),
]


def paint_leaves(painter):
    widths = build_width_profile(stops=LEAF_WIDTHS)

    for index, (start, first_control, second_control, end) in enumerate(LEAVES):
        points = sample_curve(start=start, first_control=first_control, second_control=second_control, end=end)
        shade = LEAF if index == 1 else LEAF_BACK
        painter.fill_tapered_curve(points=points, widths=widths, shade=shade, round_ends=False)


def paint_grooves(
    painter,
    points,
    widths,
    carrot_mask,
):
    """Short lines that start at alternating edges of the carrot."""
    for groove_number, position in enumerate(GROOVE_POSITIONS):
        index = int(position * (len(points) - 1))
        normal_x, normal_y = build_normal(points=points, index=index)
        side = 1 if groove_number % 2 == 0 else -1
        edge_distance = side * widths[index] / 2
        start = (points[index][0] + normal_x * edge_distance, points[index][1] + normal_y * edge_distance)
        end = (start[0] - normal_x * side * GROOVE_LENGTH, start[1] - normal_y * side * GROOVE_LENGTH)
        painter.fill_stroke(start=start, end=end, width=GROOVE_WIDTH, shade=GROOVE, clip=carrot_mask)


def paint_carrot(painter):
    points = sample_curve(start=(300, 300), first_control=(430, 430), second_control=(600, 640), end=(840, 830))
    widths = build_width_profile(stops=CARROT_WIDTHS)
    carrot_mask = painter.build_tapered_curve_mask(points=points, widths=widths)
    painter.fill(mask=carrot_mask, shade=CARROT)
    paint_grooves(painter=painter, points=points, widths=widths, carrot_mask=carrot_mask)


def render_carrot_image():
    painter = FoodPainter()
    paint_leaves(painter)
    paint_carrot(painter)
    painter.save_image(name="carrot")


if __name__ == "__main__":
    render_carrot_image()
