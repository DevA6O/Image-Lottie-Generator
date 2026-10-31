"""
Scene for the irregular verb "wear" (wore, worn).
Output: wear_infinitive.png, wear_past.png and wear_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from painting.flat_painter import solid
from verbs.props import ORANGE, draw_check_mark
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

SCARF_COLOR = ORANGE
SCARF_DARK = (214, 118, 30)
SCARF_STRIPE = (255, 214, 120)
WAVING_ARM = (130, 0)    # Straight and raised to the side
HANDS_ON_HIPS_LEFT_ARM = (-50, 100)
HANDS_ON_HIPS_RIGHT_ARM = (50, -100)


def paint_wear_scene(painter, form):
    if form == INFINITIVE:
        pose = Pose(eyes="happy", mouth="smile", left_arm=(-14, 0), right_arm=WAVING_ARM)
    elif form == PAST:
        pose = Pose(eyes="happy", mouth="smile", left_arm=(-20, 0), right_arm=(20, 0))
    else:
        pose = Pose(eyes="happy", mouth="grin", left_arm=HANDS_ON_HIPS_LEFT_ARM, right_arm=HANDS_ON_HIPS_RIGHT_ARM)

    Milo(hip=STAND_HIP).draw(painter=painter, pose=pose, before_arms=lambda skeleton: paint_worn_scarf(painter=painter, skeleton=skeleton))

    if form == PAST:
        paint_past_clock(painter=painter, center=(810, 250))
    elif form != INFINITIVE:
        draw_check_mark(painter=painter, center=(800, 330), size=44)


def paint_worn_scarf(
    painter,
    skeleton,
):
    """A band around the neck and one tail that hangs down the middle of the shirt."""
    neck_x, neck_y = skeleton.neck
    painter.fill_ellipse(center=(neck_x, neck_y + 8), radius_x=66, radius_y=24, shade=solid(SCARF_COLOR))
    tail = [(-14, 12), (34, 12), (40, 118), (-6, 118)]
    painter.fill_polygon(points=[(neck_x + x, neck_y + y) for x, y in tail], shade=solid(SCARF_DARK))
    painter.flat_polygon(
        points=[(neck_x + x, neck_y + y) for x, y in [(-3, 84), (38, 84), (39, 98), (-4, 98)]],
        color=SCARF_STRIPE,
    )


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="wear", paint_scene=paint_wear_scene)
