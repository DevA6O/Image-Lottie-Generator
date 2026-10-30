"""
Scene for the irregular verb "fall" (fell, fallen).
Output: fall_infinitive.png, fall_past.png and fall_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import draw_arrow, draw_banana_peel, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock


def paint_fall_scene(painter, form):
    if form == INFINITIVE:
        slipping_pose = Pose(lean=-18, head_tilt=-6, left_arm=(-125, 0), right_arm=(135, 0), left_leg=(-10, 0), right_leg=(75, -15), eyes="wide", mouth="open", brows="worry")
        character = Character(hip=(440, 590))
        skeleton = character.build_skeleton(pose=slipping_pose)
        draw_banana_peel(painter=painter, center=(skeleton.right_foot[0] + 20, skeleton.left_foot[1] - 40))
        character.draw(painter=painter, pose=slipping_pose)
    elif form == PAST:
        falling_pose = Pose(lean=-50, head_tilt=-8, left_arm=(-75, 0), right_arm=(150, 0), left_leg=(-30, 0), right_leg=(40, -30), eyes="wide", mouth="open", brows="worry")
        Character(hip=(480, 570)).draw(painter=painter, pose=falling_pose)

        for x in (690, 770, 850):
            draw_arrow(painter=painter, start=(x, 380), end=(x, 500), color=(140, 172, 220), width=12)

        paint_past_clock(painter=painter, center=(800, 220))
    else:
        lying_pose = Pose(lean=-88, left_arm=(60, 0), right_arm=(120, 0), left_leg=(80, 0), right_leg=(96, 0), eyes="closed", mouth="open")
        Character(hip=(640, 740)).draw(painter=painter, pose=lying_pose)

        for center, size in (((260, 560), 26), ((340, 500), 20), ((200, 650), 18)):
            draw_star(painter=painter, center=center, size=size)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="fall", paint_scene=paint_fall_scene)
