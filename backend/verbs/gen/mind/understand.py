"""
Scene for the irregular verb "understand" (understood, understood).
Output: understand_infinitive.png, understand_past.png and understand_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose, STAND_HIP
from verbs.props import BLUE, GRAY, draw_exclamation_mark, draw_gear, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE


def paint_understand_scene(painter, form):
    pose = Pose(left_arm=(-65, 0), right_arm=(65, 0), eyes="wide", mouth="o", brows="raised")
    Character(hip=STAND_HIP).draw(painter=painter, pose=pose)
    draw_exclamation_mark(painter=painter, center=(512, 190), size=1.2)

    if form != INFINITIVE:
        draw_gear(painter=painter, center=(270, 330), size=0.9, color=GRAY)
        draw_gear(painter=painter, center=(350, 280), size=0.7, color=BLUE)

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(740, 340), size=36)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="understand", paint_scene=paint_understand_scene)
