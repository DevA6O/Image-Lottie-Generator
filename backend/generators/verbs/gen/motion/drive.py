"""
Scene for the irregular verb "drive" (drove, driven).
Output: drive_infinitive.png, drive_past.png and drive_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from verbs.props import draw_car_body, draw_car_cabin, draw_sparkle, draw_wind_lines
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE


def paint_drive_scene(painter, form):
    car_center = (512, 680)

    if form != PARTICIPLE:
        draw_wind_lines(painter=painter, origin=(250, 650), length=190, count=3)
    draw_car_cabin(painter=painter, center=car_center)
    driver = Milo(hip=(440, 719), scale=0.75)
    driver.draw(painter=painter, pose=Pose(left_arm=(40, 30), right_arm=(40, 30), mouth="grin"), with_legs=False)
    draw_car_body(painter=painter, center=car_center)
    painter.fill_ring(center=(500, 600), outer_radius=34, inner_radius=22, color=(60, 66, 86))

    if form == PARTICIPLE:
        draw_sparkle(painter=painter, center=(780, 400), size=40)
        draw_sparkle(painter=painter, center=(250, 450), size=28)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="drive", paint_scene=paint_drive_scene)
