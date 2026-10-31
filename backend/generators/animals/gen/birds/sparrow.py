"""
Sparrow image, drawn from scratch.
Output: sparrow.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import HEAD_CENTER, draw_perched_bird

BODY = (168, 122, 82)
BELLY = (226, 216, 202)
WING = (122, 80, 52)
HEAD = (150, 122, 104)
BEAK = (112, 106, 112)
BIB = (60, 48, 48)
CHEEK = (246, 240, 230)


def render_sparrow_image():
    painter = AnimalPainter()
    draw_perched_bird(
        painter=painter,
        body_color=BODY,
        belly_color=BELLY,
        wing_color=WING,
        head_color=HEAD,
        beak_color=BEAK,
        tail_length=190,
        beak_length=55,
    )
    painter.spot(center=(HEAD_CENTER[0] + 20, HEAD_CENTER[1] + 60), radius_x=62, radius_y=26, color=CHEEK, angle=10)
    painter.spot(center=(HEAD_CENTER[0] - 35, HEAD_CENTER[1] + 100), radius_x=36, radius_y=26, color=BIB)
    painter.save_image(name="sparrow")


if __name__ == "__main__":
    render_sparrow_image()
