"""
Scene for the irregular verb "mean" (meant, meant).
Output: mean_infinitive.png, mean_past.png and mean_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose, STAND_HIP
from verbs.props import BLUE, GRAY, ORANGE, PINK, draw_check_mark, draw_question_mark, draw_speech_bubble
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE


def paint_mean_scene(painter, form):
    pose = Pose(left_arm=(-70, 40), right_arm=(70, -40), eyes="open", mouth="flat", brows="worry", head_tilt=-6)
    Character(hip=STAND_HIP).draw(painter=painter, pose=pose)
    draw_speech_bubble(painter=painter, center=(430, 190), width=440, height=170, tail_tip=(480, 300))
    left_color, right_color = (GRAY, GRAY) if form == INFINITIVE else (ORANGE, PINK)

    painter.fill_circle(center=(320, 190), radius=40, shade=(left_color, left_color))
    painter.fill_circle(center=(540, 190), radius=40, shade=(right_color, right_color))
    painter.flat_stroke(start=(400, 168), end=(460, 168), width=14, color=BLUE)
    painter.flat_stroke(start=(400, 212), end=(460, 212), width=14, color=BLUE)

    if form == INFINITIVE:
        draw_question_mark(painter=painter, center=(790, 360), size=0.9)
    elif form == PARTICIPLE:
        draw_check_mark(painter=painter, center=(790, 380), size=40)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="mean", paint_scene=paint_mean_scene)
