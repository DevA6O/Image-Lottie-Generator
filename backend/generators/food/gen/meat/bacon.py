"""
Bacon strip image, drawn from scratch.
Output: bacon.png (1024x1024, transparent background) in frontend/results/food
"""
import math

from food.food_painter import FoodPainter
from painting.flat_painter import rotate_point

MEAT = ((206, 70, 52), (156, 44, 38))
FAT = ((255, 226, 204), (246, 196, 170))

STRIP_LEFT, STRIP_RIGHT = 170, 854
STRIP_CENTER_Y = 512
WAVE_HEIGHT = 55
WAVE_COUNT = 2.5
TILT_DEGREES = -22
STRIP_WIDTH = 190
FAT_OFFSET = 42
FAT_WIDTH = 36


def build_wave_points(vertical_offset):
    points = []

    for step in range(81):
        progress = step / 80
        x = STRIP_LEFT + (STRIP_RIGHT - STRIP_LEFT) * progress
        y = STRIP_CENTER_Y + vertical_offset + WAVE_HEIGHT * math.sin(progress * WAVE_COUNT * 2 * math.pi)
        points.append(rotate_point(point=(x, y), center=(512, 512), angle_degrees=TILT_DEGREES))

    return points


def paint_strip(painter):
    painter.fill_curve(points=build_wave_points(vertical_offset=0), width=STRIP_WIDTH, shade=MEAT)

    for offset in (-FAT_OFFSET, FAT_OFFSET):
        painter.fill_curve(points=build_wave_points(vertical_offset=offset), width=FAT_WIDTH, shade=FAT)


def render_bacon_image():
    painter = FoodPainter()
    paint_strip(painter)
    painter.save_image(name="bacon")


if __name__ == "__main__":
    render_bacon_image()
