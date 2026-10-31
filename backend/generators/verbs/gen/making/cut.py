"""
Scene for the irregular verb "cut" (cut, cut).
Output: cut_infinitive.png, cut_past.png and cut_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from painting.flat_painter import solid
from verbs.props import draw_scissors, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST


def paint_cut_scene(painter, form):
    skeleton = Milo(hip=(380, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 70), eyes="happy", mouth="smile"))
    paper_left, paper_top, paper_right, paper_bottom = 560, 600, 900, 760

    if form == INFINITIVE:
        painter.fill_rounded_rect(box=(paper_left, paper_top, paper_right, paper_bottom), radius=8, shade=solid((250, 250, 255)))
        draw_scissors(painter=painter, pivot=(skeleton.right_hand[0] + 60, skeleton.right_hand[1] - 30), size=0.8, open_angle=20, direction=70)
        return

    gap = 26 if form == PAST else 50
    middle = (paper_left + paper_right) / 2
    painter.fill_rounded_rect(box=(paper_left - gap / 2, paper_top, middle - gap / 2, paper_bottom), radius=8, shade=solid((250, 250, 255)))
    painter.fill_rounded_rect(box=(middle + gap / 2, paper_top, paper_right + gap / 2, paper_bottom), radius=8, shade=solid((250, 250, 255)))

    if form == PAST:
        draw_scissors(painter=painter, pivot=(middle, paper_top - 60), size=0.8, open_angle=8, direction=90)
    else:
        draw_sparkle(painter=painter, center=(middle, paper_top - 80), size=36)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="cut", paint_scene=paint_cut_scene)
