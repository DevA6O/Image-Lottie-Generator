"""
Scene for the irregular verb "see" (saw, seen).
Output: see_infinitive.png, see_past.png and see_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from verbs.props import draw_check_mark, draw_exclamation_mark, draw_eye, draw_speech_bubble, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock


def paint_see_scene(painter, form):
    if form == INFINITIVE:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(40, 185), eyes="wide", mouth="o"))
        draw_eye(painter=painter, center=(512, 140), size=1.0)
    elif form == PAST:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-65, 0), right_arm=(65, 0), eyes="wide", mouth="o", brows="raised"))
        draw_star(painter=painter, center=(740, 330), size=60)
        draw_exclamation_mark(painter=painter, center=(290, 340), size=0.9)
        paint_past_clock(painter=painter, center=(800, 150))
    else:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(50, -100), eyes="happy", mouth="smile"))
        draw_speech_bubble(painter=painter, center=(430, 140), width=380, height=150, tail_tip=(470, 246))
        draw_eye(painter=painter, center=(360, 140), size=0.5)
        draw_check_mark(painter=painter, center=(520, 145), size=36)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="see", paint_scene=paint_see_scene)
