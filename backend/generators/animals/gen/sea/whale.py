"""
Whale image, drawn from scratch.
Output: whale.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_width_profile, sample_curve, solid

SKIN = (76, 128, 214)
BELLY = (186, 216, 248)
FIN = (60, 104, 190)
SPOUT = (150, 214, 250)


def paint_tail(painter):
    tail_points = sample_curve(start=(640, 600), first_control=(780, 600), second_control=(860, 520), end=(850, 380))
    painter.fill_tapered_curve(points=tail_points, widths=build_width_profile(stops=[(0.0, 190), (1.0, 50)]), shade=solid(SKIN))

    painter.blob(center=(790, 330), radius_x=120, radius_y=48, color=FIN, angle=-48)
    painter.blob(center=(910, 340), radius_x=120, radius_y=48, color=FIN, angle=48)


def paint_body(painter):
    body_mask = painter.build_rotated_ellipse_mask(center=(440, 610), radius_x=340, radius_y=235)
    painter.fill(mask=body_mask, shade=solid(SKIN))
    painter.fill_ellipse(center=(400, 780), radius_x=370, radius_y=130, shade=solid(BELLY), clip=body_mask)

    painter.blob(center=(480, 760), radius_x=120, radius_y=40, color=FIN, angle=30)


def paint_face_and_spout(painter):
    painter.spot(center=(250, 590), radius_x=22, radius_y=22, color=EYE)
    painter.spot(center=(244, 583), radius_x=7, radius_y=7, color=(255, 255, 255))
    painter.arc_line(center=(240, 560), radius=130, start_angle=30, end_angle=80, width=12, color=FIN)

    for drop_x, drop_y in ((330, 300), (400, 235), (470, 300)):
        painter.blob(center=(drop_x, drop_y), radius_x=24, radius_y=42, color=SPOUT)


def render_whale_image():
    painter = AnimalPainter()
    paint_tail(painter)
    paint_body(painter)
    paint_face_and_spout(painter)
    painter.save_image(name="whale")


if __name__ == "__main__":
    render_whale_image()
