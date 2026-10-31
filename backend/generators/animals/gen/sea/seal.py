"""
Seal image, drawn from scratch.
Output: seal.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, NOSE

SKIN = (150, 162, 182)
BELLY = (226, 232, 242)
SNOUT = (222, 228, 238)
WHISKER = (252, 252, 254)


def paint_body(painter):
    painter.blob(center=(430, 905), radius_x=95, radius_y=42, color=SKIN, angle=-12)
    painter.blob(center=(594, 905), radius_x=95, radius_y=42, color=SKIN, angle=12)

    body_mask = painter.build_rotated_ellipse_mask(center=(512, 700), radius_x=235, radius_y=235)
    painter.fill(mask=body_mask, shade=(SKIN, SKIN))
    painter.fill_ellipse(center=(512, 770), radius_x=170, radius_y=170, shade=(BELLY, BELLY), clip=body_mask)

    painter.blob(center=(260, 720), radius_x=48, radius_y=130, color=SKIN, angle=22)
    painter.blob(center=(764, 720), radius_x=48, radius_y=130, color=SKIN, angle=-22)


def paint_head(painter):
    painter.blob(center=(512, 400), radius_x=185, radius_y=170, color=SKIN)
    painter.blob(center=(512, 470), radius_x=110, radius_y=82, color=SNOUT)
    painter.blob(center=(512, 440), radius_x=42, radius_y=28, color=NOSE)

    for side in (-1, 1):
        painter.spot(center=(512 + side * 98, 360), radius_x=30, radius_y=30, color=EYE)
        painter.spot(center=(512 + side * 90, 350), radius_x=9, radius_y=9, color=(255, 255, 255))

        for whisker_y, whisker_end in ((470, 455), (498, 505)):
            painter.line(points=[(512 + side * 70, whisker_y), (512 + side * 190, whisker_end)], width=8, color=WHISKER)

    painter.arc_line(center=(512, 470), radius=45, start_angle=35, end_angle=145, width=10, color=NOSE)


def render_seal_image():
    painter = AnimalPainter()
    paint_body(painter)
    paint_head(painter)
    painter.save_image(name="seal")


if __name__ == "__main__":
    render_seal_image()
