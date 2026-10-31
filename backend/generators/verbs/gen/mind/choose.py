"""
Scene for the irregular verb "choose" (chose, chosen).
Output: choose_infinitive.png, choose_past.png and choose_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import ORANGE, RED, WHITE, draw_check_mark, draw_question_mark, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST


def paint_choose_scene(painter, form):
    pose = Pose(left_arm=(-30, 150), right_arm=(100, 0), eyes="side", mouth="flat", brows="raised")
    Milo(hip=(400, 620)).draw(painter=painter, pose=pose)
    painter.fill_circle(center=(250, 330), radius=70, shade=((ORANGE), (ORANGE)))
    painter.fill_circle(center=(740, 520), radius=90, shade=((RED), (RED)))

    if form == INFINITIVE:
        draw_question_mark(painter=painter, center=(520, 220), size=0.9)
    elif form == PAST:
        draw_check_mark(painter=painter, center=(740, 520), size=50, color=WHITE)
    else:
        draw_check_mark(painter=painter, center=(740, 520), size=50, color=WHITE)
        draw_star(painter=painter, center=(740, 400), size=36)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="choose", paint_scene=paint_choose_scene)
