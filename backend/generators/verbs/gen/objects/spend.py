"""
Scene for the irregular verb "spend" (spent, spent).
Output: spend_infinitive.png, spend_past.png and spend_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from painting.flat_painter import solid
from verbs.props import BROWN, draw_coin, draw_sweat_drop
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, PARTICIPLE, paint_past_clock

WALLET_HALF_WIDTH = 80
WALLET_HALF_HEIGHT = 50
COIN_RISE = 130


def paint_spend_scene(painter, form):
    is_sad = form == PARTICIPLE
    pose = Pose(left_arm=(-14, 0), right_arm=(100, 20), eyes="wide", mouth="sad" if is_sad else "open", brows="worry" if is_sad else "none")
    skeleton = Milo(hip=(360, 620)).draw(painter=painter, pose=pose)
    wallet_center = (skeleton.right_hand[0] + 20, skeleton.right_hand[1] + WALLET_HALF_HEIGHT + 10)
    paint_wallet(painter=painter, center=wallet_center)

    if form == PARTICIPLE:
        draw_sweat_drop(painter=painter, center=(480, 330))
        return

    coin_count = 2 if form == INFINITIVE else 4

    for index in range(coin_count):
        coin_center = (wallet_center[0] - 20 + index * 70, wallet_center[1] - COIN_RISE - (index % 2) * 70)
        draw_coin(painter=painter, center=coin_center, radius=36)

    if form == PAST:
        paint_past_clock(painter=painter, center=(200, 170))


def paint_wallet(
    painter,
    center,
):
    box = (center[0] - WALLET_HALF_WIDTH, center[1] - WALLET_HALF_HEIGHT, center[0] + WALLET_HALF_WIDTH, center[1] + WALLET_HALF_HEIGHT)
    painter.fill_rounded_rect(box=box, radius=14, shade=solid(BROWN))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="spend", paint_scene=paint_spend_scene)
