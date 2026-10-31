"""
Scene for the irregular verb "put" (put, put).
Output: put_infinitive.png, put_past.png and put_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from painting.flat_painter import solid
from verbs.props import BLUE, BROWN, WOOD, draw_arrow, draw_gift_box, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE


def paint_put_scene(painter, form):
    painter.fill_rounded_rect(box=(620, 600, 920, 636), radius=8, shade=solid(WOOD))
    painter.fill_stroke(start=(660, 636), end=(660, 760), width=14, shade=solid(BROWN))
    painter.fill_stroke(start=(880, 636), end=(880, 760), width=14, shade=solid(BROWN))
    Milo(hip=(380, 620)).draw(painter=painter, pose=Pose(left_arm=(80, 30), right_arm=(100, 20), mouth="smile"))

    if form == INFINITIVE:
        draw_gift_box(painter=painter, center=(640, 380), size=0.7)
        draw_arrow(painter=painter, start=(760, 340), end=(760, 470), color=BLUE)
    else:
        draw_gift_box(painter=painter, center=(770, 540), size=0.7)

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(880, 420), size=32)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="put", paint_scene=paint_put_scene)
