"""
Scene for the irregular verb "say" (said, said).
Output: say_infinitive.png, say_past.png and say_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from verbs.props import draw_check_mark, draw_heart, draw_speech_bubble, draw_text_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

BUBBLE_CENTER = (430, 140)


def paint_say_scene(painter, form):
    Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(100, 20), mouth="open", head_tilt=-4))
    draw_speech_bubble(painter=painter, center=BUBBLE_CENTER, width=420, height=150, tail_tip=(450, 246))

    if form == INFINITIVE:
        draw_text_lines(painter=painter, center=BUBBLE_CENTER, width=300, count=2)
    elif form == PAST:
        draw_heart(painter=painter, center=BUBBLE_CENTER, size=50)
        paint_past_clock(painter=painter, center=(820, 230))
    else:
        draw_check_mark(painter=painter, center=BUBBLE_CENTER, size=46)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="say", paint_scene=paint_say_scene)
