"""
Hedgehog image, drawn from scratch.
Output: hedgehog.png (1024x1024, transparent background) in frontend/results/animals
"""
import math

from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, NOSE
from painting.flat_painter import solid

SPINES = (112, 80, 62)
SKIN = (246, 206, 160)
EAR = (226, 170, 128)
SPINE_COUNT = 19
SPINE_BASE_RADIUS = 330
SPINE_LENGTH = 70
DOME_CENTER = (560, 730)


def build_spiny_dome_points():
    """The upper half of a circle with a zigzag edge. Every second point sticks out."""
    points: list[tuple[float, float]] = [(DOME_CENTER[0] - SPINE_BASE_RADIUS, DOME_CENTER[1] + 40)]

    for index in range(SPINE_COUNT * 2 + 1):
        angle = math.radians(180 + index * 180 / (SPINE_COUNT * 2))
        radius = SPINE_BASE_RADIUS + (SPINE_LENGTH if index % 2 == 1 else 0)
        points.append((DOME_CENTER[0] + radius * math.cos(angle), DOME_CENTER[1] + radius * math.sin(angle) * 1.05))

    points.append((DOME_CENTER[0] + SPINE_BASE_RADIUS, DOME_CENTER[1] + 40))

    return points


def paint_feet(painter):
    painter.blob(center=(430, 850), radius_x=70, radius_y=42, color=SKIN)
    painter.blob(center=(680, 850), radius_x=70, radius_y=42, color=SKIN)


def paint_spines(painter):
    spines_mask = painter.build_soft_polygon_mask(points=build_spiny_dome_points(), softness=14)
    painter.fill(mask=spines_mask, shade=solid(SPINES))


def paint_face(painter):
    painter.blob(center=(400, 745), radius_x=215, radius_y=130, color=SKIN, angle=-10)
    painter.blob(center=(370, 585), radius_x=48, radius_y=44, color=EAR)
    painter.blob(center=(195, 770), radius_x=44, radius_y=38, color=NOSE)
    painter.spot(center=(300, 710), radius_x=24, radius_y=24, color=EYE)
    painter.spot(center=(293, 702), radius_x=7, radius_y=7, color=(255, 255, 255))
    painter.arc_line(center=(300, 800), radius=44, start_angle=20, end_angle=120, width=11, color=EAR)


def render_hedgehog_image():
    painter = AnimalPainter()
    paint_feet(painter)
    paint_spines(painter)
    paint_face(painter)
    painter.save_image(name="hedgehog")


if __name__ == "__main__":
    render_hedgehog_image()
