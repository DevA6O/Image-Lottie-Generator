"""
Scene for the irregular verb "wear" (wore, worn).
Output: wear_infinitive.png, wear_past.png and wear_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from painting.flat_painter import solid
from verbs.props import BLUE, ORANGE, RED, draw_hat
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import INFINITIVE, PARTICIPLE, PAST


def paint_wear_scene(painter, form):
    pose = Pose(right_arm=(150, 30), left_arm=(-14, 0), eyes="happy", mouth="smile") if form == INFINITIVE else Pose(eyes="happy", mouth="grin", left_arm=(-50, 100), right_arm=(50, -100))
    skeleton = Milo(hip=STAND_HIP).draw(painter=painter, pose=pose)

    if form == INFINITIVE:
        draw_hat(painter=painter, center=(skeleton.right_hand[0] + 10, skeleton.right_hand[1] - 40), size=0.8)
        return

    draw_hat(painter=painter, center=(skeleton.head[0], skeleton.head[1] - 62), size=0.95, color=RED if form == PAST else BLUE)

    if form == PARTICIPLE:
        painter.fill_ellipse(center=(skeleton.neck[0], skeleton.neck[1] + 6), radius_x=66, radius_y=22, shade=solid(ORANGE))
        painter.fill_polygon(
            points=[(skeleton.neck[0] + 20, skeleton.neck[1] + 14), (skeleton.neck[0] + 60, skeleton.neck[1] + 8), (skeleton.neck[0] + 70, skeleton.neck[1] + 120), (skeleton.neck[0] + 34, skeleton.neck[1] + 120)],
            shade=solid(ORANGE),
        )


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="wear", paint_scene=paint_wear_scene)
