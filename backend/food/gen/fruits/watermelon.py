"""
Watermelon slice image, drawn from scratch.
Output: watermelon.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

RIND = ((70, 160, 80), (34, 108, 56))
WHITE_RIND = ((226, 246, 200), (200, 232, 170))
FLESH = ((255, 96, 108), (222, 40, 76))
SEED = ((60, 40, 40), (30, 20, 24))

SLICE_CENTER_Y = 340
RIND_RADIUS = 420
WHITE_RIND_RADIUS = 385
FLESH_RADIUS = 350

# (x, y, angle): all inside the red flesh, tilted along the radius
SEEDS = [(400, 600, 25), (512, 640, 0), (624, 600, -25), (440, 480, 20), (584, 480, -20), (512, 520, 0), (330, 500, 45), (694, 500, -45)]


def build_half_disc_mask(
    painter,
    radius,
):
    disc_mask = painter.build_rotated_ellipse_mask(center=(512, SLICE_CENTER_Y), radius_x=radius, radius_y=radius)
    lower_half = painter.build_box_mask(left=0, top=SLICE_CENTER_Y, right=1024, bottom=1024)

    return painter.round_corners(mask=painter.intersect_masks(first_mask=disc_mask, second_mask=lower_half), radius=20)


def paint_slice(painter):
    painter.fill(mask=build_half_disc_mask(painter=painter, radius=RIND_RADIUS), shade=RIND)
    painter.fill(mask=build_half_disc_mask(painter=painter, radius=WHITE_RIND_RADIUS), shade=WHITE_RIND)
    painter.fill(mask=build_half_disc_mask(painter=painter, radius=FLESH_RADIUS), shade=FLESH)


def paint_seeds(painter):
    # The clip makes sure that no seed can ever reach into the rind
    flesh_mask = build_half_disc_mask(painter=painter, radius=FLESH_RADIUS)

    for x, y, angle in SEEDS:
        painter.fill_ellipse(center=(x, y), radius_x=14, radius_y=28, shade=SEED, angle=angle, clip=flesh_mask)


def render_watermelon_image():
    painter = FoodPainter()
    paint_slice(painter)
    paint_seeds(painter)
    painter.save_image(name="watermelon")


if __name__ == "__main__":
    render_watermelon_image()
