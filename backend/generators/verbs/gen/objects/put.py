"""
Scene for the irregular verb "put" (put, put).
Output: put_infinitive.png, put_past.png and put_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from painting.flat_painter import solid
from verbs.props import BLUE, BROWN, WOOD, draw_arrow, draw_check_mark, draw_gift_box
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, PAST, paint_past_clock

MILO_HIP = (380, 620)
HOLDING_ARM = (82, 0)    # Straight, the hand is under the corner of the gift
RELEASING_ARM = (65, 0)    # Straight, the hand is next to the gift on the table
RESTING_ARM = (14, 0)
TABLE_BOX = (560, 600, 900, 636)
TABLE_LEG_XS = (600, 860)
FLOOR_Y = 836
GIFT_SIZE = 0.7
GIFT_OFFSET_FROM_HAND = (35, -30)
GIFT_RESTING_CENTER = (660, 551)    # The box bottom touches the table top


def paint_put_scene(painter, form):
    painter.fill_rounded_rect(box=TABLE_BOX, radius=8, shade=solid(WOOD))

    for leg_x in TABLE_LEG_XS:
        painter.fill_stroke(start=(leg_x, TABLE_BOX[3]), end=(leg_x, FLOOR_Y), width=14, shade=solid(BROWN))

    arm = {INFINITIVE: HOLDING_ARM, PAST: RELEASING_ARM}.get(form, RESTING_ARM)
    putter = Milo(hip=MILO_HIP)
    pose = Pose(left_arm=(-14, 0), right_arm=arm, mouth="smile", eyes="happy")
    hand = putter.build_skeleton(pose=pose).right_hand

    if form == INFINITIVE:
        draw_gift_box(painter=painter, center=(hand[0] + GIFT_OFFSET_FROM_HAND[0], hand[1] + GIFT_OFFSET_FROM_HAND[1]), size=GIFT_SIZE)
        draw_arrow(painter=painter, start=(780, 400), end=(780, 540), color=BLUE)
    else:
        draw_gift_box(painter=painter, center=GIFT_RESTING_CENTER, size=GIFT_SIZE)

    putter.draw(painter=painter, pose=pose)

    if form == PAST:
        paint_past_clock(painter=painter, center=(780, 400))
    elif form == PARTICIPLE:
        draw_check_mark(painter=painter, center=(660, 400), size=40)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="put", paint_scene=paint_put_scene)
