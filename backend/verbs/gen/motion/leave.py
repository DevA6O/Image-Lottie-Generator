"""
Scene for the irregular verb "leave" (left, left).
Output: leave_infinitive.png, leave_past.png and leave_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import draw_door, draw_footprints
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE, PAST
from verbs.verb_painter import solid

WALK_POSE_WAVING = Pose(lean=4, head_tilt=-6, left_arm=(-12, 0), right_arm=(150, 40), left_leg=(-20, 6), right_leg=(22, -12), eyes="happy")


def paint_leave_scene(painter, form):
    draw_door(painter=painter, bottom_center=(250, 836), width=150, height=320, is_open=True)

    if form == PARTICIPLE:
        draw_footprints(painter=painter, start=(380, 830), end=(660, 830), count=5)
        Character(hip=(800, 700), scale=0.5).draw(painter=painter, pose=Pose(right_arm=(150, 40)))
        return
    traveler = Character(hip=(610, 600))
    skeleton = traveler.draw(painter=painter, pose=WALK_POSE_WAVING)
    suitcase_center = (skeleton.left_hand[0], skeleton.left_hand[1] + 36)
    painter.fill_rounded_rect(box=(suitcase_center[0] - 48, suitcase_center[1] - 36, suitcase_center[0] + 48, suitcase_center[1] + 40), radius=10, shade=solid((184, 100, 70)))
    painter.fill_stroke(start=(suitcase_center[0] - 20, suitcase_center[1] - 36), end=(suitcase_center[0] + 20, suitcase_center[1] - 36), width=12, shade=solid((120, 70, 50)))

    if form == PAST:
        draw_footprints(painter=painter, start=(400, 830), end=(480, 830), count=2)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="leave", paint_scene=paint_leave_scene)
