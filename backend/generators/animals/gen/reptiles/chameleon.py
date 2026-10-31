"""
Chameleon image, drawn from scratch.
Output: chameleon.png (1024x1024, transparent background) in frontend/results/animals
"""
import math

from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_width_profile, solid

SKIN = (116, 192, 96)
STRIPE = (252, 178, 60)
DARK = (70, 148, 86)
EYE_RING = (252, 220, 80)
SPIRAL_CENTER = (800, 650)
SPIRAL_START_RADIUS = 150
SPIRAL_END_RADIUS = 40
SPIRAL_POINT_COUNT = 90


def build_tail_points():
    points = []

    for step in range(SPIRAL_POINT_COUNT + 1):
        progress = step / SPIRAL_POINT_COUNT
        radius = SPIRAL_START_RADIUS + (SPIRAL_END_RADIUS - SPIRAL_START_RADIUS) * progress
        angle = math.radians(180 - 90 + progress * 600)
        points.append((SPIRAL_CENTER[0] + radius * math.cos(angle), SPIRAL_CENTER[1] + radius * math.sin(angle)))

    return points


def paint_legs_and_tail(painter):
    tail_points = build_tail_points()
    painter.fill_tapered_curve(points=tail_points, widths=build_width_profile(stops=[(0.0, 100), (1.0, 22)], point_count=len(tail_points)), shade=solid(SKIN))

    for leg_x in (360, 630):
        painter.line(points=[(leg_x, 700), (leg_x - 10, 810)], width=50, color=DARK)
        painter.line(points=[(leg_x - 50, 835), (leg_x - 10, 810), (leg_x + 40, 840)], width=36, color=DARK)


def paint_body(painter):
    body_mask = painter.build_rotated_ellipse_mask(center=(500, 580), radius_x=285, radius_y=190)
    painter.fill(mask=body_mask, shade=solid(SKIN))

    for stripe_x in (430, 520, 610):
        painter.fill_stroke(start=(stripe_x, 420), end=(stripe_x - 20, 700), width=34, shade=solid(STRIPE), clip=body_mask)


def paint_head(painter):
    painter.blob(center=(250, 500), radius_x=140, radius_y=105, color=SKIN)
    painter.soft_polygon(points=[(260, 410), (330, 320), (400, 440)], color=DARK, softness=30)
    painter.blob(center=(235, 440), radius_x=72, radius_y=72, color=DARK)
    painter.spot(center=(235, 440), radius_x=44, radius_y=44, color=EYE_RING)
    painter.spot(center=(228, 440), radius_x=20, radius_y=20, color=EYE)
    painter.arc_line(center=(170, 520), radius=70, start_angle=15, end_angle=80, width=12, color=DARK)


def render_chameleon_image():
    painter = AnimalPainter()
    paint_legs_and_tail(painter)
    paint_body(painter)
    paint_head(painter)
    painter.save_image(name="chameleon")


if __name__ == "__main__":
    render_chameleon_image()
