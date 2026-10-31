"""
Koala image, drawn from scratch: sitting, seen from the front.
Output: koala.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from animals.quadruped_shape import EYE_HIGHLIGHT
from painting.flat_painter import build_width_profile, solid

FUR = (162, 168, 184)
FUR_FAR = (128, 134, 152)
BELLY = (226, 230, 240)
EAR_INNER = (246, 242, 236)
NOSE_COLOR = (50, 44, 54)


def paint_body(painter):
    painter.blob(center=(512, 700), radius_x=250, radius_y=260, color=FUR)
    painter.blob(center=(512, 730), radius_x=150, radius_y=190, color=BELLY)
    painter.blob(center=(340, 880), radius_x=105, radius_y=42, color=FUR_FAR)
    painter.blob(center=(684, 880), radius_x=105, radius_y=42, color=FUR_FAR)


def paint_arms(painter):
    widths = build_width_profile(stops=[(0.0, 90), (1.0, 70)], point_count=3)

    for side in (-1, 1):
        points = [(512 + side * 200, 560), (512 + side * 235, 680), (512 + side * 215, 780)]
        painter.fill_tapered_curve(points=points, widths=widths, shade=solid(FUR_FAR))


def paint_head(painter):
    for side in (-1, 1):
        painter.blob(center=(512 + side * 215, 270), radius_x=100, radius_y=95, color=FUR)
        painter.spot(center=(512 + side * 215, 275), radius_x=62, radius_y=60, color=EAR_INNER)

    painter.blob(center=(512, 380), radius_x=215, radius_y=185, color=FUR)

    for side in (-1, 1):
        painter.spot(center=(512 + side * 95, 360), radius_x=17, radius_y=17, color=EYE)
        painter.spot(center=(512 + side * 95 - 5, 354), radius_x=6, radius_y=6, color=EYE_HIGHLIGHT)

    painter.blob(center=(512, 440), radius_x=48, radius_y=68, color=NOSE_COLOR)


def render_koala_image():
    painter = AnimalPainter()
    paint_body(painter=painter)
    paint_arms(painter=painter)
    paint_head(painter=painter)
    painter.save_image(name="koala")


if __name__ == "__main__":
    render_koala_image()
