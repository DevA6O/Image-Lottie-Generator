"""
Scene for the irregular verb "break" (broke, broken).
Output: break_infinitive.png, break_past.png and break_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import draw_shards, draw_star, draw_sweat_drop, draw_vase
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock
from verbs.verb_painter import build_polyline_points

VASE_COLOR = (90, 180, 210)


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


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="break", paint_scene=paint_break_scene)
