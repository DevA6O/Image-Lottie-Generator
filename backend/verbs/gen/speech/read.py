"""
Scene for the irregular verb "read" (read, read).
Output: read_infinitive.png, read_past.png and read_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose, STAND_HIP
from verbs.props import BLUE, GREEN, ORANGE, draw_closed_book, draw_open_book, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE, PAST


def paint_read_scene(painter, form):
    pose = Pose(left_arm=(-40, 110), right_arm=(40, -110), eyes="closed", mouth="smile")
    Character(hip=STAND_HIP).draw(painter=painter, pose=pose)
    draw_open_book(painter=painter, center=(512, 560), width=300, height=190)

    if form == PAST:
        draw_sparkle(painter=painter, center=(780, 400), size=34)
    elif form == PARTICIPLE:
        draw_closed_book(painter=painter, center=(820, 780), width=190, height=50, color=BLUE)
        draw_closed_book(painter=painter, center=(830, 730), width=170, height=50, color=GREEN)
        draw_closed_book(painter=painter, center=(815, 680), width=180, height=50, color=ORANGE)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="read", paint_scene=paint_read_scene)
