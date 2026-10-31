"""
Scene for the irregular verb "bring" (brought, brought).
Output: bring_infinitive.png, bring_past.png and bring_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import CARRY_LEFT_ARM, CARRY_RIGHT_ARM
from painting.flat_painter import solid
from verbs.held_gift import paint_held_gift
from verbs.props import BLUE, BROWN, RED, draw_arrow, draw_gift_box, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, paint_past_clock

HOUSE_X = 800


def _draw_house(
    painter,
    bottom_center,
):
    wall_box = (bottom_center[0] - 90, bottom_center[1] - 140, bottom_center[0] + 90, bottom_center[1])
    painter.fill_rounded_rect(box=wall_box, radius=6, shade=solid((246, 226, 190)))
    painter.fill_polygon(
        points=[(wall_box[0] - 20, wall_box[1] + 6), (bottom_center[0], wall_box[1] - 90), (wall_box[2] + 20, wall_box[1] + 6)],
        shade=solid(RED),
    )
    painter.fill_rounded_rect(box=(bottom_center[0] - 24, bottom_center[1] - 80, bottom_center[0] + 24, bottom_center[1]), radius=6, shade=solid(BROWN))


def paint_bring_scene(painter, form):
    _draw_house(painter=painter, bottom_center=(HOUSE_X, 836))

    if form == PARTICIPLE:
        Milo(hip=(440, 620)).draw(painter=painter, pose=Pose(eyes="happy", mouth="grin", left_arm=(-50, 100), right_arm=(50, -100)))
        draw_gift_box(painter=painter, center=(640, 790), size=0.7)
        return

    walking_pose = Pose(
        lean=6,
        left_arm=CARRY_LEFT_ARM,
        right_arm=CARRY_RIGHT_ARM,
        left_leg=(-24, 6),
        right_leg=(26, -14),
        mouth="smile",
    )
    hip_x = 400 if form == INFINITIVE else 470
    Milo(hip=(hip_x, 620)).draw(painter=painter, pose=walking_pose, before_arms=lambda skeleton: paint_held_gift(painter=painter, skeleton=skeleton))

    if form == INFINITIVE:
        draw_arrow(painter=painter, start=(480, 190), end=(680, 190), color=BLUE)
    else:
        draw_wind_lines(painter=painter, origin=(250, 560), length=140, count=3)
        paint_past_clock(painter=painter, center=(760, 250))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="bring", paint_scene=paint_bring_scene)
