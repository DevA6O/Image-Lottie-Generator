"""
Scene for the irregular verb "speak" (spoke, spoken).
Output: speak_infinitive.png, speak_past.png and speak_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import draw_microphone, draw_music_note, draw_sound_waves, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE, PAST


def paint_speak_scene(painter, form):
    skeleton = Character(hip=(400, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(60, 120), mouth="open", eyes="happy"))
    microphone_center = (skeleton.right_hand[0] + 10, skeleton.right_hand[1] - 40)
    draw_microphone(painter=painter, center=microphone_center, size=0.8)
    draw_sound_waves(painter=painter, center=(microphone_center[0] + 40, microphone_center[1]), size=1.0, facing=1)

    if form == PAST:
        draw_music_note(painter=painter, center=(820, 560), size=0.9)
    elif form == PARTICIPLE:
        draw_star(painter=painter, center=(800, 600), size=40)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="speak", paint_scene=paint_speak_scene)
