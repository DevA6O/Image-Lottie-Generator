"""
Scene for the irregular verb "find" (found, found).
Output: find_infinitive.png, find_past.png and find_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from painting.flat_painter import move_point
from verbs.props import BLUE, draw_exclamation_mark, draw_magnifier, draw_question_mark, draw_sparkle, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, paint_past_clock

SEARCHING_ARM = (110, 0)    # Straight, the hand grips the end of the handle
LENS_RADIUS = 70
HANDLE_LENGTH_IN_FRONT_OF_HAND = 80


def paint_find_scene(painter, form):

    if form == PARTICIPLE:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-150, 0), right_arm=(150, 0), eyes="happy", mouth="grin"))
        draw_star(painter=painter, center=(300, 330), size=60)
        draw_sparkle(painter=painter, center=(740, 360), size=34)
        return

    skeleton = Milo(hip=(400, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=SEARCHING_ARM, eyes="side", mouth="o"))
    lens_center = move_point(point=skeleton.right_hand, angle=-45, distance=LENS_RADIUS + HANDLE_LENGTH_IN_FRONT_OF_HAND)
    draw_magnifier(painter=painter, center=lens_center, radius=LENS_RADIUS, handle_angle=135)

    if form == INFINITIVE:
        draw_question_mark(painter=painter, center=lens_center, size=0.7, color=BLUE)
    else:
        draw_star(painter=painter, center=lens_center, size=40)
        draw_exclamation_mark(painter=painter, center=(240, 400), size=0.9)
        paint_past_clock(painter=painter, center=(840, 190))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="find", paint_scene=paint_find_scene)
