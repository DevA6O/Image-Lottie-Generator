"""
Scene for the irregular verb "lose" (lost, lost).
Output: lose_infinitive.png, lose_past.png and lose_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from verbs.props import BLUE, GRAY, draw_arrow, draw_coin, draw_question_mark, draw_sweat_drop
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

GHOST_COIN_CENTER = (780, 740)
GHOST_COIN_RADIUS = 50
GHOST_COIN_LIGHT = (214, 220, 232)


def paint_lose_scene(painter, form):
    if form == INFINITIVE:
        slipping_pose = Pose(left_arm=(-60, 0), right_arm=(60, 0), eyes="wide", mouth="open", brows="worry")
        Milo(hip=STAND_HIP).draw(painter=painter, pose=slipping_pose)
        draw_coin(painter=painter, center=(770, 640), radius=44)
        draw_arrow(painter=painter, start=(770, 710), end=(770, 830), color=BLUE, width=18)
    elif form == PAST:
        empty_hands_pose = Pose(left_arm=(-70, 40), right_arm=(70, -40), eyes="side", mouth="sad", brows="worry")
        Milo(hip=STAND_HIP).draw(painter=painter, pose=empty_hands_pose)
        draw_question_mark(painter=painter, center=(512, 190), size=1.0)
        paint_past_clock(painter=painter, center=(840, 230))
    else:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(eyes="closed", mouth="sad", brows="worry", head_tilt=-6))
        draw_sweat_drop(painter=painter, center=(690, 380))
        draw_sweat_drop(painter=painter, center=(330, 420), radius=11)
        painter.fill_circle(center=GHOST_COIN_CENTER, radius=GHOST_COIN_RADIUS, shade=(GRAY, GRAY))
        painter.flat_circle(center=GHOST_COIN_CENTER, radius=GHOST_COIN_RADIUS * 0.6, color=GHOST_COIN_LIGHT)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="lose", paint_scene=paint_lose_scene)
