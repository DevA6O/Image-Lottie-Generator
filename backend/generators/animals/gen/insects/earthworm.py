"""
Earthworm image, drawn from scratch.
Output: earthworm.png (1024x1024, transparent background) in frontend/results/animals
"""
import math

from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_normal, build_width_profile, solid

SKIN = (240, 150, 160)
RING = (214, 112, 130)
BAND = (250, 192, 196)
POINT_COUNT = 160
RING_SPACING = 7


def build_worm_points():
    points = []

    for step in range(POINT_COUNT + 1):
        progress = step / POINT_COUNT
        x = 880 - 720 * progress
        y = 640 + 150 * math.sin(progress * math.pi * 2.4 + 0.4) - 120 * progress
        points.append((x, y))

    return points


def paint_body(painter, points):
    widths = build_width_profile(stops=[(0.0, 36), (0.15, 100), (0.9, 112), (1.0, 100)], point_count=len(points))
    body_mask = painter.build_tapered_curve_mask(points=points, widths=widths)
    painter.fill(mask=body_mask, shade=solid(SKIN))
    painter.fill_curve(points=points[120:140], width=118, shade=solid(BAND), clip=body_mask)

    for index in range(RING_SPACING, POINT_COUNT - 4, RING_SPACING):
        normal_x, normal_y = build_normal(points=points, index=index)
        reach = widths[index] / 2 - 14
        x, y = points[index]
        painter.line(points=[(x + normal_x * reach, y + normal_y * reach), (x - normal_x * reach, y - normal_y * reach)], width=7, color=RING)


def paint_face(painter, points):
    x, y = points[-1]

    for side in (-1, 1):
        painter.spot(center=(x - 22, y + side * 24 - 10), radius_x=12, radius_y=12, color=EYE)

    painter.arc_line(center=(x - 40, y), radius=30, start_angle=-50, end_angle=50, width=9, color=EYE)


def render_earthworm_image():
    painter = AnimalPainter()
    points = build_worm_points()
    paint_body(painter, points=points)
    paint_face(painter, points=points)
    painter.save_image(name="earthworm")


if __name__ == "__main__":
    render_earthworm_image()
