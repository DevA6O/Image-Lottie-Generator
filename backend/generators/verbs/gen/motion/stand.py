"""
Scene for the irregular verb "stand" (stood, stood).
Output: stand_infinitive.png, stand_past.png and stand_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import BLUE, ORANGE, draw_arrow, draw_chair, draw_flag
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

SIDE_CHAIR_CENTER = (230, 684)
STANDING_HIP = (560, 620)
PUSHED_BACK_CHAIR_CENTER = (330, 684)
HAND_ON_BACKREST_ARM = (-70, 0)    # Straight, the hand reaches the top of the chair back
HANDS_ON_HIPS_LEFT_ARM = (-50, 100)
HANDS_ON_HIPS_RIGHT_ARM = (50, -100)


def paint_stand_scene(painter, form):
    if form == INFINITIVE:
        draw_chair(painter=painter, seat_center=PUSHED_BACK_CHAIR_CENTER)
        standing_up_pose = Pose(left_arm=HAND_ON_BACKREST_ARM, right_arm=(14, 0), eyes="happy", mouth="grin")
        Milo(hip=STANDING_HIP).draw(painter=painter, pose=standing_up_pose)
        draw_arrow(painter=painter, start=(860, 700), end=(860, 480), color=BLUE)
        return

    draw_chair(painter=painter, seat_center=SIDE_CHAIR_CENTER)

    if form == PAST:
        Milo(hip=STANDING_HIP).draw(painter=painter, pose=Pose(mouth="grin", left_arm=HANDS_ON_HIPS_LEFT_ARM, right_arm=HANDS_ON_HIPS_RIGHT_ARM))
        paint_past_clock(painter=painter, center=(850, 230))
    else:
        Milo(hip=STANDING_HIP).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(120, 70), eyes="happy", mouth="grin"))
        draw_flag(painter=painter, pole_bottom=(860, 836), pole_height=300, width=130, height=84, color=ORANGE)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="stand", paint_scene=paint_stand_scene)
