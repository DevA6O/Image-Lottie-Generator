"""
Scene for the irregular verb "run" (ran, run).
Output: run_infinitive.png, run_past.png and run_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.poses import RUN_POSE
from verbs.props import draw_medal, draw_sweat_drop, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock


def _hang_medal_on_neck(painter):
    def hang_medal(skeleton):
        medal_center = (skeleton.neck[0] + (skeleton.hip[0] - skeleton.neck[0]) * 0.38, skeleton.neck[1] + (skeleton.hip[1] - skeleton.neck[1]) * 0.38)
        draw_medal(painter=painter, neck=skeleton.neck, medal_center=medal_center, size=0.85)

    return hang_medal


def paint_run_scene(painter, form):
    if form == INFINITIVE:
        draw_wind_lines(painter=painter, origin=(330, 520), length=170, count=3)
        Character(hip=(540, 570)).draw(painter=painter, pose=RUN_POSE)
        draw_sweat_drop(painter=painter, center=(700, 300))
    elif form == PAST:
        Character(hip=(440, 570), fade=0.8).draw(painter=painter, pose=RUN_POSE)
        Character(hip=(580, 570), fade=0.5).draw(painter=painter, pose=RUN_POSE)
        Character(hip=(720, 570)).draw(painter=painter, pose=RUN_POSE)
        paint_past_clock(painter=painter, center=(240, 260))
    else:
        tired_pose = Pose(lean=34, head_tilt=10, left_arm=(-22, 0), right_arm=(45, 0), left_leg=(-14, 18), right_leg=(16, 10), eyes="closed", mouth="open")
        Character(hip=(512, 600)).draw(painter=painter, pose=tired_pose, before_arms=_hang_medal_on_neck(painter=painter))
        draw_sweat_drop(painter=painter, center=(700, 330))
        draw_sweat_drop(painter=painter, center=(740, 400), radius=11)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="run", paint_scene=paint_run_scene)
