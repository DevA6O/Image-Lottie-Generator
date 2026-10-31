"""
Seagull image, drawn from scratch.
Output: seagull.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import draw_perched_bird

WHITE = (252, 252, 254)
BELLY = (240, 244, 250)
WING = (166, 178, 198)
WING_TIP = (50, 52, 66)
BEAK = (252, 200, 44)
LEG = (252, 170, 60)
RED_SPOT = (230, 60, 56)


def render_seagull_image():
    painter = AnimalPainter()
    draw_perched_bird(
        painter=painter,
        body_color=WHITE,
        belly_color=BELLY,
        wing_color=WING,
        tail_color=WHITE,
        beak_color=BEAK,
        leg_color=LEG,
        tail_length=150,
        hooked_beak=True,
        beak_length=95,
        eye_ring_color=(250, 190, 40),
    )
    painter.spot(center=(715, 650), radius_x=52, radius_y=22, color=WING_TIP, angle=26)
    painter.spot(center=(240, 490), radius_x=10, radius_y=10, color=RED_SPOT)
    painter.save_image(name="seagull")


if __name__ == "__main__":
    render_seagull_image()
