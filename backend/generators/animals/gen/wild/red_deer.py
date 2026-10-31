"""
Red deer image, drawn from scratch: full body from the side, with big antlers and a mane.
Output: red_deer.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.deer_shape import DeerLook, draw_deer

LOOK = DeerLook(
    coat=(160, 96, 60),
    far_coat=(124, 72, 44),
    antler=(240, 224, 180),
    antler_scale=1.35,
)


def render_red_deer_image():
    painter = AnimalPainter()
    draw_deer(painter=painter, look=LOOK)
    painter.save_image(name="red_deer")


if __name__ == "__main__":
    render_red_deer_image()
