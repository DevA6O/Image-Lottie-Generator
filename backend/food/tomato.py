"""
Tomato image, drawn from scratch.
Output: tomato.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter, build_star_points

TOMATO = ((246, 84, 64), (188, 30, 36))
SHINE = ((255, 156, 140), (255, 140, 124))
CALYX = ((130, 205, 84), (70, 150, 52))


def paint_tomato(painter):
    tomato_mask = painter.build_rotated_ellipse_mask(center=(512, 570), radius_x=340, radius_y=290)
    painter.fill(mask=tomato_mask, shade=TOMATO)
    painter.fill_ellipse(center=(340, 500), radius_x=80, radius_y=34, shade=SHINE, angle=-40, clip=tomato_mask)


def paint_calyx(painter):
    leaf_points = build_star_points(center=(512, 330), outer_radius=190, inner_radius=60, tip_count=6, rotation=0)
    painter.fill_polygon(points=leaf_points, shade=CALYX)
    painter.fill_stroke(start=(512, 330), end=(530, 220), width=30, shade=CALYX)


def render_tomato_image():
    painter = FoodPainter()
    paint_tomato(painter)
    paint_calyx(painter)
    painter.save_image(name="tomato")


if __name__ == "__main__":
    render_tomato_image()
