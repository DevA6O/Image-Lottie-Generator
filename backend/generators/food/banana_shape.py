"""
The banana of the banana image as a function, so that other images draw the very same banana.
The defaults draw it as the full banana image.
"""
from painting.flat_painter import build_width_profile, rotate_point, sample_curve

PEEL = ((255, 232, 96), (232, 178, 34))
RIDGE = ((214, 160, 30), (214, 160, 30))
TIP = ((104, 72, 40), (70, 46, 26))
STEM = ((156, 140, 70), (110, 92, 44))

CANVAS_CENTER = (512, 512)
BANANA_WIDTHS = [(0.0, 46), (0.12, 110), (0.5, 170), (0.88, 110), (1.0, 46)]
TILT_DEGREES = -28
RIDGE_OFFSET = 46
RIDGE_TRIM = 9

def _build_banana_points(
    center,
    scale,
    tilt,
):
    curve_points = sample_curve(start=(170, 400), first_control=(270, 840), second_control=(720, 860), end=(860, 440))
    tilted_points = [rotate_point(point=point, center=CANVAS_CENTER, angle_degrees=tilt) for point in curve_points]

    return [
        (center[0] + (x - CANVAS_CENTER[0]) * scale, center[1] + (y - CANVAS_CENTER[1]) * scale)
        for x, y in tilted_points
    ]


def draw_banana(
    painter,
    center=CANVAS_CENTER,
    scale=1.0,
    tilt=TILT_DEGREES,
):
    """The center is where the middle of the banana image lands. scale 1.0 is the size of the banana image."""
    points = _build_banana_points(center=center, scale=scale, tilt=tilt)
    widths = [width * scale for width in build_width_profile(stops=BANANA_WIDTHS)]
    banana_mask = painter.build_tapered_curve_mask(points=points, widths=widths)
    painter.fill(mask=banana_mask, shade=PEEL)

    ridge_points = [(x, y + RIDGE_OFFSET * scale) for x, y in points[RIDGE_TRIM * 2:-RIDGE_TRIM * 2]]
    painter.fill_curve(points=ridge_points, width=10 * scale, shade=RIDGE, clip=banana_mask)

    painter.fill_circle(center=points[0], radius=26 * scale, shade=TIP)
    painter.fill_stroke(
        start=points[-1],
        end=(points[-1][0] + 18 * scale, points[-1][1] - 110 * scale),
        width=46 * scale,
        shade=STEM,
    )
