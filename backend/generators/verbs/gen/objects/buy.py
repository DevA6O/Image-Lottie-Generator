"""
Scene for the irregular verb "buy" (bought, bought).
Output: buy_infinitive.png, buy_past.png and buy_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import GOLD, draw_arrow, draw_coin, draw_heart, draw_shopping_bag, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock


def paint_buy_scene(painter, form):
    skeleton = Milo(hip=(440, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(40, 20), eyes="happy", mouth="grin"))
    draw_shopping_bag(painter=painter, center=(skeleton.right_hand[0] + 6, skeleton.right_hand[1] + 70), size=0.85)

    if form == INFINITIVE:
        draw_coin(painter=painter, center=(760, 360), radius=48)
        draw_arrow(painter=painter, start=(700, 440), end=(600, 540), color=GOLD, width=18)
    elif form == PAST:
        draw_coin(painter=painter, center=(760, 640), radius=44)
        draw_coin(painter=painter, center=(820, 720), radius=34)
        paint_past_clock(painter=painter, center=(760, 250))
    else:
        draw_heart(painter=painter, center=(760, 440), size=44)
        draw_sparkle(painter=painter, center=(300, 380), size=32)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="buy", paint_scene=paint_buy_scene)
