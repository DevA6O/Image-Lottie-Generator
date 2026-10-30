"""
Pizza slice image, drawn from scratch.
Output: pizza.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

CRUST = ((240, 188, 104), (204, 136, 58))
CHEESE = ((255, 224, 96), (246, 176, 40))
PEPPERONI = ((228, 76, 62), (172, 36, 40))
OLIVE = ((72, 72, 72), (30, 30, 30))

PEPPERONI_SPOTS = [((400, 450), 62), ((630, 480), 54), ((500, 650), 50)]
OLIVE_SPOTS = [(560, 360), (330, 400), (650, 620), (460, 780)]


def paint_crust(painter):
    painter.fill_stroke(start=(215, 280), end=(809, 280), width=100, shade=CRUST)


def paint_cheese(painter):
    outline = painter.build_polygon_mask(points=[(215, 320), (809, 320), (512, 870)])
    cheese_mask = painter.round_corners(mask=outline, radius=30)
    painter.fill(mask=cheese_mask, shade=CHEESE)

    return cheese_mask


def paint_toppings(
    painter,
    cheese_mask,
):
    for center, radius in PEPPERONI_SPOTS:
        painter.fill_circle(center=center, radius=radius, shade=PEPPERONI, clip=cheese_mask)

    for center in OLIVE_SPOTS:
        painter.fill_circle(center=center, radius=26, shade=OLIVE, clip=cheese_mask)


def render_pizza_image():
    painter = FoodPainter()
    paint_crust(painter)
    cheese_mask = paint_cheese(painter)
    paint_toppings(painter=painter, cheese_mask=cheese_mask)
    painter.save_image(name="pizza")


if __name__ == "__main__":
    render_pizza_image()
