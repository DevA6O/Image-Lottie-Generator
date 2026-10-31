"""
Woodpecker image, drawn from scratch.
Output: woodpecker.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import HEAD_CENTER, draw_perched_bird

BLACK = (40, 42, 52)
BELLY = (244, 238, 226)
RED = (226, 50, 56)
WHITE = (250, 250, 252)
BEAK = (76, 78, 90)
LEG = (110, 110, 124)


def render_woodpecker_image():
    painter = AnimalPainter()
    draw_perched_bird(
        painter=painter,
        body_color=BLACK,
        belly_color=BELLY,
        wing_color=BLACK,
        beak_color=BEAK,
        leg_color=LEG,
        tail_length=200,
        beak_length=150,
    )
    painter.spot(center=(HEAD_CENTER[0] - 5, HEAD_CENTER[1] + 62), radius_x=62, radius_y=26, color=WHITE, angle=8)
    painter.spot(center=(HEAD_CENTER[0] + 70, HEAD_CENTER[1] - 85), radius_x=50, radius_y=30, color=RED, angle=-30)

    for spot_x, spot_y in ((540, 560), (610, 600), (670, 640)):
        painter.spot(center=(spot_x, spot_y), radius_x=22, radius_y=16, color=WHITE, angle=26)

    painter.save_image(name="woodpecker")


if __name__ == "__main__":
    render_woodpecker_image()
