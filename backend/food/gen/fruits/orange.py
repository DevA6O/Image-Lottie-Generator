"""
Orange image, drawn from scratch.
Output: orange.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

ORANGE = ((255, 176, 56), (232, 112, 20))
SHINE = ((255, 214, 130), (255, 200, 110))
DIMPLE = ((222, 120, 26), (222, 120, 26))
LEAF = ((130, 205, 84), (70, 150, 52))
STEM_BASE = ((90, 130, 50), (70, 104, 40))

DIMPLES = [(380, 640), (520, 700), (640, 600), (700, 700), (450, 520), (600, 780), (330, 560)]


def paint_orange(painter):
    orange_mask = painter.build_rotated_ellipse_mask(center=(512, 560), radius_x=320, radius_y=310)
    painter.fill(mask=orange_mask, shade=ORANGE)
    painter.fill_ellipse(center=(380, 440), radius_x=70, radius_y=34, shade=SHINE, angle=-40, clip=orange_mask)

    for center in DIMPLES:
        painter.fill_circle(center=center, radius=8, shade=DIMPLE, clip=orange_mask)


def paint_leaf(painter):
    painter.fill_ellipse(center=(620, 240), radius_x=120, radius_y=48, shade=LEAF, angle=-20)
    painter.fill_circle(center=(512, 262), radius=34, shade=STEM_BASE)


def render_orange_image():
    painter = FoodPainter()
    paint_orange(painter)
    paint_leaf(painter)
    painter.save_image(name="orange")


if __name__ == "__main__":
    render_orange_image()
