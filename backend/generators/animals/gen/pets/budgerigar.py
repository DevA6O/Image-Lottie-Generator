"""
Budgerigar image, drawn from scratch.
Output: budgerigar.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import HEAD_CENTER, draw_perched_bird

GREEN = (110, 200, 84)
BELLY = (150, 220, 110)
WING = (60, 150, 80)
TAIL = (60, 130, 200)
YELLOW = (255, 220, 80)
CHEEK = (96, 150, 230)


def paint_budgerigar(painter):
    draw_perched_bird(
        painter=painter,
        body_color=GREEN,
        belly_color=BELLY,
        wing_color=WING,
        tail_color=TAIL,
        head_color=YELLOW,
        tail_length=230,
        beak_color=(250, 190, 150),
        beak_length=40,
    )
    painter.spot(center=(HEAD_CENTER[0] + 5, HEAD_CENTER[1] + 55), radius_x=34, radius_y=26, color=CHEEK)


def render_budgerigar_image():
    painter = AnimalPainter()
    paint_budgerigar(painter)
    painter.save_image(name="budgerigar")


if __name__ == "__main__":
    render_budgerigar_image()
