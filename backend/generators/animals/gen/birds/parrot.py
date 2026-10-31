"""
Parrot (scarlet macaw) image, drawn from scratch.
Output: parrot.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import draw_perched_bird

RED = (228, 50, 54)
BELLY = (240, 84, 76)
BLUE = (58, 120, 222)
YELLOW = (255, 214, 60)
BEAK = (252, 246, 236)
LEG = (120, 120, 134)


def render_parrot_image():
    painter = AnimalPainter()
    draw_perched_bird(
        painter=painter,
        body_color=RED,
        belly_color=BELLY,
        wing_color=BLUE,
        tail_color=BLUE,
        beak_color=BEAK,
        leg_color=LEG,
        tail_length=300,
        hooked_beak=True,
        beak_length=60,
        eye_ring_color=(255, 255, 255),
    )
    painter.spot(center=(610, 565), radius_x=95, radius_y=22, color=YELLOW, angle=26)
    painter.save_image(name="parrot")


if __name__ == "__main__":
    render_parrot_image()
