"""
Camel image, drawn from scratch.
Output: camel.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, NOSE
from painting.flat_painter import sample_curve

COAT = (222, 172, 104)
COAT_DARK = (190, 140, 84)
MUZZLE = (240, 214, 170)
LEG_WIDTH = 56


def paint_legs(painter):
    for leg_x, color in ((400, COAT_DARK), (780, COAT_DARK), (470, COAT), (700, COAT)):
        painter.line(points=[(leg_x, 700), (leg_x, 930)], width=LEG_WIDTH, color=color)
        painter.blob(center=(leg_x, 935), radius_x=40, radius_y=22, color=NOSE)


def paint_body(painter):
    painter.line(points=[(850, 600), (880, 700), (860, 780)], width=26, color=COAT_DARK)
    painter.blob(center=(590, 600), radius_x=310, radius_y=165, color=COAT)
    painter.blob(center=(650, 400), radius_x=105, radius_y=100, color=COAT)


def paint_neck_and_head(painter):
    neck_points = sample_curve(start=(380, 640), first_control=(300, 560), second_control=(320, 400), end=(250, 280))
    painter.body_curve(points=neck_points, width=120, color=COAT)
    painter.blob(center=(235, 255), radius_x=105, radius_y=72, color=COAT, angle=-18)
    painter.blob(center=(140, 290), radius_x=70, radius_y=48, color=MUZZLE, angle=-18)
    painter.blob(center=(300, 190), radius_x=26, radius_y=34, color=COAT_DARK)
    painter.spot(center=(235, 240), radius_x=15, radius_y=15, color=EYE)
    painter.spot(center=(90, 280), radius_x=10, radius_y=10, color=NOSE)


def render_camel_image():
    painter = AnimalPainter()
    paint_legs(painter)
    paint_body(painter)
    paint_neck_and_head(painter)
    painter.save_image(name="camel")


if __name__ == "__main__":
    render_camel_image()
