"""
Scene for the irregular verb "sit" (sat, sat).
Output: sit_infinitive.png, sit_past.png and sit_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import BLUE, WHITE, draw_arrow, draw_chair, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST

SITTING_LEFT_LEG = (-35, 35)
SITTING_RIGHT_LEG = (35, -35)


def paint_sit_scene(painter, form):
    draw_chair(painter=painter, seat_center=(512, 700))

    if form == INFINITIVE:
        Milo(hip=(512, 590)).draw(painter=painter, pose=Pose(mouth="open", left_leg=SITTING_LEFT_LEG, right_leg=SITTING_RIGHT_LEG))
        draw_arrow(painter=painter, start=(820, 460), end=(820, 640), color=BLUE)
    elif form == PAST:
        Milo(hip=(512, 640)).draw(painter=painter, pose=Pose(eyes="happy", left_leg=SITTING_LEFT_LEG, right_leg=SITTING_RIGHT_LEG))
    else:
        relaxed_pose = Pose(left_arm=(-24, 10), right_arm=(24, -10), eyes="closed", mouth="smile", left_leg=SITTING_LEFT_LEG, right_leg=SITTING_RIGHT_LEG)
        Milo(hip=(512, 640)).draw(painter=painter, pose=relaxed_pose)
        draw_sparkle(painter=painter, center=(790, 520), size=34, color=WHITE)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="sit", paint_scene=paint_sit_scene)
