"""
Goose image, drawn from scratch.
Output: goose.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import sample_curve

WHITE = (250, 250, 252)
WING = (222, 228, 238)
BEAK = (250, 140, 40)
FOOT = (250, 140, 40)


def paint_feet(painter):
    for foot_x in (500, 620):
        painter.line(points=[(foot_x, 800), (foot_x, 860)], width=20, color=FOOT)
        painter.blob(center=(foot_x - 24, 880), radius_x=62, radius_y=24, color=FOOT)


def paint_body(painter):
    painter.soft_polygon(points=[(760, 640), (900, 590), (860, 720)], color=WHITE, softness=60)
    painter.blob(center=(570, 690), radius_x=310, radius_y=185, color=WHITE)
    painter.blob(center=(600, 690), radius_x=190, radius_y=96, color=WING, angle=12)


def paint_neck_and_head(painter):
    neck_points = sample_curve(start=(430, 660), first_control=(250, 560), second_control=(440, 400), end=(345, 250))
    painter.body_curve(points=neck_points, width=110, color=WHITE)
    painter.blob(center=(340, 200), radius_x=100, radius_y=88, color=WHITE)
    painter.soft_polygon(points=[(270, 180), (130, 205), (130, 240), (275, 255)], color=BEAK, softness=36)
    painter.spot(center=(320, 175), radius_x=19, radius_y=19, color=EYE)
    painter.spot(center=(314, 168), radius_x=6, radius_y=6, color=(255, 255, 255))


def render_goose_image():
    painter = AnimalPainter()
    paint_feet(painter)
    paint_body(painter)
    paint_neck_and_head(painter)
    painter.save_image(name="goose")


if __name__ == "__main__":
    render_goose_image()
