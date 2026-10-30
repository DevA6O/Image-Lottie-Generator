"""
Scene for the irregular verb "keep" (kept, kept).
Output: keep_infinitive.png, keep_past.png and keep_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import draw_chest, draw_heart, draw_key, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE, PAST


def paint_keep_scene(painter, form):
    Character(hip=(512, 600)).draw(painter=painter, pose=Pose(left_arm=(40, 130), right_arm=(-40, -130), eyes="happy", mouth="smile"))
    draw_chest(painter=painter, center=(512, 640), size=1.1)

    if form == PAST:
        draw_key(painter=painter, center=(760, 460), size=0.9)
    elif form == PARTICIPLE:
        draw_heart(painter=painter, center=(512, 250), size=44)
        draw_sparkle(painter=painter, center=(760, 420), size=32)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="keep", paint_scene=paint_keep_scene)
