"""
Two olives (one black, one green with a pimento), drawn from scratch.
Output: olives.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

BLACK_OLIVE = ((88, 78, 92), (28, 22, 34))
GREEN_OLIVE = ((176, 196, 72), (96, 120, 38))
GREEN_HOLE = ((84, 104, 32), (70, 90, 28))
PIMENTO = ((236, 70, 56), (190, 40, 44))
SHINE = ((210, 224, 150), (190, 208, 120))
BLACK_SHINE = ((150, 140, 156), (120, 110, 126))


def paint_black_olive(painter):
    painter.fill_ellipse(center=(610, 400), radius_x=210, radius_y=165, shade=BLACK_OLIVE, angle=28)
    painter.fill_ellipse(center=(540, 340), radius_x=60, radius_y=26, shade=BLACK_SHINE, angle=28)


def paint_green_olive(painter):
    painter.fill_ellipse(center=(430, 620), radius_x=250, radius_y=190, shade=GREEN_OLIVE, angle=-28)
    painter.fill_ellipse(center=(330, 560), radius_x=70, radius_y=28, shade=SHINE, angle=-28)
    painter.fill_ellipse(center=(600, 540), radius_x=66, radius_y=50, shade=GREEN_HOLE, angle=-28)
    painter.fill_ellipse(center=(600, 540), radius_x=44, radius_y=32, shade=PIMENTO, angle=-28)


def render_olives_image():
    painter = FoodPainter()
    paint_black_olive(painter)
    paint_green_olive(painter)
    painter.save_image(name="olives")


if __name__ == "__main__":
    render_olives_image()
