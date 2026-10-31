"""
Scene for the irregular verb "find" (found, found).
Output: find_infinitive.png, find_past.png and find_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from verbs.props import BLUE, draw_exclamation_mark, draw_magnifier, draw_question_mark, draw_sparkle, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE


def paint_find_scene(painter, form):

    if form == PARTICIPLE:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-150, 0), right_arm=(150, 0), eyes="happy", mouth="grin"))
        draw_star(painter=painter, center=(300, 330), size=60)
        draw_sparkle(painter=painter, center=(740, 360), size=34)
        return

    skeleton = Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(60, 90), eyes="wide", mouth="o"))
    lens_center = (skeleton.right_hand[0] + 70, skeleton.right_hand[1] - 20)
    draw_magnifier(painter=painter, center=lens_center, radius=70, handle_angle=135)

    if form == INFINITIVE:
        draw_question_mark(painter=painter, center=lens_center, size=0.7, color=BLUE)
    else:
        draw_star(painter=painter, center=lens_center, size=40)
        draw_exclamation_mark(painter=painter, center=(300, 400), size=0.9)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="find", paint_scene=paint_find_scene)
