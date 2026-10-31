"""
Hare image, drawn from scratch: sitting, seen from the side, with long black-tipped ears.
Output: hare.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.rabbit_shape import draw_sitting_rabbit

COAT = (190, 140, 88)
COAT_FAR = (156, 108, 66)
BELLY = (246, 226, 196)
EAR_INNER = (232, 184, 150)
EAR_TIP = (58, 46, 48)


def render_hare_image():
    painter = AnimalPainter()
    draw_sitting_rabbit(painter=painter, coat=COAT, far_coat=COAT_FAR, belly_color=BELLY, ear_inner=EAR_INNER, ear_tip=EAR_TIP, ear_length=360)
    painter.save_image(name="hare")


if __name__ == "__main__":
    render_hare_image()
