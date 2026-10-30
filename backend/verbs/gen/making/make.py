"""
Scene for the irregular verb "make" (made, made).
Output: make_infinitive.png, make_past.png and make_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import BLUE, GREEN, RED, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE
from verbs.verb_painter import solid

BRICK_COLORS = (RED, BLUE, GREEN)


def _draw_lego_brick(
    painter,
    center,
    color,
):
    painter.fill_rounded_rect(box=(center[0] - 90, center[1] - 40, center[0] + 90, center[1] + 40), radius=8, shade=solid(color))

    for offset in (-54, 0, 54):
        painter.fill_rounded_rect(box=(center[0] + offset - 20, center[1] - 62, center[0] + offset + 20, center[1] - 38), radius=8, shade=solid(color))


def paint_make_scene(painter, form):
    Character(hip=(380, 620)).draw(painter=painter, pose=Pose(left_arm=(70, 100), right_arm=(100, 60), eyes="happy", mouth="grin"))
    brick_count = form + 1

    for index in range(brick_count):
        _draw_lego_brick(painter=painter, center=(720, 800 - index * 90), color=BRICK_COLORS[index])

    if form == PARTICIPLE:
        draw_star(painter=painter, center=(720, 480), size=40)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="make", paint_scene=paint_make_scene)
