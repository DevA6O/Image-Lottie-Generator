"""
Mosquito image, drawn from scratch.
Output: mosquito.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_width_profile, sample_curve, solid

BODY = (122, 106, 100)
STRIPE = (232, 224, 214)
LEG = (74, 62, 62)
WING = (214, 228, 242)
LEG_WIDTH = 14


def paint_legs_and_wings(painter):
    painter.blob(center=(600, 380), radius_x=210, radius_y=62, color=WING, angle=-24)
    painter.blob(center=(640, 430), radius_x=190, radius_y=50, color=WING, angle=-8)

    leg_paths = (
        [(450, 540), (360, 640), (300, 850)],
        [(490, 550), (480, 700), (440, 880)],
        [(530, 540), (620, 680), (690, 870)],
        [(500, 520), (640, 600), (800, 760)],
    )

    for leg_path in leg_paths:
        painter.line(points=leg_path, width=LEG_WIDTH, color=LEG)


def paint_body(painter):
    abdomen_points = sample_curve(start=(520, 520), first_control=(640, 540), second_control=(760, 580), end=(880, 700))
    abdomen_mask = painter.build_tapered_curve_mask(points=abdomen_points, widths=build_width_profile(stops=[(0.0, 110), (0.5, 100), (1.0, 40)]))
    painter.fill(mask=abdomen_mask, shade=solid(BODY))

    for stripe_index in (45, 80, 115):
        x, y = abdomen_points[stripe_index]
        painter.fill_stroke(start=(x, y - 60), end=(x + 10, y + 60), width=16, shade=solid(STRIPE), clip=abdomen_mask)

    painter.blob(center=(470, 500), radius_x=95, radius_y=85, color=BODY)
    painter.blob(center=(375, 545), radius_x=58, radius_y=52, color=BODY)
    painter.line(points=[(345, 570), (250, 640), (140, 720)], width=12, color=LEG)
    painter.spot(center=(360, 525), radius_x=17, radius_y=17, color=EYE)
    painter.line(points=[(370, 495), (340, 440), (370, 400)], width=10, color=LEG)


def render_mosquito_image():
    painter = AnimalPainter()
    paint_legs_and_wings(painter)
    paint_body(painter)
    painter.save_image(name="mosquito")


if __name__ == "__main__":
    render_mosquito_image()
