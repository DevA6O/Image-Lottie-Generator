"""
Scene for the irregular verb "go" (went, gone).
Output: go_infinitive.png, go_past.png and go_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.milo.milo import Milo
from character.poses import WALK_POSE
from verbs.props import BLUE, draw_arrow, draw_dust_puff, draw_footprints, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PAST, paint_past_clock


def paint_go_scene(painter, form):
    if form == INFINITIVE:
        draw_wind_lines(painter=painter, origin=(330, 560), length=170, count=3)
        Milo(hip=(540, 600)).draw(painter=painter, pose=WALK_POSE)
        draw_arrow(painter=painter, start=(700, 760), end=(880, 760), color=BLUE)
    elif form == PAST:
        draw_footprints(painter=painter, start=(120, 826), end=(560, 826), count=6)
        Milo(hip=(700, 650), scale=0.72).draw(painter=painter, pose=WALK_POSE)
        paint_past_clock(painter=painter, center=(300, 300))
    else:
        draw_dust_puff(painter=painter, center=(250, 790), size=1.2)
        draw_footprints(painter=painter, start=(380, 826), end=(780, 816), count=5)
        Milo(hip=(890, 740), scale=0.4).draw(painter=painter, pose=WALK_POSE)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="go", paint_scene=paint_go_scene)
