"""
Scene for the irregular verb "draw" (drew, drawn).
Output: draw_infinitive.png, draw_past.png and draw_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import BROWN, GOLD, draw_heart, draw_pencil, draw_star, draw_sun
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE, PAST
from verbs.verb_painter import solid


def paint_draw_scene(painter, form):
    for foot_x in (640, 740, 840):
        painter.fill_stroke(start=(740, 640), end=(foot_x, 840), width=16, shade=solid(BROWN))

    canvas_box = (610, 380, 870, 600)
    painter.fill_rounded_rect(box=canvas_box, radius=8, shade=solid(GOLD if form == PARTICIPLE else (250, 250, 255)))
    painter.fill_rounded_rect(box=(620, 390, 860, 590), radius=6, shade=solid((250, 250, 255)))
    skeleton = Character(hip=(360, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 60), eyes="closed", mouth="smile"))
    draw_pencil(painter=painter, tip=(skeleton.right_hand[0] + 40, skeleton.right_hand[1] + 10), angle=-35)

    if form == PAST:
        draw_sun(painter=painter, center=(740, 470), radius=36)
    elif form == PARTICIPLE:
        draw_sun(painter=painter, center=(700, 470), radius=30)
        draw_heart(painter=painter, center=(800, 500), size=34)
        draw_star(painter=painter, center=(880, 380), size=30)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="draw", paint_scene=paint_draw_scene)
