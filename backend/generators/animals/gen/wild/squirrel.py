"""
Squirrel image, drawn from scratch.
Output: squirrel.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import CREAM, NOSE, paint_eye_pair, paint_pointed_ears
from painting.flat_painter import build_width_profile, sample_curve, solid

FUR = (196, 108, 56)
TAIL = (214, 128, 66)
TAIL_STRIPE = (240, 176, 110)
BELLY = (252, 230, 196)
TOOTH = (255, 252, 244)


def paint_tail(painter):
    points = sample_curve(start=(640, 860), first_control=(940, 830), second_control=(900, 230), end=(660, 250))
    widths = build_width_profile(stops=[(0.0, 120), (0.5, 220), (1.0, 150)])
    painter.fill_tapered_curve(points=points, widths=widths, shade=solid(TAIL))

    stripe_points = sample_curve(start=(700, 840), first_control=(850, 790), second_control=(830, 330), end=(690, 290))
    painter.line(points=stripe_points, width=22, color=TAIL_STRIPE)


def paint_body(painter):
    painter.blob(center=(500, 790), radius_x=210, radius_y=170, color=FUR)
    painter.blob(center=(470, 810), radius_x=120, radius_y=120, color=BELLY)


def paint_head(painter):
    paint_pointed_ears(painter=painter, center_x=450, base_y=450, spread=170, height=190, half_width=85, color=FUR, inner_color=BELLY, lean=10, tuft_color=(150, 76, 40))
    painter.blob(center=(450, 560), radius_x=250, radius_y=215, color=FUR)
    painter.blob(center=(450, 650), radius_x=140, radius_y=100, color=CREAM)


def paint_face(painter):
    paint_eye_pair(painter=painter, center_x=450, y=545, spread=135, radius=28)
    painter.blob(center=(450, 625), radius_x=38, radius_y=28, color=NOSE)
    painter.line(points=[(450, 650), (450, 700)], width=13, color=NOSE)
    painter.arc_line(center=(408, 700), radius=42, start_angle=0, end_angle=160, width=13, color=NOSE)
    painter.arc_line(center=(492, 700), radius=42, start_angle=20, end_angle=180, width=13, color=NOSE)
    painter.fill_rounded_rect(box=(420, 740, 480, 800), radius=16, shade=solid(TOOTH))


def render_squirrel_image():
    painter = AnimalPainter()
    paint_tail(painter)
    paint_body(painter)
    paint_head(painter)
    paint_face(painter)
    painter.save_image(name="squirrel")


if __name__ == "__main__":
    render_squirrel_image()
