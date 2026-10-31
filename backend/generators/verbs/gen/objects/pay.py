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
from verbs.tense import INFINITIVE, PAST


def paint_pay_scene(painter, form):
    Milo(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(110, 20), mouth="smile"))
    partner = build_partner(hip=(720, 640))
    partner_skeleton = partner.draw(painter=painter, pose=Pose(left_arm=(-100, 20), right_arm=(14, 0), mouth="smile"))

    if form == INFINITIVE:
        draw_coin(painter=painter, center=(520, 420), radius=44)
        draw_arrow(painter=painter, start=(470, 340), end=(600, 340), color=BLUE, width=18)
    elif form == PAST:
        draw_coin(painter=painter, center=(partner_skeleton.left_hand[0] - 20, partner_skeleton.left_hand[1] - 40), radius=40)
    else:
        draw_coin(painter=painter, center=(partner_skeleton.left_hand[0] - 20, partner_skeleton.left_hand[1] - 40), radius=40)
        draw_heart(painter=painter, center=(520, 300), size=34)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="pay", paint_scene=paint_pay_scene)
