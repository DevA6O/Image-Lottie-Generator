"""
Scene for the irregular verb "feel" (felt, felt).
Output: feel_infinitive.png, feel_past.png and feel_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import CHEER_POSE, STAND_HIP
from verbs.props import PINK, draw_heart, draw_sparkle, draw_sweat_drop
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock


def paint_feel_scene(painter, form):
    if form == INFINITIVE:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(right_arm=(10, 210), eyes="closed", mouth="smile", head_tilt=6))
        draw_heart(painter=painter, center=(512, 180), size=56)
        draw_heart(painter=painter, center=(330, 300), size=30, color=PINK)
        draw_heart(painter=painter, center=(710, 320), size=34, color=PINK)
    elif form == PAST:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(right_arm=(10, 210), eyes="closed", mouth="sad", head_tilt=-6))
        draw_sweat_drop(painter=painter, center=(690, 380))
        draw_sweat_drop(painter=painter, center=(330, 420), radius=11)
        paint_past_clock(painter=painter, center=(800, 230))
    else:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=CHEER_POSE)
        draw_heart(painter=painter, center=(512, 150), size=56)
        draw_heart(painter=painter, center=(250, 330), size=34, color=PINK)
        draw_heart(painter=painter, center=(780, 330), size=34, color=PINK)
        draw_sparkle(painter=painter, center=(250, 520), size=30)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="feel", paint_scene=paint_feel_scene)
