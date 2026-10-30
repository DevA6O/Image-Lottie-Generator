"""
Sandwich half (cut diagonally), drawn from scratch.
Output: sandwich.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

BREAD = ((248, 216, 150), (226, 176, 96))
CRUST = ((196, 124, 56), (160, 92, 38))
HAM = ((252, 170, 170), (232, 128, 140))
CHEESE = ((255, 222, 80), (246, 178, 36))
LETTUCE = ((150, 214, 84), (92, 168, 56))
TOMATO = ((238, 70, 56), (190, 40, 40))

# (top_y, bottom_y, shade): bands from the bottom to the top of the triangle
BANDS = [(690, 790, BREAD), (630, 690, HAM), (590, 630, CHEESE), (540, 590, LETTUCE), (490, 540, TOMATO)]


def build_triangle_mask(
    painter,
    inset,
):
    outline = painter.build_polygon_mask(points=[(150 + inset, 800 - inset), (880 - inset * 2, 800 - inset), (150 + inset, 200 + inset * 2)])

    return painter.round_corners(mask=outline, radius=36)


def paint_sandwich(painter):
    painter.fill(mask=build_triangle_mask(painter=painter, inset=0), shade=CRUST)
    inner_mask = build_triangle_mask(painter=painter, inset=34)
    painter.fill(mask=inner_mask, shade=BREAD)

    for top, bottom, shade in BANDS:
        painter.fill(mask=painter.build_box_mask(left=0, top=top, right=1024, bottom=bottom), shade=shade, clip=inner_mask)


def render_sandwich_image():
    painter = FoodPainter()
    paint_sandwich(painter)
    painter.save_image(name="sandwich")


if __name__ == "__main__":
    render_sandwich_image()
