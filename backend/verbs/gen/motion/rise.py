"""
Scene for the irregular verb "rise" (rose, risen).
Output: rise_infinitive.png, rise_past.png and rise_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import CHEER_POSE, Character
from verbs.props import GREEN, draw_arrow, draw_sparkle, draw_sun
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE


def paint_rise_scene(painter, form):
    sun_height = (770, 600, 430)[form]
    draw_sun(painter=painter, center=(300, sun_height), radius=80)
    Character(hip=(650, 600)).draw(painter=painter, pose=CHEER_POSE)
    draw_arrow(painter=painter, start=(440, 700), end=(440, 520), color=GREEN)

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(520, 360), size=36)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="rise", paint_scene=paint_rise_scene)
