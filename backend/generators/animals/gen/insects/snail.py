"""
Snail image, drawn from scratch.
Output: snail.png (1024x1024, transparent background) in frontend/results/animals
"""
import math

from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_width_profile, sample_curve, solid

SKIN = (232, 208, 160)
SHELL = (214, 120, 62)
SHELL_SPIRAL = (246, 178, 108)
SHELL_CENTER = (610, 480)
SHELL_RADIUS = 255
SPIRAL_TURNS = 2.6
SPIRAL_POINT_COUNT = 120


def build_spiral_points():
    points = []

    for step in range(SPIRAL_POINT_COUNT + 1):
        progress = step / SPIRAL_POINT_COUNT
        radius = 25 + (SHELL_RADIUS - 70) * progress
        angle = progress * SPIRAL_TURNS * 2 * math.pi
        points.append((SHELL_CENTER[0] + radius * math.cos(angle), SHELL_CENTER[1] + radius * math.sin(angle)))

    return points


def paint_body(painter):
    foot_points = sample_curve(start=(180, 790), first_control=(400, 790), second_control=(700, 800), end=(920, 790))
    foot_widths = build_width_profile(stops=[(0.0, 110), (0.3, 130), (0.8, 110), (1.0, 20)])
    painter.fill_tapered_curve(points=foot_points, widths=foot_widths, shade=solid(SKIN))
    painter.blob(center=(250, 640), radius_x=95, radius_y=160, color=SKIN, angle=-12)

    for side, stalk_end in ((-1, (170, 400)), (1, (310, 410))):
        painter.line(points=[(250 + side * 20, 540), stalk_end], width=26, color=SKIN)
        painter.blob(center=stalk_end, radius_x=34, radius_y=34, color=SKIN)
        painter.spot(center=stalk_end, radius_x=15, radius_y=15, color=EYE)

    painter.arc_line(center=(215, 660), radius=50, start_angle=20, end_angle=110, width=12, color=SHELL)


def paint_shell(painter):
    shell_mask = painter.build_rotated_ellipse_mask(center=SHELL_CENTER, radius_x=SHELL_RADIUS, radius_y=SHELL_RADIUS)
    painter.fill(mask=shell_mask, shade=solid(SHELL))
    painter.fill_curve(points=build_spiral_points(), width=26, shade=solid(SHELL_SPIRAL), clip=shell_mask)


def render_snail_image():
    painter = AnimalPainter()
    paint_body(painter)
    paint_shell(painter)
    painter.save_image(name="snail")


if __name__ == "__main__":
    render_snail_image()
