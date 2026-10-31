"""
Scene for the irregular verb "fall" (fell, fallen).
Output: fall_infinitive.png, fall_past.png and fall_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import draw_arrow, draw_ice_patch, draw_star, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

ICE_SIZE = 1.5
WIND_ORIGIN = (345, 590)      # Left of Milo, so the lines trail behind him
WIND_LENGTH = 150
ICE_ABOVE_GROUND = 28      # The ice patch is flat, so its middle sits a little above the soles of the shoes
FOOT_BOTTOM_OFFSET = 27      # From the ankle down to the sole of the shoe


def paint_fall_scene(painter, form):
    if form == INFINITIVE:
        slipping_pose = Pose(lean=-18, head_tilt=-6, left_arm=(-125, 0), right_arm=(135, 0), left_leg=(-10, 0), right_leg=(75, -15), eyes="wide", mouth="open", brows="worry")
        character = Milo(hip=(440, 590))
        skeleton = character.build_skeleton(pose=slipping_pose)
        ground_y = skeleton.left_foot[1] + FOOT_BOTTOM_OFFSET
        ice_center = ((skeleton.left_foot[0] + skeleton.right_foot[0]) / 2, ground_y - ICE_ABOVE_GROUND)
        draw_ice_patch(painter=painter, center=ice_center, size=ICE_SIZE)
        draw_wind_lines(painter=painter, origin=WIND_ORIGIN, length=WIND_LENGTH, count=3)
        character.draw(painter=painter, pose=slipping_pose)
    elif form == PAST:
        falling_pose = Pose(lean=-50, head_tilt=-8, left_arm=(-75, 0), right_arm=(150, 0), left_leg=(-30, 0), right_leg=(40, -30), eyes="wide", mouth="open", brows="worry")
        Milo(hip=(480, 570)).draw(painter=painter, pose=falling_pose)

        for x in (690, 770, 850):
            draw_arrow(painter=painter, start=(x, 380), end=(x, 500), color=(140, 172, 220), width=12)

        paint_past_clock(painter=painter, center=(800, 220))
    else:
        lying_pose = Pose(lean=-88, left_arm=(60, 0), right_arm=(120, 0), left_leg=(80, 0), right_leg=(96, 0), eyes="closed", mouth="open")
        Milo(hip=(640, 740)).draw(painter=painter, pose=lying_pose)

        for center, size in (((260, 560), 26), ((340, 500), 20), ((200, 650), 18)):
            draw_star(painter=painter, center=center, size=size)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="fall", paint_scene=paint_fall_scene)
