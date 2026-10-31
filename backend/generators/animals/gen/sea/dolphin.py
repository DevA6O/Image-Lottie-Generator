"""
Dolphin image, drawn from scratch.
Output: dolphin.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_width_profile, sample_curve, solid

SKIN = (92, 150, 206)
BELLY = (214, 232, 248)
FIN = (68, 118, 180)
BODY_WIDTHS = [(0.0, 44), (0.1, 96), (0.3, 190), (0.65, 150), (1.0, 40)]


def build_body_points():
    return sample_curve(start=(130, 470), first_control=(300, 250), second_control=(700, 330), end=(770, 700))


def paint_fins(painter, body_points):
    back_point = body_points[75]
    painter.soft_polygon(points=[(back_point[0] - 60, back_point[1] - 30), (back_point[0] + 20, back_point[1] - 170), (back_point[0] + 90, back_point[1] + 10)], color=FIN, softness=36)

    tail_tip = body_points[-1]
    painter.blob(center=(tail_tip[0] - 70, tail_tip[1] + 55), radius_x=105, radius_y=38, color=FIN, angle=-25)
    painter.blob(center=(tail_tip[0] + 70, tail_tip[1] + 75), radius_x=105, radius_y=38, color=FIN, angle=35)


def paint_body(painter, body_points):
    widths = build_width_profile(stops=BODY_WIDTHS)
    body_mask = painter.build_tapered_curve_mask(points=body_points, widths=widths)
    painter.fill(mask=body_mask, shade=solid(SKIN))

    belly_points = [(x + 10, y + 70) for x, y in body_points[20:130]]
    painter.fill_curve(points=belly_points, width=70, shade=solid(BELLY), clip=body_mask)

    flipper_base = body_points[40]
    painter.blob(center=(flipper_base[0] + 50, flipper_base[1] + 150), radius_x=40, radius_y=100, color=FIN, angle=-40)


def paint_face(painter):
    painter.spot(center=(255, 385), radius_x=20, radius_y=20, color=EYE)
    painter.spot(center=(249, 378), radius_x=6, radius_y=6, color=(255, 255, 255))
    painter.arc_line(center=(150, 440), radius=120, start_angle=25, end_angle=75, width=12, color=FIN)


def render_dolphin_image():
    painter = AnimalPainter()
    body_points = build_body_points()
    paint_fins(painter, body_points=body_points)
    paint_body(painter, body_points=body_points)
    paint_face(painter)
    painter.save_image(name="dolphin")


if __name__ == "__main__":
    render_dolphin_image()
