"""
Scene for the irregular verb "send" (sent, sent).
Output: send_infinitive.png, send_past.png and send_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import GREEN, RED, draw_check_mark, draw_envelope, draw_paper_plane, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE
from verbs.verb_painter import solid


def paint_send_scene(painter, form):
    pose = Pose(left_arm=(-14, 0), right_arm=(140, 20), mouth="grin", eyes="happy")

    if form == PARTICIPLE:
        Character(hip=(330, 620)).draw(painter=painter, pose=pose)
        draw_envelope(painter=painter, center=(760, 560), width=220, height=150)
        draw_check_mark(painter=painter, center=(760, 560), size=36, color=GREEN)
        return

    Character(hip=(360, 620)).draw(painter=painter, pose=pose)

    if form == INFINITIVE:
        draw_wind_lines(painter=painter, origin=(660, 330), length=150, count=3)
        draw_paper_plane(painter=painter, center=(760, 320), size=1.1, rotation=-20)
    else:
        draw_wind_lines(painter=painter, origin=(660, 330), length=150, count=3)
        draw_envelope(painter=painter, center=(780, 320), width=170, height=116)
        painter.fill_circle(center=(780, 340), radius=16, shade=solid(RED))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="send", paint_scene=paint_send_scene)
