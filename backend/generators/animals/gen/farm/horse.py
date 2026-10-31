"""
Horse image, drawn from scratch: full body from the side.
Output: horse.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.horse_shape import HorseLook, draw_horse

LOOK = HorseLook(
    coat=(176, 108, 62),
    far_coat=(140, 84, 48),
    hoof=(62, 48, 46),
    muzzle=(204, 150, 104),
    mane=(70, 48, 40),
    ear_inner=(70, 48, 40),
)


def render_horse_image():
    painter = AnimalPainter()
    draw_horse(painter=painter, look=LOOK)
    painter.save_image(name="horse")


if __name__ == "__main__":
    render_horse_image()
