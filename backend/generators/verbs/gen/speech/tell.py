"""
Scene for the irregular verb "tell" (told, told).
Output: tell_infinitive.png, tell_past.png and tell_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.partner import build_partner
from verbs.props import draw_exclamation_mark, draw_lightbulb, draw_speech_bubble, draw_text_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

BUBBLE_CENTER = (500, 150)


def paint_tell_scene(painter, form):
    Milo(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(110, 10), mouth="open"))
    build_partner(hip=(720, 650)).draw(painter=painter, pose=Pose(eyes="wide", mouth="o", brows="raised", left_arm=(-24, 10)))
    draw_speech_bubble(painter=painter, center=BUBBLE_CENTER, width=360, height=140, tail_tip=(430, 246))

    if form == INFINITIVE:
        draw_exclamation_mark(painter=painter, center=BUBBLE_CENTER, size=0.8)
    elif form == PAST:
        draw_text_lines(painter=painter, center=BUBBLE_CENTER, width=260, count=2)
        paint_past_clock(painter=painter, center=(900, 170))
    else:
        draw_text_lines(painter=painter, center=BUBBLE_CENTER, width=260, count=2)
        draw_lightbulb(painter=painter, center=(880, 330), size=0.8)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="tell", paint_scene=paint_tell_scene)
