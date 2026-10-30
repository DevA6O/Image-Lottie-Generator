"""
Chicken drumstick image, drawn from scratch.
Output: drumstick.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

MEAT = ((232, 150, 66), (168, 84, 30))
CRISP = ((188, 104, 40), (140, 70, 26))
SHINE = ((250, 196, 120), (244, 180, 100))
BONE = ((255, 250, 238), (226, 212, 186))


def paint_bone(painter):
    painter.fill_stroke(start=(430, 580), end=(270, 740), width=64, shade=BONE)
    painter.fill_circle(center=(236, 700), radius=48, shade=BONE)
    painter.fill_circle(center=(300, 790), radius=48, shade=BONE)


def paint_meat(painter):
    painter.fill_ellipse(center=(610, 410), radius_x=270, radius_y=215, shade=CRISP, angle=40)
    painter.fill_ellipse(center=(618, 402), radius_x=250, radius_y=196, shade=MEAT, angle=40)
    painter.fill_ellipse(center=(560, 330), radius_x=90, radius_y=30, shade=SHINE, angle=40)


def render_drumstick_image():
    painter = FoodPainter()
    paint_bone(painter)
    paint_meat(painter)
    painter.save_image(name="drumstick")


if __name__ == "__main__":
    render_drumstick_image()
