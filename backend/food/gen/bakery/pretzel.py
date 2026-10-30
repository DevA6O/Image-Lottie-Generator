"""
Pretzel image, drawn from scratch.
Output: pretzel.png (1024x1024, transparent background) in frontend/results/food
"""
import math

from food.food_painter import FoodPainter
from painting.flat_painter import sample_curve

DOUGH = ((220, 146, 62), (168, 94, 34))
OUTLINE = ((104, 52, 20), (104, 52, 20))
SALT = ((255, 255, 255), (232, 232, 238))

CANVAS_WIDTH = 1024
ROPE_WIDTH = 72
OUTLINE_GROWTH = 16
SALT_COUNT_PER_ROPE = 4

BELLY_CENTER = (512, 640)
BELLY_RADIUS_X, BELLY_RADIUS_Y = 272, 190


def build_belly_points():
    """The wide loop at the bottom, from its left end around the bottom to its right end."""
    points = []

    for angle in range(180, 361, 3):
        theta = math.radians(angle)
        points.append((
            BELLY_CENTER[0] + BELLY_RADIUS_X * math.cos(theta),
            BELLY_CENTER[1] - BELLY_RADIUS_Y * math.sin(theta),
        ))

    return points


def build_left_rope_points():
    """Leaves the left end of the belly, goes around the left loop, crosses the middle and lands on the belly's right side."""
    left_loop = sample_curve(start=(250, 650), first_control=(140, 480), second_control=(200, 260), end=(340, 250))
    crossing = sample_curve(start=(340, 250), first_control=(450, 240), second_control=(480, 420), end=(580, 520))
    landing = sample_curve(start=(580, 520), first_control=(650, 590), second_control=(700, 650), end=(740, 720))

    return left_loop + crossing + landing


def mirror_horizontally(points):
    return [(CANVAS_WIDTH - x, y) for x, y in points]


def paint_rope(
    painter,
    points,
):
    painter.fill_curve(points=points, width=ROPE_WIDTH + OUTLINE_GROWTH, shade=OUTLINE)
    painter.fill_curve(points=points, width=ROPE_WIDTH, shade=DOUGH)


def paint_salt(
    painter,
    points,
):
    spacing = len(points) // SALT_COUNT_PER_ROPE

    for index in range(spacing // 2, len(points), spacing):
        painter.fill_ellipse(center=points[index], radius_x=15, radius_y=9, shade=SALT, angle=index * 7)


def render_pretzel_image():
    painter = FoodPainter()
    left_rope_points = build_left_rope_points()
    ropes = [build_belly_points(), left_rope_points, mirror_horizontally(left_rope_points)]

    for rope_points in ropes:
        paint_rope(painter=painter, points=rope_points)

    for rope_points in ropes:
        paint_salt(painter=painter, points=rope_points)

    painter.save_image(name="pretzel")


if __name__ == "__main__":
    render_pretzel_image()
