"""
Scenes for verbs of making and being: make, build, break, cut, grow, wear, have, do, be, become, lead.
Every scene function gets the painter and the form (0 infinitive, 1 past, 2 past participle).
"""
from character import CHEER_POSE, Character, Pose
from props import (
    draw_pin,
    BLUE,
    GOLD,
    GRAY,
    GREEN,
    ORANGE,
    PINK,
    RED,
    YELLOW,
    draw_brick_wall,
    draw_check_mark,
    draw_clipboard,
    draw_coin,
    draw_crown,
    draw_flag,
    draw_hammer,
    draw_hat,
    draw_heart,
    draw_pencil,
    draw_plant,
    draw_scissors,
    draw_shards,
    draw_sparkle,
    draw_star,
    draw_sweat_drop,
    draw_trophy,
    draw_vase,
)
from verb_painter import build_polyline_points
from tense import INFINITIVE, PARTICIPLE, PAST, paint_past_clock
from verb_painter import solid

STAND_HIP = (512, 620)
FOLLOWER_SHIRTS = ((190, 120, 220), (240, 110, 130), (70, 190, 170))
BRICK_COLORS = (RED, BLUE, GREEN)
CAPE_COLOR = (214, 70, 80)
VASE_COLOR = (90, 180, 210)


def _draw_lego_brick(
    painter,
    center,
    color,
):
    painter.fill_rounded_rect(box=(center[0] - 90, center[1] - 40, center[0] + 90, center[1] + 40), radius=8, shade=solid(color))

    for offset in (-54, 0, 54):
        painter.fill_rounded_rect(box=(center[0] + offset - 20, center[1] - 62, center[0] + offset + 20, center[1] - 38), radius=8, shade=solid(color))


def paint_make_scene(painter, form):
    Character(hip=(380, 620)).draw(painter=painter, pose=Pose(left_arm=(70, 100), right_arm=(100, 60), eyes="happy", mouth="grin"))
    brick_count = form + 1

    for index in range(brick_count):
        _draw_lego_brick(painter=painter, center=(720, 800 - index * 90), color=BRICK_COLORS[index])

    if form == PARTICIPLE:
        draw_star(painter=painter, center=(720, 480), size=40)



def paint_build_scene(painter, form):
    skeleton = Character(hip=(330, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 100), eyes="happy", mouth="grin"))
    draw_hammer(painter=painter, center=(skeleton.right_hand[0] + 10, skeleton.right_hand[1] - 20), size=0.8, angle=-60)
    draw_brick_wall(painter=painter, left_bottom=(560, 836), column_count=3, row_count=(1, 3, 5)[form])

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(700, 260), size=36)


def paint_break_scene(painter, form):
    if form == INFINITIVE:
        Character(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-125, 0), right_arm=(125, 0), eyes="wide", mouth="open", brows="worry"))
        draw_vase(painter=painter, center=(730, 600), size=1.6, color=VASE_COLOR)
        crack = [(716, 480), (752, 560), (716, 600), (756, 690), (740, 720)]
        painter.flat_curve(points=build_polyline_points(corners=crack), width=10, color=(255, 255, 255))
    elif form == PAST:
        Character(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-125, 0), right_arm=(125, 0), eyes="wide", mouth="open", brows="worry"))
        paint_past_clock(painter=painter, center=(520, 200))
        draw_shards(painter=painter, center=(730, 580), spread=210, color=VASE_COLOR)
        draw_star(painter=painter, center=(730, 580), size=44, color=(255, 255, 255))
    else:
        Character(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-30, 0), right_arm=(30, 0), eyes="closed", mouth="sad", brows="worry"))

        for center, spread in (((620, 790), 70), ((740, 800), 84), ((850, 780), 66)):
            draw_shards(painter=painter, center=center, spread=spread, color=VASE_COLOR)

        draw_sweat_drop(painter=painter, center=(520, 330))


def paint_cut_scene(painter, form):
    skeleton = Character(hip=(380, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 70), eyes="happy", mouth="smile"))
    paper_left, paper_top, paper_right, paper_bottom = 560, 600, 900, 760

    if form == INFINITIVE:
        painter.fill_rounded_rect(box=(paper_left, paper_top, paper_right, paper_bottom), radius=8, shade=solid((250, 250, 255)))
        draw_scissors(painter=painter, pivot=(skeleton.right_hand[0] + 60, skeleton.right_hand[1] - 30), size=0.8, open_angle=20, direction=70)
        return

    gap = 26 if form == PAST else 50
    middle = (paper_left + paper_right) / 2
    painter.fill_rounded_rect(box=(paper_left - gap / 2, paper_top, middle - gap / 2, paper_bottom), radius=8, shade=solid((250, 250, 255)))
    painter.fill_rounded_rect(box=(middle + gap / 2, paper_top, paper_right + gap / 2, paper_bottom), radius=8, shade=solid((250, 250, 255)))

    if form == PAST:
        draw_scissors(painter=painter, pivot=(middle, paper_top - 60), size=0.8, open_angle=8, direction=90)
    else:
        draw_sparkle(painter=painter, center=(middle, paper_top - 80), size=36)


def paint_grow_scene(painter, form):
    Character(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(50, -100), eyes="happy", mouth="grin"))
    draw_plant(
        painter=painter,
        pot_center=(740, 780),
        stem_height=(90, 190, 300)[form],
        leaf_count=(2, 3, 4)[form],
        has_flower=form == PARTICIPLE,
    )

    if form != PARTICIPLE:
        draw_sparkle(painter=painter, center=(880, 540), size=30)


def paint_wear_scene(painter, form):
    pose = Pose(right_arm=(150, 30), left_arm=(-14, 0), eyes="happy", mouth="smile") if form == INFINITIVE else Pose(eyes="happy", mouth="grin", left_arm=(-50, 100), right_arm=(50, -100))
    skeleton = Character(hip=STAND_HIP).draw(painter=painter, pose=pose)

    if form == INFINITIVE:
        draw_hat(painter=painter, center=(skeleton.right_hand[0] + 10, skeleton.right_hand[1] - 40), size=0.8)
        return

    draw_hat(painter=painter, center=(skeleton.head[0], skeleton.head[1] - 62), size=0.95, color=RED if form == PAST else BLUE)

    if form == PARTICIPLE:
        painter.fill_ellipse(center=(skeleton.neck[0], skeleton.neck[1] + 6), radius_x=66, radius_y=22, shade=solid(ORANGE))
        painter.fill_polygon(
            points=[(skeleton.neck[0] + 20, skeleton.neck[1] + 14), (skeleton.neck[0] + 60, skeleton.neck[1] + 8), (skeleton.neck[0] + 70, skeleton.neck[1] + 120), (skeleton.neck[0] + 34, skeleton.neck[1] + 120)],
            shade=solid(ORANGE),
        )


def paint_have_scene(painter, form):
    Character(hip=(380, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(110, 30), eyes="happy", mouth="grin"))

    for index in range((2, 4, 6)[form]):
        draw_coin(painter=painter, center=(720 + (index % 2) * 18, 800 - index * 34), radius=52)

    if form == PARTICIPLE:
        draw_heart(painter=painter, center=(520, 300), size=40)


def paint_do_scene(painter, form):
    skeleton = Character(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 90), eyes="closed", mouth="smile"))
    draw_clipboard(painter=painter, center=(740, 580), width=260, height=360, row_count=3, checked_count=(0, 2, 3)[form])
    draw_pencil(painter=painter, tip=(skeleton.right_hand[0] + 30, skeleton.right_hand[1] + 30), angle=-50)

    if form == PARTICIPLE:
        draw_trophy(painter=painter, center=(740, 280), size=0.7)


def paint_be_scene(painter, form):
    if form == INFINITIVE:
        Character(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-40, 0), right_arm=(40, 0), eyes="closed", mouth="smile"))
        draw_pin(painter=painter, center=(512, 110), color=RED)
        draw_sparkle(painter=painter, center=(300, 360), size=34)
        draw_sparkle(painter=painter, center=(730, 380), size=28)
    elif form == PAST:
        Character(hip=STAND_HIP, fade=0.6).draw(painter=painter, pose=Pose(left_arm=(-40, 0), right_arm=(40, 0), eyes="closed", mouth="smile"))
        draw_pin(painter=painter, center=(512, 110), color=GRAY)
        paint_past_clock(painter=painter)
    else:
        Character(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(50, -100), eyes="happy", mouth="grin"))

        for center in ((300, 250), (512, 130), (724, 250)):
            draw_pin(painter=painter, center=center, size=0.6, color=GREEN)
            draw_check_mark(painter=painter, center=center, size=14, color=(255, 255, 255), width=7)


def paint_become_scene(painter, form):
    painter.fill_polygon(
        points=[(450, 470), (574, 470), (700, 800), (324, 800)],
        shade=solid(CAPE_COLOR),
    )
    skeleton = Character(hip=STAND_HIP).draw(painter=painter, pose=CHEER_POSE if form == PARTICIPLE else Pose(eyes="happy", mouth="smile"))

    if form == INFINITIVE:
        draw_crown(painter=painter, center=(512, 150), size=40)
        draw_sparkle(painter=painter, center=(400, 200), size=26)
    elif form == PAST:
        draw_crown(painter=painter, center=(512, 200), size=56)
        draw_sparkle(painter=painter, center=(380, 220), size=30)
        draw_sparkle(painter=painter, center=(650, 230), size=30)
    else:
        draw_crown(painter=painter, center=(skeleton.head[0], skeleton.head[1] - 120), size=62)
        draw_star(painter=painter, center=(300, 360), size=34)
        draw_star(painter=painter, center=(730, 340), size=30)


def paint_lead_scene(painter, form):
    follower_count = 2 if form == INFINITIVE else 3

    for index in range(follower_count):
        follower = Character(hip=(180 + index * 120, 700 + (index % 2) * 40), scale=0.5, shirt=FOLLOWER_SHIRTS[index])
        follower.draw(painter=painter, pose=Pose(mouth="smile", left_arm=(-24, 10), right_arm=(24, -10)))

    leader = Character(hip=(640, 620))
    skeleton = leader.draw(painter=painter, pose=Pose(lean=4, left_arm=(-14, 0), right_arm=(40, 10), eyes="happy", mouth="grin"))
    draw_flag(painter=painter, pole_bottom=(skeleton.right_hand[0], skeleton.right_hand[1] + 60), pole_height=340, width=140, height=90, color=GREEN)

    if form == PARTICIPLE:
        draw_star(painter=painter, center=(840, 330), size=36)
        draw_sparkle(painter=painter, center=(420, 330), size=30)


SCENES = {
    "make": paint_make_scene,
    "build": paint_build_scene,
    "break": paint_break_scene,
    "cut": paint_cut_scene,
    "grow": paint_grow_scene,
    "wear": paint_wear_scene,
    "have": paint_have_scene,
    "do": paint_do_scene,
    "be": paint_be_scene,
    "become": paint_become_scene,
    "lead": paint_lead_scene,
}
