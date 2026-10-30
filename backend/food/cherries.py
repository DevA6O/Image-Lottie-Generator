"""
Two cherries on one stem, drawn from scratch.
Output: cherries.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter, sample_curve

CHERRY = ((240, 62, 76), (160, 20, 44))
SHINE = ((255, 170, 170), (255, 150, 150))
STEM = ((120, 150, 60), (84, 108, 40))
LEAF = ((130, 205, 84), (70, 150, 52))

STEM_JOIN = (560, 230)
CHERRIES = [((340, 700), 160), ((690, 740), 160)]
STEM_WIDTH = 22


def paint_stems(painter):
    left_stem = sample_curve(start=(350, 560), first_control=(380, 400), second_control=(470, 280), end=STEM_JOIN)
    right_stem = sample_curve(start=(680, 600), first_control=(660, 440), second_control=(620, 300), end=STEM_JOIN)
    painter.fill_curve(points=left_stem, width=STEM_WIDTH, shade=STEM)
    painter.fill_curve(points=right_stem, width=STEM_WIDTH, shade=STEM)


def paint_cherries(painter):
    for center, radius in CHERRIES:
        painter.fill_circle(center=center, radius=radius, shade=CHERRY)
        painter.fill_ellipse(
            center=(center[0] - 70, center[1] - 60),
            radius_x=36,
            radius_y=18,
            shade=SHINE,
            angle=-40,
        )


def paint_leaf(painter):
    painter.fill_ellipse(center=(680, 190), radius_x=120, radius_y=46, shade=LEAF, angle=-18)


def render_cherries_image():
    painter = FoodPainter()
    paint_stems(painter)
    paint_leaf(painter)
    paint_cherries(painter)
    painter.save_image(name="cherries")


if __name__ == "__main__":
    render_cherries_image()
