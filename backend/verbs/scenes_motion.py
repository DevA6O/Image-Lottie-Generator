"""
Scenes for verbs of movement: go, come, run, fall, rise, leave, drive, stand, sit, begin.
Every scene function gets the painter and the form (0 infinitive, 1 past, 2 past participle).
"""
from character import CHEER_POSE, Character, Pose
from props import (
    draw_medal,
    draw_banana_peel,
    BLUE,
    GREEN,
    ORANGE,
    WHITE,
    draw_arrow,
    draw_car_body,
    draw_car_cabin,
    draw_chair,
    draw_door,
    draw_dust_puff,
    draw_flag,
    draw_footprints,
    draw_sparkle,
    draw_star,
    draw_sun,
    draw_sweat_drop,
    draw_wind_lines,
)
from tense import INFINITIVE, PARTICIPLE, PAST, paint_past_clock
from verb_painter import solid


WALK_POSE = Pose(lean=6, head_tilt=3, left_arm=(-24, -14), right_arm=(26, 16), left_leg=(-24, 6), right_leg=(26, -14))
RUN_POSE = Pose(lean=18, head_tilt=6, left_arm=(-40, -100), right_arm=(40, 110), left_leg=(-35, -15), right_leg=(50, -80), mouth="grin")


def _hang_medal_on_neck(painter):
    def hang_medal(skeleton):
        medal_center = (skeleton.neck[0] + (skeleton.hip[0] - skeleton.neck[0]) * 0.38, skeleton.neck[1] + (skeleton.hip[1] - skeleton.neck[1]) * 0.38)
        draw_medal(painter=painter, neck=skeleton.neck, medal_center=medal_center, size=0.85)

    return hang_medal


def paint_go_scene(painter, form):
    if form == INFINITIVE:
        draw_wind_lines(painter=painter, origin=(330, 560), length=170, count=3)
        Character(hip=(540, 600)).draw(painter=painter, pose=WALK_POSE)
        draw_arrow(painter=painter, start=(700, 760), end=(880, 760), color=BLUE)
    elif form == PAST:
        draw_footprints(painter=painter, start=(120, 826), end=(560, 826), count=6)
        Character(hip=(700, 650), scale=0.72).draw(painter=painter, pose=WALK_POSE)
        paint_past_clock(painter=painter, center=(300, 300))
    else:
        draw_dust_puff(painter=painter, center=(250, 790), size=1.2)
        draw_footprints(painter=painter, start=(380, 826), end=(780, 816), count=5)
        Character(hip=(890, 740), scale=0.4).draw(painter=painter, pose=WALK_POSE)


def paint_come_scene(painter, form):

    if form == PARTICIPLE:
        Character(hip=(512, 600)).draw(painter=painter, pose=CHEER_POSE)
        draw_sparkle(painter=painter, center=(250, 400), size=40)
        draw_sparkle(painter=painter, center=(780, 460), size=34)
        return

    pose = Pose(lean=-4, left_arm=(-14, 0), right_arm=(120, 60), eyes="happy", mouth="smile")
    Character(hip=(440, 600)).draw(painter=painter, pose=pose)

    if form == INFINITIVE:
        draw_arrow(painter=painter, start=(900, 740), end=(700, 740), color=BLUE)
    else:
        draw_footprints(painter=painter, start=(900, 830), end=(640, 830), count=4)


def paint_run_scene(painter, form):
    if form == INFINITIVE:
        draw_wind_lines(painter=painter, origin=(330, 520), length=170, count=3)
        Character(hip=(540, 570)).draw(painter=painter, pose=RUN_POSE)
        draw_sweat_drop(painter=painter, center=(700, 300))
    elif form == PAST:
        Character(hip=(440, 570), fade=0.8).draw(painter=painter, pose=RUN_POSE)
        Character(hip=(580, 570), fade=0.5).draw(painter=painter, pose=RUN_POSE)
        Character(hip=(720, 570)).draw(painter=painter, pose=RUN_POSE)
        paint_past_clock(painter=painter, center=(240, 260))
    else:
        tired_pose = Pose(lean=34, head_tilt=10, left_arm=(-22, 0), right_arm=(45, 0), left_leg=(-14, 18), right_leg=(16, 10), eyes="closed", mouth="open")
        Character(hip=(512, 600)).draw(painter=painter, pose=tired_pose, before_arms=_hang_medal_on_neck(painter=painter))
        draw_sweat_drop(painter=painter, center=(700, 330))
        draw_sweat_drop(painter=painter, center=(740, 400), radius=11)


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


def paint_rise_scene(painter, form):
    sun_height = (770, 600, 430)[form]
    draw_sun(painter=painter, center=(300, sun_height), radius=80)
    Character(hip=(650, 600)).draw(painter=painter, pose=CHEER_POSE)
    draw_arrow(painter=painter, start=(440, 700), end=(440, 520), color=GREEN)

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(520, 360), size=36)


def paint_leave_scene(painter, form):
    draw_door(painter=painter, bottom_center=(250, 836), width=150, height=320, is_open=True)

    if form == PARTICIPLE:
        draw_footprints(painter=painter, start=(380, 830), end=(660, 830), count=5)
        Character(hip=(800, 700), scale=0.5).draw(painter=painter, pose=Pose(right_arm=(150, 40)))
        return
    traveler = Character(hip=(610, 600))
    skeleton = traveler.draw(painter=painter, pose=WALK_POSE_WAVING)
    suitcase_center = (skeleton.left_hand[0], skeleton.left_hand[1] + 36)
    painter.fill_rounded_rect(box=(suitcase_center[0] - 48, suitcase_center[1] - 36, suitcase_center[0] + 48, suitcase_center[1] + 40), radius=10, shade=solid((184, 100, 70)))
    painter.fill_stroke(start=(suitcase_center[0] - 20, suitcase_center[1] - 36), end=(suitcase_center[0] + 20, suitcase_center[1] - 36), width=12, shade=solid((120, 70, 50)))

    if form == PAST:
        draw_footprints(painter=painter, start=(400, 830), end=(480, 830), count=2)


WALK_POSE_WAVING = Pose(lean=4, head_tilt=-6, left_arm=(-12, 0), right_arm=(150, 40), left_leg=(-20, 6), right_leg=(22, -12), eyes="happy")


def paint_drive_scene(painter, form):
    car_center = (512, 680)

    if form != PARTICIPLE:
        draw_wind_lines(painter=painter, origin=(250, 650), length=190, count=3)
    draw_car_cabin(painter=painter, center=car_center)
    driver = Character(hip=(440, 719), scale=0.75)
    driver.draw(painter=painter, pose=Pose(left_arm=(40, 30), right_arm=(40, 30), mouth="grin"), with_legs=False)
    draw_car_body(painter=painter, center=car_center)
    painter.fill_ring(center=(500, 600), outer_radius=34, inner_radius=22, color=(60, 66, 86))

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(780, 400), size=40)
        draw_sparkle(painter=painter, center=(250, 450), size=28)


def paint_stand_scene(painter, form):

    if form == INFINITIVE:
        draw_chair(painter=painter, seat_center=(300, 690))
        rising_pose = Pose(lean=14, left_arm=(45, 10), right_arm=(60, 10), left_leg=(-20, 25), right_leg=(16, 20), mouth="open")
        Character(hip=(480, 560)).draw(painter=painter, pose=rising_pose)
        draw_arrow(painter=painter, start=(800, 720), end=(800, 540), color=BLUE)
        return

    hands_on_hips_pose = Pose(left_arm=(-50, 100), right_arm=(50, -100), mouth="grin")

    if form == PAST:
        draw_chair(painter=painter, seat_center=(250, 690))
        Character(hip=(550, 600)).draw(painter=painter, pose=hands_on_hips_pose)
        return

    Character(hip=(512, 600)).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(120, 70), eyes="happy", mouth="grin"))
    draw_flag(painter=painter, pole_bottom=(760, 836), pole_height=300, width=130, height=84, color=ORANGE)


def paint_sit_scene(painter, form):
    draw_chair(painter=painter, seat_center=(512, 700))
    sitting_legs = {"left_leg": (-35, 35), "right_leg": (35, -35)}

    if form == INFINITIVE:
        Character(hip=(512, 590)).draw(painter=painter, pose=Pose(mouth="open", **sitting_legs))
        draw_arrow(painter=painter, start=(820, 460), end=(820, 640), color=BLUE)
    elif form == PAST:
        Character(hip=(512, 640)).draw(painter=painter, pose=Pose(eyes="happy", **sitting_legs))
    else:
        relaxed_pose = Pose(left_arm=(-24, 10), right_arm=(24, -10), eyes="closed", mouth="smile", **sitting_legs)
        Character(hip=(512, 640)).draw(painter=painter, pose=relaxed_pose)
        draw_sparkle(painter=painter, center=(790, 520), size=34, color=WHITE)


def paint_begin_scene(painter, form):
    draw_flag(painter=painter, pole_bottom=(200, 836), pole_height=330, width=140, height=90, color=GREEN)

    if form == INFINITIVE:
        ready_pose = Pose(lean=22, left_arm=(-60, -20), right_arm=(40, 20), left_leg=(-30, 40), right_leg=(35, -30), mouth="grin")
        Character(hip=(480, 600)).draw(painter=painter, pose=ready_pose)
    elif form == PAST:
        draw_wind_lines(painter=painter, origin=(520, 520), length=200, count=3)
        Character(hip=(680, 570)).draw(painter=painter, pose=RUN_POSE)
    else:
        Character(hip=(520, 600)).draw(painter=painter, pose=CHEER_POSE)
        draw_sparkle(painter=painter, center=(760, 380), size=40)


SCENES = {
    "go": paint_go_scene,
    "come": paint_come_scene,
    "run": paint_run_scene,
    "fall": paint_fall_scene,
    "rise": paint_rise_scene,
    "leave": paint_leave_scene,
    "drive": paint_drive_scene,
    "stand": paint_stand_scene,
    "sit": paint_sit_scene,
    "begin": paint_begin_scene,
}
