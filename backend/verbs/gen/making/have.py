"""
Scene for the irregular verb "have" (had, had).
Output: have_infinitive.png, have_past.png and have_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import draw_coin, draw_heart
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE


def paint_have_scene(painter, form):
    Character(hip=(380, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(110, 30), eyes="happy", mouth="grin"))

    for index in range((2, 4, 6)[form]):
        draw_coin(painter=painter, center=(720 + (index % 2) * 18, 800 - index * 34), radius=52)

    if form == PARTICIPLE:
        draw_heart(painter=painter, center=(520, 300), size=40)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="have", paint_scene=paint_have_scene)
