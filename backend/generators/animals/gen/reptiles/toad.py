"""
Toad image, drawn from scratch.
Output: toad.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.frog_shape import draw_frog
from painting.flat_painter import solid

SKIN = (160, 126, 84)
BELLY = (236, 216, 172)
IRIS = (240, 182, 56)
WART = (112, 84, 56)
WART_POSITIONS = ((330, 620, 22), (420, 680, 18), (600, 690, 20), (700, 630, 24), (512, 740, 16), (250, 700, 18), (780, 710, 18), (470, 600, 14))


def render_toad_image():
    painter = AnimalPainter()
    body_mask = draw_frog(painter=painter, skin_color=SKIN, belly_color=BELLY, iris_color=IRIS, bar_pupil=True)

    for wart_x, wart_y, wart_radius in WART_POSITIONS:
        painter.fill_ellipse(center=(wart_x, wart_y), radius_x=wart_radius, radius_y=wart_radius, shade=solid(WART), clip=body_mask)

    painter.save_image(name="toad")


if __name__ == "__main__":
    render_toad_image()
