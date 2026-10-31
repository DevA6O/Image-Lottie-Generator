"""
Spider image, drawn from scratch.
Output: spider.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE

BODY = (92, 70, 124)
LEG = (70, 54, 98)
MARK = (172, 140, 206)
EYE_WHITE = (255, 255, 255)
LEG_COUNT_PER_SIDE = 4
LEG_WIDTH = 26


def paint_legs(painter):
    for side in (-1, 1):
        for leg_index in range(LEG_COUNT_PER_SIDE):
            hip = (512 + side * 80, 420 + leg_index * 45)
            knee = (512 + side * (230 + leg_index * 18), 270 + leg_index * 85)
            foot = (512 + side * (330 - leg_index * 12 + leg_index * 25), 470 + leg_index * 120)
            painter.line(points=[hip, knee, foot], width=LEG_WIDTH, color=LEG)


def paint_body(painter):
    painter.blob(center=(512, 680), radius_x=175, radius_y=205, color=BODY)
    painter.spot(center=(512, 690), radius_x=48, radius_y=95, color=MARK)
    painter.blob(center=(512, 440), radius_x=120, radius_y=105, color=BODY)


def paint_eyes(painter):
    for side in (-1, 1):
        painter.spot(center=(512 + side * 48, 410), radius_x=34, radius_y=34, color=EYE_WHITE)
        painter.spot(center=(512 + side * 48, 414), radius_x=19, radius_y=19, color=EYE)
        painter.spot(center=(512 + side * 100, 440), radius_x=14, radius_y=14, color=EYE_WHITE)
        painter.spot(center=(512 + side * 100, 442), radius_x=8, radius_y=8, color=EYE)


def render_spider_image():
    painter = AnimalPainter()
    paint_legs(painter)
    paint_body(painter)
    paint_eyes(painter)
    painter.save_image(name="spider")


if __name__ == "__main__":
    render_spider_image()
