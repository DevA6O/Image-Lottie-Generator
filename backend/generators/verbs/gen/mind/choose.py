"""
Scene for the irregular verb "choose" (chose, chosen).
Output: choose_infinitive.png, choose_past.png and choose_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import CHEER_POSE
from verbs.props import GRAY, ORANGE, RED, WHITE, draw_check_mark, draw_question_mark, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock

BALL_RADIUS = 80
LEFT_BALL = (190, 560)
RIGHT_BALL = (834, 560)
MILO_HIP = (512, 620)
CHOSEN_COLOR = RED


def paint_choose_scene(painter, form):
    if form == INFINITIVE:
        pose = Pose(left_arm=(-95, 0), right_arm=(95, 0), eyes="side", mouth="flat", brows="raised")
        Milo(hip=MILO_HIP).draw(painter=painter, pose=pose)
        paint_ball(painter=painter, center=LEFT_BALL, color=ORANGE)
        paint_ball(painter=painter, center=RIGHT_BALL, color=CHOSEN_COLOR)
        draw_question_mark(painter=painter, center=(512, 190), size=0.9)
    elif form == PAST:
        pose = Pose(left_arm=(-14, 0), right_arm=(95, 0), eyes="side", mouth="smile")
        Milo(hip=MILO_HIP).draw(painter=painter, pose=pose)
        paint_ball(painter=painter, center=LEFT_BALL, color=GRAY)
        paint_ball(painter=painter, center=RIGHT_BALL, color=CHOSEN_COLOR)
        draw_check_mark(painter=painter, center=RIGHT_BALL, size=44, color=WHITE)
        paint_past_clock(painter=painter, center=(512, 170))
    else:
        Milo(hip=MILO_HIP).draw(painter=painter, pose=CHEER_POSE)
        paint_ball(painter=painter, center=RIGHT_BALL, color=CHOSEN_COLOR)
        draw_check_mark(painter=painter, center=RIGHT_BALL, size=44, color=WHITE)
        draw_star(painter=painter, center=(RIGHT_BALL[0], RIGHT_BALL[1] - 140), size=36)


def paint_ball(
    painter,
    center,
    color,
):
    painter.fill_circle(center=center, radius=BALL_RADIUS, shade=(color, color))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="choose", paint_scene=paint_choose_scene)
