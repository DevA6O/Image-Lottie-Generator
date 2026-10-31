"""
Scene for the irregular verb "hear" (heard, heard).
Output: hear_infinitive.png, hear_past.png and hear_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import BLUE, draw_heart, draw_music_note, draw_sound_waves
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, paint_past_clock


def paint_hear_scene(painter, form):
    pose = Pose(head_tilt=10, left_arm=(-14, 0), right_arm=(120, 90), eyes="closed", mouth="smile")
    Milo(hip=(400, 620)).draw(painter=painter, pose=pose)
    draw_sound_waves(painter=painter, center=(860, 450), size=1.0, facing=-1)
    draw_music_note(painter=painter, center=(720, 300), size=0.9)

    if form != INFINITIVE:
        draw_music_note(painter=painter, center=(840, 240), size=0.7, color=BLUE)

    if form == PARTICIPLE:
        draw_heart(painter=painter, center=(240, 330), size=34)
    elif form != INFINITIVE:
        paint_past_clock(painter=painter, center=(210, 250))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="hear", paint_scene=paint_hear_scene)
