"""
Scene for the irregular verb "write" (wrote, written).
Output: write_infinitive.png, write_past.png and write_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import draw_envelope, draw_heart, draw_paper, draw_pencil, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, paint_past_clock

PAPER_CENTER = (512, 560)
PENCIL_TIP = (600, 594)    # The end of the last line
PENCIL_SIZE = 0.6
PENCIL_ANGLE = -65    # The eraser points up and to the right


def paint_write_scene(painter, form):
    if form == PARTICIPLE:
        skeleton = Milo(hip=(400, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(125, 30), eyes="happy", mouth="grin"))
        envelope_center = (skeleton.right_hand[0] + 90, skeleton.right_hand[1] - 50)
        draw_envelope(painter=painter, center=envelope_center, width=220, height=150)
        draw_heart(painter=painter, center=(envelope_center[0], envelope_center[1] + 6), size=26)
        draw_star(painter=painter, center=(envelope_center[0] + 150, envelope_center[1] - 60), size=30)
        return

    if form == INFINITIVE:
        draw_paper(painter=painter, center=PAPER_CENTER, width=300, height=400, line_count=3)
        draw_pencil(painter=painter, tip=PENCIL_TIP, angle=PENCIL_ANGLE, size=PENCIL_SIZE)
    else:
        Milo(hip=(400, 620)).draw(painter=painter, pose=Pose(left_arm=(-20, 0), right_arm=(20, 0), eyes="happy", mouth="grin"))
        draw_paper(painter=painter, center=(780, 560), width=240, height=300, line_count=5)
        draw_pencil(painter=painter, tip=(690, 660), angle=-25)
        paint_past_clock(painter=painter, center=(780, 260))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="write", paint_scene=paint_write_scene)
