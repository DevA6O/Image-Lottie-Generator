"""
Scene for the irregular verb "make" (made, made).
Output: make_infinitive.png, make_past.png and make_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import CHEER_POSE
from painting.flat_painter import solid
from verbs.props import BLUE, GREEN, RED, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, PAST, paint_past_clock

BRICK_COLORS = (RED, BLUE, GREEN)
MILO_HIP = (430, 620)
PLACING_ARM = (75, 0)    # Straight, the hand carries a brick toward the stack
HELD_BRICK_SIZE = 0.5
HELD_BRICK_OFFSET_FROM_HAND = (35, -15)
STACK_CENTER_X = 740
STACK_BOTTOM_CENTER_Y = 796
BRICK_HEIGHT_STEP = 90


def _draw_lego_brick(
    painter,
    center,
    color,
    size=1.0,
):
    painter.fill_rounded_rect(
        box=(center[0] - 90 * size, center[1] - 40 * size, center[0] + 90 * size, center[1] + 40 * size),
        radius=8 * size,
        shade=solid(color),
    )

    for offset in (-54, 0, 54):
        painter.fill_rounded_rect(
            box=(center[0] + (offset - 20) * size, center[1] - 62 * size, center[0] + (offset + 20) * size, center[1] - 38 * size),
            radius=8 * size,
            shade=solid(color),
        )


def paint_make_scene(painter, form):
    for index in range(form + 1):
        _draw_lego_brick(painter=painter, center=(STACK_CENTER_X, STACK_BOTTOM_CENTER_Y - index * BRICK_HEIGHT_STEP), color=BRICK_COLORS[index])

    if form == INFINITIVE:
        builder = Milo(hip=MILO_HIP)
        pose = Pose(left_arm=(-14, 0), right_arm=PLACING_ARM, eyes="happy", mouth="grin")
        hand = builder.build_skeleton(pose=pose).right_hand
        brick_center = (hand[0] + HELD_BRICK_OFFSET_FROM_HAND[0], hand[1] + HELD_BRICK_OFFSET_FROM_HAND[1])
        _draw_lego_brick(painter=painter, center=brick_center, color=BRICK_COLORS[form + 1], size=HELD_BRICK_SIZE)
        builder.draw(painter=painter, pose=pose)
    elif form == PAST:
        Milo(hip=MILO_HIP).draw(painter=painter, pose=Pose(eyes="happy", mouth="grin"))
        paint_past_clock(painter=painter, center=(STACK_CENTER_X, 440))
    else:
        Milo(hip=MILO_HIP).draw(painter=painter, pose=CHEER_POSE)
        draw_star(painter=painter, center=(STACK_CENTER_X, 440), size=40)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="make", paint_scene=paint_make_scene)
