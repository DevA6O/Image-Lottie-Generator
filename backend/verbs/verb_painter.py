"""
Painter for the verb images. It reuses the food painter (flat shapes with a darker crescent)
and adds shortcuts for flat details, arcs and rings.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "food"))

from food_painter import FoodPainter, build_star_points, rotate_point, sample_curve  # noqa: E402
from layer_painter import OUT_DIR as FOOD_OUT_DIR  # noqa: E402

VERB_OUT_DIR = FOOD_OUT_DIR.parent / "verbs"
ARC_POINT_COUNT = 40
POLYLINE_STEPS_PER_SEGMENT = 12


def solid(color):
    """A shade that has the same color on top and at the bottom."""
    return (color, color)


def build_direction(angle_degrees):
    """Unit vector for body angles: 0 points down, 90 points right, 180 points up."""
    angle = math.radians(angle_degrees)

    return (math.sin(angle), math.cos(angle))


def build_arc_points(
    center,
    radius,
    start_angle,
    end_angle,
):
    """Points on a circle arc. Angles in degrees: 0 is right, 90 is down, -90 is up."""
    points = []

    for step in range(ARC_POINT_COUNT + 1):
        angle = math.radians(start_angle + (end_angle - start_angle) * step / ARC_POINT_COUNT)
        points.append((center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle)))

    return points


def build_polyline_points(corners):
    """Many points along straight segments, so a curve mask draws round joints."""
    points = []

    for start, end in zip(corners, corners[1:]):
        for step in range(POLYLINE_STEPS_PER_SEGMENT):
            progress = step / POLYLINE_STEPS_PER_SEGMENT
            points.append((start[0] + (end[0] - start[0]) * progress, start[1] + (end[1] - start[1]) * progress))

    points.append(corners[-1])

    return points


def move_point(
    point,
    angle,
    distance,
):
    """Moves a point. Angle in degrees: 0 is right, 90 is down, -90 is up."""
    radians = math.radians(angle)

    return (point[0] + distance * math.cos(radians), point[1] + distance * math.sin(radians))


class VerbPainter(FoodPainter):
    """Shapes for the verb images. flat_* methods paint one solid color without a crescent (for small details)."""

    def save_verb_image(self, file_name):
        self.save(out_file=VERB_OUT_DIR / file_name)

    def flat_ellipse(
        self,
        center,
        radius_x,
        radius_y,
        color,
        angle=0,
    ):
        mask = self.build_rotated_ellipse_mask(center=center, radius_x=radius_x, radius_y=radius_y, angle=angle)
        self.fill_flat(mask=mask, shade=solid(color))

    def flat_circle(
        self,
        center,
        radius,
        color,
    ):
        self.flat_ellipse(center=center, radius_x=radius, radius_y=radius, color=color)

    def flat_stroke(
        self,
        start,
        end,
        width,
        color,
    ):
        self.fill_flat(mask=self.build_stroke_mask(start=start, end=end, width=width), shade=solid(color))

    def flat_curve(
        self,
        points,
        width,
        color,
    ):
        self.fill_flat(mask=self.build_curve_mask(points=points, width=width), shade=solid(color))

    def flat_polygon(
        self,
        points,
        color,
    ):
        self.fill_flat(mask=self.build_polygon_mask(points=points), shade=solid(color))

    def fill_ring(
        self,
        center,
        outer_radius,
        inner_radius,
        color,
    ):
        outer_mask = self.build_rotated_ellipse_mask(center=center, radius_x=outer_radius, radius_y=outer_radius)
        inner_mask = self.build_rotated_ellipse_mask(center=center, radius_x=inner_radius, radius_y=inner_radius)
        self.fill(mask=self.subtract_masks(base_mask=outer_mask, cut_mask=inner_mask), shade=solid(color))
