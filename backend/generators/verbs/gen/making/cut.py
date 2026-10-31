"""
Scene for the irregular verb "cut" (cut, cut).
Output: cut_infinitive.png, cut_past.png and cut_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
import math

from character.figure import Pose
from character.milo.milo import Milo
from painting.flat_painter import solid
from verbs.props import draw_scissors, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

PAPER_COLOR = (250, 250, 255)
PAPER_LEFT = 724
PAPER_RIGHT = 924
PAPER_TOP = 330
PAPER_BOTTOM = 600
MILO_HIP = (330, 620)
SCISSORS_ARM = (95, 0)    # Straight, the hand is in the finger rings
SCISSORS_SIZE = 0.8
RING_DISTANCE_FROM_PIVOT = 84 * SCISSORS_SIZE
OPEN_ANGLES = {INFINITIVE: 20, PAST: 8}


def paint_cut_scene(painter, form):
    cutter = Milo(hip=MILO_HIP)
    pose = Pose(left_arm=(-14, 0), right_arm=SCISSORS_ARM, eyes="happy", mouth="smile")
    hand = cutter.build_skeleton(pose=pose).right_hand
    cut_height = hand[1]

    if form == INFINITIVE:
        paint_paper(painter=painter, box=(PAPER_LEFT, PAPER_TOP, PAPER_RIGHT, PAPER_BOTTOM))
    else:
        gap = 14 if form == PAST else 70
        paint_paper(painter=painter, box=(PAPER_LEFT, PAPER_TOP, PAPER_RIGHT, cut_height - gap / 2))
        paint_paper(painter=painter, box=(PAPER_LEFT, cut_height + gap / 2, PAPER_RIGHT, PAPER_BOTTOM))

    if form in OPEN_ANGLES:
        open_angle = OPEN_ANGLES[form]
        pivot = (hand[0] + RING_DISTANCE_FROM_PIVOT * math.cos(math.radians(open_angle)), cut_height)
        draw_scissors(painter=painter, pivot=pivot, size=SCISSORS_SIZE, open_angle=open_angle, direction=0)
        cutter.draw(painter=painter, pose=pose)
    else:
        cutter.draw(painter=painter, pose=Pose(eyes="happy", mouth="grin"))
        draw_sparkle(painter=painter, center=((PAPER_LEFT + PAPER_RIGHT) / 2, cut_height), size=36)

    if form == PAST:
        paint_past_clock(painter=painter, center=(830, 210))


def paint_paper(
    painter,
    box,
):
    painter.fill_rounded_rect(box=box, radius=8, shade=solid(PAPER_COLOR))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="cut", paint_scene=paint_cut_scene)
