"""
Chicken image, drawn from scratch.
Output: chicken.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import HEAD_CENTER, draw_perched_bird

WHITE = (252, 250, 244)
BELLY = (240, 232, 218)
WING = (236, 224, 206)
TAIL = (226, 214, 196)
RED = (224, 58, 62)
BEAK = (250, 190, 50)
LEG = (244, 190, 60)


def paint_comb_and_wattle(painter):
    for comb_x, comb_y, comb_radius in ((330, 305, 38), (378, 275, 44), (428, 300, 36)):
        painter.blob(center=(comb_x, comb_y), radius_x=comb_radius, radius_y=comb_radius, color=RED)

    painter.blob(center=(HEAD_CENTER[0] - 85, HEAD_CENTER[1] + 100), radius_x=26, radius_y=42, color=RED)


def paint_chicken(painter):
    draw_perched_bird(
        painter=painter,
        body_color=WHITE,
        belly_color=BELLY,
        wing_color=WING,
        tail_color=TAIL,
        beak_color=BEAK,
        leg_color=LEG,
        tail_length=150,
        beak_length=50,
    )
    paint_comb_and_wattle(painter)


def render_chicken_image():
    painter = AnimalPainter()
    paint_chicken(painter)
    painter.save_image(name="chicken")


if __name__ == "__main__":
    render_chicken_image()
