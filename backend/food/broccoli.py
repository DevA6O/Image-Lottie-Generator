"""
Broccoli image, drawn from scratch.
Output: broccoli.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

FLORET = ((110, 190, 80), (54, 134, 52))
FLORET_RIM = ((36, 100, 44), (36, 100, 44))
STEM = ((190, 224, 130), (140, 186, 90))

RIM_GROWTH = 12
# (x, y, radius): drawn back to front
FLORETS = [(330, 440, 130), (694, 440, 130), (512, 340, 150), (400, 520, 130), (624, 520, 130), (512, 500, 130)]


def paint_stem(painter):
    painter.fill_polygon(points=[(420, 560), (604, 560), (650, 880), (374, 880)], shade=STEM)
    painter.fill_stroke(start=(420, 640), end=(330, 520), width=60, shade=STEM)
    painter.fill_stroke(start=(604, 640), end=(694, 520), width=60, shade=STEM)


def paint_florets(painter):
    for x, y, radius in FLORETS:
        painter.fill_circle(center=(x, y), radius=radius + RIM_GROWTH, shade=FLORET_RIM)
        painter.fill_circle(center=(x, y), radius=radius, shade=FLORET)


def render_broccoli_image():
    painter = FoodPainter()
    paint_stem(painter)
    paint_florets(painter)
    painter.save_image(name="broccoli")


if __name__ == "__main__":
    render_broccoli_image()
