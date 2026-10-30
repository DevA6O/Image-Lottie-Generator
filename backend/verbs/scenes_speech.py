"""
Scenes for verbs of speaking and writing: say, tell, speak, write, read, draw, meet, send.
Every scene function gets the painter and the form (0 infinitive, 1 past, 2 past participle).
"""
from character import CHEER_POSE, Character, Pose
from props import (
    BLUE,
    BROWN,
    GOLD,
    GREEN,
    ORANGE,
    PINK,
    RED,
    WHITE,
    draw_arrow,
    draw_check_mark,
    draw_closed_book,
    draw_envelope,
    draw_exclamation_mark,
    draw_heart,
    draw_lightbulb,
    draw_microphone,
    draw_music_note,
    draw_open_book,
    draw_paper,
    draw_paper_plane,
    draw_pencil,
    draw_sound_waves,
    draw_sparkle,
    draw_speech_bubble,
    draw_star,
    draw_sun,
    draw_text_lines,
    draw_wind_lines,
)
from tense import INFINITIVE, PARTICIPLE, PAST, paint_past_clock
from verb_painter import solid

STAND_HIP = (512, 620)
LISTENER_SHIRT = (190, 120, 220)
LISTENER_HAIR = (50, 50, 64)


def _build_partner(hip):
    return Character(hip=hip, shirt=LISTENER_SHIRT, hair=LISTENER_HAIR)


def paint_say_scene(painter, form):
    Character(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(100, 20), mouth="open", head_tilt=-4))
    draw_speech_bubble(painter=painter, center=(430, 190), width=420, height=170, tail_tip=(480, 330))

    if form == INFINITIVE:
        draw_text_lines(painter=painter, center=(430, 190), width=300, count=2)
    elif form == PAST:
        draw_heart(painter=painter, center=(430, 190), size=56)
    else:
        draw_check_mark(painter=painter, center=(430, 190), size=50)


def paint_tell_scene(painter, form):
    Character(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(110, 10), mouth="open"))
    _build_partner(hip=(720, 650)).draw(painter=painter, pose=Pose(eyes="wide", mouth="o", brows="raised", left_arm=(-24, 10)))
    draw_speech_bubble(painter=painter, center=(500, 200), width=360, height=160, tail_tip=(430, 320))

    if form == INFINITIVE:
        draw_exclamation_mark(painter=painter, center=(500, 200), size=0.9)
    elif form == PAST:
        draw_text_lines(painter=painter, center=(500, 200), width=260, count=2)
    else:
        draw_lightbulb(painter=painter, center=(720, 230), size=0.7)


def paint_speak_scene(painter, form):
    skeleton = Character(hip=(400, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(60, 120), mouth="open", eyes="happy"))
    microphone_center = (skeleton.right_hand[0] + 10, skeleton.right_hand[1] - 40)
    draw_microphone(painter=painter, center=microphone_center, size=0.8)
    draw_sound_waves(painter=painter, center=(microphone_center[0] + 40, microphone_center[1]), size=1.0, facing=1)

    if form == PAST:
        draw_music_note(painter=painter, center=(820, 560), size=0.9)
    elif form == PARTICIPLE:
        draw_star(painter=painter, center=(800, 600), size=40)


def paint_write_scene(painter, form):
    if form == PARTICIPLE:
        skeleton = Character(hip=(400, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(125, 30), eyes="happy", mouth="grin"))
        envelope_center = (skeleton.right_hand[0] + 90, skeleton.right_hand[1] - 50)
        draw_envelope(painter=painter, center=envelope_center, width=220, height=150)
        draw_heart(painter=painter, center=(envelope_center[0], envelope_center[1] + 6), size=26)
        draw_star(painter=painter, center=(envelope_center[0] + 150, envelope_center[1] - 60), size=30)
        return

    if form == INFINITIVE:
        writing_pose = Pose(left_arm=(-14, 0), right_arm=(80, 120), eyes="closed", mouth="smile")
        writer = Character(hip=(400, 620))
        skeleton = writer.build_skeleton(pose=writing_pose)
        pencil_tip = (skeleton.right_hand[0] + 40, skeleton.right_hand[1] + 40)
        draw_paper(painter=painter, center=(pencil_tip[0] + 120, pencil_tip[1] - 10), width=240, height=300, line_count=1)
        writer.draw(painter=painter, pose=writing_pose)
        draw_pencil(painter=painter, tip=pencil_tip, angle=-50)
    else:
        Character(hip=(400, 620)).draw(painter=painter, pose=Pose(left_arm=(-20, 0), right_arm=(20, 0), eyes="happy", mouth="grin"))
        draw_paper(painter=painter, center=(780, 560), width=240, height=300, line_count=5)
        draw_pencil(painter=painter, tip=(690, 660), angle=-25)
        paint_past_clock(painter=painter, center=(780, 260))


def paint_read_scene(painter, form):
    pose = Pose(left_arm=(-40, 110), right_arm=(40, -110), eyes="closed", mouth="smile")
    Character(hip=STAND_HIP).draw(painter=painter, pose=pose)
    draw_open_book(painter=painter, center=(512, 560), width=300, height=190)

    if form == PAST:
        draw_sparkle(painter=painter, center=(780, 400), size=34)
    elif form == PARTICIPLE:
        draw_closed_book(painter=painter, center=(820, 780), width=190, height=50, color=BLUE)
        draw_closed_book(painter=painter, center=(830, 730), width=170, height=50, color=GREEN)
        draw_closed_book(painter=painter, center=(815, 680), width=180, height=50, color=ORANGE)


def paint_draw_scene(painter, form):
    for foot_x in (640, 740, 840):
        painter.fill_stroke(start=(740, 640), end=(foot_x, 840), width=16, shade=solid(BROWN))

    canvas_box = (610, 380, 870, 600)
    painter.fill_rounded_rect(box=canvas_box, radius=8, shade=solid(GOLD if form == PARTICIPLE else (250, 250, 255)))
    painter.fill_rounded_rect(box=(620, 390, 860, 590), radius=6, shade=solid((250, 250, 255)))
    skeleton = Character(hip=(360, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 60), eyes="closed", mouth="smile"))
    draw_pencil(painter=painter, tip=(skeleton.right_hand[0] + 40, skeleton.right_hand[1] + 10), angle=-35)

    if form == PAST:
        draw_sun(painter=painter, center=(740, 470), radius=36)
    elif form == PARTICIPLE:
        draw_sun(painter=painter, center=(700, 470), radius=30)
        draw_heart(painter=painter, center=(800, 500), size=34)
        draw_star(painter=painter, center=(880, 380), size=30)


def paint_meet_scene(painter, form):
    left_pose = Pose(left_arm=(-14, 0), right_arm=(73, 0), mouth="grin", eyes="happy")
    right_pose = Pose(left_arm=(-70, 0), right_arm=(14, 0), mouth="grin", eyes="happy")

    if form == PARTICIPLE:
        Character(hip=(340, 620)).draw(painter=painter, pose=CHEER_POSE)
        _build_partner(hip=(700, 620)).draw(painter=painter, pose=CHEER_POSE)
        draw_star(painter=painter, center=(520, 360), size=40)
        return

    Character(hip=(340, 620)).draw(painter=painter, pose=left_pose)
    _build_partner(hip=(700, 620)).draw(painter=painter, pose=right_pose)

    if form == INFINITIVE:
        draw_arrow(painter=painter, start=(300, 260), end=(440, 260), color=BLUE, width=18)
        draw_arrow(painter=painter, start=(740, 260), end=(600, 260), color=BLUE, width=18)
    else:
        draw_heart(painter=painter, center=(520, 360), size=44)
        draw_heart(painter=painter, center=(440, 300), size=24, color=PINK)


def paint_send_scene(painter, form):
    pose = Pose(left_arm=(-14, 0), right_arm=(140, 20), mouth="grin", eyes="happy")

    if form == PARTICIPLE:
        Character(hip=(330, 620)).draw(painter=painter, pose=pose)
        draw_envelope(painter=painter, center=(760, 560), width=220, height=150)
        draw_check_mark(painter=painter, center=(760, 560), size=36, color=GREEN)
        return

    Character(hip=(360, 620)).draw(painter=painter, pose=pose)

    if form == INFINITIVE:
        draw_wind_lines(painter=painter, origin=(660, 330), length=150, count=3)
        draw_paper_plane(painter=painter, center=(760, 320), size=1.1, rotation=-20)
    else:
        draw_wind_lines(painter=painter, origin=(660, 330), length=150, count=3)
        draw_envelope(painter=painter, center=(780, 320), width=170, height=116)
        painter.fill_circle(center=(780, 340), radius=16, shade=solid(RED))


SCENES = {
    "say": paint_say_scene,
    "tell": paint_tell_scene,
    "speak": paint_speak_scene,
    "write": paint_write_scene,
    "read": paint_read_scene,
    "draw": paint_draw_scene,
    "meet": paint_meet_scene,
    "send": paint_send_scene,
}
