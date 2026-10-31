"""
Face parts that many animal heads share: eyes, noses, mouths and ears.
Every function draws onto an AnimalPainter. The face looks straight at the viewer.
"""
from painting.flat_painter import rotate_point, solid

EYE = (46, 36, 46)
EYE_SHINE = (255, 255, 255)
NOSE = (58, 44, 52)
PINK = (246, 150, 164)
CREAM = (252, 236, 208)
MOUTH_LINE_WIDTH = 12


def paint_eye(
    painter,
    center,
    radius,
):
    painter.spot(center=center, radius_x=radius, radius_y=radius, color=EYE)
    painter.spot(
        center=(center[0] - radius * 0.28, center[1] - radius * 0.32),
        radius_x=radius * 0.3,
        radius_y=radius * 0.3,
        color=EYE_SHINE,
    )


def paint_eye_pair(
    painter,
    center_x,
    y,
    spread,
    radius=26,
):
    """Two round eyes. spread is the distance from the middle to each eye."""
    paint_eye(painter=painter, center=(center_x - spread, y), radius=radius)
    paint_eye(painter=painter, center=(center_x + spread, y), radius=radius)


def paint_nose(
    painter,
    center,
    radius_x,
    radius_y,
    color=NOSE,
):
    painter.blob(center=center, radius_x=radius_x, radius_y=radius_y, color=color)
    painter.spot(
        center=(center[0] - radius_x * 0.3, center[1] - radius_y * 0.35),
        radius_x=radius_x * 0.28,
        radius_y=radius_y * 0.2,
        color=(255, 255, 255),
    )


def paint_cat_mouth(
    painter,
    center,
    half_width,
    color=NOSE,
):
    """Two small arcs like a 'w', hanging from the nose."""
    radius = half_width / 2
    painter.line(points=[(center[0], center[1] - 20), center], width=MOUTH_LINE_WIDTH, color=color)
    painter.arc_line(center=(center[0] - radius, center[1]), radius=radius, start_angle=0, end_angle=170, width=MOUTH_LINE_WIDTH, color=color)
    painter.arc_line(center=(center[0] + radius, center[1]), radius=radius, start_angle=10, end_angle=180, width=MOUTH_LINE_WIDTH, color=color)


def paint_smile(
    painter,
    center,
    radius,
    color=NOSE,
):
    painter.arc_line(center=center, radius=radius, start_angle=30, end_angle=150, width=MOUTH_LINE_WIDTH, color=color)


def paint_pointed_ears(
    painter,
    center_x,
    base_y,
    spread,
    height,
    half_width,
    color,
    inner_color=PINK,
    lean=0,
    tuft_color=None,
):
    """Two triangle ears. spread is the distance from the middle to the ear base, lean tilts the tips outward."""
    for side in (-1, 1):
        base_x = center_x + side * spread
        tip = (base_x + side * lean, base_y - height)
        outer_points = [(base_x - half_width, base_y), (base_x + half_width, base_y), tip]
        inner_points = [
            (base_x - half_width * 0.5, base_y - height * 0.08),
            (base_x + half_width * 0.5, base_y - height * 0.08),
            (tip[0] - side * lean * 0.05, tip[1] + height * 0.38),
        ]
        painter.soft_polygon(points=outer_points, color=color, softness=44)
        painter.flat_soft_polygon(points=inner_points, color=inner_color, softness=22)

        if tuft_color is not None:
            tuft_points = [(tip[0] - 24, tip[1] + 70), (tip[0] + 24, tip[1] + 70), (tip[0] + side * 6, tip[1] - 60)]
            painter.soft_polygon(points=tuft_points, color=tuft_color, softness=20)


def paint_round_ears(
    painter,
    center_x,
    y,
    spread,
    radius,
    color,
    inner_color=PINK,
):
    for side in (-1, 1):
        ear_center = (center_x + side * spread, y)
        painter.blob(center=ear_center, radius_x=radius, radius_y=radius, color=color)
        painter.spot(center=ear_center, radius_x=radius * 0.58, radius_y=radius * 0.58, color=inner_color)


def paint_long_ears(
    painter,
    center_x,
    base_y,
    spread,
    length,
    half_width,
    color,
    inner_color=PINK,
    lean=0,
    tip_color=None,
):
    """Tall oval ears (rabbit, hare, donkey). lean tilts them outward in degrees."""
    for side in (-1, 1):
        ear_center = (center_x + side * spread, base_y - length / 2)
        ear_mask = painter.build_rotated_ellipse_mask(center=ear_center, radius_x=half_width, radius_y=length / 2, angle=side * lean)
        painter.fill(mask=ear_mask, shade=solid(color))

        if tip_color is not None:
            tip_center = rotate_point(point=(ear_center[0], ear_center[1] - length / 2), center=ear_center, angle_degrees=side * lean)
            painter.fill_ellipse(center=tip_center, radius_x=half_width * 1.3, radius_y=length * 0.2, shade=solid(tip_color), clip=ear_mask, angle=side * lean)

        painter.spot(
            center=(ear_center[0], ear_center[1] + length * 0.06),
            radius_x=half_width * 0.52,
            radius_y=length * 0.36,
            color=inner_color,
            angle=side * lean,
        )
