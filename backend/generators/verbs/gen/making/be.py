"""
Scene for the irregular verb "be" (was / were, been).
Output: be_infinitive.png, be_past.png and be_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from verbs.props import GRAY, GREEN, RED, draw_check_mark, draw_pin, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock


def paint_be_scene(painter, form):
    if form == INFINITIVE:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-40, 0), right_arm=(40, 0), eyes="closed", mouth="smile"))
        draw_pin(painter=painter, center=(512, 110), color=RED)
        draw_sparkle(painter=painter, center=(300, 360), size=34)
        draw_sparkle(painter=painter, center=(730, 380), size=28)
    elif form == PAST:
        Milo(hip=STAND_HIP, fade=0.6).draw(painter=painter, pose=Pose(left_arm=(-40, 0), right_arm=(40, 0), eyes="closed", mouth="smile"))
        draw_pin(painter=painter, center=(512, 110), color=GRAY)
        paint_past_clock(painter=painter)
    else:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(50, -100), eyes="happy", mouth="grin"))

        for center in ((300, 250), (512, 130), (724, 250)):
            draw_pin(painter=painter, center=center, size=0.6, color=GREEN)
            draw_check_mark(painter=painter, center=center, size=14, color=(255, 255, 255), width=7)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="be", paint_scene=paint_be_scene)
