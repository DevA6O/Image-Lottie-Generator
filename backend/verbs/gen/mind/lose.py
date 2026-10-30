"""
Scene for the irregular verb "lose" (lost, lost).
Output: lose_infinitive.png, lose_past.png and lose_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose, STAND_HIP
from verbs.props import draw_coin, draw_key, draw_question_mark, draw_sweat_drop
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST


def paint_lose_scene(painter, form):
    pose = Pose(left_arm=(-70, 40), right_arm=(70, -40), eyes="wide", mouth="sad", brows="worry")
    Character(hip=STAND_HIP).draw(painter=painter, pose=pose)
    draw_question_mark(painter=painter, center=(512, 190), size=1.0)

    if form == INFINITIVE:
        draw_coin(painter=painter, center=(300, 640), radius=44)
        draw_coin(painter=painter, center=(240, 740), radius=34)
    elif form == PAST:
        draw_key(painter=painter, center=(250, 650), size=0.9)
        draw_sweat_drop(painter=painter, center=(700, 330))
    else:
        draw_sweat_drop(painter=painter, center=(700, 330))
        draw_sweat_drop(painter=painter, center=(330, 360), radius=11)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="lose", paint_scene=paint_lose_scene)
