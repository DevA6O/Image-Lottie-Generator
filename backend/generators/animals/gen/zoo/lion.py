"""
Lion image, drawn from scratch: full body from the side, with the mane.
Output: lion.png (1024x1024, transparent background) in frontend/results/animals
"""
import math

from animals.animal_painter import AnimalPainter
from animals.big_cat_shape import BigCatLook, build_big_cat_spec, paint_big_cat_body, paint_big_cat_face

LOOK = BigCatLook(
    coat=(226, 172, 96),
    far_coat=(188, 136, 66),
    belly=(246, 218, 168),
    tail_tip=(150, 92, 44),
    ear_inner=(150, 92, 44),
)
MANE = (156, 96, 46)
MANE_CENTER = (310, 470)
MANE_RADIUS = 150
MANE_CURL_COUNT = 11


def paint_mane(painter):
    for curl_index in range(MANE_CURL_COUNT):
        angle = math.radians(curl_index * 360 / MANE_CURL_COUNT)
        center = (MANE_CENTER[0] + MANE_RADIUS * math.cos(angle), MANE_CENTER[1] + MANE_RADIUS * math.sin(angle))
        painter.blob(center=center, radius_x=68, radius_y=68, color=MANE)

    painter.blob(center=MANE_CENTER, radius_x=MANE_RADIUS, radius_y=MANE_RADIUS, color=MANE)


def render_lion_image():
    painter = AnimalPainter()
    spec = build_big_cat_spec(look=LOOK)
    paint_big_cat_body(painter=painter, spec=spec, look=LOOK, before_head=lambda: paint_mane(painter=painter))
    paint_big_cat_face(painter=painter, spec=spec)
    painter.save_image(name="lion")


if __name__ == "__main__":
    render_lion_image()
