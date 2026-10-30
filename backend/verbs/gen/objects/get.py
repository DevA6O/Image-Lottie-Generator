"""
Scene for the irregular verb "get" (got, gotten).
Output: get_infinitive.png, get_past.png and get_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import CHEER_POSE, Character, Pose
from verbs.props import ORANGE, draw_sparkle, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST
from verbs.verb_painter import solid


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


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="get", paint_scene=paint_get_scene)
