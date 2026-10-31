"""
Shark image, drawn from scratch.
Output: shark.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_width_profile, sample_curve, solid

SKIN = (112, 138, 168)
BELLY = (236, 242, 248)
FIN = (86, 110, 142)
TOOTH = (255, 255, 255)
MOUTH = (70, 60, 80)
BODY_WIDTHS = [(0.0, 30), (0.2, 190), (0.45, 270), (0.8, 110), (1.0, 60)]


def build_body_points():
    return sample_curve(start=(110, 560), first_control=(350, 560), second_control=(560, 480), end=(780, 520))


def paint_fins(painter):
    painter.soft_polygon(points=[(380, 420), (520, 190), (640, 430)], color=FIN, softness=40)
    painter.soft_polygon(points=[(740, 520), (900, 300), (880, 520), (920, 760)], color=FIN, softness=44)
    painter.soft_polygon(points=[(420, 690), (350, 830), (560, 700)], color=FIN, softness=36)


def paint_body(painter):
    points = build_body_points()
    body_mask = painter.build_tapered_curve_mask(points=points, widths=build_width_profile(stops=BODY_WIDTHS))
    painter.fill(mask=body_mask, shade=solid(SKIN))

    belly_points = [(x - 20, y + 130) for x, y in points[10:140]]
    painter.fill_curve(points=belly_points, width=130, shade=solid(BELLY), clip=body_mask)

    for gill_x in (330, 370, 410):
        painter.arc_line(center=(gill_x - 70, 540), radius=90, start_angle=-30, end_angle=30, width=10, color=FIN)


def paint_face(painter):
    painter.spot(center=(240, 500), radius_x=22, radius_y=22, color=EYE)
    painter.spot(center=(234, 493), radius_x=7, radius_y=7, color=(255, 255, 255))
    painter.line(points=[(125, 590), (260, 640), (360, 620)], width=12, color=MOUTH)

    for tooth_x, tooth_y in ((170, 600), (225, 622), (280, 630)):
        painter.flat_soft_polygon(points=[(tooth_x - 16, tooth_y), (tooth_x + 16, tooth_y + 6), (tooth_x, tooth_y + 44)], color=TOOTH, softness=6)


def render_shark_image():
    painter = AnimalPainter()
    paint_fins(painter)
    paint_body(painter)
    paint_face(painter)
    painter.save_image(name="shark")


if __name__ == "__main__":
    render_shark_image()
