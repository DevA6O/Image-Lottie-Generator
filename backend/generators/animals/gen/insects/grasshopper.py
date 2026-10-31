"""
Grasshopper image, drawn from scratch.
Output: grasshopper.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_width_profile, sample_curve

GREEN = (134, 204, 72)
GREEN_DARK = (84, 150, 62)
WING = (180, 226, 120)
EYE_WHITE = (255, 255, 255)


def paint_legs(painter):
    painter.fill_tapered_curve(points=[(660, 560), (560, 640), (480, 720)], widths=[110, 90, 40], shade=(GREEN_DARK, GREEN_DARK))
    painter.line(points=[(480, 720), (600, 800), (640, 900)], width=22, color=GREEN_DARK)
    painter.line(points=[(560, 910), (640, 900), (700, 915)], width=18, color=GREEN_DARK)

    for foot_x in (300, 380):
        painter.line(points=[(foot_x + 20, 580), (foot_x, 720), (foot_x - 30, 850)], width=18, color=GREEN_DARK)


def paint_body(painter):
    body_points = sample_curve(start=(260, 520), first_control=(420, 480), second_control=(620, 510), end=(850, 600))
    body_widths = build_width_profile(stops=[(0.0, 110), (0.4, 120), (1.0, 40)])
    painter.fill_tapered_curve(points=body_points, widths=body_widths, shade=(GREEN, GREEN))
    painter.blob(center=(600, 470), radius_x=270, radius_y=55, color=WING, angle=10)


def paint_head(painter):
    painter.blob(center=(230, 500), radius_x=105, radius_y=95, color=GREEN)
    painter.spot(center=(205, 470), radius_x=32, radius_y=32, color=EYE_WHITE)
    painter.spot(center=(200, 472), radius_x=17, radius_y=17, color=EYE)
    painter.line(points=[(215, 420), (190, 290), (110, 190)], width=10, color=GREEN_DARK)
    painter.line(points=[(250, 425), (260, 290), (200, 170)], width=10, color=GREEN_DARK)
    painter.arc_line(center=(170, 540), radius=45, start_angle=20, end_angle=95, width=10, color=GREEN_DARK)


def render_grasshopper_image():
    painter = AnimalPainter()
    paint_legs(painter)
    paint_body(painter)
    paint_head(painter)
    painter.save_image(name="grasshopper")


if __name__ == "__main__":
    render_grasshopper_image()
