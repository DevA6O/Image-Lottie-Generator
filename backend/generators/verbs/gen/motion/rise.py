"""
Scene for the irregular verb "rise" (rose, risen).
Output: rise_infinitive.png, rise_past.png and rise_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.milo.milo import Milo
from character.poses import CHEER_POSE
from verbs.props import GREEN, draw_arrow, draw_sparkle, draw_sun
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PAST, PARTICIPLE, paint_past_clock

SUN_X = 230
SUN_HEIGHTS = (770, 600, 400)    # Low, halfway, high: one per form
ARROW_X = 430


def paint_rise_scene(painter, form):
    draw_sun(painter=painter, center=(SUN_X, SUN_HEIGHTS[form]), radius=80)
    Milo(hip=(680, 600)).draw(painter=painter, pose=CHEER_POSE)

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(SUN_X + 190, 280), size=36)
        return

    draw_arrow(painter=painter, start=(ARROW_X, 760), end=(ARROW_X, 580), color=GREEN)

    if form == PAST:
        paint_past_clock(painter=painter, center=(ARROW_X, 250))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="rise", paint_scene=paint_rise_scene)
