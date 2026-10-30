"""
French fries in a carton, drawn from scratch.
Output: fries.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

FRY = ((255, 224, 110), (238, 172, 50))
CARTON = ((236, 66, 58), (176, 32, 40))
LOGO = ((255, 220, 70), (244, 176, 30))

# (bottom_x, top_x, top_y): every fry leans a little differently
FRIES = [
    (330, 280, 220), (400, 370, 160), (470, 450, 240), (540, 560, 150),
    (610, 650, 230), (680, 740, 200), (370, 330, 330), (500, 500, 320), (640, 690, 330),
]
FRY_WIDTH = 76
CARTON_TOP = 540


def paint_fries(painter):
    for bottom_x, top_x, top_y in FRIES:
        painter.fill_stroke(start=(bottom_x, CARTON_TOP + 40), end=(top_x, top_y), width=FRY_WIDTH, shade=FRY)


def paint_carton(painter):
    painter.fill_polygon(points=[(270, CARTON_TOP), (754, CARTON_TOP), (696, 880), (328, 880)], shade=CARTON)
    painter.fill_circle(center=(512, 700), radius=70, shade=LOGO)


def render_fries_image():
    painter = FoodPainter()
    paint_fries(painter)
    paint_carton(painter)
    painter.save_image(name="fries")


if __name__ == "__main__":
    render_fries_image()
