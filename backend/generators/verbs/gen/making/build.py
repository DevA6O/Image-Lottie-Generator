"""
Scene for the irregular verb "build" (built, built).
Output: build_infinitive.png, build_past.png and build_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import draw_brick_wall, draw_hammer, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE


def paint_build_scene(painter, form):
    skeleton = Milo(hip=(330, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 100), eyes="happy", mouth="grin"))
    draw_hammer(painter=painter, center=(skeleton.right_hand[0] + 10, skeleton.right_hand[1] - 20), size=0.8, angle=-60)
    draw_brick_wall(painter=painter, left_bottom=(560, 836), column_count=3, row_count=(1, 3, 5)[form])

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(700, 260), size=36)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="build", paint_scene=paint_build_scene)
