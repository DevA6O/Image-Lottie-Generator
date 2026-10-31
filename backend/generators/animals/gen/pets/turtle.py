"""
Turtle image, drawn from scratch.
Output: turtle.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import solid

SKIN = (150, 200, 90)
SHELL = (86, 150, 78)
PLATE = (64, 118, 66)
RIM = (240, 214, 130)


def paint_limbs(painter):
    painter.blob(center=(780, 650), radius_x=70, radius_y=36, color=SKIN, angle=-20)
    painter.fill_rounded_rect(box=(330, 640, 440, 790), radius=40, shade=solid(SKIN))
    painter.fill_rounded_rect(box=(600, 640, 710, 790), radius=40, shade=solid(SKIN))
    painter.body_curve(points=[(290, 560), (240, 470), (205, 400)], width=110, color=SKIN)
    painter.blob(center=(185, 380), radius_x=95, radius_y=88, color=SKIN)


def paint_shell(painter):
    dome_mask = painter.intersect_masks(
        first_mask=painter.build_rotated_ellipse_mask(center=(520, 600), radius_x=330, radius_y=300),
        second_mask=painter.build_box_mask(left=0, top=0, right=1024, bottom=650),
    )
    painter.fill(mask=dome_mask, shade=solid(SHELL))

    for plate_center in ((520, 470), (365, 540), (675, 540)):
        painter.fill_ellipse(center=plate_center, radius_x=80, radius_y=62, shade=solid(PLATE), clip=dome_mask)

    painter.fill_rounded_rect(box=(180, 620, 860, 700), radius=40, shade=solid(RIM))


def paint_face(painter):
    painter.spot(center=(165, 360), radius_x=17, radius_y=17, color=EYE)
    painter.arc_line(center=(150, 395), radius=40, start_angle=20, end_angle=100, width=11, color=PLATE)


def render_turtle_image():
    painter = AnimalPainter()
    paint_limbs(painter)
    paint_shell(painter)
    paint_face(painter)
    painter.save_image(name="turtle")


if __name__ == "__main__":
    render_turtle_image()
