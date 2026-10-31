"""
Snake image, drawn from scratch.
Output: snake.png (1024x1024, transparent background) in frontend/results/animals
"""
import math

from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_width_profile, solid

SKIN = (96, 188, 90)
PATTERN = (52, 140, 74)
BELLY = (232, 238, 160)
TONGUE = (230, 58, 70)
POINT_COUNT = 140


def build_snake_points():
    """A wave from the tail on the right to the raised head on the left."""
    points = []

    for step in range(POINT_COUNT + 1):
        progress = step / POINT_COUNT
        x = 900 - 600 * progress
        y = 790 - 120 * math.sin(progress * math.pi * 2.6) - 330 * progress ** 4
        points.append((x, y))

    return points


def paint_body(painter, points):
    widths = build_width_profile(stops=[(0.0, 14), (0.3, 80), (0.9, 100), (1.0, 92)])
    body_mask = painter.build_tapered_curve_mask(points=points, widths=widths)
    painter.fill(mask=body_mask, shade=solid(SKIN))

    for point_index in range(14, POINT_COUNT - 8, 12):
        point = points[point_index]
        painter.fill_ellipse(center=point, radius_x=24, radius_y=30, shade=solid(PATTERN), clip=body_mask)


def paint_head(painter, points):
    head_center = points[-1]
    painter.blob(center=(head_center[0] - 25, head_center[1] - 20), radius_x=105, radius_y=82, color=SKIN, angle=-18)
    painter.spot(center=(head_center[0] - 40, head_center[1] - 48), radius_x=20, radius_y=20, color=(250, 220, 70))
    painter.spot(center=(head_center[0] - 40, head_center[1] - 48), radius_x=9, radius_y=14, color=EYE)

    tongue_start = (head_center[0] - 120, head_center[1] - 10)
    painter.line(points=[tongue_start, (tongue_start[0] - 70, tongue_start[1] + 10)], width=10, color=TONGUE)
    painter.line(points=[(tongue_start[0] - 70, tongue_start[1] + 10), (tongue_start[0] - 120, tongue_start[1] - 20)], width=10, color=TONGUE)
    painter.line(points=[(tongue_start[0] - 70, tongue_start[1] + 10), (tongue_start[0] - 120, tongue_start[1] + 40)], width=10, color=TONGUE)


def render_snake_image():
    painter = AnimalPainter()
    points = build_snake_points()
    paint_body(painter, points=points)
    paint_head(painter, points=points)
    painter.save_image(name="snake")


if __name__ == "__main__":
    render_snake_image()
