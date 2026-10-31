"""
Scene for the irregular verb "pay" (paid, paid).
Output: pay_infinitive.png, pay_past.png and pay_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.partner import build_partner
from verbs.props import BLUE, draw_arrow, draw_coin, draw_heart
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

COIN_RADIUS = 34
HAND_TO_COIN = 22    # The coin sits between the fingertips, so it reaches a little over the hand


def paint_pay_scene(painter, form):
    giver = Milo(hip=(330, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(95, 0), mouth="smile"))
    receiver = build_partner(hip=(790, 620)).draw(painter=painter, pose=Pose(left_arm=(-95, 0), right_arm=(14, 0), mouth="smile"))
    giver_hand = giver.right_hand
    receiver_hand = receiver.left_hand

    if form == INFINITIVE:
        draw_coin(painter=painter, center=(giver_hand[0] + HAND_TO_COIN, giver_hand[1]), radius=COIN_RADIUS)
        draw_arrow(painter=painter, start=(520, 330), end=(660, 330), color=BLUE, width=18)
    elif form == PAST:
        draw_coin(painter=painter, center=((giver_hand[0] + receiver_hand[0]) / 2, giver_hand[1]), radius=COIN_RADIUS)
        paint_past_clock(painter=painter, center=(560, 200))
    else:
        draw_coin(painter=painter, center=(receiver_hand[0] - HAND_TO_COIN, receiver_hand[1]), radius=COIN_RADIUS)
        draw_heart(painter=painter, center=(560, 280), size=36)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="pay", paint_scene=paint_pay_scene)
