"""
The front view of a sitting frog as a function, so that the frog and the toad draw the very same body.
The caller adds warts or cheeks on top of the returned body mask.
"""
from animals.face_parts import EYE
from painting.flat_painter import solid

EYE_WHITE = (255, 255, 255)
MOUTH_LINE = (70, 60, 56)
EYE_CENTERS = ((350, 390), (674, 390))


def _paint_legs(
    painter,
    skin_color,
):
    for side in (-1, 1):
        painter.blob(center=(512 + side * 285, 760), radius_x=165, radius_y=105, color=skin_color, angle=side * 25)
        painter.blob(center=(512 + side * 385, 880), radius_x=105, radius_y=36, color=skin_color, angle=side * 8)
        painter.blob(center=(512 + side * 130, 890), radius_x=85, radius_y=36, color=skin_color)


def _paint_eye(
    painter,
    center,
    skin_color,
    iris_color,
    bar_pupil,
):
    painter.blob(center=center, radius_x=105, radius_y=105, color=skin_color)
    painter.spot(center=center, radius_x=68, radius_y=68, color=EYE_WHITE)
    painter.spot(center=center, radius_x=46, radius_y=46, color=iris_color)

    if bar_pupil:
        painter.spot(center=center, radius_x=36, radius_y=12, color=EYE)
    else:
        painter.spot(center=center, radius_x=26, radius_y=26, color=EYE)
        painter.spot(center=(center[0] - 10, center[1] - 12), radius_x=9, radius_y=9, color=EYE_WHITE)


def draw_frog(
    painter,
    skin_color,
    belly_color,
    iris_color=EYE_WHITE,
    bar_pupil=False,
):
    """Returns the body mask."""
    _paint_legs(painter=painter, skin_color=skin_color)

    body_mask = painter.build_rotated_ellipse_mask(center=(512, 620), radius_x=335, radius_y=255)
    painter.fill(mask=body_mask, shade=solid(skin_color))
    painter.fill_ellipse(center=(512, 800), radius_x=215, radius_y=130, shade=solid(belly_color), clip=body_mask)

    for center in EYE_CENTERS:
        _paint_eye(painter=painter, center=center, skin_color=skin_color, iris_color=iris_color, bar_pupil=bar_pupil)

    painter.arc_line(center=(512, 540), radius=235, start_angle=28, end_angle=152, width=14, color=MOUTH_LINE)
    painter.spot(center=(480, 500), radius_x=9, radius_y=9, color=MOUTH_LINE)
    painter.spot(center=(544, 500), radius_x=9, radius_y=9, color=MOUTH_LINE)

    return body_mask
