"""
Scene for the irregular verb "lead" (led, led).
Output: lead_infinitive.png, lead_past.png and lead_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import GREEN, draw_flag, draw_sparkle, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, PAST, paint_past_clock

FOLLOWER_SHIRTS = ((190, 120, 220), (240, 110, 130), (70, 190, 170))


def paint_lead_scene(painter, form):
    follower_count = 2 if form == INFINITIVE else 3

    for index in range(follower_count):
        follower = Milo(hip=(180 + index * 120, 700 + (index % 2) * 40), scale=0.5, shirt=FOLLOWER_SHIRTS[index])
        follower.draw(painter=painter, pose=Pose(mouth="smile", left_arm=(-24, 10), right_arm=(24, -10)))

    leader = Milo(hip=(640, 620))
    skeleton = leader.draw(painter=painter, pose=Pose(lean=4, left_arm=(-14, 0), right_arm=(40, 10), eyes="happy", mouth="grin"))
    draw_flag(painter=painter, pole_bottom=(skeleton.right_hand[0], skeleton.right_hand[1] + 60), pole_height=340, width=140, height=90, color=GREEN)

    if form == PAST:
        paint_past_clock(painter=painter, center=(850, 230))
    elif form == PARTICIPLE:
        draw_star(painter=painter, center=(880, 170), size=36)
        draw_sparkle(painter=painter, center=(420, 330), size=30)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="lead", paint_scene=paint_lead_scene)
