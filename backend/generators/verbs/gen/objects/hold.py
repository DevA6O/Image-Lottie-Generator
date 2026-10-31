"""
Scene for the irregular verb "hold" (held, held).
Output: hold_infinitive.png, hold_past.png and hold_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import BLUE, GREEN, RED, draw_balloon
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, PAST, paint_past_clock


def paint_hold_scene(painter, form):
    skeleton = Milo(hip=(440, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(50, 130), eyes="happy", mouth="smile"))
    anchor = skeleton.right_hand
    draw_balloon(painter=painter, center=(anchor[0] + 80, anchor[1] - 270), radius=70, color=RED, string_end=anchor)

    if form != INFINITIVE:
        draw_balloon(painter=painter, center=(anchor[0] + 190, anchor[1] - 230), radius=60, color=BLUE, string_end=anchor)

    if form == PAST:
        paint_past_clock(painter=painter, center=(180, 230))

    if form == PARTICIPLE:
        draw_balloon(painter=painter, center=(anchor[0] + 300, anchor[1] - 260), radius=56, color=GREEN, string_end=anchor)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="hold", paint_scene=paint_hold_scene)
