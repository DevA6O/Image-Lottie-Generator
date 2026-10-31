"""
Scene for the irregular verb "come" (came, come).
Output: come_infinitive.png, come_past.png and come_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import CHEER_POSE
from verbs.props import BLUE, draw_arrow, draw_footprints, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE


def paint_come_scene(painter, form):

    if form == PARTICIPLE:
        Milo(hip=(512, 600)).draw(painter=painter, pose=CHEER_POSE)
        draw_sparkle(painter=painter, center=(250, 400), size=40)
        draw_sparkle(painter=painter, center=(780, 460), size=34)
        return

    pose = Pose(lean=-4, left_arm=(-14, 0), right_arm=(120, 60), eyes="happy", mouth="smile")
    Milo(hip=(440, 600)).draw(painter=painter, pose=pose)

    if form == INFINITIVE:
        draw_arrow(painter=painter, start=(900, 740), end=(700, 740), color=BLUE)
    else:
        draw_footprints(painter=painter, start=(900, 830), end=(640, 830), count=4)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="come", paint_scene=paint_come_scene)
