"""
Scene for the irregular verb "meet" (met, met).
Output: meet_infinitive.png, meet_past.png and meet_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import CHEER_POSE
from verbs.partner import build_partner
from verbs.props import BLUE, PINK, draw_arrow, draw_heart, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, paint_past_clock

HANDSHAKE_HIPS = (310, 712)    # The straight arms are 164 long, so the hands meet in the middle
APART_HIPS = (250, 774)
WAVING_ARM = 125    # Raised to the side and straight


def paint_meet_scene(painter, form):
    if form == PARTICIPLE:
        Milo(hip=(340, 620)).draw(painter=painter, pose=CHEER_POSE)
        build_partner(hip=(700, 620)).draw(painter=painter, pose=CHEER_POSE)
        draw_star(painter=painter, center=(520, 360), size=40)
    elif form == INFINITIVE:
        Milo(hip=(APART_HIPS[0], 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(WAVING_ARM, 0), mouth="grin", eyes="happy"))
        build_partner(hip=(APART_HIPS[1], 620)).draw(painter=painter, pose=Pose(left_arm=(-WAVING_ARM, 0), right_arm=(14, 0), mouth="grin", eyes="happy"))
        draw_arrow(painter=painter, start=(330, 190), end=(450, 190), color=BLUE, width=18)
        draw_arrow(painter=painter, start=(700, 190), end=(580, 190), color=BLUE, width=18)
    else:
        Milo(hip=(HANDSHAKE_HIPS[0], 620)).draw(painter=painter, pose=Pose(left_arm=(-14, 0), right_arm=(90, 0), mouth="grin", eyes="happy"))
        build_partner(hip=(HANDSHAKE_HIPS[1], 620)).draw(painter=painter, pose=Pose(left_arm=(-90, 0), right_arm=(14, 0), mouth="grin", eyes="happy"))
        draw_heart(painter=painter, center=(511, 340), size=44)
        draw_heart(painter=painter, center=(440, 280), size=24, color=PINK)
        paint_past_clock(painter=painter, center=(600, 170))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="meet", paint_scene=paint_meet_scene)
