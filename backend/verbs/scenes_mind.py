"""
Scenes for verbs of thinking and sensing: know, think, understand, mean, feel, choose, see, hear, find, lose.
Every scene function gets the painter and the form (0 infinitive, 1 past, 2 past participle).
"""
from character import CHEER_POSE, Character, Pose
from props import (
    BLUE,
    GRAY,
    GREEN,
    ORANGE,
    PINK,
    RED,
    WHITE,
    draw_check_mark,
    draw_coin,
    draw_exclamation_mark,
    draw_eye,
    draw_gear,
    draw_heart,
    draw_key,
    draw_lightbulb,
    draw_magnifier,
    draw_music_note,
    draw_question_mark,
    draw_sound_waves,
    draw_sparkle,
    draw_star,
    draw_sweat_drop,
    draw_thought_bubble,
    draw_speech_bubble,
)
from tense import INFINITIVE, PARTICIPLE, PAST, paint_past_clock

STAND_HIP = (512, 620)


def _stand(
    painter,
    pose,
    hip=STAND_HIP,
):

    return Character(hip=hip).draw(painter=painter, pose=pose)


def paint_know_scene(painter, form):
    if form == PARTICIPLE:
        _stand(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(50, -100), eyes="happy", mouth="grin"))
        draw_star(painter=painter, center=(512, 170), size=80)
        draw_heart(painter=painter, center=(300, 320), size=40)
        draw_heart(painter=painter, center=(724, 320), size=40)
        draw_sparkle(painter=painter, center=(380, 200), size=30)
        draw_sparkle(painter=painter, center=(650, 190), size=30)
        return

    pose = Pose(left_arm=(-50, 100), right_arm=(130, 40), eyes="happy", mouth="smile", brows="raised")
    _stand(painter=painter, pose=pose)
    draw_lightbulb(painter=painter, center=(512, 130), size=0.9, glowing=form == INFINITIVE)

    if form == PAST:
        paint_past_clock(painter=painter)


def paint_think_scene(painter, form):
    if form == PARTICIPLE:
        _stand(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(50, -100), eyes="happy", mouth="grin"))
        draw_thought_bubble(painter=painter, center=(400, 190), width=380, height=190, tail_tip=(450, 310))
        draw_lightbulb(painter=painter, center=(350, 170), size=0.6)
        draw_check_mark(painter=painter, center=(480, 195), size=34)
        return

    pose = Pose(head_tilt=8, left_arm=(-14, 0), right_arm=(40, 185), eyes="up", mouth="flat")
    _stand(painter=painter, pose=pose)
    draw_thought_bubble(painter=painter, center=(400, 190), width=380, height=190, tail_tip=(450, 310))

    if form == INFINITIVE:
        draw_question_mark(painter=painter, center=(400, 190), size=1.0)
    else:
        draw_gear(painter=painter, center=(350, 190), size=0.9, color=GRAY)
        draw_gear(painter=painter, center=(450, 190), size=0.7, color=BLUE)
        paint_past_clock(painter=painter)


def paint_understand_scene(painter, form):
    pose = Pose(left_arm=(-65, 0), right_arm=(65, 0), eyes="wide", mouth="o", brows="raised")
    _stand(painter=painter, pose=pose)
    draw_exclamation_mark(painter=painter, center=(512, 190), size=1.2)

    if form != INFINITIVE:
        draw_gear(painter=painter, center=(270, 330), size=0.9, color=GRAY)
        draw_gear(painter=painter, center=(350, 280), size=0.7, color=BLUE)

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(740, 340), size=36)


def paint_mean_scene(painter, form):
    pose = Pose(left_arm=(-70, 40), right_arm=(70, -40), eyes="open", mouth="flat", brows="worry", head_tilt=-6)
    _stand(painter=painter, pose=pose)
    draw_speech_bubble(painter=painter, center=(430, 190), width=440, height=170, tail_tip=(480, 300))
    left_color, right_color = (GRAY, GRAY) if form == INFINITIVE else (ORANGE, PINK)

    painter.fill_circle(center=(320, 190), radius=40, shade=(left_color, left_color))
    painter.fill_circle(center=(540, 190), radius=40, shade=(right_color, right_color))
    painter.flat_stroke(start=(400, 168), end=(460, 168), width=14, color=BLUE)
    painter.flat_stroke(start=(400, 212), end=(460, 212), width=14, color=BLUE)

    if form == INFINITIVE:
        draw_question_mark(painter=painter, center=(790, 360), size=0.9)
    elif form == PARTICIPLE:
        draw_check_mark(painter=painter, center=(790, 380), size=40)


def paint_feel_scene(painter, form):
    if form == PAST:
        pose = Pose(right_arm=(10, 210), eyes="closed", mouth="sad", head_tilt=-6)
    else:
        pose = Pose(right_arm=(10, 210), eyes="closed", mouth="smile", head_tilt=6)

    _stand(painter=painter, pose=pose)

    if form == PAST:
        draw_sweat_drop(painter=painter, center=(690, 380))
        draw_sweat_drop(painter=painter, center=(330, 420), radius=11)
    else:
        draw_heart(painter=painter, center=(512, 180), size=56)
        draw_heart(painter=painter, center=(330, 300), size=30, color=PINK)
        draw_heart(painter=painter, center=(710, 320), size=34, color=PINK)

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(250, 480), size=30)


def paint_choose_scene(painter, form):
    pose = Pose(left_arm=(-30, 150), right_arm=(100, 0), eyes="side", mouth="flat", brows="raised")
    _stand(painter=painter, pose=pose, hip=(400, 620))
    painter.fill_circle(center=(250, 330), radius=70, shade=((ORANGE), (ORANGE)))
    painter.fill_circle(center=(740, 520), radius=90, shade=((RED), (RED)))

    if form == INFINITIVE:
        draw_question_mark(painter=painter, center=(520, 220), size=0.9)
    elif form == PAST:
        draw_check_mark(painter=painter, center=(740, 520), size=50, color=WHITE)
    else:
        draw_check_mark(painter=painter, center=(740, 520), size=50, color=WHITE)
        draw_star(painter=painter, center=(740, 400), size=36)


def paint_see_scene(painter, form):
    if form == INFINITIVE:
        _stand(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(40, 185), eyes="wide", mouth="o"))
        draw_eye(painter=painter, center=(512, 140), size=1.0)
    elif form == PAST:
        _stand(painter=painter, pose=Pose(left_arm=(-70, 20), right_arm=(70, -20), eyes="wide", mouth="o", brows="raised"))
        draw_star(painter=painter, center=(740, 330), size=60)
        draw_exclamation_mark(painter=painter, center=(290, 340), size=0.9)
        paint_past_clock(painter=painter, center=(800, 150))
    else:
        _stand(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(50, -100), eyes="happy", mouth="smile"))
        draw_speech_bubble(painter=painter, center=(430, 190), width=380, height=170, tail_tip=(480, 320))
        draw_eye(painter=painter, center=(360, 190), size=0.5)
        draw_check_mark(painter=painter, center=(520, 195), size=36)


def paint_hear_scene(painter, form):
    pose = Pose(head_tilt=10, left_arm=(-14, 0), right_arm=(120, 90), eyes="closed", mouth="smile")
    _stand(painter=painter, pose=pose, hip=(400, 620))
    draw_sound_waves(painter=painter, center=(860, 450), size=1.0, facing=-1)
    draw_music_note(painter=painter, center=(720, 300), size=0.9)

    if form != INFINITIVE:
        draw_music_note(painter=painter, center=(840, 240), size=0.7, color=BLUE)

    if form == PARTICIPLE:
        draw_heart(painter=painter, center=(240, 330), size=34)


def paint_find_scene(painter, form):

    if form == PARTICIPLE:
        Character(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-150, 0), right_arm=(150, 0), eyes="happy", mouth="grin"))
        draw_star(painter=painter, center=(300, 330), size=60)
        draw_sparkle(painter=painter, center=(740, 360), size=34)
        return

    skeleton = Character(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(60, 90), eyes="wide", mouth="o"))
    lens_center = (skeleton.right_hand[0] + 70, skeleton.right_hand[1] - 20)
    draw_magnifier(painter=painter, center=lens_center, radius=70, handle_angle=135)

    if form == INFINITIVE:
        draw_question_mark(painter=painter, center=lens_center, size=0.7, color=BLUE)
    else:
        draw_star(painter=painter, center=lens_center, size=40)
        draw_exclamation_mark(painter=painter, center=(300, 400), size=0.9)


def paint_lose_scene(painter, form):
    pose = Pose(left_arm=(-70, 40), right_arm=(70, -40), eyes="wide", mouth="sad", brows="worry")
    _stand(painter=painter, pose=pose)
    draw_question_mark(painter=painter, center=(512, 190), size=1.0)

    if form == INFINITIVE:
        draw_coin(painter=painter, center=(300, 640), radius=44)
        draw_coin(painter=painter, center=(240, 740), radius=34)
    elif form == PAST:
        draw_key(painter=painter, center=(250, 650), size=0.9)
        draw_sweat_drop(painter=painter, center=(700, 330))
    else:
        draw_sweat_drop(painter=painter, center=(700, 330))
        draw_sweat_drop(painter=painter, center=(330, 360), radius=11)


SCENES = {
    "know": paint_know_scene,
    "think": paint_think_scene,
    "understand": paint_understand_scene,
    "mean": paint_mean_scene,
    "feel": paint_feel_scene,
    "choose": paint_choose_scene,
    "see": paint_see_scene,
    "hear": paint_hear_scene,
    "find": paint_find_scene,
    "lose": paint_lose_scene,
}
