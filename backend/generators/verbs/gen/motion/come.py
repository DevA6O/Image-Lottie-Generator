"""
Scene for the irregular verb "come" (came, come).
Output: come_infinitive.png, come_past.png and come_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import CHEER_POSE
from verbs.props import BLUE, draw_check_mark, draw_door, draw_footprints, draw_sound_waves
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

DOOR_BOTTOM_CENTER = (720, 836)
DOOR_WIDTH = 150
DOOR_HEIGHT = 320
KNOCKING_ARM = (62, 0)    # Straight, the fist reaches the door at chest height


def paint_come_scene(painter, form):
    draw_door(painter=painter, bottom_center=DOOR_BOTTOM_CENTER, width=DOOR_WIDTH, height=DOOR_HEIGHT, is_open=form == PAST)

    if form == INFINITIVE:
        knocking_pose = Pose(left_arm=(-14, 0), right_arm=KNOCKING_ARM, eyes="happy", mouth="smile")
        skeleton = Milo(hip=(410, 620)).draw(painter=painter, pose=knocking_pose)
        draw_sound_waves(painter=painter, center=(skeleton.right_hand[0] + 10, skeleton.right_hand[1] - 70), size=0.45, facing=1, color=BLUE)
    elif form == PAST:
        Milo(hip=(380, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(125, 30), eyes="happy", mouth="smile"))
        draw_footprints(painter=painter, start=(600, 840), end=(480, 840), count=3)
        paint_past_clock(painter=painter, center=(720, 390))
    else:
        Milo(hip=(380, 620)).draw(painter=painter, pose=CHEER_POSE)
        draw_check_mark(painter=painter, center=(720, 330), size=44)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="come", paint_scene=paint_come_scene)
