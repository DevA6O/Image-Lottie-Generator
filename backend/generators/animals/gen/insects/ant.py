"""
Ant image, drawn from scratch.
Output: ant.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE

BODY = (178, 70, 48)
LEG = (140, 52, 40)
EYE_WHITE = (255, 255, 255)
LEG_WIDTH = 20


def paint_legs_and_antennae(painter):
    for hip_x, knee_x, foot_x in ((380, 330, 280), (430, 470, 480), (490, 590, 660)):
        painter.line(points=[(hip_x, 590), (knee_x, 710), (foot_x, 850)], width=LEG_WIDTH, color=LEG)

    for hip_x, knee_x, foot_x in ((400, 440, 400), (460, 380, 340)):
        painter.line(points=[(hip_x, 580), (knee_x, 660), (foot_x, 760)], width=LEG_WIDTH - 4, color=LEG)

    painter.line(points=[(240, 460), (190, 330), (110, 290)], width=14, color=LEG)
    painter.line(points=[(290, 450), (300, 320), (250, 240)], width=14, color=LEG)


def paint_body(painter):
    painter.line(points=[(480, 550), (560, 560)], width=36, color=LEG)
    painter.blob(center=(710, 560), radius_x=200, radius_y=155, color=BODY, angle=-6)
    painter.blob(center=(430, 530), radius_x=95, radius_y=75, color=BODY)
    painter.blob(center=(250, 520), radius_x=100, radius_y=90, color=BODY)

    painter.spot(center=(225, 495), radius_x=28, radius_y=28, color=EYE_WHITE)
    painter.spot(center=(219, 497), radius_x=15, radius_y=15, color=EYE)
    painter.line(points=[(170, 560), (200, 585)], width=12, color=LEG)


def render_ant_image():
    painter = AnimalPainter()
    paint_legs_and_antennae(painter)
    paint_body(painter)
    painter.save_image(name="ant")


if __name__ == "__main__":
    render_ant_image()
