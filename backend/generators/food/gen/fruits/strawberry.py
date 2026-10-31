"""
Strawberry image, drawn from scratch.
Output: strawberry.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter
from painting.flat_painter import build_star_points

BERRY = ((246, 76, 88), (190, 30, 54))
SEED = ((255, 228, 120), (240, 196, 70))
LEAF = ((130, 205, 84), (70, 150, 52))

SEED_COLUMNS = [380, 470, 560, 650]
SEED_ROW_SPACING = 105


def build_berry_mask(painter):
    outline = painter.build_polygon_mask(points=[(190, 330), (834, 330), (512, 900)])

    return painter.round_corners(mask=outline, radius=110)


def paint_berry(painter):
    berry_mask = build_berry_mask(painter)
    painter.fill(mask=berry_mask, shade=BERRY)

    for row in range(5):
        for column_index, x in enumerate(SEED_COLUMNS):
            row_offset = 45 if row % 2 else 0
            center = (x - 25 + row_offset - row * 6, 440 + row * SEED_ROW_SPACING * 0.78)
            painter.fill_ellipse(center=center, radius_x=11, radius_y=18, shade=SEED, clip=berry_mask)


def paint_leaves(painter):
    leaf_points = build_star_points(center=(512, 340), outer_radius=230, inner_radius=70, tip_count=7)
    painter.fill_polygon(points=leaf_points, shade=LEAF)
    painter.fill_stroke(start=(512, 340), end=(540, 210), width=30, shade=LEAF)


def render_strawberry_image():
    painter = FoodPainter()
    paint_berry(painter)
    paint_leaves(painter)
    painter.save_image(name="strawberry")


if __name__ == "__main__":
    render_strawberry_image()
