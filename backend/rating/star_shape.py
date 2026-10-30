"""
Shared star geometry and colors for the star images and the star Lottie animations.
Both scripts use the same outline, so the image and the animation always match.
"""
import math
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[2] / "frontend" / "results" / "rating"

CANVAS_SIZE = 1024
STAR_RADIUS = 300.0
STAR_POINT_COUNT = 5
INNER_RADIUS_RATIO = 0.5

# Rounded corners: tips get a bigger cut than the valleys between them
TIP_ROUNDING = 42.0
VALLEY_ROUNDING = 20.0
CORNER_SAMPLE_COUNT = 8

STAR_CENTER_X = CANVAS_SIZE / 2
# The star is taller above its center than below, so it is shifted down to look centered
_STAR_BOTTOM_RATIO = math.cos(math.pi / STAR_POINT_COUNT)
STAR_CENTER_Y = CANVAS_SIZE / 2 + STAR_RADIUS * (1 - _STAR_BOTTOM_RATIO) / 2

# Gold gradient from the top (0.0) to the bottom (1.0) of the star
STAR_COLOR_STOPS = [(0.0, (255, 226, 102)), (0.55, (255, 190, 35)), (1.0, (240, 150, 15))]
EMPTY_STAR_COLOR = (62, 62, 72)


def _build_sharp_vertices():
    vertices = []

    for index in range(STAR_POINT_COUNT * 2):
        is_tip = index % 2 == 0
        radius = STAR_RADIUS if is_tip else STAR_RADIUS * INNER_RADIUS_RATIO
        angle = -math.pi / 2 + index * math.pi / STAR_POINT_COUNT
        vertices.append((radius * math.cos(angle), radius * math.sin(angle)))

    return vertices


def _move_towards(
    from_point,
    to_point,
    distance,
):
    delta_x = to_point[0] - from_point[0]
    delta_y = to_point[1] - from_point[1]
    length = math.hypot(delta_x, delta_y)

    return (
        from_point[0] + delta_x / length * distance,
        from_point[1] + delta_y / length * distance,
    )


def _round_corner(
    previous_vertex,
    vertex,
    next_vertex,
    rounding,
):
    """Replaces a sharp corner by a small curve (quadratic Bezier with the corner as control point)."""
    curve_start = _move_towards(from_point=vertex, to_point=previous_vertex, distance=rounding)
    curve_end = _move_towards(from_point=vertex, to_point=next_vertex, distance=rounding)
    points = []

    for sample in range(CORNER_SAMPLE_COUNT + 1):
        t = sample / CORNER_SAMPLE_COUNT
        start_weight = (1 - t) ** 2
        control_weight = 2 * (1 - t) * t
        end_weight = t ** 2
        points.append((
            start_weight * curve_start[0] + control_weight * vertex[0] + end_weight * curve_end[0],
            start_weight * curve_start[1] + control_weight * vertex[1] + end_weight * curve_end[1],
        ))

    return points


def build_star_outline():
    """Returns the rounded star as a closed polygon around (0, 0), as a list of (x, y)."""
    vertices = _build_sharp_vertices()
    outline = []

    for index, vertex in enumerate(vertices):
        is_tip = index % 2 == 0
        outline += _round_corner(
            previous_vertex=vertices[index - 1],
            vertex=vertex,
            next_vertex=vertices[(index + 1) % len(vertices)],
            rounding=TIP_ROUNDING if is_tip else VALLEY_ROUNDING,
        )

    return outline


def _find_crossing_with_center_line(
    inside_point,
    outside_point,
):
    t = (0 - inside_point[0]) / (outside_point[0] - inside_point[0])

    return (0.0, inside_point[1] + t * (outside_point[1] - inside_point[1]))


def clip_to_left_half(outline):
    """Cuts the polygon at x = 0 and keeps the left side (Sutherland-Hodgman, one edge)."""
    clipped = []

    for current_point, next_point in zip(outline, outline[1:] + outline[:1]):
        is_current_inside = current_point[0] <= 0
        is_next_inside = next_point[0] <= 0

        if is_current_inside:
            clipped.append(current_point)

        if is_current_inside != is_next_inside:
            clipped.append(_find_crossing_with_center_line(
                inside_point=current_point if is_current_inside else next_point,
                outside_point=next_point if is_current_inside else current_point,
            ))

    return clipped
