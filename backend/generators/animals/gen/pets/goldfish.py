"""
Goldfish image, drawn from scratch.
Output: goldfish.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import solid

ORANGE = (252, 138, 52)
FIN = (255, 178, 90)
SCALE = (255, 168, 84)
BELLY = (255, 205, 140)


def paint_fins(painter):
    painter.soft_polygon(points=[(640, 520), (850, 330), (900, 520), (850, 710)], color=FIN, softness=60)
    painter.soft_polygon(points=[(330, 345), (470, 215), (640, 330), (600, 400)], color=FIN, softness=50)
    painter.soft_polygon(points=[(430, 640), (520, 760), (610, 620)], color=FIN, softness=44)


def paint_body(painter):
    body_mask = painter.build_rotated_ellipse_mask(center=(470, 520), radius_x=280, radius_y=210)
    painter.fill(mask=body_mask, shade=solid(ORANGE))
    painter.fill_ellipse(center=(450, 650), radius_x=230, radius_y=90, shade=solid(BELLY), clip=body_mask)

    for scale_x, scale_y in ((470, 470), (560, 540), (400, 560), (590, 440)):
        painter.arc_line(center=(scale_x, scale_y), radius=48, start_angle=-60, end_angle=60, width=11, color=SCALE)

    painter.arc_line(center=(390, 520), radius=140, start_angle=-50, end_angle=50, width=14, color=FIN)


def paint_face(painter):
    painter.spot(center=(290, 470), radius_x=42, radius_y=42, color=(255, 255, 255))
    painter.spot(center=(284, 472), radius_x=24, radius_y=24, color=EYE)
    painter.arc_line(center=(250, 570), radius=26, start_angle=20, end_angle=120, width=11, color=(180, 80, 40))


def render_goldfish_image():
    painter = AnimalPainter()
    paint_fins(painter)
    paint_body(painter)
    paint_face(painter)
    painter.save_image(name="goldfish")


if __name__ == "__main__":
    render_goldfish_image()
