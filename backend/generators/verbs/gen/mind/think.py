"""
Scene for the irregular verb "think" (thought, thought).
Output: think_infinitive.png, think_past.png and think_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from verbs.props import (
    BLUE,
    GRAY,
    draw_check_mark,
    draw_gear,
    draw_lightbulb,
    draw_question_mark,
    draw_thought_bubble,
)
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, paint_past_clock


def paint_think_scene(painter, form):
    if form == PARTICIPLE:
        Milo(hip=STAND_HIP).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(50, -100), eyes="happy", mouth="grin"))
        draw_thought_bubble(painter=painter, center=(400, 178), width=380, height=140, tail_tip=(440, 258))
        draw_lightbulb(painter=painter, center=(350, 158), size=0.6)
        draw_check_mark(painter=painter, center=(480, 183), size=34)
        return

    pose = Pose(head_tilt=8, left_arm=(-14, 0), right_arm=(40, 185), eyes="up", mouth="flat")
    Milo(hip=STAND_HIP).draw(painter=painter, pose=pose)
    draw_thought_bubble(painter=painter, center=(400, 178), width=380, height=140, tail_tip=(440, 258))

    if form == INFINITIVE:
        draw_question_mark(painter=painter, center=(400, 178), size=1.0)
    else:
        draw_gear(painter=painter, center=(350, 178), size=0.9, color=GRAY)
        draw_gear(painter=painter, center=(450, 178), size=0.7, color=BLUE)
        paint_past_clock(painter=painter)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="think", paint_scene=paint_think_scene)
