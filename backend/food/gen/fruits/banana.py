"""
Banana image, drawn from scratch.
Output: banana.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter
from painting.flat_painter import build_width_profile, rotate_point, sample_curve

PEEL = ((255, 232, 96), (232, 178, 34))
RIDGE = ((214, 160, 30), (214, 160, 30))
TIP = ((104, 72, 40), (70, 46, 26))
STEM = ((156, 140, 70), (110, 92, 44))

BANANA_WIDTHS = [(0.0, 46), (0.12, 110), (0.5, 170), (0.88, 110), (1.0, 46)]
TILT_DEGREES = -28
RIDGE_OFFSET = 46
RIDGE_TRIM = 9


def build_banana_points():
    curve_points = sample_curve(start=(170, 400), first_control=(270, 840), second_control=(720, 860), end=(860, 440))

    return [rotate_point(point=point, center=(512, 512), angle_degrees=TILT_DEGREES) for point in curve_points]


def paint_banana(painter):
    points = build_banana_points()
    banana_mask = painter.build_tapered_curve_mask(points=points, widths=build_width_profile(stops=BANANA_WIDTHS))
    painter.fill(mask=banana_mask, shade=PEEL)

    ridge_points = [(x, y + RIDGE_OFFSET) for x, y in points[RIDGE_TRIM * 2:-RIDGE_TRIM * 2]]
    painter.fill_curve(points=ridge_points, width=10, shade=RIDGE, clip=banana_mask)

    return points


def paint_tips(
    painter,
    points,
):
    painter.fill_circle(center=points[0], radius=26, shade=TIP)
    painter.fill_stroke(start=points[-1], end=(points[-1][0] + 18, points[-1][1] - 110), width=46, shade=STEM)


def render_banana_image():
    painter = FoodPainter()
    points = paint_banana(painter)
    paint_tips(painter=painter, points=points)
    painter.save_image(name="banana")


if __name__ == "__main__":
    render_banana_image()
