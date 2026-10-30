"""
Hot dog image, drawn from scratch.
Output: hot_dog.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

BUN_BACK = ((214, 146, 70), (180, 112, 46))
BUN_FRONT = ((240, 180, 96), (204, 134, 60))
SAUSAGE = ((222, 92, 64), (164, 52, 38))
MUSTARD = ((255, 218, 60), (240, 176, 20))

SAUSAGE_Y = 500
ZIGZAG_POINTS = [(190 + step * 60, 500 + (-34 if step % 2 == 0 else 34)) for step in range(12)]


def paint_back_bun(painter):
    painter.fill_rounded_rect(box=(150, 440, 874, 720), radius=140, shade=BUN_BACK)


def paint_sausage(painter):
    painter.fill_stroke(start=(170, SAUSAGE_Y), end=(854, SAUSAGE_Y), width=170, shade=SAUSAGE)
    painter.fill_curve(points=ZIGZAG_POINTS, width=30, shade=MUSTARD)


def paint_front_bun(painter):
    painter.fill_rounded_rect(box=(150, 560, 874, 790), radius=115, shade=BUN_FRONT)


def render_hot_dog_image():
    painter = FoodPainter()
    paint_back_bun(painter)
    paint_sausage(painter)
    paint_front_bun(painter)
    painter.save_image(name="hot_dog")


if __name__ == "__main__":
    render_hot_dog_image()
