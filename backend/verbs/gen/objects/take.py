"""
Scene for the irregular verb "take" (took, taken).
Output: take_infinitive.png, take_past.png and take_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import WOOD, draw_gift_box, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST
from verbs.verb_painter import solid


def paint_take_scene(painter, form):
    if form == INFINITIVE:
        painter.fill_rounded_rect(box=(660, 560, 900, 590), radius=8, shade=solid(WOOD))
        draw_gift_box(painter=painter, center=(780, 500), size=0.75)
        Character(hip=(360, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(100, 5), eyes="side", mouth="open"))
    elif form == PAST:
        skeleton = Character(hip=(460, 620)).draw(painter=painter, pose=Pose(left_arm=(70, 20), right_arm=(110, 10), eyes="happy", mouth="grin"))
        draw_gift_box(painter=painter, center=(skeleton.right_hand[0] + 30, skeleton.right_hand[1] - 40), size=0.7)
    else:
        Character(hip=(420, 620)).draw(painter=painter, pose=Pose(left_arm=(70, 30), right_arm=(110, 10), eyes="happy", mouth="grin"))
        draw_gift_box(painter=painter, center=(560, 560), size=0.8)
        draw_wind_lines(painter=painter, origin=(200, 560), length=120, count=2)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="take", paint_scene=paint_take_scene)
