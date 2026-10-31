"""
Scene for the irregular verb "give" (gave, given).
Output: give_infinitive.png, give_past.png and give_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.partner import build_partner
from verbs.props import PINK, draw_gift_box, draw_heart
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

FORWARD_LEFT_ARM = (65, 35)
FORWARD_RIGHT_ARM = (95, 10)


def paint_give_scene(painter, form):
    if form == INFINITIVE:
        skeleton = Milo(hip=(360, 620)).draw(painter=painter, pose=Pose(mouth="smile", left_arm=FORWARD_LEFT_ARM, right_arm=FORWARD_RIGHT_ARM))
        draw_gift_box(painter=painter, center=(skeleton.right_hand[0] + 20, skeleton.right_hand[1] - 40), size=0.8)
        draw_heart(painter=painter, center=(560, 300), size=36)
    elif form == PAST:
        Milo(hip=(300, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 0), mouth="smile"))
        build_partner(hip=(760, 650)).draw(painter=painter, pose=Pose(left_arm=(-105, 0), right_arm=(100, 0), eyes="wide", mouth="o", brows="raised"))
        draw_gift_box(painter=painter, center=(580, 440), size=0.7)
        paint_past_clock(painter=painter, center=(520, 200))
    else:
        Milo(hip=(250, 670), scale=0.75).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(150, 40), eyes="happy", mouth="grin"))
        build_partner(hip=(620, 620)).draw(painter=painter, pose=Pose(left_arm=(-20, 70), right_arm=(20, -70), eyes="happy", mouth="grin"))
        draw_gift_box(painter=painter, center=(620, 660), size=0.7)
        draw_heart(painter=painter, center=(780, 300), size=40)
        draw_heart(painter=painter, center=(470, 330), size=24, color=PINK)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="give", paint_scene=paint_give_scene)
