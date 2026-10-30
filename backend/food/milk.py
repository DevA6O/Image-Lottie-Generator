"""
Milk carton image, drawn from scratch.
Output: milk.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

CARTON = ((255, 255, 255), (214, 224, 240))
ROOF = ((236, 242, 252), (200, 214, 236))
BLUE = ((84, 160, 236), (40, 100, 190))
DROP = ((255, 255, 255), (232, 240, 252))

CARTON_LEFT, CARTON_RIGHT = 320, 704


def paint_carton(painter):
    painter.fill_polygon(points=[(CARTON_LEFT, 420), (430, 270), (594, 270), (CARTON_RIGHT, 420)], shade=ROOF)
    painter.fill_rounded_rect(box=(CARTON_LEFT, 410, CARTON_RIGHT, 870), radius=14, shade=CARTON)
    painter.fill_rounded_rect(box=(430, 190, 594, 290), radius=14, shade=ROOF)


def paint_label(painter):
    painter.fill_rounded_rect(box=(CARTON_LEFT, 540, CARTON_RIGHT, 780), radius=0, shade=BLUE)
    drop_mask = painter.build_polygon_mask(points=[(512, 570), (580, 690), (444, 690)])
    painter.fill(mask=drop_mask, shade=DROP)
    painter.fill_circle(center=(512, 692), radius=68, shade=DROP)


def render_milk_image():
    painter = FoodPainter()
    paint_carton(painter)
    paint_label(painter)
    painter.save_image(name="milk")


if __name__ == "__main__":
    render_milk_image()
