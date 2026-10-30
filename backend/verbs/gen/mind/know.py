"""
Scene for the irregular verb "know" (knew, known).
Output: know_infinitive.png, know_past.png and know_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose, STAND_HIP
from verbs.props import draw_heart, draw_lightbulb, draw_sparkle, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, PAST, paint_past_clock


def paint_know_scene(painter, form):
    if form == PARTICIPLE:
        Character(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(50, -100), eyes="happy", mouth="grin"))
        draw_star(painter=painter, center=(512, 170), size=80)
        draw_heart(painter=painter, center=(300, 320), size=40)
        draw_heart(painter=painter, center=(724, 320), size=40)
        draw_sparkle(painter=painter, center=(380, 200), size=30)
        draw_sparkle(painter=painter, center=(650, 190), size=30)
        return

    pose = Pose(left_arm=(-50, 100), right_arm=(130, 40), eyes="happy", mouth="smile", brows="raised")
    Character(hip=STAND_HIP).draw(painter=painter, pose=pose)
    draw_lightbulb(painter=painter, center=(512, 130), size=0.9, glowing=form == INFINITIVE)

    if form == PAST:
        paint_past_clock(painter=painter)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="know", paint_scene=paint_know_scene)
