"""
Scene for the irregular verb "write" (wrote, written).
Output: write_infinitive.png, write_past.png and write_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import draw_envelope, draw_heart, draw_paper, draw_pencil, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, paint_past_clock


def paint_write_scene(painter, form):
    if form == PARTICIPLE:
        skeleton = Character(hip=(400, 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(125, 30), eyes="happy", mouth="grin"))
        envelope_center = (skeleton.right_hand[0] + 90, skeleton.right_hand[1] - 50)
        draw_envelope(painter=painter, center=envelope_center, width=220, height=150)
        draw_heart(painter=painter, center=(envelope_center[0], envelope_center[1] + 6), size=26)
        draw_star(painter=painter, center=(envelope_center[0] + 150, envelope_center[1] - 60), size=30)
        return

    if form == INFINITIVE:
        writing_pose = Pose(left_arm=(-14, 0), right_arm=(80, 120), eyes="closed", mouth="smile")
        writer = Character(hip=(400, 620))
        skeleton = writer.build_skeleton(pose=writing_pose)
        pencil_tip = (skeleton.right_hand[0] + 40, skeleton.right_hand[1] + 40)
        draw_paper(painter=painter, center=(pencil_tip[0] + 120, pencil_tip[1] - 10), width=240, height=300, line_count=1)
        writer.draw(painter=painter, pose=writing_pose)
        draw_pencil(painter=painter, tip=pencil_tip, angle=-50)
    else:
        Character(hip=(400, 620)).draw(painter=painter, pose=Pose(left_arm=(-20, 0), right_arm=(20, 0), eyes="happy", mouth="grin"))
        draw_paper(painter=painter, center=(780, 560), width=240, height=300, line_count=5)
        draw_pencil(painter=painter, tip=(690, 660), angle=-25)
        paint_past_clock(painter=painter, center=(780, 260))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="write", paint_scene=paint_write_scene)
