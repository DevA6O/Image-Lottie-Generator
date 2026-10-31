"""
Kangaroo image, drawn from scratch.
Output: kangaroo.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, NOSE
from painting.flat_painter import build_width_profile, sample_curve, solid

FUR = (208, 142, 84)
FUR_DARK = (178, 112, 64)
BELLY = (246, 218, 176)
EAR_INNER = (240, 170, 160)


def paint_tail_and_legs(painter):
    tail_points = sample_curve(start=(640, 760), first_control=(820, 860), second_control=(880, 800), end=(960, 900))
    painter.fill_tapered_curve(points=tail_points, widths=build_width_profile(stops=[(0.0, 170), (1.0, 34)]), shade=solid(FUR_DARK))
    painter.blob(center=(570, 800), radius_x=190, radius_y=110, color=FUR, angle=-8)
    painter.blob(center=(430, 925), radius_x=190, radius_y=42, color=FUR_DARK, angle=-2)


def paint_body(painter):
    body_mask = painter.build_rotated_ellipse_mask(center=(500, 620), radius_x=185, radius_y=290, angle=10)
    painter.fill(mask=body_mask, shade=solid(FUR))
    painter.fill_ellipse(center=(440, 690), radius_x=120, radius_y=210, shade=solid(BELLY), clip=body_mask, angle=10)

    for hand_end in ((310, 640), (330, 700)):
        painter.line(points=[(420, 540), hand_end], width=46, color=FUR_DARK)


def paint_head(painter):
    for ear_x, ear_angle in ((470, 14), (410, -6)):
        painter.blob(center=(ear_x, 195), radius_x=30, radius_y=92, color=FUR, angle=ear_angle)
        painter.spot(center=(ear_x, 200), radius_x=14, radius_y=62, color=EAR_INNER, angle=ear_angle)

    painter.blob(center=(430, 320), radius_x=105, radius_y=115, color=FUR)
    painter.blob(center=(345, 365), radius_x=85, radius_y=62, color=FUR, angle=20)
    painter.blob(center=(270, 372), radius_x=26, radius_y=22, color=NOSE)
    painter.spot(center=(385, 300), radius_x=20, radius_y=20, color=EYE)
    painter.spot(center=(380, 293), radius_x=6, radius_y=6, color=(255, 255, 255))


def render_kangaroo_image():
    painter = AnimalPainter()
    paint_tail_and_legs(painter)
    paint_body(painter)
    paint_head(painter)
    painter.save_image(name="kangaroo")


if __name__ == "__main__":
    render_kangaroo_image()
