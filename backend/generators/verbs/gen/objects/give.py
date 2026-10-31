"""
Scene for the irregular verb "give" (gave, given).
Output: give_infinitive.png, give_past.png and give_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import CARRY_LEFT_ARM, CARRY_RIGHT_ARM
from verbs.held_gift import paint_held_gift
from verbs.partner import build_partner
from verbs.props import PINK, draw_gift_box, draw_heart
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

OFFERING_ARM = (88, 0)    # Straight, the hand is under the corner of the gift
GIFT_SIZE = 0.8
GIFT_OFFSET_FROM_HAND = (35, -30)


def paint_give_scene(painter, form):
    if form == INFINITIVE:
        paint_giver_with_gift(painter=painter, giver=Milo(hip=(330, 620)))
        draw_heart(painter=painter, center=(640, 250), size=36)
    elif form == PAST:
        paint_giver_with_gift(painter=painter, giver=Milo(hip=(290, 620)))
        receiver_pose = Pose(left_arm=(-OFFERING_ARM[0], 0), eyes="happy", mouth="grin", brows="raised")
        build_partner(hip=(772, 620)).draw(painter=painter, pose=receiver_pose)
        paint_past_clock(painter=painter, center=(531, 230))
    else:
        Milo(hip=(250, 661), scale=0.75).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(130, 0), eyes="happy", mouth="grin"))
        receiver_pose = Pose(left_arm=CARRY_LEFT_ARM, right_arm=CARRY_RIGHT_ARM, eyes="happy", mouth="grin")
        build_partner(hip=(620, 620)).draw(painter=painter, pose=receiver_pose, before_arms=lambda skeleton: paint_held_gift(painter=painter, skeleton=skeleton))
        draw_heart(painter=painter, center=(780, 300), size=40)
        draw_heart(painter=painter, center=(470, 330), size=24, color=PINK)


def paint_giver_with_gift(
    painter,
    giver,
):
    pose = Pose(mouth="smile", eyes="happy", right_arm=OFFERING_ARM)
    hand = giver.build_skeleton(pose=pose).right_hand
    draw_gift_box(painter=painter, center=(hand[0] + GIFT_OFFSET_FROM_HAND[0], hand[1] + GIFT_OFFSET_FROM_HAND[1]), size=GIFT_SIZE)
    giver.draw(painter=painter, pose=pose)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="give", paint_scene=paint_give_scene)
