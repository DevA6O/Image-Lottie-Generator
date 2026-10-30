"""
Croissant image, drawn from scratch.
Output: croissant.png (1024x1024, transparent background) in frontend/results/food
"""
import math

from food_painter import FoodPainter

DOUGH = ((240, 180, 84), (196, 122, 44))
SEAM = ((150, 84, 30), (150, 84, 30))

ARC_CENTER_X = 512
ARC_HALF_WIDTH = 300
ARC_BASE_Y = 650
ARC_HEIGHT = 260
SEGMENT_OVERLAP_RIM = 12

# (position on the arc from -1 to 1, half length along the arc, half thickness across it)
SEGMENTS = [
    (-1.08, 70, 42),
    (1.08, 70, 42),
    (-0.9, 100, 86),
    (0.9, 100, 86),
    (-0.6, 112, 118),
    (0.6, 112, 118),
    (-0.28, 118, 140),
    (0.28, 118, 140),
    (0.0, 122, 150),
]


def build_segment_position(position):
    x = ARC_CENTER_X + ARC_HALF_WIDTH * position
    y = ARC_BASE_Y - ARC_HEIGHT * (1 - position ** 2)
    angle = math.degrees(math.atan2(2 * ARC_HEIGHT * position, ARC_HALF_WIDTH))

    return (x, y), angle


def paint_segments(painter):
    for position, half_length, half_thickness in SEGMENTS:
        center, angle = build_segment_position(position)
        painter.fill_ellipse(
            center=center,
            radius_x=half_length + SEGMENT_OVERLAP_RIM,
            radius_y=half_thickness + SEGMENT_OVERLAP_RIM,
            shade=SEAM,
            angle=angle,
        )
        painter.fill_ellipse(center=center, radius_x=half_length, radius_y=half_thickness, shade=DOUGH, angle=angle)


def render_croissant_image():
    painter = FoodPainter()
    paint_segments(painter)
    painter.save_image(name="croissant")


if __name__ == "__main__":
    render_croissant_image()
