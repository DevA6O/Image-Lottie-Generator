"""
Scene for the irregular verb "bring" (brought, brought).
Output: bring_infinitive.png, bring_past.png and bring_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import Character, Pose
from verbs.props import BLUE, BROWN, RED, draw_arrow, draw_gift_box, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE
from verbs.verb_painter import solid


def _draw_house(
    painter,
    bottom_center,
):
    wall_box = (bottom_center[0] - 90, bottom_center[1] - 140, bottom_center[0] + 90, bottom_center[1])
    painter.fill_rounded_rect(box=wall_box, radius=6, shade=solid((246, 226, 190)))
    painter.fill_polygon(
        points=[(wall_box[0] - 20, wall_box[1] + 6), (bottom_center[0], wall_box[1] - 90), (wall_box[2] + 20, wall_box[1] + 6)],
        shade=solid(RED),
    )
    painter.fill_rounded_rect(box=(bottom_center[0] - 24, bottom_center[1] - 80, bottom_center[0] + 24, bottom_center[1]), radius=6, shade=solid(BROWN))


def paint_bring_scene(painter, form):
    house_x = 800

    if form == PARTICIPLE:
        _draw_house(painter=painter, bottom_center=(house_x, 836))
        Character(hip=(440, 620)).draw(painter=painter, pose=Pose(eyes="happy", mouth="grin", left_arm=(-50, 100), right_arm=(50, -100)))
        draw_gift_box(painter=painter, center=(620, 790), size=0.7)
        return

    walking_pose = Pose(lean=6, left_arm=(60, 90), right_arm=(70, 90), left_leg=(-24, 6), right_leg=(26, -14), mouth="smile")
    skeleton = Character(hip=(400 if form == INFINITIVE else 480, 620)).draw(painter=painter, pose=walking_pose)
    draw_gift_box(painter=painter, center=(skeleton.right_hand[0] + 10, skeleton.right_hand[1] - 70), size=0.7)
    _draw_house(painter=painter, bottom_center=(house_x, 836))

    if form == INFINITIVE:
        draw_arrow(painter=painter, start=(480, 300), end=(680, 300), color=BLUE)
    else:
        draw_wind_lines(painter=painter, origin=(250, 560), length=140, count=3)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="bring", paint_scene=paint_bring_scene)
