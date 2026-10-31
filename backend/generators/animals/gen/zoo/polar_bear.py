"""
Polar bear image, drawn from scratch: full body from the side.
Output: polar_bear.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bear_shape import BearLook, build_bear_spec, paint_bear_body
from animals.quadruped_shape import paint_face

LOOK = BearLook(
    coat=(248, 250, 254),
    far_coat=(204, 212, 228),
    foot=(226, 232, 244),
    muzzle=(222, 230, 244),
    ear=(248, 250, 254),
    ear_inner=(190, 206, 232),
    nose=(52, 48, 58),
)


def render_polar_bear_image():
    painter = AnimalPainter()
    spec = build_bear_spec(look=LOOK)
    paint_bear_body(painter=painter, spec=spec, look=LOOK)
    paint_face(painter=painter, spec=spec)
    painter.save_image(name="polar_bear")


if __name__ == "__main__":
    render_polar_bear_image()
