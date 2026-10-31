"""
Ostrich image, drawn from scratch.
Output: ostrich.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import sample_curve

BLACK = (52, 52, 64)
WHITE = (248, 246, 240)
SKIN = (238, 186, 176)
BEAK = (250, 206, 176)
LEG_WIDTH = 46


def paint_legs(painter):
    for leg_x in (540, 650):
        painter.line(points=[(leg_x, 690), (leg_x - 10, 920)], width=LEG_WIDTH, color=SKIN)
        painter.blob(center=(leg_x - 40, 940), radius_x=70, radius_y=28, color=SKIN)


def paint_body(painter):
    painter.blob(center=(850, 480), radius_x=90, radius_y=70, color=WHITE, angle=-20)
    painter.blob(center=(850, 570), radius_x=90, radius_y=70, color=WHITE, angle=20)
    painter.blob(center=(590, 560), radius_x=285, radius_y=195, color=BLACK)
    painter.blob(center=(640, 530), radius_x=190, radius_y=100, color=WHITE, angle=14)


def paint_neck_and_head(painter):
    neck_points = sample_curve(start=(430, 520), first_control=(290, 470), second_control=(470, 280), end=(360, 170))
    painter.body_curve(points=neck_points, width=80, color=SKIN)
    painter.blob(center=(340, 150), radius_x=70, radius_y=52, color=SKIN)
    painter.soft_polygon(points=[(280, 140), (200, 150), (200, 175), (285, 178)], color=BEAK, softness=22)
    painter.spot(center=(335, 135), radius_x=24, radius_y=24, color=(255, 255, 255))
    painter.spot(center=(330, 137), radius_x=14, radius_y=14, color=EYE)


def render_ostrich_image():
    painter = AnimalPainter()
    paint_legs(painter)
    paint_body(painter)
    paint_neck_and_head(painter)
    painter.save_image(name="ostrich")


if __name__ == "__main__":
    render_ostrich_image()
