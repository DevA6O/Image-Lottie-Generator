"""
Scene for the irregular verb "grow" (grew, grown).
Output: grow_infinitive.png, grow_past.png and grow_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import draw_plant, draw_sparkle
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE, PAST, paint_past_clock


def paint_grow_scene(painter, form):
    Milo(hip=(340, 620)).draw(painter=painter, pose=Pose(left_arm=(-50, 100), right_arm=(50, -100), eyes="happy", mouth="grin"))
    draw_plant(
        painter=painter,
        pot_center=(740, 780),
        stem_height=(90, 190, 300)[form],
        leaf_count=(2, 3, 4)[form],
        has_flower=form == PARTICIPLE,
    )

    if form != PARTICIPLE:
        draw_sparkle(painter=painter, center=(880, 540), size=30)

    if form == PAST:
        paint_past_clock(painter=painter, center=(740, 230))


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="grow", paint_scene=paint_grow_scene)
