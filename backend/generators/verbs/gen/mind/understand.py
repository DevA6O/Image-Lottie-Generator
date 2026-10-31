"""
Scene for the irregular verb "understand" (understood, understood).
Output: understand_infinitive.png, understand_past.png and understand_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from verbs.props import draw_check_mark, draw_exclamation_mark, draw_lightbulb, draw_question_mark
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

IDEA_CENTER = (280, 330)
SIGN_CENTER = (740, 330)


def paint_understand_scene(painter, form):
    if form == INFINITIVE:
        confused_pose = Pose(head_tilt=-6, left_arm=(-60, 0), right_arm=(60, 0), eyes="up", mouth="flat", brows="worry")
        Milo(hip=STAND_HIP).draw(painter=painter, pose=confused_pose)
        draw_question_mark(painter=painter, center=(512, 190), size=1.0)
    elif form == PAST:
        surprised_pose = Pose(left_arm=(-65, 0), right_arm=(65, 0), eyes="wide", mouth="o", brows="raised")
        Milo(hip=STAND_HIP).draw(painter=painter, pose=surprised_pose)
        draw_lightbulb(painter=painter, center=IDEA_CENTER, size=0.8)
        draw_exclamation_mark(painter=painter, center=SIGN_CENTER, size=1.0)
        paint_past_clock(painter=painter, center=(512, 170))
    else:
        hands_on_hips_pose = Pose(left_arm=(-50, 100), right_arm=(50, -100), eyes="happy", mouth="grin")
        Milo(hip=STAND_HIP).draw(painter=painter, pose=hands_on_hips_pose)
        draw_lightbulb(painter=painter, center=IDEA_CENTER, size=0.8)
        draw_check_mark(painter=painter, center=SIGN_CENTER, size=44)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="understand", paint_scene=paint_understand_scene)
