"""
Blackbird image, drawn from scratch.
Output: blackbird.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import draw_perched_bird

BODY = (74, 72, 90)
BELLY = (98, 94, 114)
WING = (56, 54, 70)
BEAK = (252, 190, 40)
LEG = (140, 100, 70)


def render_blackbird_image():
    painter = AnimalPainter()
    draw_perched_bird(
        painter=painter,
        body_color=BODY,
        belly_color=BELLY,
        wing_color=WING,
        beak_color=BEAK,
        leg_color=LEG,
        tail_length=210,
        beak_length=75,
        eye_ring_color=BEAK,
    )
    painter.save_image(name="blackbird")


if __name__ == "__main__":
    render_blackbird_image()
