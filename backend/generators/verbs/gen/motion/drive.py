"""
Scene for the irregular verb "drive" (drove, driven).
Output: drive_infinitive.png, drive_past.png and drive_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from painting.flat_painter import solid
from verbs.props import ORANGE, draw_car_body, draw_car_cabin, draw_dust_puff, draw_flag, draw_sparkle, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

CAR_Y = 680
DRIVER_SCALE = 0.72
DRIVER_OFFSET = (-72, -10)    # Driver hip relative to the car center
DRIVER_ARMS = (78, 8)    # Both arms reach the wheel, so the second arm hides behind the first
WHEEL_COLOR = (60, 66, 86)
WHEEL_COLUMN_COLOR = (96, 106, 130)


def paint_drive_scene(painter, form):
    if form == INFINITIVE:
        draw_wind_lines(painter=painter, origin=(250, 650), length=190, count=3)
        paint_car_with_driver(painter=painter, center_x=512)
    elif form == PAST:
        draw_dust_puff(painter=painter, center=(200, 780), size=1.3)
        draw_dust_puff(painter=painter, center=(340, 800), size=0.9)
        paint_car_with_driver(painter=painter, center_x=600)
        paint_past_clock(painter=painter, center=(330, 330))
    else:
        draw_flag(painter=painter, pole_bottom=(860, 836), pole_height=330, width=120, height=80, color=ORANGE)
        paint_car_with_driver(painter=painter, center_x=420)
        draw_sparkle(painter=painter, center=(210, 440), size=36)
        draw_sparkle(painter=painter, center=(640, 380), size=28)


def paint_car_with_driver(
    painter,
    center_x,
):
    car_center = (center_x, CAR_Y)
    driver_hip = (center_x + DRIVER_OFFSET[0], CAR_Y + DRIVER_OFFSET[1])

    draw_car_cabin(painter=painter, center=car_center)
    Milo(hip=driver_hip, scale=DRIVER_SCALE).draw(
        painter=painter,
        pose=Pose(left_arm=DRIVER_ARMS, right_arm=DRIVER_ARMS, mouth="grin"),
        with_legs=False,
        before_arms=lambda skeleton: paint_steering_wheel(painter=painter, hands=skeleton.right_hand),
    )
    draw_car_body(painter=painter, center=car_center)


def paint_steering_wheel(
    painter,
    hands,
):
    """Seen from the side, the wheel is a tilted ellipse on a column that goes down into the dashboard."""
    column_end = (hands[0] + 30, hands[1] + 64)
    painter.fill_stroke(start=hands, end=column_end, width=12, shade=solid(WHEEL_COLUMN_COLOR))
    painter.fill_ellipse(center=(hands[0] + 14, hands[1]), radius_x=18, radius_y=56, shade=solid(WHEEL_COLOR), angle=-15)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="drive", paint_scene=paint_drive_scene)
