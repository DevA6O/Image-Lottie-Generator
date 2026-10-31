"""
Monkey image, drawn from scratch: sitting, seen from the side, with the curly tail.
Output: monkey.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, NOSE
from animals.quadruped_shape import EYE_HIGHLIGHT
from painting.flat_painter import build_width_profile, sample_curve, solid

FUR = (150, 98, 58)
FUR_FAR = (116, 72, 42)
SKIN = (246, 208, 160)
EAR_INNER = (232, 170, 130)


def paint_tail(painter):
    points = sample_curve(start=(760, 800), first_control=(930, 830), second_control=(990, 640), end=(890, 560))
    widths = build_width_profile(stops=[(0.0, 54), (1.0, 34)], point_count=len(points))
    painter.fill_tapered_curve(points=points, widths=widths, shade=solid(FUR_FAR))


def paint_body(painter):
    painter.blob(center=(610, 620), radius_x=195, radius_y=260, color=FUR, angle=-8)
    painter.blob(center=(530, 650), radius_x=115, radius_y=175, color=SKIN)
    painter.blob(center=(640, 790), radius_x=165, radius_y=105, color=FUR)
    painter.blob(center=(470, 885), radius_x=120, radius_y=36, color=SKIN)


def paint_arm(painter):
    points = [(480, 500), (420, 610), (380, 700)]
    widths = build_width_profile(stops=[(0.0, 84), (1.0, 62)], point_count=3)
    painter.fill_tapered_curve(points=points, widths=widths, shade=solid(FUR_FAR))
    painter.blob(center=(372, 725), radius_x=46, radius_y=46, color=SKIN)


def paint_head(painter):
    painter.blob(center=(500, 370), radius_x=48, radius_y=48, color=FUR)
    painter.spot(center=(500, 372), radius_x=26, radius_y=26, color=EAR_INNER)
    painter.blob(center=(410, 380), radius_x=125, radius_y=115, color=FUR)
    painter.blob(center=(350, 410), radius_x=92, radius_y=78, color=SKIN)
    painter.spot(center=(335, 380), radius_x=15, radius_y=15, color=EYE)
    painter.spot(center=(330, 374), radius_x=5, radius_y=5, color=EYE_HIGHLIGHT)
    painter.spot(center=(268, 405), radius_x=10, radius_y=8, color=NOSE)
    painter.arc_line(center=(320, 440), radius=34, start_angle=20, end_angle=110, width=8, color=NOSE)


def render_monkey_image():
    painter = AnimalPainter()
    paint_tail(painter=painter)
    paint_body(painter=painter)
    paint_arm(painter=painter)
    paint_head(painter=painter)
    painter.save_image(name="monkey")


if __name__ == "__main__":
    render_monkey_image()
