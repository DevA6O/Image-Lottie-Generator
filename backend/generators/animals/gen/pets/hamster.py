"""
Hamster image, drawn from scratch: round body seen from the side.
Output: hamster.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, NOSE
from animals.quadruped_shape import EYE_HIGHLIGHT

COAT = (226, 170, 100)
COAT_FAR = (190, 136, 72)
BELLY = (255, 238, 208)
PINK = (244, 160, 170)
EAR = (150, 98, 56)


def paint_feet(painter):
    painter.blob(center=(720, 850), radius_x=110, radius_y=50, color=PINK)
    painter.blob(center=(460, 870), radius_x=60, radius_y=45, color=PINK)
    painter.blob(center=(350, 840), radius_x=52, radius_y=44, color=PINK)


def paint_body(painter):
    painter.blob(center=(600, 640), radius_x=330, radius_y=250, color=COAT)
    painter.blob(center=(470, 720), radius_x=215, radius_y=150, color=BELLY)
    painter.blob(center=(470, 585), radius_x=130, radius_y=65, color=COAT_FAR, angle=-15)


def paint_head(painter):
    painter.blob(center=(300, 540), radius_x=215, radius_y=170, color=COAT)
    painter.blob(center=(250, 610), radius_x=120, radius_y=75, color=BELLY)
    painter.blob(center=(370, 395), radius_x=52, radius_y=52, color=EAR)
    painter.spot(center=(370, 400), radius_x=28, radius_y=28, color=PINK)
    painter.spot(center=(260, 500), radius_x=19, radius_y=19, color=EYE)
    painter.spot(center=(254, 493), radius_x=6, radius_y=6, color=EYE_HIGHLIGHT)
    painter.spot(center=(125, 545), radius_x=24, radius_y=18, color=NOSE)


def render_hamster_image():
    painter = AnimalPainter()
    paint_feet(painter=painter)
    paint_body(painter=painter)
    paint_head(painter=painter)
    painter.save_image(name="hamster")


if __name__ == "__main__":
    render_hamster_image()
