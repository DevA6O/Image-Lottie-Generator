"""
Scene for the irregular verb "meet" (met, met).
Output: meet_infinitive.png, meet_past.png and meet_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.character import CHEER_POSE, Character, Pose, build_partner
from verbs.props import BLUE, PINK, draw_arrow, draw_heart, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE


def paint_meet_scene(painter, form):
    left_pose = Pose(left_arm=(-14, 0), right_arm=(73, 0), mouth="grin", eyes="happy")
    right_pose = Pose(left_arm=(-70, 0), right_arm=(14, 0), mouth="grin", eyes="happy")

    if form == PARTICIPLE:
        Character(hip=(340, 620)).draw(painter=painter, pose=CHEER_POSE)
        build_partner(hip=(700, 620)).draw(painter=painter, pose=CHEER_POSE)
        draw_star(painter=painter, center=(520, 360), size=40)
        return

    Character(hip=(340, 620)).draw(painter=painter, pose=left_pose)
    build_partner(hip=(700, 620)).draw(painter=painter, pose=right_pose)

    if form == INFINITIVE:
        draw_arrow(painter=painter, start=(300, 260), end=(440, 260), color=BLUE, width=18)
        draw_arrow(painter=painter, start=(740, 260), end=(600, 260), color=BLUE, width=18)
    else:
        draw_heart(painter=painter, center=(520, 360), size=44)
        draw_heart(painter=painter, center=(440, 300), size=24, color=PINK)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="meet", paint_scene=paint_meet_scene)
