"""
Hooded crow image, drawn from scratch.
Output: crow.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import draw_perched_bird

BODY = (178, 180, 190)
BELLY = (200, 202, 210)
BLACK = (46, 46, 58)
BEAK = (36, 36, 46)
LEG = (70, 66, 80)


def render_crow_image():
    painter = AnimalPainter()
    draw_perched_bird(
        painter=painter,
        body_color=BODY,
        belly_color=BELLY,
        wing_color=BLACK,
        tail_color=BLACK,
        head_color=BLACK,
        beak_color=BEAK,
        leg_color=LEG,
        tail_length=190,
        beak_length=80,
        eye_ring_color=(130, 130, 150),
    )
    painter.save_image(name="crow")


if __name__ == "__main__":
    render_crow_image()
