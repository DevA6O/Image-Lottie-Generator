"""
Bear image, drawn from scratch: full body from the side.
Output: bear.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bear_shape import BearLook, build_bear_spec, paint_bear_body
from animals.quadruped_shape import paint_face

LOOK = BearLook(
    coat=(150, 98, 58),
    far_coat=(112, 70, 40),
    foot=(96, 60, 36),
    muzzle=(214, 168, 112),
    ear=(150, 98, 58),
    ear_inner=(214, 168, 112),
    nose=(52, 40, 40),
)


def render_bear_image():
    painter = AnimalPainter()
    spec = build_bear_spec(look=LOOK)
    paint_bear_body(painter=painter, spec=spec, look=LOOK)
    paint_face(painter=painter, spec=spec)
    painter.save_image(name="bear")


if __name__ == "__main__":
    render_bear_image()
