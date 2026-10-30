"""
Scene for the irregular verb "spend" (spent, spent).
Output: spend_infinitive.png, spend_past.png and spend_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import BROWN, draw_coin, draw_sweat_drop
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE
from verbs.verb_painter import solid


def paint_spend_scene(painter, form):
    pose = Pose(left_arm=(-14, 0), right_arm=(70, 100), eyes="wide", mouth="open") if form != PARTICIPLE else Pose(left_arm=(-70, 40), right_arm=(70, -40), eyes="wide", mouth="sad", brows="worry")
    skeleton = Character(hip=(400, 620)).draw(painter=painter, pose=pose)

    if form == PARTICIPLE:
        draw_sweat_drop(painter=painter, center=(540, 330))
        draw_coin(painter=painter, center=(780, 700), radius=36)
        return

    wallet_center = (skeleton.right_hand[0] + 20, skeleton.right_hand[1] + 40)
    painter.fill_rounded_rect(
        box=(wallet_center[0] - 80, wallet_center[1] - 50, wallet_center[0] + 80, wallet_center[1] + 50),
        radius=14,
        shade=solid(BROWN),
    )

    for index in range(2 if form == INFINITIVE else 4):
        draw_coin(painter=painter, center=(wallet_center[0] + 40 + index * 70, wallet_center[1] - 150 - (index % 2) * 70), radius=36)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="spend", paint_scene=paint_spend_scene)
