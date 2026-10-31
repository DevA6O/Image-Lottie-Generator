"""
Scene for the irregular verb "sit" (sat, sat).
Output: sit_infinitive.png, sit_past.png and sit_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import BLUE, WHITE, draw_arrow, draw_chair, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

CHAIR_CENTER = (512, 685)
CHAIR_SIZE = 1.5
CHAIR_LEG_LENGTH = 95    # The seat is as low as the shins, so the feet stand on the floor
SEATED_HIP = (512, 660)
SEATED_LEG_FORESHORTENING = 0.35    # The thighs point toward the viewer
SITTING_LEFT_LEG = (-8, 8)
SITTING_RIGHT_LEG = (8, -8)
LOWERING_HIP_RISE = 70


def paint_sit_scene(painter, form):
    draw_chair(painter=painter, seat_center=CHAIR_CENTER, size=CHAIR_SIZE, leg_length=CHAIR_LEG_LENGTH)

    if form == INFINITIVE:
        lowering_pose = Pose(mouth="open", left_leg=(-14, 14), right_leg=(14, -14), left_arm=(-24, 0), right_arm=(24, 0), thigh_factor=0.7, lean=-6)
        Milo(hip=(SEATED_HIP[0], SEATED_HIP[1] - LOWERING_HIP_RISE)).draw(painter=painter, pose=lowering_pose)
        draw_arrow(painter=painter, start=(840, 440), end=(840, 640), color=BLUE)
    elif form == PAST:
        Milo(hip=SEATED_HIP).draw(painter=painter, pose=build_seated_pose(eyes="happy", mouth="smile"))
        paint_past_clock(painter=painter, center=(830, 230))
    else:
        Milo(hip=SEATED_HIP).draw(painter=painter, pose=build_seated_pose(eyes="closed", mouth="smile"))
        draw_sparkle(painter=painter, center=(790, 520), size=34, color=WHITE)


def build_seated_pose(
    eyes,
    mouth,
):
    return Pose(
        left_arm=(-24, 10),
        right_arm=(24, -10),
        left_leg=SITTING_LEFT_LEG,
        right_leg=SITTING_RIGHT_LEG,
        thigh_factor=SEATED_LEG_FORESHORTENING,
        eyes=eyes,
        mouth=mouth,
    )


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="sit", paint_scene=paint_sit_scene)
