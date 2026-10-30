"""
Scenes for verbs that move things around: give, take, get, bring, buy, pay, put, hold, keep, let, spend.
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
    WOOD,
    draw_arrow,
    draw_balloon,
    draw_bird,
    draw_chest,
    draw_coin,
    draw_gift_box,
    draw_heart,
    draw_key,
    draw_shopping_bag,
    draw_sparkle,
    draw_star,
    draw_sweat_drop,
    draw_wind_lines,
)
from tense import INFINITIVE, PARTICIPLE, PAST, paint_past_clock
from verb_painter import solid

STAND_HIP = (512, 620)
PARTNER_SHIRT = (190, 120, 220)
PARTNER_HAIR = (50, 50, 64)
FORWARD_ARMS = {"left_arm": (65, 35), "right_arm": (95, 10)}


def _build_partner(hip):
    return Character(hip=hip, shirt=PARTNER_SHIRT, hair=PARTNER_HAIR)


def _draw_ball(
    painter,
    center,
    radius=46,
):
    painter.fill_circle(center=center, radius=radius, shade=solid(ORANGE))
    painter.flat_stroke(start=(center[0] - radius, center[1]), end=(center[0] + radius, center[1]), width=6, color=(150, 80, 30))
    painter.flat_stroke(start=(center[0], center[1] - radius), end=(center[0], center[1] + radius), width=6, color=(150, 80, 30))


def _draw_house(
    painter,
    bottom_center,
):
    wall_box = (bottom_center[0] - 90, bottom_center[1] - 140, bottom_center[0] + 90, bottom_center[1])
    painter.fill_rounded_rect(box=wall_box, radius=6, shade=solid((246, 226, 190)))
    painter.fill_polygon(
        points=[(wall_box[0] - 20, wall_box[1] + 6), (bottom_center[0], wall_box[1] - 90), (wall_box[2] + 20, wall_box[1] + 6)],
        shade=solid(RED),
    )
    painter.fill_rounded_rect(box=(bottom_center[0] - 24, bottom_center[1] - 80, bottom_center[0] + 24, bottom_center[1]), radius=6, shade=solid(BROWN))


def paint_give_scene(painter, form):
    if form == INFINITIVE:
        skeleton = Character(hip=(360, 620)).draw(painter=painter, pose=Pose(mouth="smile", **FORWARD_ARMS))
        draw_gift_box(painter=painter, center=(skeleton.right_hand[0] + 20, skeleton.right_hand[1] - 40), size=0.8)
        draw_heart(painter=painter, center=(560, 300), size=36)
    elif form == PAST:
        Character(hip=(300, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 0), mouth="smile"))
        _build_partner(hip=(760, 650)).draw(painter=painter, pose=Pose(left_arm=(-105, 0), right_arm=(100, 0), eyes="wide", mouth="o", brows="raised"))
        draw_wind_lines(painter=painter, origin=(500, 440), length=110, count=2)
        draw_gift_box(painter=painter, center=(580, 440), size=0.7)
        paint_past_clock(painter=painter, center=(520, 200))
    else:
        Character(hip=(250, 670), scale=0.75).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(150, 40), eyes="happy", mouth="grin"))
        _build_partner(hip=(620, 620)).draw(painter=painter, pose=Pose(left_arm=(-20, 70), right_arm=(20, -70), eyes="happy", mouth="grin"))
        draw_gift_box(painter=painter, center=(620, 660), size=0.7)
        draw_heart(painter=painter, center=(780, 300), size=40)
        draw_heart(painter=painter, center=(470, 330), size=24, color=PINK)


def paint_take_scene(painter, form):
    if form == INFINITIVE:
        painter.fill_rounded_rect(box=(660, 560, 900, 590), radius=8, shade=solid(WOOD))
        draw_gift_box(painter=painter, center=(780, 500), size=0.75)
        Character(hip=(360, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 5), eyes="side", mouth="open"))
    elif form == PAST:
        skeleton = Character(hip=(460, 620)).draw(painter=painter, pose=Pose(left_arm=(70, 20), right_arm=(110, 10), eyes="happy", mouth="grin"))
        draw_gift_box(painter=painter, center=(skeleton.right_hand[0] + 30, skeleton.right_hand[1] - 40), size=0.7)
    else:
        Character(hip=(420, 620)).draw(painter=painter, pose=Pose(left_arm=(70, 30), right_arm=(110, 10), eyes="happy", mouth="grin"))
        draw_gift_box(painter=painter, center=(560, 560), size=0.8)
        draw_wind_lines(painter=painter, origin=(200, 560), length=120, count=2)


def paint_get_scene(painter, form):
    if form == INFINITIVE:
        Character(hip=(420, 620)).draw(painter=painter, pose=Pose(left_arm=(110, 40), right_arm=(130, 40), eyes="wide", mouth="open"))
        draw_wind_lines(painter=painter, origin=(880, 380), length=160, count=3)
        _draw_ball(painter=painter, center=(730, 380))
    elif form == PAST:
        skeleton = Character(hip=(512, 620)).draw(painter=painter, pose=Pose(left_arm=(40, 120), right_arm=(-40, -120), eyes="happy", mouth="grin"))
        _draw_ball(painter=painter, center=(512, skeleton.right_hand[1] - 30))
    else:
        Character(hip=(512, 620)).draw(painter=painter, pose=CHEER_POSE)
        _draw_ball(painter=painter, center=(512, 250))
        draw_sparkle(painter=painter, center=(720, 300), size=32)


def paint_bring_scene(painter, form):
    house_x = 800

    if form == PARTICIPLE:
        _draw_house(painter=painter, bottom_center=(house_x, 836))
        Character(hip=(440, 620)).draw(painter=painter, pose=Pose(eyes="happy", mouth="grin", left_arm=(-50, 100), right_arm=(50, -100)))
        draw_gift_box(painter=painter, center=(620, 790), size=0.7)
        return

    walking_pose = Pose(lean=6, left_arm=(60, 90), right_arm=(70, 90), left_leg=(-24, 6), right_leg=(26, -14), mouth="smile")
    skeleton = Character(hip=(400 if form == INFINITIVE else 480, 620)).draw(painter=painter, pose=walking_pose)
    draw_gift_box(painter=painter, center=(skeleton.right_hand[0] + 10, skeleton.right_hand[1] - 70), size=0.7)
    _draw_house(painter=painter, bottom_center=(house_x, 836))

    if form == INFINITIVE:
        draw_arrow(painter=painter, start=(480, 300), end=(680, 300), color=BLUE)
    else:
        draw_wind_lines(painter=painter, origin=(250, 560), length=140, count=3)


def paint_buy_scene(painter, form):
    skeleton = Character(hip=(440, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(40, 20), eyes="happy", mouth="grin"))
    draw_shopping_bag(painter=painter, center=(skeleton.right_hand[0] + 6, skeleton.right_hand[1] + 70), size=0.85)

    if form == INFINITIVE:
        draw_coin(painter=painter, center=(760, 360), radius=48)
        draw_arrow(painter=painter, start=(700, 440), end=(600, 540), color=GOLD, width=18)
    elif form == PAST:
        draw_coin(painter=painter, center=(760, 640), radius=44)
        draw_coin(painter=painter, center=(820, 720), radius=34)
    else:
        draw_heart(painter=painter, center=(760, 440), size=44)
        draw_sparkle(painter=painter, center=(300, 380), size=32)


def paint_pay_scene(painter, form):
    Character(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(110, 20), mouth="smile"))
    partner = _build_partner(hip=(720, 640))
    partner_skeleton = partner.draw(painter=painter, pose=Pose(left_arm=(-100, 20), right_arm=(14, 0), mouth="smile"))

    if form == INFINITIVE:
        draw_coin(painter=painter, center=(520, 420), radius=44)
        draw_arrow(painter=painter, start=(470, 340), end=(600, 340), color=BLUE, width=18)
    elif form == PAST:
        draw_coin(painter=painter, center=(partner_skeleton.left_hand[0] - 20, partner_skeleton.left_hand[1] - 40), radius=40)
    else:
        draw_coin(painter=painter, center=(partner_skeleton.left_hand[0] - 20, partner_skeleton.left_hand[1] - 40), radius=40)
        draw_heart(painter=painter, center=(520, 300), size=34)


def paint_put_scene(painter, form):
    painter.fill_rounded_rect(box=(620, 600, 920, 636), radius=8, shade=solid(WOOD))
    painter.fill_stroke(start=(660, 636), end=(660, 760), width=14, shade=solid(BROWN))
    painter.fill_stroke(start=(880, 636), end=(880, 760), width=14, shade=solid(BROWN))
    Character(hip=(380, 620)).draw(painter=painter, pose=Pose(left_arm=(80, 30), right_arm=(100, 20), mouth="smile"))

    if form == INFINITIVE:
        draw_gift_box(painter=painter, center=(640, 380), size=0.7)
        draw_arrow(painter=painter, start=(760, 340), end=(760, 470), color=BLUE)
    else:
        draw_gift_box(painter=painter, center=(770, 540), size=0.7)

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(880, 420), size=32)


def paint_hold_scene(painter, form):
    skeleton = Character(hip=(440, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(50, 130), eyes="happy", mouth="smile"))
    anchor = skeleton.right_hand
    draw_balloon(painter=painter, center=(anchor[0] + 40, anchor[1] - 260), radius=70, color=RED, string_end=anchor)

    if form != INFINITIVE:
        draw_balloon(painter=painter, center=(anchor[0] + 150, anchor[1] - 230), radius=60, color=BLUE, string_end=anchor)

    if form == PARTICIPLE:
        draw_balloon(painter=painter, center=(anchor[0] - 60, anchor[1] - 220), radius=56, color=GREEN, string_end=anchor)


def paint_keep_scene(painter, form):
    Character(hip=(512, 600)).draw(painter=painter, pose=Pose(left_arm=(40, 130), right_arm=(-40, -130), eyes="happy", mouth="smile"))
    draw_chest(painter=painter, center=(512, 640), size=1.1)

    if form == PAST:
        draw_key(painter=painter, center=(760, 460), size=0.9)
    elif form == PARTICIPLE:
        draw_heart(painter=painter, center=(512, 250), size=44)
        draw_sparkle(painter=painter, center=(760, 420), size=32)


def paint_let_scene(painter, form):
    pose = Pose(left_arm=(-14, 0), right_arm=(110, 30), eyes="happy", mouth="smile")

    if form == PARTICIPLE:
        Character(hip=(380, 620)).draw(painter=painter, pose=pose)
        draw_bird(painter=painter, center=(800, 260), size=0.5, color=BLUE)
        draw_sparkle(painter=painter, center=(640, 330), size=28)
        return

    skeleton = Character(hip=(380, 620)).draw(painter=painter, pose=pose)

    if form == INFINITIVE:
        draw_bird(painter=painter, center=(skeleton.right_hand[0] + 20, skeleton.right_hand[1] - 40), size=0.6, color=BLUE)
        draw_arrow(painter=painter, start=(700, 400), end=(860, 300), color=BLUE, width=18)
    else:
        draw_bird(painter=painter, center=(700, 300), size=0.8, color=BLUE)
        draw_wind_lines(painter=painter, origin=(610, 320), length=100, count=2)


def paint_spend_scene(painter, form):
    pose = Pose(left_arm=(-14, 0), right_arm=(70, 100), eyes="wide", mouth="open") if form != PARTICIPLE else Pose(left_arm=(-70, 40), right_arm=(70, -40), eyes="wide", mouth="sad", brows="worry")
    skeleton = Character(hip=(400, 620)).draw(painter=painter, pose=pose)

    if form == PARTICIPLE:
        draw_sweat_drop(painter=painter, center=(540, 330))
        draw_coin(painter=painter, center=(780, 700), radius=36)
        return

    wallet_center = (skeleton.right_hand[0] + 20, skeleton.right_hand[1] + 40)
    painter.fill_rounded_rect(
        box=(wallet_center[0] - 80, wallet_center[1] - 50, wallet_center[0] + 80, wallet_center[1] + 50),
        radius=14,
        shade=solid(BROWN),
    )

    for index in range(2 if form == INFINITIVE else 4):
        draw_coin(painter=painter, center=(wallet_center[0] + 40 + index * 70, wallet_center[1] - 150 - (index % 2) * 70), radius=36)


SCENES = {
    "give": paint_give_scene,
    "take": paint_take_scene,
    "get": paint_get_scene,
    "bring": paint_bring_scene,
    "buy": paint_buy_scene,
    "pay": paint_pay_scene,
    "put": paint_put_scene,
    "hold": paint_hold_scene,
    "keep": paint_keep_scene,
    "let": paint_let_scene,
    "spend": paint_spend_scene,
}
