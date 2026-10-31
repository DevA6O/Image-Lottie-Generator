"""
Banana image, drawn from scratch.
Output: banana.png (1024x1024, transparent background) in frontend/results/food
"""
from food.banana_shape import draw_banana
from food.food_painter import FoodPainter


def render_banana_image():
    painter = FoodPainter()
    draw_banana(painter=painter)
    painter.save_image(name="banana")


if __name__ == "__main__":
    render_banana_image()
