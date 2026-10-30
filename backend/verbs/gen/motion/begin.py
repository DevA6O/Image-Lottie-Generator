"""
Scene for the irregular verb "begin" (began, begun).
Output: begin_infinitive.png, begin_past.png and begin_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import CHEER_POSE, Character, Pose
from verbs.poses import RUN_POSE
from verbs.props import GREEN, draw_flag, draw_sparkle, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST


def paint_begin_scene(painter, form):
    draw_flag(painter=painter, pole_bottom=(200, 836), pole_height=330, width=140, height=90, color=GREEN)

    if form == INFINITIVE:
        ready_pose = Pose(lean=22, left_arm=(-60, -20), right_arm=(40, 20), left_leg=(-30, 40), right_leg=(35, -30), mouth="grin")
        Character(hip=(480, 600)).draw(painter=painter, pose=ready_pose)
    elif form == PAST:
        draw_wind_lines(painter=painter, origin=(520, 520), length=200, count=3)
        Character(hip=(680, 570)).draw(painter=painter, pose=RUN_POSE)
    else:
        Character(hip=(520, 600)).draw(painter=painter, pose=CHEER_POSE)
        draw_sparkle(painter=painter, center=(760, 380), size=40)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="begin", paint_scene=paint_begin_scene)
