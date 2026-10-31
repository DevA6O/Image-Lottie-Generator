"""
Scene for the irregular verb "become" (became, become).
Output: become_infinitive.png, become_past.png and become_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import CHEER_POSE, STAND_HIP
from painting.flat_painter import solid
from verbs.props import draw_crown, draw_sparkle, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

CAPE_COLOR = (214, 70, 80)
CROWN_SIZE = 44
CROWN_ON_HEAD_Y = 258    # The crown base sinks into the hair
HANDS_ON_HIPS_POSE = Pose(eyes="happy", mouth="grin", left_arm=(-50, 100), right_arm=(50, -100))


def paint_become_scene(painter, form):
    paint_cape(painter=painter)
    pose = {INFINITIVE: HANDS_ON_HIPS_POSE, PAST: Pose(eyes="happy", mouth="smile")}.get(form, CHEER_POSE)
    skeleton = Milo(hip=STAND_HIP).draw(painter=painter, pose=pose)
    draw_crown(painter=painter, center=(skeleton.head[0] + 8, CROWN_ON_HEAD_Y), size=CROWN_SIZE)

    if form == INFINITIVE:
        draw_sparkle(painter=painter, center=(380, 200), size=30)
        draw_sparkle(painter=painter, center=(650, 230), size=24)
    elif form == PAST:
        paint_past_clock(painter=painter, center=(810, 230))
    else:
        draw_star(painter=painter, center=(300, 360), size=34)
        draw_star(painter=painter, center=(730, 340), size=30)


def paint_cape(painter):
    painter.fill_polygon(
        points=[(450, 470), (574, 470), (700, 800), (324, 800)],
        shade=solid(CAPE_COLOR),
    )


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="become", paint_scene=paint_become_scene)
