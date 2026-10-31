"""
Rabbit image, drawn from scratch: sitting, seen from the side.
Output: rabbit.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.rabbit_shape import draw_sitting_rabbit

COAT = (246, 240, 232)
COAT_FAR = (214, 206, 198)
BELLY = (255, 252, 248)
EAR_INNER = (246, 176, 190)


def render_rabbit_image():
    painter = AnimalPainter()
    draw_sitting_rabbit(painter=painter, coat=COAT, far_coat=COAT_FAR, belly_color=BELLY, ear_inner=EAR_INNER)
    painter.save_image(name="rabbit")


if __name__ == "__main__":
    render_rabbit_image()
