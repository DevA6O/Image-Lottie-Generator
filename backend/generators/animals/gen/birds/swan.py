"""
Swan image, drawn from scratch.
Output: swan.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import sample_curve

WHITE = (252, 252, 254)
WING = (222, 228, 240)
BEAK = (250, 140, 44)
BLACK = (50, 48, 58)
NECK_WIDTH = 96


def paint_body(painter):
    painter.soft_polygon(points=[(740, 700), (930, 600), (850, 760)], color=WHITE, softness=60)
    painter.blob(center=(560, 770), radius_x=340, radius_y=165, color=WHITE)
    painter.blob(center=(610, 690), radius_x=230, radius_y=100, color=WING, angle=-16)


def paint_neck_and_head(painter):
    neck_points = sample_curve(start=(330, 730), first_control=(110, 640), second_control=(560, 400), end=(340, 210))
    painter.body_curve(points=neck_points, width=NECK_WIDTH, color=WHITE)
    painter.blob(center=(335, 195), radius_x=82, radius_y=68, color=WHITE)
    painter.soft_polygon(points=[(270, 180), (130, 200), (130, 232), (275, 238)], color=BEAK, softness=30)
    painter.spot(center=(265, 195), radius_x=24, radius_y=20, color=BLACK)
    painter.spot(center=(325, 170), radius_x=16, radius_y=16, color=EYE)


def render_swan_image():
    painter = AnimalPainter()
    paint_body(painter)
    paint_neck_and_head(painter)
    painter.save_image(name="swan")


if __name__ == "__main__":
    render_swan_image()
