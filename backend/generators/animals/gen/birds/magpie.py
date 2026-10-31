"""
Magpie image, drawn from scratch.
Output: magpie.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import draw_perched_bird

BLACK = (38, 40, 54)
WHITE = (250, 250, 252)
WING = (46, 92, 140)
TAIL = (40, 118, 120)
BEAK = (30, 30, 40)
LEG = (70, 66, 80)


def render_magpie_image():
    painter = AnimalPainter()
    draw_perched_bird(
        painter=painter,
        body_color=BLACK,
        belly_color=WHITE,
        wing_color=WING,
        tail_color=TAIL,
        beak_color=BEAK,
        leg_color=LEG,
        tail_length=300,
        beak_length=70,
        eye_ring_color=(120, 120, 150),
    )
    painter.spot(center=(470, 520), radius_x=64, radius_y=24, color=WHITE, angle=24)
    painter.save_image(name="magpie")


if __name__ == "__main__":
    render_magpie_image()
