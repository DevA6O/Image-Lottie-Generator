"""
Sheep image, drawn from scratch: woolly body from the side.
Output: sheep.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from animals.quadruped_shape import EYE_HIGHLIGHT

WOOL = (250, 246, 238)
SKIN = (84, 74, 78)
SKIN_FAR = (62, 54, 58)
WOOL_CLUSTER = [
    ((470, 500), 150),
    ((620, 450), 165),
    ((760, 520), 150),
    ((560, 600), 170),
    ((720, 640), 150),
    ((410, 600), 120),
]
LEG_X_VALUES = (440, 520, 720, 790)


def paint_legs(painter):
    for leg_x in LEG_X_VALUES:
        color = SKIN_FAR if leg_x in (520, 720) else SKIN
        painter.line(points=[(leg_x, 650), (leg_x, 890)], width=44, color=color)
        painter.blob(center=(leg_x - 6, 892), radius_x=34, radius_y=20, color=SKIN_FAR)


def paint_wool(painter):
    for center, radius in WOOL_CLUSTER:
        painter.blob(center=center, radius_x=radius, radius_y=radius, color=WOOL)


def paint_head(painter):
    painter.blob(center=(330, 520), radius_x=70, radius_y=36, color=SKIN_FAR, angle=-20)
    painter.blob(center=(250, 560), radius_x=100, radius_y=118, color=SKIN, angle=12)
    painter.blob(center=(290, 430), radius_x=82, radius_y=62, color=WOOL)
    painter.spot(center=(230, 540), radius_x=18, radius_y=18, color=(250, 238, 200))
    painter.spot(center=(230, 540), radius_x=9, radius_y=9, color=EYE)
    painter.spot(center=(226, 535), radius_x=3, radius_y=3, color=EYE_HIGHLIGHT)
    painter.spot(center=(190, 665), radius_x=18, radius_y=12, color=SKIN_FAR)


def render_sheep_image():
    painter = AnimalPainter()
    paint_legs(painter=painter)
    paint_wool(painter=painter)
    paint_head(painter=painter)
    painter.save_image(name="sheep")


if __name__ == "__main__":
    render_sheep_image()
