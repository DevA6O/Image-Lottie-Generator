"""
Bat image, drawn from scratch.
Output: bat.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, paint_pointed_ears

BODY = (92, 76, 128)
WING = (132, 106, 176)
WING_BONE = (92, 76, 128)
EYE_YELLOW = (255, 226, 100)
FANG = (255, 252, 244)
INNER_EAR = (236, 160, 190)


def build_wing_points(side):
    wing_points = [(430, 470), (110, 300), (150, 560), (250, 540), (290, 670), (390, 610), (440, 730)]

    return [(512 + side * (512 - x), y) for x, y in wing_points]


def paint_wings(painter):
    for side in (-1, 1):
        painter.soft_polygon(points=build_wing_points(side=side), color=WING, softness=26)

        for tip in ((110, 300), (250, 540), (390, 610)):
            painter.line(points=[(512 + side * 70, 480), (512 + side * (512 - tip[0]), tip[1])], width=12, color=WING_BONE)


def paint_body(painter):
    painter.blob(center=(512, 600), radius_x=125, radius_y=170, color=BODY)
    paint_pointed_ears(painter=painter, center_x=512, base_y=360, spread=70, height=150, half_width=48, color=BODY, inner_color=INNER_EAR, lean=10)
    painter.blob(center=(512, 410), radius_x=108, radius_y=100, color=BODY)


def paint_face(painter):
    for side in (-1, 1):
        painter.spot(center=(512 + side * 45, 395), radius_x=28, radius_y=28, color=EYE_YELLOW)
        painter.spot(center=(512 + side * 45, 397), radius_x=13, radius_y=13, color=EYE)

        fang_points = [(512 + side * 28 - 14, 452), (512 + side * 28 + 14, 452), (512 + side * 28, 495)]
        painter.flat_soft_polygon(points=fang_points, color=FANG, softness=10)

    painter.arc_line(center=(512, 440), radius=34, start_angle=40, end_angle=140, width=10, color=EYE)


def render_bat_image():
    painter = AnimalPainter()
    paint_wings(painter)
    paint_body(painter)
    paint_face(painter)
    painter.save_image(name="bat")


if __name__ == "__main__":
    render_bat_image()
