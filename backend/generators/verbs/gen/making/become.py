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
from verbs.tense import INFINITIVE, PARTICIPLE, PAST

CAPE_COLOR = (214, 70, 80)


def paint_become_scene(painter, form):
    painter.fill_polygon(
        points=[(450, 470), (574, 470), (700, 800), (324, 800)],
        shade=solid(CAPE_COLOR),
    )
    skeleton = Milo(hip=STAND_HIP).draw(painter=painter, pose=CHEER_POSE if form == PARTICIPLE else Pose(eyes="happy", mouth="smile"))

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


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="become", paint_scene=paint_become_scene)
