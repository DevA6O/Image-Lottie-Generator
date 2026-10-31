"""
Jellyfish image, drawn from scratch.
Output: jellyfish.png (1024x1024, transparent background) in frontend/results/animals
"""
import math

from animals.animal_painter import AnimalPainter
from animals.face_parts import paint_eye_pair
from painting.flat_painter import solid

BELL = (244, 142, 196)
TENTACLE = (250, 176, 214)
ARM = (214, 100, 168)
BELL_BOTTOM_Y = 520
SCALLOP_COUNT = 7


def build_wave_points(
    start,
    length,
    amplitude,
    wave_count,
):
    points = []

    for step in range(41):
        progress = step / 40
        points.append((start[0] + amplitude * math.sin(progress * wave_count * 2 * math.pi), start[1] + length * progress))

    return points


def paint_tentacles(painter):
    for tentacle_x, length in ((290, 380), (370, 440), (454, 400), (570, 440), (654, 380), (734, 400)):
        painter.line(points=build_wave_points(start=(tentacle_x, 500), length=length, amplitude=22, wave_count=3), width=22, color=TENTACLE)

    for arm_x, length in ((440, 380), (584, 380)):
        painter.line(points=build_wave_points(start=(arm_x, 500), length=length, amplitude=34, wave_count=2), width=42, color=ARM)


def paint_bell(painter):
    dome_mask = painter.intersect_masks(
        first_mask=painter.build_rotated_ellipse_mask(center=(512, 500), radius_x=300, radius_y=300),
        second_mask=painter.build_box_mask(left=0, top=0, right=1024, bottom=BELL_BOTTOM_Y),
    )
    scallop_masks = [dome_mask]

    for index in range(SCALLOP_COUNT):
        scallop_x = 512 - 300 + 300 * 2 * (index + 0.5) / SCALLOP_COUNT
        scallop_masks.append(painter.build_rotated_ellipse_mask(center=(scallop_x, BELL_BOTTOM_Y - 10), radius_x=44, radius_y=34))

    painter.fill(mask=painter.union_all(masks=scallop_masks), shade=solid(BELL))
    painter.spot(center=(370, 300), radius_x=40, radius_y=80, color=(255, 214, 236), angle=40)


def render_jellyfish_image():
    painter = AnimalPainter()
    paint_tentacles(painter)
    paint_bell(painter)
    paint_eye_pair(painter=painter, center_x=512, y=420, spread=110, radius=28)
    painter.arc_line(center=(512, 450), radius=50, start_angle=35, end_angle=145, width=12, color=(46, 36, 46))
    painter.save_image(name="jellyfish")


if __name__ == "__main__":
    render_jellyfish_image()
