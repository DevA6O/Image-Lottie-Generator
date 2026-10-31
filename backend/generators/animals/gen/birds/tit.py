"""
Blue tit image, drawn from scratch.
Output: tit.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import HEAD_CENTER, HEAD_RADIUS, draw_perched_bird
from painting.flat_painter import solid

BODY = (252, 218, 74)
BELLY = (255, 236, 120)
WING = (82, 140, 212)
HEAD = (252, 252, 250)
CAP = (82, 140, 212)
BEAK = (70, 70, 80)
LEG = (110, 120, 140)


def paint_blue_cap(painter):
    head_mask = painter.build_rotated_ellipse_mask(center=HEAD_CENTER, radius_x=HEAD_RADIUS, radius_y=HEAD_RADIUS)
    painter.fill_ellipse(center=(HEAD_CENTER[0] + 20, HEAD_CENTER[1] - 90), radius_x=150, radius_y=70, shade=solid(CAP), clip=head_mask, angle=-12)


def render_tit_image():
    painter = AnimalPainter()
    draw_perched_bird(
        painter=painter,
        body_color=BODY,
        belly_color=BELLY,
        wing_color=WING,
        head_color=HEAD,
        beak_color=BEAK,
        leg_color=LEG,
        tail_length=170,
        beak_length=45,
    )
    paint_blue_cap(painter)
    painter.save_image(name="tit")


if __name__ == "__main__":
    render_tit_image()
