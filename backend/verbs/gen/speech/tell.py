"""
Scene for the irregular verb "tell" (told, told).
Output: tell_infinitive.png, tell_past.png and tell_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose, build_partner
from verbs.props import draw_exclamation_mark, draw_lightbulb, draw_speech_bubble, draw_text_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST


def paint_tell_scene(painter, form):
    Character(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(110, 10), mouth="open"))
    build_partner(hip=(720, 650)).draw(painter=painter, pose=Pose(eyes="wide", mouth="o", brows="raised", left_arm=(-24, 10)))
    draw_speech_bubble(painter=painter, center=(500, 200), width=360, height=160, tail_tip=(430, 320))

    if form == INFINITIVE:
        draw_exclamation_mark(painter=painter, center=(500, 200), size=0.9)
    elif form == PAST:
        draw_text_lines(painter=painter, center=(500, 200), width=260, count=2)
    else:
        draw_lightbulb(painter=painter, center=(720, 230), size=0.7)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="tell", paint_scene=paint_tell_scene)
