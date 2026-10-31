"""
Scene for the irregular verb "do" (did, done).
Output: do_infinitive.png, do_past.png and do_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import draw_clipboard, draw_pencil, draw_trophy
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE


def paint_do_scene(painter, form):
    skeleton = Milo(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 90), eyes="closed", mouth="smile"))
    draw_clipboard(painter=painter, center=(740, 580), width=260, height=360, row_count=3, checked_count=(0, 2, 3)[form])
    draw_pencil(painter=painter, tip=(skeleton.right_hand[0] + 30, skeleton.right_hand[1] + 30), angle=-50)

    if form == PARTICIPLE:
        draw_trophy(painter=painter, center=(740, 280), size=0.7)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="do", paint_scene=paint_do_scene)
