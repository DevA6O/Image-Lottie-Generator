"""
Roe deer image, drawn from scratch: full body from the side.
Output: deer.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.deer_shape import DeerLook, draw_deer

LOOK = DeerLook(coat=(204, 144, 86), far_coat=(170, 112, 64), antler=(240, 224, 180))


def render_deer_image():
    painter = AnimalPainter()
    draw_deer(painter=painter, look=LOOK)
    painter.save_image(name="deer")


if __name__ == "__main__":
    render_deer_image()
