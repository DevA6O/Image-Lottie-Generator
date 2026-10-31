"""
Elephant image, drawn from scratch: full body from the side, with trunk, tusk and big ear.
Output: elephant.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from animals.quadruped_shape import EYE_HIGHLIGHT
from painting.flat_painter import build_width_profile, sample_curve, solid

SKIN = (152, 164, 190)
SKIN_FAR = (120, 132, 160)
EAR_INNER = (216, 172, 190)
TUSK = (252, 242, 214)
NAIL = (238, 232, 228)
GROUND_Y = 905
LEG_X_VALUES = ((330, SKIN_FAR), (780, SKIN_FAR), (440, SKIN), (690, SKIN))


def paint_legs(painter):
    for leg_x, color in LEG_X_VALUES:
        widths = build_width_profile(stops=[(0.0, 150), (1.0, 130)], point_count=3)
        painter.fill_tapered_curve(points=[(leg_x, 650), (leg_x, 780), (leg_x, GROUND_Y - 30)], widths=widths, shade=solid(color))
        painter.blob(center=(leg_x - 6, GROUND_Y - 28), radius_x=74, radius_y=30, color=color)

        for nail_offset in (-40, 0, 40):
            painter.spot(center=(leg_x - 6 + nail_offset, GROUND_Y - 22), radius_x=11, radius_y=9, color=NAIL)


def paint_body_and_tail(painter):
    painter.line(points=[(930, 520), (970, 650), (955, 760)], width=22, color=SKIN_FAR)
    painter.blob(center=(955, 775), radius_x=20, radius_y=34, color=SKIN_FAR)
    painter.blob(center=(620, 560), radius_x=335, radius_y=250, color=SKIN)


def paint_head(painter):
    trunk_points = sample_curve(start=(210, 540), first_control=(100, 600), second_control=(70, 800), end=(180, 880))
    trunk_widths = build_width_profile(stops=[(0.0, 170), (0.5, 100), (1.0, 62)], point_count=len(trunk_points))
    painter.fill_tapered_curve(points=trunk_points, widths=trunk_widths, shade=solid(SKIN))
    painter.blob(center=(290, 500), radius_x=185, radius_y=175, color=SKIN)
    painter.body_curve(points=[(215, 620), (150, 690), (120, 700)], width=30, color=TUSK)
    painter.blob(center=(380, 470), radius_x=115, radius_y=165, color=SKIN_FAR, angle=8)
    painter.spot(center=(385, 470), radius_x=68, radius_y=115, color=EAR_INNER, angle=8)
    painter.spot(center=(250, 440), radius_x=17, radius_y=17, color=EYE)
    painter.spot(center=(244, 434), radius_x=6, radius_y=6, color=EYE_HIGHLIGHT)


def render_elephant_image():
    painter = AnimalPainter()
    paint_legs(painter=painter)
    paint_body_and_tail(painter=painter)
    paint_head(painter=painter)
    painter.save_image(name="elephant")


if __name__ == "__main__":
    render_elephant_image()
