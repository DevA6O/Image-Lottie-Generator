"""
Cupcake with swirled frosting and a cherry, drawn from scratch.
Output: cupcake.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

WRAPPER = ((120, 200, 230), (60, 140, 190))
WRAPPER_RIDGE = ((90, 170, 205), (50, 120, 170))
FROSTING = ((255, 214, 230), (244, 150, 196))
CHERRY = ((238, 60, 70), (170, 28, 46))
CHERRY_SHINE = ((255, 170, 170), (255, 150, 150))

# (center_y, half width, half height) from the bottom tier to the top tier
FROSTING_TIERS = [(520, 270, 110), (410, 210, 90), (310, 140, 76)]
RIDGE_POSITIONS = [350, 430, 512, 594, 674]


def paint_wrapper(painter):
    wrapper_mask = painter.build_polygon_mask(points=[(270, 540), (754, 540), (690, 870), (334, 870)])
    painter.fill(mask=wrapper_mask, shade=WRAPPER)

    for x in RIDGE_POSITIONS:
        painter.fill_stroke(
            start=(x, 540),
            end=(512 + (x - 512) * 0.8, 870),
            width=16,
            shade=WRAPPER_RIDGE,
            clip=wrapper_mask,
        )


def paint_frosting(painter):
    for center_y, radius_x, radius_y in FROSTING_TIERS:
        painter.fill_ellipse(center=(512, center_y), radius_x=radius_x, radius_y=radius_y, shade=FROSTING)

    painter.fill_polygon(points=[(470, 250), (512, 190), (556, 250)], shade=FROSTING)


def paint_cherry(painter):
    painter.fill_circle(center=(512, 200), radius=56, shade=CHERRY)
    painter.fill_ellipse(center=(490, 180), radius_x=16, radius_y=10, shade=CHERRY_SHINE, angle=-30)


def render_cupcake_image():
    painter = FoodPainter()
    paint_wrapper(painter)
    paint_frosting(painter)
    paint_cherry(painter)
    painter.save_image(name="cupcake")


if __name__ == "__main__":
    render_cupcake_image()
