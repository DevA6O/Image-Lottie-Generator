"""
Red mushroom with white dots, drawn from scratch.
Output: mushroom.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

CAP = ((240, 80, 70), (180, 30, 44))
STEM = ((255, 244, 224), (226, 200, 160))
DOT = ((255, 255, 255), (240, 236, 236))

CAP_BASE_Y = 520
DOTS = [((360, 400), 52), ((540, 300), 60), ((690, 420), 46), ((520, 450), 34), ((250, 480), 26)]


def paint_stem(painter):
    painter.fill_rounded_rect(box=(390, 470, 634, 850), radius=70, shade=STEM)


def paint_cap(painter):
    disc_mask = painter.build_rotated_ellipse_mask(center=(512, CAP_BASE_Y), radius_x=380, radius_y=290)
    upper_half = painter.build_box_mask(left=0, top=0, right=1024, bottom=CAP_BASE_Y)
    cap_mask = painter.round_corners(mask=painter.intersect_masks(first_mask=disc_mask, second_mask=upper_half), radius=24)
    painter.fill(mask=cap_mask, shade=CAP)

    for center, radius in DOTS:
        painter.fill_circle(center=center, radius=radius, shade=DOT, clip=cap_mask)


def render_mushroom_image():
    painter = FoodPainter()
    paint_stem(painter)
    paint_cap(painter)
    painter.save_image(name="mushroom")


if __name__ == "__main__":
    render_mushroom_image()
