"""
A gift held in front of the belly. Pair it with CARRY_LEFT_ARM and CARRY_RIGHT_ARM: the hands grip the sides of the box.
"""
from verbs.props import draw_gift_box

HELD_GIFT_OFFSET_Y = -5
HELD_GIFT_SIZE = 0.8


def paint_held_gift(
    painter,
    skeleton,
):
    """Use it as `before_arms`, so the hands are painted on top of the box."""
    hands_middle_x = (skeleton.left_hand[0] + skeleton.right_hand[0]) / 2
    draw_gift_box(painter=painter, center=(hands_middle_x, skeleton.left_hand[1] + HELD_GIFT_OFFSET_Y), size=HELD_GIFT_SIZE)
