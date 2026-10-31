"""
Donkey image, drawn from scratch: full body from the side, with long ears.
Output: donkey.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.horse_shape import HorseLook, draw_horse

LOOK = HorseLook(
    coat=(154, 148, 150),
    far_coat=(120, 114, 118),
    hoof=(62, 56, 58),
    muzzle=(236, 228, 220),
    mane=(88, 82, 86),
    ear_inner=(236, 200, 200),
    ear_length=190,
    stocky=True,
)


def render_donkey_image():
    painter = AnimalPainter()
    draw_horse(painter=painter, look=LOOK)
    painter.save_image(name="donkey")


if __name__ == "__main__":
    render_donkey_image()
