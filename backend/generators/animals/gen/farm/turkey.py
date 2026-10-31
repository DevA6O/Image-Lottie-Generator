"""
Turkey image, drawn from scratch.
Output: turkey.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_direction, solid

FEATHER = (168, 92, 52)
FEATHER_TIP = (240, 190, 110)
FEATHER_BAND = (214, 130, 60)
BODY = (146, 92, 58)
WING = (112, 70, 46)
HEAD = (236, 98, 84)
BEAK = (250, 190, 50)
LEG = (244, 170, 70)
FAN_PIVOT = (512, 640)
FAN_ANGLES = (-72, -48, -24, 0, 24, 48, 72)
FEATHER_DISTANCE = 270
FEATHER_RADIUS_X = 78
FEATHER_RADIUS_Y = 245


def paint_tail_fan(painter):
    for angle in FAN_ANGLES:
        direction = build_direction(angle_degrees=180 - angle)
        center = (FAN_PIVOT[0] + direction[0] * FEATHER_DISTANCE, FAN_PIVOT[1] + direction[1] * FEATHER_DISTANCE)
        painter.blob(center=center, radius_x=FEATHER_RADIUS_X, radius_y=FEATHER_RADIUS_Y, color=FEATHER, angle=angle)

        band_center = (FAN_PIVOT[0] + direction[0] * (FEATHER_DISTANCE + 130), FAN_PIVOT[1] + direction[1] * (FEATHER_DISTANCE + 130))
        painter.spot(center=band_center, radius_x=FEATHER_RADIUS_X * 0.6, radius_y=FEATHER_RADIUS_Y * 0.3, color=FEATHER_TIP, angle=angle)
        band_center = (FAN_PIVOT[0] + direction[0] * (FEATHER_DISTANCE + 50), FAN_PIVOT[1] + direction[1] * (FEATHER_DISTANCE + 50))
        painter.spot(center=band_center, radius_x=FEATHER_RADIUS_X * 0.7, radius_y=FEATHER_RADIUS_Y * 0.1, color=FEATHER_BAND, angle=angle)


def paint_body(painter):
    for leg_x in (450, 574):
        painter.line(points=[(leg_x, 800), (leg_x, 900)], width=22, color=LEG)
        painter.line(points=[(leg_x - 50, 910), (leg_x, 896), (leg_x + 50, 910)], width=18, color=LEG)

    painter.blob(center=(512, 690), radius_x=185, radius_y=190, color=BODY)
    painter.blob(center=(512, 720), radius_x=120, radius_y=120, color=WING)


def paint_head(painter):
    painter.blob(center=(512, 520), radius_x=48, radius_y=62, color=HEAD)
    painter.body_curve(points=[(512, 440), (512, 500)], width=62, color=HEAD)
    painter.blob(center=(512, 410), radius_x=80, radius_y=85, color=HEAD)
    painter.soft_polygon(points=[(488, 430), (536, 430), (512, 480)], color=BEAK, softness=22)
    painter.blob(center=(556, 500), radius_x=16, radius_y=46, color=(190, 56, 60))

    for eye_x in (470, 554):
        painter.spot(center=(eye_x, 385), radius_x=14, radius_y=14, color=EYE)


def render_turkey_image():
    painter = AnimalPainter()
    paint_tail_fan(painter)
    paint_body(painter)
    paint_head(painter)
    painter.save_image(name="turkey")


if __name__ == "__main__":
    render_turkey_image()
