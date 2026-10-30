"""
Burger image, drawn from scratch.
Output: burger.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

BUN = ((240, 172, 86), (204, 124, 52))
BOTTOM_BUN = ((228, 160, 80), (196, 120, 50))
PATTY = ((128, 70, 44), (84, 42, 28))
CHEESE = ((255, 222, 80), (246, 178, 36))
LETTUCE = ((150, 214, 84), (92, 168, 56))
TOMATO = ((238, 70, 56), (190, 40, 40))
SESAME = ((255, 244, 214), (240, 220, 170))

SESAME_SPOTS = [(380, 340, 20), (500, 290, 0), (630, 340, -20), (440, 420, 30), (580, 430, -30), (330, 450, 10), (690, 450, -10)]


def paint_bottom_layers(painter):
    painter.fill_rounded_rect(box=(220, 700, 804, 790), radius=44, shade=BOTTOM_BUN)
    painter.fill_rounded_rect(box=(195, 610, 829, 712), radius=50, shade=PATTY)


def paint_cheese_and_greens(painter):
    painter.fill_polygon(points=[(205, 585), (819, 585), (780, 640), (700, 650), (610, 700), (520, 650), (210, 640)], shade=CHEESE)

    for x in range(235, 800, 56):
        painter.fill_circle(center=(x, 560), radius=40, shade=LETTUCE)

    painter.fill_rounded_rect(box=(220, 505, 804, 570), radius=30, shade=TOMATO)


def paint_top_bun(painter):
    dome_mask = painter.build_rotated_ellipse_mask(center=(512, 520), radius_x=330, radius_y=290)
    top_half = painter.build_box_mask(left=0, top=0, right=1024, bottom=520)
    bun_mask = painter.round_corners(mask=painter.intersect_masks(first_mask=dome_mask, second_mask=top_half), radius=24)
    painter.fill(mask=bun_mask, shade=BUN)

    for x, y, angle in SESAME_SPOTS:
        painter.fill_ellipse(center=(x, y), radius_x=24, radius_y=12, shade=SESAME, angle=angle, clip=bun_mask)


def render_burger_image():
    painter = FoodPainter()
    paint_bottom_layers(painter)
    paint_cheese_and_greens(painter)
    paint_top_bun(painter)
    painter.save_image(name="burger")


if __name__ == "__main__":
    render_burger_image()
