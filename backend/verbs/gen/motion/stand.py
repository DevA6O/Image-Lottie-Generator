"""
Scene for the irregular verb "stand" (stood, stood).
Output: stand_infinitive.png, stand_past.png and stand_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import BLUE, ORANGE, draw_arrow, draw_chair, draw_flag
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST


def paint_stand_scene(painter, form):

    if form == INFINITIVE:
        draw_chair(painter=painter, seat_center=(300, 690))
        rising_pose = Pose(lean=14, left_arm=(45, 10), right_arm=(60, 10), left_leg=(-20, 25), right_leg=(16, 20), mouth="open")
        Character(hip=(480, 560)).draw(painter=painter, pose=rising_pose)
        draw_arrow(painter=painter, start=(800, 720), end=(800, 540), color=BLUE)
        return

    hands_on_hips_pose = Pose(left_arm=(-50, 100), right_arm=(50, -100), mouth="grin")

    if form == PAST:
        draw_chair(painter=painter, seat_center=(250, 690))
        Character(hip=(550, 600)).draw(painter=painter, pose=hands_on_hips_pose)
        return

    Character(hip=(512, 600)).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(120, 70), eyes="happy", mouth="grin"))
    draw_flag(painter=painter, pole_bottom=(760, 836), pole_height=300, width=130, height=84, color=ORANGE)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="stand", paint_scene=paint_stand_scene)
