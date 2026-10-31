"""
Scene for the irregular verb "let" (let, let).
Output: let_infinitive.png, let_past.png and let_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import BLUE, draw_arrow, draw_bird, draw_sparkle, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, paint_past_clock


def paint_let_scene(painter, form):
    pose = Pose(left_arm=(-14, 0), right_arm=(110, 30), eyes="happy", mouth="smile")

    if form == PARTICIPLE:
        Milo(hip=(380, 620)).draw(painter=painter, pose=pose)
        draw_bird(painter=painter, center=(800, 260), size=0.5, color=BLUE)
        draw_sparkle(painter=painter, center=(640, 330), size=28)
        return

    skeleton = Milo(hip=(380, 620)).draw(painter=painter, pose=pose)

    if form == INFINITIVE:
        draw_bird(painter=painter, center=(skeleton.right_hand[0] + 20, skeleton.right_hand[1] - 40), size=0.6, color=BLUE)
        draw_arrow(painter=painter, start=(700, 400), end=(860, 300), color=BLUE, width=18)
    else:
        draw_bird(painter=painter, center=(700, 300), size=0.8, color=BLUE)
        draw_wind_lines(painter=painter, origin=(610, 320), length=100, count=2)
        paint_past_clock(painter=painter, center=(880, 180))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="let", paint_scene=paint_let_scene)
