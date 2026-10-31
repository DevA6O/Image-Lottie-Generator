"""
Duck image, drawn from scratch.
Output: duck.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE

YELLOW = (255, 222, 96)
WING = (244, 190, 62)
BEAK = (250, 140, 40)
FOOT = (250, 140, 40)


def paint_feet(painter):
    for foot_x in (460, 600):
        painter.line(points=[(foot_x, 790), (foot_x, 850)], width=20, color=FOOT)
        painter.blob(center=(foot_x - 24, 870), radius_x=62, radius_y=24, color=FOOT)


def paint_body(painter):
    painter.soft_polygon(points=[(740, 600), (890, 470), (850, 680)], color=YELLOW, softness=60)
    painter.blob(center=(530, 640), radius_x=330, radius_y=190, color=YELLOW)
    painter.blob(center=(560, 650), radius_x=190, radius_y=100, color=WING, angle=14)


def paint_head(painter):
    painter.body_curve(points=[(340, 450), (390, 540)], width=210, color=YELLOW)
    painter.blob(center=(330, 390), radius_x=140, radius_y=135, color=YELLOW)
    painter.soft_polygon(points=[(235, 380), (95, 400), (95, 440), (240, 470)], color=BEAK, softness=40)
    painter.spot(center=(300, 350), radius_x=22, radius_y=22, color=EYE)
    painter.spot(center=(293, 342), radius_x=7, radius_y=7, color=(255, 255, 255))


def render_duck_image():
    painter = AnimalPainter()
    paint_feet(painter)
    paint_body(painter)
    paint_head(painter)
    painter.save_image(name="duck")


if __name__ == "__main__":
    render_duck_image()
