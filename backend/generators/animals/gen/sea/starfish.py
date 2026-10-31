"""
Starfish image, drawn from scratch.
Output: starfish.png (1024x1024, transparent background) in frontend/results/animals
"""
import math

from animals.animal_painter import AnimalPainter
from painting.flat_painter import build_star_points, solid

SKIN = (252, 148, 72)
DOT = (255, 206, 130)
STAR_CENTER = (512, 540)
OUTER_RADIUS = 400
INNER_RADIUS = 175
ARM_COUNT = 5
DOTS_PER_ARM = 3


def paint_dots(painter, star_mask):
    for arm_index in range(ARM_COUNT):
        angle = math.radians(-90 + arm_index * 360 / ARM_COUNT)

        for dot_index in range(DOTS_PER_ARM):
            distance = 120 + dot_index * 85
            dot_center = (STAR_CENTER[0] + distance * math.cos(angle), STAR_CENTER[1] + distance * math.sin(angle))
            dot_radius = 22 - dot_index * 4
            painter.fill_ellipse(center=dot_center, radius_x=dot_radius, radius_y=dot_radius, shade=solid(DOT), clip=star_mask)


def render_starfish_image():
    painter = AnimalPainter()
    star_points = build_star_points(center=STAR_CENTER, outer_radius=OUTER_RADIUS, inner_radius=INNER_RADIUS, tip_count=ARM_COUNT)
    star_mask = painter.build_soft_polygon_mask(points=star_points, softness=110)
    painter.fill(mask=star_mask, shade=solid(SKIN))
    paint_dots(painter, star_mask=star_mask)
    painter.save_image(name="starfish")


if __name__ == "__main__":
    render_starfish_image()
