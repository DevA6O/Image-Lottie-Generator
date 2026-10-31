"""
Scene for the irregular verb "get" (got, gotten).
Output: get_infinitive.png, get_past.png and get_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from painting.flat_painter import solid
from verbs.props import ORANGE, draw_sparkle, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock


def _draw_ball(
    painter,
    center,
    radius=46,
):
    painter.fill_circle(center=center, radius=radius, shade=solid(ORANGE))
    painter.flat_stroke(start=(center[0] - radius, center[1]), end=(center[0] + radius, center[1]), width=6, color=(150, 80, 30))
    painter.flat_stroke(start=(center[0], center[1] - radius), end=(center[0], center[1] + radius), width=6, color=(150, 80, 30))


def paint_get_scene(painter, form):
    if form == INFINITIVE:
        Milo(hip=(420, 620)).draw(painter=painter, pose=Pose(left_arm=(110, 40), right_arm=(130, 40), eyes="wide", mouth="open"))
        draw_wind_lines(painter=painter, origin=(880, 380), length=160, count=3)
        _draw_ball(painter=painter, center=(730, 380))
    elif form == PAST:
        skeleton = Milo(hip=(420, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 5), eyes="happy", mouth="grin"))
        _draw_ball(painter=painter, center=(skeleton.right_hand[0] + 40, skeleton.right_hand[1] - 20))
        paint_past_clock(painter=painter, center=(840, 230))
    else:
        skeleton = Milo(hip=(420, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(150, 0), eyes="happy", mouth="grin"))
        _draw_ball(painter=painter, center=(skeleton.right_hand[0] + 65, skeleton.right_hand[1] - 55))
        draw_sparkle(painter=painter, center=(760, 360), size=32)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="get", paint_scene=paint_get_scene)
