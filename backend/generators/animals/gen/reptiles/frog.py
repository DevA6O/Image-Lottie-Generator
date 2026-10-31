"""
Frog image, drawn from scratch.
Output: frog.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.frog_shape import draw_frog

SKIN = (104, 196, 84)
BELLY = (232, 244, 168)
CHEEK = (250, 150, 150)


def render_frog_image():
    painter = AnimalPainter()
    draw_frog(painter=painter, skin_color=SKIN, belly_color=BELLY)
    painter.spot(center=(300, 600), radius_x=44, radius_y=30, color=CHEEK)
    painter.spot(center=(724, 600), radius_x=44, radius_y=30, color=CHEEK)
    painter.save_image(name="frog")


if __name__ == "__main__":
    render_frog_image()
