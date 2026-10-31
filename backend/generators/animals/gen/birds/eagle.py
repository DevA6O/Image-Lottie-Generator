"""
Bald eagle image, drawn from scratch.
Output: eagle.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE

BROWN = (112, 74, 48)
BROWN_LIGHT = (146, 100, 66)
WHITE = (252, 250, 244)
BEAK = (252, 200, 44)
EYE_GOLD = (246, 196, 50)


def paint_body(painter):
    painter.blob(center=(580, 740), radius_x=320, radius_y=250, color=BROWN)

    for scale_x, scale_y in ((470, 730), (590, 710), (700, 740), (530, 810), (650, 820)):
        painter.arc_line(center=(scale_x, scale_y), radius=44, start_angle=20, end_angle=160, width=12, color=BROWN_LIGHT)

    painter.body_curve(points=[(500, 580), (470, 540)], width=240, color=WHITE)


def paint_head(painter):
    painter.blob(center=(450, 420), radius_x=190, radius_y=170, color=WHITE)
    painter.soft_polygon(points=[(330, 330), (180, 400), (150, 545), (210, 590), (260, 520), (340, 500)], color=BEAK, softness=30)
    painter.spot(center=(385, 405), radius_x=34, radius_y=34, color=EYE_GOLD)
    painter.spot(center=(380, 408), radius_x=15, radius_y=15, color=EYE)
    painter.line(points=[(330, 345), (440, 385)], width=22, color=WHITE)
    painter.line(points=[(355, 355), (445, 388)], width=12, color=(220, 214, 200))


def render_eagle_image():
    painter = AnimalPainter()
    paint_body(painter)
    paint_head(painter)
    painter.save_image(name="eagle")


if __name__ == "__main__":
    render_eagle_image()
