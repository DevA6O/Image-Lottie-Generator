"""
Pear image, drawn from scratch.
Output: pear.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

PEAR = ((206, 224, 90), (136, 172, 44))
SHINE = ((234, 244, 160), (226, 240, 140))
STEM = ((140, 84, 44), (100, 56, 28))
LEAF = ((130, 205, 84), (70, 150, 52))


def paint_pear(painter):
    pear_mask = painter.build_pear_mask(
        center_x=512,
        top_center_y=400,
        top_radius=150,
        bottom_center_y=640,
        bottom_radius=250,
    )
    painter.fill(mask=pear_mask, shade=PEAR)
    painter.fill_ellipse(center=(400, 680), radius_x=34, radius_y=100, shade=SHINE, angle=15, clip=pear_mask)


def paint_stem_and_leaf(painter):
    painter.fill_curve(points=[(512, 270), (520, 220), (550, 170)], width=30, shade=STEM)
    painter.fill_ellipse(center=(650, 230), radius_x=100, radius_y=40, shade=LEAF, angle=-25)


def render_pear_image():
    painter = FoodPainter()
    paint_pear(painter)
    paint_stem_and_leaf(painter)
    painter.save_image(name="pear")


if __name__ == "__main__":
    render_pear_image()
