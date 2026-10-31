"""
Scene for the irregular verb "take" (took, taken).
Output: take_infinitive.png, take_past.png and take_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import CARRY_LEFT_ARM, CARRY_RIGHT_ARM
from painting.flat_painter import solid
from verbs.held_gift import paint_held_gift
from verbs.props import WOOD, draw_gift_box, draw_heart, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

MILO_HIP = (330, 620)
REACHING_ARM = (95, 0)    # Straight, the hand touches the side of the gift on the shelf
GIFT_SIZE_ON_SHELF = 0.75
GIFT_CENTER_ON_SHELF = (610, 462)
SHELF_TOP_Y = 514
SHELF_HALF_WIDTH = 140


def paint_take_scene(painter, form):
    shelf_box = (GIFT_CENTER_ON_SHELF[0] - SHELF_HALF_WIDTH, SHELF_TOP_Y, GIFT_CENTER_ON_SHELF[0] + SHELF_HALF_WIDTH, SHELF_TOP_Y + 30)
    painter.fill_rounded_rect(box=shelf_box, radius=8, shade=solid(WOOD))

    if form == INFINITIVE:
        draw_gift_box(painter=painter, center=GIFT_CENTER_ON_SHELF, size=GIFT_SIZE_ON_SHELF)
        Milo(hip=MILO_HIP).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=REACHING_ARM, eyes="side", mouth="open"))
        return

    pose = Pose(left_arm=CARRY_LEFT_ARM, right_arm=CARRY_RIGHT_ARM, eyes="happy", mouth="grin")
    Milo(hip=MILO_HIP).draw(painter=painter, pose=pose, before_arms=lambda skeleton: paint_held_gift(painter=painter, skeleton=skeleton))

    if form == PAST:
        paint_past_clock(painter=painter, center=(800, 300))
    else:
        draw_heart(painter=painter, center=(800, 300), size=40)
        draw_sparkle(painter=painter, center=(640, 330), size=30)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="take", paint_scene=paint_take_scene)
