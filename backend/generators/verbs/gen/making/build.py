"""
Scene for the irregular verb "build" (built, built).
Output: build_infinitive.png, build_past.png and build_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from painting.flat_painter import move_point
from verbs.props import draw_brick_wall, draw_hammer, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE, PAST, paint_past_clock

MILO_HIP = (330, 620)
HAMMER_ARM = (95, 0)    # Straight, the hand grips the handle
HAMMER_SIZE = 0.8
HAMMER_ANGLE = 150    # From the head to the handle end: the head points to the wall
HEAD_TO_GRIP_DISTANCE = 96


def paint_build_scene(painter, form):
    builder = Milo(hip=MILO_HIP)
    pose = Pose(left_arm=(-14, 0), right_arm=HAMMER_ARM, eyes="happy", mouth="grin")
    hand = builder.build_skeleton(pose=pose).right_hand
    hammer_head = move_point(point=hand, angle=HAMMER_ANGLE + 180, distance=HEAD_TO_GRIP_DISTANCE)
    draw_hammer(painter=painter, center=hammer_head, size=HAMMER_SIZE, angle=HAMMER_ANGLE)
    builder.draw(painter=painter, pose=pose)
    draw_brick_wall(painter=painter, left_bottom=(660, 836), column_count=3, row_count=(1, 3, 5)[form])

    if form == PAST:
        paint_past_clock(painter=painter, center=(780, 330))
    elif form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(780, 330), size=36)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="build", paint_scene=paint_build_scene)
