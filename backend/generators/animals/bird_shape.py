"""
The side view of a perched bird as a function, so that every small bird draws the very same body.
The bird looks to the left. Colors, tail length and beak make the different species.
"""
from painting.flat_painter import build_width_profile, sample_curve, solid

BEAK_DEFAULT = (250, 170, 50)
LEG_DEFAULT = (232, 150, 60)
EYE = (46, 36, 46)

BODY_CENTER = (540, 590)
BODY_RADIUS_X = 240
BODY_RADIUS_Y = 190
BODY_TILT = 22
HEAD_CENTER = (370, 410)
HEAD_RADIUS = 125
TAIL_START = (700, 650)
TAIL_WIDTH = 130


def _paint_tail(
    painter,
    tail_color,
    tail_length,
):
    end = (TAIL_START[0] + tail_length * 0.62, TAIL_START[1] + tail_length * 0.78)
    points = sample_curve(
        start=TAIL_START,
        first_control=(TAIL_START[0] + tail_length * 0.2, TAIL_START[1] + tail_length * 0.3),
        second_control=(end[0] - tail_length * 0.2, end[1] - tail_length * 0.3),
        end=end,
    )
    widths = build_width_profile(stops=[(0.0, TAIL_WIDTH * 0.7), (0.6, TAIL_WIDTH), (1.0, TAIL_WIDTH * 0.85)])
    painter.fill_tapered_curve(points=points, widths=widths, shade=solid(tail_color))


def _paint_legs(
    painter,
    leg_color,
):
    for foot_x in (500, 580):
        painter.line(points=[(foot_x, 740), (foot_x - 10, 850)], width=18, color=leg_color)
        painter.line(points=[(foot_x - 60, 862), (foot_x - 10, 850), (foot_x + 30, 866)], width=16, color=leg_color)


def _paint_beak(
    painter,
    beak_color,
    hooked,
    beak_length,
):
    tip_x = HEAD_CENTER[0] - HEAD_RADIUS - beak_length

    if hooked:
        points = [(HEAD_CENTER[0] - 80, 350), (tip_x + 20, 420), (tip_x, 500), (HEAD_CENTER[0] - 80, 480)]
        painter.soft_polygon(points=points, color=beak_color, softness=36)
    else:
        points = [(HEAD_CENTER[0] - 90, 372), (tip_x, 425), (HEAD_CENTER[0] - 90, 468)]
        painter.soft_polygon(points=points, color=beak_color, softness=24)


def _paint_eye(
    painter,
    eye_ring_color,
):
    eye_center = (HEAD_CENTER[0] - 40, HEAD_CENTER[1] - 20)

    if eye_ring_color is not None:
        painter.spot(center=eye_center, radius_x=36, radius_y=36, color=eye_ring_color)

    painter.spot(center=eye_center, radius_x=21, radius_y=21, color=EYE)
    painter.spot(center=(eye_center[0] - 6, eye_center[1] - 7), radius_x=6, radius_y=6, color=(255, 255, 255))


def draw_perched_bird(
    painter,
    body_color,
    belly_color,
    wing_color,
    tail_color=None,
    head_color=None,
    beak_color=BEAK_DEFAULT,
    leg_color=LEG_DEFAULT,
    tail_length=170,
    hooked_beak=False,
    beak_length=70,
    eye_ring_color=None,
):
    """Returns the head center, so the caller can add a crest or a patch."""
    tail_color = tail_color or wing_color
    head_color = head_color or body_color

    _paint_tail(painter=painter, tail_color=tail_color, tail_length=tail_length)
    _paint_legs(painter=painter, leg_color=leg_color)

    body_mask = painter.build_rotated_ellipse_mask(center=BODY_CENTER, radius_x=BODY_RADIUS_X, radius_y=BODY_RADIUS_Y, angle=BODY_TILT)
    painter.fill(mask=body_mask, shade=solid(body_color))
    painter.fill_ellipse(center=(450, 690), radius_x=190, radius_y=120, shade=solid(belly_color), angle=BODY_TILT, clip=body_mask)

    painter.blob(center=(590, 590), radius_x=165, radius_y=84, color=wing_color, angle=BODY_TILT + 4)

    painter.blob(center=HEAD_CENTER, radius_x=HEAD_RADIUS, radius_y=HEAD_RADIUS, color=head_color)
    _paint_beak(painter=painter, beak_color=beak_color, hooked=hooked_beak, beak_length=beak_length)
    _paint_eye(painter=painter, eye_ring_color=eye_ring_color)

    return HEAD_CENTER
