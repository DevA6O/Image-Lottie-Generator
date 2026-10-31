"""
Scene for the irregular verb "mean" (meant, meant).
Output: mean_infinitive.png, mean_past.png and mean_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from verbs.props import BLUE, GRAY, ORANGE, PINK, draw_check_mark, draw_question_mark, draw_speech_bubble
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, paint_past_clock

BUBBLE_CENTER = (430, 140)
LEFT_CIRCLE = (320, 140)
RIGHT_CIRCLE = (540, 140)
EQUALS_LEFT_X = 400
EQUALS_RIGHT_X = 460
EQUALS_GAP = 22


def paint_mean_scene(painter, form):
    pose = Pose(left_arm=(-70, 40), right_arm=(70, -40), eyes="open", mouth="flat", brows="worry", head_tilt=-6)
    Milo(hip=STAND_HIP).draw(painter=painter, pose=pose)
    draw_speech_bubble(painter=painter, center=BUBBLE_CENTER, width=440, height=150, tail_tip=(470, 246))

    left_color, right_color = (GRAY, GRAY) if form == INFINITIVE else (ORANGE, PINK)
    painter.fill_circle(center=LEFT_CIRCLE, radius=40, shade=(left_color, left_color))
    painter.fill_circle(center=RIGHT_CIRCLE, radius=40, shade=(right_color, right_color))
    painter.flat_stroke(start=(EQUALS_LEFT_X, BUBBLE_CENTER[1] - EQUALS_GAP), end=(EQUALS_RIGHT_X, BUBBLE_CENTER[1] - EQUALS_GAP), width=14, color=BLUE)
    painter.flat_stroke(start=(EQUALS_LEFT_X, BUBBLE_CENTER[1] + EQUALS_GAP), end=(EQUALS_RIGHT_X, BUBBLE_CENTER[1] + EQUALS_GAP), width=14, color=BLUE)

    if form == INFINITIVE:
        draw_question_mark(painter=painter, center=(790, 360), size=0.9)
    elif form == PARTICIPLE:
        draw_check_mark(painter=painter, center=(790, 380), size=40)
    else:
        paint_past_clock(painter=painter, center=(800, 340))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="mean", paint_scene=paint_mean_scene)
