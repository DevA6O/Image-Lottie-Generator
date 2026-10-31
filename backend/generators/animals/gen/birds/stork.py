"""
Stork image, drawn from scratch.
Output: stork.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import sample_curve

WHITE = (250, 250, 252)
BLACK = (50, 50, 62)
RED = (232, 66, 56)
LEG_WIDTH = 24


def paint_legs(painter):
    for foot_x in (540, 640):
        painter.line(points=[(foot_x, 620), (foot_x + 10, 930)], width=LEG_WIDTH, color=RED)
        painter.line(points=[(foot_x - 40, 940), (foot_x + 10, 930), (foot_x + 60, 945)], width=20, color=RED)


def paint_body(painter):
    painter.soft_polygon(points=[(760, 480), (910, 560), (790, 600)], color=BLACK, softness=40)
    painter.blob(center=(570, 500), radius_x=260, radius_y=150, color=WHITE, angle=8)
    painter.blob(center=(630, 490), radius_x=180, radius_y=80, color=BLACK, angle=10)


def paint_neck_and_head(painter):
    neck_points = sample_curve(start=(400, 480), first_control=(300, 440), second_control=(430, 300), end=(350, 190))
    painter.body_curve(points=neck_points, width=76, color=WHITE)
    painter.blob(center=(345, 170), radius_x=62, radius_y=52, color=WHITE)
    painter.soft_polygon(points=[(300, 160), (60, 205), (300, 195)], color=RED, softness=26)
    painter.spot(center=(335, 150), radius_x=15, radius_y=15, color=EYE)


def render_stork_image():
    painter = AnimalPainter()
    paint_legs(painter)
    paint_body(painter)
    paint_neck_and_head(painter)
    painter.save_image(name="stork")


if __name__ == "__main__":
    render_stork_image()
